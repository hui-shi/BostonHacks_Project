# BostonHacks_Project: Sustainable Solutions Track

### **Goal: Promote sustainable food habits and reduce household banana waste.**

Bananas are one of the most wasted foods globally[<sup>1</sup>](https://www.openaccessgovernment.org/browning-banana-food-waste-household/135392/). This project aims to tackle this challenge through a machine learning tool that empowers sustainable banana consumption.

The tool classifies banana ripeness from images using a convolutional neural network (CNN) model trained on labeled data of ripe and unripe bananas. The CNN extracts visual features to accurately predict if an uploaded banana image is ripe or unripe.

A user-friendly web application built with Streamlit allows households to get ripeness predictions on their bananas by uploading images. For bananas classified as ripe, the app suggests recipes to fully utilize the banana and prevent waste.

By providing easy access to ripeness prediction and recommended uses for ripe bananas, this project aims to reduce banana waste, promote sustainable food consumption habits, and contribute to a more environmentally conscious society. The customizable model and interface are designed for extensibility to other fruits.

## Project Overview

### Back end:
**1. Data Collection and Preprocessing**:  <br /> 
- Collect a dataset of images of ripe and unripe bananas (80% for training and 20% for validation).
- Preprocessed the images by resizing to 150x150 pixels and normalizing pixel values to [0,1].

**2. Model Training and Implementation**: <br /> 
- Evaluated model performance on the validation set in terms of loss and accuracy.
- Achieved a validation accuracy of 99.9% after 10 epochs of training.

### Front end:  <br /> 
Integrated the trained model into a Streamlit web application. Users can upload images of bananas and receive ripeness predictions.

## Technologies Used
Python
 <br /> Streamlit
 <br /> Keras
 <br />matplotlib

## Project Setup

## Running the Project


## Team Members:
Hui Shi [huishi@bu.edu]
 <br />Lulu Jiang [lulujiang219@gmail.com][luluj@bu.edu]
 <br />Matthew He Yan [mhyan@bu.edu][notm477h3w@gmail.com]
