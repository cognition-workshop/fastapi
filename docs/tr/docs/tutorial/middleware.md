# Middleware

**FastAPI** uygulamalarına middleware ekleyebilirsiniz.

Bir "middleware", her **istek** herhangi bir belirli *yol operasyonu* tarafından işlenmeden önce onunla çalışan bir fonksiyondur. Ayrıca her **yanıt** döndürülmeden önce de.

* Uygulamanıza gelen her **isteği** alır.
* Ardından bu **istek** ile bir şeyler yapabilir veya gerekli herhangi bir kodu çalıştırabilir.
* Sonra **isteği** uygulamanın geri kalanı tarafından işlenmesi için (bir *yol operasyonu* tarafından) iletir.
* Ardından uygulama tarafından (bir *yol operasyonu* tarafından) oluşturulan **yanıtı** alır.
* Bu **yanıt** ile bir şeyler yapabilir veya gerekli herhangi bir kodu çalıştırabilir.
* Sonra **yanıtı** döndürür.

/// note | Teknik Detaylar

`yield` ile bağımlılıklarınız varsa, çıkış kodu middleware'den *sonra* çalışacaktır.

Herhangi bir arka plan görevi varsa ([Arka Plan Görevleri](background-tasks.md){.internal-link target=_blank} bölümünde ele alınmıştır, daha sonra göreceksiniz), tüm middleware'den *sonra* çalışacaktır.

///

## Bir middleware oluşturun

Bir middleware oluşturmak için bir fonksiyonun üstünde `@app.middleware("http")` dekoratörünü kullanırsınız.

Middleware fonksiyonu şunları alır:

* `request`.
* Parametre olarak `request`'i alacak bir `call_next` fonksiyonu.
    * Bu fonksiyon, `request`'i ilgili *yol operasyonuna* iletecektir.
    * Ardından ilgili *yol operasyonu* tarafından oluşturulan `response`'u döndürür.
* Ardından `response`'u döndürmeden önce daha fazla değiştirebilirsiniz.

{* ../../docs_src/middleware/tutorial001.py hl[8:9,11,14] *}

/// tip

Özel tescilli header'ların <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers" class="external-link" target="_blank">'X-' öneki kullanılarak</a> eklenebileceğini unutmayın.

Ancak bir tarayıcıdaki istemcinin görebilmesini istediğiniz özel header'larınız varsa, bunları <a href="https://www.starlette.io/middleware/#corsmiddleware" class="external-link" target="_blank">Starlette'in CORS belgelerinde</a> belgelenen `expose_headers` parametresini kullanarak CORS yapılandırmalarınıza ([CORS (Çapraz Kaynak Paylaşımı)](cors.md){.internal-link target=_blank}) eklemeniz gerekir.

///

/// note | Teknik Detaylar

`from starlette.requests import Request` ifadesini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için bunu sunar. Ancak doğrudan Starlette'ten gelir.

///

### `response`'tan önce ve sonra

Herhangi bir *yol operasyonu* almadan önce `request` ile çalıştırılacak kod ekleyebilirsiniz.

Ve ayrıca `response` oluşturulduktan sonra, döndürülmeden önce.

Örneğin, isteği işlemek ve yanıt oluşturmak için geçen süreyi saniye cinsinden içeren özel bir `X-Process-Time` header'ı ekleyebilirsiniz:

{* ../../docs_src/middleware/tutorial001.py hl[10,12:13] *}

/// tip

Burada bu kullanım durumları için daha hassas olabileceğinden `time.time()` yerine <a href="https://docs.python.org/3/library/time.html#time.perf_counter" class="external-link" target="_blank">`time.perf_counter()`</a> kullanıyoruz. 🤓

///

## Diğer middleware'ler

Diğer middleware'ler hakkında daha sonra [Gelişmiş Kullanıcı Kılavuzu: Gelişmiş Middleware](../advanced/middleware.md){.internal-link target=_blank} bölümünde daha fazla bilgi edinebilirsiniz.

Bir sonraki bölümde <abbr title="Çapraz Kaynak Paylaşımı">CORS</abbr>'u bir middleware ile nasıl ele alacağınızı okuyacaksınız.
