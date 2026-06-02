# قالب‌ها

شما می‌توانید از هر موتور قالب‌سازی که می‌خواهید با **FastAPI** استفاده کنید.

یک انتخاب رایج Jinja2 است، همان موردی که توسط Flask و سایر ابزارها استفاده می‌شود.

ابزارهایی برای پیکربندی آسان آن وجود دارد که می‌توانید مستقیماً در برنامه **FastAPI** خود استفاده کنید (ارائه شده توسط Starlette).

## نصب وابستگی‌ها

مطمئن شوید که یک [محیط مجازی](../virtual-environments.md){.internal-link target=_blank} ایجاد کرده‌اید، آن را فعال کنید و `jinja2` را نصب کنید:

<div class="termy">

```console
$ pip install jinja2

---> 100%
```

</div>

## استفاده از `Jinja2Templates`

* `Jinja2Templates` را وارد کنید.
* یک شیء `templates` ایجاد کنید که بعداً بتوانید دوباره استفاده کنید.
* یک پارامتر `Request` را در *عملیات مسیر* که یک قالب برمی‌گرداند تعریف کنید.
* از `templates` ایجاد شده برای رندر و برگرداندن یک `TemplateResponse` استفاده کنید، نام قالب، شیء درخواست و یک دیکشنری "context" با جفت‌های کلید-مقدار برای استفاده در قالب Jinja2 را ارسال کنید.

{* ../../docs_src/templates/tutorial001.py hl[4,11,15:18] *}

/// note

قبل از FastAPI 0.108.0، Starlette 0.29.0، `name` اولین پارامتر بود.

همچنین، قبل از آن، در نسخه‌های قبلی، شیء `request` به عنوان بخشی از جفت‌های کلید-مقدار در context برای Jinja2 ارسال می‌شد.

///

/// tip

با تعریف `response_class=HTMLResponse`، رابط مستندات قادر خواهد بود بداند که پاسخ HTML خواهد بود.

///

/// note | جزئیات فنی

شما همچنین می‌توانید از `from starlette.templating import Jinja2Templates` استفاده کنید.

**FastAPI** همان `starlette.templating` را به عنوان `fastapi.templating` فقط به عنوان یک سهولت برای شما به عنوان برنامه‌نویس فراهم می‌کند. اما بیشتر پاسخ‌های موجود مستقیماً از Starlette می‌آیند. همینطور `Request` و `StaticFiles`.

///

## نوشتن قالب‌ها

سپس می‌توانید یک قالب در `templates/item.html` بنویسید، برای مثال:

```jinja hl_lines="7"
{!../../docs_src/templates/templates/item.html!}
```

### مقادیر Context قالب

در HTML که شامل:

{% raw %}

```jinja
Item ID: {{ id }}
```

{% endraw %}

...مقدار `id` گرفته شده از دیکشنری "context" که ارسال کردید را نمایش می‌دهد:

```Python
{"id": id}
```

برای مثال، با ID برابر `42`، این به صورت زیر رندر می‌شود:

```html
Item ID: 42
```

### آرگومان‌های `url_for` قالب

همچنین می‌توانید از `url_for()` در داخل قالب استفاده کنید، همان آرگومان‌هایی را می‌گیرد که توسط *تابع عملیات مسیر* شما استفاده می‌شود.

بنابراین، بخش:

{% raw %}

```jinja
<a href="{{ url_for('read_item', id=id) }}">
```

{% endraw %}

...لینکی به همان URL که توسط *تابع عملیات مسیر* `read_item(id=id)` مدیریت می‌شود تولید خواهد کرد.

برای مثال، با ID برابر `42`، این به صورت زیر رندر می‌شود:

```html
<a href="/items/42">
```

## قالب‌ها و فایل‌های استاتیک

همچنین می‌توانید از `url_for()` در داخل قالب استفاده کنید و آن را، برای مثال، با `StaticFiles` که با `name="static"` سوار کرده‌اید استفاده کنید.

```jinja hl_lines="4"
{!../../docs_src/templates/templates/item.html!}
```

در این مثال، به یک فایل CSS در `static/styles.css` لینک می‌دهد با:

```CSS hl_lines="4"
{!../../docs_src/templates/static/styles.css!}
```

و از آنجا که از `StaticFiles` استفاده می‌کنید، آن فایل CSS به طور خودکار توسط برنامه **FastAPI** شما در URL `/static/styles.css` سرو خواهد شد.

## جزئیات بیشتر

برای جزئیات بیشتر، از جمله نحوه تست قالب‌ها، <a href="https://www.starlette.io/templates/" class="external-link" target="_blank">مستندات Starlette درباره قالب‌ها</a> را بررسی کنید.
