from book import Book

class EBook(Book):
    def __init__(self, title, auther):
        super().__init__(title, auther, total_copies=float("inf"))
    def borrow(self):
        print("Download completed successfully")
    def __str__(self):
        return f"Electronic book: {self.title}, auther: {self.auther}"