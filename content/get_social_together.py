import streamlit as st

def display_get_social_together():
    st.header("Get Social Together")
    st.write("""
    I don't drink or smoke, but there are plenty of fun activities to do together with a smile!
     Here are some activities you might enjoy:
    """)

    # Options for activities
    activities = [
        'Running in Nature',
        'Nature Exploration',
        'Running',
        'Swimming',
        'Yoga',
        'Badminton',
        'Squash',
        'Basketball',
        'Snorkeling',
        'Diving',
        'Cold Bath',
        'Swimming in Cold Ocean',
        'Playing Video Games',
        'Board Games',
        'Music Festival',
        'Techno & House Party',
        'Modern Art Exhibition',
        'Concert & Theater'
    ]

    # Create checkboxes for each activity with a unique key
    selected_activities = []
    for i, activity in enumerate(activities):
        if st.checkbox(activity, key=f"checkbox_{i}"):
            selected_activities.append(activity)

    # If any activities are selected, provide Facebook and Instagram links
    if selected_activities:
        st.write("Great choices! If you want to connect and make friends, feel free to reach me out on social media:")
        st.write("**Facebook:** [Your Facebook Link](https://www.facebook.com/homayoon.khadivi.7)")
        st.write("**Instagram:** [Your Instagram Link](https://www.instagram.com/homayoon.khadivi/)")
