# پیکربندی رابط Swagger

می‌توانید برخی <a href="https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/" class="external-link" target="_blank">پارامترهای اضافی Swagger UI</a> را پیکربندی کنید.

برای پیکربندی آنها، آرگومان `swagger_ui_parameters` را هنگام ایجاد شیء برنامه `FastAPI()` یا به تابع `get_swagger_ui_html()` ارسال کنید.

`swagger_ui_parameters` یک دیکشنری با پیکربندی‌هایی که مستقیماً به Swagger UI ارسال می‌شوند دریافت می‌کند.

FastAPI پیکربندی‌ها را به **JSON** تبدیل می‌کند تا با JavaScript سازگار شوند، زیرا Swagger UI به آن نیاز دارد.

## غیرفعال کردن هایلایت نحوی

برای مثال، می‌توانید هایلایت نحوی را در Swagger UI غیرفعال کنید.

بدون تغییر تنظیمات، هایلایت نحوی به طور پیش‌فرض فعال است:

<img src="/img/tutorial/extending-openapi/image02.png">

اما می‌توانید آن را با تنظیم `syntaxHighlight` به `False` غیرفعال کنید:

{* ../../docs_src/configure_swagger_ui/tutorial001.py hl[3] *}

...و سپس Swagger UI دیگر هایلایت نحوی را نمایش نخواهد داد:

<img src="/img/tutorial/extending-openapi/image03.png">

## تغییر تم

به همین ترتیب می‌توانید تم هایلایت نحوی را با کلید `"syntaxHighlight.theme"` تنظیم کنید (توجه کنید که یک نقطه در وسط دارد):

{* ../../docs_src/configure_swagger_ui/tutorial002.py hl[3] *}

آن پیکربندی تم رنگ هایلایت نحوی را تغییر خواهد داد:

<img src="/img/tutorial/extending-openapi/image04.png">

## تغییر پارامترهای پیش‌فرض Swagger UI

FastAPI شامل برخی پارامترهای پیکربندی پیش‌فرض مناسب برای اکثر موارد استفاده است.

شامل این پیکربندی‌های پیش‌فرض است:

{* ../../fastapi/openapi/docs.py ln[8:23] hl[17:23] *}

می‌توانید هر یک از آنها را با تنظیم مقدار متفاوت در آرگومان `swagger_ui_parameters` بازنویسی کنید.

برای مثال، برای غیرفعال کردن `deepLinking` می‌توانید این تنظیمات را به `swagger_ui_parameters` ارسال کنید:

{* ../../docs_src/configure_swagger_ui/tutorial003.py hl[3] *}

## سایر پارامترهای Swagger UI

برای مشاهده تمام پیکربندی‌های ممکن دیگر، <a href="https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/" class="external-link" target="_blank">مستندات رسمی پارامترهای Swagger UI</a> را بخوانید.

## تنظیمات فقط JavaScript

Swagger UI همچنین اجازه می‌دهد پیکربندی‌های دیگری به صورت اشیاء **فقط JavaScript** باشند (برای مثال، توابع JavaScript).

FastAPI همچنین این تنظیمات `presets` فقط JavaScript را شامل می‌شود:

```JavaScript
presets: [
    SwaggerUIBundle.presets.apis,
    SwaggerUIBundle.SwaggerUIStandalonePreset
]
```

اینها اشیاء **JavaScript** هستند، نه رشته‌ها، بنابراین نمی‌توانید آنها را مستقیماً از کد Python ارسال کنید.

اگر نیاز به استفاده از پیکربندی‌های فقط JavaScript مانند آنها دارید، می‌توانید از یکی از روش‌های بالا استفاده کنید. تمام *عملیات مسیر* Swagger UI را بازنویسی کنید و هر JavaScript مورد نیاز را به صورت دستی بنویسید.
