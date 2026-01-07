import streamlit as st
from google import genai

try:
    client = genai.Client(api_key=st.secrets["AIzaSyBhwR6bbd5t4neTkSVB3i3DHqYFyA_Zy-w"])
    st.write("Gemini API client configured.")

    prompt = "Benefits of API key management?"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write(f"Response: {response.text}")

except Exception as e:
    st.error(f"Error: {e}. Check your 'GEMINI_API_KEY' in secrets.")
