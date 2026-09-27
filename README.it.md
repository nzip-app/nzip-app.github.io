<p align="center"><img src="img/nzip-256.png" width="112" alt="NZip"></p>

<h1 align="center">NZip</h1>

<p align="center"><b>Archivi più piccoli, verificati e riparabili — per Windows, macOS e Linux.</b></p>

<p align="center"><a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest"><img alt="release" src="https://img.shields.io/github/v/release/nzip-app/nzip-app.github.io?label=NZip&color=7c5cf6"></a> <a href="https://github.com/nzip-app/nzip-app.github.io/releases"><img alt="downloads" src="https://img.shields.io/github/downloads/nzip-app/nzip-app.github.io/total?color=3b82f6"></a> <img alt="platforms" src="https://img.shields.io/badge/Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-555"> <img alt="license" src="https://img.shields.io/badge/license-freeware-2ea44f"> <a href="https://paypal.me/cavallomarcoapp"><img alt="coffee" src="https://img.shields.io/badge/%E2%98%95-PayPal-f59e0b"></a></p>

<p align="center"><a href="README.md">English</a> · <b>Italiano</b> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>

<p align="center"><a href="https://nzip-app.github.io/it/"><b>Sito</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe"><b>Scarica per Windows</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest">Ultima versione: 3.2.7</a></p>

---

NZip è un compressore di file moderno. Crea archivi .nzip più piccoli di quelli di 7-Zip e RAR, rilegge e verifica ogni file prima di dichiarare conclusa l'operazione e apre anche gli archivi degli altri programmi: ZIP, RAR, 7z, TAR, ISO e molti altri. L'edizione base è gratuita per tutti, anche per l'uso aziendale.

## In breve

- **Più piccoli**: pixel delle immagini PNG in JPEG XL senza perdite, ricompressione senza perdite di JPEG, ZIP e documenti Office, compressori moderni scelti per ogni tipo di dato.
- **Verificati**: ogni file è confrontato con l'originale (BLAKE3) prima di chiudere l'archivio e di nuovo durante l'estrazione.
- **Riparabili**: i dati di ripristino permettono di recuperare archivi danneggiati.
- **Sicuri**: cifratura AES-256 di contenuto e nomi; con NZip Pro anche firma digitale e cifratura per destinatari.
- **Compatibili**: legge ed estrae ZIP, RAR, 7z, TAR, GZ, BZ2, XZ, ZSTD, LZH, ARJ, CAB, ISO, WIM e li converte in .nzip.
- **Integrati**: menu di Esplora file (Windows 11 e 10), Finder, Dolphin, Nautilus e Nemo; 7 lingue.

## Benchmark

Dimensione degli archivi ottenuti sulle stesse cartelle, sullo stesso PC. Ogni archivio è stato estratto e confrontato byte per byte con l'originale.

**Documenti** · 723,6 MB — 981 documenti reali: PDF, Word, Excel, PowerPoint, HTML (Govdocs1)

| Programma | Dimensione | rispetto a 7-Zip ultra |
|---|---:|---:|
| ZIP (massima) | 454,5 MB | +9,0% |
| RAR 7 (migliore, solido) | 431,3 MB | +3,4% |
| tar.xz (xz, massima) | 416,9 MB | −0,0% |
| tar.zst (zstd 19, long) | 396,6 MB | −4,9% |
| 7-Zip ultra | 417,0 MB | — |
| **NZip normale** | 328,2 MB | **−21,3%** |
| **NZip massima** | 324,1 MB | **−22,3%** |

**Immagini** · 147,6 MB — 24 PNG della Kodak Image Suite e 40 foto JPEG originali NASA

| Programma | Dimensione | rispetto a 7-Zip ultra |
|---|---:|---:|
| ZIP (massima) | 145,7 MB | +0,4% |
| RAR 7 (migliore, solido) | 145,9 MB | +0,5% |
| tar.xz (xz, massima) | 145,1 MB | +0,0% |
| tar.zst (zstd 19, long) | 145,1 MB | −0,0% |
| 7-Zip ultra | 145,1 MB | — |
| **NZip normale** | 114,9 MB | **−20,8%** |
| **NZip massima** | 114,2 MB | **−21,3%** |

**Backup di sorgenti** · 303,8 MB — cartella di backup di un progetto: 3 versioni consecutive dei sorgenti di Python (3.13.5, 3.13.6, 3.13.7)

| Programma | Dimensione | rispetto a 7-Zip ultra |
|---|---:|---:|
| ZIP (massima) | 87,9 MB | +173,4% |
| RAR 7 (migliore, solido) | 25,9 MB | −19,4% |
| tar.xz (xz, massima) | 33,7 MB | +4,8% |
| tar.zst (zstd 19, long) | 22,9 MB | −28,8% |
| 7-Zip ultra | 32,1 MB | — |
| **NZip normale** | 21,2 MB | **−34,2%** |
| **NZip massima** | 20,6 MB | **−35,8%** |

**Codice sorgente** · 101,3 MB — sorgenti ufficiali di Python 3.13.7 (testo, C e Python)

| Programma | Dimensione | rispetto a 7-Zip ultra |
|---|---:|---:|
| ZIP (massima) | 29,3 MB | +39,3% |
| RAR 7 (migliore, solido) | 23,4 MB | +11,2% |
| tar.xz (xz, massima) | 21,1 MB | +0,4% |
| tar.zst (zstd 19, long) | 21,7 MB | +3,4% |
| 7-Zip ultra | 21,0 MB | — |
| **NZip normale** | 20,7 MB | **−1,6%** |
| **NZip massima** | 20,3 MB | **−3,6%** |

<sub>I tempi di NZip comprendono la verifica completa dell'archivio, che gli altri programmi non eseguono. Le percentuali verdi e rosse sono rispetto a 7-Zip ultra.</sub>

[Tutti i dettagli, i tempi e gli altri formati sul sito.](https://nzip-app.github.io/it/#benchmark)

## Download

| Piattaforma | File |
|---|---|
| Windows 10 e 11 (64 bit) — Programma di installazione | [NZip-Setup.exe](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe) |
| Windows 10 e 11 (64 bit) — Pacchetto MSI | [NZip.msi](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip.msi) |
| Modelli ADMX dei criteri aziendali | [NZip-ADMX.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-ADMX.zip) |
| macOS — Apple Silicon | [NZip-macos-arm64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-arm64.zip) |
| macOS — Intel | [NZip-macos-x64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-x64.zip) |
| Linux — x86-64 | [NZip-linux-x64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-x64.tar.gz) |
| Linux — ARM64 | [NZip-linux-arm64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-arm64.tar.gz) |

Le versioni per macOS e Linux sono in anteprima. Verifica l'integrità dei file scaricati con [SHA256SUMS.txt](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/SHA256SUMS.txt).

## Requisiti

- Windows 10 o 11 a 64 bit (x64)
- macOS 13 o successivo (Apple Silicon o Intel) — anteprima
- Linux x86-64 o ARM64 con glibc 2.28 o successiva — anteprima

## Edizioni

- **NZip** — gratuito per tutti, privati e aziende, per qualsiasi uso.
- **NZip Pro** — licenza personale: compressione Ultra, archivi divisi e autoestraenti, firma digitale, backup pianificati, ricerca negli archivi, copia su cloud.
- **NZip Enterprise** — licenza aziendale per postazioni: criteri aziendali, chiave di recupero, registro attività, MSI, SDK.

**NZip Pro · NZip Enterprise** — Come ottenerla: apri NZip → Impostazioni → Passa a Pro o Enterprise, inserisci i tuoi dati e invia la richiesta. Riceverai la chiave di licenza da incollare nell'app: si attiva subito, anche senza internet.

La versione base è gratuita per sempre. Pro ed Enterprise si richiedono direttamente dall'app.

## ☕ Sostieni NZip

NZip è gratuito per tutti e lo resterà. Se ti fa risparmiare tempo e spazio, offrimi un caffè: anche un piccolo contributo su PayPal fa la differenza. Grazie!

<p><a href="https://paypal.me/cavallomarcoapp"><img alt="Offrimi un caffè" src="https://img.shields.io/badge/%E2%98%95%20Offrimi%20un%20caffè-PayPal-f59e0b?logo=paypal&logoColor=white&style=for-the-badge"></a></p>

## Licenza

NZip è software proprietario, distribuito gratuitamente nell'edizione base. L'uso è regolato dal **Contratto di licenza con l'utente finale (EULA)**, mostrato e accettato durante l'installazione. Il codice sorgente non è pubblico; il formato .nzip è documentato apertamente.

- 📦 [Licenze dei componenti di terze parti](legal/TERZE-PARTI.txt)
- Il motore di 7-Zip (7z.dll), usato solo per leggere gli archivi di altri programmi, è distribuito con licenza GNU LGPL con la restrizione unRAR; i testi completi sono inclusi nel programma. [7-Zip-26.02-src.7z](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/7-Zip-26.02-src.7z)

## Documentazione

- [Specifica del formato .nzip](docs/NZIP-FORMAT.md)
- [SDK per sviluppatori](docs/SDK.md)
- [Note di rilascio](https://github.com/nzip-app/nzip-app.github.io/releases)

## Segnalazioni

Hai trovato un problema o hai un suggerimento? Apri una segnalazione nella sezione [Issues](https://github.com/nzip-app/nzip-app.github.io/issues) di questo repository. Oppure scrivi al supporto dal sito: [contatta il supporto](https://nzip-app.github.io/it/).

---

<sub>© 2026 Marco Cavallo. Tutti i diritti riservati. NZip, il nome e il logo NZip sono di Marco Cavallo, ideatore e autore del programma.</sub>
