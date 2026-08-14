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
    background: rgba(0,0,0,0.75);
    backdrop-filter: blur(1px);
    z-index: -1;
}

/* Title */

h1 {
    text-align: center;
    color: white !important;
    font-size: 85px !important;

    text-shadow:
        0px 0px 10px black,
        0px 0px 20px black,
        0px 0px 30px black;
}

/* Headings */

h2 {
    text-align: center;
    color: #FFE5FF !important;
    font-size: 42px !important;

    text-shadow:
        0px 0px 10px black;
}

/* Paragraphs */

p {
    text-align: center;
    color: white !important;
    font-size: 24px !important;

    text-shadow:
        2px 2px 10px rgba(0,0,0,1);
}

/* Hero Card */

.hero-box {

    background: rgba(0,0,0,0.45);

    padding: 35px;

    border-radius: 25px;

    margin-top: 20px;
    margin-bottom: 40px;

    backdrop-filter: blur(3px);
}

/* Buttons */

.stButton > button {

    width: 100% !important;
    height: 90px !important;

    font-size: 24px !important;
    font-weight: bold !important;

    color: white !important;

    border-radius: 20px !important;
    border: none !important;

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

    transform: scale(1.04);

    box-shadow:
        0px 0px 25px rgba(232,121,249,1);
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 Arena of Minds 🌸")

st.markdown("""
<div class="hero-box">

<h2>🏟️ Welcome to Arena of Minds 🏟️</h2>

<p>
Step into a world of curiosity, creativity, and discovery.
</p>

<p>
Every challenge is a quest.<br>
Every lesson is an adventure.
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

    if st.button("📚 Scholar's Library", use_container_width=True):
        st.switch_page("pages/Scholars_Library.py")

    if st.button("🤖 Athena Tower", use_container_width=True):
        st.switch_page("pages/Athena_Tower.py")

    if st.button("🎨 Creative Kingdom", use_container_width=True):
        st.switch_page("pages/Creative_Kingdom.py")

with col2:

    if st.button("🧮 Math Kingdom", use_container_width=True):
        st.switch_page("pages/Math_Kingdom.py")

    if st.button("💻 Tech Fortress", use_container_width=True):
        st.switch_page("pages/Tech_Fortress.py")

    if st.button("🌿 Serenity Gardens", use_container_width=True):
        st.switch_page("pages/Serenity_Gardens.py")

st.markdown(
"""
<div style='text-align:center; margin-top:30px;'>

<h3 style='color:#FFD9FF;'>

🌸 Grow your mind like a wisteria vine. 🌸

</h3>

</div>
""",
unsafe_allow_html=True
)
