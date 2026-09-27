"""Downloads the public data of the NZip benchmark from the original sources and checks every file.

  python bench_data.py <cartella>        creates <cartella>/sorgenti, <cartella>/immagini, <cartella>/documenti
  python bench_data.py --hash <cartella> prints the SHA-256 list of the downloaded files (to fill SHA256 below)

Every download is verified with the SHA-256 recorded here: whoever repeats the benchmark gets the same bytes.

  sorgenti   CPython 3.13.7 source code, https://www.python.org/ftp/python/3.13.7/Python-3.13.7.tar.xz
             (Python Software Foundation License)
  immagini   Kodak Lossless True Color Image Suite, 24 PNG images, https://r0k.us/graphics/kodak/
             (released by Eastman Kodak for unrestricted use)
             + 40 original photos of the Apollo 11 mission, JPEG, NASA Image and Video Library
             https://images.nasa.gov (public domain, NASA media usage guidelines)
  backup     backup folder of a project: the official sources of three consecutive CPython releases,
             3.13.5, 3.13.6 and 3.13.7, side by side (same site and license as "sorgenti")
  documenti  Govdocs1, thread 000: 1,000 documents (PDF, Word, Excel, PowerPoint, HTML, text...) collected from
             U.S. government web sites, https://digitalcorpora.org/corpora/file-corpora/files/ (public domain,
             corpus created for research)
"""
import hashlib
import json
import os
import shutil
import sys
import tarfile
import urllib.request
import zipfile

PYTHON = 'https://www.python.org/ftp/python/3.13.7/Python-3.13.7.tar.xz'
BACKUP = [f'https://www.python.org/ftp/python/{v}/Python-{v}.tar.xz' for v in ('3.13.5', '3.13.6', '3.13.7')]
KODAK = [f'https://r0k.us/graphics/kodak/kodak/kodim{i:02d}.png' for i in range(1, 25)]
NASA_IDS = ['as11-36-5299', 'as11-36-5337', 'as11-36-5355', 'as11-36-5365', 'as11-36-5389', 'as11-36-5390',
            'as11-37-5445', 'as11-37-5448', 'as11-37-5505', 'as11-37-5528', 'as11-37-5545', 'as11-37-5551',
            'as11-40-5863', 'as11-40-5866', 'as11-40-5868', 'as11-40-5873', 'as11-40-5874', 'as11-40-5875',
            'as11-40-5878', 'as11-40-5880', 'as11-40-5881', 'as11-40-5899', 'as11-40-5902', 'as11-40-5903',
            'as11-40-5917', 'as11-40-5927', 'as11-40-5931', 'as11-40-5942', 'as11-40-5948', 'as11-40-5964',
            'as11-42-6179', 'as11-42-6237', 'as11-42-6248', 'as11-42-6285', 'as11-43-6412', 'as11-43-6422',
            'as11-43-6439', 'as11-44-6548', 'as11-44-6549', 'as11-44-6550']
NASA = [f'https://images-assets.nasa.gov/image/{i}/{i}~orig.jpg' for i in NASA_IDS]
GOVDOCS = 'https://downloads.digitalcorpora.org/corpora/files/govdocs1/zipfiles/000.zip'

HERE = os.path.dirname(os.path.abspath(__file__))
SHA256 = {}  # file name -> SHA-256 (bench_data.sha256.json next to this script)
_sums = os.path.join(HERE, 'bench_data.sha256.json')
if os.path.exists(_sums):
    SHA256 = json.load(open(_sums, encoding='utf-8'))


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def fetch(url, dest):
    name = os.path.basename(dest)
    if not os.path.exists(dest):
        print('scarico', url, flush=True)
        req = urllib.request.Request(url, headers={'User-Agent': 'NZip-benchmark/1.0'})
        with urllib.request.urlopen(req) as r, open(dest + '.part', 'wb') as f:
            shutil.copyfileobj(r, f, 1 << 20)
        os.replace(dest + '.part', dest)
    want = SHA256.get(name)
    if want and sha256(dest) != want:
        sys.exit(f'{name}: SHA-256 diverso da quello pubblicato (file cambiato alla fonte?)')
    return dest


def main():
    if sys.argv[1] == '--hash':
        root = os.path.join(sys.argv[2], '_download')
        sums = {f: sha256(os.path.join(root, f)) for f in sorted(os.listdir(root))}
        json.dump(sums, open(_sums, 'w', encoding='utf-8'), indent=1)
        print(f'{len(sums)} file -> {_sums}')
        return
    out = os.path.abspath(sys.argv[1])
    dl = os.path.join(out, '_download')
    os.makedirs(dl, exist_ok=True)
    # sources
    src = os.path.join(out, 'sorgenti')
    if not os.path.isdir(src):
        tarfile.open(fetch(PYTHON, os.path.join(dl, 'Python-3.13.7.tar.xz'))).extractall(src, filter='data')
    # backup of a project: three consecutive releases side by side
    bak = os.path.join(out, 'backup')
    if not os.path.isdir(bak):
        for url in BACKUP:
            tarfile.open(fetch(url, os.path.join(dl, os.path.basename(url)))).extractall(bak, filter='data')
    # images
    img = os.path.join(out, 'immagini')
    os.makedirs(img, exist_ok=True)
    for url in KODAK + NASA:
        name = os.path.basename(url).replace('~orig', '')
        path = fetch(url, os.path.join(dl, name))
        if not os.path.exists(os.path.join(img, name)):
            shutil.copy(path, os.path.join(img, name))
    # documents
    doc = os.path.join(out, 'documenti')
    if not os.path.isdir(doc):
        zipfile.ZipFile(fetch(GOVDOCS, os.path.join(dl, 'govdocs1-000.zip'))).extractall(doc)
    for name, folder in (('sorgenti', src), ('backup', bak), ('immagini', img), ('documenti', doc)):
        n = sum(len(f) for _, _, f in os.walk(folder))
        size = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(folder) for f in fs)
        print(f'{name}: {n} file, {size / 2**20:.1f} MB')
    print('Benchmark: python bench.py risultati.json', ' '.join(f'{n}={os.path.join(out, n)}' for n in ('sorgenti', 'backup', 'immagini', 'documenti')))


main()
