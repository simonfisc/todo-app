# Note: This script runs only on a local IDE with "streamlit run d19bonus.py"
import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start de camera
    camera_image = st.camera_input("Camera")
    print(camera_image)

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Render the grayscale image to webpage
    st.image(gray_img, caption='Gray Image')

if uploaded_image:
    # Open the user oploaded image with PIL
    img_uploaded = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_image = img_uploaded.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_image, caption='Uploaded Image')