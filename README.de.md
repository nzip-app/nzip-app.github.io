<p align="center"><img src="img/nzip-256.png" width="112" alt="NZip"></p>

<h1 align="center">NZip</h1>

<p align="center"><b>Kleinere, geprüfte und reparierbare Archive — für Windows, macOS und Linux.</b></p>

<p align="center"><a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest"><img alt="release" src="https://img.shields.io/github/v/release/nzip-app/nzip-app.github.io?label=NZip&color=7c5cf6"></a> <a href="https://github.com/nzip-app/nzip-app.github.io/releases"><img alt="downloads" src="https://img.shields.io/github/downloads/nzip-app/nzip-app.github.io/total?color=3b82f6"></a> <img alt="platforms" src="https://img.shields.io/badge/Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-555"> <img alt="license" src="https://img.shields.io/badge/license-freeware-2ea44f"> <a href="https://paypal.me/cavallomarcoapp"><img alt="coffee" src="https://img.shields.io/badge/%E2%98%95-PayPal-f59e0b"></a></p>

<p align="center"><a href="README.md">English</a> · <a href="README.it.md">Italiano</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <b>Deutsch</b> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>

<p align="center"><a href="https://nzip-app.github.io/de/"><b>Website</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe"><b>Download für Windows</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest">Neueste Version: 3.2.7</a></p>

---

NZip ist ein modernes Komprimierungsprogramm. Es erstellt .nzip-Archive, die kleiner sind als die von 7-Zip und RAR, liest jede Datei erneut ein und prüft sie, bevor ein Vorgang als abgeschlossen gilt, und öffnet auch die Archive anderer Programme: ZIP, RAR, 7z, TAR, ISO und viele weitere. Die Basisversion ist für alle kostenlos, auch für die geschäftliche Nutzung.

## Auf einen Blick

- **Kleiner**: PNG-Pixel als verlustfreies JPEG XL, verlustfreie Rekompression von JPEG, ZIP und Office-Dokumenten, moderne Kompressoren passend zu jedem Datentyp.
- **Geprüft**: Jede Datei wird vor dem Abschließen des Archivs und erneut beim Entpacken mit dem Original verglichen (BLAKE3).
- **Reparierbar**: Wiederherstellungsdaten ermöglichen die Rettung beschädigter Archive.
- **Sicher**: AES-256-Verschlüsselung von Inhalt und Dateinamen; mit NZip Pro zusätzlich digitale Signatur und Verschlüsselung für Empfänger.
- **Kompatibel**: Liest und entpackt ZIP, RAR, 7z, TAR, GZ, BZ2, XZ, ZSTD, LZH, ARJ, CAB, ISO und WIM und wandelt sie in .nzip um.
- **Integriert**: Menüs im Datei-Explorer (Windows 11 und 10), Finder, Dolphin, Nautilus und Nemo; 7 Sprachen.

## Benchmarks

Größe der Archive, die aus denselben Ordnern auf demselben PC erstellt wurden. Jedes Archiv wurde entpackt und Byte für Byte mit dem Original verglichen.

**Dokumente** · 723,6 MB — 981 echte Dokumente: PDF, Word, Excel, PowerPoint, HTML (Govdocs1)

| Programm | Größe | im Vergleich zu 7-Zip Ultra |
|---|---:|---:|
| ZIP (Maximum) | 454,5 MB | +9,0% |
| RAR 7 (beste, solid) | 431,3 MB | +3,4% |
| tar.xz (xz, Maximum) | 416,9 MB | −0,0% |
| tar.zst (zstd 19, long) | 396,6 MB | −4,9% |
| 7-Zip Ultra | 417,0 MB | — |
| **NZip Normal** | 328,2 MB | **−21,3%** |
| **NZip Maximum** | 324,1 MB | **−22,3%** |

**Bilder** · 147,6 MB — 24 PNGs aus der Kodak Image Suite und 40 originale JPEG-Fotos der NASA

| Programm | Größe | im Vergleich zu 7-Zip Ultra |
|---|---:|---:|
| ZIP (Maximum) | 145,7 MB | +0,4% |
| RAR 7 (beste, solid) | 145,9 MB | +0,5% |
| tar.xz (xz, Maximum) | 145,1 MB | +0,0% |
| tar.zst (zstd 19, long) | 145,1 MB | −0,0% |
| 7-Zip Ultra | 145,1 MB | — |
| **NZip Normal** | 114,9 MB | **−20,8%** |
| **NZip Maximum** | 114,2 MB | **−21,3%** |

**Quellcode-Sicherungen** · 303,8 MB — Sicherungsordner eines Projekts: 3 aufeinanderfolgende Versionen des Python-Quellcodes (3.13.5, 3.13.6, 3.13.7)

| Programm | Größe | im Vergleich zu 7-Zip Ultra |
|---|---:|---:|
| ZIP (Maximum) | 87,9 MB | +173,4% |
| RAR 7 (beste, solid) | 25,9 MB | −19,4% |
| tar.xz (xz, Maximum) | 33,7 MB | +4,8% |
| tar.zst (zstd 19, long) | 22,9 MB | −28,8% |
| 7-Zip Ultra | 32,1 MB | — |
| **NZip Normal** | 21,2 MB | **−34,2%** |
| **NZip Maximum** | 20,6 MB | **−35,8%** |

**Quellcode** · 101,3 MB — offizielle Quellen von Python 3.13.7 (Text, C und Python)

| Programm | Größe | im Vergleich zu 7-Zip Ultra |
|---|---:|---:|
| ZIP (Maximum) | 29,3 MB | +39,3% |
| RAR 7 (beste, solid) | 23,4 MB | +11,2% |
| tar.xz (xz, Maximum) | 21,1 MB | +0,4% |
| tar.zst (zstd 19, long) | 21,7 MB | +3,4% |
| 7-Zip Ultra | 21,0 MB | — |
| **NZip Normal** | 20,7 MB | **−1,6%** |
| **NZip Maximum** | 20,3 MB | **−3,6%** |

<sub>Die Zeiten von NZip enthalten die vollständige Prüfung des Archivs, die andere Programme nicht durchführen. Grüne und rote Prozentwerte beziehen sich auf 7-Zip Ultra.</sub>

[Alle Details, Zeiten und weitere Formate finden Sie auf der Website.](https://nzip-app.github.io/de/#benchmark)

## Download

| Plattform | Datei |
|---|---|
| Windows 10 und 11 (64 Bit) — Installationsprogramm | [NZip-Setup.exe](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe) |
| Windows 10 und 11 (64 Bit) — MSI-Paket | [NZip.msi](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip.msi) |
| ADMX-Vorlagen für Unternehmensrichtlinien | [NZip-ADMX.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-ADMX.zip) |
| macOS — Apple Silicon | [NZip-macos-arm64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-arm64.zip) |
| macOS — Intel | [NZip-macos-x64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-x64.zip) |
| Linux — x86-64 | [NZip-linux-x64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-x64.tar.gz) |
| Linux — ARM64 | [NZip-linux-arm64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-arm64.tar.gz) |

Die Versionen für macOS und Linux befinden sich in der Vorschau. Prüfen Sie die Integrität der heruntergeladenen Dateien mit [SHA256SUMS.txt](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/SHA256SUMS.txt).

## Systemvoraussetzungen

- Windows 10 oder 11, 64 Bit (x64)
- macOS 13 oder neuer (Apple Silicon oder Intel) — Vorschau
- Linux x86-64 oder ARM64 mit glibc 2.28 oder neuer — Vorschau

## Editionen

- **NZip** — kostenlos für alle, Privatpersonen und Unternehmen, für jeden Zweck.
- **NZip Pro** — persönliche Lizenz: Ultra-Kompression, geteilte und selbstentpackende Archive, digitale Signatur, geplante Backups, Suche in Archiven, Kopie in die Cloud.
- **NZip Enterprise** — Unternehmenslizenz pro Arbeitsplatz: Unternehmensrichtlinien, Wiederherstellungsschlüssel, Aktivitätsprotokoll, MSI, SDK.

**NZip Pro · NZip Enterprise** — So erhalten Sie sie: Öffnen Sie NZip → Einstellungen → Zu Pro oder Enterprise wechseln, geben Sie Ihre Daten ein und senden Sie die Anfrage. Sie erhalten einen Lizenzschlüssel, den Sie in der App einfügen: Er ist sofort aktiv, auch offline.

Die Basisversion ist für immer kostenlos. Pro und Enterprise werden direkt in der App beantragt.

## ☕ NZip unterstützen

NZip ist für alle kostenlos und bleibt es. Wenn es Ihnen Zeit und Speicherplatz spart, spendieren Sie mir einen Kaffee: Schon ein kleiner Beitrag über PayPal hilft. Vielen Dank!

<p><a href="https://paypal.me/cavallomarcoapp"><img alt="Spendieren Sie mir einen Kaffee" src="https://img.shields.io/badge/%E2%98%95%20Spendieren%20Sie%20mir%20einen%20Kaffee-PayPal-f59e0b?logo=paypal&logoColor=white&style=for-the-badge"></a></p>

## Lizenz

NZip ist proprietäre Software, deren Basisversion kostenlos vertrieben wird. Die Nutzung unterliegt dem **Endbenutzer-Lizenzvertrag (EULA)**, der während der Installation angezeigt und akzeptiert wird. Der Quellcode ist nicht öffentlich; das .nzip-Format ist offen dokumentiert.

- 📦 [Lizenzen von Drittanbieterkomponenten](legal/TERZE-PARTI.txt)
- Die 7-Zip-Engine (7z.dll), die ausschließlich zum Lesen der Archive anderer Programme verwendet wird, wird unter der GNU LGPL mit der unRAR-Einschränkung vertrieben; die vollständigen Lizenztexte sind im Programm enthalten. [7-Zip-26.02-src.7z](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/7-Zip-26.02-src.7z)

## Dokumentation

- [Spezifikation des .nzip-Formats](docs/NZIP-FORMAT.md)
- [SDK für Entwickler](docs/SDK.md)
- [Versionshinweise](https://github.com/nzip-app/nzip-app.github.io/releases)

## Fehlermeldungen und Vorschläge

Haben Sie ein Problem gefunden oder einen Vorschlag? Erstellen Sie eine Meldung im Bereich [Issues](https://github.com/nzip-app/nzip-app.github.io/issues) dieses Repositorys. Oder kontaktieren Sie den Support über die Website: [support kontaktieren](https://nzip-app.github.io/de/).

---

<sub>© 2026 Marco Cavallo. Alle Rechte vorbehalten. NZip, der Name und das Logo NZip gehören Marco Cavallo, dem Schöpfer und Autor der Software.</sub>
