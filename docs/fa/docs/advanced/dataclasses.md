# استفاده از Dataclasses

FastAPI بر روی **Pydantic** ساخته شده است و من به شما نشان داده‌ام که چگونه از مدل‌های Pydantic برای تعریف درخواست‌ها و پاسخ‌ها استفاده کنید.

اما FastAPI همچنین از استفاده <a href="https://docs.python.org/3/library/dataclasses.html" class="external-link" target="_blank">`dataclasses`</a> به همان روش پشتیبانی می‌کند:

{* ../../docs_src/dataclasses/tutorial001.py hl[1,7:12,19:20] *}

این همچنان به لطف **Pydantic** پشتیبانی می‌شود، زیرا <a href="https://docs.pydantic.dev/latest/concepts/dataclasses/#use-of-stdlib-dataclasses-with-basemodel" class="external-link" target="_blank">پشتیبانی داخلی از `dataclasses`</a> دارد.

بنابراین، حتی با کد بالا که به صراحت از Pydantic استفاده نمی‌کند، FastAPI از Pydantic برای تبدیل آن dataclassهای استاندارد به نسخه خود Pydantic از dataclasses استفاده می‌کند.

و البته، همان موارد را پشتیبانی می‌کند:

* اعتبارسنجی داده‌ها
* سریال‌سازی داده‌ها
* مستندسازی داده‌ها و غیره.

این به همان روش مدل‌های Pydantic کار می‌کند. و در واقع در زیر به همان روش و با استفاده از Pydantic انجام می‌شود.

/// info

به خاطر داشته باشید که dataclasses نمی‌توانند همه کارهایی که مدل‌های Pydantic انجام می‌دهند را انجام دهند.

بنابراین، ممکن است همچنان نیاز به استفاده از مدل‌های Pydantic داشته باشید.

اما اگر تعداد زیادی dataclass دارید، این یک ترفند خوب برای استفاده از آنها برای تغذیه یک API وب با استفاده از FastAPI است. 🤓

///

## Dataclasses در `response_model`

همچنین می‌توانید از `dataclasses` در پارامتر `response_model` استفاده کنید:

{* ../../docs_src/dataclasses/tutorial002.py hl[1,7:13,19] *}

dataclass به طور خودکار به یک Pydantic dataclass تبدیل خواهد شد.

به این ترتیب، شمای آن در رابط مستندات API نمایش داده خواهد شد:

<img src="/img/tutorial/dataclasses/image01.png">

## Dataclasses در ساختارهای داده تودرتو

همچنین می‌توانید `dataclasses` را با سایر حاشیه‌نویسی‌های تایپ ترکیب کنید تا ساختارهای داده تودرتو بسازید.

در برخی موارد، ممکن است همچنان نیاز به استفاده از نسخه Pydantic از `dataclasses` داشته باشید. برای مثال، اگر خطاهایی با مستندات API تولید شده خودکار دارید.

در آن صورت، می‌توانید به سادگی `dataclasses` استاندارد را با `pydantic.dataclasses` جایگزین کنید، که یک جایگزین مستقیم است:

{* ../../docs_src/dataclasses/tutorial003.py hl[1,5,8:11,14:17,23:25,28] *}

1. ما همچنان `field` را از `dataclasses` استاندارد وارد می‌کنیم.

2. `pydantic.dataclasses` یک جایگزین مستقیم برای `dataclasses` است.

3. dataclass `Author` شامل لیستی از dataclassهای `Item` است.

4. dataclass `Author` به عنوان پارامتر `response_model` استفاده می‌شود.

5. می‌توانید از سایر حاشیه‌نویسی‌های تایپ استاندارد با dataclasses به عنوان بدنه درخواست استفاده کنید.

    در این مورد، لیستی از dataclassهای `Item` است.

6. در اینجا یک دیکشنری برمی‌گردانیم که شامل `items` است که لیستی از dataclasses است.

    FastAPI همچنان قادر به <abbr title="تبدیل داده‌ها به فرمتی که قابل انتقال باشد">سریال‌سازی</abbr> داده‌ها به JSON است.

7. در اینجا `response_model` از حاشیه‌نویسی تایپ لیست dataclassهای `Author` استفاده می‌کند.

    مجدداً، می‌توانید `dataclasses` را با حاشیه‌نویسی‌های تایپ استاندارد ترکیب کنید.

8. توجه کنید که این *تابع عملیات مسیر* از `def` معمولی به جای `async def` استفاده می‌کند.

    مثل همیشه، در FastAPI می‌توانید `def` و `async def` را بر حسب نیاز ترکیب کنید.

    اگر نیاز به یادآوری درباره اینکه چه زمانی از کدام استفاده کنید دارید، بخش _"عجله دارید?"_ در مستندات [`async` و `await`](../async.md#in-a-hurry){.internal-link target=_blank} را بررسی کنید.

9. این *تابع عملیات مسیر* dataclasses را برنمی‌گرداند (اگرچه می‌تواند)، بلکه لیستی از دیکشنری‌ها با داده‌های داخلی برمی‌گرداند.

    FastAPI از پارامتر `response_model` (که شامل dataclasses است) برای تبدیل پاسخ استفاده خواهد کرد.

می‌توانید `dataclasses` را با سایر حاشیه‌نویسی‌های تایپ در ترکیب‌های مختلف زیادی برای تشکیل ساختارهای داده پیچیده ترکیب کنید.

برای مشاهده جزئیات خاص بیشتر، نکات حاشیه‌نویسی درون کد بالا را بررسی کنید.

## بیشتر بیاموزید

همچنین می‌توانید `dataclasses` را با سایر مدل‌های Pydantic ترکیب کنید، از آنها ارث‌بری کنید، آنها را در مدل‌های خود بگنجانید و غیره.

برای اطلاعات بیشتر، <a href="https://docs.pydantic.dev/latest/concepts/dataclasses/" class="external-link" target="_blank">مستندات Pydantic درباره dataclasses</a> را بررسی کنید.

## نسخه

این از نسخه `0.67.0` FastAPI در دسترس است. 🔖
