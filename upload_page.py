import streamlit as st
import keras.models 
import numpy as np
import cv2
from PIL import Image

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
model = keras.models.load_model('models/banana_ripeness_model.h5')

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
        else:
            st.write("The fruit is not ripe yet.")
