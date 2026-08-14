import streamlit as st

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Poppins:wght@300;400;500&display=swap" rel="
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
    background: rgba(10, 10, 20, 0.30);
    backdrop-filter: blur(4px);
    z-index: -1;
}

/* Main content box */

.block-container {
    background: rgba(20, 20, 30, 0.45);
    border-radius: 25px;
    padding: 2rem;
    backdrop-filter: blur(8px);
}

/* Title */

h1 {
    font-family: 'Cinzel', serif !important;
    color: #F8E8FF !important;
    text-align: center;
    text-shadow: 0px 0px 20px #d8b4fe;
}

/* Headings */

h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #F3D5FF !important;
}

/* Text */

p, div, label {
    font-family: 'Poppins', sans-serif !important;
    color: white !important;
    font-size: 18px;
}

/* Selectbox */

.stSelectbox {
    background-color: rgba(255,255,255,0.05);
}

/* Buttons */

.stButton > button {
    background: linear-gradient(135deg,#a855f7,#7e22ce);
    color: white;
    border-radius: 15px;
    border: none;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 Arena of Minds 🌸")

st.markdown("""
### ✨ Welcome to the Wisteria Courtyard

Beneath the ancient wisteria blossoms lies a realm of learning, creativity, and discovery.

Choose your destination and begin your adventure.
""")

page = st.selectbox(
    "🌙 Travel To",
    [
        "🌸 Wisteria Courtyard",
        "🔬 Science Valley",
        "💻 Tech Fortress",
        "🤖 Athena Tower",
        "🌿 Serenity Gardens"
    ]
)

if page == "🌸 Wisteria Courtyard":
    st.header("🌸 Wisteria Courtyard")
    st.write("The heart of Arena of Minds. Start your journey here.")

elif page == "🔬 Science Valley":
    st.header("🔬 Science Valley")
    st.write("Explore experiments, discoveries and the wonders of science.")

elif page == "💻 Tech Fortress":
    st.header("💻 Tech Fortress")
    st.write("Train your coding skills and build awesome projects.")

elif page == "🤖 Athena Tower":
    st.header("🤖 Athena Tower")
    question = st.text_input("Ask Athena a question")

    if question:
        st.success("Athena says: Keep learning. Every master was once a beginner.")

elif page == "🌿 Serenity Gardens":
    st.header("🌿 Serenity Gardens")
    st.write("Take a deep breath and recharge your mind.")

st.divider()

st.markdown("""
<center>

🌸 <b>Grow your mind like a wisteria vine.</b> 🌸

</center>
""", unsafe_allow_html=True)
