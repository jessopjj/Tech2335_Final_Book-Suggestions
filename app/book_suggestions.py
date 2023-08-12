import requests
import random

from app.alpha import API_KEY

# Base URL for Google Books API
BASE_URL = 'https://www.googleapis.com/books/v1/volumes'

# Function to search for books
def search_books(query):
    params = {'q': query, 'key': API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

# Function to display book details
def display_book_details(book):
    volume_info = book.get('volumeInfo', {})
    title = volume_info.get('title', 'No Title')
    authors = volume_info.get('authors', ['Unknown Author'])
    description = volume_info.get('description', 'No description available')
    print(f"Title: {title}")
    print(f"Authors: {', '.join(authors)}")
    print(f"Description: {description}")
    print("=" * 20)

# Function to suggest a random book
def suggest_random_book(books_data):
    if 'items' in books_data:
        random_book = random.choice(books_data['items'])
        display_book_details(random_book)
    else:
        print("Sorry, no books found for your query.")


# Prompt the user for input
user_query = input("Enter a genre or title to search for: ")

# Search for books based on user input
books_data = search_books(user_query)

# Display search results
print("Search Results:")
for index, book in enumerate(books_data.get('items', []), start=1):
    volume_info = book.get('volumeInfo', {})
    title = volume_info.get('title', 'No Title')
    authors = volume_info.get('authors', ['Unknown Author'])
    print(f"{index}. Title: {title}")
    print(f"   Authors: {', '.join(authors)}")
    print("=" * 20)


print("Woah! These are are a lot of books. Which one should you start with?")

# Ask if the user wants a random book suggestion
random_choice = input("Do you want a random book suggestion? (ofc/no): ")
if random_choice.lower() == 'ofc':
    suggest_random_book(books_data)
else:
    print("Okay! Enjoy the list above!")