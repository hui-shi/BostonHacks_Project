import requests
import streamlit as st
import json

custom_css = '''
<style>
body {
    background-color: black;
    color: white; /* Change text color to white for better visibility */
}
</style>'''


st.markdown(custom_css, unsafe_allow_html=True)

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
parsedIngredients = []

for count in range(10):
    temp = ""
    for ingredients in data["hits"][count]["recipe"]["ingredientLines"]:
        temp = temp + ingredients + "\n"
    parsedIngredients.append(temp)

st.write(parsedIngredients)

def main():
    # Define section titles and corresponding content
    sections = [

        {"title": data["hits"][0]["recipe"]["label"], "content": st.markdown(parsedIngredients[0]), "url": data["hits"][0]["recipe"]["url"]},
        {"title": data["hits"][1]["recipe"]["label"], "content": parsedIngredients[1], "url": data["hits"][1]["recipe"]["url"]},
        {"title": data["hits"][2]["recipe"]["label"], "content": parsedIngredients[2], "url": data["hits"][2]["recipe"]["url"]},
        {"title": data["hits"][3]["recipe"]["label"], "content": parsedIngredients[3], "url": data["hits"][3]["recipe"]["url"]},
        {"title": data["hits"][4]["recipe"]["label"], "content": parsedIngredients[4], "url": data["hits"][4]["recipe"]["url"]},
        {"title": data["hits"][5]["recipe"]["label"], "content": parsedIngredients[5], "url": data["hits"][5]["recipe"]["url"]},
        {"title": data["hits"][6]["recipe"]["label"], "content": parsedIngredients[6], "url": data["hits"][6]["recipe"]["url"]},
        {"title": data["hits"][7]["recipe"]["label"], "content": parsedIngredients[7], "url": data["hits"][7]["recipe"]["url"]},
        {"title": data["hits"][8]["recipe"]["label"], "content": parsedIngredients[8], "url": data["hits"][8]["recipe"]["url"]},
        {"title": data["hits"][9]["recipe"]["label"], "content": parsedIngredients[9], "url": data["hits"][9]["recipe"]["url"]},
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
            #st.button(section["Check out the recipe"], on_click=open_page, args=(section["url"]))
            st.link_button("Check out the recipe", section['url'])

if __name__ == "__main__":
    main()