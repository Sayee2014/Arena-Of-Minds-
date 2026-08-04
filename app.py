import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🏟️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0B1F3A, #1E3A5F);
}

.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-top: 50px;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: #D6F4FF;
    margin-bottom: 40px;
}

div.stButton > button {
    display: block;
    margin: auto;
    border-radius: 15px;
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
