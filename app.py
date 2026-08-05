import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🏟️",
    layout="wide"
)

# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- CSS ----------------

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

.main-title {
    text-align: center;
    font-size: 90px;
    font-weight: bold;
    color: #7DF9FF;
    text-shadow: 0 0 20px rgba(125,249,255,0.7);
}

.subtitle {
    text-align: center;
    font-size: 36px;
    color: white;
    font-weight: bold;
}

.icons {
    text-align: center;
    font-size: 38px;
    margin-bottom: 30px;
}

/* Buttons */

div.stButton > button {
    background: white;
    color: black;
    width: 100%;
    height: 90px;
    border-radius: 20px;
    border: none;
    font-size: 24px;
    font-weight: bold;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------

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

    if st.button("🚀 Begin Journey"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- DASHBOARD ----------------

elif st.session_state.page == "dashboard":

    st.markdown(
        "<h1 style='text-align:center;color:white;'>🏟️ Central Arena</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;color:#FFEAA7;'>Welcome, Learner!</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;color:white;'>⭐ XP: 0 | 🌌 Aura: 0</h2>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📚 Learn"):
            st.session_state.page = "science"
            st.rerun()

        st.button("📝 Quests")

        if st.button("😌 Relax Zone"):
            st.session_state.page = "relax"
            st.rerun()

        st.button("🔍 Just Curious")

    with col2:

        st.button("💻 Coding")

        st.button("🏆 Achievements")

        if st.button("🤖 AI Mentor"):
            st.session_state.page = "mentor"
            st.rerun()

# ---------------- SCIENCE VALLEY ----------------

elif st.session_state.page == "science":

    st.markdown(
        "<h1 style='text-align:center;color:white;'>🔬 Science Valley</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;color:#FFEAA7;'>Choose Your Grade</h2>",
        unsafe_allow_html=True
    )

    st.button("📚 Grade 5")
    st.button("📚 Grade 6")
    st.button("📚 Grade 7")
    st.button("📚 Grade 8")

    if st.button("⬅ Back to Arena"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- SERENITY GARDENS ----------------

elif st.session_state.page == "relax":

    st.markdown(
        "<h1 style='text-align:center;color:white;'>😌 Serenity Gardens</h1>",
        unsafe_allow_html=True
    )

    st.success("🌿 Take a deep breath.")

    st.markdown(
        "<h3 style='text-align:center;'>🌙 You are doing better than you think.</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>⭐ Small progress is still progress.</h3>",
        unsafe_allow_html=True
    )

    if st.button("⬅ Back to Arena"):
        st.session_state.page = "dashboard"
        st.rerun()

# ---------------- ATHENA ----------------

elif st.session_state.page == "mentor":

    st.markdown(
        "<h1 style='text-align:center;color:white;'>🤖 Athena</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;color:#FFEAA7;'>Your Learning Guide</h2>",
        unsafe_allow_html=True
    )

    st.write("📚 Need help with studies?")
    st.write("💙 Need motivation?")
    st.write("🏆 Want to improve?")
    st.write("🚀 Let's learn together!")

    if st.button("⬅ Back to Arena"):
        st.session_state.page = "dashboard"
        st.rerun()
