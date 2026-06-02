# Koşullu OpenAPI

Gerekirse, ortama bağlı olarak OpenAPI'yi koşullu olarak yapılandırmak ve hatta tamamen devre dışı bırakmak için ayarları ve ortam değişkenlerini kullanabilirsiniz.

## Güvenlik, API'ler ve belgeler hakkında

Üretimde belge kullanıcı arayüzlerinizi gizlemek, API'nizi korumanın yolu *olmamalıdır*.

Bu, API'nize herhangi bir ekstra güvenlik eklemez, *yol operasyonları* hala bulundukları yerde mevcut olacaktır.

Kodunuzda bir güvenlik açığı varsa, hala var olmaya devam edecektir.

Belgeleri gizlemek yalnızca API'nizle nasıl etkileşim kurulacağını anlamayı zorlaştırır ve üretimde hata ayıklamanızı zorlaştırabilir. Bu basitçe bir tür <a href="https://en.wikipedia.org/wiki/Security_through_obscurity" class="external-link" target="_blank">Gizlilik Yoluyla Güvenlik</a> olarak kabul edilebilir.

API'nizi güvence altına almak istiyorsanız, yapabileceğiniz birkaç daha iyi şey vardır, örneğin:

* İstek gövdeleri ve yanıtlar için iyi tanımlanmış Pydantic modelleriniz olduğundan emin olun.
* Bağımlılıkları kullanarak gerekli izinleri ve rolleri yapılandırın.
* Asla düz metin şifreleri saklamayın, yalnızca şifre hash'lerini saklayın.
* Passlib ve JWT token'ları gibi iyi bilinen kriptografik araçları uygulayın ve kullanın.
* Gerektiğinde OAuth2 kapsamlarıyla daha ayrıntılı izin kontrolleri ekleyin.
* ...vb.

Yine de, belirli bir ortam için (örn. üretim için) API belgelerini gerçekten devre dışı bırakmanız veya ortam değişkenlerinden gelen yapılandırmalara bağlı olarak bunu yapmanız gereken çok spesifik bir kullanım durumunuz olabilir.

## Ayarlardan ve ortam değişkenlerinden koşullu OpenAPI

Oluşturulan OpenAPI'nizi ve belge arayüzlerinizi yapılandırmak için aynı Pydantic ayarlarını kolayca kullanabilirsiniz.

Örneğin:

{* ../../docs_src/conditional_openapi/tutorial001.py hl[6,11] *}

Burada `openapi_url` ayarını aynı `"/openapi.json"` varsayılanıyla tanımlıyoruz.

Ve ardından `FastAPI` uygulamasını oluştururken kullanıyoruz.

Daha sonra `OPENAPI_URL` ortam değişkenini boş dizeye ayarlayarak OpenAPI'yi (belge arayüzleri dahil) devre dışı bırakabilirsiniz, örneğin:

<div class="termy">

```console
$ OPENAPI_URL= uvicorn main:app

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Ardından `/openapi.json`, `/docs` veya `/redoc` URL'lerine giderseniz, şöyle bir `404 Not Found` hatası alırsınız:

```JSON
{
    "detail": "Not Found"
}
```
