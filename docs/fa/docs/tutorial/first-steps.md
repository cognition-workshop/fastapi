# اولین قدم‌ها

ساده‌ترین فایل FastAPI می‌تواند به این شکل باشد:

{* ../../docs_src/first_steps/tutorial001.py *}

آن را در فایلی به نام `main.py` کپی کنید.

سرور زنده را اجرا کنید:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

در خروجی، خطی وجود دارد شبیه به:

```hl_lines="4"
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

آن خط URL جایی که برنامه شما سرویس‌دهی می‌شود را در ماشین محلی شما نشان می‌دهد.

### بررسی کنید

مرورگر خود را در <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> باز کنید.

پاسخ JSON را به این شکل خواهید دید:

```JSON
{"message": "Hello World"}
```

### مستندات تعاملی API

حال به <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> بروید.

مستندات تعاملی خودکار API را خواهید دید (ارائه شده توسط <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### مستندات جایگزین API

و حال، به <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> بروید.

مستندات جایگزین خودکار را خواهید دید (ارائه شده توسط <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### OpenAPI

**FastAPI** یک "اسکیما" با تمام API شما با استفاده از استاندارد **OpenAPI** برای تعریف APIها تولید می‌کند.

#### "اسکیما"

یک "اسکیما" تعریف یا توصیف چیزی است. نه کدی که آن را پیاده‌سازی می‌کند، بلکه فقط یک توصیف انتزاعی.

#### اسکیمای API

در این مورد، <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> مشخصه‌ای است که نحوه تعریف اسکیمای API شما را تعیین می‌کند.

این تعریف اسکیما شامل مسیرهای API شما، پارامترهای احتمالی آنها و غیره می‌شود.

#### اسکیمای داده

اصطلاح "اسکیما" ممکن است به شکل داده‌ها هم اشاره داشته باشد، مانند محتوای JSON.

در آن صورت، به معنای ویژگی‌های JSON و انواع داده‌ای آنها و غیره خواهد بود.

#### OpenAPI و JSON Schema

OpenAPI اسکیمایی برای API شما تعریف می‌کند. و آن اسکیما شامل تعاریف (یا "اسکیماهای") داده‌های ارسال و دریافت شده توسط API شما با استفاده از **JSON Schema**، استاندارد اسکیماهای داده JSON است.

#### بررسی `openapi.json`

اگر کنجکاو هستید که اسکیمای خام OpenAPI چگونه به نظر می‌رسد، FastAPI به طور خودکار یک JSON (اسکیما) با توضیحات تمام API شما تولید می‌کند.

می‌توانید آن را مستقیماً در: <a href="http://127.0.0.1:8000/openapi.json" class="external-link" target="_blank">http://127.0.0.1:8000/openapi.json</a> ببینید.

یک JSON را نشان خواهد داد که با چیزی شبیه به این شروع می‌شود:

```JSON
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...
```

#### OpenAPI برای چیست

اسکیمای OpenAPI چیزی است که دو سیستم مستندات تعاملی شامل شده را تقویت می‌کند.

و ده‌ها جایگزین وجود دارد، همه بر اساس OpenAPI. شما می‌توانید به راحتی هر یک از آن جایگزین‌ها را به برنامه ساخته شده با **FastAPI** اضافه کنید.

همچنین می‌توانید از آن برای تولید خودکار کد برای کلاینت‌هایی که با API شما ارتباط برقرار می‌کنند استفاده کنید. برای مثال، برنامه‌های فرانت‌اند، موبایل یا IoT.

## خلاصه، قدم به قدم

### مرحله ۱: وارد کردن `FastAPI`

{* ../../docs_src/first_steps/tutorial001.py hl[1] *}

`FastAPI` یک کلاس پایتون است که تمام عملکرد API شما را فراهم می‌کند.

/// note | جزئیات فنی

`FastAPI` کلاسی است که مستقیماً از `Starlette` ارث‌بری می‌کند.

شما می‌توانید از تمام عملکرد <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> نیز با `FastAPI` استفاده کنید.

///

### مرحله ۲: ایجاد یک "نمونه" `FastAPI`

{* ../../docs_src/first_steps/tutorial001.py hl[3] *}

اینجا متغیر `app` یک "نمونه" از کلاس `FastAPI` خواهد بود.

این نقطه اصلی تعامل برای ایجاد تمام API شما خواهد بود.

### مرحله ۳: ایجاد یک *عملیات مسیر*

#### مسیر

"مسیر" اینجا به آخرین بخش URL از اولین `/` اشاره دارد.

بنابراین، در URL مانند:

```
https://example.com/items/foo
```

...مسیر خواهد بود:

```
/items/foo
```

/// info

"مسیر" همچنین معمولاً "endpoint" یا "route" نامیده می‌شود.

///

هنگام ساخت یک API، "مسیر" راه اصلی برای جداسازی "دغدغه‌ها" و "منابع" است.

#### عملیات

"عملیات" اینجا به یکی از "متدهای" HTTP اشاره دارد.

یکی از:

* `POST`
* `GET`
* `PUT`
* `DELETE`

...و موارد کمتر رایج:

* `OPTIONS`
* `HEAD`
* `PATCH`
* `TRACE`

در پروتکل HTTP، می‌توانید با هر مسیر با استفاده از یکی (یا بیشتر) از این "متدها" ارتباط برقرار کنید.

---

هنگام ساخت APIها، معمولاً از این متدهای HTTP خاص برای انجام یک عمل خاص استفاده می‌کنید.

معمولاً از:

* `POST`: برای ایجاد داده.
* `GET`: برای خواندن داده.
* `PUT`: برای به‌روزرسانی داده.
* `DELETE`: برای حذف داده.

استفاده می‌کنید.

بنابراین، در OpenAPI، هر یک از متدهای HTTP یک "عملیات" نامیده می‌شود.

ما نیز آنها را "**عملیات**" خواهیم نامید.

#### تعریف یک *دکوراتور عملیات مسیر*

{* ../../docs_src/first_steps/tutorial001.py hl[6] *}

`@app.get("/")` به **FastAPI** می‌گوید که تابع زیر مسئول مدیریت درخواست‌هایی است که به:

* مسیر `/`
* با استفاده از <abbr title="متد HTTP GET"><code>get</code> عملیات</abbr>

می‌آیند.

/// info | اطلاعات `@decorator`

آن سینتکس `@something` در پایتون "دکوراتور" نامیده می‌شود.

شما آن را بالای یک تابع قرار می‌دهید. مانند یک کلاه تزئینی زیبا (حدس می‌زنم اصطلاح از اینجا آمده است).

یک "دکوراتور" تابع زیر را می‌گیرد و کاری با آن انجام می‌دهد.

در مورد ما، این دکوراتور به **FastAPI** می‌گوید که تابع زیر مربوط به **مسیر** `/` با **عملیات** `get` است.

این "**دکوراتور عملیات مسیر**" است.

///

شما همچنین می‌توانید از سایر عملیات‌ها استفاده کنید:

* `@app.post()`
* `@app.put()`
* `@app.delete()`

و موارد کمتر رایج:

* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

/// tip

شما آزاد هستید هر عملیات (متد HTTP) را همانطور که می‌خواهید استفاده کنید.

**FastAPI** هیچ معنای خاصی را اجبار نمی‌کند.

اطلاعات اینجا به عنوان یک راهنما ارائه شده، نه یک الزام.

برای مثال، هنگام استفاده از GraphQL معمولاً تمام اعمال را فقط با استفاده از عملیات‌های `POST` انجام می‌دهید.

///

### مرحله ۴: تعریف **تابع عملیات مسیر**

این "**تابع عملیات مسیر**" ماست:

* **مسیر**: `/` است.
* **عملیات**: `get` است.
* **تابع**: تابع زیر "دکوراتور" است (زیر `@app.get("/")`).

{* ../../docs_src/first_steps/tutorial001.py hl[7] *}

این یک تابع پایتون است.

هر زمان که درخواستی به URL "`/`" با عملیات `GET` دریافت کند، توسط **FastAPI** فراخوانی خواهد شد.

در این مورد، یک تابع `async` است.

---

شما همچنین می‌توانید آن را به جای `async def` به عنوان یک تابع معمولی تعریف کنید:

{* ../../docs_src/first_steps/tutorial003.py hl[7] *}

/// note

اگر تفاوت را نمی‌دانید، [Async: *"عجله دارید؟"*](../async.md#in-a-hurry){.internal-link target=_blank} را بررسی کنید.

///

### مرحله ۵: برگرداندن محتوا

{* ../../docs_src/first_steps/tutorial001.py hl[8] *}

شما می‌توانید یک `dict`، `list`، مقادیر تکی مانند `str`، `int` و غیره برگردانید.

همچنین می‌توانید مدل‌های Pydantic برگردانید (بعداً بیشتر درباره آن خواهید دید).

بسیاری از اشیاء و مدل‌های دیگر وجود دارند که به طور خودکار به JSON تبدیل خواهند شد (از جمله ORMها و غیره). سعی کنید از مورد علاقه‌های خود استفاده کنید، به احتمال زیاد از قبل پشتیبانی می‌شوند.

## خلاصه

* `FastAPI` را وارد کنید.
* یک نمونه `app` ایجاد کنید.
* یک **دکوراتور عملیات مسیر** با استفاده از دکوراتورهایی مانند `@app.get("/")` بنویسید.
* یک **تابع عملیات مسیر** تعریف کنید؛ برای مثال، `def root(): ...`.
* سرور توسعه را با دستور `fastapi dev` اجرا کنید.
