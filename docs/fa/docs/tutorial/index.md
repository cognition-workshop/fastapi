# آموزش - راهنمای کاربر

این آموزش نحوه استفاده از **FastAPI** با بیشتر ویژگی‌های آن را، قدم به قدم، به شما نشان می‌دهد.

هر بخش به تدریج بر بخش‌های قبلی بنا شده، اما به گونه‌ای ساختاردهی شده که موضوعات جدا باشند، تا بتوانید مستقیماً به هر مورد خاص بروید و نیاز خاص API خود را حل کنید.

همچنین به گونه‌ای ساخته شده که به عنوان یک مرجع آینده عمل کند تا بتوانید برگردید و دقیقاً آنچه نیاز دارید را ببینید.

## اجرای کد

تمام بلوک‌های کد قابل کپی و استفاده مستقیم هستند (آنها در واقع فایل‌های پایتون تست شده هستند).

برای اجرای هر یک از مثال‌ها، کد را در فایلی به نام `main.py` کپی کنید و `fastapi dev` را اجرا کنید:

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

**به شدت توصیه می‌شود** که کد را بنویسید یا کپی کنید، آن را ویرایش کنید و به صورت محلی اجرا کنید.

استفاده از آن در ویرایشگر شما چیزی است که واقعاً مزایای FastAPI را به شما نشان می‌دهد، با دیدن اینکه چقدر کد کمی باید بنویسید، تمام بررسی‌های تایپ، تکمیل خودکار و غیره.

---

## نصب FastAPI

اولین قدم نصب FastAPI است.

مطمئن شوید یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کنید، آن را فعال کنید و سپس **FastAPI را نصب کنید**:

<div class="termy">

```console
$ pip install "fastapi[standard]"

---> 100%
```

</div>

/// note

وقتی با `pip install "fastapi[standard]"` نصب می‌کنید، برخی وابستگی‌های استاندارد اختیاری پیش‌فرض همراه آن می‌آیند.

اگر نمی‌خواهید آن وابستگی‌های اختیاری را داشته باشید، می‌توانید به جای آن `pip install fastapi` نصب کنید.

///

## راهنمای کاربر پیشرفته

همچنین یک **راهنمای کاربر پیشرفته** وجود دارد که می‌توانید بعداً بعد از این **آموزش - راهنمای کاربر** بخوانید.

**راهنمای کاربر پیشرفته** بر این آموزش بنا شده، از همان مفاهیم استفاده می‌کند و برخی ویژگی‌های اضافی را آموزش می‌دهد.

اما ابتدا باید **آموزش - راهنمای کاربر** (آنچه الان می‌خوانید) را بخوانید.

به گونه‌ای طراحی شده که بتوانید یک برنامه کامل فقط با **آموزش - راهنمای کاربر** بسازید و سپس آن را به روش‌های مختلف، بسته به نیازهایتان، با استفاده از برخی ایده‌های اضافی از **راهنمای کاربر پیشرفته** گسترش دهید.
