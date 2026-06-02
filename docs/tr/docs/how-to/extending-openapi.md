# OpenAPI'yi Genişletme

Oluşturulan OpenAPI şemasını değiştirmeniz gerekebilecek bazı durumlar vardır.

Bu bölümde nasıl yapacağınızı göreceksiniz.

## Normal süreç

Normal (varsayılan) süreç aşağıdaki gibidir.

Bir `FastAPI` uygulaması (örneği) OpenAPI şemasını döndürmesi beklenen bir `.openapi()` metoduna sahiptir.

Uygulama nesnesinin oluşturulmasının bir parçası olarak, `/openapi.json` için (veya `openapi_url` olarak ne ayarladıysanız onun için) bir *yol operasyonu* kaydedilir.

Bu, uygulamanın `.openapi()` metodunun sonucuyla bir JSON yanıtı döndürür.

Varsayılan olarak, `.openapi()` metodunun yaptığı şey `.openapi_schema` özelliğini kontrol ederek içeriği olup olmadığına bakmak ve varsa döndürmektir.

Yoksa, `fastapi.openapi.utils.get_openapi` yardımcı fonksiyonunu kullanarak oluşturur.

Ve bu `get_openapi()` fonksiyonu parametre olarak alır:

* `title`: Belgelerde gösterilen OpenAPI başlığı.
* `version`: API'nizin sürümü, örn. `2.5.0`.
* `openapi_version`: Kullanılan OpenAPI spesifikasyonunun sürümü. Varsayılan olarak en son: `3.1.0`.
* `summary`: API'nin kısa bir özeti.
* `description`: API'nizin açıklaması, markdown içerebilir ve belgelerde gösterilir.
* `routes`: Rotaların bir listesi, bunlar kaydedilen her bir *yol operasyonudur*. `app.routes`'tan alınır.

/// info

`summary` parametresi OpenAPI 3.1.0 ve üstünde mevcuttur, FastAPI 0.99.0 ve üstü tarafından desteklenir.

///

## Varsayılanları geçersiz kılma

Yukarıdaki bilgileri kullanarak, aynı yardımcı fonksiyonu kullanarak OpenAPI şemasını oluşturabilir ve ihtiyacınız olan her parçayı geçersiz kılabilirsiniz.

Örneğin, <a href="https://github.com/Rebilly/ReDoc/blob/master/docs/redoc-vendor-extensions.md#x-logo" class="external-link" target="_blank">ReDoc'un özel bir logo eklemek için OpenAPI uzantısını</a> ekleyelim.

### Normal **FastAPI**

İlk olarak, tüm **FastAPI** uygulamanızı normal şekilde yazın:

{* ../../docs_src/extending_openapi/tutorial001.py hl[1,4,7:9] *}

### OpenAPI şemasını oluşturma

Ardından, aynı yardımcı fonksiyonu kullanarak OpenAPI şemasını bir `custom_openapi()` fonksiyonu içinde oluşturun:

{* ../../docs_src/extending_openapi/tutorial001.py hl[2,15:21] *}

### OpenAPI şemasını değiştirme

Şimdi ReDoc uzantısını ekleyebilirsiniz, OpenAPI şemasındaki `info` "nesnesine" özel bir `x-logo` ekleyerek:

{* ../../docs_src/extending_openapi/tutorial001.py hl[22:24] *}

### OpenAPI şemasını önbelleğe alma

`.openapi_schema` özelliğini "önbellek" olarak kullanarak oluşturduğunuz şemayı depolayabilirsiniz.

Bu şekilde, uygulamanız bir kullanıcı API belgelerinizi her açtığında şemayı yeniden oluşturmak zorunda kalmaz.

Yalnızca bir kez oluşturulur ve ardından sonraki istekler için aynı önbelleğe alınmış şema kullanılır.

{* ../../docs_src/extending_openapi/tutorial001.py hl[13:14,25:26] *}

### Metodu geçersiz kılma

Şimdi `.openapi()` metodunu yeni fonksiyonunuzla değiştirebilirsiniz.

{* ../../docs_src/extending_openapi/tutorial001.py hl[29] *}

### Kontrol edin

<a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>'a gittiğinizde özel logonuzu (bu örnekte **FastAPI**'nin logosu) kullandığınızı göreceksiniz:

<img src="/img/tutorial/extending-openapi/image01.png">
