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

    st.write("### Share Your Book and Podcast Recommendations")
    with st.form("recommendation_form"):
        st.write("**Submit your recommendations for books or podcasts!**")
        title = st.text_input("Title", key="recommendation_title")
        author_host = st.text_input("Author/Host", key="recommendation_author_host")
        summary = st.text_area("Summary", key="recommendation_summary")
        tag = st.selectbox("Tag",
                           ["Personal Development", "Memoir", "Self-Help", "Science", "Education", "Mental Health",
                            "Inspiration", "Varied"], key="recommendation_tag")
        type_of_recommendation = st.selectbox("Type of Recommendation", ["Book", "Podcast"], key="recommendation_type")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Initialize session state if it does not exist
            if 'books' not in st.session_state:
                st.session_state['books'] = recommended_books
            if 'podcasts' not in st.session_state:
                st.session_state['podcasts'] = recommended_podcasts

            # Add recommendation based on type
            if type_of_recommendation == 'Book':
                st.session_state['books'].append({
                    'title': title,
                    'author': author_host,
                    'summary': summary,
                    'tag': tag
                })
            else:
                st.session_state['podcasts'].append({
                    'title': title,
                    'host': author_host,
                    'summary': summary,
                    'tag': tag
                })

            # Optionally, update the display
            st.write("Thank you for your recommendation!")
            st.write(pd.DataFrame(st.session_state['books']))
            st.write(pd.DataFrame(st.session_state['podcasts']))
