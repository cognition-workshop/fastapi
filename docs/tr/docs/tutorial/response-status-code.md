# Yanıt Durum Kodu

Bir yanıt modeli belirlediğiniz gibi, *yol operasyonlarından* herhangi birinde `status_code` parametresiyle yanıt için kullanılan HTTP durum kodunu da bildirebilirsiniz:

* `@app.get()`
* `@app.post()`
* `@app.put()`
* `@app.delete()`
* vb.

{* ../../docs_src/response_status_code/tutorial001.py hl[6] *}

/// note

`status_code`'un "dekoratör" metodunun (`get`, `post`, vb.) bir parametresi olduğuna dikkat edin. Tüm parametreler ve gövde gibi *yol operasyonu fonksiyonunuzun* değil.

///

`status_code` parametresi, HTTP durum kodu içeren bir sayı alır.

/// info

`status_code` alternatif olarak Python'un <a href="https://docs.python.org/3/library/http.html#http.HTTPStatus" class="external-link" target="_blank">`http.HTTPStatus`</a>'u gibi bir `IntEnum` de alabilir.

///

Şunları yapacaktır:

* Yanıtta bu durum kodunu döndürür.
* OpenAPI şemasında (ve dolayısıyla kullanıcı arayüzlerinde) böyle belgelendirir:

<img src="/img/tutorial/response-status-code/image01.png">

/// note

Bazı yanıt kodları (sonraki bölüme bakın) yanıtın bir gövdesi olmadığını belirtir.

FastAPI bunu bilir ve gövde yanıtı olmadığını belirten OpenAPI belgeleri üretir.

///

## HTTP durum kodları hakkında

/// note

HTTP durum kodlarının ne olduğunu zaten biliyorsanız, sonraki bölüme geçin.

///

HTTP'de, yanıtın bir parçası olarak 3 haneli sayısal bir durum kodu gönderirsiniz.

Bu durum kodlarının tanınması için ilişkilendirilmiş bir adı vardır, ancak önemli olan kısım sayıdır.

Kısaca:

* `100 - 199` "Bilgi" içindir. Bunları doğrudan nadiren kullanırsınız. Bu durum kodlarına sahip yanıtların bir gövdesi olamaz.
* **`200 - 299`** "Başarılı" yanıtlar içindir. Bunları en çok kullanırsınız.
    * `200` varsayılan durum kodudur, her şeyin "Tamam" olduğu anlamına gelir.
    * Başka bir örnek `201`, "Oluşturuldu" olabilir. Genellikle veritabanında yeni bir kayıt oluşturduktan sonra kullanılır.
    * Özel bir durum `204`, "İçerik Yok"tur. Bu yanıt, istemciye döndürülecek içerik olmadığında kullanılır ve bu nedenle yanıtın bir gövdesi olmamalıdır.
* **`300 - 399`** "Yönlendirme" içindir. Bu durum kodlarına sahip yanıtların bir gövdesi olabilir de olmayabilir de, ancak `304`, "Değiştirilmedi" hariç, onun bir gövdesi olmamalıdır.
* **`400 - 499`** "İstemci hatası" yanıtları içindir. Bunlar muhtemelen en çok kullanacağınız ikinci türdür.
    * Bir örnek `404`, "Bulunamadı" yanıtı içindir.
    * İstemciden genel hatalar için `400` kullanabilirsiniz.
* `500 - 599` sunucu hataları içindir. Bunları doğrudan neredeyse hiç kullanmazsınız. Uygulama kodunuzun veya sunucunuzun herhangi bir yerinde bir şeyler ters gittiğinde, otomatik olarak bu durum kodlarından birini döndürür.

/// tip

Her durum kodu ve hangi kodun ne için olduğu hakkında daha fazla bilgi edinmek için, <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status" class="external-link" target="_blank"><abbr title="Mozilla Developer Network">MDN</abbr> HTTP durum kodları hakkındaki belgelere</a> göz atın.

///

## Adları hatırlamak için kısayol

Önceki örneğe tekrar bakalım:

{* ../../docs_src/response_status_code/tutorial001.py hl[6] *}

`201`, "Oluşturuldu" için durum kodudur.

Ancak bu kodların her birinin ne anlama geldiğini ezberlemeniz gerekmez.

`fastapi.status`'tan kolaylık değişkenlerini kullanabilirsiniz.

{* ../../docs_src/response_status_code/tutorial002.py hl[1,6] *}

Bunlar yalnızca bir kolaylıktır, aynı sayıyı tutarlar, ancak bu şekilde editörünüzün otomatik tamamlama özelliğini kullanarak onları bulabilirsiniz:

<img src="/img/tutorial/response-status-code/image02.png">

/// note | Teknik Detaylar

`from starlette import status` ifadesini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için aynı `starlette.status`'ı `fastapi.status` olarak sunar. Ancak doğrudan Starlette'ten gelir.

///

## Varsayılanı değiştirme

Daha sonra, [Gelişmiş Kullanıcı Kılavuzu](../advanced/response-change-status-code.md){.internal-link target=_blank}'nda, burada bildirdiğiniz varsayılandan farklı bir durum kodu döndürmeyi göreceksiniz.
