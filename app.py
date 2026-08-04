import streamlit as st

st.title("🏟️ Arena of Minds")
st.subheader("Enter the Arena. Master Your Mind.")

if st.button("🚀 Begin Journey"):
    st.success("Welcome to Arena of Minds!")

    st.header("📚 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("📚 Learn")
        st.button("💻 Coding")

    with col2:
        st.button("📝 Quests")
        st.button("🏆 Achievements")

    with col3:
        st.button("😌 Relax Zone")
        st.button("🤖 AI Mentor")

    st.button("🔍 Just Curious")
