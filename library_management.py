class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_borrowed = False  # وضعیت اولیه: کتاب موجوده، امانت نرفته

    @property
    def is_borrowed(self):
        # getter: وقتی کسی بنویسه book.is_borrowed، این مقدار رو برمی‌گردونه
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, value: bool):
        # setter: وقتی کسی بنویسه book.is_borrowed = True/False، این متد اجرا میشه
        if value == False:
            # کاربر می‌خواد کتاب رو پس بده
            if self._is_borrowed is False:
                # کتاب از قبل موجود بود، پس دادن بی‌معنیه
                print("Book was already available")
            else:
                # کتاب واقعاً امانت رفته بود، حالا داره پس داده میشه
                print("The book is taken back")
                self._is_borrowed = False
        elif value == True:
            # کاربر می‌خواد کتاب رو امانت بگیره
            if self._is_borrowed is True:
                # کتاب از قبل امانت رفته، نمیشه دوباره امانت داد
                print("The book was lent")
            else:
                # کتاب موجود بود، حالا با موفقیت امانت داده میشه
                print("Book borrowed successfully")
                self._is_borrowed = True

    def __str__(self):
        # نمایش خوانا از اطلاعات کتاب هنگام print کردن
        return f"Title:{self.title}, Author:{self.author}, International Standard Book Number:{self.isbn}, Borrowed:{self._is_borrowed}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrow_books = []  # لیست کتاب‌هایی که این عضو الان دستشه

    def borrow_book(self, book):
        # عضو می‌خواد یک کتاب رو امانت بگیره
        if book not in self.borrow_books:
            self.borrow_books.append(book)  # کتاب رو به لیست خودش اضافه می‌کنه
            book.is_borrowed = True         # وضعیت خود کتاب رو هم آپدیت می‌کنه (sync)
        else:
            print("this book already borrowed")

    def return_book(self, book):
        # عضو می‌خواد یک کتاب رو پس بده
        if book not in self.borrow_books:
            # اگه این کتاب اصلاً دست این عضو نبوده، خطا بده
            raise ValueError("This book is not lent")
        else:
            self.borrow_books.remove(book)  # کتاب رو از لیست خودش حذف می‌کنه
            book.is_borrowed = False        # وضعیت خود کتاب رو هم آپدیت می‌کنه (sync)


class Library:
    def __init__(self):
        self.books = []    # همه کتاب‌های موجود تو کتابخونه
        self.members = []  # همه اعضای ثبت‌شده تو کتابخونه

    def add_book(self, book):
        # یک کتاب جدید رو به کتابخونه اضافه می‌کنه
        self.books.append(book)

    def register_member(self, member):
        # یک عضو جدید رو تو کتابخونه ثبت می‌کنه
        self.members.append(member)

    def find_book_by_isbn(self, isbn):
        # روی همه کتاب‌ها می‌گرده تا کتابی با isbn مشخص پیدا کنه
        for book in self.books:
            if isbn == book.isbn:
                return book  # همین که پیدا شد، برش می‌گردونه و حلقه متوقف میشه
        return None  # اگه حلقه تموم شد و چیزی پیدا نشد

    def lend_book(self, member, isbn):
        # کتابخونه واسطه میشه بین عضو و کتاب برای عملیات امانت
        book = self.find_book_by_isbn(isbn)
        if book == None:
            print("Book is not available")
        else:
            member.borrow_book(book)  # مسئولیت رو به Member می‌سپاره

    def return_book(self, member, isbn):
        # کتابخونه واسطه میشه بین عضو و کتاب برای عملیات پس دادن
        book = self.find_book_by_isbn(isbn)
        if book == None:
            print("Book not found")
        else:
            member.return_book(book)  # مسئولیت رو به Member می‌سپاره

# ساخت کتابخانه
lib = Library()

# ساخت چند کتاب
b1 = Book("1984", "George Orwell", "111")
b2 = Book("Brave New World", "Aldous Huxley", "222")

lib.add_book(b1)
lib.add_book(b2)

# ساخت یک عضو
m1 = Member("Ali", "M001")
lib.register_member(m1)

# امانت گرفتن کتاب
lib.lend_book(m1, "111")   # باید "Book borrowed successfully" چاپ کنه
print(b1)                   # باید Borrowed:True نشون بده

# تلاش برای امانت گرفتن دوباره همون کتاب توسط یکی دیگه
m2 = Member("Sara", "M002")
lib.register_member(m2)
lib.lend_book(m2, "111")    # باید "The book was lent" چاپ کنه (چون از قبل امانت رفته)

# پس دادن کتاب
lib.return_book(m1, "111")  # باید "The book is taken back" چاپ کنه
print(b1)                    # باید Borrowed:False نشون بده

# جستجوی کتابی که وجود نداره
lib.lend_book(m1, "999")    # باید "Book is not available" چاپ کنه