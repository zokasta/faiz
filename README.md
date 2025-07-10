# 🚀 **faiz** — Your All-in-One Super Command-Line Toolkit

**faiz** is a powerful **command-line utility** designed to streamline your daily tasks—whether you're a developer, tech enthusiast, sysadmin, or just someone who loves automation.

From image conversions and QR code generation to SSH management and project scaffolding, **faiz** puts everything you need right at your fingertips in one clean, easy-to-use command.

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
| 🖼️ Image Converter    | Convert images to **WebP** and **AVIF** formats easily       |
| 🔍 Web Search          | Search instantly via Google or Microsoft Edge                |
| 🔑 SSH Manager         | Save, list, and connect to SSH profiles quickly              |
| 🐙 Git Automation      | Perform common Git operations faster                         |
| 📱 QR Code Generator   | Generate QR codes from text, links, or data                  |
| 🧮 File Type Counter   | Count files by extension in any directory                    |
| 👟 Cursor Fun          | Move mouse cursor randomly for fun or screen awake scenarios |
| ⚛️ React.js Setup      | Scaffold basic React.js projects quickly                     |
| 🄻 Laravel Setup       | Bootstrap Laravel PHP projects in seconds                    |

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
faiz webp *.png
faiz avif *
faiz avif *.png
```

### 🔍 Quick Web Searches

```bash
faiz search "Best AI tools"
```

### Auto Search for Edge Rewards

```bash
faiz edge 
faiz edge_mobile
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

### 📱 QR Code Generation

```bash
faiz qr "https://example.com"
```

### 🧮 File Counting

```bash
faiz count *
faiz count * --deep 
faiz count "*.jpg"
faiz count "*.pdf"
faiz count folder
```

### 👟 Cursor Movement

```bash
faiz cursor
```

---

## 📋 All Available Commands

| Command            | Description                        |
| ------------------ | ---------------------------------- |
| `faiz avif`        | Convert images to AVIF             |
| `faiz webp`        | Convert images to WebP             |
| `faiz search`      | Google Search                      |
| `faiz edge`        | Search in Microsoft Edge (Desktop) |
| `faiz edge_mobile` | Search in Edge (Mobile simulation) |
| `faiz ssh`         | SSH profile manager                |
| `faiz git`         | Git helper                         |
| `faiz qr`          | QR Code generator                  |
| `faiz cursor`      | Move cursor randomly               |
| `faiz count`       | File type counter                  |
| `faiz env`         | Environment manager                |
| `faiz reactjs`     | React.js scaffolding               |
| `faiz laravel`     | Laravel scaffolding                |
| `faiz version`     | Show version                       |
| `faiz --version`   | Show version                       |
| `faiz list`        | List all commands                  |

---

## 🌱 Future Feature Ideas

Here are some exciting ideas planned for future versions of **faiz**:

| Feature                    | Description                                         |
| -------------------------- | --------------------------------------------------- |
| 📄 **PDF Maker**           | Convert text or images into PDF files               |
| 🖼️ **Multi-Type Changer** | Batch convert images between multiple formats       |
| 📼 **Image Compressor**    | Compress images while maintaining quality           |
| 🔍 **File Finder**         | Quickly locate files by name, size, or type         |
| 🤖 **Mini AI Assistant**   | Simple AI for device-based text summarization, chat |
| 🗃️ **Docker Manager**     | Manage Docker containers and images from CLI        |
| 📝 **Markdown to HTML**    | Instant Markdown to HTML conversion                 |
| 🎤 **Text-to-Speech**      | Convert text to spoken audio                        |
| 💼 **Price Tracker**       | Track online product prices via command-line        |
| 📊 **SEO Rank Checker**    | Check website ranking for keywords                  |
| ⚡ **AI Code Generator**    | AI-assisted code snippets based on prompts          |

👉 Have more ideas? [Open an issue](https://github.com/zokasta/faiz/issues) or send a pull request!

---

## 💡 Contribute

We welcome contributions from the community. Feel free to fork the repository, submit issues, or open pull requests here:

👉 **GitHub:** [https://github.com/zokasta/faiz](https://github.com/zokasta/faiz)

---

## ⚖️ License

Licensed under the **MIT License**.

---

> Made with ❤️ by **Faiz Rajput** — Fast. Clean. Efficient.
