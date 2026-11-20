
import streamlit as st
import asyncio
import edge_tts
import os
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="VoxGen AI | Voice Studio",
    page_icon="🎙️",
    layout="wide"
)

os.makedirs("generated_audio", exist_ok=True)

# ==========================================
# SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

if "generated_count" not in st.session_state:
    st.session_state.generated_count = 0

if "text_input" not in st.session_state:
    st.session_state.text_input = ""

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background: #0b1120;
    color: #f1f5f9;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    color: #38bdf8;
    font-size: 42px;
}

h2, h3 {
    color: #e2e8f0;
}

.subtitle {
    color: #94a3b8;
    font-size: 17px;
}

.card {
    background: #172033;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #263449;
    margin-bottom: 15px;
}

.stButton > button {
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    min-height: 45px;
}

.stButton > button:hover {
    border: 1px solid #38bdf8;
}

.metric-label {
    color: #94a3b8;
    font-size: 14px;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("🎙️ VoxGen AI")

st.markdown(
    '<p class="subtitle">Your Personal AI Voice Generation Studio</p>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# VOICE OPTIONS
# ==========================================

voice_options = {
    "English (US) - Female": "en-US-AriaNeural",
    "English (US) - Male": "en-US-GuyNeural",
    "English (UK) - Female": "en-GB-SoniaNeural",
    "English (UK) - Male": "en-GB-RyanNeural",
    "English (India) - Female": "en-IN-NeerjaNeural",
    "English (India) - Male": "en-IN-PrabhatNeural",
    "Tamil - Female": "ta-IN-PallaviNeural",
    "Tamil - Male": "ta-IN-ValluvarNeural",
    "Hindi - Female": "hi-IN-SwaraNeural",
    "Hindi - Male": "hi-IN-MadhurNeural",
    "French - Female": "fr-FR-DeniseNeural",
    "German - Female": "de-DE-KatjaNeural",
    "Spanish - Female": "es-ES-ElviraNeural"
}

# ==========================================
# DASHBOARD METRICS
# ==========================================

st.subheader("📊 Dashboard Overview")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Total Generations",
        st.session_state.generated_count
    )

with m2:
    st.metric(
        "Available Voices",
        len(voice_options)
    )

with m3:
    st.metric(
        "Languages",
        6
    )

st.divider()

# ==========================================
# MAIN WORKSPACE
# ==========================================

col1, col2 = st.columns([2, 1])

with col1:

    st.subheader("📝 Text Workspace")

    text_input = st.text_area(
        "Enter your text",
        placeholder="Type something you want VoxGen AI to speak...",
        height=220,
        key="text_input"
    )

    st.caption(f"Characters: {len(text_input)}")

    def clear_text():
        st.session_state.text_input = ""

    if st.button("🗑️ Clear Text", on_click=clear_text):
        pass
with col2:

    st.subheader("⚙️ Voice Studio")

    selected_voice = st.selectbox(
        "Choose AI Voice",
        list(voice_options.keys())
    )

    voice = voice_options[selected_voice]

    speed = st.slider(
        "🎚️ Speech Speed",
        -50, 50, 0, 5
    )

    volume = st.slider(
        "🔊 Volume",
        -50, 50, 0, 5
    )

    pitch = st.slider(
        "🎭 Voice Pitch",
        -50, 50, 0, 5
    )

st.divider()

# ==========================================
# GENERATE SPEECH
# ==========================================

if st.button("🚀 Generate AI Speech", use_container_width=True):

    if not text_input.strip():

        st.warning("Please enter some text first.")

    else:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_file = f"generated_audio/voxgen_{timestamp}.mp3"

        async def generate_audio():

            communicate = edge_tts.Communicate(
                text=text_input,
                voice=voice,
                rate=f"{speed:+d}%",
                volume=f"{volume:+d}%",
                pitch=f"{pitch:+d}Hz"
            )

            await communicate.save(output_file)

        try:

            with st.spinner("🎙️ Creating your AI voice..."):

                asyncio.run(generate_audio())

            with open(output_file, "rb") as audio:

                audio_bytes = audio.read()

            st.session_state.generated_count += 1

            st.session_state.history.insert(
                0,
                {
                    "file": output_file,
                    "text": text_input,
                    "voice": selected_voice,
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "size": len(audio_bytes)
                }
            )

            st.success("🎉 AI Speech Generated Successfully!")

            st.subheader("🎧 Audio Preview")

            st.audio(
                audio_bytes,
                format="audio/mp3"
            )

            st.download_button(
                "📥 Download MP3",
                data=audio_bytes,
                file_name="voxgen_audio.mp3",
                mime="audio/mpeg",
                use_container_width=True
            )

            st.divider()

            st.subheader("📈 Generation Details")

            a, b, c = st.columns(3)

            with a:
                st.metric("Characters", len(text_input))

            with b:
                st.metric("Audio Size", f"{len(audio_bytes)/1024:.2f} KB")

            with c:
                st.metric("Voice", selected_voice)

        except Exception as e:

            st.error(f"Generation failed: {e}")

# ==========================================
# AUDIO HISTORY
# ==========================================

st.divider()

st.subheader("📜 Recent Audio History")

if st.session_state.history:

    for index, item in enumerate(st.session_state.history):

        with st.expander(
            f"🎵 {item['voice']} — {item['time']}"
        ):

            st.write("**Generated Text:**")
            st.write(item["text"])

            st.write(f"Audio Size: {item['size']/1024:.2f} KB")

            if os.path.exists(item["file"]):

                with open(item["file"], "rb") as audio:

                    audio_bytes = audio.read()

                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    "📥 Download",
                    data=audio_bytes,
                    file_name=f"voxgen_history_{index}.mp3",
                    mime="audio/mpeg",
                    key=f"download_{index}"
                )

    if st.button("🗑️ Clear History"):

        st.session_state.history = []
        st.session_state.generated_count = 0
        st.rerun()

else:

    st.info("No audio generated yet. Create your first AI voice!")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<div class="footer">
    <h3>🎙️ VoxGen AI</h3>
    <p>AI-Powered Text-to-Speech Studio</p>
    <p>Built with Python | Streamlit | Edge TTS</p>
    <p>Day 14 • 30 Days 30 AI Projects</p>
</div>
""", unsafe_allow_html=True)
