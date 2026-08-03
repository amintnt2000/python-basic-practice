class Library:
    def __init__(self):
        self.books = []
    def add_books(self, book):
        self.books.append(book)
    def show_all_books(self):
        for book in self.books:
            print(book)