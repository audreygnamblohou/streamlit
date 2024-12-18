import streamlit as st

st.header("This is a button")

if st.button("Say Hello"):
    st.write("Hello y'all !!")
else:
    st.write("Goodbye")