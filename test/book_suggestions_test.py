# this is the "test/book_suggestions_test.py" file...

from app.book_suggestions import search_books, display_book_details, suggest_random_book


# Function to test search for books, return dictionary
def test_search_books():
    data = search_books("fiction")
    assert isinstance(data, list) 

