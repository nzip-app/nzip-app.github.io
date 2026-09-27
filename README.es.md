<p align="center"><img src="img/nzip-256.png" width="112" alt="NZip"></p>

<h1 align="center">NZip</h1>

<p align="center"><b>Archivos comprimidos más pequeños, verificados y reparables — para Windows, macOS y Linux.</b></p>

<p align="center"><a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest"><img alt="release" src="https://img.shields.io/github/v/release/nzip-app/nzip-app.github.io?label=NZip&color=7c5cf6"></a> <a href="https://github.com/nzip-app/nzip-app.github.io/releases"><img alt="downloads" src="https://img.shields.io/github/downloads/nzip-app/nzip-app.github.io/total?color=3b82f6"></a> <img alt="platforms" src="https://img.shields.io/badge/Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-555"> <img alt="license" src="https://img.shields.io/badge/license-freeware-2ea44f"> <a href="https://paypal.me/cavallomarcoapp"><img alt="coffee" src="https://img.shields.io/badge/%E2%98%95-PayPal-f59e0b"></a></p>

<p align="center"><a href="README.md">English</a> · <a href="README.it.md">Italiano</a> · <b>Español</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <a href="README.zh.md">中文</a></p>

<p align="center"><a href="https://nzip-app.github.io/es/"><b>Sitio web</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe"><b>Descargar para Windows</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest">Última versión: 3.2.7</a></p>

---

NZip es un compresor de archivos moderno. Crea archivos .nzip más pequeños que los de 7-Zip y RAR, vuelve a leer y verifica cada archivo antes de dar por concluida la operación, y también abre los archivos comprimidos de otros programas: ZIP, RAR, 7z, TAR, ISO y muchos más. La edición básica es gratuita para todos, también para uso empresarial.

## En resumen

- **Más pequeños**: píxeles de las imágenes PNG en JPEG XL sin pérdida, recompresión sin pérdida de JPEG, ZIP y documentos de Office, y compresores modernos elegidos para cada tipo de datos.
- **Verificados**: cada archivo se compara con el original (BLAKE3) antes de cerrar el archivo comprimido y de nuevo durante la extracción.
- **Reparables**: los datos de recuperación permiten restaurar archivos comprimidos dañados.
- **Seguros**: cifrado AES-256 del contenido y de los nombres; con NZip Pro, también firma digital y cifrado por destinatario.
- **Compatibles**: lee y extrae ZIP, RAR, 7z, TAR, GZ, BZ2, XZ, ZSTD, LZH, ARJ, CAB, ISO y WIM, y los convierte a .nzip.
- **Integrados**: menús del Explorador de archivos (Windows 11 y 10), Finder, Dolphin, Nautilus y Nemo; 7 idiomas.

## Pruebas comparativas

Tamaño de los archivos comprimidos obtenidos a partir de las mismas carpetas, en el mismo PC. Cada archivo comprimido se extrajo y se comparó byte a byte con el original.

**Documentos** · 723,6 MB — 981 documentos reales: PDF, Word, Excel, PowerPoint, HTML (Govdocs1)

| Programa | Tamaño | respecto a 7-Zip ultra |
|---|---:|---:|
| ZIP (máxima) | 454,5 MB | +9,0% |
| RAR 7 (mejor, sólido) | 431,3 MB | +3,4% |
| tar.xz (xz, máxima) | 416,9 MB | −0,0% |
| tar.zst (zstd 19, long) | 396,6 MB | −4,9% |
| 7-Zip ultra | 417,0 MB | — |
| **NZip normal** | 328,2 MB | **−21,3%** |
| **NZip máxima** | 324,1 MB | **−22,3%** |

**Imágenes** · 147,6 MB — 24 PNG de la Kodak Image Suite y 40 fotos JPEG originales de la NASA

| Programa | Tamaño | respecto a 7-Zip ultra |
|---|---:|---:|
| ZIP (máxima) | 145,7 MB | +0,4% |
| RAR 7 (mejor, sólido) | 145,9 MB | +0,5% |
| tar.xz (xz, máxima) | 145,1 MB | +0,0% |
| tar.zst (zstd 19, long) | 145,1 MB | −0,0% |
| 7-Zip ultra | 145,1 MB | — |
| **NZip normal** | 114,9 MB | **−20,8%** |
| **NZip máxima** | 114,2 MB | **−21,3%** |

**Copias de seguridad de código fuente** · 303,8 MB — carpeta de copias de seguridad de un proyecto: 3 versiones consecutivas del código fuente de Python (3.13.5, 3.13.6, 3.13.7)

| Programa | Tamaño | respecto a 7-Zip ultra |
|---|---:|---:|
| ZIP (máxima) | 87,9 MB | +173,4% |
| RAR 7 (mejor, sólido) | 25,9 MB | −19,4% |
| tar.xz (xz, máxima) | 33,7 MB | +4,8% |
| tar.zst (zstd 19, long) | 22,9 MB | −28,8% |
| 7-Zip ultra | 32,1 MB | — |
| **NZip normal** | 21,2 MB | **−34,2%** |
| **NZip máxima** | 20,6 MB | **−35,8%** |

**Código fuente** · 101,3 MB — fuentes oficiales de Python 3.13.7 (texto, C y Python)

| Programa | Tamaño | respecto a 7-Zip ultra |
|---|---:|---:|
| ZIP (máxima) | 29,3 MB | +39,3% |
| RAR 7 (mejor, sólido) | 23,4 MB | +11,2% |
| tar.xz (xz, máxima) | 21,1 MB | +0,4% |
| tar.zst (zstd 19, long) | 21,7 MB | +3,4% |
| 7-Zip ultra | 21,0 MB | — |
| **NZip normal** | 20,7 MB | **−1,6%** |
| **NZip máxima** | 20,3 MB | **−3,6%** |

<sub>Los tiempos de NZip incluyen la verificación completa del archivo, que los demás programas no realizan. Los porcentajes en verde y rojo son respecto a 7-Zip ultra.</sub>

[Todos los detalles, los tiempos y los demás formatos, en el sitio web.](https://nzip-app.github.io/es/#benchmark)

## Descarga

| Plataforma | Archivo |
|---|---|
| Windows 10 y 11 (64 bits) — Instalador | [NZip-Setup.exe](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe) |
| Windows 10 y 11 (64 bits) — Paquete MSI | [NZip.msi](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip.msi) |
| Plantillas ADMX de directivas empresariales | [NZip-ADMX.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-ADMX.zip) |
| macOS — Apple Silicon | [NZip-macos-arm64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-arm64.zip) |
| macOS — Intel | [NZip-macos-x64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-x64.zip) |
| Linux — x86-64 | [NZip-linux-x64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-x64.tar.gz) |
| Linux — ARM64 | [NZip-linux-arm64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-arm64.tar.gz) |

Las versiones para macOS y Linux están en vista previa. Comprueba la integridad de los archivos descargados con [SHA256SUMS.txt](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/SHA256SUMS.txt).

## Requisitos

- Windows 10 u 11 de 64 bits (x64)
- macOS 13 o posterior (Apple Silicon o Intel) — vista previa
- Linux x86-64 o ARM64 con glibc 2.28 o posterior — vista previa

## Ediciones

- **NZip** — gratuito para todos, particulares y empresas, para cualquier uso.
- **NZip Pro** — licencia personal: compresión Ultra, archivos divididos y autoextraíbles, firma digital, copias de seguridad programadas, búsqueda en archivos, copia a la nube.
- **NZip Enterprise** — licencia empresarial por puesto: directivas empresariales, clave de recuperación, registro de actividad, MSI, SDK.

**NZip Pro · NZip Enterprise** — Cómo obtenerla: abre NZip → Configuración → Pasar a Pro o Enterprise, introduce tus datos y envía la solicitud. Recibirás una clave de licencia para pegar en la app: se activa al instante, incluso sin internet.

La edición básica es gratuita para siempre. Pro y Enterprise se solicitan directamente desde la app.

## ☕ Apoya NZip

NZip es gratuito para todos y lo seguirá siendo. Si te ahorra tiempo y espacio, invítame a un café: incluso una pequeña aportación en PayPal marca la diferencia. ¡Gracias!

<p><a href="https://paypal.me/cavallomarcoapp"><img alt="Invítame a un café" src="https://img.shields.io/badge/%E2%98%95%20Invítame%20a%20un%20café-PayPal-f59e0b?logo=paypal&logoColor=white&style=for-the-badge"></a></p>

## Licencia

NZip es software propietario, distribuido gratuitamente en su edición básica. Su uso se rige por el **Contrato de licencia de usuario final (EULA)**, que se muestra y se acepta durante la instalación. El código fuente no es público; el formato .nzip está documentado abiertamente.

- 📦 [Licencias de componentes de terceros](legal/TERZE-PARTI.txt)
- El motor de 7-Zip (7z.dll), utilizado únicamente para leer archivos comprimidos de otros programas, se distribuye bajo la licencia GNU LGPL con la restricción de unRAR; los textos completos se incluyen en el programa. [7-Zip-26.02-src.7z](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/7-Zip-26.02-src.7z)

## Documentación

- [Especificación del formato .nzip](docs/NZIP-FORMAT.md)
- [SDK para desarrolladores](docs/SDK.md)
- [Notas de la versión](https://github.com/nzip-app/nzip-app.github.io/releases)

## Incidencias y sugerencias

¿Has encontrado un problema o tienes una sugerencia? Abre una incidencia en la sección [Issues](https://github.com/nzip-app/nzip-app.github.io/issues) de este repositorio. O contacta con soporte desde el sitio web: [contactar con soporte](https://nzip-app.github.io/es/).

---

<sub>© 2026 Marco Cavallo. Todos los derechos reservados. NZip, el nombre y el logotipo de NZip pertenecen a Marco Cavallo, creador y autor del programa.</sub>
