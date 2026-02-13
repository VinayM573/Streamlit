import streamlit as st
import time

st.set_page_config(page_title="💖 For You", page_icon="🌹")

# Custom Background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ff758c, #ff7eb3);
}
.big-text {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:white;
}
.message {
    font-size:20px;
    color:white;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-text">💌 A Special Message From Vinay 💌</div>', unsafe_allow_html=True)
st.write("")

name = st.text_input("🌸 Enter Your Name")

if st.button("💖 Open My Heart"):
    if name:
        st.balloons()
        st.markdown(f'<div class="message">Dear {name}, 💕</div>', unsafe_allow_html=True)
        st.write("")

        message = f"""
        From the day you came into my life,
        everything feels brighter 🌟  
        Your smile makes my world complete 😊  
        You are not just special...  
        You are my peace, my happiness, my everything ❤️  

        I don’t need a perfect day,  
        I just need you by my side 💑  

        Will you always stay with me? 💍
        """

        for line in message.split("\n"):
            st.markdown(f'<div class="message">{line}</div>', unsafe_allow_html=True)
            time.sleep(1)

        st.success("💖 Forever Yours, Vinay 💖")
    else:
        st.warning("Please enter her name first ❤️")
