<p align="center"><img src="img/nzip-256.png" width="112" alt="NZip"></p>

<h1 align="center">NZip</h1>

<p align="center"><b>更小、经过校验、可修复的压缩包 — 适用于 Windows、macOS 和 Linux。</b></p>

<p align="center"><a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest"><img alt="release" src="https://img.shields.io/github/v/release/nzip-app/nzip-app.github.io?label=NZip&color=7c5cf6"></a> <a href="https://github.com/nzip-app/nzip-app.github.io/releases"><img alt="downloads" src="https://img.shields.io/github/downloads/nzip-app/nzip-app.github.io/total?color=3b82f6"></a> <img alt="platforms" src="https://img.shields.io/badge/Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-555"> <img alt="license" src="https://img.shields.io/badge/license-freeware-2ea44f"> <a href="https://paypal.me/cavallomarcoapp"><img alt="coffee" src="https://img.shields.io/badge/%E2%98%95-PayPal-f59e0b"></a></p>

<p align="center"><a href="README.md">English</a> · <a href="README.it.md">Italiano</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.ru.md">Русский</a> · <b>中文</b></p>

<p align="center"><a href="https://nzip-app.github.io/zh/"><b>官方网站</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe"><b>下载 Windows 版</b></a> · <a href="https://github.com/nzip-app/nzip-app.github.io/releases/latest">最新版本: 3.2.7</a></p>

---

NZip 是一款现代文件压缩软件。它生成的 .nzip 压缩包比 7-Zip 和 RAR 更小，在报告操作完成之前会重新读取并校验每个文件，还能打开其他程序创建的压缩包：ZIP、RAR、7z、TAR、ISO 等众多格式。基础版对所有人免费，包括商业用途。

## 概览

- **更小**：PNG 图像像素以无损 JPEG XL 存储，对 JPEG、ZIP 和 Office 文档进行无损再压缩，并针对每种数据类型选用现代压缩算法。
- **经过校验**：在完成压缩包之前以及解压时，每个文件都会与原始文件进行比对（BLAKE3）。
- **可修复**：恢复记录可用于修复损坏的压缩包。
- **安全可靠**：AES-256 加密文件内容和文件名；NZip Pro 还提供数字签名和面向收件人的加密。
- **兼容性强**：可读取并解压 ZIP、RAR、7z、TAR、GZ、BZ2、XZ、ZSTD、LZH、ARJ、CAB、ISO 和 WIM，并将其转换为 .nzip。
- **深度集成**：文件资源管理器菜单（Windows 11 和 10）、Finder、Dolphin、Nautilus 和 Nemo；支持 7 种语言。

## 基准测试

在同一台电脑上对相同文件夹进行压缩所得压缩包的大小。每个压缩包都经过解压，并与原始文件逐字节比对。

**文档** · 723.6 MB — 981 份真实文档：PDF、Word、Excel、PowerPoint、HTML（Govdocs1）

| 程序 | 大小 | 相对于 7-Zip 极限 |
|---|---:|---:|
| ZIP（最大） | 454.5 MB | +9.0% |
| RAR 7（最佳，固实） | 431.3 MB | +3.4% |
| tar.xz（xz，最大） | 416.9 MB | −0.0% |
| tar.zst（zstd 19，long） | 396.6 MB | −4.9% |
| 7-Zip 极限 | 417.0 MB | — |
| **NZip 标准** | 328.2 MB | **−21.3%** |
| **NZip 最大** | 324.1 MB | **−22.3%** |

**图像** · 147.6 MB — 来自 Kodak Image Suite 的 24 张 PNG 和 40 张 NASA 原始 JPEG 照片

| 程序 | 大小 | 相对于 7-Zip 极限 |
|---|---:|---:|
| ZIP（最大） | 145.7 MB | +0.4% |
| RAR 7（最佳，固实） | 145.9 MB | +0.5% |
| tar.xz（xz，最大） | 145.1 MB | +0.0% |
| tar.zst（zstd 19，long） | 145.1 MB | −0.0% |
| 7-Zip 极限 | 145.1 MB | — |
| **NZip 标准** | 114.9 MB | **−20.8%** |
| **NZip 最大** | 114.2 MB | **−21.3%** |

**源代码备份** · 303.8 MB — 项目的备份文件夹：Python 源代码的 3 个连续版本（3.13.5、3.13.6、3.13.7）

| 程序 | 大小 | 相对于 7-Zip 极限 |
|---|---:|---:|
| ZIP（最大） | 87.9 MB | +173.4% |
| RAR 7（最佳，固实） | 25.9 MB | −19.4% |
| tar.xz（xz，最大） | 33.7 MB | +4.8% |
| tar.zst（zstd 19，long） | 22.9 MB | −28.8% |
| 7-Zip 极限 | 32.1 MB | — |
| **NZip 标准** | 21.2 MB | **−34.2%** |
| **NZip 最大** | 20.6 MB | **−35.8%** |

**源代码** · 101.3 MB — Python 3.13.7 官方源代码（文本、C 和 Python）

| 程序 | 大小 | 相对于 7-Zip 极限 |
|---|---:|---:|
| ZIP（最大） | 29.3 MB | +39.3% |
| RAR 7（最佳，固实） | 23.4 MB | +11.2% |
| tar.xz（xz，最大） | 21.1 MB | +0.4% |
| tar.zst（zstd 19，long） | 21.7 MB | +3.4% |
| 7-Zip 极限 | 21.0 MB | — |
| **NZip 标准** | 20.7 MB | **−1.6%** |
| **NZip 最大** | 20.3 MB | **−3.6%** |

<sub>NZip 的用时包含对压缩包的完整校验，其他程序不执行此步骤。绿色和红色百分比均相对于 7-Zip 极限。</sub>

[完整细节、用时及其他格式的结果请访问官方网站。](https://nzip-app.github.io/zh/#benchmark)

## 下载

| 平台 | 文件 |
|---|---|
| Windows 10 和 11（64 位） — 安装程序 | [NZip-Setup.exe](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-Setup.exe) |
| Windows 10 和 11（64 位） — MSI 安装包 | [NZip.msi](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip.msi) |
| 企业策略 ADMX 模板 | [NZip-ADMX.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-ADMX.zip) |
| macOS — Apple Silicon | [NZip-macos-arm64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-arm64.zip) |
| macOS — Intel | [NZip-macos-x64.zip](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-macos-x64.zip) |
| Linux — x86-64 | [NZip-linux-x64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-x64.tar.gz) |
| Linux — ARM64 | [NZip-linux-arm64.tar.gz](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/NZip-linux-arm64.tar.gz) |

macOS 和 Linux 版本目前为预览版。 请使用 [SHA256SUMS.txt](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/SHA256SUMS.txt) 校验所下载文件的完整性。

## 系统要求

- Windows 10 或 11，64 位（x64）
- macOS 13 或更高版本（Apple Silicon 或 Intel）— 预览版
- Linux x86-64 或 ARM64，glibc 2.28 或更高版本 — 预览版

## 版本

- **NZip** — 对所有人免费，个人和企业均可用于任何用途。
- **NZip Pro** — 个人许可：极限压缩、分卷压缩包和自解压压缩包、数字签名、计划备份、压缩包内搜索、复制到云端。
- **NZip Enterprise** — 按工作站计的企业许可：企业策略、恢复密钥、活动日志、MSI、SDK。

**NZip Pro · NZip Enterprise** — 获取方式：打开 NZip → 设置 → 升级到 Pro 或 Enterprise，填写您的信息并发送申请。您将收到一个许可证密钥，粘贴到应用中即可立即激活，无需联网。

基础版永久免费。Pro 和 Enterprise 直接在应用中申请。

## ☕ 支持 NZip

NZip 对所有人免费，并将一直免费。如果它为您节省了时间和空间，请我喝杯咖啡吧：即使是通过 PayPal 的小额捐助也意义重大。谢谢！

<p><a href="https://paypal.me/cavallomarcoapp"><img alt="请我喝杯咖啡" src="https://img.shields.io/badge/%E2%98%95%20请我喝杯咖啡-PayPal-f59e0b?logo=paypal&logoColor=white&style=for-the-badge"></a></p>

## 许可

NZip 是专有软件，其基础版免费分发。使用本软件受 **最终用户许可协议（EULA）** 约束，该协议在安装过程中显示并由用户接受。源代码不公开；.nzip 格式的文档公开提供。

- 📦 [第三方组件许可](legal/TERZE-PARTI.txt)
- 7-Zip 引擎（7z.dll）仅用于读取其他程序创建的压缩包，依据 GNU LGPL 许可并附带 unRAR 限制条款分发；完整许可文本已随程序提供。 [7-Zip-26.02-src.7z](https://github.com/nzip-app/nzip-app.github.io/releases/latest/download/7-Zip-26.02-src.7z)

## 文档

- [.nzip 格式规范](docs/NZIP-FORMAT.md)
- [开发者 SDK](docs/SDK.md)
- [发行说明](https://github.com/nzip-app/nzip-app.github.io/releases)

## 问题反馈

发现问题或有任何建议？请在本仓库的 [Issues](https://github.com/nzip-app/nzip-app.github.io/issues) 部分提交反馈。 也可以通过网站联系技术支持：[联系技术支持](https://nzip-app.github.io/zh/)。

---

<sub>© 2026 Marco Cavallo。保留所有权利。NZip、NZip 名称和标志归本软件的创作者和作者 Marco Cavallo 所有。</sub>
