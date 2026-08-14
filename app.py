import streamlit as st

st.set_page_config(page_title="Arena of Minds", page_icon="🏟️")

st.title("🏟️ Arena of Minds")
st.subheader("Learn • Explore • Grow")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name}!")

location = st.selectbox(
    "Choose a location",
    [
        "Science Valley 🔬",
        "Tech Fortress 💻",
        "Serenity Gardens 🌿",
        "Athena Tower 🤖"
    ]
)

if location == "Science Valley 🔬":
    st.header("🔬 Science Valley")
    st.write("Discover experiments and scientific knowledge!")

elif location == "Tech Fortress 💻":
    st.header("💻 Tech Fortress")
    st.write("Practice coding and build amazing projects!")

elif location == "Serenity Gardens 🌿":
    st.header("🌿 Serenity Gardens")
    st.write("Take a break and recharge your mind.")

elif location == "Athena Tower 🤖":
    st.header("🤖 Athena Tower")
    question = st.text_input("Ask Athena a question")
    
    if question:
        st.write("Athena says:")
        st.info("Keep learning. Every expert was once a beginner.")

st.divider()

st.write("⭐ Arena of Minds Version 1.0")
