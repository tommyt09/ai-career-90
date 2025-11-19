# app.py - AI Portfolio Dashboard (Day 5)
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Tommy Taylor | AI Engineer", layout="centered")

# Sidebar navigation
st.sidebar.title("🚀 My AI Projects")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "🚢 Titanic Survival",
    "🧠 TweetVibe",
    "🤖 GrokMini Chatbot",
    "👨‍💻 About Me"
])

# ——— HOME ———
if page == "🏠 Home":
    st.title("Tommy Taylor – AI Engineer")
    st.write("### 90-Day Challenge: From £0 → AI Job")
    st.write("Built & deployed 5 AI apps in 5 days with @grok")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("Day 1–2: ML + Web App")
        st.info("Day 3: NLP Sentiment")
    with col2:
        st.success("Day 4: Llama 3 Chatbot")
        st.info("Day 5: This Portfolio")

    st.balloons()

# ——— TITANIC ———
elif page == "🚢 Titanic Survival":
    st.header("🚢 Titanic Survival Predictor")
    st.write("Classic ML model deployed with Streamlit")
    st.link_button("Open App →", "https://ai-career-90-mxl9n59gb25cmpjasd4p6c.streamlit.app")

# ——— TWEETVIBE ———
elif page == "🧠 TweetVibe":
    st.header("🧠 TweetVibe – Sentiment Analyzer")
    st.write("Real-time emotion detection using Hugging Face")
    st.link_button("Open App →", "https://ai-career-90-8c9xdkqnzrf56hggppbtkd.streamlit.app")

# ——— GROKMINI ———
elif page == "🤖 GrokMini Chatbot":
    st.header("🤖 GrokMini – Personal AI Chatbot")
    st.write("Powered by Llama 3 + memory")
    st.link_button("Talk to GrokMini →", "https://ai-career-90-gwa2piga66evzf35pkkrpx.streamlit.app")

# ——— ABOUT ———
elif page == "👨‍💻 About Me":
    st.header("Tommy Taylor")
    st.write("UK | Self-taught AI Engineer | Building in public")
    st.write("🔗 GitHub: https://github.com/tommytaylor09")
    st.write("🔗 X: https://x.com/tommytaylor09")
    st.write("📧 Email: tommytaylor09@gmail.com (or DM me)")
    st.write("Currently open to junior AI/ML roles in London/remote")

st.sidebar.markdown("---")
st.sidebar.caption("Day 5/90 · Built with @grok · Nov 2025")
