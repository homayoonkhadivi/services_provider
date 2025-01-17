import streamlit as st
import pandas as pd
from PIL import Image
import os

# Importing functions from other modules
from content.swimming import display_swimming
from content.datascience import display_datascience
from content.tax_advice import display_tax_advice
from content.visa_advice import display_visa_advice
from content.books_podcasts import display_books_podcasts
from content.get_social_together import display_get_social_together

# Directory path for images
image_dir = './images'

# Function to load images safely
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Image not found: {image_path}")
        return None

# Define image paths
swimming_image_path = os.path.join(image_dir, 'swimming.jpg')
datascience_image_path = os.path.join(image_dir, 'data_science.jpg')
visa_cdr_image_path = os.path.join(image_dir, 'visa_cdr.jpg')

# Load images
swimming_image = load_image(swimming_image_path)
datascience_image = load_image(datascience_image_path)
visa_cdr_image = load_image(visa_cdr_image_path)

# Title of the app
st.title("Welcome to My Exciting Life Journey App! 🎉")

# Description
st.write("""
    I offer servicies and activitis in six exciting areas: Swimming, Data Science, Tax Return Advice, Australia Visa Advice & Assessment, Books & Podcasts for Personal Growth, and Get Social Together. Choose one to get started!
""")

# Options for the user to choose
option = st.selectbox(
    'What would you like to learn?',
    ('Select an option', 'Swimming Lessons', 'Data Science Teaching', 'Tax Return Advice', 'Visa & Assessment Advice', 'Books & Podcasts for Personal Growth', 'Get Social Together')
)

# Display content based on the user's choice
if option == 'Swimming Lessons':
    display_swimming()
elif option == 'Data Science Teaching':
    display_datascience()
elif option == 'Visa & Assessment Advice':
    display_visa_advice()
elif option == 'Tax Return Advice':
    display_tax_advice()
elif option == 'Books & Podcasts for Personal Growth':
    display_books_podcasts()
elif option == 'Get Social Together':
    display_get_social_together()
