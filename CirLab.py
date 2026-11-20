import streamlit as st

st.set_page_config(
    page_title="CircuitLab",
    page_icon="⚡",
    layout="wide"
)


# ================= CUSTOM CSS =================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1120, #101d35);
    color: white;
}

.stApp {
    animation: pageFade 0.8s ease-in-out;
}

@keyframes pageFade {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

h1 {
    color: #38bdf8 !important;
}

h2, h3 {
    color: #7dd3fc !important;
}

[data-testid="stSidebar"] {
    background: #111c30;
}

.stButton button {
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border-radius: 10px;
    border: 1px solid #38bdf8;
    padding: 10px 20px;
    transition: all 0.3s ease;
}

.stButton button:hover {
    background: linear-gradient(90deg, #0ea5e9, #3b82f6);
    box-shadow: 0 0 12px #38bdf8,
                0 0 25px #0284c7;
    transform: translateY(-3px);
}

.feature-card {
    background: linear-gradient(145deg, #172033, #1e293b);
    border: 1px solid #334155;
    border-radius: 15px;
    padding: 22px;
    min-height: 145px;
    margin-bottom: 18px;
    transition: all 0.35s ease;
    animation: cardAppear 0.8s ease both;
}

.feature-card:hover {
    transform: translateY(-8px);
    border: 1px solid #38bdf8;
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.35);
}

.feature-card h3 {
    color: #38bdf8;
    margin-bottom: 12px;
}

.feature-card p {
    color: #cbd5e1;
    font-size: 14px;
}

@keyframes cardAppear {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero {
    background: linear-gradient(120deg, #10243d, #123b59);
    border: 1px solid #38bdf8;
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 25px;
    animation: heroGlow 3s ease-in-out infinite alternate;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
    text-shadow: 0 0 15px rgba(56, 189, 248, 0.6);
}

.hero p {
    color: #cbd5e1;
    font-size: 17px;
}

@keyframes heroGlow {
    from {
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.15);
    }
    to {
        box-shadow: 0 0 22px rgba(56, 189, 248, 0.4);
    }
}

/* INFORMATION PAGE */

.info-hero {
    background: linear-gradient(120deg, #10243d, #123b59);
    border: 1px solid #38bdf8;
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 20px;
    text-align: center;
    animation: heroGlow 3s ease-in-out infinite alternate;
}

.info-hero .info-icon {
    font-size: 60px;
}

.info-hero h1 {
    font-size: 42px;
    margin: 5px 0;
}

.info-hero p {
    color: #cbd5e1;
    font-size: 17px;
}

.section-title {
    color: #7dd3fc;
    font-size: 24px;
    margin: 25px 0 10px 0;
    border-left: 4px solid #38bdf8;
    padding-left: 12px;
}

.info-text {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.8;
}

.mini-card {
    background: linear-gradient(145deg, #172033, #1e293b);
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 15px;
    min-height: 130px;
    transition: all 0.3s ease;
}

.mini-card:hover {
    transform: translateY(-5px);
    border: 1px solid #38bdf8;
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
}

.mini-card h4 {
    color: #38bdf8;
    margin: 0 0 8px 0;
    font-size: 17px;
}

.mini-card p {
    color: #cbd5e1;
    font-size: 14px;
    margin: 0;
}

.chip {
    display: inline-block;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid #38bdf8;
    color: #7dd3fc;
    border-radius: 30px;
    padding: 8px 16px;
    margin: 5px;
    font-size: 14px;
}

.quote-box {
    background: linear-gradient(120deg, #10243d, #123b59);
    border-radius: 18px;
    border: 1px solid #38bdf8;
    padding: 30px;
    margin: 30px 0 15px 0;
    text-align: center;
}

.quote-box p {
    font-style: italic;
    font-size: 27px;
    color: #e0f2fe;
    margin: 0;
}

.thanks {
    text-align: center;
    margin: 50px 0 10px 0;
}

.thanks h1 {
    font-size: 65px;
    letter-spacing: 5px;
}

.thanks p {
    color: #7dd3fc;
    font-size: 16px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# ================= NAVIGATION FUNCTIONS =================

if "info_page" not in st.session_state:
    st.session_state.info_page = None


def open_info(key):
    st.session_state.info_page = key


def go_tool(name):
    st.session_state.nav = name
    st.session_state.info_page = None


def clear_info():
    st.session_state.info_page = None


# ================= INFORMATION CONTENT =================

INFO = {

    "ohm": {
        "icon": "⚡",
        "title": "Ohm's Law",
        "tagline": "The most fundamental rule of electrical circuits",

        "what": """
        Ohm's Law, discovered by Georg Simon Ohm, states that the
        current flowing through a conductor is directly proportional
        to the voltage across it, provided the temperature stays constant.

        It connects three important electrical quantities:
        Voltage (V), Current (I) and Resistance (R).
        """,

        "formulas": [
            "V = I \\times R",
            "I = \\frac{V}{R}",
            "R = \\frac{V}{I}"
        ],

        "uses": [
            ("🔌", "Circuit Analysis",
             "Used in KVL, KCL, nodal and mesh analysis."),

            ("🛠️", "Practical Labs",
             "Helps in selecting resistor values and checking circuit values."),

            ("💻", "Embedded Systems",
             "Used in Arduino and microcontroller projects."),

            ("📡", "Electronics Design",
             "Useful in voltage dividers and transistor circuits.")
        ],

        "tool": "Ohm's Law"
    },


    "resistor": {
        "icon": "🔌",
        "title": "Resistor Calculator",
        "tagline": "Series and parallel combinations made simple",

        "what": """
        Resistors are important components used to control current
        in electrical circuits.

        In a series connection, the same current flows through
        every resistor and the total resistance is the sum.

        In a parallel connection, the same voltage appears
        across every resistor.
        """,

        "formulas": [
            "R_{series} = R_1 + R_2 + R_3 + \\dots",

            "\\frac{1}{R_{parallel}} = "
            "\\frac{1}{R_1} + \\frac{1}{R_2} + \\dots"
        ],

        "uses": [
            ("🧮", "Network Simplification",
             "Simplifies complex resistor networks."),

            ("🎛️", "Voltage Dividers",
             "Used in sensors and electronic circuits."),

            ("🔧", "Custom Values",
             "Combines standard resistors to obtain required values."),

            ("📝", "Exam Practice",
             "Helps verify answers to circuit problems.")
        ],

        "tool": "Resistor Calculator"
    },


    "power": {
        "icon": "💡",
        "title": "Electrical Power",
        "tagline": "Understanding electrical energy transfer",

        "what": """
        Electrical power is the rate at which electrical energy
        is transferred or consumed in a circuit.

        It is measured in Watts (W).

        Power calculations help us understand the energy used
        by electrical components and devices.
        """,

        "formulas": [
            "P = V \\times I",
            "P = I^2 \\times R",
            "P = \\frac{V^2}{R}"
        ],

        "uses": [
            ("🔥", "Component Ratings",
             "Helps select suitable resistor power ratings."),

            ("🔋", "Battery Design",
             "Helps estimate battery and power supply requirements."),

            ("⚙️", "Power Electronics",
             "Used in converters and motor drivers."),

            ("🏭", "Electrical Engineering",
             "Used in load calculations and energy consumption.")
        ],

        "tool": "Power Calculator"
    },


    "colour": {
        "icon": "🎨",
        "title": "Resistor Colour Code",
        "tagline": "Identify resistor values using colour bands",

        "what": """
        Small resistors usually do not have numerical values
        printed on them.

        Instead, coloured bands are used to identify their
        resistance values.

        In a four-band resistor:

        First band represents the first digit.

        Second band represents the second digit.

        Third band represents the multiplier.

        Fourth band represents the tolerance.
        """,

        "formulas": [
            "R = (10 \\times D_1 + D_2) \\times 10^M"
        ],

        "uses": [
            ("🔍", "Lab Identification",
             "Identify resistors during practical experiments."),

            ("📚", "Viva and Exams",
             "Important for electronics laboratory examinations."),

            ("🧰", "Repair and Prototyping",
             "Identify resistor values on electronic boards."),

            ("✅", "Tolerance",
             "Understand the permitted variation in resistance.")
        ],

        "tool": "Colour Code"
    },


    "led": {
        "icon": "💡",
        "title": "LED Resistor Calculator",
        "tagline": "Calculate the current limiting resistor",

        "what": """
        LED stands for Light Emitting Diode.

        An LED requires a suitable current limiting resistor
        to control the current flowing through it.

        The resistor value depends on the supply voltage,
        LED forward voltage and desired LED current.
        """,

        "formulas": [
            "R = \\frac{V_{supply} - V_{LED}}{I_{LED}}"
        ],

        "uses": [
            ("🧪", "Mini Projects",
             "Used in LED indicators and Arduino projects."),

            ("🛡️", "Component Protection",
             "Helps prevent excessive current through an LED."),

            ("🔢", "Standard Values",
             "Helps select suitable standard resistor values."),

            ("🏗️", "Hardware Design",
             "Used in electronic signalling and indicator circuits.")
        ],

        "tool": "LED Calculator"
    }

}


# ================= LEARN ELECTRONICS CONTENT =================

LEARN_TOPICS = [
    "🔌 Circuit Analysis",
    "📈 Analog Electronics",
    "🔢 Digital Electronics",
    "📊 Signals & Systems",
    "🧠 Microprocessors & Microcontrollers",
    "📡 Analog & Digital Communication",
    "⚙️ Power Electronics",
    "🧬 VLSI Design",
    "🎛️ Control Systems",
    "🌐 Electromagnetic Theory",
    "📟 Embedded Systems",
    "📶 Antennas & Wave Propagation"
]


LEARN_GETS = [
    ("⚡", "Ohm's Law",
     "Voltage, current and resistance in one click."),

    ("🔌", "Resistor Calculator",
     "Series and parallel equivalent resistance."),

    ("💡", "Power Calculator",
     "Three power formulas with instant answers."),

    ("🎨", "Colour Code",
     "Decode resistor bands quickly."),

    ("💡", "LED Calculator",
     "Calculate the current limiting resistor."),

    ("📘", "Concept Pages",
     "Clear explanations, formulas and real uses.")
]


# ================= THANK YOU SECTION =================

def show_thanks():

    st.markdown("""
    <div class="thanks">
        <h1>THANK YOU</h1>
        <p>⚡ KEEP LEARNING • KEEP BUILDING • KEEP INNOVATING ⚡</p>
    </div>
    """, unsafe_allow_html=True)


# ================= INFORMATION PAGE =================

def show_info(key):

    # LEARN ELECTRONICS PAGE

    if key == "learn":

        st.markdown("""
        <div class="info-hero">
            <div class="info-icon">📘</div>
            <h1>Learn Electronics</h1>
            <p>Everything an Electronics Engineering student
            needs to get started</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "← Back to Home",
            key="back_learn",
            on_click=go_tool,
            args=("Home",)
        )

        st.markdown(
            '<div class="section-title">Electronics Engineering Students</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="info-text">Electronics and Communication '
            'Engineering (ECE) covers a wide range of subjects. '
            'These are the core topics where the basics you practise '
            'in CircuitLab keep showing up:</p>',
            unsafe_allow_html=True
        )

        chips = "".join(
            f'<span class="chip">{topic}</span>'
            for topic in LEARN_TOPICS
        )

        st.markdown(chips, unsafe_allow_html=True)

        st.markdown(
            '<div class="section-title">What You Get in This App</div>',
            unsafe_allow_html=True
        )

        cols = st.columns(3)

        for i, (icon, name, description) in enumerate(LEARN_GETS):

            with cols[i % 3]:

                st.markdown(
                    f"""
                    <div class="mini-card">
                        <h4>{icon} {name}</h4>
                        <p>{description}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown("""
        <div class="quote-box">
            <p>Visit the tools to see the Magic ✨</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "🚀 Go to Home Dashboard",
            key="learn_home",
            on_click=go_tool,
            args=("Home",),
            use_container_width=True
        )

        show_thanks()

        return


    # OTHER INFORMATION PAGES

    data = INFO[key]

    st.markdown(
        f"""
        <div class="info-hero">
            <div class="info-icon">{data["icon"]}</div>
            <h1>{data["title"]}</h1>
            <p>{data["tagline"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button(
        "← Back to Home",
        key="back_info",
        on_click=go_tool,
        args=("Home",)
    )

    st.markdown(
        f'<div class="section-title">What is {data["title"]}?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<p class="info-text">{data["what"]}</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Formula</div>',
        unsafe_allow_html=True
    )

    for formula in data["formulas"]:
        st.latex(formula)

    st.markdown(
        '<div class="section-title">Where It Is Useful for Engineering Students</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    for i, (icon, name, description) in enumerate(data["uses"]):

        with cols[i % 2]:

            st.markdown(
                f"""
                <div class="mini-card">
                    <h4>{icon} {name}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("""
    <div class="quote-box">
        <p>Visit the tool to see the Magic ✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.button(
        f"🚀 Open {data['title']} Tool",
        key="open_info_tool",
        on_click=go_tool,
        args=(data["tool"],),
        use_container_width=True
    )

    show_thanks()


# ================= SIDEBAR =================

st.sidebar.title("⚡ CircuitLab")
st.sidebar.caption("Electronics Learning Hub")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Ohm's Law",
        "Resistor Calculator",
        "Power Calculator",
        "Colour Code",
        "LED Calculator"
    ],
    key="nav",
    on_change=clear_info
)


# ================= INFORMATION PAGE DISPLAY =================

if st.session_state.info_page is not None:

    show_info(st.session_state.info_page)


# ================= HOME PAGE =================

elif page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>⚡ CircuitLab</h1>
        <p>Your Interactive Electronics Learning Hub</p>
        <p>
            Learn electronics, explore electrical concepts
            and perform calculations with interactive tools.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.header("🚀 Explore Our Tools")

    # FIRST ROW

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Ohm's Law</h3>
            <p>Calculate voltage, current and resistance
            using Ohm's Law.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Learn more →",
            key="card_ohm",
            on_click=open_info,
            args=("ohm",),
            use_container_width=True
        )

    with col2:

        st.markdown("""
        <div class="feature-card">
            <h3>🔌 Resistor Calculator</h3>
            <p>Calculate equivalent resistance
            in series and parallel circuits.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Learn more →",
            key="card_resistor",
            on_click=open_info,
            args=("resistor",),
            use_container_width=True
        )

    with col3:

        st.markdown("""
        <div class="feature-card">
            <h3>💡 Power Calculator</h3>
            <p>Calculate electrical power using
            different power formulas.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Learn more →",
            key="card_power",
            on_click=open_info,
            args=("power",),
            use_container_width=True
        )


    # SECOND ROW

    col4, col5, col6 = st.columns(3)

    with col4:

        st.markdown("""
        <div class="feature-card">
            <h3>🎨 Colour Code</h3>
            <p>Decode resistor colour bands
            and identify resistance values.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Learn more →",
            key="card_colour",
            on_click=open_info,
            args=("colour",),
            use_container_width=True
        )

    with col5:

        st.markdown("""
        <div class="feature-card">
            <h3>💡 LED Calculator</h3>
            <p>Calculate the required resistance
            for an LED circuit.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Learn more →",
            key="card_led",
            on_click=open_info,
            args=("led",),
            use_container_width=True
        )

    with col6:

        st.markdown("""
        <div class="feature-card">
            <h3>📘 Learn Electronics</h3>
            <p>Discover the fundamentals
            of electrical and electronic concepts.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Learn more →",
            key="card_learn",
            on_click=open_info,
            args=("learn",),
            use_container_width=True
        )

    st.divider()

    st.markdown("""
    <center>
        <p style="color:#7dd3fc;">
            ⚡ CircuitLab | Learn • Calculate • Explore
        </p>
    </center>
    """, unsafe_allow_html=True)


# ================= OHM'S LAW CALCULATOR =================

elif page == "Ohm's Law":

    st.title("⚡ Ohm's Law Calculator")

    st.write("Calculate voltage, current and resistance.")

    st.latex("V = I \\times R")

    choice = st.selectbox(
        "What do you want to calculate?",
        ["Voltage", "Current", "Resistance"]
    )

    if choice == "Voltage":

        current = st.number_input(
            "Current (Amperes)",
            min_value=0.0,
            value=2.0
        )

        resistance = st.number_input(
            "Resistance (Ohms)",
            min_value=0.0,
            value=10.0
        )

        if st.button("Calculate Voltage"):

            voltage = current * resistance

            st.success(f"Voltage = {voltage:.2f} V")


    elif choice == "Current":

        voltage = st.number_input(
            "Voltage (Volts)",
            min_value=0.0,
            value=12.0
        )

        resistance = st.number_input(
            "Resistance (Ohms)",
            min_value=0.1,
            value=6.0
        )

        if st.button("Calculate Current"):

            current = voltage / resistance

            st.success(f"Current = {current:.2f} A")


    elif choice == "Resistance":

        voltage = st.number_input(
            "Voltage (Volts)",
            min_value=0.0,
            value=12.0
        )

        current = st.number_input(
            "Current (Amperes)",
            min_value=0.1,
            value=2.0
        )

        if st.button("Calculate Resistance"):

            resistance = voltage / current

            st.success(f"Resistance = {resistance:.2f} Ω")


# ================= RESISTOR CALCULATOR =================

elif page == "Resistor Calculator":

    st.title("🔌 Resistor Calculator")

    st.write("Calculate equivalent resistance in electrical circuits.")

    st.divider()

    connection = st.radio(
        "Select Connection Type",
        ["Series", "Parallel"],
        horizontal=True
    )

    st.subheader("Enter Resistor Values")

    count = st.number_input(
        "Number of Resistors",
        min_value=2,
        max_value=10,
        value=3,
        step=1
    )

    resistors = []

    cols = st.columns(3)

    for i in range(int(count)):

        with cols[i % 3]:

            value = st.number_input(
                f"Resistor R{i+1} (Ω)",
                min_value=0.1,
                value=float((i+1)*10),
                key=f"resistor_{i}"
            )

            resistors.append(value)

    st.divider()

    if st.button("Calculate Total Resistance"):

        if connection == "Series":

            total = sum(resistors)

        else:

            total = 1 / sum(1/r for r in resistors)

        st.success("Calculation Completed!")

        st.metric(
            label="Equivalent Resistance",
            value=f"{total:.2f} Ω"
        )

        if connection == "Series":

            st.info(
                "Series: Total resistance is the sum of all resistors."
            )

        else:

            st.info(
                "Parallel: Reciprocal of total resistance equals "
                "the sum of individual reciprocals."
            )


# ================= COLOUR CODE CALCULATOR =================

elif page == "Colour Code":

    st.title("🎨 Resistor Colour Code Decoder")

    st.write("Decode the resistance value using four colour bands.")

    st.divider()

    colors = {
        "Black": 0,
        "Brown": 1,
        "Red": 2,
        "Orange": 3,
        "Yellow": 4,
        "Green": 5,
        "Blue": 6,
        "Violet": 7,
        "Grey": 8,
        "White": 9
    }

    multipliers = {
        "Black": 1,
        "Brown": 10,
        "Red": 100,
        "Orange": 1000,
        "Yellow": 10000,
        "Green": 100000,
        "Blue": 1000000,
        "Gold": 0.1,
        "Silver": 0.01
    }

    tolerances = {
        "Brown": "±1%",
        "Red": "±2%",
        "Green": "±0.5%",
        "Blue": "±0.25%",
        "Violet": "±0.1%",
        "Gold": "±5%",
        "Silver": "±10%"
    }

    st.subheader("Select Resistor Bands")

    col1, col2 = st.columns(2)

    with col1:

        band1 = st.selectbox(
            "First Band",
            list(colors.keys())
        )

        band2 = st.selectbox(
            "Second Band",
            list(colors.keys())
        )

    with col2:

        band3 = st.selectbox(
            "Third Band (Multiplier)",
            list(multipliers.keys())
        )

        band4 = st.selectbox(
            "Fourth Band (Tolerance)",
            list(tolerances.keys())
        )

    st.divider()

    if st.button("Decode Resistor"):

        first_digit = colors[band1]

        second_digit = colors[band2]

        multiplier = multipliers[band3]

        resistance = (
            first_digit * 10 + second_digit
        ) * multiplier

        st.success("Resistor Decoded Successfully!")

        st.metric(
            "Resistance Value",
            f"{resistance:g} Ω"
        )

        st.metric(
            "Tolerance",
            tolerances[band4]
        )

        st.info(
            f"Calculation: ({first_digit}{second_digit}) "
            f"× {multiplier:g}"
        )


# ================= POWER CALCULATOR =================

elif page == "Power Calculator":

    st.title("⚡ Electrical Power Calculator")

    st.write(
        "Calculate electrical power using voltage, current and resistance."
    )

    st.divider()

    st.latex("P = V \\times I")

    option = st.selectbox(
        "Choose Calculation",
        [
            "Power (P = V × I)",
            "Power (P = I² × R)",
            "Power (P = V² / R)"
        ]
    )

    col1, col2 = st.columns(2)

    if option == "Power (P = V × I)":

        with col1:

            voltage = st.number_input(
                "Voltage (V)",
                min_value=0.0,
                value=12.0
            )

        with col2:

            current = st.number_input(
                "Current (A)",
                min_value=0.0,
                value=2.0
            )

        if st.button("Calculate Power"):

            power = voltage * current

            st.success(
                f"Electrical Power = {power:.2f} W"
            )


    elif option == "Power (P = I² × R)":

        with col1:

            current = st.number_input(
                "Current (A)",
                min_value=0.0,
                value=2.0
            )

        with col2:

            resistance = st.number_input(
                "Resistance (Ω)",
                min_value=0.1,
                value=10.0
            )

        if st.button("Calculate Power"):

            power = current ** 2 * resistance

            st.success(
                f"Electrical Power = {power:.2f} W"
            )


    else:

        with col1:

            voltage = st.number_input(
                "Voltage (V)",
                min_value=0.0,
                value=12.0
            )

        with col2:

            resistance = st.number_input(
                "Resistance (Ω)",
                min_value=0.1,
                value=10.0
            )

        if st.button("Calculate Power"):

            power = voltage ** 2 / resistance

            st.success(
                f"Electrical Power = {power:.2f} W"
            )

    st.divider()

    st.info("Power is measured in Watts (W).")


# ================= LED CALCULATOR =================

elif page == "LED Calculator":

    st.title("💡 LED Resistor Calculator")

    st.write(
        "Calculate the appropriate resistor for your LED circuit."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        supply_voltage = st.number_input(
            "Supply Voltage (V)",
            min_value=0.1,
            value=5.0
        )

        led_voltage = st.number_input(
            "LED Forward Voltage (V)",
            min_value=0.1,
            value=2.0
        )

    with col2:

        led_current = st.number_input(
            "LED Current (mA)",
            min_value=0.1,
            value=20.0
        )

    if st.button(
        "Calculate Resistance",
        use_container_width=True
    ):

        voltage_drop = supply_voltage - led_voltage

        if voltage_drop <= 0:

            st.error(
                "Supply voltage must be greater than LED voltage."
            )

        else:

            current = led_current / 1000

            resistance = voltage_drop / current

            power = voltage_drop * current

            st.success("Calculation Completed!")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Required Resistance",
                f"{resistance:.2f} Ω"
            )

            c2.metric(
                "Voltage Drop",
                f"{voltage_drop:.2f} V"
            )

            c3.metric(
                "Resistor Power",
                f"{power:.3f} W"
            )

            st.info(
                f"Use a standard resistor of approximately "
                f"{resistance:.0f} Ω or the next higher standard value."
            )

            st.caption(
                "Choose a resistor with a suitable power rating "
                "and adequate margin."
            )