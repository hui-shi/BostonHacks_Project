import streamlit as st
import keras.models 
import numpy as np
import cv2
from PIL import Image
import requests
from streamlit_extras.switch_page_button import switch_page
from recipe import show_recipes
import subprocess




def preprocess(img):

  try:
    # Convert to NumPy array
    img = np.asarray(img)
    
    # Print image details for debugging
    print(f"Image shape: {img.shape}, type: {img.dtype}")
    
    # Convert to RGB
    if img.ndim == 2:
      img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif img.shape[2] == 4:
      img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
      
    # Resize 
    img = cv2.resize(img, (150, 150))  
    
    # Normalize 
    img = (img - 127.5) / 127.5
    
  except Exception as e:
    print(f"Preprocessing error: {e}")
    
  return img



# Load the trained model
model = keras.models.load_model('../models/banana_ripeness_model.h5')

def main():
    st.header("Welcome to :rainbow[fruitcalendar.com]!")

    st.write("Upload an image of any fruit to see if it’s expired or not")
    uploaded_file = st.file_uploader("Choose an image")

    if uploaded_file:
        img = Image.open(uploaded_file)
        preprocessed_img = preprocess(img)

        predictions = model.predict(np.expand_dims(preprocessed_img, axis=0))[0][0]

        if predictions > 0.5:
            st.write("The fruit is ripe!") 
            if st.button("Check out the recipes!"):
                show_recipes()  # Call the show_recipes function from api.py
        else:
            st.write("Your fruit is not ripe yet.")

if __name__ == "__main__":
    main()

    
    
    