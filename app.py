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
    background:
    radial-gradient(circle at top right, #2E5BBA 0%, transparent 30%),
    radial-gradient(circle at bottom left, #4A90E2 0%, transparent 30%),
    linear-gradient(135deg, #0B1F3A, #1E3A5F);
}

.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: 700;
    color: white;
    margin-top: 40px;
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
    border-radius: 20px;
    height: 70px;
    width: 350px;
    font-size: 24px;
    font-weight: bold;
    background-color: #4AA3DF;
    color: white;
    border: none;
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
