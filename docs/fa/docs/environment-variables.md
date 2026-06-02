# متغیرهای محیطی

/// tip

اگر قبلاً می‌دانید "متغیرهای محیطی" چیست و چگونه از آنها استفاده کنید، می‌توانید از این بخش رد شوید.

///

یک متغیر محیطی (همچنین به عنوان "**env var**" شناخته می‌شود) متغیری است که **خارج** از کد پایتون، در **سیستم عامل** زندگی می‌کند و می‌تواند توسط کد پایتون شما (یا توسط برنامه‌های دیگر نیز) خوانده شود.

متغیرهای محیطی می‌توانند برای مدیریت **تنظیمات** برنامه، به عنوان بخشی از **نصب** پایتون و غیره مفید باشند.

## ایجاد و استفاده از متغیرهای محیطی

می‌توانید متغیرهای محیطی را در **شل (ترمینال)** ایجاد و استفاده کنید، بدون نیاز به پایتون:

//// tab | Linux, macOS, Windows Bash

<div class="termy">

```console
// You could create an env var MY_NAME with
$ export MY_NAME="Wade Wilson"

// Then you could use it with other programs, like
$ echo "Hello $MY_NAME"

Hello Wade Wilson
```

</div>

////

//// tab | Windows PowerShell

<div class="termy">

```console
// Create an env var MY_NAME
$ $Env:MY_NAME = "Wade Wilson"

// Use it with other programs, like
$ echo "Hello $Env:MY_NAME"

Hello Wade Wilson
```

</div>

////

## خواندن متغیرهای محیطی در پایتون

همچنین می‌توانید متغیرهای محیطی را **خارج** از پایتون، در ترمینال (یا با هر روش دیگری) ایجاد کنید و سپس **آنها را در پایتون بخوانید**.

به عنوان مثال می‌توانید فایل `main.py` با محتوای زیر داشته باشید:

```Python hl_lines="3"
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
```

/// tip

آرگومان دوم <a href="https://docs.python.org/3.8/library/os.html#os.getenv" class="external-link" target="_blank">`os.getenv()`</a> مقدار پیش‌فرض برای برگرداندن است.

اگر ارائه نشود، به طور پیش‌فرض `None` است، اینجا `"World"` را به عنوان مقدار پیش‌فرض ارائه می‌دهیم.

///

سپس می‌توانید آن برنامه پایتون را فراخوانی کنید:

//// tab | Linux, macOS, Windows Bash

<div class="termy">

```console
// Here we don't set the env var yet
$ python main.py

// As we didn't set the env var, we get the default value

Hello World from Python

// But if we create an environment variable first
$ export MY_NAME="Wade Wilson"

// And then call the program again
$ python main.py

// Now it can read the environment variable

Hello Wade Wilson from Python
```

</div>

////

//// tab | Windows PowerShell

<div class="termy">

```console
// Here we don't set the env var yet
$ python main.py

// As we didn't set the env var, we get the default value

Hello World from Python

// But if we create an environment variable first
$ $Env:MY_NAME = "Wade Wilson"

// And then call the program again
$ python main.py

// Now it can read the environment variable

Hello Wade Wilson from Python
```

</div>

////

از آنجا که متغیرهای محیطی می‌توانند خارج از کد تنظیم شوند، اما توسط کد خوانده شوند و نیازی به ذخیره (commit به `git`) همراه با بقیه فایل‌ها ندارند، استفاده از آنها برای پیکربندی‌ها یا **تنظیمات** رایج است.

همچنین می‌توانید یک متغیر محیطی فقط برای **فراخوانی خاص یک برنامه** ایجاد کنید، که فقط برای آن برنامه و فقط در طول مدت اجرای آن در دسترس است.

برای این کار، آن را درست قبل از خود برنامه، در همان خط ایجاد کنید:

<div class="termy">

```console
// Create an env var MY_NAME in line for this program call
$ MY_NAME="Wade Wilson" python main.py

// Now it can read the environment variable

Hello Wade Wilson from Python

// The env var no longer exists afterwards
$ python main.py

Hello World from Python
```

</div>

/// tip

می‌توانید بیشتر درباره آن در <a href="https://12factor.net/config" class="external-link" target="_blank">The Twelve-Factor App: Config</a> بخوانید.

///

## انواع و اعتبارسنجی

این متغیرهای محیطی فقط می‌توانند **رشته‌های متنی** را مدیریت کنند، زیرا خارجی نسبت به پایتون هستند و باید با برنامه‌های دیگر و بقیه سیستم (و حتی با سیستم‌عامل‌های مختلف مانند Linux، Windows، macOS) سازگار باشند.

این به این معنی است که **هر مقداری** که در پایتون از یک متغیر محیطی خوانده شود **یک `str` خواهد بود** و هر تبدیل به نوع دیگر یا هر اعتبارسنجی باید در کد انجام شود.

بیشتر درباره استفاده از متغیرهای محیطی برای مدیریت **تنظیمات برنامه** در [راهنمای کاربر پیشرفته - تنظیمات و متغیرهای محیطی](./advanced/settings.md){.internal-link target=_blank} خواهید آموخت.

## متغیر محیطی `PATH`

یک متغیر محیطی **خاص** به نام **`PATH`** وجود دارد که توسط سیستم‌عامل‌ها (Linux، macOS، Windows) برای یافتن برنامه‌ها جهت اجرا استفاده می‌شود.

مقدار متغیر `PATH` یک رشته طولانی است که از دایرکتوری‌هایی تشکیل شده که با دو نقطه `:` در Linux و macOS و با نقطه ویرگول `;` در Windows جدا شده‌اند.

به عنوان مثال، متغیر محیطی `PATH` می‌تواند مانند زیر باشد:

//// tab | Linux, macOS

```plaintext
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

این به این معنی است که سیستم باید برنامه‌ها را در دایرکتوری‌های زیر جستجو کند:

* `/usr/local/bin`
* `/usr/bin`
* `/bin`
* `/usr/sbin`
* `/sbin`

////

//// tab | Windows

```plaintext
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32
```

این به این معنی است که سیستم باید برنامه‌ها را در دایرکتوری‌های زیر جستجو کند:

* `C:\Program Files\Python312\Scripts`
* `C:\Program Files\Python312`
* `C:\Windows\System32`

////

وقتی یک **دستور** را در ترمینال تایپ می‌کنید، سیستم عامل برنامه را در **هر یک از آن دایرکتوری‌ها** لیست‌شده در متغیر محیطی `PATH` **جستجو می‌کند**.

به عنوان مثال، وقتی `python` را در ترمینال تایپ می‌کنید، سیستم عامل برنامه‌ای به نام `python` را در **اولین دایرکتوری** آن لیست جستجو می‌کند.

اگر آن را پیدا کند، **از آن استفاده می‌کند**. در غیر این صورت به جستجو در **دایرکتوری‌های دیگر** ادامه می‌دهد.

### نصب پایتون و به‌روزرسانی `PATH`

هنگام نصب پایتون، ممکن است از شما پرسیده شود آیا می‌خواهید متغیر محیطی `PATH` را به‌روزرسانی کنید.

//// tab | Linux, macOS

فرض کنید پایتون را نصب می‌کنید و در دایرکتوری `/opt/custompython/bin` قرار می‌گیرد.

اگر بله را برای به‌روزرسانی متغیر محیطی `PATH` بگویید، نصب‌کننده `/opt/custompython/bin` را به متغیر محیطی `PATH` اضافه خواهد کرد.

می‌تواند مانند زیر باشد:

```plaintext
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/custompython/bin
```

به این ترتیب، وقتی `python` را در ترمینال تایپ می‌کنید، سیستم برنامه پایتون را در `/opt/custompython/bin` (آخرین دایرکتوری) پیدا و از آن استفاده خواهد کرد.

////

//// tab | Windows

فرض کنید پایتون را نصب می‌کنید و در دایرکتوری `C:\opt\custompython\bin` قرار می‌گیرد.

اگر بله را برای به‌روزرسانی متغیر محیطی `PATH` بگویید، نصب‌کننده `C:\opt\custompython\bin` را به متغیر محیطی `PATH` اضافه خواهد کرد.

```plaintext
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32;C:\opt\custompython\bin
```

به این ترتیب، وقتی `python` را در ترمینال تایپ می‌کنید، سیستم برنامه پایتون را در `C:\opt\custompython\bin` (آخرین دایرکتوری) پیدا و از آن استفاده خواهد کرد.

////

بنابراین، اگر تایپ کنید:

<div class="termy">

```console
$ python
```

</div>

//// tab | Linux, macOS

سیستم برنامه `python` را در `/opt/custompython/bin` **پیدا** و اجرا خواهد کرد.

تقریباً معادل تایپ کردن زیر خواهد بود:

<div class="termy">

```console
$ /opt/custompython/bin/python
```

</div>

////

//// tab | Windows

سیستم برنامه `python` را در `C:\opt\custompython\bin\python` **پیدا** و اجرا خواهد کرد.

تقریباً معادل تایپ کردن زیر خواهد بود:

<div class="termy">

```console
$ C:\opt\custompython\bin\python
```

</div>

////

این اطلاعات هنگام یادگیری درباره [محیط‌های مجازی](virtual-environments.md){.internal-link target=_blank} مفید خواهد بود.

## نتیجه‌گیری

با این مطالب باید درک پایه‌ای از **متغیرهای محیطی** و نحوه استفاده از آنها در پایتون داشته باشید.

همچنین می‌توانید بیشتر درباره آنها در <a href="https://en.wikipedia.org/wiki/Environment_variable" class="external-link" target="_blank">ویکی‌پدیا برای متغیر محیطی</a> بخوانید.

در بسیاری از موارد مشخص نیست که متغیرهای محیطی چگونه فوراً مفید و قابل استفاده هستند. اما در بسیاری از سناریوهای مختلف هنگام توسعه ظاهر می‌شوند، بنابراین دانستن درباره آنها خوب است.

به عنوان مثال، به این اطلاعات در بخش بعدی، درباره [محیط‌های مجازی](virtual-environments.md) نیاز خواهید داشت.
