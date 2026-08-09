# 📚 سیستم مدیریت کتابخانه (Library Management System)

یک پروژه ساده به زبان پایتون برای شبیه‌سازی عملکردهای اصلی یک کتابخانه، با استفاده از مفاهیم برنامه‌نویسی شی‌گرا (OOP).

## 🎯 هدف پروژه

این پروژه به‌عنوان یک تمرین جمع‌بندی برای مفاهیم OOP در پایتون نوشته شده و موارد زیر را در بر می‌گیرد:

- تعریف کلاس و ساخت آبجکت
- Encapsulation با `@property` و `@setter`
- ارتباط بین چند کلاس (Composition)
- تفویض مسئولیت بین کلاس‌ها (Delegation)
- مدیریت وضعیت (State Management)

## 🏗️ ساختار پروژه

پروژه از سه کلاس اصلی تشکیل شده است:

### `Book`
نماینده یک کتاب در کتابخانه است.

- **Attributes:** `title`, `author`, `isbn`, `is_borrowed`
- وضعیت امانت کتاب (`is_borrowed`) از طریق `@property` مدیریت می‌شود و منطق زیر را پیاده‌سازی می‌کند:
  - جلوگیری از امانت دادن کتابی که از قبل امانت رفته
  - جلوگیری از پس گرفتن کتابی که اصلاً امانت نرفته

### `Member`
نماینده یک عضو کتابخانه است.

- **Attributes:** `name`, `member_id`, `borrow_books` (لیست کتاب‌های امانت‌گرفته‌شده)
- **متدها:**
  - `borrow_book(book)`: کتاب را امانت می‌گیرد و وضعیت کتاب را به‌روزرسانی می‌کند
  - `return_book(book)`: کتاب را پس می‌دهد و وضعیت کتاب را به‌روزرسانی می‌کند

### `Library`
نقش هماهنگ‌کننده (Coordinator) بین کتاب‌ها و اعضا را دارد.

- **Attributes:** `books` (لیست همه کتاب‌ها), `members` (لیست همه اعضا)
- **متدها:**
  - `add_book(book)`: افزودن کتاب جدید به کتابخانه
  - `register_member(member)`: ثبت عضو جدید
  - `find_book_by_isbn(isbn)`: جستجوی کتاب بر اساس شماره ISBN
  - `lend_book(member, isbn)`: امانت دادن کتاب به یک عضو
  - `return_book(member, isbn)`: پس گرفتن کتاب از یک عضو

## 🚀 نحوه استفاده

```python
from library import Library, Book, Member

# ساخت کتابخانه
lib = Library()

# افزودن کتاب‌ها
b1 = Book("1984", "George Orwell", "111")
b2 = Book("Brave New World", "Aldous Huxley", "222")
lib.add_book(b1)
lib.add_book(b2)

# ثبت عضو
m1 = Member("Ali", "M001")
lib.register_member(m1)

# امانت گرفتن کتاب
lib.lend_book(m1, "111")

# پس دادن کتاب
lib.return_book(m1, "111")
```

## 📋 خروجی نمونه

```
Book borrowed successfully
Title:1984, Author:George Orwell, International Standard Book Number:111, Borrowed:True
The book is taken back
Title:1984, Author:George Orwell, International Standard Book Number:111, Borrowed:False
```

## 🧠 نکات آموزشی

این پروژه چند مفهوم کلیدی OOP را در عمل نشان می‌دهد:

1. **Encapsulation:** به‌جای دسترسی مستقیم به `_is_borrowed`، همه تغییرات از طریق `@property`/`@setter` انجام می‌شود که امکان اعتبارسنجی (validation) و پیام‌های مناسب را فراهم می‌کند.
2. **Delegation:** کلاس `Library` مستقیماً وضعیت کتاب را تغییر نمی‌دهد؛ این کار را به `Member` می‌سپارد که خودش هم آن را به `Book` واگذار می‌کند.
3. **Single Responsibility:** هر کلاس فقط مسئول کاری است که به آن مربوط می‌شود.

## 🔜 مراحل بعدی

- تبدیل این پروژه به یک REST API با استفاده از **FastAPI**
- افزودن پایگاه داده (Database) برای ذخیره‌سازی دائمی اطلاعات
- افزودن قابلیت‌هایی مثل تاریخ سررسید امانت و جریمه تأخیر

---

ساخته شده به‌عنوان بخشی از مسیر یادگیری پایتون در راستای هدف نهایی توسعه ML/AI و FastAPI.
