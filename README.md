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
# PLAYER DATA
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
            with open(SAVE_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_DATA.copy()

    return DEFAULT_DATA.copy()


def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump(st.session_state.player, f, indent=4)


if "player" not in st.session_state:
    st.session_state.player = load_data()

if "page" not in st.session_state:
    st.session_state.page = "home"

if "subject" not in st.session_state:
    st.session_state.subject = None

if "division" not in st.session_state:
    st.session_state.division = None

if "topic" not in st.session_state:
    st.session_state.topic = None

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "game_active" not in st.session_state:
    st.session_state.game_active = False

player = st.session_state.player


# ============================================================
# XP SYSTEM
# ============================================================

def xp_needed():
    return player["level"] * 100


def add_rewards(xp, aura):

    player["xp"] += xp
    player["aura"] += aura

    level_up = False

    while player["xp"] >= xp_needed():
        player["xp"] -= xp_needed()
        player["level"] += 1
        level_up = True

    save_data()

    if level_up:
        st.balloons()
        st.success(
            f"🔥 LEVEL UP! You reached Level {player['level']}!"
        )


# ============================================================
# BACKGROUND
# ============================================================

def get_background():

    if not os.path.exists(BACKGROUND_IMAGE):
        return ""

    try:
        with open(BACKGROUND_IMAGE, "rb") as f:
            return base64.b64encode(f.read()).decode()

    except:
        return ""


background = get_background()

if background:

    background_css = f"""
    background-image:
    linear-gradient(
        rgba(3, 25, 70, 0.35),
        rgba(2, 20, 55, 0.75)
    ),
    url("data:image/jpeg;base64,{background}");
    """

else:

    background_css = """
    background-image:
    radial-gradient(
        circle at top,
        #1768b8,
        #0b4385 40%,
        #041d42 75%,
        #02142e
    );
    """


# ============================================================
# DESIGN
# ============================================================

st.markdown(
    f"""
<style>

.stApp {{
    {background_css}
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}}

.block-container {{
    max-width: 1250px;
    padding-top: 25px;
}}

.aom-title {{
    text-align: center;
    font-family: "Comic Sans MS", "Trebuchet MS", sans-serif;
    font-size: 58px;
    font-weight: 900;
    color: white;
    letter-spacing: 4px;
    text-shadow:
        4px 4px 0 #0755b8,
        0 0 15px #39a9ff,
        0 0 30px #0077ff;
    animation: bounce 2s infinite;
}}

@keyframes bounce {{
    0%, 100% {{
        transform: translateY(0) rotate(-1deg);
    }}
    50% {{
        transform: translateY(-7px) rotate(1deg);
    }}
}}

.aom-subtitle {{
    text-align: center;
    color: #bde4ff;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 6px;
    margin-bottom: 30px;
}}

.section-title {{
    text-align: center;
    font-family: "Comic Sans MS", "Trebuchet MS", sans-serif;
    font-size: 34px;
    font-weight: 900;
    color: white;
    text-shadow:
        3px 3px 0 #0755b8,
        0 0 15px #1e9bff;
    margin: 25px 0;
}}

.card {{
    background:
        linear-gradient(
            145deg,
            rgba(5, 35, 80, 0.94),
            rgba(8, 70, 140, 0.94)
        );
    border: 1px solid rgba(80, 190, 255, 0.6);
    border-radius: 22px;
    padding: 25px;
    margin: 10px 0;
    box-shadow: 0 10px 35px rgba(0, 80, 180, 0.4);
}}

.stat {{
    background:
        linear-gradient(
            145deg,
            rgba(5, 38, 85, 0.96),
            rgba(8, 70, 140, 0.96)
        );
    border: 1px solid rgba(80, 190, 255, 0.6);
    border-radius: 20px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0, 80, 180, 0.35);
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
    text-shadow: 0 0 12px #168fff;
}}

.game-card {{
    background:
        linear-gradient(
            145deg,
            rgba(5, 35, 80, 0.96),
            rgba(9, 67, 135, 0.96)
        );
    border: 1px solid rgba(60, 175, 255, 0.6);
    border-radius: 24px;
    padding: 25px;
    text-align: center;
    min-height: 150px;
    box-shadow: 0 10px 30px rgba(0, 60, 150, 0.4);
}}

.game-title {{
    font-size: 21px;
    font-weight: 900;
    color: white;
}}

.game-description {{
    color: #b8dcff;
    font-size: 13px;
    margin-top: 8px;
}}

.stButton > button {{
    border-radius: 14px;
    border: 1px solid rgba(70, 180, 255, 0.7);
    background:
        linear-gradient(
            135deg,
            #0755b8,
            #087bd1
        );
    color: white;
    font-weight: 900;
    min-height: 45px;
}}

.stButton > button:hover {{
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 140, 255, 0.5);
}}

.stTextInput input {{
    background: rgba(5, 30, 70, 0.95);
    color: white;
    border: 1px solid #237bc7;
    border-radius: 12px;
}}

section[data-testid="stSidebar"] {{
    background:
        linear-gradient(
            180deg,
            rgba(3, 25, 58, 0.98),
            rgba(3, 50, 100, 0.98)
        );
}}

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
        """<div class="aom-title">⚔️ ARENA OF MINDS ⚔️</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<div class="aom-subtitle">LEARN • CHALLENGE • CONQUER</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# STUDY STRUCTURE
# ============================================================

STUDY_STRUCTURE = {

    "📐 MATHS": {

        "🔢 Arithmetic": [
            "Integers",
            "Fractions",
            "Decimals",
            "Percentages",
            "Ratio & Proportion",
            "Profit & Loss",
            "Simple Interest"
        ],

        "✖️ Algebra": [
            "Expressions",
            "Variables",
            "Simple Equations",
            "Patterns",
            "Exponents"
        ],

        "📐 Geometry": [
            "Lines & Angles",
            "Triangles",
            "Quadrilaterals",
            "Circles",
            "Symmetry"
        ],

        "📏 Mensuration": [
            "Perimeter",
            "Area",
            "Volume",
            "Units of Measurement"
        ],

        "📊 Data Handling": [
            "Tables",
            "Bar Graphs",
            "Pie Charts",
            "Mean",
            "Median",
            "Mode"
        ]

    },


    "🔬 SCIENCE": {

        "⚙️ Physics": [
            "Motion",
            "Force",
            "Work & Energy",
            "Light",
            "Heat",
            "Electricity",
            "Magnets"
        ],

        "🧪 Chemistry": [
            "Matter",
            "Acids, Bases & Salts",
            "Physical & Chemical Changes",
            "Separation of Substances",
            "Atoms & Molecules",
            "Materials"
        ],

        "🧬 Biology": [
            "Plants",
            "Animals",
            "Human Body",
            "Nutrition",
            "Respiration",
            "Reproduction",
            "Microorganisms"
        ],

        "🌍 Earth & Environment": [
            "Earth",
            "Water",
            "Air",
            "Natural Resources",
            "Pollution",
            "Climate",
            "Conservation"
        ]

    },


    "🌍 SST": {

        "🏛️ History": [
            "Early Civilisations",
            "New Beginnings: Cities & States",
            "Empires",
            "Medieval India",
            "Colonial India",
            "Indian Freedom Movement"
        ],

        "🗺️ Geography": [
            "Geographical Diversity of India",
            "Landforms",
            "Climate",
            "Natural Vegetation",
            "Resources",
            "Agriculture",
            "Maps"
        ],

        "⚖️ Civics": [
            "Democracy",
            "Government",
            "Constitution",
            "Rights & Duties",
            "Local Government",
            "Elections",
            "Equality"
        ],

        "💰 Economics": [
            "Markets",
            "Money",
            "Resources",
            "Production",
            "Consumers"
        ]

    },


    "🇬🇧 ENGLISH": {

        "📖 Literature": [
            "Stories",
            "Poetry",
            "Characters",
            "Themes",
            "Literary Devices"
        ],

        "✍️ Grammar": [
            "Nouns",
            "Pronouns",
            "Verbs",
            "Adjectives",
            "Adverbs",
            "Tenses",
            "Prepositions",
            "Conjunctions",
            "Sentences"
        ],

        "📝 Writing": [
            "Story Writing",
            "Letter Writing",
            "Diary Entry",
            "Paragraph Writing",
            "Article Writing"
        ],

        "📚 Vocabulary": [
            "Synonyms",
            "Antonyms",
            "Homophones",
            "Idioms",
            "Prefixes & Suffixes"
        ],

        "🔍 Reading": [
            "Comprehension",
            "Inference",
            "Main Idea",
            "Vocabulary in Context"
        ]

    },


    "🇮🇳 HINDI": {

        "📖 साहित्य": [
            "कहानी",
            "कविता",
            "पात्र",
            "भावार्थ",
            "संदेश"
        ],

        "✍️ व्याकरण": [
            "संज्ञा",
            "सर्वनाम",
            "विशेषण",
            "क्रिया",
            "काल",
            "वचन",
            "लिंग",
            "वाक्य"
        ],

        "📝 लेखन": [
            "निबंध",
            "पत्र लेखन",
            "अनुच्छेद",
            "कहानी लेखन",
            "संवाद लेखन"
        ],

        "📚 शब्द भंडार": [
            "पर्यायवाची शब्द",
            "विलोम शब्द",
            "अनेक शब्दों के लिए एक शब्द",
            "मुहावरे",
            "अनेकार्थी शब्द"
        ],

        "📜 पठन": [
            "अपठित गद्यांश",
            "अपठित पद्यांश",
            "प्रश्न उत्तर",
            "शब्दार्थ"
        ]

    }

}


# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = {

    "Integers": [
        (
            "What is -8 + 13?",
            ["3", "5", "-5", "21"],
            "5"
        ),
        (
            "What is 7 - 12?",
            ["5", "-5", "19", "-19"],
            "-5"
        )
    ],

    "Fractions": [
        (
            "What is 1/2 + 1/2?",
            ["1", "1/2", "2", "0"],
            "1"
        )
    ],

    "Decimals": [
        (
            "What is 2.5 + 1.5?",
            ["3", "4", "4.5", "5"],
            "4"
        )
    ],

    "Percentages": [
        (
            "What is 25% of 100?",
            ["10", "20", "25", "50"],
            "25"
        )
    ],

    "Simple Equations": [
        (
            "If x + 5 = 12, what is x?",
            ["5", "6", "7", "8"],
            "7"
        )
    ],

    "Lines & Angles": [
        (
            "How many degrees are in a right angle?",
            ["45°", "90°", "180°", "360°"],
            "90°"
        )
    ],

    "Area": [
        (
            "What is the area of a square with side 5 cm?",
            ["10 cm²", "20 cm²", "25 cm²", "30 cm²"],
            "25 cm²"
        )
    ],

    "Motion": [
        (
            "Which instrument is commonly used to measure time?",
            ["Ruler", "Clock", "Thermometer", "Balance"],
            "Clock"
        )
    ],

    "Force": [
        (
            "A push or pull is called what?",
            ["Energy", "Force", "Motion", "Heat"],
            "Force"
        )
    ],

    "Light": [
        (
            "Which object produces its own light?",
            ["Moon", "Mirror", "Sun", "Book"],
            "Sun"
        )
    ],

    "Heat": [
        (
            "Which instrument measures temperature?",
            ["Barometer", "Thermometer", "Ammeter", "Ruler"],
            "Thermometer"
        )
    ],

    "Acids, Bases & Salts": [
        (
            "Which substance is acidic?",
            ["Lemon juice", "Soap solution", "Baking soda", "Toothpaste"],
            "Lemon juice"
        )
    ],

    "Plants": [
        (
            "Which part of a plant usually absorbs water?",
            ["Flower", "Root", "Fruit", "Leaf"],
            "Root"
        )
    ],

    "Animals": [
        (
            "Which animal is a mammal?",
            ["Frog", "Dolphin", "Lizard", "Fish"],
            "Dolphin"
        )
    ],

    "Human Body": [
        (
            "Which organ pumps blood around the body?",
            ["Lungs", "Brain", "Heart", "Stomach"],
            "Heart"
        )
    ],

    "Geographical Diversity of India": [
        (
            "Which is a major physical division of India?",
            ["Himalayas", "Atlantic Ocean", "Sahara Desert", "Alps"],
            "Himalayas"
        )
    ],

    "Landforms": [
        (
            "Which landform is generally higher and steeper than a hill?",
            ["Plain", "Mountain", "Valley", "Delta"],
            "Mountain"
        )
    ],

    "Climate": [
        (
            "Which factor strongly affects the climate of a place?",
            ["Latitude", "Alphabet", "Population name", "Language"],
            "Latitude"
        )
    ],

    "Natural Vegetation": [
        (
            "What does natural vegetation mean?",
            [
                "Plants grown naturally",
                "Only garden plants",
                "Plastic plants",
                "Artificial flowers"
            ],
            "Plants grown naturally"
        )
    ],

    "Democracy": [
        (
            "What is an important feature of democracy?",
            [
                "People choose representatives",
                "One person controls everything",
                "No elections",
                "No laws"
            ],
            "People choose representatives"
        )
    ],

    "Constitution": [
        (
            "What is a constitution?",
            [
                "A set of fundamental rules",
                "A storybook",
                "A map",
                "A timetable"
            ],
            "A set of fundamental rules"
        )
    ],

    "Rights & Duties": [
        (
            "What are rights?",
            [
                "Freedoms and protections",
                "Only punishments",
                "School subjects",
                "Maps"
            ],
            "Freedoms and protections"
        )
    ],

    "Nouns": [
        (
            "Which word is a noun?",
            ["Run", "Beautiful", "Teacher", "Quickly"],
            "Teacher"
        )
    ],

    "Verbs": [
        (
            "Which word is a verb?",
            ["Jump", "Blue", "Table", "Happy"],
            "Jump"
        )
    ],

    "Adjectives": [
        (
            "Which word is an adjective?",
            ["Run", "Beautiful", "Quickly", "Jump"],
            "Beautiful"
        )
    ],

    "Tenses": [
        (
            "Which sentence is in the past tense?",
            [
                "I eat food.",
                "I am eating food.",
                "I ate food.",
                "I will eat food."
            ],
            "I ate food."
        )
    ],

    "Synonyms": [
        (
            "Which word is a synonym of 'happy'?",
            ["Sad", "Joyful", "Angry", "Tired"],
            "Joyful"
        )
    ],

    "Antonyms": [
        (
            "What is the opposite of 'ancient'?",
            ["Old", "Modern", "Historic", "Past"],
            "Modern"
        )
    ],

    "संज्ञा": [
        (
            "‘राम विद्यालय जाता है।’ इसमें संज्ञा शब्द कौन-सा है?",
            ["जाता", "विद्यालय", "है", "का"],
            "विद्यालय"
        )
    ],

    "सर्वनाम": [
        (
            "‘वह स्कूल गया।’ इसमें सर्वनाम कौन-सा है?",
            ["स्कूल", "गया", "वह", "कोई नहीं"],
            "वह"
        )
    ],

    "विशेषण": [
        (
            "‘सुंदर फूल खिला।’ इसमें विशेषण कौन-सा है?",
            ["फूल", "सुंदर", "खिला", "कोई नहीं"],
            "सुंदर"
        )
    ],

    "क्रिया": [
        (
            "‘बच्चा खेल रहा है।’ इसमें क्रिया कौन-सी है?",
            ["बच्चा", "खेल रहा है", "है", "कोई नहीं"],
            "खेल रहा है"
        )
    ],

    "पर्यायवाची शब्द": [
        (
            "‘जल’ का पर्यायवाची शब्द क्या है?",
            ["अग्नि", "पानी", "आकाश", "वायु"],
            "पानी"
        )
    ],

    "विलोम शब्द": [
        (
            "‘दिन’ का विलोम शब्द क्या है?",
            ["सुबह", "रात", "दोपहर", "समय"],
            "रात"
        )
    ]

}


# ============================================================
# SETUP PAGE
# ============================================================

def setup_page():

    show_title()

    st.markdown(
        """<div class="section-title">
WELCOME, FUTURE CHAMPION
</div>""",
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            """<div class="card" style="text-align:center;">
<div style="font-size:60px;">🌙</div>
<h2>ENTER THE ARENA</h2>
<p>Begin your journey.</p>
</div>""",
            unsafe_allow_html=True
        )

        name = st.text_input("👤 What's your name?")

        grade = st.text_input("🎓 What's your grade?")

        if st.button(
            "⚔️ START YOUR JOURNEY",
            use_container_width=True
        ):

            if not name.strip():

                st.warning("Please enter your name.")

            elif not grade.strip():

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

def show_sidebar():

    with st.sidebar:

        st.markdown(
            """<div style="
text-align:center;
font-size:27px;
font-weight:900;
color:#55baff;
text-shadow:0 0 12px #008cff;
">⚔️ ARENA</div>""",
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

        buttons = [
            ("🏠 HOME", "home"),
            ("📚 STUDY", "study"),
            ("⚔️ CHALLENGES", "challenges"),
            ("🏆 RANKS", "ranks"),
            ("👤 PROFILE", "profile"),
            ("🌙 CHILL", "chill")
        ]

        for label, page in buttons:

            if st.button(
                label,
                use_container_width=True
            ):

                st.session_state.page = page

                st.session_state.subject = None
                st.session_state.division = None
                st.session_state.topic = None

                st.rerun()

        st.divider()

        st.caption(f"⭐ XP: {player['xp']}")
        st.caption(f"✨ Aura: {player['aura']}")
        st.caption(f"🏆 Level: {player['level']}")


# ============================================================
# HOME
# ============================================================

def home_page():

    show_title()

    st.markdown(
        f"""<div class="card">
<h2>Welcome, {player['name']}! 👋</h2>
<p>🎓 Grade {player['grade']} &nbsp; • &nbsp; 🏆 Level {player['level']}</p>
</div>""",
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""<div class="stat">
<div class="stat-title">⭐ XP</div>
<div class="stat-value">{player['xp']}</div>
</div>""",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""<div class="stat">
<div class="stat-title">✨ AURA</div>
<div class="stat-value">{player['aura']}</div>
</div>""",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""<div class="stat">
<div class="stat-title">🏆 LEVEL</div>
<div class="stat-value">{player['level']}</div>
</div>""",
            unsafe_allow_html=True
        )

    st.write("")

    required = xp_needed()

    st.markdown(
        f"""<div class="card">
<b>🏆 LEVEL {player['level']} PROGRESS</b>
<br><br>
⭐ {player['xp']} / {required} XP
</div>""",
        unsafe_allow_html=True
    )

    st.progress(
        player["xp"] / required
    )

    st.markdown(
        """<div class="section-title">
🔥 ENTER THE ARENA
</div>""",
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """<div class="game-card">
<div style="font-size:45px;">📚</div>
<div class="game-title">STUDY</div>
<div class="game-description">Choose subjects, divisions and topics.</div>
</div>""",
            unsafe_allow_html=True
        )

        if st.button(
            "ENTER STUDY",
            use_container_width=True
        ):

            st.session_state.page = "study"
            st.rerun()

    with c2:

        st.markdown(
            """<div class="game-card">
<div style="font-size:45px;">⚔️</div>
<div class="game-title">CHALLENGES</div>
<div class="game-description">Complete challenges and earn rewards.</div>
</div>""",
            unsafe_allow_html=True
        )

        if st.button(
            "VIEW CHALLENGES",
            use_container_width=True
        ):

            st.session_state.page = "challenges"
            st.rerun()

    with c3:

        st.markdown(
            """<div class="game-card">
<div style="font-size:45px;">🌙</div>
<div class="game-title">CHILL</div>
<div class="game-description">Take a break from the arena.</div>
</div>""",
            unsafe_allow_html=True
        )

        if st.button(
            "ENTER CHILL",
            use_container_width=True
        ):

            st.session_state.page = "chill"
            st.rerun()


# ============================================================
# STUDY PAGE
# ============================================================

def study_page():

    show_title()

    # --------------------------------------------------------
    # SUBJECT SELECTION
    # --------------------------------------------------------

    if st.session_state.subject is None:

        st.markdown(
            """<div class="section-title">
📚 CHOOSE YOUR SUBJECT
</div>""",
            unsafe_allow_html=True
        )

        st.write(
            "Choose a subject to enter its arena."
        )

        subjects = list(STUDY_STRUCTURE.keys())

        for row in range(0, len(subjects), 2):

            cols = st.columns(2)

            for i, col in enumerate(cols):

                index = row + i

                if index >= len(subjects):
                    break

                subject = subjects[index]

                with col:

                    st.markdown(
                        f"""<div class="game-card">
<div style="font-size:48px;">{subject.split()[0]}</div>
<div class="game-title">
{" ".join(subject.split()[1:])}
</div>
<div class="game-description">
Enter the {subject} arena
</div>
</div>""",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"ENTER {subject}",
                        key=f"subject_{index}",
                        use_container_width=True
                    ):

                        st.session_state.subject = subject
                        st.session_state.division = None
                        st.session_state.topic = None

                        st.rerun()

        return

    # --------------------------------------------------------
    # DIVISION SELECTION
    # --------------------------------------------------------

    subject = st.session_state.subject

    if st.session_state.division is None:

        st.markdown(
            f"""<div class="section-title">
{subject} • CHOOSE YOUR DIVISION
</div>""",
            unsafe_allow_html=True
        )

        if st.button(
            "← BACK TO SUBJECTS",
            use_container_width=True
        ):

            st.session_state.subject = None
            st.rerun()

        divisions = list(
            STUDY_STRUCTURE[subject].keys()
        )

        for row in range(0, len(divisions), 2):

            cols = st.columns(2)

            for i, col in enumerate(cols):

                index = row + i

                if index >= len(divisions):
                    break

                division = divisions[index]

                topics_count = len(
                    STUDY_STRUCTURE[subject][division]
                )

                with col:

                    st.markdown(
                        f"""<div class="game-card">
<div style="font-size:45px;">
{division.split()[0]}
</div>
<div class="game-title">
{" ".join(division.split()[1:])}
</div>
<div class="game-description">
{topics_count} topics available
</div>
</div>""",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"ENTER {division}",
                        key=f"division_{index}",
                        use_container_width=True
                    ):

                        st.session_state.division = division
                        st.session_state.topic = None

                        st.rerun()

        return

    # --------------------------------------------------------
    # TOPIC SELECTION
    # --------------------------------------------------------

    division = st.session_state.division

    if st.session_state.topic is None:

        st.markdown(
            f"""<div class="section-title">
{division} • CHOOSE A TOPIC
</div>""",
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "← BACK TO DIVISIONS",
                use_container_width=True
            ):

                st.session_state.division = None
                st.rerun()

        with c2:

            if st.button(
                "🏠 SUBJECTS",
                use_container_width=True
            ):

                st.session_state.subject = None
                st.session_state.division = None
                st.rerun()

        topics = STUDY_STRUCTURE[
            subject
        ][division]

        st.write("")

        for row in range(0, len(topics), 2):

            cols = st.columns(2)

            for i, col in enumerate(cols):

                index = row + i

                if index >= len(topics):
                    break

                topic = topics[index]

                with col:

                    st.markdown(
                        f"""<div class="game-card">
<div style="font-size:40px;">🔥</div>
<div class="game-title">{topic}</div>
<div class="game-description">
Test your knowledge
</div>
</div>""",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"START {topic}",
                        key=f"topic_{index}",
                        use_container_width=True
                    ):

                        st.session_state.topic = topic

                        if topic in QUESTION_BANK:

                            st.session_state.current_question = random.choice(
                                QUESTION_BANK[topic]
                            )

                            st.session_state.game_active = True
                            st.session_state.page = "quiz"

                        else:

                            st.session_state.game_active = False

                        st.rerun()

        return


# ============================================================
# QUIZ
# ============================================================

def quiz_page():

    topic = st.session_state.topic

    show_title()

    st.markdown(
        f"""<div class="section-title">
🔥 {topic.upper()}
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""<div class="card">
<b>📚 {st.session_state.subject}</b>
<br>
⚔️ {st.session_state.division}
<br><br>
🔥 Topic: <b>{topic}</b>
<br><br>
⭐ Correct answer = +50 XP
<br>
✨ Correct answer = +5 Aura
</div>""",
        unsafe_allow_html=True
    )

    if not st.session_state.game_active:

        st.warning(
            "This topic is ready for questions! "
            "More questions will be added here."
        )

        if st.button(
            "← BACK TO TOPICS",
            use_container_width=True
        ):

            st.session_state.topic = None
            st.session_state.page = "study"

            st.rerun()

        return

    question, options, answer = (
        st.session_state.current_question
    )

    st.markdown(
        f"""<div class="card">
<h2>{question}</h2>
</div>""",
        unsafe_allow_html=True
    )

    for i, option in enumerate(options):

        if st.button(
            option,
            key=f"answer_{topic}_{i}",
            use_container_width=True
        ):

            if option == answer:

                add_rewards(
                    50,
                    5
                )

                st.success(
                    "✅ CORRECT! +50 XP • +5 AURA"
                )

                st.session_state.current_question = random.choice(
                    QUESTION_BANK[topic]
                )

                st.rerun()

            else:

                st.error(
                    f"❌ Not quite! Correct answer: {answer}"
                )

    st.write("")

    if st.button(
        "← BACK TO TOPICS",
        use_container_width=True
    ):

        st.session_state.topic = None
        st.session_state.game_active = False
        st.session_state.page = "study"

        st.rerun()


# ============================================================
# CHALLENGES
# ============================================================

def challenges_page():

    show_title()

    st.markdown(
        """<div class="section-title">
⚔️ DAILY CHALLENGES
</div>""",
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
            "Explore a new subject.",
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

    for i, challenge in enumerate(challenges):

        name, description, xp, aura = challenge

        st.markdown(
            f"""<div class="card">
<h3>{name}</h3>
<p>{description}</p>
<b>⭐ +{xp} XP &nbsp;&nbsp; ✨ +{aura} Aura</b>
</div>""",
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
                f"🔥 Challenge completed! +{xp} XP • +{aura} Aura"
            )


# ============================================================
# PROFILE
# ============================================================

def profile_page():

    show_title()

    st.markdown(
        """<div class="section-title">
👤 YOUR PROFILE
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""<div class="card">
<h2>👤 {player['name']}</h2>
<p>🎓 Grade {player['grade']}</p>
<hr>
<p>🏆 Level: {player['level']}</p>
<p>⭐ XP: {player['xp']}</p>
<p>✨ Aura: {player['aura']}</p>
<p>⚔️ Challenges Completed:
{player['challenges_completed']}</p>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# RANKS
# ============================================================

def ranks_page():

    show_title()

    st.markdown(
        """<div class="section-title">
🏆 RANKS
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""<div class="card" style="text-align:center;">
<h1>🏆 LEVEL {player['level']}</h1>
<h2>⭐ {player['xp']} XP</h2>
<h2>✨ {player['aura']} AURA</h2>
</div>""",
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
        """<div class="section-title">
🌙 CHILL ZONE
</div>""",
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
        f"""<div class="card" style="text-align:center;">
<div style="font-size:75px;">🌌</div>
<h2>{random.choice(quotes)}</h2>
</div>""",
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

    elif st.session_state.page == "quiz":
        quiz_page()

    elif st.session_state.page == "challenges":
        challenges_page()

    elif st.session_state.page == "profile":
        profile_page()

    elif st.session_state.page == "ranks":
        ranks_page()

    elif st.session_state.page == "chill":
        chill_page()
