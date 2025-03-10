'''
import requests

# URL of the FastAPI server
url = "http://34.220.82.197:8000/predict"  # Update with your server IP if hosted on AWS

# Path to the image file
image_path = "../training/PlantVillage/Potato___healthy/0b3e5032-8ae8-49ac-8157-a1cac3df01dd___RS_HL 1817.JPG"

# Open the image file in binary mode
with open(image_path, "rb") as image_file:
    files = {"file": image_file}

    # Send a POST request to the FastAPI server
    response = requests.post(url, files=files)

# Print the response from the server
print(response.json())  # Assuming t
'''
import streamlit as st
import requests
from PIL import Image
import io

# FastAPI server URL
FASTAPI_URL = "http://34.220.82.197:8000/predict"  # Update if needed

# Streamlit UI
st.title("Potato Disease Detection")
st.write("Upload an image to predict its health condition.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    # Send request to FastAPI
    files = {"file": ("image.jpg", img_bytes, "image/jpeg")}
    response = requests.post(FASTAPI_URL, files=files)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Prediction: {prediction}")
    else:
        st.error("Failed to get prediction. Check server connection.")
