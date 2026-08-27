from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

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
        if value is False:
            # کاربر می‌خواد کتاب رو پس بده
            if self._is_borrowed is False:
                # کتاب از قبل موجود بود، پس دادن بی‌معنیه
                print("Book was already available")
            else:
                # کتاب واقعاً امانت رفته بود، حالا داره پس داده میشه
                print("The book is taken back")
                self._is_borrowed = False
        elif value is True:
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


class LibraryLogic:
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
        if book is None:
            print("Book is not available")
        else:
            member.borrow_book(book)  # مسئولیت رو به Member می‌سپاره

    def return_book(self, member, isbn):
        # کتابخونه واسطه میشه بین عضو و کتاب برای عملیات پس دادن
        book = self.find_book_by_isbn(isbn)
        if book is None:
            print("Book not found")
        else:
            member.return_book(book)  # مسئولیت رو به Member می‌سپارهساخت کتابخانه
    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
lib = LibraryLogic()

class BookResponse(BaseModel):
    title:str
    author: str
    isbn: int
    is_borrowed: bool
class CreateBookRequest(BaseModel):
    title : str = Field(min_length=1)
    author : str = Field(min_length=1)
    isbn : int = Field(gt=0)
@app.post("/books")
def book_create(request:CreateBookRequest):
    new_book = Book(request.title, request.author, request.isbn)
    lib.add_book(new_book)
    return {"message":"New book added",
            "title":new_book.title,
            "author":new_book.author,
            "isbn":new_book.isbn}
@app.get("/books", response_model=list[BookResponse])
def get_all_books():
    return lib.books

class CreateMemberRequest(BaseModel):
    name:str = Field(min_length=3)
    member_id:int = Field(gt=0)
class MemberResponse(BaseModel):
    name: str
    member_id: int
@app.post("/members")
def member_create(request:CreateMemberRequest):
    new_member = Member(request.name, request.member_id)
    lib.register_member(new_member)
    return {"message": "New member added",
            "name": request.name,
            "member_id": request.member_id}
@app.get("/members", response_model=list[MemberResponse])
def get_all_members():
    return lib.members

class LendRequest(BaseModel):
    member_id: int
    isbn: int
@app.post("/lend")
def lend_book(request:LendRequest):
    member = lib.find_member_by_id(request.member_id)
    book = lib.find_book_by_isbn(request.isbn)
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    member.borrow_book(book)
    return {"message": "Book lend successful"}
@app.post("/return")
def return_book(request:LendRequest):
    member = lib.find_member_by_id(request.member_id)
    book = lib.find_book_by_isbn(request.isbn)
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    try:
        member.return_book(book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Book return to library"}
