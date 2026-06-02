# تست

به لطف <a href="https://www.starlette.io/testclient/" class="external-link" target="_blank">Starlette</a>، تست برنامه‌های **FastAPI** آسان و لذت‌بخش است.

بر اساس <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a> ساخته شده که به نوبه خود بر اساس Requests طراحی شده، بنابراین بسیار آشنا و شهودی است.

با آن، می‌توانید مستقیماً از <a href="https://docs.pytest.org/" class="external-link" target="_blank">pytest</a> با **FastAPI** استفاده کنید.

## استفاده از `TestClient`

/// info

برای استفاده از `TestClient`، ابتدا <a href="https://www.python-httpx.org" class="external-link" target="_blank">`httpx`</a> را نصب کنید.

مطمئن شوید که یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کرده‌اید، آن را فعال کنید، و سپس آن را نصب کنید، به عنوان مثال:

```console
$ pip install httpx
```

///

`TestClient` را ایمپورت کنید.

یک `TestClient` با پاس دادن برنامه **FastAPI** خود به آن ایجاد کنید.

توابعی با نامی که با `test_` شروع می‌شود ایجاد کنید (این قراردادهای استاندارد `pytest` است).

از شیء `TestClient` به همان روشی استفاده کنید که با `httpx` استفاده می‌کنید.

دستورات `assert` ساده با عبارات استاندارد پایتون بنویسید که باید بررسی کنید (باز هم، `pytest` استاندارد).

{* ../../docs_src/app_testing/tutorial001.py hl[2,12,15:18] *}

/// tip

توجه کنید که توابع تست `def` معمولی هستند، نه `async def`.

و فراخوانی‌ها به کلاینت نیز فراخوانی‌های معمولی هستند، بدون استفاده از `await`.

این به شما اجازه می‌دهد از `pytest` مستقیماً و بدون پیچیدگی استفاده کنید.

///

/// note | جزئیات فنی

همچنین می‌توانید از `from starlette.testclient import TestClient` استفاده کنید.

**FastAPI** همان `starlette.testclient` را به عنوان `fastapi.testclient` فقط برای راحتی شما، توسعه‌دهنده، ارائه می‌دهد. اما مستقیماً از Starlette می‌آید.

///

/// tip

اگر می‌خواهید توابع `async` را در تست‌های خود علاوه بر ارسال درخواست‌ها به برنامه FastAPI صدا بزنید (مثلاً توابع پایگاه داده ناهمزمان)، به [تست‌های ناهمزمان](../advanced/async-tests.md){.internal-link target=_blank} در آموزش پیشرفته نگاه کنید.

///

## جداسازی تست‌ها

در یک برنامه واقعی، احتمالاً تست‌های خود را در فایل متفاوتی خواهید داشت.

و برنامه **FastAPI** شما نیز ممکن است از چندین فایل/ماژول و غیره تشکیل شده باشد.

### فایل برنامه **FastAPI**

فرض کنید ساختار فایلی مانند آنچه در [برنامه‌های بزرگ‌تر](bigger-applications.md){.internal-link target=_blank} توضیح داده شده دارید:

```
.
├── app
│   ├── __init__.py
│   └── main.py
```

در فایل `main.py` برنامه **FastAPI** خود را دارید:

{* ../../docs_src/app_testing/main.py *}

### فایل تست

سپس می‌توانید فایل `test_main.py` با تست‌های خود داشته باشید. می‌تواند در همان بسته پایتون (همان دایرکتوری با فایل `__init__.py`) قرار بگیرد:

``` hl_lines="5"
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

چون این فایل در همان بسته است، می‌توانید از ایمپورت‌های نسبی برای ایمپورت شیء `app` از ماژول `main` (`main.py`) استفاده کنید:

{* ../../docs_src/app_testing/test_main.py hl[3] *}

...و کد تست‌ها را درست مانند قبل داشته باشید.

## تست: مثال گسترده

حالا بیایید این مثال را گسترش دهیم و جزئیات بیشتری اضافه کنیم تا ببینیم چگونه بخش‌های مختلف را تست کنیم.

### فایل برنامه گسترده **FastAPI**

بیایید با همان ساختار فایلی قبلی ادامه دهیم:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

فرض کنید اکنون فایل `main.py` با برنامه **FastAPI** شما دارای *عملیات‌های مسیر* دیگری است.

یک عملیات `GET` دارد که می‌تواند خطا برگرداند.

یک عملیات `POST` دارد که می‌تواند چندین خطا برگرداند.

هر دو *عملیات مسیر* نیاز به هدر `X-Token` دارند.

//// tab | Python 3.10+

```Python
{!> ../../docs_src/app_testing/app_b_an_py310/main.py!}
```

////

//// tab | Python 3.9+

```Python
{!> ../../docs_src/app_testing/app_b_an_py39/main.py!}
```

////

//// tab | Python 3.8+

```Python
{!> ../../docs_src/app_testing/app_b_an/main.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip

| ترجیحاً از نسخه `Annotated` استفاده کنید اگر امکان‌پذیر است.

///

```Python
{!> ../../docs_src/app_testing/app_b_py310/main.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

| ترجیحاً از نسخه `Annotated` استفاده کنید اگر امکان‌پذیر است.

///

```Python
{!> ../../docs_src/app_testing/app_b/main.py!}
```

////

### فایل تست گسترده

سپس می‌توانید `test_main.py` را با تست‌های گسترده به‌روزرسانی کنید:

{* ../../docs_src/app_testing/app_b/test_main.py *}

هر وقت نیاز دارید کلاینت اطلاعاتی را در درخواست پاس دهد و نمی‌دانید چگونه، می‌توانید نحوه انجام آن در `httpx` را جستجو کنید (Google)، یا حتی نحوه انجام آن با `requests`، زیرا طراحی HTTPX بر اساس طراحی Requests است.

سپس همان کار را در تست‌های خود انجام دهید.

مثلاً:

* برای پاس دادن یک پارامتر *مسیر* یا *پرس‌و‌جو*، آن را به خود URL اضافه کنید.
* برای پاس دادن بدنه JSON، یک شیء پایتون (مثلاً یک `dict`) را به پارامتر `json` پاس دهید.
* اگر نیاز دارید *داده فرم* به جای JSON ارسال کنید، از پارامتر `data` استفاده کنید.
* برای پاس دادن *هدرها*، از یک `dict` در پارامتر `headers` استفاده کنید.
* برای *کوکی‌ها*، یک `dict` در پارامتر `cookies`.

برای اطلاعات بیشتر درباره نحوه پاس دادن داده به بک‌اند (با استفاده از `httpx` یا `TestClient`) مستندات <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a> را بررسی کنید.

/// info

توجه کنید که `TestClient` داده‌هایی دریافت می‌کند که می‌توان به JSON تبدیل کرد، نه مدل‌های Pydantic.

اگر یک مدل Pydantic در تست خود دارید و می‌خواهید داده‌های آن را در حین تست به برنامه ارسال کنید، می‌توانید از `jsonable_encoder` توضیح داده شده در [رمزگذار سازگار با JSON](encoder.md){.internal-link target=_blank} استفاده کنید.

///

## اجرا

بعد از آن، فقط باید `pytest` را نصب کنید.

مطمئن شوید که یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کرده‌اید، آن را فعال کنید، و سپس آن را نصب کنید، به عنوان مثال:

<div class="termy">

```console
$ pip install pytest

---> 100%
```

</div>

به طور خودکار فایل‌ها و تست‌ها را شناسایی می‌کند، آنها را اجرا می‌کند و نتایج را به شما گزارش می‌دهد.

تست‌ها را با دستور زیر اجرا کنید:

<div class="termy">

```console
$ pytest

================ test session starts ================
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/user/code/superawesome-cli/app
plugins: forked-1.1.3, xdist-1.31.0, cov-2.8.1
collected 6 items

---> 100%

test_main.py <span style="color: green; white-space: pre;">......                            [100%]</span>

<span style="color: green;">================= 1 passed in 0.03s =================</span>
```

</div>
