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

/* Main Title */
.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: 700;
    color: white;
    margin-top: 40px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 24px;
    color: #D6F4FF;
    margin-bottom: 40px;
}

/* Center Button */
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
    box-shadow: 0px 0px 20px rgba(74,163,223,0.5);
}

div.stButton > button:hover {
    background-color: #67B7F7;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)
