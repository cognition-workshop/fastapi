# Özel Request ve APIRoute Sınıfı

Bazı durumlarda, `Request` ve `APIRoute` sınıfları tarafından kullanılan mantığı geçersiz kılmak isteyebilirsiniz.

Özellikle, bu bir ara yazılımdaki mantığa iyi bir alternatif olabilir.

Örneğin, istek gövdesini uygulamanız tarafından işlenmeden önce okumak veya değiştirmek istiyorsanız.

/// danger

Bu "gelişmiş" bir özelliktir.

**FastAPI** ile yeni başlıyorsanız bu bölümü atlamak isteyebilirsiniz.

///

## Kullanım durumları

Bazı kullanım durumları şunlardır:

* JSON olmayan istek gövdelerini JSON'a dönüştürme (örn. <a href="https://msgpack.org/index.html" class="external-link" target="_blank">`msgpack`</a>).
* Gzip ile sıkıştırılmış istek gövdelerini açma.
* Tüm istek gövdelerini otomatik olarak günlüğe kaydetme.

## Özel istek gövdesi kodlamalarını yönetme

Gzip isteklerini açmak için özel bir `Request` alt sınıfının nasıl kullanılacağını görelim.

Ve o özel istek sınıfını kullanmak için bir `APIRoute` alt sınıfı.

### Özel bir `GzipRequest` sınıfı oluşturma

/// tip

Bu, nasıl çalıştığını göstermek için bir oyuncak örnektir, Gzip desteğine ihtiyacınız varsa sağlanan [`GzipMiddleware`](../advanced/middleware.md#gzipmiddleware){.internal-link target=_blank}'ı kullanabilirsiniz.

///

İlk olarak, uygun bir başlığın varlığında gövdeyi açmak için `Request.body()` metodunu geçersiz kılacak bir `GzipRequest` sınıfı oluşturuyoruz.

Başlıkta `gzip` yoksa, gövdeyi açmaya çalışmayacaktır.

Bu şekilde, aynı rota sınıfı gzip ile sıkıştırılmış veya sıkıştırılmamış istekleri işleyebilir.

{* ../../docs_src/custom_request_and_route/tutorial001.py hl[8:15] *}

### Özel bir `GzipRoute` sınıfı oluşturma

Ardından, `GzipRequest`'i kullanacak `fastapi.routing.APIRoute`'un özel bir alt sınıfını oluşturuyoruz.

Bu sefer, `APIRoute.get_route_handler()` metodunu geçersiz kılacaktır.

Bu metod bir fonksiyon döndürür. Ve o fonksiyon bir istek alıp bir yanıt döndürecek olandır.

Burada orijinal istekten bir `GzipRequest` oluşturmak için kullanıyoruz.

{* ../../docs_src/custom_request_and_route/tutorial001.py hl[18:26] *}

/// note | Teknik Detaylar

Bir `Request`'in `request.scope` özniteliği vardır, bu sadece istekle ilgili meta verileri içeren bir Python `dict`'idir.

Bir `Request`'in ayrıca bir `request.receive`'i vardır, bu isteğin gövdesini "almak" için bir fonksiyondur.

`scope` `dict`'i ve `receive` fonksiyonunun her ikisi de ASGI spesifikasyonunun bir parçasıdır.

Ve bu iki şey, `scope` ve `receive`, yeni bir `Request` örneği oluşturmak için gerekenlerdir.

`Request` hakkında daha fazla bilgi edinmek için <a href="https://www.starlette.io/requests/" class="external-link" target="_blank">Starlette'in İstekler hakkındaki belgelerine</a> bakın.

///

`GzipRequest.get_route_handler` tarafından döndürülen fonksiyonun farklı yaptığı tek şey `Request`'i `GzipRequest`'e dönüştürmektir.

Bunu yaparak, `GzipRequest`'imiz verileri *yol operasyonlarımıza* iletmeden önce (gerekirse) açma işlemini üstlenecektir.

Bundan sonra, tüm işleme mantığı aynıdır.

Ama `GzipRequest.body`'deki değişikliklerimiz nedeniyle, istek gövdesi **FastAPI** tarafından gerektiğinde yüklendiğinde otomatik olarak açılacaktır.

## Bir istisna işleyicisinde istek gövdesine erişme

/// tip

Aynı sorunu çözmek için, `RequestValidationError` için özel bir işleyicide `body` kullanmak muhtemelen çok daha kolaydır ([Hataları Yönetme](../tutorial/handling-errors.md#use-the-requestvalidationerror-body){.internal-link target=_blank}).

Ama bu örnek hala geçerlidir ve dahili bileşenlerle nasıl etkileşim kurulacağını gösterir.

///

İstek gövdesine bir istisna işleyicisinde erişmek için de aynı yaklaşımı kullanabiliriz.

Tek yapmamız gereken isteği bir `try`/`except` bloğu içinde işlemektir:

{* ../../docs_src/custom_request_and_route/tutorial002.py hl[13,15] *}

Bir istisna oluşursa, `Request` örneği hala kapsam dahilinde olacaktır, böylece hatayı işlerken istek gövdesini okuyabilir ve kullanabiliriz:

{* ../../docs_src/custom_request_and_route/tutorial002.py hl[16:18] *}

## Bir yönlendiricide özel `APIRoute` sınıfı

Bir `APIRouter`'ın `route_class` parametresini de ayarlayabilirsiniz:

{* ../../docs_src/custom_request_and_route/tutorial003.py hl[26] *}

Bu örnekte, `router` altındaki *yol operasyonları* özel `TimedRoute` sınıfını kullanacak ve yanıtın oluşturulması için geçen süreyi içeren ek bir `X-Response-Time` başlığına sahip olacaktır:

{* ../../docs_src/custom_request_and_route/tutorial003.py hl[13:20] *}
