<p align="center"><img src="img/nzip-256.png" width="112" alt="NZip"></p>

<h1 align="center">NZip</h1>

<p align="center"><b>Архивы меньше, с проверкой и возможностью восстановления — для Windows, macOS и Linux.</b></p>

<p align="center"><a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest"><img alt="release" src="https://img.shields.io/github/v/release/nzip-app/nzip-app.github.io?label=NZip&color=7c5cf6"></a> <a href="https://github.com/nzip-app/nzip-app.github.io/releases"><img alt="downloads" src="https://img.shields.io/github/downloads/nzip-app/nzip-app.github.io/total?color=3b82f6"></a> <img alt="platforms" src="https://img.shields.io/badge/Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-555"> <img alt="license" src="https://img.shields.io/badge/license-freeware-2ea44f"> <a href="https://paypal.me/cavallomarcoapp"><img alt="coffee" src="https://img.shields.io/badge/%E2%98%95-PayPal-f59e0b"></a></p>

<p align="center"><a href="README.md">English</a> · <a href="README.it.md">Italiano</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <b>Русский</b> · <a href="README.zh.md">中文</a></p>

<p align="center"><a href="https://nzip-app.github.io/ru/"><b>Сайт</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe"><b>Скачать для Windows</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest">Последняя версия: 3.2.7</a></p>

---

NZip — современный архиватор. Он создаёт архивы .nzip меньше, чем у 7-Zip и RAR, перечитывает и проверяет каждый файл, прежде чем сообщить о завершении операции, и открывает архивы других программ: ZIP, RAR, 7z, TAR, ISO и многие другие. Базовая редакция бесплатна для всех, в том числе для коммерческого использования.

## Кратко

- **Меньше**: пиксели изображений PNG в JPEG XL без потерь, пересжатие без потерь JPEG, ZIP и документов Office, современные алгоритмы сжатия под каждый тип данных.
- **С проверкой**: каждый файл сверяется с оригиналом (BLAKE3) перед закрытием архива и повторно при распаковке.
- **Восстанавливаемые**: данные для восстановления позволяют восстановить повреждённые архивы.
- **Безопасные**: шифрование AES-256 содержимого и имён файлов; в NZip Pro — также цифровая подпись и шифрование для получателей.
- **Совместимые**: читает и распаковывает ZIP, RAR, 7z, TAR, GZ, BZ2, XZ, ZSTD, LZH, ARJ, CAB, ISO и WIM и конвертирует их в .nzip.
- **Интегрированные**: меню Проводника (Windows 11 и 10), Finder, Dolphin, Nautilus и Nemo; 7 языков.

## Тесты

Размер архивов, полученных из одних и тех же папок на одном и том же ПК. Каждый архив был распакован и сверен с оригиналом байт в байт.

**Документы** · 723,6 MB — 981 реальный документ: PDF, Word, Excel, PowerPoint, HTML (Govdocs1)

| Программа | Размер | относительно 7-Zip ультра |
|---|---:|---:|
| ZIP (максимальное) | 454,5 MB | +9,0% |
| RAR 7 (наилучшее, непрерывный) | 431,3 MB | +3,4% |
| tar.xz (xz, максимальное) | 416,9 MB | −0,0% |
| tar.zst (zstd 19, long) | 396,6 MB | −4,9% |
| 7-Zip ультра | 417,0 MB | — |
| **NZip нормальное** | 328,2 MB | **−21,3%** |
| **NZip максимальное** | 324,1 MB | **−22,3%** |

**Изображения** · 147,6 MB — 24 PNG из Kodak Image Suite и 40 оригинальных фотографий NASA в JPEG

| Программа | Размер | относительно 7-Zip ультра |
|---|---:|---:|
| ZIP (максимальное) | 145,7 MB | +0,4% |
| RAR 7 (наилучшее, непрерывный) | 145,9 MB | +0,5% |
| tar.xz (xz, максимальное) | 145,1 MB | +0,0% |
| tar.zst (zstd 19, long) | 145,1 MB | −0,0% |
| 7-Zip ультра | 145,1 MB | — |
| **NZip нормальное** | 114,9 MB | **−20,8%** |
| **NZip максимальное** | 114,2 MB | **−21,3%** |

**Резервные копии исходного кода** · 303,8 MB — папка резервных копий проекта: 3 последовательные версии исходного кода Python (3.13.5, 3.13.6, 3.13.7)

| Программа | Размер | относительно 7-Zip ультра |
|---|---:|---:|
| ZIP (максимальное) | 87,9 MB | +173,4% |
| RAR 7 (наилучшее, непрерывный) | 25,9 MB | −19,4% |
| tar.xz (xz, максимальное) | 33,7 MB | +4,8% |
| tar.zst (zstd 19, long) | 22,9 MB | −28,8% |
| 7-Zip ультра | 32,1 MB | — |
| **NZip нормальное** | 21,2 MB | **−34,2%** |
| **NZip максимальное** | 20,6 MB | **−35,8%** |

**Исходный код** · 101,3 MB — официальные исходники Python 3.13.7 (текст, C и Python)

| Программа | Размер | относительно 7-Zip ультра |
|---|---:|---:|
| ZIP (максимальное) | 29,3 MB | +39,3% |
| RAR 7 (наилучшее, непрерывный) | 23,4 MB | +11,2% |
| tar.xz (xz, максимальное) | 21,1 MB | +0,4% |
| tar.zst (zstd 19, long) | 21,7 MB | +3,4% |
| 7-Zip ультра | 21,0 MB | — |
| **NZip нормальное** | 20,7 MB | **−1,6%** |
| **NZip максимальное** | 20,3 MB | **−3,6%** |

<sub>Время NZip включает полную проверку архива, которую другие программы не выполняют. Зелёные и красные проценты указаны относительно 7-Zip ультра.</sub>

[Все подробности, время работы и другие форматы — на сайте.](https://nzip-app.github.io/ru/#benchmark)

## Загрузка

| Платформа | Файл |
|---|---|
| Windows 10 и 11 (64 бит) — Установщик | [NZip-Setup.exe](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe) |
| Windows 10 и 11 (64 бит) — Пакет MSI | [NZip.msi](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip.msi) |
| Шаблоны ADMX корпоративных политик | [NZip-ADMX.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-ADMX.zip) |
| macOS — Apple Silicon | [NZip-macos-arm64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-arm64.zip) |
| macOS — Intel | [NZip-macos-x64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-x64.zip) |
| Linux — x86-64 | [NZip-linux-x64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-x64.tar.gz) |
| Linux — ARM64 | [NZip-linux-arm64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-arm64.tar.gz) |

Версии для macOS и Linux являются предварительными. Проверьте целостность загруженных файлов с помощью [SHA256SUMS.txt](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/SHA256SUMS.txt).

## Системные требования

- Windows 10 или 11, 64-разрядная (x64)
- macOS 13 или новее (Apple Silicon или Intel) — предварительная версия
- Linux x86-64 или ARM64 с glibc 2.28 или новее — предварительная версия

## Редакции

- **NZip** — бесплатно для всех, частных лиц и компаний, для любых целей.
- **NZip Pro** — персональная лицензия: ультра-сжатие, многотомные и самораспаковывающиеся архивы, цифровая подпись, резервное копирование по расписанию, поиск в архивах, копирование в облако.
- **NZip Enterprise** — корпоративная лицензия по числу рабочих мест: корпоративные политики, ключ восстановления, журнал действий, MSI, SDK.

**NZip Pro · NZip Enterprise** — Как получить: откройте NZip → Параметры → Перейти на Pro или Enterprise, введите свои данные и отправьте запрос. Вы получите лицензионный ключ, который нужно вставить в приложение: он активируется сразу, даже без интернета.

Базовая версия бесплатна навсегда. Pro и Enterprise запрашиваются прямо в приложении.

## ☕ Поддержите NZip

NZip бесплатен для всех и останется таким. Если он экономит вам время и место, угостите меня кофе: даже небольшой вклад через PayPal очень помогает. Спасибо!

<p><a href="https://paypal.me/cavallomarcoapp"><img alt="Угостите меня кофе" src="https://img.shields.io/badge/%E2%98%95%20Угостите%20меня%20кофе-PayPal-f59e0b?logo=paypal&logoColor=white&style=for-the-badge"></a></p>

## Лицензия

NZip — проприетарное программное обеспечение, базовая редакция которого распространяется бесплатно. Использование регулируется **Лицензионным соглашением с конечным пользователем (EULA)**, которое отображается и принимается при установке. Исходный код не является открытым; формат .nzip открыто документирован.

- 📦 [Лицензии сторонних компонентов](legal/TERZE-PARTI.txt)
- Движок 7-Zip (7z.dll), используемый только для чтения архивов других программ, распространяется по лицензии GNU LGPL с ограничением unRAR; полные тексты лицензий включены в программу. [7-Zip-26.02-src.7z](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/7-Zip-26.02-src.7z)

## Документация

- [Спецификация формата .nzip](docs/NZIP-FORMAT.md)
- [SDK для разработчиков](docs/SDK.md)
- [Примечания к выпуску](https://github.com/nzip-app/nzip-app.github.io/releases)

## Сообщения о проблемах

Обнаружили проблему или хотите что-то предложить? Создайте обращение в разделе [Issues](https://github.com/nzip-app/nzip-app.github.io/issues) этого репозитория. Или свяжитесь с поддержкой через сайт: [связаться с поддержкой](https://nzip-app.github.io/ru/).

---

<sub>© 2026 Marco Cavallo. Все права защищены. NZip, название и логотип NZip принадлежат Марко Кавалло (Marco Cavallo), создателю и автору программы.</sub>
