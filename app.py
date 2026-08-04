import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🏟️",
    layout="wide"
)

# -------------------- STYLING --------------------

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
    text-align:center;
    font-size:70px;
    color:#7DF9FF;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    font-size:24px;
    color:#FFEAA7;
    margin-bottom:20px;
}

.icons {
    text-align:center;
    font-size:28px;
}

div.stButton > button {
    border-radius:20px;
    height:65px;
    width:100%;
    font-size:20px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HOME PAGE --------------------

st.markdown(
    "<div class='main-title'>🏟️ Arena of Minds</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Enter the Arena. Master Your Mind.</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='icons'>🌌 ⭐ 🏆 📚 💻 🤖 ⚔️ 🎨 🚀</div>",
    unsafe_allow_html=True
)

st.write("")

# -------------------- BEGIN JOURNEY --------------------

if st.button("🚀 Begin Journey"):

    st.success("Welcome, Learner!")

    # Aura and XP
    st.info("⭐ XP: 0 | 🌌 Aura: 0")

    st.header("🏟️ Central Arena")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("📚 Learn"):
            st.header("🔬 Science Valley")

            st.write("Choose your Grade")

            st.button("📚 Grade 5")
            st.button("📚 Grade 6")
            st.button("📚 Grade 7")
            st.button("📚 Grade 8")

        if st.button("💻 Coding"):
            st.header("🏰 Tech Fortress")
            st.write("Learn Python")
            st.write("Create Projects")
            st.write("Build Apps")

    with col2:

        if st.button("📝 Quests"):
            st.header("⚔️ Quests")
            st.write("Complete lessons and earn XP.")

        if st.button("🏆 Achievements"):
            st.header("🏆 Achievements")

            st.write("🌱 Plant Apprentice")
            st.write("💻 Coding Rookie")
            st.write("🌌 Future Arena Legend")

    with col3:

        if st.button("😌 Relax Zone"):
            st.header("🌿 Serenity Gardens")

            st.success("Take a deep breath.")

            st.write(
                "🌙 You are doing better than you think."
            )

        if st.button("🤖 AI Mentor"):
            st.header("🤖 Athena")

            st.write(
                "Hello Learner! I'm here to help."
            )

    if st.button("🔍 Just Curious"):

        st.header("🌌 Curiosity Corner")

        st.write("🚀 Why is space dark?")
        st.write("🦑 Why do octopuses have three hearts?")
        st.write("🌋 Why do volcanoes erupt?")
