# Yol Operasyonu Gelişmiş Yapılandırma

## OpenAPI operationId

/// warning

OpenAPI konusunda "uzman" değilseniz, muhtemelen buna ihtiyacınız yoktur.

///

*Yol operasyonunuzda* kullanılacak OpenAPI `operationId`'yi `operation_id` parametresiyle ayarlayabilirsiniz.

Her operasyon için benzersiz olduğundan emin olmanız gerekir.

{* ../../docs_src/path_operation_advanced_configuration/tutorial001.py hl[6] *}

### *Yol operasyonu fonksiyonu* adını operationId olarak kullanma

API'lerinizin fonksiyon adlarını `operationId` olarak kullanmak istiyorsanız, hepsini yineleyebilir ve her *yol operasyonunun* `operation_id`'sini `APIRoute.name` kullanarak geçersiz kılabilirsiniz.

Bunu tüm *yol operasyonlarınızı* ekledikten sonra yapmalısınız.

{* ../../docs_src/path_operation_advanced_configuration/tutorial002.py hl[2, 12:21, 24] *}

/// tip

`app.openapi()`'yi elle çağırıyorsanız, bundan önce `operationId`'leri güncellemelisiniz.

///

/// warning

Bunu yaparsanız, her bir *yol operasyonu fonksiyonunuzun* benzersiz bir ada sahip olduğundan emin olmalısınız.

Farklı modüllerde (Python dosyalarında) olsalar bile.

///

## OpenAPI'den hariç tutma

Bir *yol operasyonunu* oluşturulan OpenAPI şemasından (ve dolayısıyla otomatik belgeleme sistemlerinden) hariç tutmak için `include_in_schema` parametresini kullanın ve `False` olarak ayarlayın:

{* ../../docs_src/path_operation_advanced_configuration/tutorial003.py hl[6] *}

## Docstring'den gelişmiş açıklama

OpenAPI için bir *yol operasyonu fonksiyonunun* docstring'inden kullanılan satırları sınırlayabilirsiniz.

Bir `\f` ("form feed" kaçış karakteri) eklemek, **FastAPI**'nin OpenAPI için kullanılan çıktıyı bu noktada kesmesine neden olur.

Belgelerde görünmeyecektir, ama diğer araçlar (Sphinx gibi) geri kalanını kullanabilecektir.

{* ../../docs_src/path_operation_advanced_configuration/tutorial004.py hl[19:29] *}

## Ek Yanıtlar

Muhtemelen bir *yol operasyonu* için `response_model` ve `status_code`'un nasıl bildirileceğini zaten gördünüz.

Bu, bir *yol operasyonunun* ana yanıtı hakkındaki meta verileri tanımlar.

Modelleri, durum kodları vb. ile ek yanıtlar da bildirebilirsiniz.

Burada belgelerde bu konuda bütün bir bölüm var, [OpenAPI'de Ek Yanıtlar](additional-responses.md){.internal-link target=_blank}'da okuyabilirsiniz.

## OpenAPI Ekstra

Uygulamanızda bir *yol operasyonu* bildirdiğinizde, **FastAPI** otomatik olarak o *yol operasyonu* hakkındaki ilgili meta verileri OpenAPI şemasına dahil edilmek üzere oluşturur.

/// note | Teknik detaylar

OpenAPI spesifikasyonunda buna <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object" class="external-link" target="_blank">Operation Object</a> denir.

///

*Yol operasyonu* hakkındaki tüm bilgilere sahiptir ve otomatik belgelemeyi oluşturmak için kullanılır.

`tags`, `parameters`, `requestBody`, `responses`, vb. içerir.

Bu *yol operasyonuna* özgü OpenAPI şeması normalde **FastAPI** tarafından otomatik olarak oluşturulur, ancak onu genişletebilirsiniz de.

/// tip

Bu düşük seviyeli bir genişletme noktasıdır.

Yalnızca ek yanıtlar bildirmeniz gerekiyorsa, bunu yapmanın daha uygun bir yolu [OpenAPI'de Ek Yanıtlar](additional-responses.md){.internal-link target=_blank}'dır.

///

Bir *yol operasyonu* için OpenAPI şemasını `openapi_extra` parametresini kullanarak genişletebilirsiniz.

### OpenAPI Uzantıları

Bu `openapi_extra`, örneğin <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#specificationExtensions" class="external-link" target="_blank">OpenAPI Uzantılarını</a> bildirmek için yararlı olabilir:

{* ../../docs_src/path_operation_advanced_configuration/tutorial005.py hl[6] *}

Otomatik API belgelerini açarsanız, uzantınız belirli *yol operasyonunun* altında görünecektir.

<img src="/img/tutorial/path-operation-advanced-configuration/image01.png">

Ve ortaya çıkan OpenAPI'yi (API'nizdeki `/openapi.json`'da) görürseniz, uzantınızı belirli *yol operasyonunun* bir parçası olarak da göreceksiniz:

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

### Özel OpenAPI *yol operasyonu* şeması

`openapi_extra` içindeki sözlük, *yol operasyonu* için otomatik olarak oluşturulan OpenAPI şemasıyla derin birleştirme yapılacaktır.

Böylece otomatik olarak oluşturulan şemaya ek veriler ekleyebilirsiniz.

Örneğin, isteği kendi kodunuzla okumaya ve doğrulamaya, FastAPI'nin Pydantic ile otomatik özelliklerini kullanmadan, ama yine de isteği OpenAPI şemasında tanımlamak isteyebileceğinize karar verebilirsiniz.

Bunu `openapi_extra` ile yapabilirsiniz:

{* ../../docs_src/path_operation_advanced_configuration/tutorial006.py hl[19:36, 39:40] *}

Bu örnekte herhangi bir Pydantic modeli bildirmedik. Aslında istek gövdesi JSON olarak bile <abbr title="bayt gibi düz bir formattan Python nesnelerine dönüştürme">ayrıştırılmıyor</abbr>, doğrudan `bytes` olarak okunuyor ve `magic_data_reader()` fonksiyonu bir şekilde ayrıştırmaktan sorumlu olacaktır.

Yine de, istek gövdesi için beklenen şemayı bildirebiliriz.

### Özel OpenAPI içerik türü

Aynı numarayı kullanarak, *yol operasyonu* için özel OpenAPI şema bölümüne dahil edilen JSON Şemasını tanımlamak için bir Pydantic modeli kullanabilirsiniz.

Ve istekteki veri türü JSON olmasa bile bunu yapabilirsiniz.

Örneğin, bu uygulamada Pydantic modellerinden JSON Şeması çıkarmak için FastAPI'nin entegre işlevselliğini veya JSON için otomatik doğrulamayı kullanmıyoruz. Aslında istek içerik türünü JSON değil YAML olarak bildiriyoruz:

//// tab | Pydantic v2

{* ../../docs_src/path_operation_advanced_configuration/tutorial007.py hl[17:22, 24] *}

////

//// tab | Pydantic v1

{* ../../docs_src/path_operation_advanced_configuration/tutorial007_pv1.py hl[17:22, 24] *}

////

/// info

Pydantic sürüm 1'de bir model için JSON Şeması alma yöntemi `Item.schema()` olarak adlandırılıyordu, Pydantic sürüm 2'de yöntem `Item.model_json_schema()` olarak adlandırılır.

///

Yine de, varsayılan entegre işlevselliği kullanmıyor olsak da, YAML'da almak istediğimiz veriler için JSON Şemasını elle oluşturmak için hala bir Pydantic modeli kullanıyoruz.

Ardından isteği doğrudan kullanıyoruz ve gövdeyi `bytes` olarak çıkarıyoruz. Bu, FastAPI'nin istek yükünü JSON olarak ayrıştırmaya bile çalışmayacağı anlamına gelir.

Ve sonra kodumuzda, YAML içeriğini doğrudan ayrıştırıyoruz ve ardından YAML içeriğini doğrulamak için yine aynı Pydantic modelini kullanıyoruz:

//// tab | Pydantic v2

{* ../../docs_src/path_operation_advanced_configuration/tutorial007.py hl[26:33] *}

////

//// tab | Pydantic v1

{* ../../docs_src/path_operation_advanced_configuration/tutorial007_pv1.py hl[26:33] *}

////

/// info

Pydantic sürüm 1'de bir nesneyi ayrıştırma ve doğrulama yöntemi `Item.parse_obj()` idi, Pydantic sürüm 2'de yöntem `Item.model_validate()` olarak adlandırılır.

///

/// tip

Burada aynı Pydantic modelini yeniden kullanıyoruz.

Ama aynı şekilde, başka bir şekilde de doğrulayabilirdik.

///
