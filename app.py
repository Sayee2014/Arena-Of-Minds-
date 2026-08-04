import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🏟️",
    layout="wide"
)

# ---------------- SESSION ---------------- #

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- CSS ---------------- #

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
    font-size: 75px;
    font-weight: bold;
    color: #7DF9FF;
    text-shadow: 0 0 20px rgba(125,249,255,0.7);
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 28px;
    color: white;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Icons */
.icons {
    text-align: center;
    font-size: 34px;
    color: white;
    margin-bottom: 25px;
}

/* Center Buttons */
div.stButton > button {
    background: white;
    color: black;
    height: 75px;
    width: 100%;
    border-radius: 20px;
    border: none;
    font-size: 22px;
    font-weight: bold;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ---------------- #

if st.session_state.page == "home":

    st.markdown(
        '<div class="main-title">🏟️ Arena of Minds</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Enter the Arena. Master Your Mind.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="icons">🌌 ⭐ 🏆 📚 💻 🤖 ⚔️ 🎨 🚀</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🚀 Begin Journey"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- DASHBOARD ---------------- #

elif st.session_state.page == "dashboard":

    st.markdown(
        "<h1 style='text-align:center;color:white;'>🏟️ Central Arena</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;color:#FFEAA7;'>Welcome, Learner!</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center;color:white;'>⭐ XP: 0 | 🌌 Aura: 0</h4>",
        unsafe_allow_html=True
    )

    st.write("")

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
