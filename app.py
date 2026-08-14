import streamlit as st

st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1526397751294-331021109fbd");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
}

h1 {
    color: #7C3AED !important;
    text-align: center;
}

h2, h3 {
    color: #9333EA !important;
}

p, label, div {
    color: #FFFFFF !important;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

</style>
""", unsafe_allow_html=True)
