# پیکربندی پیشرفته عملیات مسیر

## operationId OpenAPI

/// warning

اگر "متخصص" OpenAPI نیستید، احتمالاً به این نیاز ندارید.

///

می‌توانید `operationId` OpenAPI را که در *عملیات مسیر* شما استفاده می‌شود با پارامتر `operation_id` تنظیم کنید.

باید مطمئن شوید که برای هر عملیات منحصربه‌فرد باشد.

{* ../../docs_src/path_operation_advanced_configuration/tutorial001.py hl[6] *}

### استفاده از نام *تابع عملیات مسیر* به عنوان operationId

اگر می‌خواهید از نام توابع API خود به عنوان `operationId` استفاده کنید، می‌توانید روی همه آنها تکرار کنید و `operation_id` هر *عملیات مسیر* را با استفاده از `APIRoute.name` بازنویسی کنید.

باید این کار را بعد از اضافه کردن تمام *عملیات‌های مسیر* انجام دهید.

{* ../../docs_src/path_operation_advanced_configuration/tutorial002.py hl[2, 12:21, 24] *}

/// tip

اگر `app.openapi()` را به صورت دستی فراخوانی می‌کنید، باید `operationId`ها را قبل از آن به‌روز کنید.

///

/// warning

اگر این کار را انجام دهید، باید مطمئن شوید هر یک از *توابع عملیات مسیر* شما نام منحصربه‌فردی دارد.

حتی اگر در ماژول‌های مختلف (فایل‌های Python) باشند.

///

## حذف از OpenAPI

برای حذف یک *عملیات مسیر* از شمای OpenAPI تولید شده (و بنابراین، از سیستم‌های مستندسازی خودکار)، از پارامتر `include_in_schema` استفاده کنید و آن را به `False` تنظیم کنید:

{* ../../docs_src/path_operation_advanced_configuration/tutorial003.py hl[6] *}

## توضیحات پیشرفته از docstring

می‌توانید خطوط استفاده شده از docstring *تابع عملیات مسیر* را برای OpenAPI محدود کنید.

اضافه کردن `\f` (یک کاراکتر "form feed" فرار شده) باعث می‌شود **FastAPI** خروجی استفاده شده برای OpenAPI را در این نقطه کوتاه کند.

در مستندات نمایش داده نخواهد شد، اما ابزارهای دیگر (مانند Sphinx) قادر به استفاده از بقیه خواهند بود.

{* ../../docs_src/path_operation_advanced_configuration/tutorial004.py hl[19:29] *}

## پاسخ‌های اضافی

احتمالاً دیده‌اید چگونه `response_model` و `status_code` را برای یک *عملیات مسیر* اعلام کنید.

آن متاداده درباره پاسخ اصلی یک *عملیات مسیر* را تعریف می‌کند.

همچنین می‌توانید پاسخ‌های اضافی با مدل‌ها، کدهای وضعیت و غیره اعلام کنید.

یک فصل کامل در اینجا در مستندات درباره آن وجود دارد، می‌توانید آن را در [پاسخ‌های اضافی در OpenAPI](additional-responses.md){.internal-link target=_blank} بخوانید.

## اضافات OpenAPI

وقتی یک *عملیات مسیر* در برنامه خود اعلام می‌کنید، **FastAPI** به طور خودکار متاداده مربوطه درباره آن *عملیات مسیر* را برای گنجاندن در شمای OpenAPI تولید می‌کند.

/// note | جزئیات فنی

در مشخصات OpenAPI به آن <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object" class="external-link" target="_blank">شیء عملیات</a> گفته می‌شود.

///

تمام اطلاعات درباره *عملیات مسیر* را دارد و برای تولید مستندات خودکار استفاده می‌شود.

شامل `tags`، `parameters`، `requestBody`، `responses` و غیره می‌شود.

این شمای OpenAPI خاص *عملیات مسیر* معمولاً توسط **FastAPI** به طور خودکار تولید می‌شود، اما همچنین می‌توانید آن را گسترش دهید.

/// tip

این یک نقطه گسترش سطح پایین است.

اگر فقط نیاز به اعلام پاسخ‌های اضافی دارید، راه راحت‌تر انجام آن با [پاسخ‌های اضافی در OpenAPI](additional-responses.md){.internal-link target=_blank} است.

///

می‌توانید شمای OpenAPI را برای یک *عملیات مسیر* با استفاده از پارامتر `openapi_extra` گسترش دهید.

### افزونه‌های OpenAPI

این `openapi_extra` می‌تواند مفید باشد، برای مثال، برای اعلام [افزونه‌های OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#specificationExtensions):

{* ../../docs_src/path_operation_advanced_configuration/tutorial005.py hl[6] *}

اگر مستندات خودکار API را باز کنید، افزونه شما در پایین *عملیات مسیر* خاص نمایش داده خواهد شد.

<img src="/img/tutorial/path-operation-advanced-configuration/image01.png">

و اگر OpenAPI حاصل (در `/openapi.json` در API شما) را ببینید، افزونه خود را به عنوان بخشی از *عملیات مسیر* خاص خواهید دید:

```JSON hl_lines="22"
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "summary": "Read Items",
                "operationId": "read_items_items__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                },
                "x-aperture-labs-portal": "blue"
            }
        }
    }
}
```

### شمای سفارشی *عملیات مسیر* OpenAPI

دیکشنری در `openapi_extra` به صورت عمیق با شمای OpenAPI تولید شده خودکار برای *عملیات مسیر* ادغام خواهد شد.

بنابراین، می‌توانید داده‌های اضافی به شمای تولید شده خودکار اضافه کنید.

برای مثال، می‌توانید تصمیم بگیرید درخواست را با کد خودتان بخوانید و اعتبارسنجی کنید، بدون استفاده از ویژگی‌های خودکار FastAPI با Pydantic، اما همچنان بخواهید درخواست را در شمای OpenAPI تعریف کنید.

می‌توانید آن کار را با `openapi_extra` انجام دهید:

{* ../../docs_src/path_operation_advanced_configuration/tutorial006.py hl[19:36, 39:40] *}

در این مثال، هیچ مدل Pydantic اعلام نکردیم. در واقع، بدنه درخواست حتی به عنوان JSON <abbr title="تبدیل از برخی فرمت‌های ساده، مانند بایت، به اشیاء Python">تجزیه</abbr> نمی‌شود، مستقیماً به عنوان `bytes` خوانده می‌شود و تابع `magic_data_reader()` مسئول تجزیه آن به نحوی خواهد بود.

با این حال، می‌توانیم شمای مورد انتظار برای بدنه درخواست را اعلام کنیم.

### نوع محتوای سفارشی OpenAPI

با استفاده از همین ترفند، می‌توانید از مدل Pydantic برای تعریف شمای JSON استفاده کنید که سپس در بخش شمای سفارشی OpenAPI برای *عملیات مسیر* گنجانده می‌شود.

و می‌توانید این کار را حتی اگر نوع داده در درخواست JSON نباشد انجام دهید.

برای مثال، در این برنامه ما از عملکرد یکپارچه FastAPI برای استخراج شمای JSON از مدل‌های Pydantic و نه اعتبارسنجی خودکار برای JSON استفاده نمی‌کنیم. در واقع، نوع محتوای درخواست را YAML اعلام می‌کنیم، نه JSON:

//// tab | Pydantic v2

{* ../../docs_src/path_operation_advanced_configuration/tutorial007.py hl[17:22, 24] *}

////

//// tab | Pydantic v1

{* ../../docs_src/path_operation_advanced_configuration/tutorial007_pv1.py hl[17:22, 24] *}

////

/// info

در Pydantic نسخه 1 متد برای دریافت شمای JSON یک مدل `Item.schema()` نامیده می‌شد، در Pydantic نسخه 2 متد `Item.model_json_schema()` نامیده می‌شود.

///

با این حال، اگرچه از عملکرد یکپارچه پیش‌فرض استفاده نمی‌کنیم، همچنان از مدل Pydantic برای تولید دستی شمای JSON برای داده‌ای که می‌خواهیم در YAML دریافت کنیم استفاده می‌کنیم.

سپس درخواست را مستقیماً استفاده می‌کنیم و بدنه را به عنوان `bytes` استخراج می‌کنیم. این بدان معناست که FastAPI حتی سعی نخواهد کرد محتوای درخواست را به عنوان JSON تجزیه کند.

و سپس در کد خود، آن محتوای YAML را مستقیماً تجزیه می‌کنیم و دوباره از همان مدل Pydantic برای اعتبارسنجی محتوای YAML استفاده می‌کنیم:

//// tab | Pydantic v2

{* ../../docs_src/path_operation_advanced_configuration/tutorial007.py hl[26:33] *}

////

//// tab | Pydantic v1

{* ../../docs_src/path_operation_advanced_configuration/tutorial007_pv1.py hl[26:33] *}

////

/// info

در Pydantic نسخه 1 متد برای تجزیه و اعتبارسنجی یک شیء `Item.parse_obj()` بود، در Pydantic نسخه 2 متد `Item.model_validate()` نامیده می‌شود.

///

/// tip

اینجا همان مدل Pydantic را مجدداً استفاده می‌کنیم.

اما به همان ترتیب، می‌توانستیم آن را به نحو دیگری اعتبارسنجی کنیم.

///
