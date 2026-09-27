<p align="center"><img src="img/nzip-256.png" width="112" alt="NZip"></p>

<h1 align="center">NZip</h1>

<p align="center"><b>Des archives plus petites, vérifiées et réparables — pour Windows, macOS et Linux.</b></p>

<p align="center"><a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest"><img alt="release" src="https://img.shields.io/github/v/release/nzip-app/nzip-app.github.io?label=NZip&color=7c5cf6"></a> <a href="https://github.com/nzip-app/nzip-app.github.io/releases"><img alt="downloads" src="https://img.shields.io/github/downloads/nzip-app/nzip-app.github.io/total?color=3b82f6"></a> <img alt="platforms" src="https://img.shields.io/badge/Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-555"> <img alt="license" src="https://img.shields.io/badge/license-freeware-2ea44f"> <a href="https://paypal.me/cavallomarcoapp"><img alt="coffee" src="https://img.shields.io/badge/%E2%98%95-PayPal-f59e0b"></a></p>

<p align="center"><a href="README.md">English</a> · <a href="README.it.md">Italiano</a> · <a href="README.es.md">Español</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>

<p align="center"><a href="https://nzip-app.github.io/fr/"><b>Site web</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe"><b>Télécharger pour Windows</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest">Dernière version: 3.2.7</a></p>

---

NZip est un logiciel de compression moderne. Il crée des archives .nzip plus petites que celles de 7-Zip et RAR, relit et vérifie chaque fichier avant de déclarer l'opération terminée, et ouvre également les archives des autres logiciels : ZIP, RAR, 7z, TAR, ISO et bien d'autres. L'édition de base est gratuite pour tous, y compris pour un usage professionnel.

## En bref

- **Plus petites** : pixels des images PNG en JPEG XL sans perte, recompression sans perte des JPEG, ZIP et documents Office, et compresseurs modernes choisis pour chaque type de données.
- **Vérifiées** : chaque fichier est comparé à l'original (BLAKE3) avant la fermeture de l'archive, puis de nouveau lors de l'extraction.
- **Réparables** : les données de récupération permettent de restaurer des archives endommagées.
- **Sécurisées** : chiffrement AES-256 du contenu et des noms ; avec NZip Pro, également signature numérique et chiffrement par destinataire.
- **Compatibles** : lit et extrait ZIP, RAR, 7z, TAR, GZ, BZ2, XZ, ZSTD, LZH, ARJ, CAB, ISO et WIM, et les convertit en .nzip.
- **Intégrées** : menus de l'Explorateur de fichiers (Windows 11 et 10), Finder, Dolphin, Nautilus et Nemo ; 7 langues.

## Bancs d'essai

Taille des archives obtenues à partir des mêmes dossiers, sur le même PC. Chaque archive a été extraite et comparée octet par octet avec l'original.

**Documents** · 723,6 MB — 981 documents réels : PDF, Word, Excel, PowerPoint, HTML (Govdocs1)

| Logiciel | Taille | par rapport à 7-Zip ultra |
|---|---:|---:|
| ZIP (maximum) | 454,5 MB | +9,0% |
| RAR 7 (meilleure, solide) | 431,3 MB | +3,4% |
| tar.xz (xz, maximum) | 416,9 MB | −0,0% |
| tar.zst (zstd 19, long) | 396,6 MB | −4,9% |
| 7-Zip ultra | 417,0 MB | — |
| **NZip normal** | 328,2 MB | **−21,3%** |
| **NZip maximum** | 324,1 MB | **−22,3%** |

**Images** · 147,6 MB — 24 PNG de la Kodak Image Suite et 40 photos JPEG originales de la NASA

| Logiciel | Taille | par rapport à 7-Zip ultra |
|---|---:|---:|
| ZIP (maximum) | 145,7 MB | +0,4% |
| RAR 7 (meilleure, solide) | 145,9 MB | +0,5% |
| tar.xz (xz, maximum) | 145,1 MB | +0,0% |
| tar.zst (zstd 19, long) | 145,1 MB | −0,0% |
| 7-Zip ultra | 145,1 MB | — |
| **NZip normal** | 114,9 MB | **−20,8%** |
| **NZip maximum** | 114,2 MB | **−21,3%** |

**Sauvegardes de code source** · 303,8 MB — dossier de sauvegarde d'un projet : 3 versions consécutives des sources de Python (3.13.5, 3.13.6, 3.13.7)

| Logiciel | Taille | par rapport à 7-Zip ultra |
|---|---:|---:|
| ZIP (maximum) | 87,9 MB | +173,4% |
| RAR 7 (meilleure, solide) | 25,9 MB | −19,4% |
| tar.xz (xz, maximum) | 33,7 MB | +4,8% |
| tar.zst (zstd 19, long) | 22,9 MB | −28,8% |
| 7-Zip ultra | 32,1 MB | — |
| **NZip normal** | 21,2 MB | **−34,2%** |
| **NZip maximum** | 20,6 MB | **−35,8%** |

**Code source** · 101,3 MB — sources officielles de Python 3.13.7 (texte, C et Python)

| Logiciel | Taille | par rapport à 7-Zip ultra |
|---|---:|---:|
| ZIP (maximum) | 29,3 MB | +39,3% |
| RAR 7 (meilleure, solide) | 23,4 MB | +11,2% |
| tar.xz (xz, maximum) | 21,1 MB | +0,4% |
| tar.zst (zstd 19, long) | 21,7 MB | +3,4% |
| 7-Zip ultra | 21,0 MB | — |
| **NZip normal** | 20,7 MB | **−1,6%** |
| **NZip maximum** | 20,3 MB | **−3,6%** |

<sub>Les temps de NZip incluent la vérification complète de l'archive, que les autres logiciels n'effectuent pas. Les pourcentages en vert et en rouge sont calculés par rapport à 7-Zip ultra.</sub>

[Tous les détails, les temps et les autres formats sont disponibles sur le site.](https://nzip-app.github.io/fr/#benchmark)

## Téléchargement

| Plateforme | Fichier |
|---|---|
| Windows 10 et 11 (64 bits) — Programme d'installation | [NZip-Setup.exe](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe) |
| Windows 10 et 11 (64 bits) — Package MSI | [NZip.msi](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip.msi) |
| Modèles ADMX des stratégies d'entreprise | [NZip-ADMX.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-ADMX.zip) |
| macOS — Apple Silicon | [NZip-macos-arm64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-arm64.zip) |
| macOS — Intel | [NZip-macos-x64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-x64.zip) |
| Linux — x86-64 | [NZip-linux-x64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-x64.tar.gz) |
| Linux — ARM64 | [NZip-linux-arm64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-arm64.tar.gz) |

Les versions pour macOS et Linux sont en préversion. Vérifiez l'intégrité des fichiers téléchargés à l'aide de [SHA256SUMS.txt](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/SHA256SUMS.txt).

## Configuration requise

- Windows 10 ou 11, 64 bits (x64)
- macOS 13 ou version ultérieure (Apple Silicon ou Intel) — préversion
- Linux x86-64 ou ARM64 avec glibc 2.28 ou version ultérieure — préversion

## Éditions

- **NZip** — gratuit pour tous, particuliers et entreprises, pour tout usage.
- **NZip Pro** — licence personnelle : compression Ultra, archives en plusieurs parties et auto-extractibles, signature numérique, sauvegardes planifiées, recherche dans les archives, copie vers le cloud.
- **NZip Enterprise** — licence d'entreprise par poste : stratégies d'entreprise, clé de récupération, journal d'activité, MSI, SDK.

**NZip Pro · NZip Enterprise** — Comment l'obtenir : ouvrez NZip → Paramètres → Passer à Pro ou Enterprise, saisissez vos informations et envoyez la demande. Vous recevrez une clé de licence à coller dans l'application : elle s'active immédiatement, même hors ligne.

L'édition de base est gratuite pour toujours. Pro et Enterprise se demandent directement depuis l'application.

## ☕ Soutenir NZip

NZip est gratuit pour tous et le restera. S'il vous fait gagner du temps et de la place, offrez-moi un café : même une petite contribution sur PayPal fait la différence. Merci !

<p><a href="https://paypal.me/cavallomarcoapp"><img alt="Offrez-moi un café" src="https://img.shields.io/badge/%E2%98%95%20Offrez-moi%20un%20café-PayPal-f59e0b?logo=paypal&logoColor=white&style=for-the-badge"></a></p>

## Licence

NZip est un logiciel propriétaire, distribué gratuitement dans son édition de base. Son utilisation est régie par le **Contrat de licence utilisateur final (EULA)**, présenté et accepté lors de l'installation. Le code source n'est pas public ; le format .nzip est documenté de manière ouverte.

- 📦 [Licences des composants tiers](legal/TERZE-PARTI.txt)
- Le moteur de 7-Zip (7z.dll), utilisé uniquement pour lire les archives d'autres logiciels, est distribué sous licence GNU LGPL avec la restriction unRAR ; les textes complets sont inclus dans le logiciel. [7-Zip-26.02-src.7z](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/7-Zip-26.02-src.7z)

## Documentation

- [Spécification du format .nzip](docs/NZIP-FORMAT.md)
- [SDK pour les développeurs](docs/SDK.md)
- [Notes de version](https://github.com/nzip-app/nzip-app.github.io/releases)

## Signalements

Vous avez rencontré un problème ou souhaitez faire une suggestion ? Ouvrez un signalement dans la section [Issues](https://github.com/nzip-app/nzip-app.github.io/issues) de ce dépôt. Ou contactez l'assistance depuis le site : [contacter l'assistance](https://nzip-app.github.io/fr/).

---

<sub>© 2026 Marco Cavallo. Tous droits réservés. NZip, le nom et le logo NZip appartiennent à Marco Cavallo, créateur et auteur du logiciel.</sub>
