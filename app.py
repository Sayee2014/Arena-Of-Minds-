import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🏟️",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at top right, #2E5BBA 0%, transparent 30%),
    radial-gradient(circle at bottom left, #4A90E2 0%, transparent 30%),
    linear-gradient(135deg, #081C3B, #143D6B);
}

/* Title */
.main-title {
    text-align: center;
    font-size: 70px;
    font-weight: 700;
    color: #7DF9FF;

    text-shadow:
    0 0 10px rgba(255,255,255,0.5),
    0 0 20px rgba(125,249,255,0.7),
    0 0 40px rgba(125,249,255,0.4);
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 26px;
    color: #FFEAA7;
    margin-bottom: 25px;
}

/* Icons Row */
.icons {
    text-align: center;
    font-size: 30px;
    margin-bottom: 20px;
}

/* Location Row */
.locations {
    text-align: center;
    color: white;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Button */
div.stButton > button {
    display: block;
    margin: auto;
    width: 380px;
    height: 80px;

    border-radius: 20px;

    background-color: #4AA3DF;
    color: white;

    font-size: 26px;
    font-weight: bold;

    border: none;

    box-shadow: 0 0 20px rgba(74,163,223,0.5);
}

div.stButton > button:hover {
    background-color: #67B7F7;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🏟️ Arena of Minds</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter the Arena. Master Your Mind.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="icons">🌌 ⭐ 🏆 📚 💻 🌙 🤖 ⚔️ 🎨 🚀</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="locations">🔬 Science Valley | 💻 Tech Fortress | 😌 Serenity Gardens | 🎨 Creative Kingdom</div>',
    unsafe_allow_html=True
)

if st.button("🚀 Begin Journey"):
    st.success("Welcome to Arena of Minds!")

    st.header("📚 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("📚 Learn")
        st.button("💻 Coding")

    with col2:
        st.button("📝 Quests")
        st.button("🏆 Achievements")

    with col3:
        st.button("😌 Relax Zone")
        st.button("🤖 AI Mentor")

    st.button("🔍 Just Curious")
