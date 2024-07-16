import streamlit as st
from PIL import Image
import os

# Directory path
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
visacdr_image = load_image(visa_cdr_image_path)

# Recommended books and podcasts for personal growth
recommended_books = [
    {
        'title': 'Mindset: The New Psychology of Success',
        'author': 'Carol S. Dweck',
        'summary': 'Explores the concept of growth mindset and its impact on personal and professional development.'
    },
    {
        'title': 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones',
        'author': 'James Clear',
        'summary': 'Provides practical strategies for developing good habits and breaking bad ones to achieve goals.'
    },
    # Add more recommended books as needed
]

recommended_podcasts = [
    {
        'title': 'The Tim Ferriss Show',
        'host': 'Tim Ferriss',
        'summary': 'Interviews with top performers across various fields, exploring their habits and routines.'
    },
    {
        'title': 'The Tony Robbins Podcast',
        'host': 'Tony Robbins',
        'summary': 'Discussions on personal development, leadership, and achieving success in life.'
    },
    # Add more recommended podcasts as needed
]

# Title of the app
st.title("Welcome to My Teaching App")

# Description
st.write("""
    I offer lessons in five exciting areas: Swimming, Data Science, Tax Return Advice, Australia Visa Advice & Assessment, and Books & Podcasts for Personal Growth. Choose one to get started!
""")

# Options for the user to choose
option = st.selectbox(
    'What would you like to learn?',
    ('Select an option', 'Swimming Lessons', 'Data Science Teaching', 'Tax Return Advice', 'Visa & Assessment Advice', 'Books & Podcasts for Personal Growth')
)

# Display content based on the user's choice
if option == 'Swimming Lessons':
    st.header("Swimming Lessons")
    if swimming_image:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(swimming_image, caption='Learn to Swim', use_column_width=True)
        with col2:
            st.write("""
                I was a member of Iran's National Swimming Team for 8 years, and I held two national records in backstroke for a long time.
                I offer comprehensive swimming lessons for all skill levels. Whether you are a beginner or looking to improve your technique, I can help you achieve your swimming goals.
                
                **Topics Covered:**
                - Basic swimming techniques
                - Advanced strokes
                - Breathing techniques
                - Safety tips
                - Hydrotherapy: Used to treat aches and pains including headaches, muscle pain, migraines, and toothache
            """)
elif option == 'Data Science Teaching':
    st.header("Data Science Teaching")
    if datascience_image:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(datascience_image, caption='Learn Data Science', use_column_width=True)
        with col2:
            st.write("""
                I provide data science teaching that covers a wide range of topics, from the basics to advanced machine learning techniques. If you are looking to start a career in data science or enhance your skills, I can guide you through the process.
                I can teach you in different programming languages, software tools, and ML/ AI Concepts such as:

                •Cloud Technology: AWS (SageMaker Studio, AI Services)
                •Programming languages and libraries: Python (Pandas, Numpy, Matplotlib, Plotly, Seaborn, Sci-Kit Learn), R Studio, PostgreSQL, MySQL, Docker, SQLAlchemy, Tensorflow, Keras, Pytorch, Object Oriented Programming (OOP), HTML, CSS, StreamLit, FastAPI, MLFlow, CML CI/CD 
                •Tools: Microsoft Power BI, Tableau, SSIS, ETL Processes, , MS Office Suite
                •Computer Vision: CNN & Transfer Learning to apply Artificial Intelligence in Medical Diagnosis
                •Natural Language Processing NLP: Natural Language Understanding, Language Models like BERT, T5, GPT-2and GPT-3, Named Entity Recognition, Topic Modelling, Sentiment Analysis, Document Similarity, Text Classification, Text Summarization
                •Statistical Analysis: Bayesian Analysis, A/B testing, Regression, Time Series, Hypothesis testing, Sampling, T-Test, ANOVA
                
                **Topics Covered:**
                - Introduction to Data Science
                - Data Analysis with Python, SQL
                - Machine Learning
                - Data Visualization
                - Deep Learning
                - Machine Learning on Production
                - MLOps Concepts
                - Deploy ML Models

                **About Me:**
                - [Kaggle Expert](https://www.kaggle.com/homayoonkhadivi) in notebooks and datasets
                - [Professional AI/ML Scientist](https://www.linkedin.com/in/homayoon-khadivi/)
            """)
elif option == 'Visa & Assessment Advice':
    st.header("Australia Visa & Assessment Advice")
    if visacdr_image:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(visacdr_image, caption='Learn Australia Visa & Assessment', use_column_width=True)
        with col2:
            st.write("""
                I provide advice on Australian visas and assessments, covering a wide range of visa conditions and assessment requirements.
                
                **Topics Covered:**
                - Advice on PTE & IELTS English Exams
                - Obtaining certificate assessments from various Australian organizations, such as Engineers Australia
                - Over 50 positive CDR assessments without comments in all engineering fields
                - Guidance on selecting the most suitable visa based on your individual circumstances
            """)
elif option == 'Tax Return Advice':
    st.header("Tax Return Advice")
    st.write("""
        I offer comprehensive tax return advice to help you maximize your tax returns and optimize your financial situation.
        
        **Services Offered:**
        - Filing your tax return accurately and on time
        - Maximizing deductions and credits to ensure you get the highest possible return
        - Providing advice on tax planning strategies to minimize your tax liabilities
        - Guidance on how to handle specific tax situations and requirements
        
        Whether you're an individual or a small business owner, I can assist you in navigating the complexities of tax regulations and ensuring compliance while optimizing your financial outcomes.
    """)
elif option == 'Books & Podcasts for Personal Growth':
    st.header("Books & Podcasts for Personal Growth")
    st.write("""
        Explore recommended books and podcasts to enhance your personal growth journey.
    """)
    
    # Display recommended books
    st.subheader("Recommended Books")
    for book in recommended_books:
        st.write(f"**{book['title']}** by {book['author']}")
        st.write(f"*Summary:* {book['summary']}")
        st.write("---")

    # Display recommended podcasts
    st.subheader("Recommended Podcasts")
    for podcast in recommended_podcasts:
        st.write(f"**{podcast['title']}** hosted by {podcast['host']}")
        st.write(f"*Summary:* {podcast['summary']}")
        st.write("---")

# Footer
st.write("""
    Feel free to reach out if you have any questions or need more information!
""")
