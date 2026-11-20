# 🎙️ VoxGen AI — System Workflow

<p align="center">
  <b>From Text to Natural-Sounding Speech</b><br>
  An AI-powered multilingual Text-to-Speech application.
</p>

---

## ⚡ Application Architecture

```mermaid
flowchart TD
    A(["🚀 Launch VoxGen AI"]) --> B["🖥️ Streamlit Dashboard"]
    B --> C["✍️ Enter Text"]
    C --> D["🌍 Select Language & Voice"]
    D --> E["🎛️ Configure Speech Settings"]

    E --> F["⚡ Generate Speech"]
    F --> G{"Valid Input?"}

    G -- No --> H["⚠️ Display Error Message"]
    H --> C

    G -- Yes --> I["🤖 Edge TTS Engine"]
    I --> J["🎵 Generate MP3 Audio"]
    J --> K["💾 Save Audio File"]

    K --> L["🔊 Audio Preview"]
    L --> M["📥 Download MP3"]
    L --> N["📊 Update Generation Statistics"]
    L --> O["🕘 Update Recent Audio History"]

    M --> P(["✅ Complete"])
    N --> P
    O --> P

    style A fill:#172554,color:#fff,stroke:#3b82f6
    style I fill:#312e81,color:#fff,stroke:#818cf8
    style P fill:#064e3b,color:#fff,stroke:#10b981
    style G fill:#78350f,color:#fff,stroke:#f59e0b
```

---

## 🔄 How VoxGen AI Works

| Step | Process | Description |
|---|---|---|
| 01 | User Input | Enter text in the workspace |
| 02 | Voice Selection | Choose language and AI voice |
| 03 | Speech Controls | Adjust speed, volume and pitch |
| 04 | Processing | Edge TTS processes the text |
| 05 | Audio Generation | Generate speech in MP3 format |
| 06 | Audio Preview | Listen to generated speech |
| 07 | Download | Download the MP3 file |
| 08 | History | Track recent generations |

---

## 🧠 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| Edge TTS | Neural text-to-speech engine |
| asyncio | Asynchronous speech generation |
| MP3 | Generated audio format |

---

## 🎛️ Core Modules

- **Text Workspace:** Accepts user text.
- **Voice Studio:** Manages language and voice selection.
- **Speech Controls:** Adjusts speed, volume and pitch.
- **Audio Engine:** Generates speech through Edge TTS.
- **Audio Player:** Plays generated speech.
- **Download Manager:** Downloads generated MP3 files.
- **History Manager:** Maintains recent generation history.
- **Dashboard:** Displays usage statistics.

---

## 🔐 Data & Processing

- Text is processed through the Edge TTS online service.
- Generated MP3 files are saved locally.
- Recent history and generation statistics are maintained using Streamlit session state.
- The application requires an internet connection for speech generation.

---

## 🚀 Future Enhancements

- Audio generation history persistence
- Downloadable audio history
- More language and voice options
- Batch text-to-speech conversion
- Voice preview functionality

---

<p align="center">
  <b>🎙️ VoxGen AI</b><br>
  Transform Words into Voice with AI.
</p>