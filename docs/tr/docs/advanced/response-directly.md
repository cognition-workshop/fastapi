# Doğrudan Bir Yanıt Döndürme

Bir **FastAPI** *yol operasyonu* oluşturduğunuzda normalde ondan herhangi bir veri döndürebilirsiniz: bir `dict`, bir `list`, bir Pydantic modeli, bir veritabanı modeli, vb.

Varsayılan olarak, **FastAPI** o dönüş değerini [JSON Uyumlu Kodlayıcı](../tutorial/encoder.md){.internal-link target=_blank}'da açıklanan `jsonable_encoder` kullanarak otomatik olarak JSON'a dönüştürür.

Ardından, perde arkasında, o JSON uyumlu veriyi (ör. bir `dict`) istemciye yanıt göndermek için kullanılacak bir `JSONResponse`'un içine koyar.

Ama *yol operasyonlarınızdan* doğrudan bir `JSONResponse` döndürebilirsiniz.

Örneğin, özel başlıklar veya çerezler döndürmek için yararlı olabilir.

## Bir `Response` döndürün

Aslında, herhangi bir `Response` veya onun herhangi bir alt sınıfını döndürebilirsiniz.

/// tip

`JSONResponse`'un kendisi `Response`'un bir alt sınıfıdır.

///

Ve bir `Response` döndürdüğünüzde, **FastAPI** onu doğrudan iletecektir.

Pydantic modelleriyle veri dönüşümü yapmayacak, içerikleri herhangi bir tipe dönüştürmeyecektir, vb.

Bu size çok fazla esneklik sağlar. Herhangi bir veri tipini döndürebilir, herhangi bir veri bildirimini veya doğrulamayı geçersiz kılabilirsiniz, vb.

## Bir `Response`'da `jsonable_encoder` kullanma

**FastAPI**, döndürdüğünüz bir `Response`'da herhangi bir değişiklik yapmadığından, içeriklerinin hazır olduğundan emin olmanız gerekir.

Örneğin, tüm veri tipleri (ör. `datetime`, `UUID`, vb.) JSON uyumlu tiplere dönüştürülmeden bir Pydantic modelini `JSONResponse`'a koyamazsınız.

Bu durumlar için, verilerinizi bir yanıta iletmeden önce dönüştürmek amacıyla `jsonable_encoder`'ı kullanabilirsiniz:

{* ../../docs_src/response_directly/tutorial001.py hl[6:7,21:22] *}

/// note | Teknik Detaylar

`from starlette.responses import JSONResponse` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.responses`'ı `fastapi.responses` olarak sağlar. Ancak mevcut yanıtların çoğu doğrudan Starlette'den gelir.

///

## Özel bir `Response` döndürme

Yukarıdaki örnek ihtiyacınız olan tüm parçaları gösterir, ancak henüz çok yararlı değildir, çünkü `item`'ı doğrudan döndürebilirdiniz ve **FastAPI** onu sizin için bir `JSONResponse`'a koyar, bir `dict`'e dönüştürür, vb. Tüm bunlar varsayılan olarak.

Şimdi, bunu özel bir yanıt döndürmek için nasıl kullanabileceğinizi görelim.

Diyelim ki bir <a href="https://en.wikipedia.org/wiki/XML" class="external-link" target="_blank">XML</a> yanıtı döndürmek istiyorsunuz.

XML içeriğinizi bir dizeye koyabilir, onu bir `Response`'a koyabilir ve döndürebilirsiniz:

{* ../../docs_src/response_directly/tutorial002.py hl[1,18] *}

## Notlar

Doğrudan bir `Response` döndürdüğünüzde, verisi otomatik olarak doğrulanmaz, dönüştürülmez (serileştirilmez) veya belgelenmez.

Ancak yine de [OpenAPI'de Ek Yanıtlar](additional-responses.md){.internal-link target=_blank}'da açıklandığı gibi belgeleyebilirsiniz.

Sonraki bölümlerde bu özel `Response`'ları kullanırken/bildirirken hala otomatik veri dönüşümü, belgeleme vb. nasıl yapılacağını görebilirsiniz.
