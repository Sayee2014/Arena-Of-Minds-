import streamlit as st

st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1519681393784-d120267933ba");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

h1, h2, h3, p, label {
    color: white !important;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.main {
    background-color: rgba(0, 0, 0, 0.55);
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)
