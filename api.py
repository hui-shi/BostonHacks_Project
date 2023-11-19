import requests
import streamlit as st
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
#for recipe in data["hits"]:
#    st.write(recipe["recipe"]["label"])
#    st.write(recipe["recipe"]["url"])
#    for ingredient in recipe["recipe"]["ingredientLines"]:
#        st.write(ingredient)
#for recipe in data["hits"]:
    #st.write(recipe["recipe"]["ingredientLines"])
  
#recipeName = dataParsed["hits"][0]["label"]
#recipeLink = dataParsed["url"]
#recipeIngredients = dataParsed["ingredientLines"]

#print("Recipe Name: " + recipeName)
#print("Recipe Link: " + recipeLink)
#print("Ingredients: " + recipeIngredients)
# Using "with" notation
def main():
    # Define section titles and corresponding content
    sections = [
        {"title": data["hits"][0]["recipe"]["label"], "content": JSON.stringify(data["hits"][0]["recipe"]["ingredientLines"])},
        {"title": data["hits"][1]["recipe"]["label"], "content": data["hits"][1]["recipe"]["ingredientLines"]},
        {"title": data["hits"][2]["recipe"]["label"], "content": data["hits"][2]["recipe"]["ingredientLines"]},
        {"title": data["hits"][3]["recipe"]["label"], "content": data["hits"][3]["recipe"]["ingredientLines"]},
        {"title": data["hits"][4]["recipe"]["label"], "content": data["hits"][4]["recipe"]["ingredientLines"]},
        {"title": data["hits"][5]["recipe"]["label"], "content": data["hits"][5]["recipe"]["ingredientLines"]},
        {"title": data["hits"][6]["recipe"]["label"], "content": data["hits"][6]["recipe"]["ingredientLines"]},
        {"title": data["hits"][7]["recipe"]["label"], "content": data["hits"][7]["recipe"]["ingredientLines"]},
        {"title": data["hits"][8]["recipe"]["label"], "content": data["hits"][8]["recipe"]["ingredientLines"]},
        {"title": data["hits"][9]["recipe"]["label"], "content": data["hits"][9]["recipe"]["ingredientLines"]},
        # Add more sections as needed
    ]

    st.sidebar.title("Choose a recipe!")
    
    # Create a sidebar with dynamic links
    selected_section = st.sidebar.radio("Select Section", [section["title"] for section in sections])

    # Display the content of the selected section
    for section in sections:
        if selected_section == section["title"]:
            st.header(section["title"])
            st.write(section["content"])

if __name__ == "__main__":
    main()