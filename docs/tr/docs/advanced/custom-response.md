# Özel Yanıt - HTML, Stream, Dosya, diğerleri

Varsayılan olarak, **FastAPI** yanıtları `JSONResponse` kullanarak döndürecektir.

[Doğrudan bir Yanıt döndürme](response-directly.md){.internal-link target=_blank}'de görüldüğü gibi doğrudan bir `Response` döndürerek bunu geçersiz kılabilirsiniz.

Ama doğrudan bir `Response` (veya `JSONResponse` gibi herhangi bir alt sınıf) döndürürseniz, veriler otomatik olarak dönüştürülmeyecektir (bir `response_model` bildirseniz bile) ve belgeler otomatik olarak oluşturulmayacaktır (örneğin, oluşturulan OpenAPI'nin bir parçası olarak HTTP başlığı `Content-Type`'daki belirli "medya türünü" dahil etme).

Ama ayrıca kullanılmasını istediğiniz `Response`'u (örneğin herhangi bir `Response` alt sınıfı) `response_class` parametresini kullanarak *yol operasyonu dekoratöründe* bildirebilirsiniz.

*Yol operasyonu fonksiyonunuzdan* döndürdüğünüz içerikler o `Response`'un içine konulacaktır.

Ve o `Response`'un `JSONResponse` ve `UJSONResponse` durumunda olduğu gibi bir JSON medya türü (`application/json`) varsa, döndürdüğünüz veriler *yol operasyonu dekoratöründe* bildirdiğiniz herhangi bir Pydantic `response_model` ile otomatik olarak dönüştürülecek (ve filtrelenecek).

/// note

Medya türü olmayan bir yanıt sınıfı kullanırsanız, FastAPI yanıtınızın içerik içermemesini bekleyecek, bu yüzden oluşturulan OpenAPI belgelerinde yanıt biçimini belgelemeyecektir.

///

## `ORJSONResponse` kullanma

Örneğin, performansı sıkıştırıyorsanız, <a href="https://github.com/ijl/orjson" class="external-link" target="_blank">`orjson`</a>'u yükleyip kullanabilir ve yanıtı `ORJSONResponse` olarak ayarlayabilirsiniz.

Kullanmak istediğiniz `Response` sınıfını (alt sınıfı) içe aktarın ve *yol operasyonu dekoratöründe* bildirin.

Büyük yanıtlar için, bir sözlük döndürmekten çok daha hızlı bir şekilde doğrudan bir `Response` döndürmek.

Bunun nedeni, varsayılan olarak FastAPI'nin içerideki her öğeyi inceleyip JSON olarak serileştirilebilir olduğundan emin olmasıdır, öğreticide açıklanan aynı [JSON Uyumlu Kodlayıcı](../tutorial/encoder.md){.internal-link target=_blank}'yı kullanarak. Bu, örneğin veritabanı modelleri gibi **rastgele nesneler** döndürmenize olanak tanıyan şeydir.

Ama döndürdüğünüz içeriğin **JSON ile serileştirilebilir** olduğundan eminseniz, onu doğrudan yanıt sınıfına iletebilir ve FastAPI'nin döndürme içeriğinizi yanıt sınıfına iletmeden önce `jsonable_encoder`'dan geçirmesiyle oluşacak ekstra yükü önleyebilirsiniz.

{* ../../docs_src/custom_response/tutorial001b.py hl[2,7] *}

/// info

`response_class` parametresi yanıtın "medya türünü" tanımlamak için de kullanılacaktır.

Bu durumda, HTTP başlığı `Content-Type` `application/json` olarak ayarlanacaktır.

Ve OpenAPI'de bu şekilde belgelenecektir.

///

/// tip

`ORJSONResponse` yalnızca FastAPI'de mevcuttur, Starlette'de değil.

///

## HTML Yanıtı

**FastAPI**'den doğrudan HTML ile bir yanıt döndürmek için `HTMLResponse` kullanın.

* `HTMLResponse`'u içe aktarın.
* *Yol operasyonu dekoratörünüzün* `response_class` parametresi olarak `HTMLResponse`'u iletin.

{* ../../docs_src/custom_response/tutorial002.py hl[2,7] *}

/// info

`response_class` parametresi yanıtın "medya türünü" tanımlamak için de kullanılacaktır.

Bu durumda, HTTP başlığı `Content-Type` `text/html` olarak ayarlanacaktır.

Ve OpenAPI'de bu şekilde belgelenecektir.

///

### Bir `Response` döndürme

[Doğrudan bir Yanıt döndürme](response-directly.md){.internal-link target=_blank}'de görüldüğü gibi, *yol operasyonunuzda* yanıtı doğrudan döndürerek geçersiz kılabilirsiniz.

Yukarıdaki aynı örnek, bir `HTMLResponse` döndüren, şöyle görünebilir:

{* ../../docs_src/custom_response/tutorial003.py hl[2,7,19] *}

/// warning

*Yol operasyonu fonksiyonunuz* tarafından doğrudan döndürülen bir `Response`, OpenAPI'de belgelenmeyecektir (örneğin, `Content-Type` belgelenmeyecektir) ve otomatik etkileşimli belgelerde görünmeyecektir.

///

/// info

Elbette, gerçek `Content-Type` başlığı, durum kodu vb. döndürdüğünüz `Response` nesnesinden gelecektir.

///

### OpenAPI'de belgeleme ve `Response`'u geçersiz kılma

Fonksiyonun içinden yanıtı geçersiz kılmak ama aynı zamanda OpenAPI'de "medya türünü" belgelemek istiyorsanız, `response_class` parametresini kullanabilir VE bir `Response` nesnesi döndürebilirsiniz.

`response_class` daha sonra yalnızca OpenAPI *yol operasyonunu* belgelemek için kullanılacak, ama `Response`'unuz olduğu gibi kullanılacaktır.

#### Doğrudan bir `HTMLResponse` döndürme

Örneğin, şöyle bir şey olabilir:

{* ../../docs_src/custom_response/tutorial004.py hl[7,21,23] *}

Bu örnekte, `generate_html_response()` fonksiyonu zaten HTML'yi bir `str`'de döndürmek yerine bir `Response` oluşturur ve döndürür.

`generate_html_response()` çağrısının sonucunu döndürerek, zaten varsayılan **FastAPI** davranışını geçersiz kılacak bir `Response` döndürüyorsunuz.

Ama `response_class`'a da `HTMLResponse` geçirdiğiniz için, **FastAPI** bunu OpenAPI'de ve etkileşimli belgelerde `text/html` ile HTML olarak nasıl belgeleyeceğini bilecektir:

<img src="/img/tutorial/custom-response/image01.png">

## Mevcut yanıtlar

İşte mevcut yanıtlardan bazıları.

Başka herhangi bir şeyi döndürmek için `Response`'u kullanabileceğinizi veya hatta özel bir alt sınıf oluşturabileceğinizi unutmayın.

/// note | Teknik Detaylar

`from starlette.responses import HTMLResponse` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.responses`'u `fastapi.responses` olarak sağlar. Ama mevcut yanıtların çoğu doğrudan Starlette'den gelir.

///

### `Response`

Ana `Response` sınıfı, diğer tüm yanıtlar ondan miras alır.

Doğrudan döndürebilirsiniz.

Şu parametreleri kabul eder:

* `content` - Bir `str` veya `bytes`.
* `status_code` - Bir `int` HTTP durum kodu.
* `headers` - Dizelerin bir `dict`'i.
* `media_type` - Medya türünü veren bir `str`. Örn. `"text/html"`.

FastAPI (aslında Starlette) otomatik olarak bir Content-Length başlığı ekleyecektir. Ayrıca `media_type`'a dayanan ve metin türleri için bir karakter seti ekleyen bir Content-Type başlığı da ekleyecektir.

{* ../../docs_src/response_directly/tutorial002.py hl[1,18] *}

### `HTMLResponse`

Bir metin veya bayt alır ve yukarıda okuduğunuz gibi bir HTML yanıtı döndürür.

### `PlainTextResponse`

Bir metin veya bayt alır ve düz metin yanıtı döndürür.

{* ../../docs_src/custom_response/tutorial005.py hl[2,7,9] *}

### `JSONResponse`

Bazı verileri alır ve `application/json` kodlanmış bir yanıt döndürür.

Yukarıda okuduğunuz gibi, **FastAPI**'de kullanılan varsayılan yanıttır.

### `ORJSONResponse`

Yukarıda okuduğunuz gibi, <a href="https://github.com/ijl/orjson" class="external-link" target="_blank">`orjson`</a> kullanan hızlı bir alternatif JSON yanıtı.

/// info

Bu, `orjson`'un örneğin `pip install orjson` ile yüklenmesini gerektirir.

///

### `UJSONResponse`

<a href="https://github.com/ultrajson/ultrajson" class="external-link" target="_blank">`ujson`</a> kullanan alternatif bir JSON yanıtı.

/// info

Bu, `ujson`'un örneğin `pip install ujson` ile yüklenmesini gerektirir.

///

/// warning

`ujson`, bazı uç durumları nasıl ele aldığı konusunda Python'un yerleşik uygulamasından daha az dikkatlidir.

///

{* ../../docs_src/custom_response/tutorial001.py hl[2,7] *}

/// tip

`ORJSONResponse`'un daha hızlı bir alternatif olması mümkündür.

///

### `RedirectResponse`

Bir HTTP yönlendirmesi döndürür. Varsayılan olarak 307 durum kodunu (Geçici Yönlendirme) kullanır.

Doğrudan bir `RedirectResponse` döndürebilirsiniz:

{* ../../docs_src/custom_response/tutorial006.py hl[2,9] *}

---

Veya `response_class` parametresinde kullanabilirsiniz:

{* ../../docs_src/custom_response/tutorial006b.py hl[2,7,9] *}

Bunu yaparsanız, URL'yi doğrudan *yol operasyonu* fonksiyonunuzdan döndürebilirsiniz.

Bu durumda, kullanılan `status_code`, `RedirectResponse` için varsayılan olan `307` olacaktır.

---

`status_code` parametresini `response_class` parametresiyle birlikte de kullanabilirsiniz:

{* ../../docs_src/custom_response/tutorial006c.py hl[2,7,9] *}

### `StreamingResponse`

Bir asenkron oluşturucu veya normal bir oluşturucu/yineleyici alır ve yanıt gövdesini akış olarak gönderir.

{* ../../docs_src/custom_response/tutorial007.py hl[2,14] *}

#### `StreamingResponse`'u dosya benzeri nesnelerle kullanma

Bir dosya benzeri nesneniz varsa (örneğin `open()` tarafından döndürülen nesne), o dosya benzeri nesne üzerinde yinelemek için bir oluşturucu fonksiyonu oluşturabilirsiniz.

Bu şekilde, hepsini önce belleğe okumak zorunda kalmazsınız ve o oluşturucu fonksiyonunu `StreamingResponse`'a iletebilir ve döndürebilirsiniz.

Bu, bulut depolama, video işleme ve diğerleriyle etkileşim kurmak için birçok kütüphaneyi içerir.

{* ../../docs_src/custom_response/tutorial008.py hl[2,10:12,14] *}

1. Bu oluşturucu fonksiyonudur. İçinde `yield` ifadeleri içerdiği için bir "oluşturucu fonksiyonu"dur.
2. `with` bloğu kullanarak, oluşturucu fonksiyonu bittikten sonra dosya benzeri nesnenin kapatıldığından emin oluyoruz. Yani, yanıtı göndermeyi bitirdikten sonra.
3. Bu `yield from`, fonksiyona `file_like` adlı şeyin üzerinde yinelemesini söyler. Ve ardından, yinelenen her parça için, o parçayı bu oluşturucu fonksiyondan (`iterfile`) geliyormuş gibi verir.

    Yani, "oluşturma" işini dahili olarak başka bir şeye aktaran bir oluşturucu fonksiyondur.

    Bu şekilde yaparak, onu bir `with` bloğuna koyabiliriz ve böylece bitirdikten sonra dosya benzeri nesnenin kapatıldığından emin olabiliriz.

/// tip

Burada `async` ve `await`'i desteklemeyen standart `open()` kullandığımız için, yol operasyonunu normal `def` ile bildirdiğimize dikkat edin.

///

### `FileResponse`

Bir dosyayı asenkron olarak yanıt olarak akış halinde gönderir.

Diğer yanıt türlerinden farklı bir argüman seti ile örneklenir:

* `path` - Akış olarak gönderilecek dosyanın dosya yolu.
* `headers` - Dahil edilecek herhangi bir özel başlık, bir sözlük olarak.
* `media_type` - Medya türünü veren bir dize. Ayarlanmazsa, dosya adı veya yolu medya türünü çıkarmak için kullanılacaktır.
* `filename` - Ayarlanırsa, yanıtın `Content-Disposition`'ına dahil edilecektir.

Dosya yanıtları uygun `Content-Length`, `Last-Modified` ve `ETag` başlıklarını içerecektir.

{* ../../docs_src/custom_response/tutorial009.py hl[2,10] *}

`response_class` parametresini de kullanabilirsiniz:

{* ../../docs_src/custom_response/tutorial009b.py hl[2,8,10] *}

Bu durumda, dosya yolunu doğrudan *yol operasyonu* fonksiyonunuzdan döndürebilirsiniz.

## Özel yanıt sınıfı

`Response`'dan miras alarak kendi özel yanıt sınıfınızı oluşturabilir ve kullanabilirsiniz.

Örneğin, <a href="https://github.com/ijl/orjson" class="external-link" target="_blank">`orjson`</a>'u dahil edilen `ORJSONResponse` sınıfında kullanılmayan bazı özel ayarlarla kullanmak istediğinizi varsayalım.

Girintili ve biçimlendirilmiş JSON döndürmesini istediğinizi, bu yüzden `orjson.OPT_INDENT_2` orjson seçeneğini kullanmak istediğinizi varsayalım.

Bir `CustomORJSONResponse` oluşturabilirsiniz. Yapmanız gereken ana şey, içeriği `bytes` olarak döndüren bir `Response.render(content)` yöntemi oluşturmaktır:

{* ../../docs_src/custom_response/tutorial009c.py hl[9:14,17] *}

Şimdi şunu döndürmek yerine:

```json
{"message": "Hello World"}
```

...bu yanıt şunu döndürecektir:

```json
{
  "message": "Hello World"
}
```

Elbette, JSON biçimlendirmekten çok daha iyi bundan yararlanmanın yollarını bulacaksınız. 😉

## Varsayılan yanıt sınıfı

Bir **FastAPI** sınıf örneği veya bir `APIRouter` oluştururken, varsayılan olarak hangi yanıt sınıfını kullanacağınızı belirleyebilirsiniz.

Bunu tanımlayan parametre `default_response_class`'tır.

Aşağıdaki örnekte, **FastAPI**, `JSONResponse` yerine varsayılan olarak tüm *yol operasyonlarında* `ORJSONResponse` kullanacaktır.

{* ../../docs_src/custom_response/tutorial010.py hl[2,4] *}

/// tip

Yine de daha önce olduğu gibi *yol operasyonlarında* `response_class`'ı geçersiz kılabilirsiniz.

///

## Ek belgeler

Medya türünü ve diğer birçok ayrıntıyı `responses` kullanarak OpenAPI'de de bildirebilirsiniz: [OpenAPI'de Ek Yanıtlar](additional-responses.md){.internal-link target=_blank}.
