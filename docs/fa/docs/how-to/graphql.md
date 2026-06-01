# GraphQL

از آنجا که **FastAPI** بر اساس استاندارد **ASGI** ساخته شده است، یکپارچه‌سازی هر کتابخانه **GraphQL** که با ASGI سازگار باشد بسیار آسان است.

می‌توانید *عملیات‌های مسیر* عادی FastAPI را با GraphQL در یک برنامه ترکیب کنید.

/// tip

**GraphQL** برخی موارد استفاده بسیار خاص را حل می‌کند.

در مقایسه با **APIهای وب** رایج، **مزایا** و **معایبی** دارد.

مطمئن شوید که ارزیابی کنید آیا **فواید** برای مورد استفاده شما **معایب** را جبران می‌کند. 🤓

///

## کتابخانه‌های GraphQL

در اینجا برخی از کتابخانه‌های **GraphQL** که پشتیبانی **ASGI** دارند آمده است. می‌توانید از آنها با **FastAPI** استفاده کنید:

* <a href="https://strawberry.rocks/" class="external-link" target="_blank">Strawberry</a> 🍓
    * با <a href="https://strawberry.rocks/docs/integrations/fastapi" class="external-link" target="_blank">مستندات برای FastAPI</a>
* <a href="https://ariadnegraphql.org/" class="external-link" target="_blank">Ariadne</a>
    * با <a href="https://ariadnegraphql.org/docs/fastapi-integration" class="external-link" target="_blank">مستندات برای FastAPI</a>
* <a href="https://tartiflette.io/" class="external-link" target="_blank">Tartiflette</a>
    * با <a href="https://tartiflette.github.io/tartiflette-asgi/" class="external-link" target="_blank">Tartiflette ASGI</a> برای ارائه یکپارچه‌سازی ASGI
* <a href="https://graphene-python.org/" class="external-link" target="_blank">Graphene</a>
    * با <a href="https://github.com/ciscorn/starlette-graphene3" class="external-link" target="_blank">starlette-graphene3</a>

## GraphQL با Strawberry

اگر نیاز دارید یا می‌خواهید با **GraphQL** کار کنید، <a href="https://strawberry.rocks/" class="external-link" target="_blank">**Strawberry**</a> کتابخانه **توصیه شده** است زیرا طراحی آن نزدیک‌ترین به طراحی **FastAPI** است و همه بر اساس **حاشیه‌نویسی تایپ** هستند.

بسته به مورد استفاده شما، ممکن است ترجیح دهید از کتابخانه دیگری استفاده کنید، اما اگر از من بپرسید، احتمالاً پیشنهاد می‌کنم **Strawberry** را امتحان کنید.

در اینجا پیش‌نمایش کوچکی از نحوه یکپارچه‌سازی Strawberry با FastAPI آمده است:

{* ../../docs_src/graphql/tutorial001.py hl[3,22,25] *}

می‌توانید در <a href="https://strawberry.rocks/" class="external-link" target="_blank">مستندات Strawberry</a> بیشتر بیاموزید.

و همچنین مستندات درباره <a href="https://strawberry.rocks/docs/integrations/fastapi" class="external-link" target="_blank">Strawberry با FastAPI</a>.

## `GraphQLApp` قدیمی از Starlette

نسخه‌های قبلی Starlette شامل یک کلاس `GraphQLApp` برای یکپارچه‌سازی با <a href="https://graphene-python.org/" class="external-link" target="_blank">Graphene</a> بودند.

از Starlette منسوخ شده است، اما اگر کدی دارید که از آن استفاده می‌کرده، می‌توانید به راحتی به <a href="https://github.com/ciscorn/starlette-graphene3" class="external-link" target="_blank">starlette-graphene3</a> مهاجرت کنید که همان مورد استفاده را پوشش می‌دهد و رابط تقریباً یکسانی دارد.

/// tip

اگر نیاز به GraphQL دارید، همچنان توصیه می‌کنم <a href="https://strawberry.rocks/" class="external-link" target="_blank">Strawberry</a> را بررسی کنید، زیرا بر اساس حاشیه‌نویسی تایپ به جای کلاس‌ها و تایپ‌های سفارشی ساخته شده است.

///

## بیشتر بیاموزید

می‌توانید درباره **GraphQL** در <a href="https://graphql.org/" class="external-link" target="_blank">مستندات رسمی GraphQL</a> بیشتر بیاموزید.

همچنین می‌توانید درباره هر یک از کتابخانه‌های توضیح داده شده در بالا در لینک‌های آنها بیشتر بخوانید.
