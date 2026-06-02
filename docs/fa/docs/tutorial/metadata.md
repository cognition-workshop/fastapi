# متاداده و URLهای مستندات

می‌توانید چندین پیکربندی متاداده را در برنامه **FastAPI** خود سفارشی کنید.

## متاداده برای API

می‌توانید فیلدهای زیر را که در مشخصه OpenAPI و رابط‌های کاربری مستندات خودکار API استفاده می‌شوند تنظیم کنید:

| پارامتر | تایپ | توضیحات |
|------------|------|-------------|
| `title` | `str` | عنوان API. |
| `summary` | `str` | خلاصه کوتاه API. <small>از OpenAPI 3.1.0 و FastAPI 0.99.0 در دسترس.</small> |
| `description` | `str` | توضیحات کوتاه API. می‌تواند از Markdown استفاده کند. |
| `version` | `string` | نسخه API. این نسخه برنامه خود شماست، نه OpenAPI. برای مثال `2.5.0`. |
| `terms_of_service` | `str` | URL شرایط خدمات API. اگر ارائه شود، باید یک URL باشد. |
| `contact` | `dict` | اطلاعات تماس برای API ارائه شده. می‌تواند شامل چندین فیلد باشد. <details><summary>فیلدهای <code>contact</code></summary><table><thead><tr><th>پارامتر</th><th>تایپ</th><th>توضیحات</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>str</code></td><td>نام شناسایی شخص/سازمان تماس.</td></tr><tr><td><code>url</code></td><td><code>str</code></td><td>URL اشاره کننده به اطلاعات تماس. باید در قالب URL باشد.</td></tr><tr><td><code>email</code></td><td><code>str</code></td><td>آدرس ایمیل شخص/سازمان تماس. باید در قالب آدرس ایمیل باشد.</td></tr></tbody></table></details> |
| `license_info` | `dict` | اطلاعات مجوز برای API ارائه شده. می‌تواند شامل چندین فیلد باشد. <details><summary>فیلدهای <code>license_info</code></summary><table><thead><tr><th>پارامتر</th><th>تایپ</th><th>توضیحات</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>str</code></td><td><strong>الزامی</strong> (اگر <code>license_info</code> تنظیم شده باشد). نام مجوز استفاده شده برای API.</td></tr><tr><td><code>identifier</code></td><td><code>str</code></td><td>یک عبارت مجوز <a href="https://spdx.org/licenses/" class="external-link" target="_blank">SPDX</a> برای API. فیلد <code>identifier</code> با فیلد <code>url</code> متقابلاً انحصاری است. <small>از OpenAPI 3.1.0 و FastAPI 0.99.0 در دسترس.</small></td></tr><tr><td><code>url</code></td><td><code>str</code></td><td>URL مجوز استفاده شده برای API. باید در قالب URL باشد.</td></tr></tbody></table></details> |

می‌توانید آنها را به صورت زیر تنظیم کنید:

{* ../../docs_src/metadata/tutorial001.py hl[3:16, 19:32] *}

/// tip

می‌توانید در فیلد `description` Markdown بنویسید و در خروجی رندر خواهد شد.

///

با این پیکربندی، مستندات خودکار API به این شکل خواهد بود:

<img src="/img/tutorial/metadata/image01.png">

## شناسه مجوز

از OpenAPI 3.1.0 و FastAPI 0.99.0، همچنین می‌توانید `license_info` را با یک `identifier` به جای `url` تنظیم کنید.

برای مثال:

{* ../../docs_src/metadata/tutorial001_1.py hl[31] *}

## متاداده برای تگ‌ها

همچنین می‌توانید متاداده اضافی برای تگ‌های مختلف استفاده شده برای گروه‌بندی عملیات‌های مسیر با پارامتر `openapi_tags` اضافه کنید.

یک لیست شامل یک دیکشنری برای هر تگ می‌گیرد.

هر دیکشنری می‌تواند شامل موارد زیر باشد:

* `name` (**الزامی**): یک `str` با همان نام تگ که در پارامتر `tags` در *عملیات‌های مسیر* و `APIRouter`ها استفاده می‌کنید.
* `description`: یک `str` با توضیحات کوتاه برای تگ. می‌تواند Markdown داشته باشد و در رابط کاربری مستندات نمایش داده خواهد شد.
* `externalDocs`: یک `dict` توصیف‌کننده مستندات خارجی با:
    * `description`: یک `str` با توضیحات کوتاه برای مستندات خارجی.
    * `url` (**الزامی**): یک `str` با URL مستندات خارجی.

### ایجاد متاداده برای تگ‌ها

بیایید آن را در مثالی با تگ‌هایی برای `users` و `items` امتحان کنیم.

متاداده برای تگ‌های خود ایجاد کنید و آن را به پارامتر `openapi_tags` ارسال کنید:

{* ../../docs_src/metadata/tutorial004.py hl[3:16,18] *}

توجه کنید که می‌توانید از Markdown در توضیحات استفاده کنید، برای مثال "login" به صورت درشت (**login**) و "fancy" به صورت مورب (_fancy_) نمایش داده خواهد شد.

/// tip

لازم نیست برای تمام تگ‌هایی که استفاده می‌کنید متاداده اضافه کنید.

///

### استفاده از تگ‌ها

از پارامتر `tags` با *عملیات‌های مسیر* خود (و `APIRouter`ها) برای اختصاص آنها به تگ‌های مختلف استفاده کنید:

{* ../../docs_src/metadata/tutorial004.py hl[21,26] *}

/// info

بیشتر درباره تگ‌ها در [پیکربندی عملیات مسیر](path-operation-configuration.md#tags){.internal-link target=_blank} بخوانید.

///

### بررسی مستندات

اکنون، اگر مستندات را بررسی کنید، تمام متاداده اضافی را نشان خواهند داد:

<img src="/img/tutorial/metadata/image02.png">

### ترتیب تگ‌ها

ترتیب هر دیکشنری متاداده تگ همچنین ترتیب نمایش در رابط کاربری مستندات را تعریف می‌کند.

برای مثال، حتی اگرچه `users` از نظر الفبایی بعد از `items` می‌آید، قبل از آنها نمایش داده می‌شود، زیرا متاداده آن را به عنوان اولین دیکشنری در لیست اضافه کردیم.

## URL اسکیمای OpenAPI

به طور پیش‌فرض، اسکیمای OpenAPI در `/openapi.json` ارائه می‌شود.

اما می‌توانید آن را با پارامتر `openapi_url` پیکربندی کنید.

برای مثال، برای تنظیم ارائه آن در `/api/v1/openapi.json`:

{* ../../docs_src/metadata/tutorial002.py hl[3] *}

اگر می‌خواهید اسکیمای OpenAPI را کاملاً غیرفعال کنید، می‌توانید `openapi_url=None` تنظیم کنید، که رابط‌های کاربری مستنداتی که از آن استفاده می‌کنند را نیز غیرفعال خواهد کرد.

## URLهای مستندات

می‌توانید دو رابط کاربری مستندات شامل شده را پیکربندی کنید:

* **Swagger UI**: در `/docs` ارائه می‌شود.
    * می‌توانید URL آن را با پارامتر `docs_url` تنظیم کنید.
    * می‌توانید با تنظیم `docs_url=None` آن را غیرفعال کنید.
* **ReDoc**: در `/redoc` ارائه می‌شود.
    * می‌توانید URL آن را با پارامتر `redoc_url` تنظیم کنید.
    * می‌توانید با تنظیم `redoc_url=None` آن را غیرفعال کنید.

برای مثال، برای تنظیم Swagger UI برای ارائه در `/documentation` و غیرفعال کردن ReDoc:

{* ../../docs_src/metadata/tutorial003.py hl[3] *}
