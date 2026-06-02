# برنامه‌های بزرگ‌تر - فایل‌های متعدد

اگر در حال ساخت یک برنامه یا وب API هستید، به ندرت می‌توانید همه چیز را در یک فایل واحد قرار دهید.

**FastAPI** ابزاری مناسب برای ساختاردهی برنامه شما فراهم می‌کند در حالی که تمام انعطاف‌پذیری را حفظ می‌کند.

/// info

اگر از Flask آمده‌اید، این معادل Blueprint‌های Flask خواهد بود.

///

## یک مثال ساختار فایل

فرض کنید ساختار فایلی مانند زیر دارید:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

/// tip

چندین فایل `__init__.py` وجود دارد: یکی در هر دایرکتوری یا زیردایرکتوری.

این همان چیزی است که اجازه ایمپورت کد از یک فایل به فایل دیگر را می‌دهد.

به عنوان مثال، در `app/main.py` می‌توانید خطی مانند زیر داشته باشید:

```
from app.routers import items
```

///

* دایرکتوری `app` شامل همه چیز است. و یک فایل خالی `app/__init__.py` دارد، بنابراین یک "بسته پایتون" (مجموعه‌ای از "ماژول‌های پایتون") است: `app`.
* شامل یک فایل `app/main.py` است. از آنجا که داخل یک بسته پایتون (دایرکتوری با فایل `__init__.py`) است، یک "ماژول" آن بسته است: `app.main`.
* همچنین یک فایل `app/dependencies.py` وجود دارد، درست مانند `app/main.py`، یک "ماژول" است: `app.dependencies`.
* یک زیردایرکتوری `app/routers/` با فایل `__init__.py` دیگری وجود دارد، بنابراین یک "زیربسته پایتون" است: `app.routers`.
* فایل `app/routers/items.py` داخل یک بسته است، `app/routers/`، بنابراین یک زیرماژول است: `app.routers.items`.
* همین‌طور با `app/routers/users.py`، یک زیرماژول دیگر است: `app.routers.users`.
* همچنین یک زیردایرکتوری `app/internal/` با فایل `__init__.py` دیگری وجود دارد، بنابراین یک "زیربسته پایتون" دیگر است: `app.internal`.
* و فایل `app/internal/admin.py` یک زیرماژول دیگر است: `app.internal.admin`.

<img src="/img/tutorial/bigger-applications/package.svg">

همان ساختار فایل با توضیحات:

```
.
├── app                  # "app" یک بسته پایتون است
│   ├── __init__.py      # این فایل "app" را یک "بسته پایتون" می‌کند
│   ├── main.py          # ماژول "main"، مثلاً import app.main
│   ├── dependencies.py  # ماژول "dependencies"، مثلاً import app.dependencies
│   └── routers          # "routers" یک "زیربسته پایتون" است
│   │   ├── __init__.py  # "routers" را یک "زیربسته پایتون" می‌کند
│   │   ├── items.py     # زیرماژول "items"، مثلاً import app.routers.items
│   │   └── users.py     # زیرماژول "users"، مثلاً import app.routers.users
│   └── internal         # "internal" یک "زیربسته پایتون" است
│       ├── __init__.py  # "internal" را یک "زیربسته پایتون" می‌کند
│       └── admin.py     # زیرماژول "admin"، مثلاً import app.internal.admin
```

## `APIRouter`

فرض کنید فایل اختصاص‌یافته برای مدیریت فقط کاربران، زیرماژول در `/app/routers/users.py` است.

می‌خواهید *عملیات‌های مسیر* مرتبط با کاربران خود را از بقیه کد جدا کنید، تا سازمان‌یافته باشد.

اما همچنان بخشی از همان برنامه/وب API **FastAPI** است (بخشی از همان "بسته پایتون" است).

می‌توانید *عملیات‌های مسیر* برای آن ماژول را با استفاده از `APIRouter` ایجاد کنید.

### ایمپورت `APIRouter`

آن را ایمپورت کنید و یک "نمونه" ایجاد کنید به همان روشی که با کلاس `FastAPI` انجام می‌دهید:

```Python hl_lines="1  3" title="app/routers/users.py"
{!../../docs_src/bigger_applications/app/routers/users.py!}
```

### *عملیات‌های مسیر* با `APIRouter`

و سپس از آن برای اعلام *عملیات‌های مسیر* خود استفاده کنید.

به همان روشی استفاده کنید که از کلاس `FastAPI` استفاده می‌کنید:

```Python hl_lines="6  11  16" title="app/routers/users.py"
{!../../docs_src/bigger_applications/app/routers/users.py!}
```

می‌توانید `APIRouter` را مانند یک "کلاس کوچک `FastAPI`" در نظر بگیرید.

تمام گزینه‌های مشابه پشتیبانی می‌شوند.

تمام `parameters`، `responses`، `dependencies`، `tags` و غیره یکسان هستند.

/// tip

در این مثال، متغیر `router` نامیده شده، اما می‌توانید هر نامی که بخواهید برای آن بگذارید.

///

ما قصد داریم این `APIRouter` را در برنامه اصلی `FastAPI` اضافه کنیم، اما ابتدا بیایید وابستگی‌ها و `APIRouter` دیگری را بررسی کنیم.

## وابستگی‌ها

می‌بینیم که به برخی وابستگی‌ها نیاز خواهیم داشت که در چندین جای برنامه استفاده می‌شوند.

بنابراین آنها را در ماژول `dependencies` خود (`app/dependencies.py`) قرار می‌دهیم.

اکنون از یک وابستگی ساده برای خواندن هدر سفارشی `X-Token` استفاده خواهیم کرد:

//// tab | Python 3.9+

```Python hl_lines="3  6-8" title="app/dependencies.py"
{!> ../../docs_src/bigger_applications/app_an_py39/dependencies.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="1  5-7" title="app/dependencies.py"
{!> ../../docs_src/bigger_applications/app_an/dependencies.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

| ترجیحاً از نسخه `Annotated` استفاده کنید اگر امکان‌پذیر است.

///

```Python hl_lines="1  4-6" title="app/dependencies.py"
{!> ../../docs_src/bigger_applications/app/dependencies.py!}
```

////

/// tip

ما از یک هدر ساختگی برای ساده‌سازی این مثال استفاده می‌کنیم.

اما در موارد واقعی نتایج بهتری با استفاده از [ابزارهای امنیتی](security/index.md){.internal-link target=_blank} یکپارچه خواهید گرفت.

///

## ماژول دیگر با `APIRouter`

فرض کنید شما همچنین نقاط پایانی اختصاص‌یافته برای مدیریت "items" از برنامه خود در ماژول `app/routers/items.py` دارید.

*عملیات‌های مسیر* برای موارد زیر دارید:

* `/items/`
* `/items/{item_id}`

ساختار همانند `app/routers/users.py` است.

اما می‌خواهیم هوشمندتر باشیم و کد را کمی ساده‌تر کنیم.

می‌دانیم تمام *عملیات‌های مسیر* در این ماژول موارد زیر مشترک دارند:

* پیشوند مسیر: `/items`.
* `tags`: (فقط یک تگ: `items`).
* `responses` اضافی.
* `dependencies`: همه آنها به آن وابستگی `X-Token` که ایجاد کردیم نیاز دارند.

بنابراین، به جای افزودن همه اینها به هر *عملیات مسیر*، می‌توانیم آنها را به `APIRouter` اضافه کنیم.

```Python hl_lines="5-10  16  21" title="app/routers/items.py"
{!../../docs_src/bigger_applications/app/routers/items.py!}
```

از آنجا که مسیر هر *عملیات مسیر* باید با `/` شروع شود، مانند:

```Python hl_lines="1"
@router.get("/{item_id}")
async def read_item(item_id: str):
    ...
```

...پیشوند نباید شامل `/` نهایی باشد.

بنابراین، پیشوند در این مورد `/items` است.

همچنین می‌توانیم لیستی از `tags` و `responses` اضافی اضافه کنیم که به تمام *عملیات‌های مسیر* موجود در این router اعمال خواهد شد.

و می‌توانیم لیستی از `dependencies` اضافه کنیم که به تمام *عملیات‌های مسیر* در router اضافه خواهد شد و برای هر درخواست اجرا/حل خواهد شد.

/// tip

توجه کنید که، مانند [وابستگی‌ها در *دکوراتورهای عملیات مسیر*](dependencies/dependencies-in-path-operation-decorators.md){.internal-link target=_blank}، هیچ مقداری به *تابع عملیات مسیر* شما پاس داده نخواهد شد.

///

نتیجه نهایی این است که مسیرهای item اکنون:

* `/items/`
* `/items/{item_id}`

...همانطور که قصد داشتیم.

* آنها با لیستی از تگ‌ها که شامل یک رشته واحد `"items"` است علامت‌گذاری خواهند شد.
    * این "تگ‌ها" مخصوصاً برای سیستم‌های مستندات تعاملی خودکار (با استفاده از OpenAPI) مفید هستند.
* همه آنها `responses` از پیش تعریف‌شده را شامل خواهند شد.
* تمام این *عملیات‌های مسیر* لیست `dependencies` را قبل از آنها ارزیابی/اجرا خواهند کرد.
    * اگر همچنین وابستگی‌ها را در یک *عملیات مسیر* خاص اعلام کنید، **آنها نیز اجرا خواهند شد**.
    * وابستگی‌های router ابتدا اجرا می‌شوند، سپس [`dependencies` در دکوراتور](dependencies/dependencies-in-path-operation-decorators.md){.internal-link target=_blank}، و سپس وابستگی‌های پارامتر معمولی.
    * همچنین می‌توانید [وابستگی‌های `Security` با `scopes`](../advanced/security/oauth2-scopes.md){.internal-link target=_blank} اضافه کنید.

/// tip

داشتن `dependencies` در `APIRouter` می‌تواند استفاده شود، به عنوان مثال، برای نیاز به احراز هویت برای کل گروهی از *عملیات‌های مسیر*. حتی اگر وابستگی‌ها به صورت جداگانه به هر کدام اضافه نشده باشند.

///

/// check

پارامترهای `prefix`، `tags`، `responses` و `dependencies` (مانند بسیاری از موارد دیگر) فقط یک ویژگی از **FastAPI** برای کمک به جلوگیری از تکرار کد هستند.

///

### ایمپورت وابستگی‌ها

این کد در ماژول `app.routers.items`، فایل `app/routers/items.py` قرار دارد.

و ما باید تابع وابستگی را از ماژول `app.dependencies`، فایل `app/dependencies.py` دریافت کنیم.

بنابراین از ایمپورت نسبی با `..` برای وابستگی‌ها استفاده می‌کنیم:

```Python hl_lines="3" title="app/routers/items.py"
{!../../docs_src/bigger_applications/app/routers/items.py!}
```

#### نحوه کار ایمپورت‌های نسبی

/// tip

اگر کاملاً می‌دانید ایمپورت‌ها چگونه کار می‌کنند، به بخش بعدی زیر ادامه دهید.

///

یک نقطه واحد `.`، مانند:

```Python
from .dependencies import get_token_header
```

به معنای:

* شروع از همان بسته‌ای که این ماژول (فایل `app/routers/items.py`) در آن قرار دارد (دایرکتوری `app/routers/`)...
* ماژول `dependencies` را پیدا کن (یک فایل فرضی در `app/routers/dependencies.py`)...
* و از آن، تابع `get_token_header` را ایمپورت کن.

اما آن فایل وجود ندارد، وابستگی‌های ما در فایل `app/dependencies.py` هستند.

ساختار فایل/برنامه ما را به یاد بیاورید:

<img src="/img/tutorial/bigger-applications/package.svg">

---

دو نقطه `..`، مانند:

```Python
from ..dependencies import get_token_header
```

به معنای:

* شروع از همان بسته‌ای که این ماژول (فایل `app/routers/items.py`) در آن قرار دارد (دایرکتوری `app/routers/`)...
* به بسته والد بروید (دایرکتوری `app/`)...
* و در آنجا، ماژول `dependencies` (فایل `app/dependencies.py`) را پیدا کن...
* و از آن، تابع `get_token_header` را ایمپورت کن.

این به درستی کار می‌کند! 🎉

---

به همین ترتیب، اگر از سه نقطه `...` استفاده کرده بودیم، مانند:

```Python
from ...dependencies import get_token_header
```

به معنای:

* شروع از همان بسته‌ای که این ماژول (فایل `app/routers/items.py`) در آن قرار دارد (دایرکتوری `app/routers/`)...
* به بسته والد بروید (دایرکتوری `app/`)...
* سپس به والد آن بسته بروید (بسته والدی وجود ندارد، `app` سطح بالا است 😱)...
* و در آنجا، ماژول `dependencies` (فایل `app/dependencies.py`) را پیدا کن...
* و از آن، تابع `get_token_header` را ایمپورت کن.

این به یک بسته بالاتر از `app/`، با فایل `__init__.py` خودش و غیره اشاره خواهد کرد. اما ما آن را نداریم. بنابراین، در مثال ما خطا خواهد داد. 🚨

اما اکنون می‌دانید چگونه کار می‌کند، بنابراین می‌توانید از ایمپورت‌های نسبی در برنامه‌های خود استفاده کنید، هر چقدر پیچیده باشند. 🤓

### افزودن `tags`، `responses` و `dependencies` سفارشی

ما پیشوند `/items` یا `tags=["items"]` را به هر *عملیات مسیر* اضافه نمی‌کنیم زیرا آنها را به `APIRouter` اضافه کرده‌ایم.

اما همچنان می‌توانیم _بیشتر_ `tags` اضافه کنیم که به یک *عملیات مسیر* خاص اعمال شود، و همچنین برخی `responses` اضافی مختص آن *عملیات مسیر*:

```Python hl_lines="30-31" title="app/routers/items.py"
{!../../docs_src/bigger_applications/app/routers/items.py!}
```

/// tip

این آخرین عملیات مسیر ترکیبی از تگ‌ها خواهد داشت: `["items", "custom"]`.

و همچنین هر دو پاسخ در مستندات خواهد داشت، یکی برای `404` و یکی برای `403`.

///

## `FastAPI` اصلی

حالا، بیایید ماژول `app/main.py` را ببینیم.

اینجاست که کلاس `FastAPI` را ایمپورت و استفاده می‌کنید.

این فایل اصلی برنامه شما خواهد بود که همه چیز را به هم متصل می‌کند.

و از آنجا که بیشتر منطق شما اکنون در ماژول اختصاصی خود قرار دارد، فایل اصلی بسیار ساده خواهد بود.

### ایمپورت `FastAPI`

کلاس `FastAPI` را مانند معمول ایمپورت و ایجاد می‌کنید.

و حتی می‌توانیم [وابستگی‌های سراسری](dependencies/global-dependencies.md){.internal-link target=_blank} اعلام کنیم که با وابستگی‌های هر `APIRouter` ترکیب خواهند شد:

```Python hl_lines="1  3  7" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

### ایمپورت `APIRouter`

حالا زیرماژول‌های دیگر که `APIRouter` دارند را ایمپورت می‌کنیم:

```Python hl_lines="4-5" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

از آنجا که فایل‌های `app/routers/users.py` و `app/routers/items.py` زیرماژول‌هایی هستند که بخشی از همان بسته پایتون `app` هستند، می‌توانیم از یک نقطه واحد `.` برای ایمپورت آنها با استفاده از "ایمپورت‌های نسبی" استفاده کنیم.

### نحوه کار ایمپورت

بخش:

```Python
from .routers import items, users
```

به معنای:

* شروع از همان بسته‌ای که این ماژول (فایل `app/main.py`) در آن قرار دارد (دایرکتوری `app/`)...
* به دنبال زیربسته `routers` بگرد (دایرکتوری `app/routers/`)...
* و از آن، زیرماژول `items` (فایل `app/routers/items.py`) و `users` (فایل `app/routers/users.py`) را ایمپورت کن...

ماژول `items` یک متغیر `router` خواهد داشت (`items.router`). این همان چیزی است که در فایل `app/routers/items.py` ایجاد کردیم، یک شیء `APIRouter` است.

و سپس همین کار را برای ماژول `users` انجام می‌دهیم.

همچنین می‌توانستیم آنها را اینطور ایمپورت کنیم:

```Python
from app.routers import items, users
```

/// info

نسخه اول یک "ایمپورت نسبی" است:

```Python
from .routers import items, users
```

نسخه دوم یک "ایمپورت مطلق" است:

```Python
from app.routers import items, users
```

برای یادگیری بیشتر درباره بسته‌ها و ماژول‌های پایتون، <a href="https://docs.python.org/3/tutorial/modules.html" class="external-link" target="_blank">مستندات رسمی پایتون درباره ماژول‌ها</a> را بخوانید.

///

### اجتناب از تداخل نام‌ها

ما زیرماژول `items` را مستقیماً ایمپورت می‌کنیم، به جای ایمپورت فقط متغیر `router` آن.

این به این دلیل است که ما همچنین متغیر دیگری به نام `router` در زیرماژول `users` داریم.

اگر یکی بعد از دیگری ایمپورت کرده بودیم، مانند:

```Python
from .routers.items import router
from .routers.users import router
```

`router` از `users` آن را از `items` بازنویسی می‌کرد و نمی‌توانستیم هر دو را همزمان استفاده کنیم.

بنابراین، برای اینکه بتوانیم هر دو را در همان فایل استفاده کنیم، زیرماژول‌ها را مستقیماً ایمپورت می‌کنیم:

```Python hl_lines="5" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

### شامل کردن `APIRouter`ها برای `users` و `items`

حالا، بیایید `router`ها از زیرماژول‌های `users` و `items` را شامل کنیم:

```Python hl_lines="10-11" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

/// info

`users.router` شامل `APIRouter` داخل فایل `app/routers/users.py` است.

و `items.router` شامل `APIRouter` داخل فایل `app/routers/items.py` است.

///

با `app.include_router()` می‌توانیم هر `APIRouter` را به برنامه اصلی `FastAPI` اضافه کنیم.

تمام مسیرها از آن router را به عنوان بخشی از آن شامل خواهد کرد.

/// note | جزئیات فنی

در واقع به صورت داخلی یک *عملیات مسیر* برای هر *عملیات مسیر* که در `APIRouter` اعلام شده بود ایجاد خواهد کرد.

بنابراین، پشت صحنه، واقعاً طوری کار خواهد کرد که گویی همه چیز یک برنامه واحد بوده است.

///

/// check

نیازی نیست نگران عملکرد هنگام شامل کردن routerها باشید.

این میکروثانیه‌ها طول می‌کشد و فقط در هنگام راه‌اندازی اتفاق می‌افتد.

بنابراین عملکرد را تحت تأثیر قرار نخواهد داد. ⚡

///

### شامل کردن یک `APIRouter` با `prefix`، `tags`، `responses` و `dependencies` سفارشی

حالا، تصور کنید سازمان شما فایل `app/internal/admin.py` را به شما داده است.

شامل یک `APIRouter` با برخی *عملیات‌های مسیر* مدیریتی است که سازمان شما بین چندین پروژه به اشتراک می‌گذارد.

برای این مثال بسیار ساده خواهد بود. اما فرض کنید چون با پروژه‌های دیگر در سازمان به اشتراک گذاشته شده، نمی‌توانیم آن را تغییر دهیم و `prefix`، `dependencies`، `tags` و غیره را مستقیماً به `APIRouter` اضافه کنیم:

```Python hl_lines="3" title="app/internal/admin.py"
{!../../docs_src/bigger_applications/app/internal/admin.py!}
```

اما همچنان می‌خواهیم یک `prefix` سفارشی هنگام شامل کردن `APIRouter` تنظیم کنیم تا تمام *عملیات‌های مسیر* آن با `/admin` شروع شوند، می‌خواهیم آن را با `dependencies`ای که قبلاً برای این پروژه داریم امن کنیم و می‌خواهیم `tags` و `responses` اضافه کنیم.

می‌توانیم همه اینها را بدون نیاز به تغییر `APIRouter` اصلی با پاس دادن آن پارامترها به `app.include_router()` اعلام کنیم:

```Python hl_lines="14-17" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

به این ترتیب، `APIRouter` اصلی بدون تغییر باقی خواهد ماند، بنابراین همچنان می‌توانیم همان فایل `app/internal/admin.py` را با پروژه‌های دیگر در سازمان به اشتراک بگذاریم.

نتیجه این است که در برنامه ما، هر یک از *عملیات‌های مسیر* از ماژول `admin` خواهد داشت:

* پیشوند `/admin`.
* تگ `admin`.
* وابستگی `get_token_header`.
* پاسخ `418`. 🍵

اما این فقط بر آن `APIRouter` در برنامه ما تأثیر خواهد گذاشت، نه در هر کد دیگری که از آن استفاده می‌کند.

بنابراین، به عنوان مثال، پروژه‌های دیگر می‌توانند از همان `APIRouter` با روش احراز هویت متفاوتی استفاده کنند.

### شامل کردن یک *عملیات مسیر*

همچنین می‌توانیم *عملیات‌های مسیر* را مستقیماً به برنامه `FastAPI` اضافه کنیم.

اینجا این کار را می‌کنیم... فقط برای نشان دادن اینکه می‌توانیم 🤷:

```Python hl_lines="21-23" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

و به درستی کار خواهد کرد، همراه با تمام *عملیات‌های مسیر* دیگر اضافه‌شده با `app.include_router()`.

/// info | جزئیات بسیار فنی

**توجه**: این یک جزئیات بسیار فنی است که احتمالاً می‌توانید **رد شوید**.

---

`APIRouter`ها "mount" نمی‌شوند، از بقیه برنامه ایزوله نیستند.

این به این دلیل است که می‌خواهیم *عملیات‌های مسیر* آنها را در طرح OpenAPI و رابط‌های کاربری شامل کنیم.

از آنجا که نمی‌توانیم آنها را فقط ایزوله و "mount" کنیم مستقل از بقیه، *عملیات‌های مسیر* "شبیه‌سازی" (دوباره ایجاد) می‌شوند، نه مستقیماً شامل.

///

## بررسی مستندات خودکار API

حالا، برنامه خود را اجرا کنید:

<div class="termy">

```console
$ fastapi dev app/main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

و مستندات را در <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> باز کنید.

مستندات خودکار API را خواهید دید، شامل مسیرها از تمام زیرماژول‌ها، با استفاده از مسیرها (و پیشوندها) صحیح و تگ‌های صحیح:

<img src="/img/tutorial/bigger-applications/image01.png">

## شامل کردن چندباره همان router با `prefix` متفاوت

همچنین می‌توانید از `.include_router()` چندین بار با *همان* router با پیشوندهای متفاوت استفاده کنید.

این می‌تواند مفید باشد، به عنوان مثال، برای نمایش همان API تحت پیشوندهای مختلف، مثلاً `/api/v1` و `/api/latest`.

این یک استفاده پیشرفته است که ممکن است واقعاً نیازی به آن نداشته باشید، اما در صورت نیاز وجود دارد.

## شامل کردن یک `APIRouter` در دیگری

به همان روشی که می‌توانید یک `APIRouter` را در یک برنامه `FastAPI` شامل کنید، می‌توانید یک `APIRouter` را در `APIRouter` دیگری شامل کنید با استفاده از:

```Python
router.include_router(other_router)
```

مطمئن شوید این کار را قبل از شامل کردن `router` در برنامه `FastAPI` انجام دهید، تا *عملیات‌های مسیر* از `other_router` نیز شامل شوند.
