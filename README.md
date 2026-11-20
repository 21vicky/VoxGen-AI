<div align="center">

# 🎙️ VoxGen AI

### AI-Powered Multilingual Text-to-Speech Studio

**Transform your words into natural-sounding speech with AI.**

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Edge--TTS-AI%20Voice-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

</div>

---

## 🌟 Overview

**VoxGen AI** is a modern multilingual Text-to-Speech application built using Python, Streamlit and Microsoft Edge TTS.

It transforms written text into natural-sounding speech using neural AI voices. Users can select languages, customize voice settings, listen to generated audio and download it in MP3 format.

With an interactive dashboard and customizable speech controls, VoxGen AI makes voice generation simple and accessible.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 Multilingual Support | Generate speech in multiple languages |
| 🎙️ Neural AI Voices | Choose from different AI voices |
| ⚡ Text-to-Speech | Convert written text into audio |
| 🎛️ Voice Customization | Adjust speed, volume and pitch |
| 🔊 Audio Preview | Listen to generated speech |
| 📥 MP3 Download | Download generated audio |
| 📊 Dashboard Analytics | Track generation statistics |
| 🕘 Audio History | Access recent generations |
| 🧹 Text Management | Clear text and generation history |
| 🎨 Modern UI | Interactive Streamlit dashboard |

---

## 🖥️ Application Preview

### 🎛️ Main Dashboard

<p align="center">
  <img src="assets/voxgen-dashboard.png" alt="VoxGen AI Main Dashboard" width="95%">
</p>

### 🔊 Audio Preview

<p align="center">
  <img src="assets/voxgen-audio-preview.png" alt="VoxGen AI Audio Preview" width="95%">
</p>

---

## 🌍 Supported Languages

VoxGen AI includes neural voice options for:

- 🇺🇸 English (United States)
- 🇬🇧 English (United Kingdom)
- 🇮🇳 English (India)
- 🇮🇳 Tamil
- 🇮🇳 Hindi
- 🇫🇷 French
- 🇩🇪 German
- 🇪🇸 Spanish

*Available voices depend on the configured voice list.*

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| Edge TTS | Neural Text-to-Speech engine |
| asyncio | Asynchronous processing |
| MP3 | Generated audio format |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/21vicky/VoxGen-AI.git
```

### 2. Navigate to Project Folder

```bash
cd VoxGen-AI
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 🔄 Project Workflow

```mermaid
flowchart TD
    A(["🚀 Launch VoxGen AI"]) --> B["🖥️ Streamlit Dashboard"]
    B --> C["✍️ Enter Text"]
    C --> D["🌍 Select Language & Voice"]
    D --> E["🎛️ Configure Speech Settings"]
    E --> F["⚡ Generate Speech"]
    F --> G{"Valid Input?"}

    G -- No --> H["⚠️ Display Error"]
    H --> C

    G -- Yes --> I["🤖 Edge TTS Engine"]
    I --> J["🎵 Generate MP3"]
    J --> K["💾 Save Audio"]
    K --> L["🔊 Audio Preview"]
    L --> M["📥 Download MP3"]
    L --> N["📊 Update Statistics"]
    L --> O["🕘 Update History"]

    style A fill:#172554,color:#fff,stroke:#3b82f6
    style I fill:#312e81,color:#fff,stroke:#818cf8
    style G fill:#78350f,color:#fff,stroke:#f59e0b
    style M fill:#064e3b,color:#fff,stroke:#10b981
```

📖 **Detailed documentation:** [WORKFLOW.md](WORKFLOW.md)

---

## 📁 Project Structure

```text
VoxGen-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── WORKFLOW.md
├── .gitignore
│
├── assets/
│   ├── voxgen-dashboard.png
│   └── voxgen-audio-preview.png
│
└── generated_audio/
    └── Generated MP3 files
```

---

## 🧠 What I Learned

Through this project, I explored:

- Implementing Text-to-Speech using neural AI voices.
- Working with the Edge TTS Python library.
- Building interactive applications using Streamlit.
- Managing asynchronous Python operations.
- Customizing speech speed, volume and pitch.
- Generating and downloading MP3 audio.
- Managing application state using Streamlit session state.
- Designing a modern AI-powered dashboard.

---

## 🔮 Future Enhancements

- Persistent audio generation history.
- Batch text-to-speech conversion.
- Additional neural voice options.
- Voice preview before generation.
- Cloud deployment.

---

## ⚠️ Important Notes

- An active internet connection is required for Edge TTS speech generation.
- Generated MP3 files are saved locally.
- Recent history and generation statistics use Streamlit session state and may reset when the session restarts.

---

## 👨‍💻 Developer

<div align="center">

### Vignesh U

**Aspiring AI & ML Engineer | Full Stack Developer**

Building practical AI applications and exploring the future of Artificial Intelligence.

<p>
  <a href="https://github.com/21vicky">
    <img src="https://img.shields.io/badge/GitHub-21vicky-black?style=for-the-badge&logo=github">
  </a>
</p>

</div>

---

<div align="center">

### 🎙️ VoxGen AI

**Give Your Words a Voice.**

*Built with ❤️ using Python and Artificial Intelligence.*

</div>