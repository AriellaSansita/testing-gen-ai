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
