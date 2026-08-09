# 🏦 سیستم بانکی ساده (Simple Banking System)

یک پروژه پایتون برای شبیه‌سازی عملیات پایه‌ای بانکی، با تمرکز بر Custom Exceptions و مدیریت خطا.

## 🎯 هدف پروژه

این پروژه به‌عنوان دومین تمرین جمع‌بندی OOP نوشته شده و روی مفاهیم زیر تمرکز دارد:

- تعریف Exception های سفارشی (Custom Exceptions)
- Encapsulation و validation با `@property`
- هماهنگی بین چند کلاس برای انجام یک عملیات ترکیبی (انتقال وجه)
- مدیریت دیکشنری برای نگهداری آبجکت‌ها با کلید یکتا

## 🏗️ ساختار پروژه

### Custom Exceptions

```python
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass
```

دو نوع خطای اختصاصی که به‌جای `ValueError` عمومی استفاده می‌شوند تا خطاها معنادارتر و قابل تفکیک باشند.

### `Account`
نماینده یک حساب بانکی است.

- **Attributes:** `owner_name`, `account_number`, `balance` (از طریق property مدیریت می‌شود), `transaction_history`
- **متدها:**
  - `deposit(amount)`: واریز پول؛ در صورت مقدار نامعتبر (صفر یا منفی) خطای `InvalidAmountError` می‌دهد
  - `withdraw(amount)`: برداشت پول؛ در صورت موجودی ناکافی خطای `InsufficientFundsError` و در صورت مقدار نامعتبر خطای `InvalidAmountError` می‌دهد
  - هر تراکنش موفق در `transaction_history` ثبت می‌شود

### `Bank`
هماهنگ‌کننده بین حساب‌های مختلف.

- **Attributes:** `accounts` (دیکشنری از شماره حساب به آبجکت `Account`)
- **متدها:**
  - `create_account(owner_name)`: حساب جدید با شماره یکتا می‌سازد و آن را برمی‌گرداند
  - `find_account(account_number)`: حساب را با شماره پیدا می‌کند (در صورت نبود، `None` برمی‌گرداند)
  - `transfer(from_account_number, to_account_number, amount)`: با استفاده از `withdraw` و `deposit`، پول را بین دو حساب منتقل می‌کند

## 🚀 نحوه استفاده

```python
from bank import Bank, InsufficientFundsError, InvalidAmountError

bank = Bank()

# ساخت حساب‌ها
acc1 = bank.create_account("Ali")
acc2 = bank.create_account("Sara")

# واریز اولیه
acc1.deposit(1000)

# انتقال وجه
bank.transfer(acc1.account_number, acc2.account_number, 300)

# مدیریت خطا
try:
    bank.transfer(acc1.account_number, acc2.account_number, 10000)
except InsufficientFundsError as e:
    print(f"خطا: {e}")
```

## 📋 خروجی نمونه

```
Owner name:Ali, Account id:1 , Account balance:1000
Owner name:Ali, Account id:1 , Account balance:700
Owner name:Sara, Account id:2 , Account balance:300
خطا: Insufficient funds for this withdrawal.
خطا: The destination account does not exist.
خطا: Deposit amount must be positive.
['Deposit:1000', 'Withdraw:300']
```

## 🧠 نکات آموزشی

1. **Custom Exceptions:** به‌جای یکی‌کاسه کردن همه خطاها با `ValueError`، هر نوع خطا (مقدار نامعتبر در برابر موجودی ناکافی) کلاس اختصاصی خودش را دارد که مدیریت دقیق‌تر خطا در سمت کد فراخواننده را ممکن می‌کند.
2. **Delegation:** متد `transfer` در `Bank` مستقیماً `balance` را دستکاری نمی‌کند؛ این کار را به متدهای `withdraw` و `deposit` خود کلاس `Account` می‌سپارد که خودشان validation دارند.
3. **جستجو با دیکشنری:** استفاده از دیکشنری (به‌جای لیست) برای نگهداری حساب‌ها، جستجو با شماره حساب را در زمان ثابت (O(1)) ممکن می‌کند، برخلاف پروژه کتابخانه که با حلقه `for` روی لیست جستجو می‌شد.

## 🔜 مراحل بعدی

- تبدیل این پروژه به یک REST API با استفاده از **FastAPI**
- افزودن پایگاه داده برای ذخیره‌سازی دائمی
- افزودن قابلیت‌هایی مثل نرخ سود، تاریخچه با timestamp، و احراز هویت کاربر

---

ساخته شده به‌عنوان بخشی از مسیر یادگیری پایتون در راستای هدف نهایی توسعه ML/AI و FastAPI.
