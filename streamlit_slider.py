import streamlit as st
from datetime import time, datetime

st.header("Let's make differents slider examples")

#Exemple 1:

st.subheader("Slider to select your age:")

age = st.slider("How old are you ? ", 0, 100)

st.write("My age is: ", age)

#Exemple 2:

st.subheader("Slider to select age range")

age_range = st.slider("Select your age range", 0,100, (20,50))

st.write("My age range is: ", age_range)

#Exemple 3:

st.subheader("Slider to select time range")

appointment = st.slider("Schedule your appointment", value=(time(11,30), time(12,45)), format="hh:mm")
st.write("You are schedulded for: ", appointment)

#Exemple 4:

st.subheader("Slider to select datetime")

start_time = st.slider("When do you start ?", value=datetime(2024,12,18,12,28), format="YY/MM/DD - hh:mm")

start_time = st.slider("When do you finish ?", value=datetime(2024,12,18,17,45), format="YY/MM/DD - hh:mm")

st.write("Start time is:", start_time)

st.write("End time is:", start_time)