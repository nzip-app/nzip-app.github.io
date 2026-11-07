"""Comparative benchmark: NZip against tar, gzip, bzip2, xz, ZIP, 7-Zip, RAR and zstd on the same folders.

  python bench.py <risultati.json> nome=cartella [nome=cartella ...]
  python bench.py --meta <risultati.json>        adds versions, machine and commands to existing results

Anyone can repeat it (Windows 10/11, Python 3): programs are found in their usual places or given with
  NZIP_EXE   nzip.exe          (default: build\\bin\\nzip.exe, then %LOCALAPPDATA%\\Programs\\NZip\\nzip.exe)
  SEVENZIP   7z.exe            (default: C:\\Program Files\\7-Zip\\7z.exe)
  RAR_EXE    Rar.exe of WinRAR (optional)
  ZSTD_EXE   zstd.exe          (optional)
tar is the one of Windows (bsdtar). NZip Ultra needs an NZip Pro license, otherwise it is skipped.

Method: one run per program, all on the same computer, folders read once before (warm file cache for
everybody); archive size in bytes; times measured from start to end of the command (wall clock), indicative
because they depend on the computer. After every program the archive is
extracted and every file compared with the original (SHA-256): a result is published only if identical.
Each competitor uses its highest documented compression setting; NZip times include its own full
verification of the archive, which the other programs do not do.
"""
import glob
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def first(*paths):
    return next((p for p in paths if p and os.path.exists(p)), '')


NZ = first(os.environ.get('NZIP_EXE'), os.path.join(ROOT, 'build', 'bin', 'nzip.exe'),
           os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'NZip', 'nzip.exe'))
SZ = first(os.environ.get('SEVENZIP'), r'C:\Program Files\7-Zip\7z.exe')
TOOLS = os.environ.get('NZIP_BENCH_TOOLS', '')  # folder with winrar\Rar.exe and zstd-*\zstd.exe (portable)
RAR = first(os.environ.get('RAR_EXE'), os.path.join(TOOLS, 'winrar', 'Rar.exe'), r'C:\Program Files\WinRAR\Rar.exe')
ZSTD = first(os.environ.get('ZSTD_EXE'), *glob.glob(os.path.join(TOOLS, 'zstd*', 'zstd.exe')))
TAR = r'C:\Windows\System32\tar.exe'
WORK = os.path.join(tempfile.gettempdir(), f'nzip-bench-{os.getpid()}')

# key, label, extension, create command, extract command. Commands use {A} (archive), {F} (folder),
# {P} (parent of the folder), {N} (folder name), {D} (destination), {T} (archive without .gz/.bz2/.xz):
# the same templates are published on the web site.
PROGRAMS = [
    ('tar', 'tar (nessuna compressione)', 'tar', 'tar -cf {A} -C {P} {N}', 'tar -xf {A} -C {D}'),
    ('tgz', 'tar.gz (gzip, massima)', 'tar.gz', 'tar -cf {T} -C {P} {N} && 7z a -tgzip -mx9 {A} {T}', '7z x -o{D} {A} && tar -xf {D}\\a.tar -C {D}'),
    ('tbz', 'tar.bz2 (bzip2, massima)', 'tar.bz2', 'tar -cf {T} -C {P} {N} && 7z a -tbzip2 -mx9 {A} {T}', '7z x -o{D} {A} && tar -xf {D}\\a.tar -C {D}'),
    ('txz', 'tar.xz (xz, massima)', 'tar.xz', 'tar -cf {T} -C {P} {N} && 7z a -txz -mx9 {A} {T}', '7z x -o{D} {A} && tar -xf {D}\\a.tar -C {D}'),
    ('zip', 'ZIP (Deflate, massima)', 'zip', '7z a -tzip -mx9 {A} {F}', '7z x -o{D} {A}'),
    ('7z5', '7-Zip normale', '7z', '7z a -t7z -mx5 {A} {F}', '7z x -o{D} {A}'),
    ('7z9', '7-Zip ultra', '7z', '7z a -t7z -mx9 {A} {F}', '7z x -o{D} {A}'),
    ('rar', 'RAR 7 (migliore, solido)', 'rar', 'rar a -r -m5 -ma5 -s -ep1 {A} {F}', 'rar x {A} {D}\\'),
    ('zst', 'tar.zst (zstd -19, long)', 'tar.zst', 'tar -cf - -C {P} {N} | zstd -19 --long=31 -T0 -o {A}', 'zstd -d -c --long=31 {A} | tar -xf - -C {D}'),
    ('nz1', 'NZip veloce', 'nzip', 'nzip a -m1 {A} {F}', 'nzip x {A} -o{D}'),
    ('nz2', 'NZip normale', 'nzip', 'nzip a -m2 {A} {F}', 'nzip x {A} -o{D}'),
    ('nz3', 'NZip massima', 'nzip', 'nzip a -m3 {A} {F}', 'nzip x {A} -o{D}'),
    ('nz4', 'NZip ultra (Pro)', 'nzip', 'nzip a -m4 {A} {F}', 'nzip x {A} -o{D}'),
]
EXE = {'tar': TAR, '7z': SZ, 'rar': RAR, 'zstd': ZSTD, 'nzip': NZ}
QUIET = {'7z': ' -bso0 -bsp0 -y', 'rar': ' -idq -y', 'zstd': ' -q', 'nzip': ' -q'}


def command(template, a, f, d):
    """Turns a published template into the real command line (full paths, quiet options)."""
    v = {'A': a, 'F': f, 'P': os.path.dirname(f), 'N': os.path.basename(f), 'D': d, 'T': re.sub(r'\.(gz|bz2|xz)$', '', a)}
    parts = []
    for piece in re.split(r'( && | \| )', template):
        if piece in (' && ', ' | '):
            parts.append(piece)
            continue
        words = piece.split(' ')
        prog = words[0]
        args = []
        for w in words[1:]:
            m = re.fullmatch(r'(-o)?\{(\w)\}(\\a\.tar|\\)?', w)
            args.append((m.group(1) or '') + f'"{v[m.group(2)]}{m.group(3) or ""}"' if m else w)
        opts = QUIET.get(prog, '')
        cmdline = f'"{EXE[prog]}"' + (' ' + args[0] if prog in ('7z', 'rar', 'nzip') else '') + opts + ' ' + ' '.join(args[1:] if prog in ('7z', 'rar', 'nzip') else args)
        parts.append(cmdline)
    s = ''.join(parts)
    if template.startswith('tar -x') or template.startswith('zstd -d'):
        s = f'mkdir "{d}" && ' + s
    if 'tar -cf {T}' in template:
        s += f' && del "{v["T"]}"'
    return s


def remove(path):
    # files just written may stay locked for a moment (antivirus scan): retry, then leave them
    for _ in range(20):
        shutil.rmtree(path, ignore_errors=True)
        if not os.path.exists(path):
            return
        time.sleep(0.5)


def tree(folder):
    out, total, n = {}, 0, 0
    for dp, _, files in os.walk(folder):
        for f in files:
            p = os.path.join(dp, f)
            h = hashlib.sha256()
            with open(p, 'rb') as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b''):
                    h.update(chunk)
            out[os.path.relpath(p, folder).replace('\\', '/')] = h.hexdigest()
            total += os.path.getsize(p)
            n += 1
    return out, total, n


def timed(cmd):
    t = time.perf_counter()
    r = subprocess.run(cmd, capture_output=True, text=True, errors='replace', shell=True)
    return r.returncode, time.perf_counter() - t, (r.stderr or r.stdout)[-500:]


def first_line(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, errors='replace').stdout
        return next((l.strip() for l in out.splitlines() if l.strip()), '')
    except OSError:
        return ''


def meta():
    tools = {
        'nzip': first_line([NZ]) if NZ else '',
        '7-zip': next((l for l in subprocess.run([SZ], capture_output=True, text=True).stdout.splitlines() if l.startswith('7-Zip')), '') if SZ else '',
        'rar': next((l.strip() for l in subprocess.run([RAR], capture_output=True, text=True).stdout.splitlines() if l.strip().startswith('RAR')), '') if RAR else '',
        'zstd': first_line([ZSTD, '--version']).strip('* ') if ZSTD else '',
        'tar': first_line([TAR, '--version']),
    }
    commands = [{'key': k, 'label': l, 'create': c, 'extract': x} for k, l, _, c, x in PROGRAMS]
    return {'tools': tools, 'commands': commands}


def main():
    if sys.argv[1] == '--meta':
        path = sys.argv[2]
        r = json.load(open(path, encoding='utf-8'))
        r.update(meta())
        json.dump(r, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(json.dumps(meta(), ensure_ascii=False, indent=1))
        return
    if not NZ or not SZ:
        sys.exit('Servono nzip.exe e 7z.exe (vedi NZIP_EXE, SEVENZIP)')
    out_json = sys.argv[1]
    sets = [a.split('=', 1) for a in sys.argv[2:]]
    result = {'date': time.strftime('%Y-%m-%d'), 'sets': []}
    result.update(meta())
    for name, folder in sets:
        folder = os.path.abspath(folder)
        ref, total, nfiles = tree(folder)
        entry = {'name': name, 'bytes': total, 'files': nfiles, 'results': []}
        print(f'== {name}: {nfiles} file, {total / 2**20:.0f} MB', flush=True)
        for key, label, ext, create, extract in PROGRAMS:
            if (key == 'rar' and not RAR) or (key == 'zst' and not ZSTD):
                continue
            only = os.environ.get('NZIP_BENCH_SOLO', '')  # e.g. "nz1,nz2,nz3,nz4": only these programs
            if only and key not in only.split(','):
                continue
            work = os.path.join(WORK, f'{len(result["sets"])}-{key}')
            os.makedirs(work, exist_ok=True)
            arc = os.path.join(work, 'a.' + ext)
            dest = os.path.join(work, 'x')
            code, tc, err = timed(command(create, arc, folder, dest))
            if code not in (0, 1) or not os.path.exists(arc):
                print(f'   {label}: saltato ({err.strip()[:120]})', flush=True)
                remove(work)
                continue
            size = os.path.getsize(arc)
            code, tx, err = timed(command(extract, arc, folder, dest))
            got, _, _ = tree(os.path.join(dest, os.path.basename(folder)))
            ok = got == ref  # every program: extraction compared file by file
            entry['results'].append({'key': key, 'label': label, 'bytes': size, 'compress_s': round(tc, 1),
                                     'extract_s': round(tx, 1), 'identical': ok})
            remove(work)
            print(f'   {label:26} {size / 2**20:9.1f} MB  {tc:6.1f} s  {tx:6.1f} s  {"OK" if ok else "DIVERSO!"}', flush=True)
        result['sets'].append(entry)
        with open(out_json, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=1)
    remove(WORK)


main()
