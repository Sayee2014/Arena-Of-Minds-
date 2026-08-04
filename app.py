import streamlit as st

st.title("🏟️ Arena of Minds")
st.subheader("Enter the Arena. Master Your Mind.")

if st.button("🚀 Begin Journey"):
    st.success("Welcome to Arena of Minds!")

    st.header("📚 Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.button("📚 Learn")
        st.button("💻 Coding")

    with col2:
        st.button("📝 Quests")
        st.button("😌 Relax Zone")
``
