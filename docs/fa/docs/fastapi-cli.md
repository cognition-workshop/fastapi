# FastAPI CLI

**FastAPI CLI** یک برنامه خط فرمان است که می‌توانید از آن برای سرو کردن برنامه FastAPI خود، مدیریت پروژه FastAPI و موارد دیگر استفاده کنید.

وقتی FastAPI را نصب می‌کنید (مثلاً با `pip install "fastapi[standard]"`)، شامل پکیجی به نام `fastapi-cli` می‌شود، این پکیج دستور `fastapi` را در ترمینال فراهم می‌کند.

برای اجرای برنامه FastAPI خود برای توسعه، می‌توانید از دستور `fastapi dev` استفاده کنید:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with the
             following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C to
             quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

برنامه خط فرمانی که `fastapi` نامیده می‌شود، **FastAPI CLI** است.

FastAPI CLI مسیر برنامه پایتون شما (مثلاً `main.py`) را می‌گیرد و به طور خودکار نمونه `FastAPI` (که معمولاً `app` نامیده می‌شود) را تشخیص می‌دهد، فرآیند وارد کردن صحیح را تعیین می‌کند و سپس آن را سرو می‌کند.

برای تولید از `fastapi run` استفاده کنید. 🚀

به صورت داخلی، **FastAPI CLI** از <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> استفاده می‌کند، یک سرور ASGI با عملکرد بالا و آماده تولید. 😎

## `fastapi dev`

اجرای `fastapi dev` حالت توسعه را شروع می‌کند.

به طور پیش‌فرض، **بارگذاری مجدد خودکار** فعال است و به طور خودکار سرور را هنگام ایجاد تغییرات در کد شما مجدداً بارگذاری می‌کند. این منابع زیادی مصرف می‌کند و می‌تواند نسبت به حالت غیرفعال ناپایدارتر باشد. فقط باید از آن برای توسعه استفاده کنید. همچنین روی آدرس IP `127.0.0.1` گوش می‌دهد، که IP دستگاه شما برای ارتباط تنها با خودش (`localhost`) است.

## `fastapi run`

اجرای `fastapi run` FastAPI را به طور پیش‌فرض در حالت تولید شروع می‌کند.

به طور پیش‌فرض، **بارگذاری مجدد خودکار** غیرفعال است. همچنین روی آدرس IP `0.0.0.0` گوش می‌دهد، که به معنای تمام آدرس‌های IP موجود است، به این ترتیب برای هر کسی که بتواند با دستگاه ارتباط برقرار کند به صورت عمومی قابل دسترسی خواهد بود. معمولاً آن را اینگونه در تولید اجرا می‌کنید، برای مثال، در یک کانتینر.

در بیشتر موارد شما یک "پروکسی خاتمه" دارید (و باید داشته باشید) که HTTPS را بر روی آن مدیریت می‌کند، این بستگی به نحوه استقرار برنامه شما دارد، ارائه‌دهنده شما ممکن است این کار را برای شما انجام دهد، یا ممکن است نیاز باشد خودتان آن را تنظیم کنید.

/// tip

می‌توانید بیشتر درباره آن در [مستندات استقرار](deployment/index.md){.internal-link target=_blank} بیاموزید.

///
