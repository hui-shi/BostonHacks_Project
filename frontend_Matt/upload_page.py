import streamlit as st

st.header("Welcome to :rainbow[fruitcalendar.com]!")

st.write("Upload an image of any fruit to see if it’s expired or not")

image = st.file_uploader("Browse files","png")

if image != None:
  st.link_button("Continue","https://docs.streamlit.io/library/api-reference/widgets/st.link_button")