# داده‌های فرم

وقتی نیاز دارید به جای JSON فیلدهای فرم دریافت کنید، می‌توانید از `Form` استفاده کنید.

/// info

برای استفاده از فرم‌ها، ابتدا <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a> را نصب کنید.

مطمئن شوید یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کنید، آن را فعال کنید و سپس نصب کنید، برای مثال:

```console
$ pip install python-multipart
```

///

## وارد کردن `Form`

`Form` را از `fastapi` وارد کنید:

{* ../../docs_src/request_forms/tutorial001_an_py39.py hl[3] *}

## تعریف پارامترهای `Form`

پارامترهای فرم را به همان شکلی که برای `Body` یا `Query` ایجاد می‌کنید، بسازید:

{* ../../docs_src/request_forms/tutorial001_an_py39.py hl[9] *}

برای مثال، در یکی از روش‌هایی که مشخصه OAuth2 می‌تواند استفاده شود (به نام "password flow") ارسال `username` و `password` به عنوان فیلدهای فرم الزامی است.

<abbr title="مشخصه">spec</abbr> نیاز دارد که فیلدها دقیقاً `username` و `password` نامگذاری شوند و به عنوان فیلدهای فرم ارسال شوند، نه JSON.

با `Form` می‌توانید همان پیکربندی‌هایی که با `Body` (و `Query`، `Path`، `Cookie`) دارید اعلان کنید، شامل اعتبارسنجی، مثال‌ها، نام مستعار (مثلاً `user-name` به جای `username`) و غیره.

/// info

`Form` کلاسی است که مستقیماً از `Body` ارث‌بری می‌کند.

///

/// tip

برای اعلان بدنه‌های فرم، باید صریحاً از `Form` استفاده کنید، زیرا بدون آن پارامترها به عنوان پارامترهای کوئری یا بدنه (JSON) تفسیر خواهند شد.

///

## درباره "فیلدهای فرم"

روشی که فرم‌های HTML (`<form></form>`) داده‌ها را به سرور ارسال می‌کنند معمولاً از یک رمزگذاری "خاص" برای آن داده‌ها استفاده می‌کند، متفاوت از JSON.

**FastAPI** مطمئن خواهد شد که آن داده‌ها را از مکان صحیح به جای JSON می‌خواند.

/// note | جزئیات فنی

داده‌های فرم‌ها معمولاً با استفاده از "نوع رسانه" `application/x-www-form-urlencoded` رمزگذاری می‌شوند.

اما وقتی فرم شامل فایل‌ها باشد، به عنوان `multipart/form-data` رمزگذاری می‌شود. در فصل بعدی درباره مدیریت فایل‌ها خواهید خواند.

اگر می‌خواهید بیشتر درباره این رمزگذاری‌ها و فیلدهای فرم بخوانید، به <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST" class="external-link" target="_blank">مستندات وب <abbr title="Mozilla Developer Network">MDN</abbr> برای <code>POST</code></a> مراجعه کنید.

///

/// warning

شما می‌توانید چندین پارامتر `Form` در یک *عملیات مسیر* اعلان کنید، اما نمی‌توانید همزمان فیلدهای `Body` که انتظار دارید به عنوان JSON دریافت شوند نیز اعلان کنید، زیرا درخواست بدنه را با استفاده از `application/x-www-form-urlencoded` به جای `application/json` رمزگذاری خواهد کرد.

این محدودیت **FastAPI** نیست، بخشی از پروتکل HTTP است.

///

## خلاصه

از `Form` برای اعلان پارامترهای ورودی داده فرم استفاده کنید.
