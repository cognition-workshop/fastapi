# اجرای دستی سرور

## استفاده از دستور `fastapi run`

به طور خلاصه، از `fastapi run` برای سرو کردن برنامه FastAPI خود استفاده کنید:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> run <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting production server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000/docs</u></font>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>2306215</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
```

</div>

این برای اکثر موارد کار خواهد کرد. 😎

برای مثال می‌توانید از آن دستور برای شروع برنامه **FastAPI** خود در یک کانتینر، سرور و غیره استفاده کنید.

## سرورهای ASGI

بیایید کمی عمیق‌تر به جزئیات برویم.

FastAPI از یک استاندارد برای ساخت فریمورک‌ها و سرورهای وب Python به نام <abbr title="Asynchronous Server Gateway Interface">ASGI</abbr> استفاده می‌کند. FastAPI یک فریمورک وب ASGI است.

چیز اصلی که برای اجرای یک برنامه **FastAPI** (یا هر برنامه ASGI دیگر) در یک ماشین سرور راه دور نیاز دارید، یک برنامه سرور ASGI مانند **Uvicorn** است، که همان چیزی است که به طور پیش‌فرض در دستور `fastapi` می‌آید.

چندین جایگزین وجود دارد، از جمله:

* <a href="https://www.uvicorn.org/" class="external-link" target="_blank">Uvicorn</a>: یک سرور ASGI با کارایی بالا.
* <a href="https://hypercorn.readthedocs.io/" class="external-link" target="_blank">Hypercorn</a>: یک سرور ASGI سازگار با HTTP/2 و Trio از جمله ویژگی‌های دیگر.
* <a href="https://github.com/django/daphne" class="external-link" target="_blank">Daphne</a>: سرور ASGI ساخته شده برای Django Channels.
* <a href="https://github.com/emmett-framework/granian" class="external-link" target="_blank">Granian</a>: یک سرور HTTP Rust برای برنامه‌های Python.
* <a href="https://unit.nginx.org/howto/fastapi/" class="external-link" target="_blank">NGINX Unit</a>: NGINX Unit یک محیط اجرای سبک و انعطاف‌پذیر برنامه‌های وب است.

## ماشین سرور و برنامه سرور

یک جزئیات کوچک درباره نام‌ها وجود دارد که باید به خاطر داشته باشید. 💡

کلمه "**سرور**" معمولاً برای اشاره به هم رایانه راه دور/ابری (ماشین فیزیکی یا مجازی) و هم برنامه‌ای که روی آن ماشین اجرا می‌شود (مثلاً Uvicorn) استفاده می‌شود.

فقط به خاطر داشته باشید که وقتی "سرور" را به طور کلی می‌خوانید، ممکن است به یکی از آن دو چیز اشاره داشته باشد.

هنگام اشاره به ماشین راه دور، معمول است آن را **سرور** بنامند، اما همچنین **ماشین**، **VM** (ماشین مجازی)، **node**. همه اینها به نوعی ماشین راه دور اشاره دارند، معمولاً لینوکس اجرا می‌کنند، جایی که برنامه‌ها را اجرا می‌کنید.

## نصب برنامه سرور

وقتی FastAPI نصب می‌کنید، با یک سرور تولیدی، Uvicorn همراه می‌آید و می‌توانید آن را با دستور `fastapi run` شروع کنید.

اما همچنین می‌توانید یک سرور ASGI را به صورت دستی نصب کنید.

مطمئن شوید که [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} خود را ایجاد کرده، آن را فعال کرده و سپس می‌توانید برنامه سرور را نصب کنید.

برای مثال، برای نصب Uvicorn:

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

فرآیند مشابهی برای هر برنامه سرور ASGI دیگری اعمال خواهد شد.

/// tip

با اضافه کردن `standard`، Uvicorn برخی وابستگی‌های اضافی توصیه شده را نصب و استفاده خواهد کرد.

شامل `uvloop`، جایگزین با کارایی بالا برای `asyncio`، که افزایش سرعت همزمانی قابل توجهی ارائه می‌دهد.

///

## اجرای برنامه سرور

اگر سرور ASGI را به صورت دستی نصب کرده‌اید، معمولاً نیاز به ارسال یک رشته وارد‌سازی در فرمت خاصی دارید تا ماژول Python شما وارد شود:

<div class="termy">

```console
$ uvicorn main:app --host 0.0.0.0 --port 80

INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

</div>

/// note

دستور `uvicorn main:app` به:

* `main`: فایل `main.py` (ماژول Python).
* `app`: شیء ایجاد شده در `main.py` با خط `app = FastAPI()`.

معادل:

```Python
from main import app
```

///

هر سرور ASGI جایگزین فرمان وارد‌سازی مشابهی خواهد داشت، می‌توانید مستندات خاص آنها را بخوانید.

/// warning

Uvicorn و سرورهای دیگر از گزینه `--reload` پشتیبانی می‌کنند که در حین توسعه مفید است.

گزینه `--reload` منابع اضافی مصرف می‌کند، ناپایدارتر است و غیره.

فقط در حین **توسعه** بسیار کمک می‌کند.

نباید آن را در **تولید** استفاده کنید.

///
