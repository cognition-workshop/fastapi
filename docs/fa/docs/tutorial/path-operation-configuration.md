# پیکربندی عملیات مسیر

چندین پارامتر وجود دارد که می‌توانید به *دکوراتور عملیات مسیر* خود برای پیکربندی آن ارسال کنید.

/// warning

توجه کنید که این پارامترها مستقیماً به *دکوراتور عملیات مسیر* ارسال می‌شوند، نه به *تابع عملیات مسیر* شما.

///

## کد وضعیت پاسخ

می‌توانید (HTTP) `status_code` مورد استفاده در پاسخ *عملیات مسیر* خود را تعریف کنید.

می‌توانید مستقیماً کد `int` مانند `404` را ارسال کنید.

اما اگر به یاد ندارید هر کد عددی برای چیست، می‌توانید از ثابت‌های میانبر در `status` استفاده کنید:

{* ../../docs_src/path_operation_configuration/tutorial001_py310.py hl[1,15] *}

آن کد وضعیت در پاسخ استفاده خواهد شد و به اسکیمای OpenAPI اضافه خواهد شد.

/// note | جزئیات فنی

همچنین می‌توانید از `from starlette import status` استفاده کنید.

**FastAPI** همان `starlette.status` را به عنوان `fastapi.status` فقط به عنوان راحتی برای شما، توسعه‌دهنده، ارائه می‌دهد. اما مستقیماً از Starlette می‌آید.

///

## تگ‌ها

می‌توانید تگ‌ها به *عملیات مسیر* خود اضافه کنید، پارامتر `tags` را با یک `list` از `str` (معمولاً فقط یک `str`) ارسال کنید:

{* ../../docs_src/path_operation_configuration/tutorial002_py310.py hl[15,20,25] *}

آنها به اسکیمای OpenAPI اضافه شده و توسط رابط‌های مستندات خودکار استفاده خواهند شد:

<img src="/img/tutorial/path-operation-configuration/image01.png">

### تگ‌ها با Enum

اگر برنامه بزرگی دارید، ممکن است **تگ‌های متعدد** جمع شوند، و بخواهید مطمئن شوید همیشه **همان تگ** را برای *عملیات‌های مسیر* مرتبط استفاده می‌کنید.

در این موارد، ذخیره تگ‌ها در یک `Enum` منطقی خواهد بود.

**FastAPI** آن را به همان شکل رشته‌های ساده پشتیبانی می‌کند:

{* ../../docs_src/path_operation_configuration/tutorial002b.py hl[1,8:10,13,18] *}

## خلاصه و توضیحات

می‌توانید `summary` و `description` اضافه کنید:

{* ../../docs_src/path_operation_configuration/tutorial003_py310.py hl[18:19] *}

## توضیحات از docstring

از آنجا که توضیحات معمولاً طولانی هستند و چندین خط را پوشش می‌دهند، می‌توانید توضیحات *عملیات مسیر* را در <abbr title="یک رشته چندخطی به عنوان اولین عبارت درون یک تابع (که به هیچ متغیری اختصاص داده نشده) و برای مستندسازی استفاده می‌شود">docstring</abbr> تابع اعلان کنید و **FastAPI** آن را از آنجا خواهد خواند.

می‌توانید <a href="https://en.wikipedia.org/wiki/Markdown" class="external-link" target="_blank">Markdown</a> در docstring بنویسید، به درستی تفسیر و نمایش داده خواهد شد (با در نظر گرفتن تورفتگی docstring).

{* ../../docs_src/path_operation_configuration/tutorial004_py310.py hl[17:25] *}

در مستندات تعاملی استفاده خواهد شد:

<img src="/img/tutorial/path-operation-configuration/image02.png">

## توضیحات پاسخ

می‌توانید توضیحات پاسخ را با پارامتر `response_description` مشخص کنید:

{* ../../docs_src/path_operation_configuration/tutorial005_py310.py hl[19] *}

/// info

توجه کنید که `response_description` به طور خاص به پاسخ اشاره دارد، `description` به *عملیات مسیر* به طور کلی اشاره دارد.

///

/// check

OpenAPI مشخص می‌کند که هر *عملیات مسیر* به توضیحات پاسخ نیاز دارد.

بنابراین، اگر یکی ارائه ندهید، **FastAPI** به طور خودکار یکی با عنوان "Successful response" تولید خواهد کرد.

///

<img src="/img/tutorial/path-operation-configuration/image03.png">

## منسوخ کردن یک *عملیات مسیر*

اگر نیاز دارید یک *عملیات مسیر* را به عنوان <abbr title="منسوخ، توصیه به عدم استفاده">منسوخ</abbr> علامت‌گذاری کنید، بدون حذف آن، پارامتر `deprecated` را ارسال کنید:

{* ../../docs_src/path_operation_configuration/tutorial006.py hl[16] *}

در مستندات تعاملی به وضوح به عنوان منسوخ علامت‌گذاری خواهد شد:

<img src="/img/tutorial/path-operation-configuration/image04.png">

ببینید *عملیات‌های مسیر* منسوخ و غیرمنسوخ چگونه به نظر می‌رسند:

<img src="/img/tutorial/path-operation-configuration/image05.png">

## خلاصه

می‌توانید به راحتی با ارسال پارامترها به *دکوراتورهای عملیات مسیر*، متاداده را برای *عملیات‌های مسیر* خود پیکربندی و اضافه کنید.
