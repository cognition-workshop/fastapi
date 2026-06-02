# WebSockets

می‌توانید از <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API" class="external-link" target="_blank">WebSockets</a> با **FastAPI** استفاده کنید.

## نصب `WebSockets`

مطمئن شوید که یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کرده‌اید، آن را فعال کنید و `websockets` را نصب کنید:

<div class="termy">

```console
$ pip install websockets

---> 100%
```

</div>

## کلاینت WebSockets

### در محیط تولید

در سیستم تولید شما، احتمالاً یک فرانت‌اند با یک فریمورک مدرن مانند React، Vue.js یا Angular ایجاد کرده‌اید.

و برای ارتباط با استفاده از WebSockets با بک‌اند خود، احتمالاً از ابزارهای فرانت‌اند خود استفاده خواهید کرد.

یا ممکن است یک برنامه موبایل بومی داشته باشید که مستقیماً با بک‌اند WebSocket شما در کد بومی ارتباط برقرار می‌کند.

یا ممکن است هر روش دیگری برای ارتباط با اندپوینت WebSocket داشته باشید.

---

اما برای این مثال، ما از یک سند HTML بسیار ساده با کمی JavaScript استفاده خواهیم کرد، همه در یک رشته بلند.

البته، این بهینه نیست و در محیط تولید از آن استفاده نمی‌کنید.

در محیط تولید یکی از گزینه‌های بالا را خواهید داشت.

اما ساده‌ترین راه برای تمرکز بر سمت سرور WebSockets و داشتن یک مثال کاری است:

{* ../../docs_src/websockets/tutorial001.py hl[2,6:38,41:43] *}

## ایجاد یک `websocket`

در برنامه **FastAPI** خود، یک `websocket` ایجاد کنید:

{* ../../docs_src/websockets/tutorial001.py hl[1,46:47] *}

/// note | جزئیات فنی

شما همچنین می‌توانید از `from starlette.websockets import WebSocket` استفاده کنید.

**FastAPI** همان `WebSocket` را مستقیماً فقط به عنوان یک سهولت برای شما به عنوان برنامه‌نویس فراهم می‌کند. اما مستقیماً از Starlette می‌آید.

///

## انتظار برای پیام‌ها و ارسال پیام‌ها

در مسیر WebSocket خود می‌توانید برای پیام‌ها `await` کنید و پیام ارسال کنید.

{* ../../docs_src/websockets/tutorial001.py hl[48:52] *}

می‌توانید داده‌های باینری، متنی و JSON دریافت و ارسال کنید.

## امتحان کنید

اگر فایل شما `main.py` نام دارد، برنامه خود را با دستور زیر اجرا کنید:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

مرورگر خود را در <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> باز کنید.

یک صفحه ساده مانند زیر خواهید دید:

<img src="/img/tutorial/websockets/image01.png">

می‌توانید پیام‌ها را در کادر ورودی تایپ و ارسال کنید:

<img src="/img/tutorial/websockets/image02.png">

و برنامه **FastAPI** شما با WebSockets پاسخ خواهد داد:

<img src="/img/tutorial/websockets/image03.png">

می‌توانید پیام‌های زیادی ارسال (و دریافت) کنید:

<img src="/img/tutorial/websockets/image04.png">

و همه آنها از یک اتصال WebSocket استفاده خواهند کرد.

## استفاده از `Depends` و دیگران

در اندپوینت‌های WebSocket می‌توانید از `fastapi` وارد کنید و استفاده کنید:

* `Depends`
* `Security`
* `Cookie`
* `Header`
* `Path`
* `Query`

آنها به همان روش سایر اندپوینت‌های FastAPI/*عملیات‌های مسیر* کار می‌کنند:

{* ../../docs_src/websockets/tutorial002_an_py310.py hl[68:69,82] *}

/// info

از آنجا که این یک WebSocket است، واقعاً معنی ندارد که `HTTPException` ایجاد کنید، در عوض `WebSocketException` ایجاد می‌کنیم.

می‌توانید از کد بستن از <a href="https://tools.ietf.org/html/rfc6455#section-7.4.1" class="external-link" target="_blank">کدهای معتبر تعریف شده در مشخصات</a> استفاده کنید.

///

### امتحان WebSockets با وابستگی‌ها

اگر فایل شما `main.py` نام دارد، برنامه خود را با دستور زیر اجرا کنید:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

مرورگر خود را در <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> باز کنید.

در آنجا می‌توانید تنظیم کنید:

* "Item ID"، استفاده شده در مسیر.
* "Token" استفاده شده به عنوان پارامتر query.

/// tip

توجه کنید که query `token` توسط یک وابستگی مدیریت خواهد شد.

///

با آن می‌توانید WebSocket را متصل کنید و سپس پیام ارسال و دریافت کنید:

<img src="/img/tutorial/websockets/image05.png">

## مدیریت قطع اتصال و چندین کلاینت

هنگامی که یک اتصال WebSocket بسته می‌شود، `await websocket.receive_text()` یک استثنای `WebSocketDisconnect` ایجاد می‌کند که سپس می‌توانید آن را مانند این مثال بگیرید و مدیریت کنید.

{* ../../docs_src/websockets/tutorial003_py39.py hl[79:81] *}

برای امتحان:

* برنامه را در چندین تب مرورگر باز کنید.
* پیام‌هایی از آنها بنویسید.
* سپس یکی از تب‌ها را ببندید.

این استثنای `WebSocketDisconnect` را ایجاد می‌کند و تمام کلاینت‌های دیگر پیامی مانند زیر دریافت خواهند کرد:

```
Client #1596980209979 left the chat
```

/// tip

برنامه بالا یک مثال حداقلی و ساده برای نشان دادن نحوه مدیریت و پخش پیام‌ها به چندین اتصال WebSocket است.

اما به خاطر داشته باشید که، از آنجا که همه چیز در حافظه مدیریت می‌شود، در یک لیست واحد، فقط تا زمانی که فرآیند در حال اجراست کار خواهد کرد و فقط با یک فرآیند واحد کار خواهد کرد.

اگر نیاز به چیزی دارید که به راحتی با FastAPI یکپارچه شود اما قوی‌تر است، پشتیبانی از Redis، PostgreSQL یا موارد دیگر دارد، <a href="https://github.com/encode/broadcaster" class="external-link" target="_blank">encode/broadcaster</a> را بررسی کنید.

///
