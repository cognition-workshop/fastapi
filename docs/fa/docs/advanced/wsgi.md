# شامل کردن WSGI - Flask، Django و سایرین

شما می‌توانید برنامه‌های WSGI را مانند آنچه در [زیربرنامه‌ها - سوار کردن](sub-applications.md){.internal-link target=_blank}، [پشت پروکسی](behind-a-proxy.md){.internal-link target=_blank} دیدید، سوار کنید.

برای این کار، می‌توانید از `WSGIMiddleware` استفاده کنید و آن را برای پوشش برنامه WSGI خود، به عنوان مثال Flask، Django و غیره به کار ببرید.

## استفاده از `WSGIMiddleware`

باید `WSGIMiddleware` را وارد کنید.

سپس برنامه WSGI (مثلاً Flask) را با میان‌افزار بپوشانید.

و سپس آن را در یک مسیر سوار کنید.

{* ../../docs_src/wsgi/tutorial001.py hl[2:3,3] *}

## بررسی کنید

اکنون، هر درخواست تحت مسیر `/v1/` توسط برنامه Flask پردازش خواهد شد.

و بقیه توسط **FastAPI** پردازش خواهند شد.

اگر آن را اجرا کنید و به <a href="http://localhost:8000/v1/" class="external-link" target="_blank">http://localhost:8000/v1/</a> بروید، پاسخ Flask را خواهید دید:

```txt
Hello, World from Flask!
```

و اگر به <a href="http://localhost:8000/v2" class="external-link" target="_blank">http://localhost:8000/v2</a> بروید، پاسخ FastAPI را خواهید دید:

```JSON
{
    "message": "Hello World"
}
```
