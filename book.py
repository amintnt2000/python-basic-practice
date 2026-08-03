class Book:
    def __init__(self, title, auther, total_copies):
        self.title = title
        self.auther = auther
        self.total_copies = total_copies
        self._available_copies = self.total_copies
    @property
    def available_copies(self):
        return self._available_copies
    def borrow(self):
        if self._available_copies <= 0:
            print("Not enough book")
        else:
            self._available_copies -= 1
    def return_book(self):
        if self.total_copies > self._available_copies:
            self._available_copies += 1
        else:
            print("Can not add another book")
    def __str__(self):
        return f"title: {self.title}, auther: {self.auther}, available copies: {self._available_copies} of {self.total_copies}"

