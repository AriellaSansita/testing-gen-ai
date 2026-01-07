import streamlit as st
from google import genai

st.title("Gemini Chat")

client = genai.Client(api_key=st.secrets["AIzaSyBhwR6bbd5t4neTkSVB3i3DHqYFyA_Zy-w"])

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model="gemini-2.5-flash")
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type a message")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = st.session_state.chat.send_message(user_input)
    reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
