import requests
import streamlit as st
from streamlit_card import card
import json

#https://www.reddit.com/r/learnpython/comments/y2e5bh/can_someone_help_me_with_edamam_api/
fruit = "banana" #placeholder for actual fruit stuff
app_id = "64902cce"
app_key = "0db081c3f6bb979626d67c678e751384"
url1 = 'https://api.edamam.com/search?q='
url2 = '&app_id=64902cce&app_key=0db081c3f6bb979626d67c678e751384'
url = url1 + fruit + url2

data = requests.get(url).json()

#st.write(data)

#dataParsed = json.loads(data)

#st.write(data["hits"][0]["recipe"]["label"])
#st.write(data["hits"][0]["recipe"]["url"])
#st.write(data["hits"][0]["recipe"]["ingredientLines"])
for recipe in data["hits"]:
    st.write(recipe["recipe"]["label"])
    st.write(recipe["recipe"]["url"])
    for ingredient in recipe["recipe"]["ingredientLines"]:
        st.write(ingredient)
#for recipe in data["hits"]:
    #st.write(recipe["recipe"]["ingredientLines"])
  
#recipeName = dataParsed["hits"][0]["label"]
#recipeLink = dataParsed["url"]
#recipeIngredients = dataParsed["ingredientLines"]

#print("Recipe Name: " + recipeName)
#print("Recipe Link: " + recipeLink)
#print("Ingredients: " + recipeIngredients)
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        st.h1("Choose a Recipe"),
        (data["hits"][0]["recipe"]["label"],
         data["hits"][1]["recipe"]["label"],
         data["hits"][2]["recipe"]["label"],
         data["hits"][3]["recipe"]["label"],
         data["hits"][4]["recipe"]["label"],
         data["hits"][5]["recipe"]["label"],
         data["hits"][6]["recipe"]["label"],
         data["hits"][7]["recipe"]["label"],
         data["hits"][8]["recipe"]["label"],
         data["hits"][9]["recipe"]["label"])
    )

'''
hasClicked = card(
    title="Hello World!",
    text="Some description",
    image="http://placekitten.com/200/300",
    url="https://github.com/gamcoh/st-card"
)
'''
