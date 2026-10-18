# NZip SDK

La libreria **nzipcore** (`nzipcore.dll` su Windows, `libnzipcore.so` su Linux, `libnzipcore.dylib` su macOS)
espone il motore di NZip con un'API C stabile: è la stessa usata dall'app NZip e dall'integrazione con
Esplora file. Header: [`src/core/api/nzip_api.h`](../src/core/api/nzip_api.h).

## File da distribuire con il proprio programma

| File | Serve per |
|---|---|
| `nzipcore.dll` | tutto (creare, leggere, verificare, estrarre, riparare archivi .nzip) |
| `7z.dll` (facoltativo) | leggere gli archivi di altri programmi: RAR, ZIP, 7z, TAR, ISO... (licenza LGPL + unRAR, allegare i due testi) |
| `nzip-sfx.exe` (facoltativo) | creare archivi autoestraenti (opzione `sfx`) |

I tre file vanno nella stessa cartella. L'uso dell'SDK in prodotti distribuiti a terzi è regolato dal
contratto di licenza di NZip (sezione Enterprise). Le funzioni Pro (vedi sotto) richiedono una licenza
NZip Pro o Enterprise installata sul computer in cui girano.

## Convenzioni

- Tutte le stringhe sono **UTF-8**; i percorsi possono contenere qualsiasi carattere.
- Le funzioni restituiscono `0` = riuscita, `1` = completata con avvisi, `2` = errore (messaggio in `err`),
  `255` = annullata dalla funzione di avanzamento.
- La funzione di avanzamento `nz_progress_cb` riceve byte elaborati e totali (una chiamata con totale 0 e
  file `@fase:compressione`, `@fase:verifica` o `@fase:ripristino` annuncia una nuova fase, che riparte da 0);
  restituire un valore
  diverso da zero annulla l'operazione.
- I messaggi sono nella lingua impostata con `nz_set_language("it" | "en" | "es" | "fr" | "de" | "ru" | "zh")`.
- Le funzioni che scrivono testo in un buffer (`out`, `len`) restituiscono la lunghezza necessaria: se è
  maggiore o uguale a `len`, richiamarle con un buffer più grande.
- Un `nz_archive*` può essere usato da un solo thread alla volta.

## Funzioni principali

| Funzione | Descrizione |
|---|---|
| `nz_create_ex(inputs, n, output, opzioni_json, cb, user, stats, err, len)` | crea un archivio (vedi opzioni) |
| `nz_open_pw(path, password, &status, err, len)` | apre un archivio .nzip (anche diviso in parti, autoestraente, firmato) o di un altro programma; `status`: 0 ok, 1 serve la password, 2 password errata |
| `nz_entry_count` / `nz_entry_get` | elenco del contenuto |
| `nz_extract(a, dest, indici, n, prefisso, sovrascrivi, cb, user, stats, err, len)` | estrae tutto o una selezione; ogni file viene verificato con BLAKE3 |
| `nz_test` | verifica completa senza scrivere nulla |
| `nz_update` | aggiunge, sostituisce o elimina file in un archivio esistente |
| `nz_update_named` | aggiunge file dando loro un altro nome nell'archivio (es. «nome (2).txt» per tenerli entrambi) |
| `nz_rename` | rinomina un file o una cartella dell'archivio, senza ricomprimere |
| `nz_repair(path, output, err, len)` | ripara un archivio danneggiato con i dati di ripristino |
| `nz_convert(a, output, livello, ripristino, ...)` | converte in .nzip un archivio di un altro programma |
| `nz_join(prima_parte, output, err, len)` | riunisce un archivio diviso in parti |
| `nz_signature(path, out, len)` | firma digitale: JSON `{presente, valida, nome, impronta, ora, fidata, conosciuto, problema}` |
| `nz_sign(path, identita, err, len)` | firma un archivio esistente (Pro) |
| `nz_identities`, `nz_identity_create`, `nz_identity_import`, `nz_identity_remove` | identità per firme e cifratura per destinatari |
| `nz_archive_recipients(a, out, len)` | chi può aprire un archivio cifrato (`password;Mario Rossi;...`) |
| `nz_license_status`, `nz_license_pro` | edizione in uso |
| `nz_policies(out, len)` | criteri aziendali in vigore (Enterprise) |

### Opzioni di `nz_create_ex`

Oggetto JSON piatto, tutte le chiavi sono facoltative:

| Chiave | Valore | Edizione |
|---|---|---|
| `livello` | 0 solo archiviazione, 1 veloce, 2 normale (predefinito), 3 massima, 4 ultra | 4 = Pro |
| `ripristino` | % di dati di ripristino (1 gratuito, fino a 100) | oltre 1 = Pro |
| `password` | cifratura AES-256 di contenuto e nomi | |
| `destinatari` | `"Mario Rossi;NZID1...."`: cifratura per identità, senza password | Pro |
| `firma` | nome di una propria identità (`"*"` = la prima) | Pro |
| `parti` | dimensione di ogni parte in byte (archivio diviso `.nzip.001`, `.002`...) | Pro |
| `sfx` | 1 = eseguibile autoestraente (serve `nzip-sfx.exe`) | Pro |
| `esclusioni` | `"node_modules;*.tmp;bin"` | Pro |
| `thread` | numero di CPU da usare (0 = tutte) | Pro |
| `memoria_mb` | limite di memoria | Pro |
| `priorita_bassa` | 1 = il computer resta reattivo | Pro |
| `verifica`, `trasformazioni`, `compressione_extra` | 0/1 (predefinito 1) | |

## Esempio in C

[`samples/c/esempio.c`](../samples/c/esempio.c) crea un archivio, lo elenca, lo verifica e lo estrae.
Nel progetto è il target CMake `nzip_sdk_esempio`; fuori dal progetto:

```
cl /I<NZip>\include esempio.c nzipcore.lib            (Windows, Visual Studio)
cc -I<NZip>/include esempio.c -L. -lnzipcore          (Linux, macOS)
```

## Esempio in C#

```csharp
using System.Runtime.InteropServices;
using System.Text;

static class NZip {
    [DllImport("nzipcore", CallingConvention = CallingConvention.StdCall)]
    public static extern int nz_create_ex(byte[][] inputs, int count, byte[] output, byte[] options,
        IntPtr cb, IntPtr user, IntPtr stats, byte[] err, int errLen);

    static byte[] U8(string s) => Encoding.UTF8.GetBytes(s + "\0");

    public static void Comprimi(string cartella, string archivio) {
        var err = new byte[1024];
        int r = nz_create_ex(new[] { U8(cartella) }, 1, U8(archivio), U8("{\"livello\":3}"),
                             IntPtr.Zero, IntPtr.Zero, IntPtr.Zero, err, err.Length);
        if (r >= 2) throw new Exception(Encoding.UTF8.GetString(err).TrimEnd('\0'));
    }
}
```

L'app NZip ([`src/app/NZip/Native.cs`](../src/app/NZip/Native.cs)) è un esempio completo di uso da .NET.

## Esempio in Python

```python
import ctypes, json
nz = ctypes.CDLL('nzipcore.dll')          # 'libnzipcore.so' / 'libnzipcore.dylib'
err = ctypes.create_string_buffer(1024)
inputs = (ctypes.c_char_p * 1)(b'C:/Documenti')
r = nz.nz_create_ex(inputs, 1, b'C:/backup/documenti.nzip', json.dumps({'livello': 3}).encode(),
                    None, None, None, err, 1024)
if r >= 2:
    raise RuntimeError(err.value.decode())
out = ctypes.create_string_buffer(4096)
nz.nz_signature(b'C:/backup/documenti.nzip', out, 4096)
print(json.loads(out.value))
```

## Riga di comando

Per script e automazioni spesso basta `nzip` (stesse funzioni, codici di uscita 0/1/2):
`nzip a`, `x`, `t`, `l`, `i`, `r`, `c`, `unisci`, `firma`, `verifica-firma`, `identita`, `backup`, `cerca`,
`lotto`, `sigilla`, `carica`, `criteri`. `nzip` senza argomenti mostra la guida.
