import requests
from random import sample


def get_books():
    url = "https://www.googleapis.com/books/v1/volumes?q={}+intitle:{}".
    format("black deaf culture", "Black")
    books = requests.get(url)
    books_data = books.json()
    individual_books = books_data['items']
    books_list = []
    for book in individual_books:
        books_list.append([book['volumeInfo']['title'],
                           book['volumeInfo']['infoLink']])

    results = sample(books_list, 3)

    return results
