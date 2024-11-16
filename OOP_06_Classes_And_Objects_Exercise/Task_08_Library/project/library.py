from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # author: [book1, book2, book3]
        self.rented_books = {}  # username: {book_name: days_to_return}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available.keys() and book_name in self.books_available[author]:
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            days = 0
            for user, books in self.rented_books.items():
                if book_name in books.keys():
                    days = books[book_name]
            return f"The book \"{book_name}\" is already rented and will be available in " \
                   f"{days} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
