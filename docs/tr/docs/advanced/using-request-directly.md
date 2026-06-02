# İsteği Doğrudan Kullanma

Şimdiye kadar, isteğin ihtiyacınız olan bölümlerini tipleriyle birlikte bildiriyordunuz.

Şuralardan veri alarak:

* Yolu parametreler olarak.
* Başlıklar.
* Çerezler.
* vb.

Ve bunu yaparak, **FastAPI** o veriyi doğruluyor, dönüştürüyor ve API'niz için belgeleri otomatik olarak oluşturuyor.

Ancak `Request` nesnesine doğrudan erişmeniz gereken durumlar olabilir.

## `Request` nesnesi hakkında detaylar

**FastAPI** aslında altta **Starlette** olduğundan, üstünde çeşitli araç katmanlarıyla, Starlette'in <a href="https://www.starlette.io/requests/" class="external-link" target="_blank">`Request`</a> nesnesini doğrudan kullanabilirsiniz.

Bu ayrıca `Request` nesnesinden doğrudan veri alırsanız (örneğin, gövdeyi okumak) FastAPI tarafından doğrulanmayacağı, dönüştürülmeyeceği veya belgelenmeyeceği (OpenAPI ile, otomatik API kullanıcı arayüzü için) anlamına gelir.

Ancak normal olarak bildirilen diğer parametreler (örneğin, bir Pydantic modeli ile gövde) yine de doğrulanacak, dönüştürülecek, açıklanacak, vb.

Ancak `Request` nesnesini almanın yararlı olduğu belirli durumlar vardır.

## `Request` nesnesini doğrudan kullanın

Diyelim ki istemcinin IP adresini/host'unu *yol operasyonu fonksiyonunuzun* içinde almak istiyorsunuz.

Bunun için isteğe doğrudan erişmeniz gerekir.

{* ../../docs_src/using_request_directly/tutorial001.py hl[1,7:8] *}

Bir *yol operasyonu fonksiyonu* parametresini `Request` tipiyle bildirdiğinizde, **FastAPI** o parametreye `Request`'i iletmeyi bilecektir.

/// tip

Bu durumda, istek parametresinin yanında bir yol parametresi de bildirdiğimize dikkat edin.

Yani, yol parametresi çıkarılacak, doğrulanacak, belirtilen tipe dönüştürülecek ve OpenAPI ile açıklanacaktır.

Aynı şekilde, herhangi bir başka parametreyi normal olarak bildirebilir ve ek olarak `Request`'i de alabilirsiniz.

///

## `Request` belgeleri

<a href="https://www.starlette.io/requests/" class="external-link" target="_blank">Resmi Starlette belge sitesindeki `Request` nesnesi</a> hakkında daha fazla ayrıntı okuyabilirsiniz.

/// note | Teknik Detaylar

`from starlette.requests import Request` de kullanabilirsiniz.

**FastAPI** bunu geliştirici olarak sizin için bir kolaylık olarak doğrudan sağlar. Ancak doğrudan Starlette'den gelir.

///
