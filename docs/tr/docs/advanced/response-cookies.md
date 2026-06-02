# Yanıt Çerezleri

## Bir `Response` parametresi kullanın

*Yol operasyonu fonksiyonunuzda* `Response` tipinde bir parametre bildirebilirsiniz.

Ve ardından o *geçici* yanıt nesnesinde çerezler ayarlayabilirsiniz.

{* ../../docs_src/response_cookies/tutorial002.py hl[1, 8:9] *}

Ve ardından normalde yaptığınız gibi ihtiyacınız olan herhangi bir nesneyi döndürebilirsiniz (bir `dict`, bir veritabanı modeli, vb).

Ve bir `response_model` bildirdiyseniz, döndürdüğünüz nesneyi filtrelemek ve dönüştürmek için yine de kullanılacaktır.

**FastAPI**, çerezleri (ayrıca başlıkları ve durum kodunu) çıkarmak için o *geçici* yanıtı kullanacak ve herhangi bir `response_model` tarafından filtrelenmiş döndürdüğünüz değeri içeren son yanıta koyacaktır.

`Response` parametresini bağımlılıklarda da bildirebilir ve çerezleri (ve başlıkları) onlarda ayarlayabilirsiniz.

## Doğrudan bir `Response` döndürün

Doğrudan kodunuzda bir `Response` döndürürken de çerezler oluşturabilirsiniz.

Bunu yapmak için, [Doğrudan Bir Yanıt Döndürme](response-directly.md){.internal-link target=_blank}'de açıklandığı gibi bir yanıt oluşturabilirsiniz.

Ardından içinde çerezleri ayarlayın ve döndürün:

{* ../../docs_src/response_cookies/tutorial001.py hl[10:12] *}

/// tip

`Response` parametresini kullanmak yerine doğrudan bir yanıt döndürürseniz, FastAPI'nin onu doğrudan döndüreceğini unutmayın.

Bu yüzden, verilerinizin doğru tipte olduğundan emin olmanız gerekir. Ör. `JSONResponse` döndürüyorsanız JSON ile uyumlu olması gerekir.

Ve ayrıca bir `response_model` tarafından filtrelenmesi gereken herhangi bir veri göndermediğinizden emin olun.

///

### Daha fazla bilgi

/// note | Teknik Detaylar

`from starlette.responses import Response` veya `from starlette.responses import JSONResponse` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.responses`'ı `fastapi.responses` olarak sağlar. Ancak mevcut yanıtların çoğu doğrudan Starlette'den gelir.

Ve `Response` başlıkları ve çerezleri ayarlamak için sıkça kullanılabildiğinden, **FastAPI** bunu `fastapi.Response`'da da sağlar.

///

Mevcut tüm parametreleri ve seçenekleri görmek için <a href="https://www.starlette.io/responses/#set-cookie" class="external-link" target="_blank">Starlette'in belgelerine</a> bakın.
