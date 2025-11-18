# grokmini.py - Personal AI Chatbot with Memory
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

# YOUR HUGGING FACE TOKEN HERE
HF_TOKEN = "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"   # ← PASTE YOUR hf_... TOKEN

st.title("🤖 GrokMini – Your Personal AI Chatbot")
st.write("Built by @Tommytaylor09 | Day 4 of 90 to AI job")

# Login once
@st.cache_resource
def get_chatbot():
    sign = Login(HF_TOKEN, None)
    cookies = sign.login()
    return hugchat.ChatBot(cookies=cookies.get_dict())

# Initialize chat history + name
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Ask name on first load
if not st.session_state.user_name:
    name = st.text_input("What's your name?")
    if st.button("Start Chatting"):
        st.session_state.user_name = name
        st.session_state.messages.append({"role": "assistant", "content": f"Hey {name}! I'm GrokMini. Ask me anything."})
        st.rerun()
else:
    st.write(f"**Hey {st.session_state.user_name}!** 👋")

    # Display chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input
    if prompt := st.chat_input("Ask GrokMini anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                bot = get_chatbot()
                response = bot.chat(prompt)
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
