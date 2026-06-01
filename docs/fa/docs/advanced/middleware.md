# میان‌افزار پیشرفته

در آموزش اصلی خواندید که چگونه [میان‌افزار سفارشی](../tutorial/middleware.md){.internal-link target=_blank} به برنامه خود اضافه کنید.

و سپس خواندید که چگونه [CORS را با `CORSMiddleware`](../tutorial/cors.md){.internal-link target=_blank} مدیریت کنید.

در این بخش نحوه استفاده از سایر میان‌افزارها را خواهیم دید.

## اضافه کردن میان‌افزارهای ASGI

از آنجا که **FastAPI** بر اساس Starlette ساخته شده و مشخصات <abbr title="رابط دروازه سرور ناهمگام">ASGI</abbr> را پیاده‌سازی می‌کند، می‌توانید از هر میان‌افزار ASGI استفاده کنید.

یک میان‌افزار لازم نیست برای FastAPI یا Starlette ساخته شده باشد تا کار کند، تا زمانی که مشخصات ASGI را رعایت کند.

به طور کلی، میان‌افزارهای ASGI کلاس‌هایی هستند که انتظار دارند یک برنامه ASGI را به عنوان اولین آرگومان دریافت کنند.

بنابراین، در مستندات میان‌افزارهای ASGI شخص ثالث، احتمالاً به شما می‌گویند کاری شبیه این انجام دهید:

```Python
from unicorn import UnicornMiddleware

app = SomeASGIApp()

new_app = UnicornMiddleware(app, some_config="rainbow")
```

اما FastAPI (در واقع Starlette) راه ساده‌تری ارائه می‌دهد که اطمینان حاصل می‌کند میان‌افزارهای داخلی خطاهای سرور و هندلرهای استثنای سفارشی را به درستی مدیریت می‌کنند.

برای آن، از `app.add_middleware()` استفاده می‌کنید (مانند مثال CORS).

```Python
from fastapi import FastAPI
from unicorn import UnicornMiddleware

app = FastAPI()

app.add_middleware(UnicornMiddleware, some_config="rainbow")
```

`app.add_middleware()` یک کلاس میان‌افزار را به عنوان اولین آرگومان و هر آرگومان اضافی برای ارسال به میان‌افزار دریافت می‌کند.

## میان‌افزارهای یکپارچه

**FastAPI** شامل چندین میان‌افزار برای موارد استفاده رایج است، در ادامه نحوه استفاده از آنها را خواهیم دید.

/// note | جزئیات فنی

برای مثال‌های بعدی، همچنین می‌توانید از `from starlette.middleware.something import SomethingMiddleware` استفاده کنید.

**FastAPI** چندین میان‌افزار در `fastapi.middleware` فقط به عنوان یک سهولت برای شما به عنوان برنامه‌نویس فراهم می‌کند. اما بیشتر میان‌افزارهای موجود مستقیماً از Starlette می‌آیند.

///

## `HTTPSRedirectMiddleware`

الزام می‌کند که تمام درخواست‌های ورودی باید `https` یا `wss` باشند.

هر درخواست ورودی به `http` یا `ws` به جای آن به طرح امن هدایت خواهد شد.

{* ../../docs_src/advanced_middleware/tutorial001.py hl[2,6] *}

## `TrustedHostMiddleware`

الزام می‌کند که تمام درخواست‌های ورودی هدر `Host` به درستی تنظیم شده داشته باشند، برای محافظت در برابر حملات HTTP Host Header.

{* ../../docs_src/advanced_middleware/tutorial002.py hl[2,6:8] *}

آرگومان‌های زیر پشتیبانی می‌شوند:

* `allowed_hosts` - لیستی از نام‌های دامنه که باید به عنوان نام‌های میزبان مجاز باشند. دامنه‌های عام مانند `*.example.com` برای تطبیق زیردامنه‌ها پشتیبانی می‌شوند. برای اجازه هر نام میزبان از `allowed_hosts=["*"]` استفاده کنید یا میان‌افزار را حذف کنید.

اگر یک درخواست ورودی به درستی اعتبارسنجی نشود، پاسخ `400` ارسال خواهد شد.

## `GZipMiddleware`

پاسخ‌های GZip را برای هر درخواستی که `"gzip"` در هدر `Accept-Encoding` داشته باشد مدیریت می‌کند.

این میان‌افزار هم پاسخ‌های استاندارد و هم پاسخ‌های جریانی را مدیریت می‌کند.

{* ../../docs_src/advanced_middleware/tutorial003.py hl[2,6] *}

آرگومان‌های زیر پشتیبانی می‌شوند:

* `minimum_size` - پاسخ‌هایی که کوچک‌تر از این حداقل اندازه به بایت هستند را GZip نکنید. پیش‌فرض `500` است.
* `compresslevel` - در هنگام فشرده‌سازی GZip استفاده می‌شود. عدد صحیحی از 1 تا 9 است. پیش‌فرض `9` است. مقدار کمتر منجر به فشرده‌سازی سریع‌تر اما اندازه فایل بزرگ‌تر می‌شود، در حالی که مقدار بیشتر منجر به فشرده‌سازی کندتر اما اندازه فایل کوچک‌تر می‌شود.

## سایر میان‌افزارها

بسیاری از میان‌افزارهای ASGI دیگر وجود دارند.

برای مثال:

* <a href="https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py" class="external-link" target="_blank">`ProxyHeadersMiddleware` از Uvicorn</a>
* <a href="https://github.com/florimondmanca/msgpack-asgi" class="external-link" target="_blank">MessagePack</a>

برای مشاهده سایر میان‌افزارهای موجود، <a href="https://www.starlette.io/middleware/" class="external-link" target="_blank">مستندات میان‌افزار Starlette</a> و <a href="https://github.com/florimondmanca/awesome-asgi" class="external-link" target="_blank">لیست عالی ASGI</a> را بررسی کنید.
