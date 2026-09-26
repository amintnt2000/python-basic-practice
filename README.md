# Breast Cancer Classification — Scikit-learn Pipeline

پروژه‌ی کوچیکی برای تمرین چرخه‌ی کامل Scikit-learn: پیش‌پردازش، مدل‌سازی، ارزیابی، Cross-validation و ذخیره‌ی مدل.

## هدف

پیش‌بینی خوش‌خیم (benign) یا بدخیم (malignant) بودن تومور پستان، با استفاده از دیتاست استاندارد `load_breast_cancer` در Scikit-learn.

## مراحل کد

1. **بارگذاری داده**: دیتاست `breast_cancer` به‌صورت DataFrame بارگذاری می‌شه و ستون `target` از بقیه‌ی ویژگی‌ها (`X`) جدا می‌شه.

2. **تقسیم Train/Test**: با `train_test_split` (نسبت ۸۰/۲۰) داده به دو بخش train و test تقسیم می‌شه.

3. **Pipeline**: دو مرحله داره:
   - `StandardScaler`: مقیاس‌بندی ویژگی‌ها (میانگین صفر، انحراف معیار یک)
   - `RandomForestClassifier`: مدل کلاسیفیکیشن نهایی

   استفاده از Pipeline تضمین می‌کنه که scaler فقط روی داده‌ی train فیت بشه و از data leakage جلوگیری بشه.

4. **Cross-validation**: با `cross_val_score` (K=5)، مدل روی ۵ تقسیم‌بندی مختلف ارزیابی می‌شه تا یک تخمین قابل‌اعتمادتر از دقت واقعی به دست بیاد (نه فقط یک عدد وابسته به یک تقسیم خاص).

5. **ذخیره و بارگذاری مدل**: با `joblib.dump` کل Pipeline (هم scaler هم model، با تمام پارامترهای آموزش‌دیده) در فایل `my_model.joblib` ذخیره می‌شه، و با `joblib.load` دوباره بارگذاری می‌شه — بدون نیاز به train مجدد.

6. **ارزیابی نهایی**: مدل بارگذاری‌شده روی داده‌ی test پیش‌بینی می‌گیره و accuracy نهایی چاپ می‌شه.

## نتایج نمونه

```
Scores per fold: [0.921  0.939  0.982  0.965  0.973]
Mean accuracy:   0.9561
Std deviation:   0.0228
Test accuracy:   0.9649
```

## نکات مهم

- **چرا Pipeline؟** برای جلوگیری از data leakage — `fit_transform` فقط روی train، `transform` روی test/production.
- **چرا Cross-validation؟** یک تقسیم تنها می‌تونه گمراه‌کننده باشه؛ میانگین چند fold تخمین پایدارتری می‌ده.
- **چرا کل Pipeline ذخیره می‌شه، نه فقط مدل؟** اگه فقط مدل ذخیره بشه، حالت آموزش‌دیده‌ی scaler (میانگین/انحراف معیار) از دست می‌ره و پیش‌بینی روی داده‌ی جدید اشتباه می‌شه.

## نیازمندی‌ها

```
scikit-learn
joblib
```

## اجرا

```bash
python main.py
```
