import streamlit as st
import keras.models 
import numpy as np
import cv2
from PIL import Image
import requests
import streamlit as st
import json

def preprocess(img):
    try:
        # Check if img is not None
        if img is None:
            return None
        
        # Convert uploaded image to NumPy array
        img = np.asarray(img)

        # Check if img is already in RGB format
        if img.shape[-1] == 3:
            return img

        # Convert to OpenCV image
        img = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2RGB)

        # Resize image
        img = Image.fromarray(img).resize((150, 150))

        # Normalize
        img = (img - 127.5) / 127.5

        # Channels last
        img = np.moveaxis(img, 0, -1)

        return img
    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

# Load the trained model
model = keras.models.load_model('banana_ripeness_model.h5')

st.header("Welcome to :rainbow[fruitcalendar.com]!")

st.write("Upload an image of any fruit to see if it’s expired or not")

image = st.file_uploader("Browse files", "png")

if image is not None:
    st.link_button("Continue", "https://docs.streamlit.io/library/api-reference/widgets/st.link_button")

    # Load uploaded image
    img = np.asarray(image)

    # Resize and preprocess image like during training
    img = preprocess(img)

    if img is not None:
        # Make prediction
        prediction = model.predict(np.expand_dims(img, axis=0))[0][0]

        # Display the prediction result in Streamlit
        if prediction > 0.5:
            st.write("The fruit is ripe!") 
            if st.button("Check out the recipes!"):

                fruit = "banana" #placeholder for actual fruit stuff
                app_id = "64902cce"
                app_key = "0db081c3f6bb979626d67c678e751384"
                url1 = 'https://api.edamam.com/search?q='
                url2 = '&app_id=64902cce&app_key=0db081c3f6bb979626d67c678e751384'
                url = url1 + fruit + url2

                data = requests.get(url).json()


                parsedIngredients = []

                for count in range(10):
                    temp = ""
                    for ingredients in data["hits"][count]["recipe"]["ingredientLines"]:
                        temp = temp + ingredients + "  \n"
                        parsedIngredients.append(temp)



                def main():
                # Define section titles and corresponding content
                    sections = [

                        {"title": data["hits"][0]["recipe"]["label"], "content": parsedIngredients[0], "url": data["hits"][0]["recipe"]["url"]},
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

        else:
            st.write("The fruit is not ripe yet.")