import streamlit as st
import random

# =========================================================
# ARENA OF MINDS
# =========================================================

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="⚔️",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "name": "",
    "grade": "",
    "xp": 0,
    "aura": 0,
    "page": "home",
    "subject": None,
    "division": None,
    "topic": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top,
            #0b5ed7 0%,
            #063b82 35%,
            #021a3d 75%,
            #010b1c 100%
        );
    color: white;
}

.block-container {
    padding-top: 25px;
    max-width: 1200px;
}

h1, h2, h3, p, label {
    color: white !important;
}

.aom-title {
    text-align: center;
    font-family: "Comic Sans MS", cursive;
    font-size: 55px;
    font-weight: bold;
    color: white;
    text-shadow:
        4px 4px 0px #0755b8,
        0px 0px 18px #24a8ff;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%,100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-7px);
    }
}

.subtitle {
    text-align: center;
    color: #a9ddff !important;
    letter-spacing: 5px;
    font-weight: bold;
}

.section-title {
    text-align: center;
    font-family: "Comic Sans MS", cursive;
    font-size: 35px;
    font-weight: bold;
    margin: 25px 0px;
    text-shadow: 3px 3px 0px #0755b8;
}

.card {
    background: rgba(4, 42, 91, 0.94);
    border: 1px solid #218cff;
    border-radius: 20px;
    padding: 25px;
    margin: 12px 0px;
    box-shadow: 0px 8px 25px rgba(0, 120, 255, 0.25);
}

.stat {
    background: rgba(4, 42, 91, 0.95);
    border: 1px solid #218cff;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

.stat-number {
    font-size: 32px;
    font-weight: bold;
}

.stat-label {
    color: #9ddaff !important;
    font-weight: bold;
}

.stButton > button {
    background: linear-gradient(135deg, #0755b8, #087bd1);
    color: white !important;
    border: 1px solid #48b5ff;
    border-radius: 13px;
    font-weight: bold;
    min-height: 45px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #087bd1, #0b96ed);
    box-shadow: 0px 0px 15px #168fff;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

def show_title():
    st.markdown(
        '<div class="aom-title">⚔️ ARENA OF MINDS ⚔️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">LEARN • CHALLENGE • CONQUER</div>',
        unsafe_allow_html=True
    )


# =========================================================
# CLASS 7 STUDY DATABASE
#
# STRUCTURE:
#
# SUBJECT
#     ↓
# DIVISION
#     ↓
# CHAPTER
#     ↓
# CHALLENGE
# =========================================================

study = {

    # =====================================================
    # MATHEMATICS
    # =====================================================

    "📐 Mathematics": {

        "🔢 Number System": [
            "Integers",
            "Fractions",
            "Decimals"
        ],

        "📊 Ratio, Percentage & Data": [
            "Ratio and Proportion",
            "Percentage",
            "Data Handling"
        ],

        "✖️ Algebra": [
            "Algebraic Expressions",
            "Simple Equations",
            "Patterns"
        ],

        "📐 Geometry": [
            "Lines and Angles",
            "Triangles",
            "Symmetry"
        ],

        "📏 Mensuration": [
            "Perimeter",
            "Area",
            "Measurement"
        ]
    },


    # =====================================================
    # SCIENCE
    # =====================================================

    "🔬 Science": {

        "⚙️ Physics": [
            "Measurement of Time and Motion",
            "Light",
            "Heat",
            "Electricity",
            "Magnets",
            "Force and Motion"
        ],

        "🧪 Chemistry": [
            "Acids, Bases and Neutral",
            "Physical and Chemical Changes",
            "Matter",
            "Separation of Substances"
        ],

        "🧬 Biology": [
            "Plants",
            "Animals",
            "Nutrition",
            "Respiration",
            "Human Body",
            "Microorganisms"
        ],

        "🌱 Environment": [
            "Air",
            "Water",
            "Natural Resources",
            "Natural Vegetation",
            "Conservation"
        ]
    },


    # =====================================================
    # SOCIAL SCIENCE
    # =====================================================

    "🌍 Social Science": {

        "🏛️ History": [
            "New Beginnings: Cities and Empires",
            "Early Cities and States",
            "Empires",
            "Medieval India",
            "Colonial India",
            "The Indian Freedom Movement"
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
            "Equality",
            "Rights and Duties",
            "Local Government",
            "Elections"
        ],

        "💰 Economics": [
            "Markets",
            "Money",
            "Resources",
            "Production",
            "Consumers"
        ]
    },


    # =====================================================
    # ENGLISH
    # =====================================================

    "🇬🇧 English": {

        "📖 Literature": [
            "The Fun They Had",
            "Pierce Arrow",
            "Stories and Characters",
            "Poetry",
            "Themes and Messages"
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
            "Paragraph Writing",
            "Story Writing",
            "Letter Writing",
            "Diary Entry",
            "Article Writing"
        ],

        "📚 Vocabulary": [
            "Synonyms",
            "Antonyms",
            "Homophones",
            "Idioms"
        ],

        "🔍 Reading": [
            "Reading Comprehension",
            "Main Idea",
            "Inference",
            "Vocabulary in Context"
        ]
    },


    # =====================================================
    # HINDI
    # =====================================================

    "🇮🇳 Hindi": {

        "📖 पाठ / साहित्य": [
            "सदर नमन",
            "यह मेरा यह मीत का",
            "मिठाईवाला"
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
            "निबंध लेखन",
            "पत्र लेखन",
            "अनुच्छेद लेखन",
            "कहानी लेखन",
            "संवाद लेखन"
        ],

        "📚 शब्द भंडार": [
            "पर्यायवाची शब्द",
            "विलोम शब्द",
            "मुहावरे",
            "अनेक शब्दों के लिए एक शब्द"
        ]
    }
}


# =========================================================
# QUESTION BANK
# =========================================================

questions = {

    # ---------------- MATHS ----------------

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

    "Percentage": [
        (
            "What is 25% of 100?",
            ["10", "20", "25", "50"],
            "25"
        )
    ],

    # ---------------- SCIENCE ----------------

    "Measurement of Time and Motion": [
        (
            "Which instrument is commonly used to measure time?",
            ["Ruler", "Clock", "Thermometer", "Balance"],
            "Clock"
        )
    ],

    "Acids, Bases and Neutral": [
        (
            "Which substance is acidic?",
            ["Lemon juice", "Soap", "Toothpaste", "Baking soda"],
            "Lemon juice"
        )
    ],

    "Light": [
        (
            "Which object produces its own light?",
            ["Moon", "Mirror", "Sun", "Book"],
            "Sun"
        )
    ],

    "Plants": [
        (
            "Which part of a plant absorbs water?",
            ["Flower", "Root", "Fruit", "Leaf"],
            "Root"
        )
    ],

    # ---------------- SST ----------------

    "Landforms": [
        (
            "Which landform is generally higher and steeper than a hill?",
            ["Plain", "Mountain", "Valley", "Delta"],
            "Mountain"
        )
    ],

    "Climate": [
        (
            "Which factor strongly affects climate?",
            ["Latitude", "Language", "Population", "Alphabet"],
            "Latitude"
        )
    ],

    "Geographical Diversity of India": [
        (
            "Which of these is a major physical division of India?",
            ["Himalayas", "Equator", "Atlantic Ocean", "Sahara"],
            "Himalayas"
        )
    ],

    "Democracy": [
        (
            "What is an important feature of democracy?",
            [
                "People choose representatives",
                "One person controls everything",
                "There are no elections",
                "There are no laws"
            ],
            "People choose representatives"
        )
    ],

    # ---------------- ENGLISH ----------------

    "The Fun They Had": [
        (
            "Who wrote 'The Fun They Had'?",
            [
                "Isaac Asimov",
                "William Shakespeare",
                "Ruskin Bond",
                "R. K. Narayan"
            ],
            "Isaac Asimov"
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

    # ---------------- HINDI ----------------

    "संज्ञा": [
        (
            "‘राम विद्यालय जाता है।’ इसमें संज्ञा शब्द कौन-सा है?",
            ["राम", "जाता", "है", "कोई नहीं"],
            "राम"
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


# =========================================================
# SETUP
# =========================================================

def setup():

    show_title()

    st.markdown(
        '<div class="section-title">⚔️ ENTER THE ARENA</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <h2>🌌 Welcome, Warrior!</h2>
            <p>Enter your details to begin your journey.</p>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input("👤 Enter your name")

        grade = st.text_input("🎓 Enter your grade")

        if st.button(
            "⚔️ ENTER ARENA",
            use_container_width=True
        ):

            if name.strip() and grade.strip():

                st.session_state.name = name
                st.session_state.grade = grade
                st.session_state.page = "home"

                st.rerun()

            else:
                st.warning("Please enter your name and grade.")


# =========================================================
# SIDEBAR
# =========================================================

def sidebar():

    with st.sidebar:

        st.markdown("## ⚔️ ARENA OF MINDS")

        st.write(f"👤 **{st.session_state.name}**")
        st.write(f"🎓 Grade {st.session_state.grade}")

        st.divider()

        st.write(f"⭐ XP: **{st.session_state.xp}**")
        st.write(f"✨ Aura: **{st.session_state.aura}**")

        st.divider()

        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

        if st.button("📚 Study", use_container_width=True):

            st.session_state.page = "study"
            st.session_state.subject = None
            st.session_state.division = None
            st.session_state.topic = None

            st.rerun()

        if st.button("⚔️ Challenges", use_container_width=True):

            st.session_state.page = "challenges"
            st.rerun()

        if st.button("🌙 Chill", use_container_width=True):

            st.session_state.page = "chill"
            st.rerun()


# =========================================================
# HOME
# =========================================================

def home():

    show_title()

    st.markdown(
        f"""
        <div class="card">
            <h2>Welcome back, {st.session_state.name}! 👋</h2>
            <p>Ready to enter the Arena?</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-label">⭐ XP</div>
                <div class="stat-number">{st.session_state.xp}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-label">✨ AURA</div>
                <div class="stat-number">{st.session_state.aura}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        level = (st.session_state.xp // 100) + 1

        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-label">🏆 LEVEL</div>
                <div class="stat-number">{level}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">🔥 CHOOSE YOUR PATH</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <h1>📚</h1>
            <h2>STUDY</h2>
            <p>Master your Class 7 subjects.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("ENTER STUDY", use_container_width=True):

            st.session_state.page = "study"
            st.rerun()

    with c2:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <h1>⚔️</h1>
            <h2>CHALLENGES</h2>
            <p>Complete challenges and earn XP.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("VIEW CHALLENGES", use_container_width=True):

            st.session_state.page = "challenges"
            st.rerun()

    with c3:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <h1>🌙</h1>
            <h2>CHILL</h2>
            <p>Take a break from studying.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("ENTER CHILL", use_container_width=True):

            st.session_state.page = "chill"
            st.rerun()


# =========================================================
# STUDY PAGE
# =========================================================

def study_page():

    show_title()

    # =====================================================
    # LEVEL 1 — SUBJECT
    # =====================================================

    if st.session_state.subject is None:

        st.markdown(
            '<div class="section-title">📚 CHOOSE YOUR SUBJECT</div>',
            unsafe_allow_html=True
        )

        subjects = list(study.keys())

        for start in range(0, len(subjects), 2):

            cols = st.columns(2)

            for i in range(2):

                index = start + i

                if index >= len(subjects):
                    continue

                subject = subjects[index]

                with cols[i]:

                    st.markdown(
                        f"""
                        <div class="card" style="text-align:center;">
                            <h1>{subject.split()[0]}</h1>
                            <h2>{subject[2:]}</h2>
                            <p>
                            {len(study[subject])} divisions
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"ENTER {subject}",
                        key=f"subject_{index}",
                        use_container_width=True
                    ):

                        st.session_state.subject = subject
                        st.rerun()

        return

    # =====================================================
    # LEVEL 2 — DIVISION
    # =====================================================

    if st.session_state.division is None:

        subject = st.session_state.subject

        st.markdown(
            f"""
            <div class="section-title">
                {subject} → CHOOSE DIVISION
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "⬅️ BACK TO SUBJECTS",
            use_container_width=True
        ):

            st.session_state.subject = None
            st.rerun()

        divisions = list(study[subject].keys())

        for start in range(0, len(divisions), 2):

            cols = st.columns(2)

            for i in range(2):

                index = start + i

                if index >= len(divisions):
                    continue

                division = divisions[index]

                with cols[i]:

                    topics = study[subject][division]

                    st.markdown(
                        f"""
                        <div class="card" style="text-align:center;">
                            <h1>{division.split()[0]}</h1>
                            <h2>{division[2:]}</h2>
                            <p>{len(topics)} chapters / topics</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"ENTER {division}",
                        key=f"division_{index}",
                        use_container_width=True
                    ):

                        st.session_state.division = division
                        st.rerun()

        return

    # =====================================================
    # LEVEL 3 — CHAPTER
    # =====================================================

    if st.session_state.topic is None:

        subject = st.session_state.subject
        division = st.session_state.division

        st.markdown(
            f"""
            <div class="section-title">
                {division} → CHOOSE CHAPTER
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "⬅️ BACK TO DIVISIONS",
            use_container_width=True
        ):

            st.session_state.division = None
            st.rerun()

        topics = study[subject][division]

        for start in range(0, len(topics), 2):

            cols = st.columns(2)

            for i in range(2):

                index = start + i

                if index >= len(topics):
                    continue

                topic = topics[index]

                with cols[i]:

                    st.markdown(
                        f"""
                        <div class="card" style="text-align:center;">
                            <h1>📖</h1>
                            <h2>{topic}</h2>
                            <p>Enter this chapter.</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"START {topic}",
                        key=f"topic_{index}",
                        use_container_width=True
                    ):

                        st.session_state.topic = topic
                        st.session_state.page = "quiz"

                        st.rerun()

        return


# =========================================================
# QUIZ
# =========================================================

def quiz_page():

    topic = st.session_state.topic

    show_title()

    st.markdown(
        f"""
        <div class="section-title">
            ⚔️ {topic.upper()}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # QUESTION AVAILABLE
    # -----------------------------------------------------

    if topic not in questions:

        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <h1>🚧</h1>
                <h2>{topic}</h2>
                <p>
                    The challenge bank for this chapter
                    is coming soon!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "⬅️ BACK TO CHAPTERS",
            use_container_width=True
        ):

            st.session_state.topic = None
            st.session_state.page = "study"

            st.rerun()

        return

    # -----------------------------------------------------
    # QUESTION
    # -----------------------------------------------------

    question, options, answer = random.choice(
        questions[topic]
    )

    st.markdown(
        f"""
        <div class="card">
            <h2>🧠 {question}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    for number, option in enumerate(options):

        if st.button(
            f"{chr(65 + number)}. {option}",
            key=f"{topic}_{number}",
            use_container_width=True
        ):

            if option == answer:

                st.session_state.xp += 50
                st.session_state.aura += 5

                st.success(
                    "🔥 CORRECT! +50 XP  |  +5 AURA"
                )

            else:

                st.error(
                    f"❌ Not quite! Correct answer: {answer}"
                )

    if st.button(
        "⬅️ BACK TO CHAPTERS",
        use_container_width=True
    ):

        st.session_state.topic = None
        st.session_state.page = "study"

        st.rerun()


# =========================================================
# CHALLENGES
# =========================================================

def challenges():

    show_title()

    st.markdown(
        '<div class="section-title">⚔️ CHALLENGE ARENA</div>',
        unsafe_allow_html=True
    )

    challenge_list = [

        (
            "🧠 Brain Boost",
            "Answer a study question",
            50,
            5
        ),

        (
            "🔥 Knowledge Hunter",
            "Explore a new chapter",
            75,
            10
        ),

        (
            "⚡ Mind Warrior",
            "Complete a challenge",
            100,
            15
        )
    ]

    for i, (name, description, xp, aura) in enumerate(
        challenge_list
    ):

        st.markdown(
            f"""
            <div class="card">
                <h2>{name}</h2>
                <p>{description}</p>
                <b>⭐ +{xp} XP &nbsp;&nbsp; ✨ +{aura} Aura</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"COMPLETE {name}",
            key=f"challenge_{i}",
            use_container_width=True
        ):

            st.session_state.xp += xp
            st.session_state.aura += aura

            st.success(
                f"🔥 Challenge complete! "
                f"+{xp} XP | +{aura} Aura"
            )


# =========================================================
# CHILL
# =========================================================

def chill():

    show_title()

    st.markdown(
        '<div class="section-title">🌙 CHILL ZONE</div>',
        unsafe_allow_html=True
    )

    messages = [
        "Rest your mind. You have got this. 🌙",
        "Small progress is still progress. ✨",
        "Your next level is waiting. ⚔️",
        "Take a breath. Then come back stronger. 🔥",
        "Even warriors need rest. 🌌"
    ]

    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
            <h1>🌌</h1>
            <h2>{random.choice(messages)}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "✨ NEW MESSAGE",
        use_container_width=True
    ):
        st.rerun()


# =========================================================
# MAIN APP ROUTER
# =========================================================

if st.session_state.name == "":

    setup()

else:

    sidebar()

    if st.session_state.page == "home":
        home()

    elif st.session_state.page == "study":
        study_page()

    elif st.session_state.page == "quiz":
        quiz_page()

    elif st.session_state.page == "challenges":
        challenges()

    elif st.session_state.page == "chill":
        chill()
