# This is just a very simple class to let us add, delete and show all books which is a simple list
# of dicts which contains the book title and author. Notice that we have a method that returns JSON
# back. We will need this later for our web service to send output back.
# https://dzone.com/articles/python-rest-api-example-part-1?fromrel=true

import json

class Book:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = {}
        new_book["Title"] = title
        new_book["Author"] = author
        self.books.append(new_book)
        print("Book: {0}".format(new_book))
        return json.dumps(new_book)

    def del_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            if book["Title"] == title:
                index = idx
                found = True
                del self.books[idx]
        print("books: {0}".format(json.dumps(self.books)))
        return found

    def get_all_books(self):
        return self.books

    def json_list(self):
        return json.dumps(self.books)