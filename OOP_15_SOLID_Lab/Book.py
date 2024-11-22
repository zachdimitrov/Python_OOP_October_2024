class Book:
    def __init__(self, title, author, location):
        self.author = author
        self.title = title
        self.page = 0

    def turn_page(self, page):
        self.page = page

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 2:
            raise ValueError("Title must be longer than 2 symbols!")
        self.__title = value


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, title):
        return next((b for b in self.books if b.title == title), None)

    def edit_book(self, title, author, new_title):
        book = next((b for b in self.books if b.title == title and b.author == author), None)
        if book:
            book.title = new_title
        else:
            raise IndexError("No such book")
