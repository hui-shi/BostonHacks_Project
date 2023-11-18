import requests
import streamlit as st

#https://www.reddit.com/r/learnpython/comments/y2e5bh/can_someone_help_me_with_edamam_api/
fruit = "banana" #placeholder for actual fruit stuff
app_id = "64902cce"
app_key = "0db081c3f6bb979626d67c678e751384"
url = 'https://api.edamam.com/search?q=banana&app_id=64902cce&app_key=0db081c3f6bb979626d67c678e751384'.format(fruit, app_id, app_key)

data = requests.get("https://api.edamam.com/search?q={&fruit}&app_id=64902cce&app_key=0db081c3f6bb979626d67c678e751384").json()

st.write(data)