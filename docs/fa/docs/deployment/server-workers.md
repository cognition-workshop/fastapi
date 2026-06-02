# کارگرهای سرور - Uvicorn با کارگرها

بیایید مفاهیم استقرار قبلی را مرور کنیم:

* امنیت - HTTPS
* اجرا در هنگام راه‌اندازی
* راه‌اندازی مجدد
* **تکرار (تعداد فرآیندهای در حال اجرا)**
* حافظه
* مراحل قبلی پیش از شروع

تا این مرحله، با تمام آموزش‌های موجود در مستندات، احتمالاً یک **برنامه سرور** اجرا کرده‌اید، به عنوان مثال، با استفاده از دستور `fastapi`، که Uvicorn را اجرا می‌کند و یک **فرآیند واحد** اجرا می‌کند.

هنگام استقرار برنامه‌ها احتمالاً می‌خواهید مقداری **تکرار فرآیندها** داشته باشید تا از **هسته‌های متعدد** بهره ببرید و بتوانید درخواست‌های بیشتری را مدیریت کنید.

همانطور که در فصل قبلی درباره [مفاهیم استقرار](concepts.md){.internal-link target=_blank} دیدید، چندین استراتژی وجود دارد که می‌توانید استفاده کنید.

اینجا به شما نشان خواهم داد چگونه از **Uvicorn** با **فرآیندهای کارگر** با استفاده از دستور `fastapi` یا دستور `uvicorn` مستقیماً استفاده کنید.

/// info

اگر از کانتینرها استفاده می‌کنید، به عنوان مثال با Docker یا Kubernetes، در فصل بعدی بیشتر درباره آن خواهم گفت: [FastAPI در کانتینرها - Docker](docker.md){.internal-link target=_blank}.

به طور خاص، هنگام اجرا روی **Kubernetes** احتمالاً **نمی‌خواهید** از کارگرها استفاده کنید و در عوض **یک فرآیند واحد Uvicorn به ازای هر کانتینر** اجرا کنید، اما در آن فصل درباره آن خواهم گفت.

///

## چندین کارگر

می‌توانید چندین کارگر را با گزینه خط فرمان `--workers` شروع کنید:

//// tab | `fastapi`

اگر از دستور `fastapi` استفاده می‌کنید:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> run --workers 4 <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting production server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with the
             following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000/docs</u></font>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font> <b>(</b>Press CTRL+C to
             quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started parent process <b>[</b><font color="#34E2E2"><b>27365</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27368</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27369</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27370</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27367</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

////

//// tab | `uvicorn`

اگر ترجیح می‌دهید مستقیماً از دستور `uvicorn` استفاده کنید:

<div class="termy">

```console
$ uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
<font color="#A6E22E">INFO</font>:     Uvicorn running on <b>http://0.0.0.0:8080</b> (Press CTRL+C to quit)
<font color="#A6E22E">INFO</font>:     Started parent process [<font color="#A1EFE4"><b>27365</b></font>]
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27368</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27369</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27370</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27367</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
```

</div>

////

تنها گزینه جدید اینجا `--workers` است که به Uvicorn می‌گوید ۴ فرآیند کارگر شروع کند.

همچنین می‌توانید ببینید که **PID** هر فرآیند را نشان می‌دهد، `27365` برای فرآیند والد (این **مدیر فرآیند** است) و یکی برای هر فرآیند کارگر: `27368`، `27369`، `27370` و `27367`.

## مفاهیم استقرار

اینجا دیدید چگونه از چندین **کارگر** برای **موازی‌سازی** اجرای برنامه استفاده کنید، از **هسته‌های متعدد** CPU بهره ببرید و بتوانید **درخواست‌های بیشتری** سرویس دهید.

از لیست مفاهیم استقرار بالا، استفاده از کارگرها عمدتاً به بخش **تکرار** کمک می‌کند، و کمی به **راه‌اندازی مجدد**، اما همچنان باید موارد دیگر را مدیریت کنید:

* **امنیت - HTTPS**
* **اجرا در هنگام راه‌اندازی**
* ***راه‌اندازی مجدد***
* تکرار (تعداد فرآیندهای در حال اجرا)
* **حافظه**
* **مراحل قبلی پیش از شروع**

## کانتینرها و Docker

در فصل بعدی درباره [FastAPI در کانتینرها - Docker](docker.md){.internal-link target=_blank} برخی استراتژی‌هایی را توضیح خواهم داد که می‌توانید برای مدیریت سایر **مفاهیم استقرار** استفاده کنید.

به شما نشان خواهم داد چگونه **ایمیج خود را از صفر بسازید** تا یک فرآیند واحد Uvicorn اجرا کنید. یک فرآیند ساده است و احتمالاً همان چیزی است که می‌خواهید هنگام استفاده از یک سیستم مدیریت کانتینر توزیع‌شده مانند **Kubernetes** انجام دهید.

## جمع‌بندی

می‌توانید از چندین فرآیند کارگر با گزینه CLI `--workers` با دستورات `fastapi` یا `uvicorn` برای بهره‌برداری از **CPUهای چند هسته‌ای** و اجرای **چندین فرآیند به صورت موازی** استفاده کنید.

اگر در حال تنظیم **سیستم استقرار خود** هستید و خودتان مفاهیم استقرار دیگر را مدیریت می‌کنید، می‌توانید از این ابزارها و ایده‌ها استفاده کنید.

فصل بعدی را بررسی کنید تا درباره **FastAPI** با کانتینرها (مثلاً Docker و Kubernetes) بیاموزید. خواهید دید که آن ابزارها راه‌های ساده‌ای برای حل سایر **مفاهیم استقرار** نیز دارند. ✨
