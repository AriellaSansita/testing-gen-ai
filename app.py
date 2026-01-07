import streamlit as st
import google.genai
try:
   client = google.genai.Client()
  st.write("Gemini API client configured.")
   prompt = "Benefits of API key management?"
   response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
   )
  st.write(f"Response: {response.text}")
except Exception as e:
  st.error(f"Error: {e}. Check your 'GEMINI_API_KEY' in secrets.")


