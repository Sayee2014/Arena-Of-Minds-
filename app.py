col1, col2 = st.columns(2)

with col1:

    if st.button("🔬 Science Valley", use_container_width=True):
        st.switch_page("pages/Science_Hub.py")

    if st.button("📚 Scholar's Library", use_container_width=True):
        st.switch_page("pages/Scholars_Library.py")

    if st.button("🤖 Athena Tower", use_container_width=True):
        st.switch_page("pages/Athena_Tower.py")

    if st.button("🎨 Creative Kingdom", use_container_width=True):
        st.switch_page("pages/Creative_Kingdom.py")

with col2:

    if st.button("🧮 Math Kingdom", use_container_width=True):
        st.switch_page("pages/Math_Hub.py")

    if st.button("💻 Tech Fortress", use_container_width=True):
        st.switch_page("pages/Tech_Fortress.py")

    if st.button("📖 English Realm", use_container_width=True):
        st.switch_page("pages/English_Realm.py")

    if st.button("🌿 Serenity Gardens", use_container_width=True):
        st.switch_page("pages/Serenity_Gardens.py")
