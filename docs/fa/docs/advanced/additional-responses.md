# پاسخ‌های اضافی در OpenAPI

/// warning

این یک موضوع نسبتاً پیشرفته است.

اگر تازه با **FastAPI** شروع کرده‌اید، ممکن است به آن نیاز نداشته باشید.

///

می‌توانید پاسخ‌های اضافی با کدهای وضعیت، تایپ‌های رسانه، توضیحات و غیره اعلان کنید.

آن پاسخ‌های اضافی در اسکیمای OpenAPI گنجانده خواهند شد، بنابراین در مستندات API نیز ظاهر خواهند شد.

اما برای آن پاسخ‌های اضافی باید مطمئن شوید که مستقیماً یک `Response` مانند `JSONResponse` با کد وضعیت و محتوای خود برگردانید.

## پاسخ اضافی با `model`

می‌توانید پارامتر `responses` را به *دکوراتورهای عملیات مسیر* ارسال کنید.

این یک `dict` دریافت می‌کند: کلیدها کدهای وضعیت برای هر پاسخ هستند (مانند `200`)، و مقادیر `dict`های دیگری با اطلاعات هر کدام هستند.

هر یک از آن `dict`های پاسخ می‌تواند کلید `model` داشته باشد که شامل مدل Pydantic است، دقیقاً مانند `response_model`.

**FastAPI** آن مدل را خواهد گرفت، JSON Schema آن را تولید و در مکان صحیح OpenAPI قرار خواهد داد.

برای مثال، برای اعلان پاسخ دیگری با کد وضعیت `404` و مدل Pydantic به نام `Message`، می‌توانید بنویسید:

{* ../../docs_src/additional_responses/tutorial001.py hl[18,22] *}

/// note

به خاطر داشته باشید که باید `JSONResponse` را مستقیماً برگردانید.

///

/// info

کلید `model` بخشی از OpenAPI نیست.

**FastAPI** مدل Pydantic را از آنجا خواهد گرفت، JSON Schema را تولید و در مکان صحیح قرار خواهد داد.

مکان صحیح عبارت است از:

* در کلید `content`، که مقدارش شیء JSON دیگری (`dict`) است که شامل:
    * کلیدی با تایپ رسانه مثلاً `application/json`، که مقدارش شیء JSON دیگری است که شامل:
        * کلید `schema`، که مقدارش JSON Schema مدل است، اینجا مکان صحیح است.
            * **FastAPI** یک ارجاع به JSON Schemaهای سراسری در مکان دیگری از OpenAPI اضافه می‌کند به جای اینکه مستقیماً آن را درج کند. به این ترتیب، برنامه‌ها و کلاینت‌های دیگر می‌توانند مستقیماً از آن JSON Schemaها استفاده کنند، ابزارهای تولید کد بهتری ارائه دهند و غیره.

///

پاسخ‌های تولید شده در OpenAPI برای این *عملیات مسیر* خواهند بود:

```JSON hl_lines="3-12"
{
    "responses": {
        "404": {
            "description": "Additional Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/Message"
                    }
                }
            }
        },
        "200": {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/Item"
                    }
                }
            }
        },
        "422": {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/HTTPValidationError"
                    }
                }
            }
        }
    }
}
```

اسکیماها در مکان دیگری درون اسکیمای OpenAPI ارجاع داده شده‌اند:

```JSON hl_lines="4-16"
{
    "components": {
        "schemas": {
            "Message": {
                "title": "Message",
                "required": [
                    "message"
                ],
                "type": "object",
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string"
                    }
                }
            },
            "Item": {
                "title": "Item",
                "required": [
                    "id",
                    "value"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "string"
                    },
                    "value": {
                        "title": "Value",
                        "type": "string"
                    }
                }
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "msg": {
                        "title": "Message",
                        "type": "string"
                    },
                    "type": {
                        "title": "Error Type",
                        "type": "string"
                    }
                }
            },
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        }
                    }
                }
            }
        }
    }
}
```

## تایپ‌های رسانه اضافی برای پاسخ اصلی

می‌توانید از همین پارامتر `responses` برای اضافه کردن تایپ‌های رسانه مختلف برای همان پاسخ اصلی استفاده کنید.

برای مثال، می‌توانید تایپ رسانه اضافی `image/png` اضافه کنید و اعلان کنید که *عملیات مسیر* شما می‌تواند یک شیء JSON (با تایپ رسانه `application/json`) یا یک تصویر PNG برگرداند:

{* ../../docs_src/additional_responses/tutorial002.py hl[19:24,28] *}

/// note

توجه کنید که باید تصویر را مستقیماً با استفاده از `FileResponse` برگردانید.

///

/// info

مگر اینکه صریحاً تایپ رسانه متفاوتی در پارامتر `responses` خود مشخص کنید، FastAPI فرض خواهد کرد پاسخ همان تایپ رسانه کلاس پاسخ اصلی را دارد (پیش‌فرض `application/json`).

اما اگر کلاس پاسخ سفارشی با `None` به عنوان تایپ رسانه مشخص کرده باشید، FastAPI از `application/json` برای هر پاسخ اضافی‌ای که مدل مرتبط دارد استفاده خواهد کرد.

///

## ترکیب اطلاعات

همچنین می‌توانید اطلاعات پاسخ از مکان‌های مختلف ترکیب کنید، از جمله پارامترهای `response_model`، `status_code` و `responses`.

می‌توانید یک `response_model` اعلان کنید، با استفاده از کد وضعیت پیش‌فرض `200` (یا یک مورد سفارشی در صورت نیاز)، و سپس اطلاعات اضافی برای همان پاسخ را در `responses`، مستقیماً در اسکیمای OpenAPI اعلان کنید.

**FastAPI** اطلاعات اضافی از `responses` را نگه خواهد داشت و آن را با JSON Schema مدل شما ترکیب خواهد کرد.

برای مثال، می‌توانید پاسخی با کد وضعیت `404` که از مدل Pydantic استفاده می‌کند و `description` سفارشی دارد اعلان کنید.

و پاسخی با کد وضعیت `200` که از `response_model` شما استفاده می‌کند، اما شامل یک `example` سفارشی است:

{* ../../docs_src/additional_responses/tutorial003.py hl[20:31] *}

همه اینها ترکیب شده و در OpenAPI شما گنجانده خواهند شد و در مستندات API نمایش داده خواهند شد:

<img src="/img/tutorial/additional-responses/image01.png">

## ترکیب پاسخ‌های از پیش تعریف شده و سفارشی

ممکن است بخواهید پاسخ‌های از پیش تعریف شده‌ای داشته باشید که برای بسیاری از *عملیات‌های مسیر* اعمال شوند، اما بخواهید آنها را با پاسخ‌های سفارشی مورد نیاز هر *عملیات مسیر* ترکیب کنید.

برای آن موارد، می‌توانید از تکنیک پایتون "باز کردن" یک `dict` با `**dict_to_unpack` استفاده کنید:

```Python
old_dict = {
    "old key": "old value",
    "second old key": "second old value",
}
new_dict = {**old_dict, "new key": "new value"}
```

اینجا، `new_dict` شامل تمام جفت کلید-مقدارهای `old_dict` به اضافه جفت کلید-مقدار جدید خواهد بود:

```Python
{
    "old key": "old value",
    "second old key": "second old value",
    "new key": "new value",
}
```

می‌توانید از این تکنیک برای استفاده مجدد از پاسخ‌های از پیش تعریف شده در *عملیات‌های مسیر* خود و ترکیب آنها با موارد سفارشی اضافی استفاده کنید.

برای مثال:

{* ../../docs_src/additional_responses/tutorial004.py hl[13:17,26] *}

## اطلاعات بیشتر درباره پاسخ‌های OpenAPI

برای دیدن اینکه دقیقاً چه چیزی می‌توانید در پاسخ‌ها بگنجانید، می‌توانید این بخش‌ها را در مشخصه OpenAPI بررسی کنید:

* <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#responses-object" class="external-link" target="_blank">شیء پاسخ‌های OpenAPI</a>، شامل `Response Object` است.
* <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#response-object" class="external-link" target="_blank">شیء پاسخ OpenAPI</a>، می‌توانید هر چیزی از این را مستقیماً در هر پاسخ درون پارامتر `responses` خود بگنجانید. از جمله `description`، `headers`، `content` (درون آن است که تایپ‌های رسانه مختلف و JSON Schemaها را اعلان می‌کنید) و `links`.
