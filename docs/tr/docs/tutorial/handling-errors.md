# Hataları Yönetme

API'nizi kullanan bir istemciye bir hata bildirmeniz gereken birçok durum vardır.

Bu istemci, ön yüzlü bir tarayıcı, başka birinin kodu, bir IoT cihazı vb. olabilir.

İstemciye şunları bildirmeniz gerekebilir:

* İstemcinin bu işlem için yeterli yetkileri yok.
* İstemcinin bu kaynağa erişimi yok.
* İstemcinin erişmeye çalıştığı öğe mevcut değil.
* vb.

Bu durumlarda, normalde **400** aralığında (400 ile 499 arası) bir **HTTP durum kodu** döndürürsünüz.

Bu, 200 HTTP durum kodlarına (200 ile 299 arası) benzer. Bu "200" durum kodları, istekte bir şekilde "başarı" olduğu anlamına gelir.

400 aralığındaki durum kodları, istemciden bir hata olduğu anlamına gelir.

Tüm o **"404 Bulunamadı"** hatalarını (ve şakaları) hatırlıyor musunuz?

## `HTTPException` kullanın

İstemciye hata içeren HTTP yanıtları döndürmek için `HTTPException` kullanırsınız.

### `HTTPException`'ı içe aktarın

{* ../../docs_src/handling_errors/tutorial001.py hl[1] *}

### Kodunuzda bir `HTTPException` yükseltin

`HTTPException`, API'ler için ilgili ek verilere sahip normal bir Python istisnasıdır.

Bir Python istisnası olduğu için, onu `return` etmezsiniz, `raise` edersiniz.

Bu ayrıca, *yol operasyonu fonksiyonunuzun* içinde çağırdığınız bir yardımcı fonksiyonun içindeyseniz ve o yardımcı fonksiyonun içinden `HTTPException`'ı yükseltirseniz, *yol operasyonu fonksiyonundaki* kodun geri kalanını çalıştırmayacağı, o isteği hemen sonlandıracağı ve `HTTPException`'dan gelen HTTP hatasını istemciye göndereceği anlamına gelir.

Bir değer `return` etmek yerine bir istisna `raise` etmenin avantajı, Bağımlılıklar ve Güvenlik hakkındaki bölümde daha belirgin olacaktır.

Bu örnekte, istemci mevcut olmayan bir ID ile bir öğe istediğinde, `404` durum koduyla bir istisna yükseltin:

{* ../../docs_src/handling_errors/tutorial001.py hl[11] *}

### Sonuç yanıtı

İstemci `http://example.com/items/foo` isterse (`"foo"` `item_id`'si ile), 200 HTTP durum kodu ve şu JSON yanıtı alacaktır:

```JSON
{
  "item": "The Foo Wrestlers"
}
```

Ancak istemci `http://example.com/items/bar` isterse (mevcut olmayan `"bar"` `item_id`'si ile), 404 HTTP durum kodu ("bulunamadı" hatası) ve şu JSON yanıtı alacaktır:

```JSON
{
  "detail": "Item not found"
}
```

/// tip

Bir `HTTPException` yükseltirken, yalnızca `str` değil, JSON'a dönüştürülebilen herhangi bir değeri `detail` parametresi olarak iletebilirsiniz.

Bir `dict`, bir `list` vb. iletebilirsiniz.

Bunlar **FastAPI** tarafından otomatik olarak işlenir ve JSON'a dönüştürülür.

///

## Özel header'lar ekleme

HTTP hatasına özel header'lar ekleyebilmenin yararlı olduğu bazı durumlar vardır. Örneğin, bazı güvenlik türleri için.

Muhtemelen doğrudan kodunuzda kullanmanıza gerek kalmayacaktır.

Ancak gelişmiş bir senaryo için ihtiyacınız olursa, özel header'lar ekleyebilirsiniz:

{* ../../docs_src/handling_errors/tutorial002.py hl[14] *}

## Özel istisna işleyicileri yükleme

<a href="https://www.starlette.io/exceptions/" class="external-link" target="_blank">Starlette'in aynı istisna yardımcılarını</a> kullanarak özel istisna işleyicileri ekleyebilirsiniz.

Diyelim ki sizin (veya kullandığınız bir kütüphanenin) `raise` edebileceği özel bir `UnicornException` istisnanız var.

Ve bu istisnayı FastAPI ile global olarak işlemek istiyorsunuz.

`@app.exception_handler()` ile özel bir istisna işleyicisi ekleyebilirsiniz:

{* ../../docs_src/handling_errors/tutorial003.py hl[5:7,13:18,24] *}

Burada, `/unicorns/yolo` isterseniz, *yol operasyonu* bir `UnicornException` `raise` edecektir.

Ancak `unicorn_exception_handler` tarafından işlenecektir.

Böylece, `418` HTTP durum kodu ve şu JSON içeriğiyle temiz bir hata alacaksınız:

```JSON
{"message": "Oops! yolo did something. There goes a rainbow..."}
```

/// note | Teknik Detaylar

`from starlette.requests import Request` ve `from starlette.responses import JSONResponse` ifadelerini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için aynı `starlette.responses`'ı `fastapi.responses` olarak sunar. Ancak mevcut yanıtların çoğu doğrudan Starlette'ten gelir. `Request` için de aynı durum geçerlidir.

///

## Varsayılan istisna işleyicilerini geçersiz kılma

**FastAPI**'nin bazı varsayılan istisna işleyicileri vardır.

Bu işleyiciler, bir `HTTPException` `raise` ettiğinizde ve istek geçersiz veri içerdiğinde varsayılan JSON yanıtlarını döndürmekle sorumludur.

Bu istisna işleyicilerini kendi işleyicilerinizle geçersiz kılabilirsiniz.

### İstek doğrulama istisnalarını geçersiz kılma

Bir istek geçersiz veri içerdiğinde, **FastAPI** dahili olarak bir `RequestValidationError` yükseltir.

Ve bunun için varsayılan bir istisna işleyicisi de içerir.

Geçersiz kılmak için, `RequestValidationError`'ı içe aktarın ve onu `@app.exception_handler(RequestValidationError)` ile istisna işleyicisini dekore etmek için kullanın.

İstisna işleyicisi bir `Request` ve istisnayı alacaktır.

{* ../../docs_src/handling_errors/tutorial004.py hl[2,14:16] *}

Şimdi, `/items/foo` adresine giderseniz, varsayılan JSON hatası yerine:

```JSON
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

şu metin sürümünü alacaksınız:

```
1 validation error
path -> item_id
  value is not a valid integer (type=type_error.integer)
```

#### `RequestValidationError` vs `ValidationError`

/// warning

Bunlar, şu anda sizin için önemli değilse atlayabileceğiniz teknik detaylardır.

///

`RequestValidationError`, Pydantic'in <a href="https://docs.pydantic.dev/latest/concepts/models/#error-handling" class="external-link" target="_blank">`ValidationError`</a>'unun bir alt sınıfıdır.

**FastAPI** bunu kullanır, böylece `response_model`'de bir Pydantic modeli kullanırsanız ve verilerinizde bir hata varsa, günlüğünüzde hatayı göreceksiniz.

Ancak istemci/kullanıcı bunu görmez. Bunun yerine, istemci `500` HTTP durum kodu ile bir "Internal Server Error" alacaktır.

Bu böyle olmalıdır çünkü *yanıtınızda* veya kodunuzun herhangi bir yerinde (istemcinin *isteğinde* değil) bir Pydantic `ValidationError` varsa, bu aslında kodunuzdaki bir hatadır.

Ve siz bunu düzeltirken, istemcileriniz/kullanıcılarınız hata hakkında dahili bilgilere erişmemelidir, çünkü bu bir güvenlik açığını ortaya çıkarabilir.

### `HTTPException` hata işleyicisini geçersiz kılma

Aynı şekilde, `HTTPException` işleyicisini geçersiz kılabilirsiniz.

Örneğin, bu hatalar için JSON yerine düz metin yanıtı döndürmek isteyebilirsiniz:

{* ../../docs_src/handling_errors/tutorial004.py hl[3:4,9:11,22] *}

/// note | Teknik Detaylar

`from starlette.responses import PlainTextResponse` ifadesini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için aynı `starlette.responses`'ı `fastapi.responses` olarak sunar. Ancak mevcut yanıtların çoğu doğrudan Starlette'ten gelir.

///

### `RequestValidationError` gövdesini kullanma

`RequestValidationError`, geçersiz veri ile aldığı `body`'yi içerir.

Uygulamanızı geliştirirken gövdeyi günlüğe kaydetmek ve hata ayıklamak, kullanıcıya döndürmek vb. için kullanabilirsiniz.

{* ../../docs_src/handling_errors/tutorial005.py hl[14] *}

Şimdi geçersiz bir öğe göndermeyi deneyin:

```JSON
{
  "title": "towel",
  "size": "XL"
}
```

Alınan gövdeyi içeren verilerin geçersiz olduğunu söyleyen bir yanıt alacaksınız:

```JSON hl_lines="12-15"
{
  "detail": [
    {
      "loc": [
        "body",
        "size"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ],
  "body": {
    "title": "towel",
    "size": "XL"
  }
}
```

#### FastAPI'nin `HTTPException`'ı vs Starlette'in `HTTPException`'ı

**FastAPI**'nin kendi `HTTPException`'ı vardır.

Ve **FastAPI**'nin `HTTPException` hata sınıfı, Starlette'in `HTTPException` hata sınıfından miras alır.

Tek fark, **FastAPI**'nin `HTTPException`'ının `detail` alanı için JSON'a dönüştürülebilen herhangi bir veriyi kabul etmesidir, Starlette'inki ise yalnızca string kabul eder.

Bu yüzden, kodunuzda **FastAPI**'nin `HTTPException`'ını normalde olduğu gibi yükseltmeye devam edebilirsiniz.

Ancak bir istisna işleyicisi kaydettiğinizde, onu Starlette'in `HTTPException`'ı için kaydetmelisiniz.

Bu şekilde, Starlette'in dahili kodunun herhangi bir parçası veya bir Starlette eklentisi ya da uzantısı bir Starlette `HTTPException` yükseltirse, işleyiciniz onu yakalayıp işleyebilecektir.

Bu örnekte, aynı kodda her iki `HTTPException`'a sahip olabilmek için, Starlette'in istisnaları `StarletteHTTPException` olarak yeniden adlandırılmıştır:

```Python
from starlette.exceptions import HTTPException as StarletteHTTPException
```

### **FastAPI**'nin istisna işleyicilerini yeniden kullanma

İstisnayı **FastAPI**'nin aynı varsayılan istisna işleyicileriyle birlikte kullanmak istiyorsanız, `fastapi.exception_handlers`'dan varsayılan istisna işleyicilerini içe aktarıp yeniden kullanabilirsiniz:

{* ../../docs_src/handling_errors/tutorial006.py hl[2:5,15,21] *}

Bu örnekte hatayı çok ifade edici bir mesajla `print` ediyorsunuz, ancak fikri anlıyorsunuz. İstisnayı kullanabilir ve ardından varsayılan istisna işleyicilerini yeniden kullanabilirsiniz.
