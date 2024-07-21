import streamlit as st
import pandas as pd 
from PIL import Image
import os

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

# Recommended books and podcasts for personal growth
recommended_books = [
    {
        'title': 'Emotional Intelligence',
        'author': 'Daniel Goleman',
        'summary': 'Explores the concept of emotional intelligence and its impact on personal and professional success.',
        'tag': 'Personal Development'
    },
    {
        'title': 'The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change',
        'author': 'Stephen R. Covey',
        'summary': 'Offers a principle-centered approach for solving personal and professional problems, with a focus on effectiveness.',
        'tag': 'Personal Development'
    },
    {
        'title': 'High Performance Habits: How Extraordinary People Become That Way',
        'author': 'Brendon Burchard',
        'summary': 'Provides insights and strategies for achieving high performance and success.',
        'tag': 'Personal Development'
    },
    {
        'title': 'The 10X Rule: The Only Difference Between Success and Failure',
        'author': 'Grant Cardone',
        'summary': 'Discusses the concept of taking massive action to achieve success and exceed goals.',
        'tag': 'Personal Development'
    },
    {
        'title': 'Change Your Questions, Change Your Life: 10 Powerful Tools for Life and Work, 2nd Edition, Revised and Expanded',
        'author': 'Marilee Adams',
        'summary': 'Offers tools for transforming your thinking and asking better questions to improve your life and work.',
        'tag': 'Personal Development'
    },
    {
        'title': 'Greenlights: Raucous Stories and Outlaw Wisdom from the Academy Award-Winning Actor',
        'author': 'Matthew McConaughey',
        'summary': 'A memoir filled with stories and lessons from the life of actor Matthew McConaughey.',
        'tag': 'Memoir'
    },
    {
        'title': 'Level Up: Get Focused, Stop Procrastinating and Upgrade Your Life',
        'author': 'Rob Dial',
        'summary': 'Provides strategies for overcoming procrastination and achieving personal goals.',
        'tag': 'Personal Development'
    },
    {
        'title': 'Never Finished: Unshackle Your Mind and Win the War Within',
        'author': 'David Goggins',
        'summary': 'Offers insights into mental toughness and overcoming obstacles.',
        'tag': 'Personal Development'
    },
    {
        'title': 'The 6 Habits of Growth',
        'author': 'Brendon Burchard',
        'summary': 'Focuses on habits that promote personal and professional growth.',
        'tag': 'Personal Development'
    },
    {
        'title': 'Can\'t Hurt Me: Master Your Mind and Defy the Odds',
        'author': 'David Goggins',
        'summary': 'Shares experiences and lessons from David Goggins on mental and physical resilience.',
        'tag': 'Personal Development'
    },
    {
        'title': 'Everything Is F*cked: A Book About Hope',
        'author': 'Mark Manson',
        'summary': 'Explores the complexities of hope and how to find meaning in a chaotic world.',
        'tag': 'Philosophy'
    },
    {
        'title': 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones',
        'author': 'James Clear',
        'summary': 'Provides practical strategies for developing good habits and breaking bad ones to achieve goals.',
        'tag': 'Personal Development'
    },
    {
        'title': '48 Laws of Power',
        'author': 'Robert Greene',
        'summary': 'Explores strategies for gaining and maintaining power.',
        'tag': 'Self-Help'
    },
    {
        'title': 'Becoming',
        'author': 'Michelle Obama',
        'summary': 'A memoir by former First Lady Michelle Obama, reflecting on her life and experiences.',
        'tag': 'Memoir'
    },
    {
        'title': 'The Decision: Overcoming Today\'s BS for Tomorrow\'s Success',
        'author': 'Kevin Hart',
        'summary': 'Kevin Hart shares his journey and insights into overcoming challenges and achieving success.',
        'tag': 'Memoir'
    },
    {
        'title': 'The Power of Body Language',
        'author': 'Joe Navarro',
        'summary': 'Explores how body language can influence interactions and communication.',
        'tag': 'Self-Help'
    },
    {
        'title': 'Endure: How to Work Hard, Outlast and Keep Hammering',
        'author': 'Cameron Hanes',
        'summary': 'Offers insights into building resilience and endurance through hard work.',
        'tag': 'Personal Development'
    },
    {
        'title': 'Magic Words: What You Say Matters',
        'author': 'Jonah Berger',
        'summary': 'Discusses the impact of language on behavior and decision-making.',
        'tag': 'Self-Help'
    },
    {
        'title': 'I Can\'t Make This Up: Life Lessons',
        'author': 'Kevin Hart',
        'summary': 'Kevin Hart shares humorous and inspirational stories from his life.',
        'tag': 'Memoir'
    },
    {
        'title': 'Undisputed Truth: My Autobiography',
        'author': 'Mike Tyson',
        'summary': 'Mike Tyson’s autobiography detailing his life and career in boxing.',
        'tag': 'Memoir'
    },
    {
        'title': 'Born a Crime: Stories from a South African Childhood',
        'author': 'Trevor Noah',
        'summary': 'Trevor Noah’s memoir about growing up in South Africa during apartheid.',
        'tag': 'Memoir'
    }
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
elif option == 'Data Science Teaching':
    st.header("Data Science Teaching")
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
elif option == 'Visa & Assessment Advice':
    st.header("Australia Visa & Assessment Advice")
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
elif option == 'Tax Return Advice':
    st.header("Tax Return Advice")
    st.write("""
   Are you looking to maximize your tax returns and optimize your financial situation? As a professional tax return advisor, I offer comprehensive tax return advice to help you make the most of your taxes.

    **Services Offered:**
    - Filing your tax return accurately and on-time
    - Maximizing deductions and credits to ensure you get the highest possible return
    - Providing advice on tax planning strategies to minimize your tax liabilities
    - Offering guidance on how to handle specific tax situations and requirements

    Whether you're an individual or a small business owner, I can assist you in navigating the complexities of tax regulations and ensuring compliance while optimizing your financial outcomes. Let me help you get back the tax you deserve!
    """)
elif option == 'Books & Podcasts for Personal Growth':
    st.header("Books & Podcasts for Personal Growth")
    st.write("""
    **My Reading Journey 📚**
    
    I wasn’t always a fan of reading. In fact, I used to find it quite challenging to sit down with a book. However, something changed, and now, I make it a point to read a book every month. This simple habit has had a profound impact on my life, offering new perspectives and valuable lessons. I’m excited to share some of the books that have transformed my mindset and growth.
    """)
    
    # Display recommended books as a table
    st.subheader("Recommended Books")
    books_df = pd.DataFrame(recommended_books)
    st.write(books_df)

    # Display recommended podcasts as a table
    st.subheader("Recommended Podcasts")
    podcasts_df = pd.DataFrame(recommended_podcasts)
    st.write(podcasts_df)

# Footer
#st.write("""
#Feel free to reach out if you have any questions or need more information!
#""")
