import streamlit as st
import json
import os
import random
import base64

# ============================================================
# ARENA OF MINDS
# ============================================================

SAVE_FILE = "arena_of_minds_data.json"
BACKGROUND_IMAGE = "anime_background.jpg"

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="⚔️",
    layout="wide"
)

# ============================================================
# DATA
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


if "player" not in st.session_state:
    st.session_state.player = load_data()

if "page" not in st.session_state:
    st.session_state.page = "home"

if "game" not in st.session_state:
    st.session_state.game = None

if "current_question" not in st.session_state:
    st.session_state.current_question = None

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
# BACKGROUND
# ============================================================

def get_background():

    if os.path.exists(BACKGROUND_IMAGE):

        try:

            with open(
                BACKGROUND_IMAGE,
                "rb"
            ) as image_file:

                encoded = base64.b64encode(
                    image_file.read()
                ).decode()

            return f"data:image/jpeg;base64,{encoded}"

        except:
            return ""

    return ""


background = get_background()


# ============================================================
# CSS
# ============================================================

if background:

    background_css = f"""
    background-image:
        linear-gradient(
            rgba(8, 30, 75, 0.35),
            rgba(3, 18, 55, 0.75)
        ),
        url("{background}");
    """

else:

    background_css = """
    background-image:
        radial-gradient(
            circle at 50% 10%,
            #164c91 0%,
            #0b2e63 30%,
            #061a3b 65%,
            #031027 100%
        );
    """


st.markdown(
    f"""
<style>

/* ============================================================
   MAIN BACKGROUND
   ============================================================ */

.stApp {{

    {background_css}

    background-size: cover;

    background-position: center;

    background-attachment: fixed;

    color: white;

    min-height: 100vh;
}}


/* ============================================================
   BLUE ATMOSPHERIC OVERLAY
   ============================================================ */

.stApp::before {{

    content: "";

    position: fixed;

    inset: 0;

    pointer-events: none;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(30,120,255,0.18),
            transparent 30%
        ),

        radial-gradient(
            circle at 80% 70%,
            rgba(0,170,255,0.15),
            transparent 30%
        );

    z-index: 0;
}}


/* ============================================================
   CONTENT
   ============================================================ */

.block-container {{

    position: relative;

    z-index: 1;

    max-width: 1250px;

    padding-top: 25px;

    padding-bottom: 50px;
}}


/* ============================================================
   BOUNCY TITLE
   ============================================================ */

.aom-title {{

    text-align: center;

    font-family:
        "Comic Sans MS",
        "Trebuchet MS",
        sans-serif;

    font-size: 60px;

    font-weight: 900;

    letter-spacing: 4px;

    color: #ffffff;

    text-shadow:

        4px 4px 0px #0755b8,

        0px 0px 12px #39a9ff,

        0px 0px 30px #0077ff;

    animation: bounceTitle 2s infinite;

    margin-bottom: 4px;
}}


@keyframes bounceTitle {{

    0%, 100% {{
        transform:
            translateY(0px)
            rotate(-1deg);
    }}

    50% {{
        transform:
            translateY(-8px)
            rotate(1deg);
    }}

}}


/* ============================================================
   SUBTITLE
   ============================================================ */

.aom-subtitle {{

    text-align: center;

    color: #b9ddff;

    font-size: 14px;

    font-weight: bold;

    letter-spacing: 6px;

    margin-bottom: 30px;
}}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.section-title {{

    text-align: center;

    font-family:
        "Comic Sans MS",
        "Trebuchet MS",
        sans-serif;

    font-size: 34px;

    font-weight: 900;

    color: white;

    text-shadow:

        3px 3px 0px #0755b8,

        0px 0px 15px #1e9bff;

    margin: 25px 0;
}}


/* ============================================================
   CARDS
   ============================================================ */

.card {{

    background:
        linear-gradient(
            145deg,
            rgba(5, 35, 80, 0.88),
            rgba(8, 57, 115, 0.88)
        );

    border:

        1px solid
        rgba(70, 170, 255, 0.5);

    border-radius: 22px;

    padding: 25px;

    margin: 10px 0;

    box-shadow:

        0px 10px 35px
        rgba(0, 70, 160, 0.35);

    backdrop-filter: blur(8px);
}}


/* ============================================================
   STAT CARDS
   ============================================================ */

.stat {{

    background:
        linear-gradient(
            145deg,
            rgba(5, 38, 85, 0.92),
            rgba(8, 63, 125, 0.92)
        );

    border:
        1px solid
        rgba(80, 180, 255, 0.55);

    border-radius: 20px;

    padding: 22px;

    text-align: center;

    box-shadow:
        0px 8px 25px
        rgba(0,80,180,0.35);

    transition:
        transform 0.2s;
}}


.stat:hover {{

    transform:
        translateY(-5px);
}}


.stat-title {{

    color: #a9d9ff;

    font-size: 14px;

    font-weight: bold;
}}


.stat-value {{

    font-size: 34px;

    font-weight: 900;

    color: white;

    text-shadow:
        0px 0px 10px #168fff;
}}


/* ============================================================
   GAME CARDS
   ============================================================ */

.game-card {{

    background:
        linear-gradient(
            145deg,
            rgba(5, 35, 80, 0.93),
            rgba(9, 67, 130, 0.93)
        );

    border:
        1px solid
        rgba(60, 165, 255, 0.55);

    border-radius: 24px;

    padding: 28px;

    text-align: center;

    min-height: 160px;

    box-shadow:
        0px 10px 30px
        rgba(0,60,150,0.4);

    transition:
        transform 0.2s,
        box-shadow 0.2s;
}}


.game-card:hover {{

    transform:
        translateY(-7px)
        scale(1.01);

    box-shadow:
        0px 15px 40px
        rgba(0,130,255,0.35);
}}


.game-title {{

    font-size: 22px;

    font-weight: 900;

    color: white;
}}


.game-description {{

    color: #b8dcff;

    font-size: 13px;

    margin-top: 8px;
}}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {{

    border-radius: 14px;

    border:
        1px solid
        rgba(70, 175, 255, 0.65);

    background:
        linear-gradient(
            135deg,
            #0755b8,
            #087bd1
        );

    color: white;

    font-weight: 900;

    min-height: 45px;

    transition:
        transform 0.15s,
        box-shadow 0.15s;
}}


.stButton > button:hover {{

    transform:
        translateY(-3px);

    box-shadow:
        0px 8px 25px
        rgba(0,140,255,0.5);

    border-color:
        #65c5ff;
}}


/* ============================================================
   INPUTS
   ============================================================ */

.stTextInput input {{

    background:
        rgba(5, 30, 70, 0.9);

    color: white;

    border:
        1px solid #237bc7;

    border-radius: 12px;
}}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {{

    background:
        linear-gradient(
            180deg,
            rgba(3, 25, 58, 0.98),
            rgba(3, 45, 90, 0.98)
        );

    border-right:
        1px solid
        rgba(40,150,255,0.35);
}}


/* ============================================================
   PROGRESS
   ============================================================ */

.stProgress > div > div > div > div {{

    background:
        linear-gradient(
            90deg,
            #0066ff,
            #32b7ff
        );
}}


/* ============================================================
   HIDE STREAMLIT UI
   ============================================================ */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

def show_title():

    st.markdown(
        '<div class="aom-title">'
        '⚔️ ARENA OF MINDS ⚔️'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="aom-subtitle">'
        'LEARN • CHALLENGE • CONQUER'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SETUP
# ============================================================

def setup_page():

    show_title()

    st.markdown(
        '<div class="section-title">'
        'WELCOME, FUTURE CHAMPION'
        '</div>',
        unsafe_allow_html=True
    )

    left, center, right = st.columns(
        [1, 2, 1]
    )

    with center:

        st.markdown(
            """
            <div class="card"
                 style="text-align:center;">

                <div style="font-size:60px;">
                🌙
                </div>

                <h2>
                ENTER THE ARENA
                </h2>

                <p>
                Begin your journey.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        name = st.text_input(
            "👤 What's your name?"
        )

        grade = st.text_input(
            "🎓 What's your grade?"
        )

        if st.button(
            "⚔️ START YOUR JOURNEY",
            use_container_width=True
        ):

            if not name.strip():

                st.warning(
                    "Please enter your name."
                )

            elif not grade.strip():

                st.warning(
                    "Please enter your grade."
                )

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

def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:26px;
                font-weight:900;
                color:#55baff;
                text-shadow:0 0 12px #008cff;
            ">
            ⚔️ ARENA
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            f"### 👤 {player['name']}"
        )

        st.caption(
            f"🎓 Grade {player['grade']}"
        )

        st.divider()

        if st.button(
            "🏠 HOME",
            use_container_width=True
        ):

            st.session_state.page = "home"
            st.rerun()

        if st.button(
            "📚 STUDY",
            use_container_width=True
        ):

            st.session_state.page = "study"
            st.rerun()

        if st.button(
            "⚔️ CHALLENGES",
            use_container_width=True
        ):

            st.session_state.page = "challenges"
            st.rerun()

        if st.button(
            "🏆 RANKS",
            use_container_width=True
        ):

            st.session_state.page = "ranks"
            st.rerun()

        if st.button(
            "👤 PROFILE",
            use_container_width=True
        ):

            st.session_state.page = "profile"
            st.rerun()

        if st.button(
            "🌙 CHILL",
            use_container_width=True
        ):

            st.session_state.page = "chill"
            st.rerun()

        st.divider()

        st.caption(
            f"⭐ XP: {player['xp']}"
        )

        st.caption(
            f"✨ Aura: {player['aura']}"
        )

        st.caption(
            f"🏆 Level: {player['level']}"
        )


# ============================================================
# HOME
# ============================================================

def home_page():

    show_title()

    st.markdown(
        f"""
        <div class="card">

            <h2>
            Welcome, {player['name']}! 👋
            </h2>

            <p>
            🎓 Grade {player['grade']}
            &nbsp; • &nbsp;
            🏆 Level {player['level']}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            f"""
            <div class="stat">

                <div class="stat-title">
                ⭐ XP
                </div>

                <div class="stat-value">
                {player['xp']}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="stat">

                <div class="stat-title">
                ✨ AURA
                </div>

                <div class="stat-value">
                {player['aura']}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            f"""
            <div class="stat">

                <div class="stat-title">
                🏆 LEVEL
                </div>

                <div class="stat-value">
                {player['level']}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    required = xp_needed()

    progress = player["xp"] / required

    st.markdown(
        f"""
        <div class="card">

        <b>
        🏆 LEVEL {player['level']} PROGRESS
        </b>

        <br><br>

        ⭐ {player['xp']} / {required} XP

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.markdown(
        '<div class="section-title">'
        '🔥 ENTER THE ARENA'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="game-card">

                <div style="font-size:45px;">
                📚
                </div>

                <div class="game-title">
                STUDY
                </div>

                <div class="game-description">
                Turn learning into games.
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

                <div style="font-size:45px;">
                ⚔️
                </div>

                <div class="game-title">
                CHALLENGES
                </div>

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

                <div style="font-size:45px;">
                🌙
                </div>

                <div class="game-title">
                CHILL
                </div>

                <div class="game-description">
                Take a break from the arena.
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
# STUDY
# ============================================================

def study_page():

    show_title()

    st.markdown(
        '<div class="section-title">'
        '📚 STUDY ARENA'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Choose your learning game."
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
            "Grammar and vocabulary.",
            "hindi"
        ),

        (
            "🇬🇧",
            "WORD BATTLE",
            "Battle your way through English.",
            "english"
        )

    ]

    for row in range(
        0,
        len(games),
        2
    ):

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

                        <div style="font-size:45px;">
                        {icon}
                        </div>

                        <div class="game-title">
                        {name}
                        </div>

                        <div class="game-description">
                        {description}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"PLAY {name}",
                    key=f"play_{game_id}",
                    use_container_width=True
                ):

                    st.session_state.game = game_id

                    st.session_state.current_question = random.choice(
                        QUESTIONS[game_id]
                    )

                    st.session_state.page = "game"

                    st.rerun()


# ============================================================
# QUESTIONS
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
            [
                "Oxygen",
                "Carbon dioxide",
                "Nitrogen",
                "Hydrogen"
            ],
            "Carbon dioxide"
        ),

        (
            "What is the boiling point of water at sea level?",
            [
                "50°C",
                "75°C",
                "100°C",
                "150°C"
            ],
            "100°C"
        )

    ],

    "sst": [

        (
            "Which is a major landform of India?",
            [
                "Mountains",
                "Moon",
                "Asteroid",
                "Comet"
            ],
            "Mountains"
        ),

        (
            "Which institution makes laws in a democracy?",
            [
                "Legislature",
                "Hospital",
                "Museum",
                "Bank"
            ],
            "Legislature"
        )

    ],

    "hindi": [

        (
            "‘दिन’ का विलोम शब्द क्या है?",
            [
                "सुबह",
                "रात",
                "दोपहर",
                "समय"
            ],
            "रात"
        ),

        (
            "‘जल’ का पर्यायवाची शब्द क्या है?",
            [
                "आकाश",
                "पानी",
                "अग्नि",
                "वायु"
            ],
            "पानी"
        )

    ],

    "english": [

        (
            "Choose the correct plural of 'child'.",
            [
                "Childs",
                "Children",
                "Childes",
                "Childrens"
            ],
            "Children"
        ),

        (
            "Which word is an adjective?",
            [
                "Run",
                "Beautiful",
                "Quickly",
                "Jump"
            ],
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
# GAME
# ============================================================

def game_page():

    show_title()

    game = st.session_state.game

    st.markdown(
        f"""
        <div class="section-title">
        {GAME_NAMES[game]}
        </div>
        """,
        unsafe_allow_html=True
    )

    question, options, answer = (
        st.session_state.current_question
    )

    st.markdown(
        f"""
        <div class="card">

        <h2>
        {question}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    for i, option in enumerate(options):

        if st.button(
            option,
            key=f"answer_{game}_{i}",
            use_container_width=True
        ):

            if option == answer:

                st.success(
                    "✅ CORRECT!  +50 XP  +5 AURA"
                )

                add_rewards(
                    50,
                    5
                )

                st.session_state.current_question = random.choice(
                    QUESTIONS[game]
                )

                st.rerun()

            else:

                st.error(
                    f"❌ Wrong! Correct answer: {answer}"
                )

    st.write("")

    if st.button(
        "← BACK TO STUDY",
        use_container_width=True
    ):

        st.session_state.current_question = None

        st.session_state.page = "study"

        st.rerun()


# ============================================================
# CHALLENGES
# ============================================================

def challenges_page():

    show_title()

    st.markdown(
        '<div class="section-title">'
        '⚔️ DAILY CHALLENGES'
        '</div>',
        unsafe_allow_html=True
    )

    challenges = [

        (
            "⭐ KNOWLEDGE WARRIOR",
            "Answer a study question.",
            100,
            10
        ),

        (
            "🔥 ARENA EXPLORER",
            "Complete one study game.",
            75,
            5
        ),

        (
            "🧠 BRAIN MASTER",
            "Complete a challenge.",
            125,
            15
        )

    ]

    for i, (
        name,
        description,
        xp,
        aura
    ) in enumerate(challenges):

        st.markdown(
            f"""
            <div class="card">

            <h3>
            {name}
            </h3>

            <p>
            {description}
            </p>

            <b>
            ⭐ +{xp} XP
            &nbsp;&nbsp;
            ✨ +{aura} Aura
            </b>

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

            add_rewards(
                xp,
                aura
            )

            st.success(
                f"🔥 Challenge completed! "
                f"+{xp} XP and +{aura} Aura!"
            )


# ============================================================
# PROFILE
# ============================================================

def profile_page():

    show_title()

    st.markdown(
        '<div class="section-title">'
        '👤 YOUR PROFILE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">

        <h2>
        👤 {player['name']}
        </h2>

        <p>
        🎓 Grade {player['grade']}
        </p>

        <hr>

        <p>
        🏆 Level: {player['level']}
        </p>

        <p>
        ⭐ XP: {player['xp']}
        </p>

        <p>
        ✨ Aura: {player['aura']}
        </p>

        <p>
        ⚔️ Challenges Completed:
        {player['challenges_completed']}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RANKS
# ============================================================

def ranks_page():

    show_title()

    st.markdown(
        '<div class="section-title">'
        '🏆 RANKS'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card"
             style="text-align:center;">

        <h1>
        🏆 LEVEL {player['level']}
        </h1>

        <h2>
        ⭐ {player['xp']} XP
        </h2>

        <h2>
        ✨ {player['aura']} AURA
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "🌐 Online leaderboards can be added later."
    )


# ============================================================
# CHILL
# ============================================================

def chill_page():

    show_title()

    st.markdown(
        '<div class="section-title">'
        '🌙 CHILL ZONE'
        '</div>',
        unsafe_allow_html=True
    )

    quotes = [

        "Small progress is still progress. 🌱",

        "Rest. Reset. Return stronger. 🌙",

        "Your mind is your greatest arena. 🧠",

        "One challenge at a time. ⚔️",

        "You don't have to be perfect. "
        "Just keep learning. ✨"

    ]

    st.markdown(
        f"""
        <div class="card"
             style="text-align:center;">

        <div style="font-size:75px;">
        🌌
        </div>

        <h2>
        {random.choice(quotes)}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "✨ ANOTHER THOUGHT",
        use_container_width=True
    ):

        st.rerun()


# ============================================================
# APP ROUTER
# ============================================================

if player["name"] == "":

    setup_page()

else:

    show_sidebar()

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
