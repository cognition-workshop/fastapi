# Özel Belge Arayüzü Statik Dosyaları (Kendi Sunucunuzda Barındırma)

API belgeleri **Swagger UI** ve **ReDoc** kullanır ve bunların her birinin bazı JavaScript ve CSS dosyalarına ihtiyacı vardır.

Varsayılan olarak, bu dosyalar bir <abbr title="Content Delivery Network: Normalde birden fazla sunucudan oluşan, JavaScript ve CSS gibi statik dosyaları sunan bir hizmet. İstemciye en yakın sunucudan dosya sunarak performansı artırmak için yaygın olarak kullanılır.">CDN</abbr>'den sunulur.

Ama bunu özelleştirmek mümkündür, belirli bir CDN ayarlayabilir veya dosyaları kendiniz sunabilirsiniz.

## JavaScript ve CSS İçin Özel CDN

Farklı bir <abbr title="Content Delivery Network">CDN</abbr> kullanmak istediğinizi varsayalım, örneğin `https://unpkg.com/` kullanmak isteyebilirsiniz.

Bu, örneğin bazı URL'leri kısıtlayan bir ülkede yaşıyorsanız yararlı olabilir.

### Otomatik belgeleri devre dışı bırakma

İlk adım otomatik belgeleri devre dışı bırakmaktır, çünkü varsayılan olarak bunlar varsayılan CDN'yi kullanır.

Bunları devre dışı bırakmak için, `FastAPI` uygulamanızı oluştururken URL'lerini `None` olarak ayarlayın:

{* ../../docs_src/custom_docs_ui/tutorial001.py hl[8] *}

### Özel belgeleri dahil etme

Şimdi özel belgeler için *yol operasyonları* oluşturabilirsiniz.

FastAPI'nin belgeler için HTML sayfalarını oluşturan dahili fonksiyonlarını yeniden kullanabilir ve gerekli argümanları geçirebilirsiniz:

* `openapi_url`: Belgeler için HTML sayfasının API'nizin OpenAPI şemasını alabileceği URL. Burada `app.openapi_url` özniteliğini kullanabilirsiniz.
* `title`: API'nizin başlığı.
* `oauth2_redirect_url`: Varsayılanı kullanmak için burada `app.swagger_ui_oauth2_redirect_url` kullanabilirsiniz.
* `swagger_js_url`: Swagger UI belgeleriniz için HTML'in **JavaScript** dosyasını alabileceği URL. Bu, özel CDN URL'sidir.
* `swagger_css_url`: Swagger UI belgeleriniz için HTML'in **CSS** dosyasını alabileceği URL. Bu, özel CDN URL'sidir.

Ve ReDoc için benzer şekilde...

{* ../../docs_src/custom_docs_ui/tutorial001.py hl[2:6,11:19,22:24,27:33] *}

/// tip

`swagger_ui_redirect` için *yol operasyonu* OAuth2 kullandığınızda bir yardımcıdır.

API'nizi bir OAuth2 sağlayıcısıyla entegre ederseniz, kimlik doğrulaması yapabilir ve edindiğiniz kimlik bilgileriyle API belgelerine geri dönebilirsiniz. Ve gerçek OAuth2 kimlik doğrulamasını kullanarak onunla etkileşim kurabilirsiniz.

Swagger UI bunu arka planda sizin için yönetecektir, ama bu "yönlendirme" yardımcısına ihtiyacı vardır.

///

### Test etmek için bir *yol operasyonu* oluşturma

Şimdi, her şeyin çalıştığını test edebilmek için bir *yol operasyonu* oluşturun:

{* ../../docs_src/custom_docs_ui/tutorial001.py hl[36:38] *}

### Test edin

Şimdi, <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>'taki belgelerinize gidebilir ve sayfayı yeniden yükleyebilirsiniz, varlıkları yeni CDN'den yükleyecektir.

## JavaScript ve CSS'i Kendi Sunucunuzda Barındırma

JavaScript ve CSS'i kendi sunucunuzda barındırmak, örneğin uygulamanızın çevrimdışıyken, açık İnternet erişimi olmadan veya yerel bir ağda bile çalışmaya devam etmesini istiyorsanız yararlı olabilir.

Burada bu dosyaları kendiniz, aynı FastAPI uygulamasında nasıl sunacağınızı ve belgeleri bunları kullanacak şekilde nasıl yapılandıracağınızı göreceksiniz.

### Proje dosya yapısı

Proje dosya yapınızın şöyle göründüğünü varsayalım:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
```

Şimdi bu statik dosyaları depolamak için bir dizin oluşturun.

Yeni dosya yapınız şöyle görünebilir:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
└── static/
```

### Dosyaları indirme

Belgeler için gereken statik dosyaları indirin ve `static/` dizinine koyun.

Muhtemelen her bağlantıya sağ tıklayıp `Bağlantıyı farklı kaydet...` gibi bir seçenek seçebilirsiniz.

**Swagger UI** şu dosyaları kullanır:

* <a href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js" class="external-link" target="_blank">`swagger-ui-bundle.js`</a>
* <a href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css" class="external-link" target="_blank">`swagger-ui.css`</a>

Ve **ReDoc** şu dosyayı kullanır:

* <a href="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js" class="external-link" target="_blank">`redoc.standalone.js`</a>

Bundan sonra, dosya yapınız şöyle görünebilir:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
└── static
    ├── redoc.standalone.js
    ├── swagger-ui-bundle.js
    └── swagger-ui.css
```

### Statik dosyaları sunma

* `StaticFiles`'ı içe aktarın.
* Bir `StaticFiles()` örneğini belirli bir yola "bağlayın".

{* ../../docs_src/custom_docs_ui/tutorial002.py hl[7,11] *}

### Statik dosyaları test etme

Uygulamanızı başlatın ve <a href="http://127.0.0.1:8000/static/redoc.standalone.js" class="external-link" target="_blank">http://127.0.0.1:8000/static/redoc.standalone.js</a>'a gidin.

**ReDoc** için çok uzun bir JavaScript dosyası görmelisiniz.

Şöyle bir şeyle başlayabilir:

```JavaScript
/*!
 * ReDoc - OpenAPI/Swagger-generated API Reference Documentation
 * -------------------------------------------------------------
 *   Version: "2.0.0-rc.18"
 *   Repo: https://github.com/Redocly/redoc
 */
!function(e,t){"object"==typeof exports&&"object"==typeof m

...
```

Bu, uygulamanızdan statik dosyaları sunabildiğinizi ve belgeler için statik dosyaları doğru yere koyduğunuzu doğrular.

Şimdi uygulamayı bu statik dosyaları belgeler için kullanacak şekilde yapılandırabiliriz.

### Statik dosyalar için otomatik belgeleri devre dışı bırakma

Özel bir CDN kullanırken olduğu gibi, ilk adım otomatik belgeleri devre dışı bırakmaktır, çünkü bunlar varsayılan olarak CDN'yi kullanır.

Bunları devre dışı bırakmak için, `FastAPI` uygulamanızı oluştururken URL'lerini `None` olarak ayarlayın:

{* ../../docs_src/custom_docs_ui/tutorial002.py hl[9] *}

### Statik dosyalar için özel belgeleri dahil etme

Ve özel bir CDN'de olduğu gibi, şimdi özel belgeler için *yol operasyonları* oluşturabilirsiniz.

Yine, FastAPI'nin belgeler için HTML sayfalarını oluşturan dahili fonksiyonlarını yeniden kullanabilir ve gerekli argümanları geçirebilirsiniz:

* `openapi_url`: Belgeler için HTML sayfasının API'nizin OpenAPI şemasını alabileceği URL. Burada `app.openapi_url` özniteliğini kullanabilirsiniz.
* `title`: API'nizin başlığı.
* `oauth2_redirect_url`: Varsayılanı kullanmak için burada `app.swagger_ui_oauth2_redirect_url` kullanabilirsiniz.
* `swagger_js_url`: Swagger UI belgeleriniz için HTML'in **JavaScript** dosyasını alabileceği URL. **Bu, kendi uygulamanızın artık sunduğu dosyadır**.
* `swagger_css_url`: Swagger UI belgeleriniz için HTML'in **CSS** dosyasını alabileceği URL. **Bu, kendi uygulamanızın artık sunduğu dosyadır**.

Ve ReDoc için benzer şekilde...

{* ../../docs_src/custom_docs_ui/tutorial002.py hl[2:6,14:22,25:27,30:36] *}

/// tip

`swagger_ui_redirect` için *yol operasyonu* OAuth2 kullandığınızda bir yardımcıdır.

API'nizi bir OAuth2 sağlayıcısıyla entegre ederseniz, kimlik doğrulaması yapabilir ve edindiğiniz kimlik bilgileriyle API belgelerine geri dönebilirsiniz. Ve gerçek OAuth2 kimlik doğrulamasını kullanarak onunla etkileşim kurabilirsiniz.

Swagger UI bunu arka planda sizin için yönetecektir, ama bu "yönlendirme" yardımcısına ihtiyacı vardır.

///

### Statik dosyaları test etmek için bir *yol operasyonu* oluşturma

Şimdi, her şeyin çalıştığını test edebilmek için bir *yol operasyonu* oluşturun:

{* ../../docs_src/custom_docs_ui/tutorial002.py hl[39:41] *}

### Statik Dosya Arayüzünü Test Etme

Şimdi, WiFi'nizi kesebilir, <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>'taki belgelerinize gidebilir ve sayfayı yeniden yükleyebilirsiniz.

Ve İnternet olmadan bile, API'niz için belgeleri görebilir ve onunla etkileşim kurabilirsiniz.
