# BostonHacks_Project: Sustainable Solutions Track

### **Goal: Promote sustainable food habits and reduce household banana waste.**

Food waste is a major environmental issue that often falls under the radar. According to one statistic, "40% of food produced, processed, and transported in the U.S. is wasted and ends up in our landfills" [(Rescuing Leftover Cuisine)](https://www.rescuingleftovercuisine.org/challenge?gad_source=1&gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r2bf9zu4hONZ45O7n7HOI3HEtk_oiF0UBkJLzPuD5gIfFl_bdHv2DUaAhjLEALw_wcB). To bring more awareness to this issue and to help combat it (to some extent) we have developed this web interface.

Through our user-friendly front-end built with Streamlit, our web interface allows the user to upload any image of any fruit. Based on the uploaded image, our web interface can then determine the fruit's ripeness using a convolutional neural network (CNN) model trained on labeled data of ripe and unripe fruits. The CNN extracts visual features to accurately predict if the uploaded image ripe or unripe fruit. For fruits determined as ripe, the app will suggest recipes that allow the user to fully utilize the fruit and reduce waste.

By providing easy access to ripeness prediction and recommended uses for still-ripe fruits, this project aims to reduce food waste, promote sustainable food consumption habits, and contribute to a more environmentally conscious society.

## Project Overview

### Back end:
**1. Data Collection and Preprocessing**:  <br /> 
- Collect a dataset of images of ripe and unripe fruits (80% for training and 20% for validation).
- Preprocessed the images by resizing to 150x150 pixels and normalizing pixel values to [0,1].

**2. Model Training and Implementation**: <br /> 
- Evaluated model performance on the validation set in terms of loss and accuracy.
- Achieved a validation accuracy of 99.9% after 10 epochs of training.

### Front end:  <br /> 
Integrated the trained model into a Streamlit web interface. Users can upload images of fruits and know whether the fruit is ripe or not.

## Technologies Used
Python
 <br /> Streamlit
 <br /> Keras
 <br /> matplotlib
 <br /> tensorflow

## Team Members:
Hui Shi [huishi@bu.edu]
 <br />Lulu Jiang [lulujiang219@gmail.com][luluj@bu.edu]
 <br />Matthew He Yan [mhyan@bu.edu][notm477h3w@gmail.com]
