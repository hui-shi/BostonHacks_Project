# recipes.py
import streamlit as st
import requests

def show_recipes():
    st.header("Recipes Page")
    st.write("This is the recipes page. You can display recipes and other content here.")

    # Replace with your Edamam API code to fetch recipes
    fruit = "banana"  # Placeholder for actual fruit
    app_id = "64902cce"
    app_key = "0db081c3f6bb979626d67c678e751384"
    url1 = "https://api.edamam.com/search?q="
    url2 = "&app_id=64902cce&app_key=0db081c3f6bb979626d67c678e751384"
    url = url1 + fruit + url2

    data = requests.get(url).json()

    # Display the list of recipes
    if 'hits' in data:
        for recipe in data['hits']:
            recipe_label = recipe['recipe']['label']
            recipe_url = recipe['recipe']['url']
            recipe_ingredients = recipe['recipe']['ingredientLines']

            st.subheader(recipe_label)
            st.write(f"URL: [{recipe_label}]({recipe_url})")
            st.write("Ingredients:")
            for ingredient in recipe_ingredients:
                st.write(f"- {ingredient}")

    # You can customize the display of recipes further as needed
