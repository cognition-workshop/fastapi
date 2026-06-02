# Gelişmiş Ara Katman

Ana öğreticide uygulamanıza nasıl [Özel Ara Katman](../tutorial/middleware.md){.internal-link target=_blank} ekleyeceğinizi okudunuz.

Ve ardından [`CORSMiddleware` ile CORS'u](../tutorial/cors.md){.internal-link target=_blank} nasıl ele alacağınızı da okudunuz.

Bu bölümde diğer ara katmanların nasıl kullanılacağını göreceğiz.

## ASGI ara katmanları ekleme

**FastAPI** Starlette üzerine kurulu olduğundan ve <abbr title="Asenkron Sunucu Geçidi Arayüzü">ASGI</abbr> spesifikasyonunu uyguladığından, herhangi bir ASGI ara katmanını kullanabilirsiniz.

Bir ara katmanın çalışması için FastAPI veya Starlette için yapılmış olması gerekmez, ASGI spesifikasyonunu takip etmesi yeterlidir.

Genel olarak, ASGI ara katmanları ilk argüman olarak bir ASGI uygulaması almayı bekleyen sınıflardır.

Bu nedenle, üçüncü taraf ASGI ara katmanları belgelerinde muhtemelen size şöyle bir şey yapmanızı söylerler:

```Python
from unicorn import UnicornMiddleware

app = SomeASGIApp()

new_app = UnicornMiddleware(app, some_config="rainbow")
```

Ancak FastAPI (aslında Starlette), iç ara katmanların sunucu hatalarını ele almasını ve özel istisna işleyicilerin düzgün çalışmasını sağlayan daha basit bir yol sunar.

Bunun için `app.add_middleware()` kullanırsınız (CORS örneğindeki gibi).

```Python
from fastapi import FastAPI
from unicorn import UnicornMiddleware

app = FastAPI()

app.add_middleware(UnicornMiddleware, some_config="rainbow")
```

`app.add_middleware()` ilk argüman olarak bir ara katman sınıfı ve ara katmana iletilecek ek argümanları alır.

## Entegre ara katmanlar

**FastAPI**, yaygın kullanım senaryoları için çeşitli ara katmanlar içerir, bunları nasıl kullanacağımızı göreceğiz.

/// note | Teknik Detaylar

Sonraki örneklerde `from starlette.middleware.something import SomethingMiddleware` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak `fastapi.middleware`'da çeşitli ara katmanlar sağlar. Ancak mevcut ara katmanların çoğu doğrudan Starlette'den gelir.

///

## `HTTPSRedirectMiddleware`

Tüm gelen isteklerin `https` veya `wss` olması gerektiğini zorunlu kılar.

`http` veya `ws`'ye gelen herhangi bir istek, bunun yerine güvenli şemaya yönlendirilecektir.

{* ../../docs_src/advanced_middleware/tutorial001.py hl[2,6] *}

## `TrustedHostMiddleware`

HTTP Host Header saldırılarına karşı koruma sağlamak için tüm gelen isteklerin doğru şekilde ayarlanmış bir `Host` başlığına sahip olmasını zorunlu kılar.

{* ../../docs_src/advanced_middleware/tutorial002.py hl[2,6:8] *}

Aşağıdaki argümanlar desteklenir:

* `allowed_hosts` - Ana bilgisayar adları olarak izin verilmesi gereken alan adlarının listesi. Alt alan adlarını eşleştirmek için `*.example.com` gibi joker alan adları desteklenir. Herhangi bir ana bilgisayar adına izin vermek için `allowed_hosts=["*"]` kullanın veya ara katmanı atlayın.

Gelen bir istek doğru şekilde doğrulanmazsa, bir `400` yanıtı gönderilecektir.

## `GZipMiddleware`

`Accept-Encoding` başlığında `"gzip"` içeren herhangi bir istek için GZip yanıtlarını ele alır.

Ara katman hem standart hem de akış yanıtlarını ele alacaktır.

{* ../../docs_src/advanced_middleware/tutorial003.py hl[2,6] *}

Aşağıdaki argümanlar desteklenir:

* `minimum_size` - Bu minimum boyuttan (bayt cinsinden) daha küçük yanıtları GZip ile sıkıştırma. Varsayılan `500`'dür.
* `compresslevel` - GZip sıkıştırma sırasında kullanılır. 1 ile 9 arasında bir tam sayıdır. Varsayılan `9`'dur. Düşük değer daha hızlı sıkıştırma ancak daha büyük dosya boyutu, yüksek değer ise daha yavaş sıkıştırma ancak daha küçük dosya boyutu ile sonuçlanır.

## Diğer ara katmanlar

Birçok başka ASGI ara katmanı vardır.

Örneğin:

* <a href="https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py" class="external-link" target="_blank">Uvicorn'un `ProxyHeadersMiddleware`'ı</a>
* <a href="https://github.com/florimondmanca/msgpack-asgi" class="external-link" target="_blank">MessagePack</a>

Diğer mevcut ara katmanları görmek için <a href="https://www.starlette.io/middleware/" class="external-link" target="_blank">Starlette'in Ara Katman belgelerine</a> ve <a href="https://github.com/florimondmanca/awesome-asgi" class="external-link" target="_blank">ASGI Awesome Listesine</a> bakın.
