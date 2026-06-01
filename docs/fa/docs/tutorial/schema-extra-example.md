# اعلان داده‌های نمونه درخواست

می‌توانید نمونه‌هایی از داده‌هایی که برنامه شما می‌تواند دریافت کند را اعلان کنید.

در اینجا چندین راه برای انجام آن آمده.

## داده‌های اضافی JSON Schema در مدل‌های Pydantic

می‌توانید `examples` را برای یک مدل Pydantic اعلان کنید که به JSON Schema تولید شده اضافه خواهد شد.

//// tab | Pydantic v2

{* ../../docs_src/schema_extra_example/tutorial001_py310.py hl[13:24] *}

////

//// tab | Pydantic v1

{* ../../docs_src/schema_extra_example/tutorial001_pv1_py310.py hl[13:23] *}

////

آن اطلاعات اضافی به همان شکل به **JSON Schema** خروجی آن مدل اضافه خواهد شد و در مستندات API استفاده خواهد شد.

//// tab | Pydantic v2

در نسخه 2 Pydantic، از ویژگی `model_config` استفاده می‌کنید، که یک `dict` می‌گیرد همانطور که در <a href="https://docs.pydantic.dev/latest/api/config/" class="external-link" target="_blank">مستندات Pydantic: پیکربندی</a> توضیح داده شده.

می‌توانید `"json_schema_extra"` را با یک `dict` شامل هر داده اضافی‌ای که می‌خواهید در JSON Schema تولید شده نمایش داده شود تنظیم کنید، از جمله `examples`.

////

//// tab | Pydantic v1

در نسخه 1 Pydantic، از یک کلاس داخلی `Config` و `schema_extra` استفاده می‌کنید، همانطور که در <a href="https://docs.pydantic.dev/1.10/usage/schema/#schema-customization" class="external-link" target="_blank">مستندات Pydantic: سفارشی‌سازی Schema</a> توضیح داده شده.

می‌توانید `schema_extra` را با یک `dict` شامل هر داده اضافی‌ای که می‌خواهید در JSON Schema تولید شده نمایش داده شود تنظیم کنید، از جمله `examples`.

////

/// tip

می‌توانید از همین تکنیک برای گسترش JSON Schema و اضافه کردن اطلاعات اضافی سفارشی خود استفاده کنید.

برای مثال می‌توانید از آن برای اضافه کردن متاداده برای رابط کاربری فرانت‌اند و غیره استفاده کنید.

///

/// info

OpenAPI 3.1.0 (که از FastAPI 0.99.0 استفاده می‌شود) پشتیبانی از `examples` را اضافه کرد، که بخشی از استاندارد **JSON Schema** است.

قبل از آن، فقط از کلمه کلیدی `example` با یک نمونه تکی پشتیبانی می‌کرد. آن همچنان توسط OpenAPI 3.1.0 پشتیبانی می‌شود، اما منسوخ شده و بخشی از استاندارد JSON Schema نیست. بنابراین تشویق می‌شوید `example` را به `examples` مهاجرت دهید. 🤓

می‌توانید بیشتر در انتهای این صفحه بخوانید.

///

## آرگومان‌های اضافی `Field`

هنگام استفاده از `Field()` با مدل‌های Pydantic، همچنین می‌توانید `examples` اضافی اعلان کنید:

{* ../../docs_src/schema_extra_example/tutorial002_py310.py hl[2,8:11] *}

## `examples` در JSON Schema - OpenAPI

هنگام استفاده از هر یک از:

* `Path()`
* `Query()`
* `Header()`
* `Cookie()`
* `Body()`
* `Form()`
* `File()`

همچنین می‌توانید گروهی از `examples` با اطلاعات اضافی اعلان کنید که به **JSON Schemaهای** آنها درون **OpenAPI** اضافه خواهد شد.

### `Body` با `examples`

اینجا `examples` شامل یک نمونه از داده‌های مورد انتظار در `Body()` ارسال می‌کنیم:

{* ../../docs_src/schema_extra_example/tutorial003_an_py310.py hl[22:29] *}

### نمونه در رابط کاربری مستندات

با هر یک از روش‌های بالا به این شکل در `/docs` نمایش داده خواهد شد:

<img src="/img/tutorial/body-fields/image01.png">

### `Body` با چندین `examples`

البته همچنین می‌توانید چندین `examples` ارسال کنید:

{* ../../docs_src/schema_extra_example/tutorial004_an_py310.py hl[23:38] *}

وقتی این کار را انجام می‌دهید، نمونه‌ها بخشی از **JSON Schema** داخلی برای آن داده بدنه خواهند بود.

با این حال، در <abbr title="2023-08-26">زمان نگارش این مطلب</abbr>، Swagger UI، ابزار مسئول نمایش رابط کاربری مستندات، از نمایش چندین نمونه برای داده‌ها در **JSON Schema** پشتیبانی نمی‌کند. اما برای راه‌حل جایگزین ادامه بخوانید.

### `examples` مختص OpenAPI

از قبل از اینکه **JSON Schema** از `examples` پشتیبانی کند، OpenAPI پشتیبانی از فیلد متفاوتی به نام `examples` داشت.

این `examples` **مختص OpenAPI** در بخش دیگری از مشخصه OpenAPI قرار می‌گیرد. در **جزئیات هر *عملیات مسیر*** قرار می‌گیرد، نه درون هر JSON Schema.

و Swagger UI مدتی است که از این فیلد `examples` خاص پشتیبانی می‌کند. بنابراین، می‌توانید از آن برای **نمایش** **نمونه‌های** مختلف در **رابط کاربری مستندات** استفاده کنید.

شکل این فیلد `examples` مختص OpenAPI یک `dict` با **چندین نمونه** (به جای `list`) است، هر کدام با اطلاعات اضافی‌ای که به **OpenAPI** نیز اضافه خواهد شد.

این درون هر JSON Schema موجود در OpenAPI نمی‌رود، بلکه بیرون از آن، مستقیماً در *عملیات مسیر* قرار می‌گیرد.

### استفاده از پارامتر `openapi_examples`

می‌توانید `examples` مختص OpenAPI را در FastAPI با پارامتر `openapi_examples` برای موارد زیر اعلان کنید:

* `Path()`
* `Query()`
* `Header()`
* `Cookie()`
* `Body()`
* `Form()`
* `File()`

کلیدهای `dict` هر نمونه را شناسایی می‌کنند و هر مقدار یک `dict` دیگر است.

هر `dict` نمونه خاص در `examples` می‌تواند شامل موارد زیر باشد:

* `summary`: توضیحات کوتاه برای نمونه.
* `description`: توضیحات بلند که می‌تواند شامل متن Markdown باشد.
* `value`: نمونه واقعی نمایش داده شده، مثلاً یک `dict`.
* `externalValue`: جایگزین `value`، یک URL اشاره‌کننده به نمونه. اگرچه ممکن است توسط ابزارهای کمتری نسبت به `value` پشتیبانی شود.

می‌توانید آن را اینطور استفاده کنید:

{* ../../docs_src/schema_extra_example/tutorial005_an_py310.py hl[23:49] *}

### نمونه‌های OpenAPI در رابط کاربری مستندات

با اضافه شدن `openapi_examples` به `Body()`، `/docs` به این شکل خواهد بود:

<img src="/img/tutorial/body-fields/image02.png">

## جزئیات فنی

/// tip

اگر از **FastAPI** نسخه **0.99.0 یا بالاتر** استفاده می‌کنید، احتمالاً می‌توانید این جزئیات را **رد** کنید.

آنها بیشتر مربوط به نسخه‌های قدیمی‌تر هستند، قبل از اینکه OpenAPI 3.1.0 در دسترس باشد.

می‌توانید این را یک **درس تاریخ** کوتاه OpenAPI و JSON Schema در نظر بگیرید. 🤓

///

/// warning

اینها جزئیات بسیار فنی درباره استانداردهای **JSON Schema** و **OpenAPI** هستند.

اگر ایده‌های بالا قبلاً برای شما کار می‌کنند، ممکن است کافی باشد و احتمالاً به این جزئیات نیاز ندارید، خیالتان راحت باشد و رد شوید.

///

قبل از OpenAPI 3.1.0، OpenAPI از نسخه قدیمی‌تر و اصلاح شده **JSON Schema** استفاده می‌کرد.

JSON Schema فیلد `examples` نداشت، بنابراین OpenAPI فیلد `example` خاص خود را به نسخه اصلاح شده خود اضافه کرد.

OpenAPI همچنین فیلدهای `example` و `examples` را به بخش‌های دیگر مشخصه اضافه کرد:

* <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#parameter-object" class="external-link" target="_blank">`Parameter Object` (در مشخصه)</a> که توسط موارد زیر FastAPI استفاده می‌شد:
    * `Path()`
    * `Query()`
    * `Header()`
    * `Cookie()`
* <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#media-type-object" class="external-link" target="_blank">`Request Body Object`، در فیلد `content`، در `Media Type Object` (در مشخصه)</a> که توسط موارد زیر FastAPI استفاده می‌شد:
    * `Body()`
    * `File()`
    * `Form()`

/// info

این پارامتر `examples` مختص OpenAPI قدیمی اکنون `openapi_examples` در FastAPI `0.103.0` است.

///

### فیلد `examples` در JSON Schema

اما سپس JSON Schema فیلد <a href="https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.9.5" class="external-link" target="_blank">`examples`</a> را به نسخه جدید مشخصه اضافه کرد.

و سپس OpenAPI 3.1.0 جدید بر اساس آخرین نسخه (JSON Schema 2020-12) بود که این فیلد `examples` جدید را شامل می‌شد.

و اکنون این فیلد `examples` جدید بر فیلد قدیمی تکی (و سفارشی) `example` که اکنون منسوخ شده اولویت دارد.

این فیلد `examples` جدید در JSON Schema **فقط یک `list`** از نمونه‌هاست، نه یک dict با متاداده اضافی مانند مکان‌های دیگر در OpenAPI (که بالا توضیح داده شد).

/// info

حتی بعد از انتشار OpenAPI 3.1.0 با این ادغام جدید ساده‌تر با JSON Schema، برای مدتی، Swagger UI، ابزاری که مستندات خودکار را ارائه می‌دهد، از OpenAPI 3.1.0 پشتیبانی نمی‌کرد (از نسخه 5.0.0 پشتیبانی می‌کند 🎉).

به همین دلیل، نسخه‌های FastAPI قبل از 0.99.0 همچنان از نسخه‌های OpenAPI پایین‌تر از 3.1.0 استفاده می‌کردند.

///

### `examples` در Pydantic و FastAPI

وقتی `examples` را درون یک مدل Pydantic اضافه می‌کنید، با استفاده از `schema_extra` یا `Field(examples=["something"])`، آن نمونه به **JSON Schema** آن مدل Pydantic اضافه می‌شود.

و آن **JSON Schema** مدل Pydantic در **OpenAPI** API شما گنجانده شده و سپس در رابط کاربری مستندات استفاده می‌شود.

در نسخه‌های FastAPI قبل از 0.99.0 (0.99.0 و بالاتر از OpenAPI 3.1.0 جدیدتر استفاده می‌کنند) وقتی از `example` یا `examples` با سایر ابزارها (`Query()`، `Body()` و غیره) استفاده می‌کردید، آن نمونه‌ها به JSON Schema توصیف‌کننده آن داده اضافه نمی‌شدند (حتی به نسخه خاص OpenAPI از JSON Schema)، بلکه مستقیماً به اعلان *عملیات مسیر* در OpenAPI اضافه می‌شدند (خارج از بخش‌هایی از OpenAPI که از JSON Schema استفاده می‌کنند).

اما اکنون که FastAPI 0.99.0 و بالاتر از OpenAPI 3.1.0 استفاده می‌کند، که از JSON Schema 2020-12 استفاده می‌کند، و Swagger UI 5.0.0 و بالاتر، همه چیز سازگارتر است و نمونه‌ها در JSON Schema گنجانده شده‌اند.

### Swagger UI و `examples` مختص OpenAPI

اکنون، چون Swagger UI از چندین نمونه JSON Schema پشتیبانی نمی‌کرد (تا تاریخ 2023-08-26)، کاربران راهی برای نمایش چندین نمونه در مستندات نداشتند.

برای حل این مسئله، FastAPI `0.103.0` **پشتیبانی** از اعلان همان فیلد `examples` **مختص OpenAPI** قدیمی را با پارامتر جدید `openapi_examples` اضافه کرد. 🤓

### خلاصه

من عادت داشتم بگویم خیلی تاریخ دوست ندارم... و نگاه کنید الان دارم "درس‌های تاریخ فناوری" می‌دهم. 😅

در خلاصه، **به FastAPI 0.99.0 یا بالاتر ارتقا دهید**، و همه چیز بسیار **ساده‌تر، سازگارتر و بدیهی‌تر** است، و لازم نیست همه این جزئیات تاریخی را بدانید. 😎
