# Yanıt Başlıkları

## Bir `Response` parametresi kullanın

*Yol operasyonu fonksiyonunuzda* `Response` tipinde bir parametre bildirebilirsiniz (çerezler için yapabildiğiniz gibi).

Ve ardından o *geçici* yanıt nesnesinde başlıklar ayarlayabilirsiniz.

{* ../../docs_src/response_headers/tutorial002.py hl[1, 7:8] *}

Ve ardından normalde yaptığınız gibi ihtiyacınız olan herhangi bir nesneyi döndürebilirsiniz (bir `dict`, bir veritabanı modeli, vb).

Ve bir `response_model` bildirdiyseniz, döndürdüğünüz nesneyi filtrelemek ve dönüştürmek için yine de kullanılacaktır.

**FastAPI**, başlıkları (ayrıca çerezleri ve durum kodunu) çıkarmak için o *geçici* yanıtı kullanacak ve herhangi bir `response_model` tarafından filtrelenmiş döndürdüğünüz değeri içeren son yanıta koyacaktır.

`Response` parametresini bağımlılıklarda da bildirebilir ve başlıkları (ve çerezleri) onlarda ayarlayabilirsiniz.

## Doğrudan bir `Response` döndürün

Doğrudan bir `Response` döndürürken de başlıklar ekleyebilirsiniz.

[Doğrudan Bir Yanıt Döndürme](response-directly.md){.internal-link target=_blank}'de açıklandığı gibi bir yanıt oluşturun ve başlıkları ek bir parametre olarak iletin:

{* ../../docs_src/response_headers/tutorial001.py hl[10:12] *}

/// note | Teknik Detaylar

`from starlette.responses import Response` veya `from starlette.responses import JSONResponse` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.responses`'ı `fastapi.responses` olarak sağlar. Ancak mevcut yanıtların çoğu doğrudan Starlette'den gelir.

Ve `Response` başlıkları ve çerezleri ayarlamak için sıkça kullanılabildiğinden, **FastAPI** bunu `fastapi.Response`'da da sağlar.

///

## Özel Başlıklar

Özel tescilli başlıkların <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers" class="external-link" target="_blank">'X-' öneki kullanılarak</a> eklenebileceğini unutmayın.

Ancak bir tarayıcıdaki istemcinin görebilmesini istediğiniz özel başlıklarınız varsa, bunları CORS yapılandırmalarınıza eklemeniz gerekir ([CORS (Cross-Origin Resource Sharing)](../tutorial/cors.md){.internal-link target=_blank}'da daha fazla bilgi edinin), <a href="https://www.starlette.io/middleware/#corsmiddleware" class="external-link" target="_blank">Starlette'in CORS belgelerinde</a> belgelenen `expose_headers` parametresini kullanarak.
