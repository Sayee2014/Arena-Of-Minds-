import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>

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
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(1px);
    z-index: -1;
}

/* Remove ugly block look */
.block-container {
    padding-top: 2rem;
}

/* Title */
h1 {
    text-align: center;
    font-size: 80px !important;
    color: #FFE8FF !important;
    text-shadow: 0px 0px 25px #f0abfc;
}

/* Subtitles */
h2,h3 {
    text-align: center;
    color: #F5D0FE !important;
}

/* Text */
p,div,label {
    text-align: center;
    color: white !important;
    font-size: 24px !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 80px;
    font-size: 24px;
    font-weight: bold;

    border-radius: 20px;
    border: none;

    color: white;

    background: linear-gradient(
        135deg,
        #d946ef,
        #9333ea
    );

    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px #d946ef;
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 Arena of Minds 🌸")

st.markdown("""
## ✨ Welcome to the Wisteria Courtyard ✨

Beneath the glowing wisteria blossoms lies a realm of learning,
creativity and discovery.

Choose your destination and begin your journey.
""")

st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:

    if st.button("🔬 Science Valley"):
        st.switch_page("pages/Science_Valley.py")

    if st.button("🤖 Athena Tower"):
        st.switch_page("pages/Athena_Tower.py")

with col2:

    if st.button("💻 Tech Fortress"):
        st.switch_page("pages/Tech_Fortress.py")

    if st.button("🌿 Serenity Gardens"):
        st.switch_page("pages/Serenity_Gardens.py")

st.write("")
st.write("")

st.markdown("""
### 🌸 Grow your mind like a wisteria vine. 🌸
""")
