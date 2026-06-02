# مدل‌های فرم

شما می‌توانید از **مدل‌های Pydantic** برای تعریف **فیلدهای فرم** در FastAPI استفاده کنید.

/// info

برای استفاده از فرم‌ها، ابتدا <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a> را نصب کنید.

مطمئن شوید که یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کرده‌اید، آن را فعال کنید و سپس نصب کنید، برای مثال:

```console
$ pip install python-multipart
```

///

/// note

این از نسخه `0.113.0` FastAPI پشتیبانی می‌شود. 🤓

///

## مدل‌های Pydantic برای فرم‌ها

فقط باید یک **مدل Pydantic** با فیلدهایی که می‌خواهید به عنوان **فیلدهای فرم** دریافت کنید تعریف کنید و سپس پارامتر را به عنوان `Form` تعریف کنید:

{* ../../docs_src/request_form_models/tutorial001_an_py39.py hl[9:11,15] *}

**FastAPI** داده‌ها را برای **هر فیلد** از **داده‌های فرم** در درخواست **استخراج** می‌کند و مدل Pydantic تعریف شده شما را به شما می‌دهد.

## مستندات را بررسی کنید

می‌توانید آن را در رابط مستندات در `/docs` تأیید کنید:

<div class="screenshot">
<img src="/img/tutorial/request-form-models/image01.png">
</div>

## ممنوع کردن فیلدهای فرم اضافی

در برخی موارد استفاده خاص (احتمالاً خیلی رایج نیست)، ممکن است بخواهید فیلدهای فرم را فقط به آنهایی که در مدل Pydantic تعریف شده‌اند **محدود** کنید. و هر فیلد **اضافی** را **ممنوع** کنید.

/// note

این از نسخه `0.114.0` FastAPI پشتیبانی می‌شود. 🤓

///

می‌توانید از پیکربندی مدل Pydantic برای `forbid` کردن هر فیلد `extra` استفاده کنید:

{* ../../docs_src/request_form_models/tutorial002_an_py39.py hl[12] *}

اگر یک کلاینت سعی کند داده‌های اضافی ارسال کند، پاسخ **خطا** دریافت خواهد کرد.

به عنوان مثال، اگر کلاینت سعی کند فیلدهای فرم زیر را ارسال کند:

* `username`: `Rick`
* `password`: `Portal Gun`
* `extra`: `Mr. Poopybutthole`

پاسخ خطایی دریافت خواهد کرد که به آنها می‌گوید فیلد `extra` مجاز نیست:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["body", "extra"],
            "msg": "Extra inputs are not permitted",
            "input": "Mr. Poopybutthole"
        }
    ]
}
```

## خلاصه

شما می‌توانید از مدل‌های Pydantic برای تعریف فیلدهای فرم در FastAPI استفاده کنید. 😎
