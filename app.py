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
# CSS
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

/* MAIN TITLE */

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

/* SECTION TITLE */

.section-title {
    text-align: center;
    font-family: "Comic Sans MS", cursive;
    font-size: 35px;
    font-weight: bold;
    margin: 25px 0px;
    text-shadow: 3px 3px 0px #0755b8;
}

/* CARDS */

.card {
    background: rgba(4, 42, 91, 0.94);
    border: 1px solid #218cff;
    border-radius: 20px;
    padding: 25px;
    margin: 12px 0px;
    box-shadow: 0px 8px 25px rgba(0, 120, 255, 0.25);
}

/* STATS */

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

/* BUTTONS */

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

/* LEARNING CONTENT */

.learning-box {
    background: rgba(3, 32, 70, 0.96);
    border: 1px solid #218cff;
    border-radius: 22px;
    padding: 35px;
    margin-top: 20px;
    box-shadow: 0px 8px 30px rgba(0, 120, 255, 0.25);
}

.learning-box h2 {
    color: #55baff !important;
}

.learning-box h3 {
    color: #8bd3ff !important;
}

.learning-box p {
    font-size: 18px;
    line-height: 1.7;
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
# STUDY LIBRARY
#
# SUBJECT
#      ↓
# DIVISION
#      ↓
# CHAPTER
#      ↓
# LEARNING PAGE
# =========================================================

study = {

    # =====================================================
    # MATHEMATICS
    # =====================================================

    "📐 Mathematics": {

        "🔢 Numbers": [
            "Integers",
            "Fractions",
            "Decimals",
            "Percentages",
            "Ratio and Proportion"
        ],

        "✖️ Algebra": [
            "Variables",
            "Expressions",
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
            "शब्दार्थ",
            "प्रश्न उत्तर"
        ]
    }
}


# =========================================================
# LEARNING CONTENT
# =========================================================

learning_content = {

    "Integers": """
    <h2>🔢 What are Integers?</h2>

    <p>
    Integers are whole numbers that include positive numbers,
    negative numbers and zero.
    </p>

    <h3>Examples</h3>

    <p>
    ..., -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ...
    </p>

    <h3>Number Line</h3>

    <p>
    On a number line, positive integers are placed to the
    right of zero and negative integers are placed to the
    left of zero.
    </p>

    <h3>Important Rule</h3>

    <p>
    When adding integers with the same sign, add their
    values and keep the same sign.
    </p>
    """,

    "Fractions": """
    <h2>🍕 Fractions</h2>

    <p>
    A fraction represents a part of a whole.
    </p>

    <h3>Parts of a Fraction</h3>

    <p>
    In 3/5, 3 is the numerator and 5 is the denominator.
    </p>

    <h3>Types of Fractions</h3>

    <p>
    Proper fractions, improper fractions and mixed fractions
    are common types of fractions.
    </p>
    """,

    "Acids, Bases and Neutral": """
    <h2>🧪 Acids, Bases and Neutral Substances</h2>

    <p>
    Substances can be classified as acidic, basic or neutral
    depending on their properties.
    </p>

    <h3>Acids</h3>

    <p>
    Acids generally have a sour taste. Lemon juice and vinegar
    are common examples.
    </p>

    <h3>Bases</h3>

    <p>
    Bases generally feel soapy. Soap solution and baking soda
    solution are examples.
    </p>

    <h3>Neutral Substances</h3>

    <p>
    Neutral substances are neither acidic nor basic.
    Pure water is an example.
    </p>

    <h3>Indicators</h3>

    <p>
    Indicators are substances that help us identify whether
    a substance is acidic or basic by showing a colour change.
    </p>
    """,

    "Measurement of Time and Motion": """
    <h2>⏱️ Measurement of Time and Motion</h2>

    <p>
    Time tells us when an event happens and how long it lasts.
    </p>

    <h3>Measurement of Time</h3>

    <p>
    We commonly measure time using seconds, minutes, hours,
    days and years.
    </p>

    <h3>Motion</h3>

    <p>
    An object is said to be in motion when its position changes
    with time.
    </p>

    <h3>Examples</h3>

    <p>
    A moving car, a flying bird and a rotating fan are examples
    of objects in motion.
    </p>
    """,

    "Geographical Diversity of India": """
    <h2>🗺️ Geographical Diversity of India</h2>

    <p>
    India has a great variety of physical features.
    These include mountains, plains, plateaus, deserts,
    coastal areas and islands.
    </p>

    <h3>Major Physical Features</h3>

    <p>
    The Himalayas form a major mountain system in the north.
    The Northern Plains are fertile plains formed by rivers.
    The Peninsular Plateau is an ancient landmass.
    India also has extensive coastal regions and islands.
    </p>

    <h3>Why is diversity important?</h3>

    <p>
    Different geographical regions influence people's climate,
    occupations, food, clothing and ways of life.
    </p>
    """,

    "Landforms": """
    <h2>🏔️ Landforms</h2>

    <p>
    Landforms are natural features of the Earth's surface.
    </p>

    <h3>Major Landforms</h3>

    <p>
    Mountains are high and steep areas of land.
    Plateaus are elevated areas with relatively flat tops.
    Plains are broad areas of mostly level land.
    Valleys are low areas between hills or mountains.
    </p>

    <h3>Formation</h3>

    <p>
    Landforms are shaped by processes such as erosion,
    weathering, deposition and movements inside the Earth.
    </p>
    """,

    "Climate": """
    <h2>🌦️ Climate</h2>

    <p>
    Climate refers to the long-term pattern of weather
    experienced by a place.
    </p>

    <h3>Factors Affecting Climate</h3>

    <p>
    Latitude, altitude, distance from the sea, winds and
    relief can influence the climate of a region.
    </p>
    """,

    "The Fun They Had": """
    <h2>📖 The Fun They Had</h2>

    <p>
    <b>The Fun They Had</b> is a science-fiction story by
    Isaac Asimov.
    </p>

    <h3>Main Idea</h3>

    <p>
    The story explores a future in which children study
    individually with mechanical teachers at home.
    </p>

    <h3>Central Theme</h3>

    <p>
    The story makes us think about the value of traditional
    schools, teachers, classmates and learning together.
    </p>
    """,

    "Nouns": """
    <h2>✍️ Nouns</h2>

    <p>
    A noun is a word used to name a person, place, animal,
    thing or idea.
    </p>

    <h3>Examples</h3>

    <p>
    Person — teacher<br>
    Place — school<br>
    Animal — tiger<br>
    Thing — book<br>
    Idea — honesty
    </p>
    """,

    "संज्ञा": """
    <h2>🇮🇳 संज्ञा</h2>

    <p>
    किसी व्यक्ति, स्थान, वस्तु, प्राणी या भाव के नाम को
    संज्ञा कहते हैं।
    </p>

    <h3>उदाहरण</h3>

    <p>
    राम, विद्यालय, पुस्तक, गाय, ईमानदारी आदि संज्ञा के उदाहरण हैं।
    </p>
    """,

    "सर्वनाम": """
    <h2>🇮🇳 सर्वनाम</h2>

    <p>
    जो शब्द संज्ञा के स्थान पर प्रयोग किए जाते हैं,
    उन्हें सर्वनाम कहते हैं।
    </p>

    <h3>उदाहरण</h3>

    <p>
    मैं, हम, तुम, वह, वे, यह आदि सर्वनाम हैं।
    </p>
    """
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
            <p>
                Enter your name and begin your learning journey.
            </p>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input(
            "👤 Enter your name"
        )

        if st.button(
            "⚔️ ENTER ARENA",
            use_container_width=True
        ):

            if name.strip():

                st.session_state.name = name
                st.session_state.page = "home"

                st.rerun()

            else:

                st.warning(
                    "Please enter your name."
                )


# =========================================================
# SIDEBAR
# =========================================================

def sidebar():

    with st.sidebar:

        st.markdown(
            "## ⚔️ ARENA OF MINDS"
        )

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
# HOME
# =========================================================

def home():

    show_title()

    st.markdown(
        f"""
        <div class="card">
            <h2>Welcome back, {st.session_state.name}! 👋</h2>
            <p>
                Your mind. Your journey. Your arena.
            </p>
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
                <div class="stat-number">
                    {st.session_state.xp}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="stat">
                <div class="stat-label">✨ AURA</div>
                <div class="stat-number">
                    {st.session_state.aura}
                </div>
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
                <div class="stat-number">
                    {level}
                </div>
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
            <p>
                Explore subjects, divisions and chapters.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "ENTER STUDY",
            use_container_width=True
        ):

            st.session_state.page = "study"
            st.rerun()

    with c2:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <h1>⚔️</h1>
            <h2>CHALLENGES</h2>
            <p>
                Take on challenges and earn rewards.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "VIEW CHALLENGES",
            use_container_width=True
        ):

            st.session_state.page = "challenges"
            st.rerun()

    with c3:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <h1>🌙</h1>
            <h2>CHILL</h2>
            <p>
                Take a break and relax your mind.
            </p>
        </div>
        """, unsafe_allow_html=True)

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
    # STEP 1 — SUBJECT
    # =====================================================

    if st.session_state.subject is None:

        st.markdown(
            '<div class="section-title">📚 SUBJECTS</div>',
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
                        <div class="card"
                             style="text-align:center;">

                            <h1>
                                {subject.split()[0]}
                            </h1>

                            <h2>
                                {subject[2:]}
                            </h2>

                            <p>
                                Explore
                                {len(study[subject])}
                                divisions
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
                        st.session_state.division = None
                        st.session_state.chapter = None

                        st.rerun()

        return


    # =====================================================
    # STEP 2 — DIVISION
    # =====================================================

    if st.session_state.division is None:

        subject = st.session_state.subject

        st.markdown(
            f"""
            <div class="section-title">
                {subject} → DIVISIONS
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

        st.markdown(
            """
            <div class="card" style="text-align:center;">
                <h2>📂 Choose a Division</h2>
                <p>
                    Select the area you want to learn.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        divisions = list(
            study[subject].keys()
        )

        for start in range(0, len(divisions), 2):

            cols = st.columns(2)

            for i in range(2):

                index = start + i

                if index >= len(divisions):
                    continue

                division = divisions[index]

                with cols[i]:

                    st.markdown(
                        f"""
                        <div class="card"
                             style="text-align:center;">

                            <h1>
                                {division.split()[0]}
                            </h1>

                            <h2>
                                {division[2:]}
                            </h2>

                            <p>
                                {len(
                                    study[subject][division]
                                )} chapters
                            </p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"OPEN {division}",
                        key=f"division_{index}",
                        use_container_width=True
                    ):

                        st.session_state.division = division
                        st.session_state.chapter = None

                        st.rerun()

        return


    # =====================================================
    # STEP 3 — CHAPTER
    # =====================================================

    if st.session_state.chapter is None:

        subject = st.session_state.subject
        division = st.session_state.division

        st.markdown(
            f"""
            <div class="section-title">
                {division} → CHAPTERS
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

        chapters = study[subject][division]

        for start in range(0, len(chapters), 2):

            cols = st.columns(2)

            for i in range(2):

                index = start + i

                if index >= len(chapters):
                    continue

                chapter = chapters[index]

                with cols[i]:

                    st.markdown(
                        f"""
                        <div class="card"
                             style="text-align:center;">

                            <h1>📖</h1>

                            <h2>
                                {chapter}
                            </h2>

                            <p>
                                Learn this chapter.
                            </p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        f"📖 LEARN {chapter}",
                        key=f"chapter_{index}",
                        use_container_width=True
                    ):

                        st.session_state.chapter = chapter
                        st.rerun()

        return


    # =====================================================
    # STEP 4 — LEARNING PAGE
    # =====================================================

    subject = st.session_state.subject
    division = st.session_state.division
    chapter = st.session_state.chapter

    st.markdown(
        f"""
        <div class="section-title">
            📖 {chapter}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align:center;">
            <p>
                {subject} → {division}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "⬅️ BACK TO CHAPTERS",
        use_container_width=True
    ):

        st.session_state.chapter = None
        st.rerun()

    # Learning content

    if chapter in learning_content:

        st.markdown(
            f"""
            <div class="learning-box">
                {learning_content[chapter]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="learning-box"
                 style="text-align:center;">

                <h2>📚 {chapter}</h2>

                <p>
                    Learning material for this chapter
                    will be added here.
                </p>

                <p>
                    This is your learning space —
                    no quiz, no pressure.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # Reward for exploring a chapter

    st.markdown("---")

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

def challenges():

    show_title()

    st.markdown(
        '<div class="section-title">⚔️ CHALLENGE ARENA</div>',
        unsafe_allow_html=True
    )

    challenge_list = [

        (
            "🧠 Brain Boost",
            "Complete a learning challenge.",
            50,
            5
        ),

        (
            "🔥 Knowledge Hunter",
            "Explore something new.",
            75,
            10
        ),

        (
            "⚡ Mind Warrior",
            "Complete a challenge.",
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
        <div class="card"
             style="text-align:center;">

            <h1>🌌</h1>

            <h2>
                {random.choice(messages)}
            </h2>

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
# MAIN ROUTER
# =========================================================

if st.session_state.name == "":

    setup()

else:

    sidebar()

    if st.session_state.page == "home":

        home()

    elif st.session_state.page == "study":

        study_page()

    elif st.session_state.page == "challenges":

        challenges()

    elif st.session_state.page == "chill":

        chill()
