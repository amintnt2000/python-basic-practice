# ⚡ FastAPI - سیستم مدیریت کاربران (User Management API)

اولین پروژه FastAPI، پیاده‌سازی یک REST API کامل با عملیات CRUD (Create, Read, Update, Delete) برای مدیریت کاربران.

## 🎯 هدف پروژه

این پروژه به‌عنوان اولین تجربه با FastAPI نوشته شده و مفاهیم زیر را پوشش می‌دهد:

- ساخت route های GET، POST، PUT، و DELETE
- Path Parameters و Query Parameters
- Validation خودکار با Pydantic و `Field`
- مدیریت خطای HTTP استاندارد با `HTTPException`
- ذخیره‌سازی موقت داده در حافظه (In-Memory Storage)
- مستندات خودکار و تعاملی (Swagger UI)

## 🏗️ ساختار پروژه

### مدل داده (`User`)

```python
class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=120)
    email: str = Field(min_length=5)
```

هر کاربر شامل نام (حداقل ۲ کاراکتر)، سن (بین ۰ تا ۱۲۰)، و ایمیل (حداقل ۵ کاراکتر) است. Pydantic به‌طور خودکار این محدودیت‌ها را روی هر درخواست ورودی اعمال می‌کند.

### Endpoint ها

| متد | آدرس | توضیح |
|---|---|---|
| `POST` | `/users` | ساخت کاربر جدید |
| `GET` | `/users` | دریافت لیست همه کاربران |
| `GET` | `/users/{user_id}` | دریافت یک کاربر خاص با شناسه |
| `PUT` | `/users/{user_id}` | ویرایش اطلاعات یک کاربر موجود |
| `DELETE` | `/users/{user_id}` | حذف یک کاربر |

هر کاربر هنگام ساخت، یک `id` یکتا و خودکار دریافت می‌کند.

## 🚀 نحوه اجرا

### نصب:
```bash
pip install fastapi uvicorn
```

### اجرا:
```bash
uvicorn main:app --reload
```

### دسترسی به مستندات تعاملی:
```
http://127.0.0.1:8000/docs
```

## 📋 مثال استفاده

**ساخت کاربر جدید:**
```
POST /users
Body: {"name": "Amin", "age": 25, "email": "amin@test.com"}
```

**دریافت همه کاربران:**
```
GET /users
```

**دریافت یک کاربر خاص:**
```
GET /users/1
```

**ویرایش کاربر:**
```
PUT /users/1
Body: {"name": "Amin Updated", "age": 26, "email": "amin@test.com"}
```

**حذف کاربر:**
```
DELETE /users/1
```

## 🧠 نکات آموزشی

1. **تفاوت GET و POST در تست:** درخواست‌های POST/PUT/DELETE را نمی‌توان مستقیم از نوار آدرس مرورگر تست کرد (چون مرورگر همیشه GET می‌فرستد)؛ باید از Swagger UI یا ابزارهایی مثل Postman استفاده شود.

2. **اهمیت Type Hints:** با نوشتن `user_id: int` به‌جای `user_id` ساده، FastAPI به‌طور خودکار مقدار ورودی را به نوع درست تبدیل و اعتبارسنجی می‌کند؛ بدون آن، مقایسه‌های عددی (مثل جستجوی id) به‌درستی کار نمی‌کنند.

3. **HTTPException در مقابل Exception های سفارشی:** برخلاف پروژه‌های OOP قبلی که از `raise CustomError(...)` استفاده می‌شد، در FastAPI برای برگرداندن خطای قابل‌فهم به کاربر نهایی API، از `HTTPException` با یک `status_code` استاندارد (مثل ۴۰۴) استفاده می‌شود.

4. **ترکیب Path و Body Parameter:** در `update_user(user_id: int, updated_user: User)`، FastAPI به‌طور خودکار تشخیص می‌دهد که `user_id` باید از مسیر URL و `updated_user` باید از بدنه درخواست خوانده شود.

## ⚠️ محدودیت فعلی

داده‌ها فقط در حافظه (RAM) نگهداری می‌شوند و با هر بار ری‌استارت سرور، از بین می‌روند. این مناسب یادگیری است، اما برای استفاده واقعی نیاز به یک پایگاه داده دارد.

## 🔜 مراحل بعدی

- اتصال به پایگاه داده واقعی (مثل SQLite یا PostgreSQL) با SQLAlchemy یا SQLModel
- افزودن احراز هویت کاربر (Authentication)
- تبدیل پروژه‌های قبلی OOP (کتابخانه، بانک، فروشگاه) به API با FastAPI

---

ساخته شده به‌عنوان بخشی از مسیر یادگیری پایتون در راستای هدف نهایی توسعه ML/AI.
