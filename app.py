import streamlit as st

# Title Page
st.title("🏟️ Arena of Minds")
st.subheader("Enter the Arena. Master Your Mind.")

# Begin Journey Button
if st.button("🚀 Begin Journey"):

    st.success("Welcome to Arena of Minds!")

    st.header("📚 Dashboard")

    # Dashboard Layout
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📚 Learn"):
            st.write("🔬 Welcome to Science Valley!")

        if st.button("💻 Coding"):
            st.write("🏰 Welcome to Tech Fortress!")

    with col2:
        if st.button("📝 Quests"):
            st.write("⚔️ Complete quests and earn Aura!")

        if st.button("🏆 Achievements"):
            st.write("🏅 Your badges will appear here.")

    with col3:
        if st.button("😌 Relax Zone"):
            st.write("🌿 Welcome to Serenity Gardens!")

        if st.button("🤖 AI Mentor"):
            st.write("🧠 Your guide will arrive soon.")

    if st.button("🔍 Just Curious"):
        st.write("🌌 Explore amazing facts and mysteries!")
