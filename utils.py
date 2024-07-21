import os
from PIL import Image
import pandas as pd

# Directory path for images
image_dir = './images'

# Function to load images safely
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        return None

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
        'summary': 'Interviews with top performers across various fields, exploring their habits and routines.',
        'tag': 'Personal Development'
    },
    {
        'title': 'The Tony Robbins Podcast',
        'host': 'Tony Robbins',
        'summary': 'Discussions on personal development, leadership, and achieving success in life.',
        'tag': 'Personal Development'
    },
    # New Podcasts
    {
        'title': 'The Mindset Mentor',
        'host': 'Rob Dial',
        'summary': 'Provides actionable strategies to help you unlock your potential and overcome mental blocks.',
        'tag': 'Personal Development'
    },
    {
        'title': 'All in the Mind',
        'host': 'Rafael Epstein',
        'summary': 'Explores the fascinating world of psychology and mental health.',
        'tag': 'Psychology'
    },
    {
        'title': 'Ted Talks Daily',
        'host': 'Various',
        'summary': 'Daily episodes featuring some of the world’s leading thinkers and doers sharing their insights and ideas.',
        'tag': 'Inspirational'
    },
    {
        'title': 'The Science of Everything',
        'host': 'Various',
        'summary': 'Explains complex scientific topics in a way that’s accessible and engaging.',
        'tag': 'Science'
    },
    {
        'title': 'Stuff You Should Know',
        'host': 'Josh Clark & Chuck Bryant',
        'summary': 'Explains how things work and explores fascinating topics in a conversational manner.',
        'tag': 'Education'
    },
    {
        'title': 'The Art of Communication',
        'host': 'Various',
        'summary': 'Provides insights and strategies for improving communication skills.',
        'tag': 'Communication'
    },
    {
        'title': 'Huberman Lab',
        'host': 'Andrew Huberman',
        'summary': 'Shares cutting-edge science and practical tools to improve mental and physical health.',
        'tag': 'Health'
    },
    {
        'title': 'Gold Minds with Kevin Hart',
        'host': 'Kevin Hart',
        'summary': 'Kevin Hart interviews successful individuals from various fields to uncover their secrets to success.',
        'tag': 'Personal Development'
    },
    {
        'title': 'The Joe Rogan Experience',
        'host': 'Joe Rogan',
        'summary': 'Features long-form conversations with a diverse range of guests on a variety of topics.',
        'tag': 'General'
    },
    {
        'title': 'The Lex Fridman Podcast',
        'host': 'Lex Fridman',
        'summary': 'Interviews with experts and thought leaders in artificial intelligence, technology, and more.',
        'tag': 'Technology'
    }
]

