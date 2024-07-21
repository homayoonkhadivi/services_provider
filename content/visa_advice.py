import streamlit as st
from utils import load_image

def display_visa_advice():
    st.header("Australia Visa & Assessment Advice")
    visa_cdr_image_path = './images/visa_cdr.jpg'
    visa_cdr_image = load_image(visa_cdr_image_path)
    if visa_cdr_image:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(visa_cdr_image, caption='Learn Australia Visa & Assessment', use_column_width=True)
        with col2:
            st.write("""
            Looking to migrate to Australia or obtain professional assessment for your engineering qualifications? As a professional advisor, I can guide you through the visa and assessment process, ensuring a smooth and successful outcome.

    **Topics Covered:**
    - Advice on PTE & IELTS English Exams
    - Obtaining certificate assessments from various Australian organizations, such as Engineers Australia, TRA (Trades Recognition Australia), WETassess, etc.
    - Over 50 successful CDR assessments in all engineering fields with no comments
    - Guidance on selecting the most suitable visa based on your individual circumstances

    With expertise and experience in the field, I can address all your concerns and guide you through the complexities of the visa and assessment process. Whether you're an engineer seeking recognition or an individual looking to migrate to Australia, I can offer personalized advice to ensure we achieve your desired outcomes.
    """)
