import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>

/* Background */

.stApp {
    background-image: url("https://i.pinimg.com/1200x/d4/58/75/d45875edac6347e1b2254dc4ea1b48bc.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark overlay */

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.78);
    backdrop-filter: blur(1px);
    z-index: -1;
}

/* Main area */

.block-container {
    padding-top: 2rem;
}

/* Title */

h1 {
    text-align: center;
    font-size: 85px !important;
    color: white !important;

    text-shadow:
        0 0 10px black,
        0 0 20px black,
        0 0 30px black;
}

/* Headings */

h2 {
    text-align: center;
    font-size: 42px !important;

    color: #FFE5FF !important;

    text-shadow:
        0 0 10px black;
}

/* Text */

p, div, label {
    text-align: center;
    color: white !important;
    font-size: 24px !important;

    text-shadow:
        2px 2px 8px rgba(0,0,0,0.9);
}

/* Welcome card */

.hero-box {
    background: rgba(0,0,0,0.45);
    padding: 35px;
    border-radius: 25px;
    margin-bottom: 35px;
    backdrop-filter: blur(3px);
}

/* Buttons */

.stButton > button {

    width: 100% !important;
    height: 95px !important;

    font-size: 26px !important;
    font-weight: bold !important;

    border-radius: 20px !important;
    border: none !important;

    color: white !important;

    background: linear-gradient(
        135deg,
        #e879f9,
        #9333ea
    ) !important;

    box-shadow:
        0px 0px 15px rgba(232,121,249,0.6);

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.05);

    box-shadow:
        0px 0px 25px rgba(232,121,249,0.9);
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 Arena of Minds 🌸")

st.markdown("""
<div class="hero-box">

<h2>✨ Welcome to the Wisteria Courtyard ✨</h2>

<p>
Beneath the glowing wisteria blossoms lies a realm of learning,
creativity and discovery.
</p>

<p>
Choose your destination and begin your journey.
</p>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    if st.button("🔬 Science Valley", use_container_width=True):
        st.switch_page("pages/Science_Valley.py")

    if st.button("🤖 Athena Tower", use_container_width=True):
        st.switch_page("pages/Athena_Tower.py")

with col2:

    if st.button("💻 Tech Fortress", use_container_width=True):
        st.switch_page("pages/Tech_Fortress.py")

    if st.button("🌿 Serenity Gardens", use_container_width=True):
        st.switch_page("pages/Serenity_Gardens.py")

st.write("")

st.markdown("""
<h3 style="text-align:center; color:#FFD9FF;">
🌸 Grow your mind like a wisteria vine. 🌸
</h3>
""", unsafe_allow_html=True)
