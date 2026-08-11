# 🛒 سیستم فروشگاه و سبد خرید (Store & Cart System)

یک پروژه پایتون برای شبیه‌سازی مدیریت موجودی کالا و فرآیند خرید، با استفاده از سه کلاس مرتبط به هم.

## 🎯 هدف پروژه

سومین و پیچیده‌ترین تمرین جمع‌بندی OOP، با تمرکز بر:

- مدیریت موجودی (Inventory) به‌جای وضعیت ساده True/False
- هماهنگی بین سه کلاس مجزا (Product, Cart, Store)
- چند نوع Exception اختصاصی برای سناریوهای مختلف خطا
- کار با دیکشنری برای نگهداری کالاها با کلیدهای معنادار (اسم محصول)

## 🏗️ ساختار پروژه

### Custom Exceptions

```python
class OutOfStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class ThereIsNoItemError(Exception):
    pass
```

هر کدام برای یک سناریوی خطای مشخص:
- `OutOfStockError`: موجودی انبار برای انجام عملیات کافی نیست
- `InvalidQuantityError`: مقدار ورودی (تعداد) نامعتبر است (صفر یا منفی)
- `ThereIsNoItemError`: تلاش برای حذف کالایی که در سبد خرید وجود ندارد

### `Product`
نماینده یک کالا در انبار فروشگاه است.

- **Attributes:** `name`, `price`, `quantity`
- **متدها:**
  - `reduce_stock(amount)`: کاهش موجودی هنگام فروش؛ در صورت کمبود موجودی `OutOfStockError` می‌دهد
  - `add_stock(amount)`: افزایش موجودی هنگام ورود کالای جدید

### `Cart`
نماینده سبد خرید یک مشتری است.

- **Attributes:** `items` (دیکشنری از آبجکت `Product` به تعداد درخواستی)
- **متدها:**
  - `add_item(product, quantity)`: افزودن کالا به سبد (در صورت وجود قبلی، تعداد جمع می‌شود)
  - `remove_item(product)`: حذف کامل یک کالا از سبد
  - `total_price()`: محاسبه مجموع قیمت تمام کالاهای سبد

### `Store`
هماهنگ‌کننده بین موجودی انبار و سبدهای خرید مشتریان.

- **Attributes:** `products` (دیکشنری از نام محصول به آبجکت `Product`)
- **متدها:**
  - `add_product(product)`: افزودن کالای جدید به فروشگاه
  - `find_product(name)`: جستجوی کالا با نام (در صورت نبود، `None` برمی‌گرداند)
  - `checkout(cart)`: پردازش نهایی خرید — موجودی هر کالا را کم می‌کند و مبلغ کل را برمی‌گرداند

## 🚀 نحوه استفاده

```python
from store import Store, Cart, Product, OutOfStockError

store = Store()

# افزودن محصولات
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 20, 50)
store.add_product(p1)
store.add_product(p2)

# ساخت سبد خرید
cart = Cart()
cart.add_item(p1, 2)
cart.add_item(p2, 5)

# تسویه حساب
total = store.checkout(cart)
print(f"Total charged: {total}")
```

## 📋 خروجی نمونه

```
Total charged: 2100.0
Product Name: Laptop, Product Price: 1000, Product Stock: 3
Product Name: Mouse, Product Price: 20, Product Stock: 45
خطا: Product is out of stock
```

## 🧠 نکات آموزشی

1. **تفکیک دقیق Exception ها:** برای دو سناریوی مشابه ولی مفهوماً متفاوت (مقدار نامعتبر در برابر موجودی ناکافی)، استفاده از دو کلاس Exception جدا خوانایی و قابلیت مدیریت خطا را بهبود می‌دهد.
2. **تفاوت attribute و متد دیکشنری:** نکته‌ای که در این پروژه به‌طور مستقیم تمرین شد: `cart.items` (خود دیکشنری) در مقابل `cart.items.items()` (پیمایش جفت‌های کلید-مقدار).
3. **هماهنگی سه کلاس:** برخلاف پروژه‌های قبلی که دو کلاس با هم کار می‌کردند، اینجا `Store` باید هم‌زمان با `Product` و `Cart` هماهنگ شود — نمونه‌ای نزدیک‌تر به پیچیدگی پروژه‌های واقعی.

## 🔜 مراحل بعدی

- تبدیل این پروژه به REST API با **FastAPI**
- افزودن تخفیف و کوپن به `Cart`
- افزودن پایگاه داده برای ذخیره‌سازی دائمی موجودی

---

ساخته شده به‌عنوان بخشی از مسیر یادگیری پایتون در راستای هدف نهایی توسعه ML/AI و FastAPI.
