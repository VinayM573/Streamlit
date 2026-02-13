import streamlit as st
import time

st.set_page_config(page_title="💖 For Someone Special", page_icon="🌹")

# -----------------------
# Session State Setup
# -----------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "her_name" not in st.session_state:
    st.session_state.her_name = ""

# -----------------------
# Styling
# -----------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ff758c, #ff7eb3);
}
.title {
    text-align:center;
    font-size:38px;
    font-weight:bold;
    color:white;
}
.message {
    font-size:20px;
    color:white;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💌 A Special Surprise 💌</div>', unsafe_allow_html=True)
st.write("")

# -----------------------
# STEP 1 → Ask Name
# -----------------------
# -----------------------
# STEP 1 → Romantic Entry
# -----------------------
# -----------------------
# STEP 1 → Cinematic Entry
# -----------------------
if st.session_state.step == 1:

    st.markdown("""
    <style>
    /* Floating hearts animation */
    .hearts {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }

    .heart {
        position: absolute;
        bottom: -50px;
        font-size: 24px;
        animation: floatUp 8s linear infinite;
        color: rgba(255,255,255,0.7);
    }

    @keyframes floatUp {
        0% { transform: translateY(0) scale(1); opacity: 1; }
        100% { transform: translateY(-100vh) scale(1.5); opacity: 0; }
    }

    /* Fade-in effect */
    .fade-in {
        animation: fadeIn 3s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .title {
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:white;
    }

    .message {
        text-align:center;
        font-size:20px;
        color:white;
    }
    div.stButton > button {
        display:block;
        margin-left:50px;
        padding:14px 35px;
        font-size:18px;
        font-weight:bold;
        border-radius:30px;
        background:white;
        color:#ff4d6d;
        border:none;
        transition:0.3s;
    }

    div.stButton > button:hover {
        transform:scale(1.07);
        background:#ffe6ec;
    }

    </style>

    <div class="hearts">
        <div class="heart" style="left:10%;">❤️</div>
        <div class="heart" style="left:25%; animation-delay:2s;">💖</div>
        <div class="heart" style="left:40%; animation-delay:4s;">💕</div>
        <div class="heart" style="left:60%; animation-delay:1s;">💘</div>
        <div class="heart" style="left:80%; animation-delay:3s;">💗</div>
        <div class="heart" style="left:50%; animation-delay:5s;">💞</div>

    </div>
    """, unsafe_allow_html=True)

    # Typing Effect for Hey Baby
    placeholder = st.empty()
    text = "Hey Baby ❤️"
    typed = ""

    for char in text:
        typed += char
        placeholder.markdown(f'<div class="title fade-in">{typed}</div>', unsafe_allow_html=True)
        time.sleep(0.1)

    st.markdown("""
        <div class="message fade-in">
        I made something special just for you... 💕<br><br>
        Are you ready to see it? 😘
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2.5)
    st.markdown('<div class="button-space"></div>', unsafe_allow_html=True)

    # Centered Button
    if st.button("Open My Surprise 💖"):
        st.session_state.step = 2
        st.rerun()
# -----------------------
# STEP 2 → Show Message
# -----------------------
elif st.session_state.step == 2:
    st.markdown("""
        <style>
             div.stButton > button {
        display:block;
        margin-left:65px;
        padding:14px 35px;
        font-size:18px;
        font-weight:bold;
        border-radius:30px;
        background:white;
        color:#ff4d6d;
        border:none;
        transition:0.3s;
    }

    div.stButton > button:hover {
        transform:scale(1.07);
        background:#ffe6ec;
    }   
        </style>
                """, unsafe_allow_html=True)
    name = "Kripa"

    if "message_shown" not in st.session_state:
        st.session_state.message_shown = False

    if not st.session_state.message_shown:
        message = f"""
        Dear {name}, ❤️

        Since the day you came into my life,
        everything feels magical ✨  

        Your smile makes my world brighter 🌸  
        Your presence gives me peace 💕  

        I don’t need a perfect world,
        I just need you by my side 💑  

        You are my today and all my tomorrows ❤️
        """

        for line in message.split("\n"):
            st.markdown(f'<div class="message">{line}</div>', unsafe_allow_html=True)
            time.sleep(1)

        st.session_state.message_shown = True

    else:
        st.markdown(f"""
        <div class="message">
        Dear {name}, ❤️ <br><br>
        Since the day you came into my life, everything feels magical ✨ <br>
        Your smile makes my world brighter 🌸 <br>
        You are my today and all my tomorrows ❤️
        </div>
        """, unsafe_allow_html=True)

    if st.button("Continue 💌"):
        st.session_state.step = 3
        st.rerun()

# -----------------------
# STEP 3 → Proposal Question
# -----------------------
elif st.session_state.step == 3:

    st.markdown('<div class="title">💍 I Have One Last Question...</div>', unsafe_allow_html=True)
    st.write("")

    question = st.radio(
        "Will you stay with me forever? ❤️",
        ["Yes 💖", "Absolutely Yes 😘", "Always Forever 💞"]
    )

    if st.button("Submit Answer 💕"):
        st.session_state.selected_answer = question
        st.session_state.step = 4
        st.rerun()

# -----------------------
# STEP 4 → Celebration + Slideshow
# -----------------------
elif st.session_state.step == 4:

    answer = st.session_state.get("selected_answer", "")

    st.balloons()

    st.markdown(
        f'<div class="title">💖 Congratulations! 💖</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="message">
        You chose: <b>{answer}</b> 💕<br><br>
        So now... I am fully yours forever ❤️💍<br><br>
        Officially Forever Together 😍
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("## 📸 Our Beautiful Future Together")

    photos = [
        "images/1.jpeg",
        "images/2.jpeg",
        "images/3.jpeg",
        "images/4.jpeg",
        "images/5.jpeg",
        
    ]

    placeholder = st.empty()
    for img in photos:
        placeholder.image(img, width=400)
        time.sleep(2)