# OpenAPI Webhook'ları

Bazı durumlarda API **kullanıcılarınıza** uygulamanızın onların uygulamasını çağırabileceğini (bir istek göndererek) bazı verilerle, normalde bir tür **olayı** **bildirmek** için söylemek isteyebilirsiniz.

Bu, kullanıcılarınızın API'nize istek gönderme normal sürecinin yerine, **sizin API'nizin** (veya uygulamanızın) **onların sistemine** (onların API'sine, onların uygulamasına) **istek gönderebileceği** anlamına gelir.

Bu normalde **webhook** olarak adlandırılır.

## Webhook adımları

Süreç normalde şöyledir: kodunuzda göndereceğiniz mesajın ne olduğunu, **isteğin gövdesini** **tanımlarsınız**.

Ayrıca uygulamanızın bu istekleri veya olayları göndereceği **anları** bir şekilde tanımlarsınız.

Ve **kullanıcılarınız**, uygulamanızın bu istekleri göndermesi gereken **URL'yi** bir şekilde (örneğin bir web panelinde) tanımlar.

Webhook'lar için URL'leri kaydetmenin tüm **mantığı** ve bu istekleri gerçekten gönderecek kod size bağlıdır. Bunu **kendi kodunuzda** istediğiniz şekilde yazarsınız.

## **FastAPI** ve OpenAPI ile webhook'ları belgeleme

**FastAPI** ile OpenAPI kullanarak, bu webhook'ların adlarını, uygulamanızın gönderebileceği HTTP operasyon tiplerini (ör. `POST`, `PUT`, vb.) ve uygulamanızın göndereceği istek **gövdelerini** tanımlayabilirsiniz.

Bu, kullanıcılarınızın **webhook** isteklerinizi alacak **kendi API'lerini uygulamasını** çok daha kolay hale getirebilir, hatta kendi API kodlarının bir kısmını otomatik olarak oluşturabilirler bile.

/// info

Webhook'lar OpenAPI 3.1.0 ve üstünde mevcuttur, FastAPI `0.99.0` ve üstü tarafından desteklenir.

///

## Webhook'lu bir uygulama

Bir **FastAPI** uygulaması oluşturduğunuzda, *yol operasyonlarını* tanımladığınız gibi *webhook'ları* tanımlamak için kullanabileceğiniz bir `webhooks` niteliği vardır, örneğin `@app.webhooks.post()` ile.

{* ../../docs_src/openapi_webhooks/tutorial001.py hl[9:13,36:53] *}

Tanımladığınız webhook'lar **OpenAPI** şemasında ve otomatik **belge arayüzünde** görünecektir.

/// info

`app.webhooks` nesnesi aslında sadece bir `APIRouter`'dır, uygulamanızı birden fazla dosyayla yapılandırırken kullanacağınız türle aynıdır.

///

Webhook'larla aslında bir *yol* bildirmediğinize (`/items/` gibi) dikkat edin, orada ilettiğiniz metin sadece webhook'un bir **tanımlayıcısıdır** (olayın adı), örneğin `@app.webhooks.post("new-subscription")`'da webhook adı `new-subscription`'dır.

Bunun nedeni, **kullanıcılarınızın** webhook isteğini almak istedikleri gerçek **URL yolunu** başka bir şekilde (ör. bir web panelinde) tanımlamasının beklenmesidir.

### Belgelere bakın

Şimdi uygulamanızı başlatabilir ve <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> adresine gidebilirsiniz.

Belgelerinizin normal *yol operasyonlarına* ve ayrıca bazı **webhook'lara** sahip olduğunu göreceksiniz:

<img src="/img/tutorial/openapi-webhooks/image01.png">
