# We import the Book class we defined in the last part so that we can work with books. Next, we import
# three handlers that we will define in the next part of this series.
# Next, we define the MainHandler class, which is derived from tornado.web.RequestHandler. This is a
# very basic version of a RequestHandler that will just return "Book Microservice v1" to the browser.
# https://dzone.com/articles/python-rest-api-example-part-2

import tornado.ioloop
import tornado.web
from book import Book
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

# books inherits from Book class
books = Book()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Book Microservice v1")


def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addbook", AddHandler, dict(books = books)),
        (r"/v1/delbook", DelHandler, dict(books = books)),
        (r"/v1/getbooks", GetHandler, dict(books = books)),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()