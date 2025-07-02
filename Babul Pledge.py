import streamlit as st
import random

st.set_page_config(page_title="Green Footprint Calculator - Babul Films Society", page_icon="🌱", layout="centered")

# --- DATA ---
all_questions = [
    {
        "question": "How do you usually get to work or school?",
        "options": [
            ("Walk or bike", 0),
            ("Public transport", 1),
            ("Car (shared)", 3),
            ("Car (alone)", 5),
            ("Work from home", 0)
        ]
    },
    {
        "question": "How often do you fly for travel?",
        "options": [
            ("Never", 0),
            ("Once a year", 2),
            ("2-3 times a year", 4),
            ("More than 3 times", 6)
        ]
    },
    {
        "question": "What's your home energy source?",
        "options": [
            ("100% renewable energy", 0),
            ("Mostly renewable", 1),
            ("Mixed sources", 3),
            ("Mostly fossil fuels", 5)
        ]
    },
    {
        "question": "How much meat do you eat?",
        "options": [
            ("Vegetarian/Vegan", 0),
            ("Rarely (1-2 times/week)", 1),
            ("Occasionally (3-4 times/week)", 3),
            ("Daily", 5)
        ]
    },
    {
        "question": "How do you handle food waste?",
        "options": [
            ("Compost and minimal waste", 0),
            ("Try to minimize waste", 1),
            ("Some food waste", 3),
            ("Significant food waste", 5)
        ]
    },
    {
        "question": "What's your shopping style for clothes?",
        "options": [
            ("Buy only when needed, second-hand", 0),
            ("Buy occasionally, good quality", 1),
            ("Regular shopping", 3),
            ("Frequent fast fashion", 5)
        ]
    },
    {
        "question": "How do you heat/cool your home?",
        "options": [
            ("Very efficient system, well-insulated", 0),
            ("Efficient system", 1),
            ("Standard system", 3),
            ("Old, inefficient system", 5)
        ]
    },
    {
        "question": "How much do you recycle?",
        "options": [
            ("Everything possible", 0),
            ("Most items", 1),
            ("Some items", 3),
            ("Rarely recycle", 5)
        ]
    },
    {
        "question": "What's your water usage like?",
        "options": [
            ("Very conservative, short showers", 0),
            ("Mindful of usage", 1),
            ("Average usage", 3),
            ("High usage, long showers/baths", 5)
        ]
    },
    {
        "question": "How often do you buy new electronics?",
        "options": [
            ("Only when broken, repair first", 0),
            ("Every few years when needed", 1),
            ("Every 2-3 years", 3),
            ("Love getting latest gadgets", 5)
        ]
    },
    {
        "question": "How do you usually dispose of plastic waste?",
        "options": [
            ("Avoid plastic completely", 0),
            ("Recycle all plastic properly", 1),
            ("Some recycling, some trash", 3),
            ("Mostly throw in general trash", 5)
        ]
    },
    {
        "question": "What's your approach to buying groceries?",
        "options": [
            ("Local farmers market, organic", 0),
            ("Mix of local and supermarket", 1),
            ("Mainly supermarket shopping", 3),
            ("Convenience stores, packaged food", 5)
        ]
    },
    {
        "question": "How often do you eat out or order takeaway?",
        "options": [
            ("Rarely, mostly home cooking", 0),
            ("Once a week", 1),
            ("2-3 times a week", 3),
            ("Almost daily", 5)
        ]
    },
    {
        "question": "What's your car usage pattern?",
        "options": [
            ("Don't own a car", 0),
            ("Use only for long trips", 1),
            ("Use for most errands", 3),
            ("Use for everything, even short trips", 5)
        ]
    },
    {
        "question": "How do you manage your home's lighting?",
        "options": [
            ("LED bulbs, natural light when possible", 0),
            ("Energy-efficient bulbs, mindful usage", 1),
            ("Mix of bulb types, average usage", 3),
            ("Keep lights on, older bulbs", 5)
        ]
    },
    {
        "question": "What's your approach to packaging when shopping?",
        "options": [
            ("Bring own bags, avoid packaged items", 0),
            ("Reusable bags, minimal packaging", 1),
            ("Sometimes forget bags", 3),
            ("Don't think about packaging", 5)
        ]
    },
    {
        "question": "How do you handle household chemicals and cleaners?",
        "options": [
            ("Eco-friendly, homemade cleaners", 0),
            ("Green products when possible", 1),
            ("Mix of regular and eco products", 3),
            ("Use whatever's cheapest/strongest", 5)
        ]
    },
    {
        "question": "What's your digital consumption like?",
        "options": [
            ("Minimal streaming, energy-saving devices", 0),
            ("Moderate usage, turn off when not needed", 1),
            ("Regular streaming and device usage", 3),
            ("Heavy streaming, devices always on", 5)
        ]
    },
    {
        "question": "How do you handle yard waste and gardening?",
        "options": [
            ("Compost everything, native plants", 0),
            ("Some composting, eco-friendly gardening", 1),
            ("Basic lawn care, some waste disposal", 3),
            ("Heavy fertilizers, all waste to trash", 5)
        ]
    },
    {
        "question": "What's your approach to paper usage?",
        "options": [
            ("Paperless, digital everything", 0),
            ("Minimal paper, recycle everything", 1),
            ("Moderate paper use, some recycling", 3),
            ("Print freely, don't always recycle", 5)
        ]
    }
]

tips = [
    "Switch to LED bulbs - they use 75% less energy than traditional bulbs",
    "Take shorter showers to save water and energy",
    "Use public transport, walk, or bike instead of driving alone",
    "Eat more plant-based meals - even one day a week makes a difference",
    "Unplug electronics when not in use to avoid phantom energy drain",
    "Buy local and seasonal produce to reduce transportation emissions",
    "Use reusable bags, water bottles, and containers",
    "Set your thermostat 2°C lower in winter and higher in summer",
    "Air-dry clothes instead of using the dryer when possible",
    "Choose quality items that last longer over cheap disposables",
    "Start composting food scraps to reduce methane emissions",
    "Use cold water for washing clothes - it saves energy",
    "Plant trees or support reforestation projects in your area",
    "Choose renewable energy options if available in your area",
    "Reduce food waste by meal planning and proper storage"
]

# --- SESSION STATE ---
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(all_questions, 10)
    st.session_state.answers = [None] * 10
    st.session_state.current = 0
    st.session_state.show_results = False

def reset_quiz():
    st.session_state.questions = random.sample(all_questions, 10)
    st.session_state.answers = [None] * 10
    st.session_state.current = 0
    st.session_state.show_results = False

# --- HEADER ---
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #2ecc71, #27ae60); color: white; border-radius: 16px; padding: 24px; text-align: center; margin-bottom: 16px;">
        <h1 style="margin-bottom: 8px;">🌱 Green Footprint Calculator</h1>
        <p style="font-size: 1.1em;">Discover your environmental impact - Babul Films Society</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- QUIZ LOGIC ---
if not st.session_state.show_results:
    q = st.session_state.questions[st.session_state.current]
    st.progress((st.session_state.current + 1) / len(st.session_state.questions))
    st.write(f"**Question {st.session_state.current + 1} of {len(st.session_state.questions)}**")
    st.markdown(f"### {q['question']}")
    options = [opt[0] for opt in q["options"]]
    answer = st.radio(
        "Select an option:",
        options,
        index=options.index(options[st.session_state.answers[st.session_state.current]]) if st.session_state.answers[st.session_state.current] is not None else None,
        key=f"q{st.session_state.current}"
    )

    # Save answer
    if answer:
        idx = options.index(answer)
        st.session_state.answers[st.session_state.current] = q["options"][idx][1]

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.session_state.current > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current -= 1
    with col2:
        pass
    with col3:
        if st.session_state.answers[st.session_state.current] is not None:
            if st.session_state.current < len(st.session_state.questions) - 1:
                if st.button("Next ➡️"):
                    st.session_state.current += 1
            else:
                if st.button("See Results"):
                    st.session_state.show_results = True

else:
    score = sum(st.session_state.answers)
    co2_tons = round(score * 0.8 + 2, 1)
    if score <= 10:
        rating, rating_class, message = "Excellent", "🟢", "Outstanding! You're living very sustainably!"
    elif score <= 20:
        rating, rating_class, message = "Good", "🟩", "Great job! You're making a positive environmental impact!"
    elif score <= 35:
        rating, rating_class, message = "Fair", "🟨", "You're on the right track, but there's room for improvement!"
    else:
        rating, rating_class, message = "Poor", "🟥", "There's significant opportunity to reduce your environmental impact!"

    trees_needed = int(co2_tons * 16)
    random_tips = random.sample(tips, 5)

    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; border-radius: 16px; padding: 24px; text-align: center; margin-bottom: 16px;">
            <h2 style="font-size: 2.5em;">{co2_tons}</h2>
            <p style="font-size: 1.2em;">Tons of CO₂ per year</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style="background: #f8f9fa; border-radius: 12px; padding: 18px; text-align: center; margin-bottom: 16px;">
            <span style="font-size: 1.5em;">{rating_class}</span>
            <b style="font-size: 1.2em;"> {rating}</b><br>
            <span>{message}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style="background: #e8f5e8; border-radius: 12px; padding: 18px; text-align: center; margin-bottom: 16px;">
            <b>🌳 {trees_needed} trees</b><br>
            needed to offset your annual carbon footprint
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='background: #f8f9fa; border-radius: 12px; padding: 18px; margin-bottom: 16px;'>"
        "<h4>💡 Personalized Tips for You</h4><ul>" +
        "".join([f"<li>{tip}</li>" for tip in random_tips]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

    st.button("Take Again", on_click=reset_quiz)

    share_text = (
        f"I just calculated my carbon footprint! 🌱\n\n"
        f"My annual CO₂ emissions: {co2_tons} tons\n"
        f"Rating: {rating}\n\n"
        f"Calculate yours with Babul Films Society's Green Footprint Calculator!"
    )
    st.text_area("Share your results:", share_text, height=100)
    st.write("Copy and share your results with friends!")

# --- FOOTER ---
st.markdown(
    """
    <hr>
    <div style="text-align: center; color: #888; font-size: 0.95em;">
        Created with ❤️ by <b>Raja Vardhan D</b><br>
        Green Footprint Calculator - Babul Films Society
    </div>
    """,
    unsafe_allow_html=True
)
