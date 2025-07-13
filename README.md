# 🚀 **faiz** — Your All-in-One Super Command-Line Toolkit

**faiz** is a powerful **command-line utility** designed to streamline your daily tasks—whether you're a developer, tech enthusiast, sysadmin, or just someone who loves automation.

From image conversions and QR code generation to SSH management, project scaffolding, and comprehensive PDF operations, **faiz** puts everything you need right at your fingertips in one clean, easy-to-use command.

✅ Fast • 🗭️ Secure • 🔧 Modular • 🌐 Internet-Ready • ⚡ Productivity-Boosting

> **Note:** Currently, **faiz** is only supported on **Windows** systems.

---

## 📦 Installation

### Install via **PyPI**

```bash
pip install faiz
```

👉 **PyPI Package:** [https://pypi.org/project/faiz/](https://pypi.org/project/faiz/)

### Or Clone via **GitHub**

```bash
git clone https://github.com/zokasta/faiz.git
cd faiz
python setup.py install
```

👉 **GitHub Repository:** [https://github.com/zokasta/faiz](https://github.com/zokasta/faiz)

---

## ✨ Key Features Overview

| Feature                | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| ⚙️ Environment Manager | Manage and edit `.env` files effortlessly                    |
| 🖼️ Image Converter    | Convert images to **WebP**, **AVIF**, **JPEG**, **PNG**      |
| 🔍 Web Search          | Search instantly via Google or Microsoft Edge                |
| 🔑 SSH Manager         | Save, list, and connect to SSH profiles quickly              |
| 🐙 Git Automation      | Perform common Git operations faster                         |
| 📱 QR Code Generator   | Generate QR codes from text, links, or data                  |
| 🧮 File Type Counter   | Count files by extension and size in any directory           |
| 👟 Cursor Fun          | Move mouse cursor randomly for fun or screen awake scenarios |
| ⚛️ React.js Setup      | Scaffold basic React.js projects quickly                     |
| 🄻 Laravel Setup       | Bootstrap Laravel PHP projects in seconds                    |
| 📄 **PDF Suite**       | Lock, unlock, merge, split, compress, rotate, watermark PDFs |

---

## 🔥 Example Usage

### ✅ Manage Environment Variables

```bash
faiz env set "API_KEY title" myapikey
faiz env list
faiz env get "API_KEY title"
faiz env remove "API_KEY title"
```

### 🖼️ Image Conversion

```bash
faiz webp *
faiz avif *.png
faiz jpeg *.jpg
faiz png *.bmp
```

### 🔍 Quick Web Searches

```bash
faiz search "Best AI tools"
```

### 🔑 SSH Shortcuts

```bash
faiz ssh list
faiz ssh create
faiz ssh connect myserver
faiz ssh delete myserver
```

### 🐙 Git Automation

```bash
faiz git clone title https://github.com/zokasta/faiz.git
faiz git run title
faiz git make title
faiz git list
```

### 🧮 File Counting

```bash
faiz count *
faiz count * --deep
faiz count "*.jpg"
faiz count folder
```

### 📄 PDF Operations

```bash
# Lock/Unlock
faiz pdf lock report.pdf --password 1234
faiz pdf unlock locked_report.pdf    # prompts for password

# Merge PDFs
faiz pdf merge a.pdf b.pdf c.pdf output.pdf

# Split PDF into pages
faiz pdf split document.pdf

# Compress PDF
faiz pdf compress large.pdf --output small.pdf

# Rotate PDF pages
faiz pdf rotate doc.pdf --angle 90 --output rotated.pdf

# Add page numbers
faiz pdf pagenum file.pdf --output numbered.pdf
```

> 🔧 **Tip:** Run `faiz pdf` with no arguments to see full PDF usage guide.

---

## 📋 All Available Commands

| Command            | Description                   |
| ------------------ | ----------------------------- |
| `faiz avif`        | Convert to AVIF               |
| `faiz webp`        | Convert to WebP               |
| `faiz jpeg`        | Convert to JPEG               |
| `faiz png`         | Convert to PNG                |
| `faiz search`      | Web search                    |
| `faiz edge`        | Edge desktop search           |
| `faiz edge_mobile` | Edge mobile simulation search |
| `faiz ssh`         | SSH profile manager           |
| `faiz git`         | Git helper                    |
| `faiz qr`          | QR Code generator             |
| `faiz cursor`      | Cursor movement fun           |
| `faiz count`       | Count files/folders and sizes |
| `faiz env`         | Environment manager           |
| `faiz reactjs`     | React.js scaffolding          |
| `faiz laravel`     | Laravel scaffolding           |
| `faiz pdf`         | Comprehensive PDF toolkit     |
| `faiz version`     | Show version                  |
| `faiz --version`   | Show version                  |
| `faiz list`        | List all available commands   |

---

## 🌱 Future Feature Ideas

| Feature                      | Description                                  |
| ---------------------------- | -------------------------------------------- |
| 📄 **PDF to Word/PPT/Excel** | Convert PDF to Office formats                |
| 🛠️ **PDF OCR**              | Extract text from scanned PDFs               |
| 🎨 **Edit PDF**              | Add text, images, shapes, annotations        |
| 💧 **Advanced Watermark**    | Text & image watermark customization         |
| 📐 **Crop/Redact**           | Crop margins or redact sensitive information |
| 🌐 **HTML to PDF**           | Convert web pages to PDF                     |
| 🩹 **Repair PDF**            | Fix corrupted or damaged PDFs                |
| 🗃️ **PDF/A Conversion**     | Archive-standard PDF format                  |

👉 Have more ideas? [Open an issue](https://github.com/zokasta/faiz/issues) or send a pull request!

---

## 💡 Contribute

We welcome contributions from the community. Feel free to fork the repository, submit issues, or open pull requests:

👉 **GitHub:** [https://github.com/zokasta/faiz](https://github.com/zokasta/faiz)

---

## ⚖️ License

Licensed under the **MIT License**.

---

> Made with ❤️ by **Faiz Rajput** — Fast. Clean. Efficient.
