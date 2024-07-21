import streamlit as st
import pandas as pd
from utils import recommended_books, recommended_podcasts


def display_books_podcasts():
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

    st.write("### Share Your Book Recommendations")
    with st.form("recommendation_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        summary = st.text_area("Summary")
        tag = st.selectbox("Tag", ["Personal Development", "Memoir", "Self-Help", "Other"])
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Append new book recommendation to the list
            recommended_books.append({
                'title': title,
                'author': author,
                'summary': summary,
                'tag': tag
            })
            # Optionally, update the display
            st.write("Thank you for your recommendation!")
            st.write(pd.DataFrame(recommended_books))
