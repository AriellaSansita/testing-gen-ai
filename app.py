import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini Chat")
st.title("Gemini Chat")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type a message")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    reply = response.text.strip()

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)


"""
import streamlit as st
from google import genai

while True:
   user_input = input("You: ")
   if user_input.lower() == "exit":
       print("Bot: Goodbye!")
   break

try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    st.write("Gemini API client configured.")

    prompt = "Benefits of API key management?"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    st.write(f"Response: {response.text}")

except Exception as e:
    st.error(f"Error: {e}. Check your 'GEMINI_API_KEY' in secrets.")
"""
