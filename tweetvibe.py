# tweetvibe.py - Real-time X/Tweet Sentiment Analyzer
import streamlit as st
from transformers import pipeline

# Load Hugging Face model (runs once)
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", 
                    model="cardiffnlp/twitter-roberta-base-sentiment-latest")

st.title("🧠 TweetVibe – Instant Sentiment Analyzer")
st.write("Built by @Tommytaylor09 | Day 3 of 90 to AI job")

# Text input
tweet = st.text_area("Paste any X/Tweet here:", height=150,
                     placeholder="Just landed my dream AI job 🔥 @grok is a legend")

if st.button("Analyze Vibe"):
    if tweet.strip():
        with st.spinner("Reading the vibe..."):
            model = load_sentiment_model()
            result = model(tweet)[0]
            label = result['label']
            score = result['score'] * 100

            # Map labels
            if label == "LABEL_0":
                vibe = "😡 Negative"
            elif label == "LABEL_1":
                vibe = "😐 Neutral"
            else:
                vibe = "😍 Positive"

            st.metric("Vibe Detected", vibe, f"{score:.1f}% confidence")
            st.progress(score / 100)
    else:
        st.warning("Paste a tweet first!")
