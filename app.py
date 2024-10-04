# Q&A Chatbot

from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
from PIL import Image
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()

# Set Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo", page_icon="🖼️", layout="wide")

# App header
st.title("🖼️ Gemini Image Description Application")
st.write("Provide a prompt and upload an image to get detailed information using the Gemini model.")

# Input section
input = st.text_input("Enter a text prompt (optional):", placeholder="Describe the scene, objects, etc.", key="input")

uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG):", type=["jpg", "jpeg", "png"])

# Display uploaded image
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Show image metadata
    st.write(f"**Image details:** {uploaded_file.name}, {image.size[0]}x{image.size[1]}, {image.format}")

# Button to submit
submit = st.button("🔍 Analyze Image")

# If the submit button is clicked
if submit:
    if uploaded_file is None:
        st.error("Please upload an image to analyze.")
    else:
        with st.spinner('Processing...'):
            time.sleep(2)  # Simulate a delay (useful when waiting for API response)
            try:
                response = get_gemini_response(input, image)
                st.subheader("📋 Image Analysis")
                st.success("Here is the information about your image:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
