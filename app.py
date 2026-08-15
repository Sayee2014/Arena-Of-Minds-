import streamlit as st
import json
import os
import random

# ============================================================
# ARENA OF MINDS
# Streamlit Version 1
# ============================================================

SAVE_FILE = "arena_of_minds_data.json"


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="⚔️",
    layout="wide"
)


# ============================================================
# COLORS / DESIGN
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top, #252044 0%, #0b0b16 45%, #05050b 100%);
    color: white;
}

/* Main heading */
.aom-title {
    text-align: center;
    font-family: "Comic Sans MS", "Trebuchet MS", sans-serif;
    font-size: 55px;
    font-weight: 900;
    letter-spacing: 3px;
    padding: 20px 0 5px 0;
    text-shadow:
        4px 4px 0px #5d2fa3,
        0px 0px 18px #b98cff;
}

/* Subtitle */
.aom-subtitle {
    text-align: center;
    font-size: 15px;
    letter-spacing: 5px;
    color: #aaaac7;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: rgba(25, 25, 45, 0.92);
    border: 1px solid #39395c;
    border-radius: 20px;
    padding: 25px;
    margin: 10px 0;
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
}

/* Stat cards */
.stat {
    background: linear-gradient(145deg, #19192f, #252541);
    border: 1px solid #414166;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.stat-title {
    color: #aaaac7;
    font-size: 14px;
    font-weight: bold;
}

.stat-value {
    font-size: 30px;
    font-weight: 900;
}

/* Game cards */
.game-card {
    background: linear-gradient(145deg, #17172c, #262643);
    border: 1px solid #42426b;
    border-radius: 22px;
    padding: 25px;
    text-align: center;
    min-height: 150px;
}

.game-title {
    font-size: 22px;
    font-weight: 900;
}

.game-description {
    color: #b7b7cc;
    font-size: 13px;
}

/* Section headings */
.section-title {
    font-family: "Comic Sans MS", "Trebuchet MS", sans-serif;
    font-size: 32px;
    font-weight: 900;
    text-align: center;
    margin: 20px 0;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SAVE / LOAD
# ============================================================

DEFAULT_DATA = {
    "name": "",
    "grade": "",
    "xp": 0,
    "aura": 0,
    "level": 1,
    "challenges_completed": 0
}


def load_data():

    if os.path.exists(SAVE_FILE):

        try:
            with open(SAVE_FILE, "r") as file:
                return json.load(file)

        except:
            return DEFAULT_DATA.copy()

    return DEFAULT_DATA.copy()


def save_data():

    with open(SAVE_FILE, "w") as file:
        json.dump(st.session_state.player, file, indent=4)


# ============================================================
# SESSION STATE
# ============================================================

if "player" not in st.session_state:
    st.session_state.player = load_data()

if "page" not in st.session_state:
    st.session_state.page = "home"


player = st.session_state.player


# ============================================================
# XP SYSTEM
# ============================================================

def xp_needed():

    return player["level"] * 100


def add_rewards(xp=0, aura=0):

    player["xp"] += xp
    player["aura"] += aura

    leveled_up = False

    while player["xp"] >= xp_needed():

        player["xp"] -= xp_needed()
        player["level"] += 1
        leveled_up = True

    save_data()

    if leveled_up:

        st.balloons()

        st.success(
            f"🔥 LEVEL UP! You reached Level {player['level']}!"
        )


# ============================================================
# TITLE
# ============================================================

def title():

    st.markdown(
        '<div class="aom-title">⚔️ ARENA OF MINDS ⚔️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="aom-subtitle">LEARN • CHALLENGE • CONQUER</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SETUP PAGE
# ============================================================

def setup_page():

    title()

    st.markdown(
        '<div class="section-title">WELCOME, FUTURE CHAMPION</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        name = st.text_input(
            "👤 What's your name?"
        )

        grade = st.text_input(
            "🎓 What's your grade?"
        )

        st.markdown("</div>", unsafe_allow_html=True)

        if st.button(
            "⚔️ START YOUR JOURNEY",
            use_container_width=True
        ):

            if name.strip() == "":
                st.warning("Please enter your name.")

            elif grade.strip() == "":
                st.warning("Please enter your grade.")

            else:

                player["name"] = name.strip()
                player["grade"] = grade.strip()
                player["xp"] = 0
                player["aura"] = 0
                player["level"] = 1
                player["challenges_completed"] = 0

                save_data()

                st.session_state.page = "home"

                st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

def sidebar():

    with st.sidebar:

        st.markdown(
            "## ⚔️ ARENA OF MINDS"
        )

        st.markdown(
            f"### 👤 {player['name']}"
        )

        st.markdown(
            f"🎓 Grade {player['grade']}"
        )

        st.divider()

        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"

        if st.button("📚 Study", use_container_width=True):
            st.session_state.page = "study"

        if st.button("⚔️ Challenges", use_container_width=True):
            st.session_state.page = "challenges"

        if st.button("🏆 Ranks", use_container_width=True):
            st.session_state.page = "ranks"

        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = "profile"

        if st.button("🌙 Chill", use_container_width=True):
            st.session_state.page = "chill"

        st.divider()

        st.caption(
            "⭐ XP  •  ✨ Aura  •  🏆 Levels"
        )


# ============================================================
# HOME
# ============================================================

def home_page():

    title()

    st.markdown(
        f"""
        <div class="card">
        <h2>Welcome, {player['name']}! 👋</h2>
        <p>Grade {player['grade']} • Your journey continues...</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Stats

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="stat">
            <div class="stat-title">⭐ XP</div>
            <div class="stat-value">{player['xp']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="stat">
            <div class="stat-title">✨ AURA</div>
            <div class="stat-value">{player['aura']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="stat">
            <div class="stat-title">🏆 LEVEL</div>
            <div class="stat-value">{player['level']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # XP progress

    required = xp_needed()

    progress = player["xp"] / required

    st.write(
        f"**Level {player['level']} Progress — {player['xp']} / {required} XP**"
    )

    st.progress(progress)

    st.write("")

    st.markdown(
        '<div class="section-title">🔥 ENTER THE ARENA</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="game-card">
            <div class="game-title">📚 STUDY</div>
            <div class="game-description">
            Turn studying into games.
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "ENTER STUDY",
            key="home_study",
            use_container_width=True
        ):
            st.session_state.page = "study"
            st.rerun()

    with c2:

        st.markdown(
            """
            <div class="game-card">
            <div class="game-title">⚔️ CHALLENGES</div>
            <div class="game-description">
            Complete challenges and earn rewards.
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "VIEW CHALLENGES",
            key="home_challenges",
            use_container_width=True
        ):
            st.session_state.page = "challenges"
            st.rerun()

    with c3:

        st.markdown(
            """
            <div class="game-card">
            <div class="game-title">🌙 CHILL</div>
            <div class="game-description">
            Take a break and relax.
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "ENTER CHILL",
            key="home_chill",
            use_container_width=True
        ):
            st.session_state.page = "chill"
            st.rerun()


# ============================================================
# STUDY PAGE
# ============================================================

def study_page():

    title()

    st.markdown(
        '<div class="section-title">📚 STUDY ARENA</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Choose a game and turn learning into an adventure."
    )

    games = [
        (
            "➗",
            "MATH MAZE",
            "Solve maths questions to escape the maze.",
            "math"
        ),
        (
            "🔬",
            "SCIENCE LAB",
            "Experiment, think and solve.",
            "science"
        ),
        (
            "⚔️",
            "SST CHRONICLES",
            "History, geography and civics.",
            "sst"
        ),
        (
            "🇮🇳",
            "HINDI HUNT",
            "Grammar, vocabulary and Hindi challenges.",
            "hindi"
        ),
        (
            "🇬🇧",
            "WORD BATTLE",
            "Battle your way through English.",
            "english"
        )
    ]

    for row in range(0, len(games), 2):

        cols = st.columns(2)

        for i, col in enumerate(cols):

            index = row + i

            if index >= len(games):
                break

            icon, name, description, game_id = games[index]

            with col:

                st.markdown(
                    f"""
                    <div class="game-card">
                    <div style="font-size:40px">{icon}</div>
                    <div class="game-title">{name}</div>
                    <div class="game-description">
                    {description}
                    </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"PLAY {name}",
                    key=f"game_{game_id}",
                    use_container_width=True
                ):

                    st.session_state.game = game_id
                    st.session_state.page = "game"

                    st.rerun()


# ============================================================
# GAME DATA
# ============================================================

QUESTIONS = {

    "math": [

        (
            "What is 7 × 8?",
            ["54", "56", "64", "48"],
            "56"
        ),

        (
            "What is 144 ÷ 12?",
            ["10", "11", "12", "14"],
            "12"
        ),

        (
            "What is 25 + 37?",
            ["52", "62", "72", "58"],
            "62"
        ),

        (
            "What is 100 − 43?",
            ["47", "57", "67", "53"],
            "57"
        )

    ],

    "science": [

        (
            "Which gas do plants mainly take in during photosynthesis?",
            ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
            "Carbon dioxide"
        ),

        (
            "What is the boiling point of water at sea level?",
            ["50°C", "75°C", "100°C", "150°C"],
            "100°C"
        )

    ],

    "sst": [

        (
            "Which is a major landform of India?",
            ["Mountains", "Moon", "Asteroid", "Comet"],
            "Mountains"
        ),

        (
            "Which institution makes laws in a democracy?",
            ["Legislature", "Hospital", "Museum", "Bank"],
            "Legislature"
        )

    ],

    "hindi": [

        (
            "‘दिन’ का विलोम शब्द क्या है?",
            ["सुबह", "रात", "दोपहर", "समय"],
            "रात"
        ),

        (
            "‘जल’ का पर्यायवाची शब्द क्या है?",
            ["आकाश", "पानी", "अग्नि", "वायु"],
            "पानी"
        )

    ],

    "english": [

        (
            "Choose the correct plural of 'child'.",
            ["Childs", "Children", "Childes", "Childrens"],
            "Children"
        ),

        (
            "Which word is an adjective?",
            ["Run", "Beautiful", "Quickly", "Jump"],
            "Beautiful"
        )

    ]

}


GAME_NAMES = {
    "math": "➗ MATH MAZE",
    "science": "🔬 SCIENCE LAB",
    "sst": "⚔️ SST CHRONICLES",
    "hindi": "🇮🇳 HINDI HUNT",
    "english": "🇬🇧 WORD BATTLE"
}


# ============================================================
# GAME PAGE
# ============================================================

def game_page():

    game = st.session_state.game

    title()

    st.markdown(
        f'<div class="section-title">{GAME_NAMES[game]}</div>',
        unsafe_allow_html=True
    )

    if "current_question" not in st.session_state:

        st.session_state.current_question = random.choice(
            QUESTIONS[game]
        )

    question, options, answer = st.session_state.current_question

    st.markdown(
        f"""
        <div class="card">
        <h2>{question}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    for option in options:

        if st.button(
            option,
            key=f"answer_{option}",
            use_container_width=True
        ):

            if option == answer:

                st.success("✅ Correct! +50 XP and +5 Aura!")

                add_rewards(50, 5)

                st.session_state.current_question = random.choice(
                    QUESTIONS[game]
                )

                st.rerun()

            else:

                st.error(
                    f"❌ Not quite! The correct answer was: {answer}"
                )

    st.write("")

    if st.button("← Back to Study"):

        if "current_question" in st.session_state:
            del st.session_state.current_question

        st.session_state.page = "study"

        st.rerun()


# ============================================================
# CHALLENGES
# ============================================================

def challenges_page():

    title()

    st.markdown(
        '<div class="section-title">⚔️ DAILY CHALLENGES</div>',
        unsafe_allow_html=True
    )

    challenges = [

        ("⭐ Knowledge Warrior",
         "Answer a study question.",
         100,
         10),

        ("🔥 Arena Explorer",
         "Play one Study Arena game.",
         75,
         5),

        ("🧠 Brain Master",
         "Complete a challenge.",
         125,
         15)

    ]

    for i, (name, description, xp, aura) in enumerate(challenges):

        st.markdown(
            f"""
            <div class="card">
            <h3>{name}</h3>
            <p>{description}</p>
            <p>⭐ +{xp} XP &nbsp;&nbsp; ✨ +{aura} Aura</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"COMPLETE {name}",
            key=f"challenge_{i}",
            use_container_width=True
        ):

            player["challenges_completed"] += 1

            add_rewards(xp, aura)

            st.success(
                f"🔥 Challenge completed! +{xp} XP and +{aura} Aura!"
            )


# ============================================================
# PROFILE
# ============================================================

def profile_page():

    title()

    st.markdown(
        '<div class="section-title">👤 YOUR PROFILE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">
        <h2>👤 {player['name']}</h2>
        <p>🎓 Grade {player['grade']}</p>
        <hr>
        <p>🏆 Level: {player['level']}</p>
        <p>⭐ XP: {player['xp']}</p>
        <p>✨ Aura: {player['aura']}</p>
        <p>⚔️ Challenges Completed: {player['challenges_completed']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RANKS
# ============================================================

def ranks_page():

    title()

    st.markdown(
        '<div class="section-title">🏆 RANKS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">
        <h2>🏆 Level {player['level']}</h2>
        <h3>⭐ {player['xp']} XP</h3>
        <h3>✨ {player['aura']} Aura</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Online leaderboards can be added later when we connect Arena of Minds to an online database."
    )


# ============================================================
# CHILL
# ============================================================

def chill_page():

    title()

    st.markdown(
        '<div class="section-title">🌙 CHILL ZONE</div>',
        unsafe_allow_html=True
    )

    quotes = [

        "Small progress is still progress. 🌱",

        "Rest. Reset. Return stronger. 🌙",

        "Your mind is your greatest arena. 🧠",

        "One challenge at a time. ⚔️",

        "You don't have to be perfect. Just keep learning. ✨"

    ]

    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
        <div style="font-size:70px;">🌌</div>
        <h2>{random.choice(quotes)}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "✨ GIVE ME ANOTHER THOUGHT",
        use_container_width=True
    ):
        st.rerun()


# ============================================================
# PAGE ROUTER
# ============================================================

if player["name"] == "":

    setup_page()

else:

    sidebar()

    if st.session_state.page == "home":
        home_page()

    elif st.session_state.page == "study":
        study_page()

    elif st.session_state.page == "game":
        game_page()

    elif st.session_state.page == "challenges":
        challenges_page()

    elif st.session_state.page == "profile":
        profile_page()

    elif st.session_state.page == "ranks":
        ranks_page()

    elif st.session_state.page == "chill":
        chill_page()
