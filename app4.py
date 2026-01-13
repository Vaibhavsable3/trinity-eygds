import streamlit as st
import google.generativeai as genai
st.title("welcome to streamlit app")
user_input = st.text_input("ask me anything")
genai.configure(api_key="AIzaSyB09Zf92WgBYckYL4O7aNfjQ3Jq8Uc1n7o")
model =genai.GenerativeModel("gemini-1.5-pro")
if user_input:
    response = model.generate_content(prompt=user_input )
    st.write("AI Response: ", response.text)
