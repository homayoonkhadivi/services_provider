import streamlit as st
from utils import load_image

def display_datascience():
    st.header("Data Science Teaching")
    datascience_image_path = './images/data_science.jpg'
    datascience_image = load_image(datascience_image_path)
    if datascience_image:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(datascience_image, caption='Learn Data Science', use_column_width=True)
        with col2:
            st.write("""
            Are you ready to embark on a journey into the world of data science? Whether you're a beginner looking to learn the basics or an experienced professional seeking to enhance your skills, I offer comprehensive data science teaching that covers a wide array of topics, from fundamental concepts to advanced machine learning techniques.

            **Topics Covered:**

            **Programming Languages and Libraries:**
            - Python (Pandas, Numpy, Matplotlib, Plotly, Seaborn, Sci-Kit Learn)
            - R Studio
            - PostgreSQL, MySQL
            - Docker, SQLAlchemy
            - TensorFlow, Keras, PyTorch
            - Object-Oriented Programming (OOP)
            - HTML, CSS
            - Streamlit, FastAPI
            - MLFlow, CML CI/CD

            **Tools:**
            - Microsoft Power BI
            - Tableau
            - SSIS
            - ETL Processes
            - MS Office Suite

            **Cloud Technology:**
            - AWS (SageMaker Studio, AI Services)

            **Computer Vision:**
            - CNN & Transfer Learning for applying Artificial Intelligence in Medical Diagnosis

            **Natural Language Processing (NLP):**
            - Natural Language Understanding
            - Language Models like BERT, T5, GPT-2, and GPT-3
            - Named Entity Recognition
            - Topic Modelling
            - Sentiment Analysis
            - Document Similarity
            - Text Classification
            - Text Summarization

            **Teaching Topics:**
            - Introduction to Data Science
            - Data Analysis with Python, SQL
            - Machine Learning
            - Data Visualization
            - Deep Learning
            - Machine Learning in Production
            - MLOps Concepts
            - Deploying ML Models

            **About Me:**
            - [Kaggle Expert](https://www.kaggle.com/homayoonkhadivi) in notebooks and datasets
            - [Professional AI/ML Scientist](https://www.linkedin.com/in/homayoon-khadivi/)
            """)
