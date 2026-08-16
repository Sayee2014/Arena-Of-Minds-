import streamlit as st
import random

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Arena of Minds",
    page_icon="⚔️",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "name" not in st.session_state:
    st.session_state.name = ""

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "aura" not in st.session_state:
    st.session_state.aura = 0

if "page" not in st.session_state:
    st.session_state.page = "home"

if "subject" not in st.session_state:
    st.session_state.subject = None

if "division" not in st.session_state:
    st.session_state.division = None

if "chapter" not in st.session_state:
    st.session_state.chapter = None


# =========================================================
# BLUE ANIME-STYLE DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top,
            #1265d8 0%,
            #073c83 35%,
            #031d43 70%,
            #010b1c 100%
        );
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 25px;
}

h1, h2, h3 {
    color: white !important;
}

.aom-title {
    text-align: center;
    font-family: "Comic Sans MS", cursive;
    font-size: 56px;
    font-weight: bold;
    color: white;
    text-shadow:
        4px 4px 0px #0755b8,
        0px 0px 18px #24a8ff;
    animation: bounce 2s infinite;
}

@keyframes bounce {

    0%, 100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-8px);
    }

}

.subtitle {
    text-align: center;
    color: #a9ddff !important;
    letter-spacing: 5px;
    font-weight: bold;
    margin-bottom: 30px;
}

.card {
    background: rgba(4, 42, 91, 0.95);
    border: 1px solid #218cff;
    border-radius: 20px;
    padding: 25px;
    margin: 12px 0;
    box-shadow:
        0px 8px 25px rgba(0, 120, 255, 0.25);
}

.division-card {
    background:
        linear-gradient(
            145deg,
            rgba(5, 73, 150, 0.98),
            rgba(3, 31, 72, 0.98)
        );

    border: 2px solid #299cff;
    border-radius: 24px;

    padding: 28px;

    margin: 10px 0;

    min-height: 190px;

    text-align: center;

    box-shadow:
        0px 8px 30px rgba(0, 120, 255, 0.3);
}

.chapter-card {
    background: rgba(3, 38, 82, 0.96);

    border: 1px solid #208cff;

    border-radius: 20px;

    padding: 22px;

    min-height: 145px;

    text-align: center;

    box-shadow:
        0px 6px 20px rgba(0, 120, 255, 0.2);
}

.learning-card {
    background: rgba(3, 31, 68, 0.98);

    border: 2px solid #218cff;

    border-radius: 25px;

    padding: 35px;

    margin-top: 20px;

    box-shadow:
        0px 8px 35px rgba(0, 120, 255, 0.25);
}

.learning-text {
    color: #edf8ff;
    font-size: 18px;
    line-height: 1.8;
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

.section-title {
    text-align: center;
    font-family: "Comic Sans MS", cursive;
    font-size: 36px;
    font-weight: bold;
    margin: 25px 0;
    text-shadow: 3px 3px 0px #0755b8;
}

.stButton > button {
    background: linear-gradient(
        135deg,
        #0755b8,
        #087bd1
    );

    color: white !important;

    border: 1px solid #48b5ff;

    border-radius: 13px;

    font-weight: bold;

    min-height: 45px;
}

.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #087bd1,
        #0b96ed
    );

    box-shadow:
        0px 0px 15px #168fff;
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
# STUDY DATABASE
#
# SUBJECT
#       ↓
# DIVISION
#       ↓
# CHAPTER
#       ↓
# LEARNING
# =========================================================

STUDY = {

    # =====================================================
    # MATHEMATICS
    # =====================================================

    "📐 Mathematics": {

        "🔢 Number System": [
            "Integers",
            "Fractions",
            "Decimals",
            "Percentages",
            "Ratio and Proportion"
        ],

        "✖️ Algebra": [
            "Variables",
            "Algebraic Expressions",
            "Simple Equations",
            "Patterns",
            "Exponents"
        ],

        "📐 Geometry": [
            "Lines and Angles",
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
            "Mean",
            "Median",
            "Mode"
        ]
    },


    # =====================================================
    # SCIENCE
    # =====================================================

    "🔬 Science": {

        "⚙️ Physics": [
            "Measurement of Time and Motion",
            "Force and Motion",
            "Light",
            "Heat",
            "Electricity",
            "Magnets"
        ],

        "🧪 Chemistry": [
            "Acids, Bases and Neutral",
            "Matter",
            "Physical and Chemical Changes",
            "Separation of Substances",
            "Atoms and Molecules"
        ],

        "🧬 Biology": [
            "Plants",
            "Animals",
            "Human Body",
            "Nutrition",
            "Respiration",
            "Microorganisms"
        ],

        "🌱 Environment": [
            "Air",
            "Water",
            "Natural Resources",
            "Pollution",
            "Climate",
            "Conservation"
        ]
    },


    # =====================================================
    # SOCIAL SCIENCE
    # =====================================================

    "🌍 Social Science": {

        "🏛️ History": [
            "New Beginnings: Cities and Empires",
            "Early Civilisations",
            "Cities and States",
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
            "Rights and Duties",
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


    # =====================================================
    # ENGLISH
    # =====================================================

    "🇬🇧 English": {

        "📖 Literature": [
            "The Fun They Had",
            "Pierce Arrow",
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
            "Prefixes and Suffixes"
        ],

        "🔍 Reading": [
            "Comprehension",
            "Main Idea",
            "Inference",
            "Vocabulary in Context"
        ]
    },


    # =====================================================
    # HINDI
    # =====================================================

    "🇮🇳 Hindi": {

        "📖 साहित्य": [
            "सदर नमन",
            "यह मेरा यह मीत का",
            "मिठाईवाला",
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
        ],

        "📜 पठन": [
            "अपठित गद्यांश",
            "अपठित पद्यांश",
            "शब्दार्थ"
        ]
    }
}


# =========================================================
# LEARNING CONTENT
#
# IMPORTANT:
# This uses ONLY Streamlit text functions.
# There is NO HTML here.
# =========================================================

LEARNING = {

    "Integers": {
        "title": "🔢 Integers",
        "sections": [
            (
                "What are Integers?",
                "Integers are whole numbers that include positive numbers, "
                "negative numbers and zero."
            ),
            (
                "Examples",
                "..., -3, -2, -1, 0, 1, 2, 3, ..."
            ),
            (
                "Number Line",
                "Positive integers are placed to the right of zero, "
                "while negative integers are placed to the left."
            ),
            (
                "Remember",
                "When adding integers with the same sign, add their "
                "values and keep the same sign."
            )
        ]
    },


    "Fractions": {
        "title": "🍕 Fractions",
        "sections": [
            (
                "What is a Fraction?",
                "A fraction represents a part of a whole."
            ),
            (
                "Parts of a Fraction",
                "In 3/5, 3 is the numerator and 5 is the denominator."
            ),
            (
                "Types of Fractions",
                "Fractions can be proper, improper or mixed fractions."
            )
        ]
    },


    "Measurement of Time and Motion": {
        "title": "⏱️ Measurement of Time and Motion",
        "sections": [
            (
                "Time",
                "Time tells us when something happens and how long "
                "an event takes."
            ),
            (
                "Units of Time",
                "Seconds, minutes, hours, days, months and years "
                "are common units of time."
            ),
            (
                "Motion",
                "An object is said to be in motion when its position "
                "changes with respect to time."
            ),
            (
                "Examples",
                "A moving car, a flying bird and a rotating fan "
                "are examples of objects in motion."
            )
        ]
    },


    "Acids, Bases and Neutral": {
        "title": "🧪 Acids, Bases and Neutral",
        "sections": [
            (
                "Acids",
                "Acids generally have a sour taste. Lemon juice and "
                "vinegar are common examples."
            ),
            (
                "Bases",
                "Bases generally have a soapy feel. Soap solution "
                "and baking soda solution are examples."
            ),
            (
                "Neutral Substances",
                "A neutral substance is neither acidic nor basic. "
                "Pure water is an example."
            ),
            (
                "Indicators",
                "Indicators help us identify acidic and basic substances "
                "by showing changes such as colour changes."
            )
        ]
    },


    "Geographical Diversity of India": {
        "title": "🗺️ Geographical Diversity of India",
        "sections": [
            (
                "Introduction",
                "India has a remarkable variety of physical features."
            ),
            (
                "Major Features",
                "India contains mountains, plains, plateaus, deserts, "
                "coastal regions and islands."
            ),
            (
                "Importance",
                "Geography influences climate, agriculture, occupations, "
                "food, clothing and the ways people live."
            )
        ]
    },


    "Landforms": {
        "title": "🏔️ Landforms",
        "sections": [
            (
                "Meaning",
                "Landforms are natural features found on the Earth's surface."
            ),
            (
                "Mountains",
                "Mountains are high and usually steep areas of land."
            ),
            (
                "Plateaus",
                "Plateaus are elevated areas with relatively flat tops."
            ),
            (
                "Plains",
                "Plains are broad areas of mostly level land."
            ),
            (
                "Valleys",
                "Valleys are low areas between hills or mountains."
            ),
            (
                "Formation",
                "Landforms can be shaped by weathering, erosion, deposition "
                "and movements within the Earth."
            )
        ]
    },


    "Climate": {
        "title": "🌦️ Climate",
        "sections": [
            (
                "Meaning",
                "Climate is the long-term pattern of weather in a particular region."
            ),
            (
                "Factors",
                "Latitude, altitude, distance from the sea, winds and relief "
                "can affect climate."
            )
        ]
    },


    "New Beginnings: Cities and Empires": {
        "title": "🏛️ New Beginnings: Cities and Empires",
        "sections": [
            (
                "Cities",
                "The growth of cities was connected with agriculture, trade, "
                "crafts and administration."
            ),
            (
                "Empires",
                "Empires brought large territories under organised systems "
                "of administration and power."
            ),
            (
                "Why It Matters",
                "The development of cities and empires changed the way people "
                "lived, worked and interacted."
            )
        ]
    },


    "The Fun They Had": {
        "title": "📖 The Fun They Had",
        "sections": [
            (
                "Author",
                "The story was written by Isaac Asimov."
            ),
            (
                "Main Idea",
                "The story presents a future where children study at home "
                "with mechanical teachers."
            ),
            (
                "Theme",
                "The story encourages readers to think about schools, "
                "teachers, classmates and learning together."
            )
        ]
    },


    "Nouns": {
        "title": "✍️ Nouns",
        "sections": [
            (
                "Definition",
                "A noun is a word that names a person, place, animal, "
                "thing or idea."
            ),
            (
                "Examples",
                "Teacher, school, tiger, book and honesty are examples of nouns."
            )
        ]
    },


    "संज्ञा": {
        "title": "🇮🇳 संज्ञा",
        "sections": [
            (
                "परिभाषा",
                "किसी व्यक्ति, स्थान, वस्तु, प्राणी या भाव के नाम को "
                "संज्ञा कहते हैं।"
            ),
            (
                "उदाहरण",
                "राम, विद्यालय, पुस्तक, गाय और ईमानदारी संज्ञा के उदाहरण हैं।"
            )
        ]
    },


    "सर्वनाम": {
        "title": "🇮🇳 सर्वनाम",
        "sections": [
            (
                "परिभाषा",
                "जो शब्द संज्ञा के स्थान पर प्रयोग किए जाते हैं, "
                "उन्हें सर्वनाम कहते हैं।"
            ),
            (
                "उदाहरण",
                "मैं, हम, तुम, वह, वे और यह सर्वनाम हैं।"
            )
        ]
    }
}


# =========================================================
# SETUP PAGE
# =========================================================

def setup_page():

    show_title()

    st.markdown(
        '<div class="section-title">⚔️ ENTER THE ARENA</div>',
        unsafe_allow_html=True
    )

    left, middle, right = st.columns([1, 2, 1])

    with middle:

        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True
        )

        st.subheader("🌌 Welcome, Warrior!")

        st.write(
            "Enter your name to begin your journey."
        )

        name = st.text_input(
            "👤 Your Name"
        )

        if st.button(
            "⚔️ ENTER ARENA",
            use_container_width=True
        ):

            if name.strip():

                st.session_state.name = name.strip()
                st.session_state.page = "home"

                st.rerun()

            else:

                st.warning(
                    "Please enter your name."
                )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# =========================================================
# SIDEBAR
# =========================================================

def show_sidebar():

    with st.sidebar:

        st.title("⚔️ Arena of Minds")

        st.write(
            f"👤 **{st.session_state.name}**"
        )

        st.divider()

        st.write(
            f"⭐ XP: **{st.session_state.xp}**"
        )

        st.write(
            f"✨ Aura: **{st.session_state.aura}**"
        )

        st.divider()

        if st.button(
            "🏠 Home",
            use_container_width=True
        ):

            st.session_state.page = "home"
            st.rerun()

        if st.button(
            "📚 Study",
            use_container_width=True
        ):

            st.session_state.page = "study"

            st.session_state.subject = None
            st.session_state.division = None
            st.session_state.chapter = None

            st.rerun()

        if st.button(
            "⚔️ Challenges",
            use_container_width=True
        ):

            st.session_state.page = "challenges"
            st.rerun()

        if st.button(
            "🌙 Chill",
            use_container_width=True
        ):

            st.session_state.page = "chill"
            st.rerun()


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    show_title()

    st.markdown(
        f"""
        <div class="card">
        """,
        unsafe_allow_html=True
    )

    st.header(
        f"Welcome back, {st.session_state.name}! 👋"
    )

    st.write(
        "Your mind. Your journey. Your arena."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            '<div class="stat">',
            unsafe_allow_html=True
        )

        st.write("⭐ XP")
        st.subheader(
            str(st.session_state.xp)
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="stat">',
            unsafe_allow_html=True
        )

        st.write("✨ AURA")
        st.subheader(
            str(st.session_state.aura)
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    with col3:

        level = (
            st.session_state.xp // 100
        ) + 1

        st.markdown(
            '<div class="stat">',
            unsafe_allow_html=True
        )

        st.write("🏆 LEVEL")
        st.subheader(
            str(level)
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">🔥 CHOOSE YOUR PATH</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True
        )

        st.markdown("## 📚 STUDY")

        st.write(
            "Learn through subjects, divisions and chapters."
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if st.button(
            "ENTER STUDY",
            use_container_width=True
        ):

            st.session_state.page = "study"
            st.rerun()

    with col2:

        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True
        )

        st.markdown("## ⚔️ CHALLENGES")

        st.write(
            "Complete challenges and earn XP and Aura."
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if st.button(
            "VIEW CHALLENGES",
            use_container_width=True
        ):

            st.session_state.page = "challenges"
            st.rerun()

    with col3:

        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True
        )

        st.markdown("## 🌙 CHILL")

        st.write(
            "Take a break and relax your mind."
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if st.button(
            "ENTER CHILL",
            use_container_width=True
        ):

            st.session_state.page = "chill"
            st.rerun()


# =========================================================
# STUDY PAGE
# =========================================================

def study_page():

    show_title()

    # =====================================================
    # SUBJECT SELECTION
    # =====================================================

    if st.session_state.subject is None:

        st.markdown(
            '<div class="section-title">📚 CHOOSE SUBJECT</div>',
            unsafe_allow_html=True
        )

        subjects = list(STUDY.keys())

        for row in range(
            0,
            len(subjects),
            2
        ):

            columns = st.columns(2)

            for i in range(2):

                index = row + i

                if index >= len(subjects):
                    continue

                subject = subjects[index]

                with columns[i]:

                    st.markdown(
                        """
                        <div class="card">
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"# {subject.split()[0]}"
                    )

                    st.markdown(
                        f"## {subject[2:]}"
                    )

                    st.write(
                        f"{len(STUDY[subject])} divisions"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"ENTER {subject}",
                        key=f"subject_{index}",
                        use_container_width=True
                    ):

                        st.session_state.subject = subject
                        st.session_state.division = None
                        st.session_state.chapter = None

                        st.rerun()

        return


    # =====================================================
    # DIVISION SELECTION
    # =====================================================

    if st.session_state.division is None:

        subject = st.session_state.subject

        st.markdown(
            f'<div class="section-title">{subject}</div>',
            unsafe_allow_html=True
        )

        st.info(
            "📂 Choose a division to see its chapters."
        )

        if st.button(
            "⬅️ BACK TO SUBJECTS",
            use_container_width=True
        ):

            st.session_state.subject = None
            st.rerun()

        divisions = list(
            STUDY[subject].keys()
        )

        for row in range(
            0,
            len(divisions),
            2
        ):

            columns = st.columns(2)

            for i in range(2):

                index = row + i

                if index >= len(divisions):
                    continue

                division = divisions[index]

                chapters = STUDY[subject][division]

                with columns[i]:

                    st.markdown(
                        """
                        <div class="division-card">
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"# {division.split()[0]}"
                    )

                    st.markdown(
                        f"## {division[2:]}"
                    )

                    st.write(
                        f"📚 {len(chapters)} chapters"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"📂 OPEN {division[2:]}",
                        key=f"division_{index}",
                        use_container_width=True
                    ):

                        st.session_state.division = division
                        st.session_state.chapter = None

                        st.rerun()

        return


    # =====================================================
    # CHAPTER SELECTION
    # =====================================================

    if st.session_state.chapter is None:

        subject = st.session_state.subject
        division = st.session_state.division

        chapters = STUDY[subject][division]

        st.markdown(
            f'<div class="section-title">{division}</div>',
            unsafe_allow_html=True
        )

        st.info(
            "📖 Choose a chapter to start learning."
        )

        if st.button(
            "⬅️ BACK TO DIVISIONS",
            use_container_width=True
        ):

            st.session_state.division = None
            st.rerun()

        for row in range(
            0,
            len(chapters),
            2
        ):

            columns = st.columns(2)

            for i in range(2):

                index = row + i

                if index >= len(chapters):
                    continue

                chapter = chapters[index]

                with columns[i]:

                    st.markdown(
                        """
                        <div class="chapter-card">
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        "## 📖"
                    )

                    st.markdown(
                        f"### {chapter}"
                    )

                    st.write(
                        "Learning Chapter"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        "📖 START LEARNING",
                        key=f"chapter_{index}",
                        use_container_width=True
                    ):

                        st.session_state.chapter = chapter
                        st.rerun()

        return


    # =====================================================
    # LEARNING PAGE
    # =====================================================

    chapter = st.session_state.chapter

    st.markdown(
        f'<div class="section-title">📖 {chapter}</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "⬅️ BACK TO CHAPTERS",
        use_container_width=True
    ):

        st.session_state.chapter = None
        st.rerun()

    st.markdown(
        """
        <div class="learning-card">
        """,
        unsafe_allow_html=True
    )

    if chapter in LEARNING:

        content = LEARNING[chapter]

        st.title(
            content["title"]
        )

        for heading, text in content["sections"]:

            st.header(
                heading
            )

            st.write(
                text
            )

    else:

        st.title(
            f"📖 {chapter}"
        )

        st.info(
            "Learning material for this chapter "
            "will be added soon."
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "✨ MARK CHAPTER AS LEARNED",
        use_container_width=True
    ):

        st.session_state.xp += 10
        st.session_state.aura += 2

        st.success(
            "✨ Chapter completed! "
            "+10 XP | +2 Aura"
        )


# =========================================================
# CHALLENGES
# =========================================================

def challenges_page():

    show_title()

    st.markdown(
        '<div class="section-title">⚔️ CHALLENGE ARENA</div>',
        unsafe_allow_html=True
    )

    challenges = [
        (
            "🧠 Brain Boost",
            "Complete a learning challenge.",
            50,
            5
        ),
        (
            "🔥 Knowledge Hunter",
            "Explore a new chapter.",
            75,
            10
        ),
        (
            "⚡ Mind Warrior",
            "Complete an arena challenge.",
            100,
            15
        )
    ]

    for i, challenge in enumerate(challenges):

        name, description, xp, aura = challenge

        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True
        )

        st.subheader(name)

        st.write(description)

        st.write(
            f"⭐ +{xp} XP     ✨ +{aura} Aura"
        )

        st.markdown(
            "</div>",
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

def chill_page():

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
        """
        <div class="card">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "## 🌌"
    )

    st.subheader(
        random.choice(messages)
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    if st.button(
        "✨ NEW MESSAGE",
        use_container_width=True
    ):

        st.rerun()


# =========================================================
# MAIN PROGRAM
# =========================================================

if st.session_state.name == "":

    setup_page()

else:

    show_sidebar()

    if st.session_state.page == "home":

        home_page()

    elif st.session_state.page == "study":

        study_page()

    elif st.session_state.page == "challenges":

        challenges_page()

    elif st.session_state.page == "chill":

        chill_page()
