import streamlit as st
st.title("some basic commands like slider button in  streamlit")
age=st.slider("select your age",1,100)
city=st.selectbox("choose your city",["delhi","mumbai","pune","sambhajinagar"])
if st.button("show details"):
    st.write("your age is ",age)
    st.write("your city is ",city)
    st.write(age,city)
