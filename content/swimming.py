import streamlit as st
from utils import load_image

def display_swimming():
    st.header("Swimming Lessons")
    swimming_image_path = './images/swimming.jpg'
    swimming_image = load_image(swimming_image_path)
    if swimming_image:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(swimming_image, caption='Learn to Swim', use_column_width=True)
         with col2:
            st.write("""
            ### Introduction:
            I am a professional swimmer, swim coach, international lifeguard, and water therapist. Having been a member of Iran's National Swimming Team for 8 years and holding two national records in backstroke for a significant period,
            I offer comprehensive swimming lessons for students of all skill levels.

            #### Services Offered:
            - Swimming Lessons

            **Topics Covered:**
            - Basic swimming techniques
            - Advanced strokes
            - Breathing techniques
            - Safety tips

            **Hydrotherapy Sessions:**
            - **Benefits:**
            Treat aches and pains such as headaches, muscle pain, migraines, and toothaches

           **Contact Information:**
            Feel free to reach out if you have any questions or need more information!

            **Follow Me:**
            - 📘[Facebook](https://www.facebook.com/homayoon.khadivi.7) 
            - 📸[Instagram](https://www.instagram.com/homayoon.khadivi/)
            """)
