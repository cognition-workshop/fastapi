# İstek Örnek Verilerini Bildirme

Uygulamanızın alabileceği verilerin örneklerini bildirebilirsiniz.

İşte bunu yapmanın birkaç yolu.

## Pydantic modellerinde ek JSON Schema verisi

Oluşturulan JSON Schema'ya eklenecek bir Pydantic modeli için `examples` bildirebilirsiniz.

//// tab | Pydantic v2

{* ../../docs_src/schema_extra_example/tutorial001_py310.py hl[13:24] *}

////

//// tab | Pydantic v1

{* ../../docs_src/schema_extra_example/tutorial001_pv1_py310.py hl[13:23] *}

////

Bu ek bilgi, o model için çıktı **JSON Schema**'sına olduğu gibi eklenecek ve API belgelerinde kullanılacaktır.

//// tab | Pydantic v2

Pydantic sürüm 2'de, <a href="https://docs.pydantic.dev/latest/api/config/" class="external-link" target="_blank">Pydantic belgelerinde açıklandığı gibi: Yapılandırma</a> bir `dict` alan `model_config` özelliğini kullanırsınız.

Oluşturulan JSON Schema'da göstermek istediğiniz ek verileri içeren bir `dict` ile `"json_schema_extra"` ayarlayabilirsiniz, buna `examples` dahildir.

////

//// tab | Pydantic v1

Pydantic sürüm 1'de, <a href="https://docs.pydantic.dev/1.10/usage/schema/#schema-customization" class="external-link" target="_blank">Pydantic belgelerinde açıklandığı gibi: Schema customization</a> dahili bir `Config` sınıfı ve `schema_extra` kullanırsınız.

Oluşturulan JSON Schema'da göstermek istediğiniz ek verileri içeren bir `dict` ile `schema_extra` ayarlayabilirsiniz, buna `examples` dahildir.

////

/// tip

Aynı tekniği JSON Schema'yı genişletmek ve kendi özel ek bilgilerinizi eklemek için de kullanabilirsiniz.

Örneğin, bir ön yüz kullanıcı arayüzü için meta veri eklemek vb. için kullanabilirsiniz.

///

/// info

OpenAPI 3.1.0 (FastAPI 0.99.0'dan beri kullanılır) **JSON Schema** standardının bir parçası olan `examples` desteği ekledi.

Bundan önce, yalnızca tek bir örnek içeren `example` anahtar kelimesini destekliyordu. Bu hala OpenAPI 3.1.0 tarafından desteklenmektedir, ancak kullanımdan kaldırılmıştır ve JSON Schema standardının bir parçası değildir. Bu yüzden `example`'dan `examples`'a geçmeniz teşvik edilmektedir. 🤓

Bu sayfanın sonunda daha fazla bilgi okuyabilirsiniz.

///

## `Field` ek argümanları

Pydantic modelleriyle `Field()` kullanırken, ek `examples` da bildirebilirsiniz:

{* ../../docs_src/schema_extra_example/tutorial002_py310.py hl[2,8:11] *}

## JSON Schema'da `examples` - OpenAPI

Şunlardan herhangi birini kullanırken:

* `Path()`
* `Query()`
* `Header()`
* `Cookie()`
* `Body()`
* `Form()`
* `File()`

**OpenAPI** içindeki **JSON Schema**'larına eklenecek ek bilgilerle bir `examples` grubu da bildirebilirsiniz.

### `Body` ile `examples`

Burada `Body()`'de beklenen verilerin bir örneğini içeren `examples` iletiyoruz:

{* ../../docs_src/schema_extra_example/tutorial003_an_py310.py hl[22:29] *}

### Belge arayüzünde örnek

Yukarıdaki yöntemlerden herhangi biriyle `/docs`'ta şöyle görünecektir:

<img src="/img/tutorial/body-fields/image01.png">

### Birden fazla `examples` ile `Body`

Elbette birden fazla `examples` da iletebilirsiniz:

{* ../../docs_src/schema_extra_example/tutorial004_an_py310.py hl[23:38] *}

Bunu yaptığınızda, örnekler o gövde verisi için dahili **JSON Schema**'nın parçası olacaktır.

Yine de, <abbr title="2023-08-26">bu yazının yazıldığı tarihte</abbr>, belge arayüzünü göstermekten sorumlu araç olan Swagger UI, **JSON Schema**'daki veriler için birden fazla örnek göstermeyi desteklememektedir. Ancak bir geçici çözüm için aşağıyı okuyun.

### OpenAPI'ye özgü `examples`

**JSON Schema**'nın `examples`'ı desteklemesinden önce, OpenAPI'nin de `examples` adlı farklı bir alanı için desteği vardı.

Bu **OpenAPI'ye özgü** `examples`, OpenAPI spesifikasyonunun başka bir bölümüne gider. Her bir JSON Schema içine değil, **her *yol operasyonunun* ayrıntılarına** gider.

Ve Swagger UI bu özel `examples` alanını bir süredir desteklemektedir. Bu yüzden, onu **belge arayüzünde** farklı **örnekleri göstermek** için kullanabilirsiniz.

Bu OpenAPI'ye özgü `examples` alanının şekli, **birden fazla örnek** içeren bir `dict`'tir (bir `list` yerine), her biri **OpenAPI**'ye de eklenecek ek bilgiler içerir.

Bu, OpenAPI'de bulunan her JSON Schema'nın içine girmez, doğrudan *yol operasyonunda*, dışarıda gider.

### `openapi_examples` Parametresini Kullanma

OpenAPI'ye özgü `examples`'ı FastAPI'de şunlar için `openapi_examples` parametresiyle bildirebilirsiniz:

* `Path()`
* `Query()`
* `Header()`
* `Cookie()`
* `Body()`
* `Form()`
* `File()`

`dict`'in anahtarları her örneği tanımlar ve her değer başka bir `dict`'tir.

`examples`'daki her belirli örnek `dict`'i şunları içerebilir:

* `summary`: Örnek için kısa açıklama.
* `description`: Markdown metni içerebilen uzun bir açıklama.
* `value`: Gösterilen gerçek örnek, örn. bir `dict`.
* `externalValue`: `value`'ya alternatif, örneğe yönlendiren bir URL. Ancak bu, `value` kadar çok araç tarafından desteklenmeyebilir.

Şu şekilde kullanabilirsiniz:

{* ../../docs_src/schema_extra_example/tutorial005_an_py310.py hl[23:49] *}

### Belge Arayüzünde OpenAPI Örnekleri

`Body()`'ye `openapi_examples` eklendiğinde `/docs` şöyle görünecektir:

<img src="/img/tutorial/body-fields/image02.png">

## Teknik Detaylar

/// tip

Zaten **FastAPI** sürüm **0.99.0 veya üzeri** kullanıyorsanız, muhtemelen bu ayrıntıları **atlayabilirsiniz**.

Bunlar, OpenAPI 3.1.0 kullanılabilir olmadan önceki eski sürümler için daha ilgilidir.

Bunu kısa bir OpenAPI ve JSON Schema **tarih dersi** olarak düşünebilirsiniz. 🤓

///

/// warning

Bunlar, **JSON Schema** ve **OpenAPI** standartları hakkında çok teknik detaylardır.

Yukarıdaki fikirler zaten sizin için çalışıyorsa, bu yeterli olabilir ve muhtemelen bu ayrıntılara ihtiyacınız yoktur, atlamaktan çekinmeyin.

///

OpenAPI 3.1.0'dan önce, OpenAPI **JSON Schema**'nın eski ve değiştirilmiş bir sürümünü kullanıyordu.

JSON Schema'da `examples` yoktu, bu yüzden OpenAPI kendi değiştirilmiş sürümüne kendi `example` alanını ekledi.

OpenAPI ayrıca spesifikasyonun diğer bölümlerine de `example` ve `examples` alanları ekledi:

* <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#parameter-object" class="external-link" target="_blank">`Parameter Object` (spesifikasyonda)</a> FastAPI'nin şunları tarafından kullanıldı:
    * `Path()`
    * `Query()`
    * `Header()`
    * `Cookie()`
* <a href="https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#media-type-object" class="external-link" target="_blank">`Request Body Object`, `content` alanında, `Media Type Object` üzerinde (spesifikasyonda)</a> FastAPI'nin şunları tarafından kullanıldı:
    * `Body()`
    * `File()`
    * `Form()`

/// info

Bu eski OpenAPI'ye özgü `examples` parametresi artık FastAPI `0.103.0`'dan beri `openapi_examples`'tır.

///

### JSON Schema'nın `examples` alanı

Ancak sonra JSON Schema, spesifikasyonun yeni bir sürümüne bir <a href="https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.9.5" class="external-link" target="_blank">`examples`</a> alanı ekledi.

Ve ardından yeni OpenAPI 3.1.0, bu yeni `examples` alanını içeren en son sürüme (JSON Schema 2020-12) dayandırıldı.

Ve şimdi bu yeni `examples` alanı, artık kullanımdan kaldırılmış olan eski tekil (ve özel) `example` alanına göre öncelik alır.

JSON Schema'daki bu yeni `examples` alanı, OpenAPI'deki diğer yerlerde olduğu gibi (yukarıda açıklanan) ek meta verilerle birlikte bir dict değil, **sadece bir `list`** örneklerdir.

/// info

OpenAPI 3.1.0 bu yeni ve daha basit JSON Schema entegrasyonuyla yayınlandıktan sonra bile, bir süreliğine, otomatik belgeleri sağlayan araç olan Swagger UI, OpenAPI 3.1.0'ı desteklemedi (5.0.0 sürümünden beri destekliyor 🎉).

Bu nedenle, 0.99.0'dan önceki FastAPI sürümleri hala 3.1.0'dan düşük OpenAPI sürümlerini kullanıyordu.

///

### Pydantic ve FastAPI `examples`

Pydantic modelinin içine `examples` eklediğinizde, `schema_extra` veya `Field(examples=["something"])` kullanarak, bu örnek o Pydantic modelinin **JSON Schema**'sına eklenir.

Ve Pydantic modelinin bu **JSON Schema**'sı API'nizin **OpenAPI**'sine dahil edilir ve ardından belge arayüzünde kullanılır.

0.99.0'dan önceki FastAPI sürümlerinde (0.99.0 ve üzeri daha yeni OpenAPI 3.1.0 kullanır), diğer yardımcı araçlardan herhangi biriyle (`Query()`, `Body()`, vb.) `example` veya `examples` kullandığınızda, bu örnekler o veriyi tanımlayan JSON Schema'ya eklenmiyordu (OpenAPI'nin kendi JSON Schema sürümüne bile değil), doğrudan OpenAPI'deki *yol operasyonu* bildirimine ekleniyordu (JSON Schema kullanan OpenAPI bölümlerinin dışında).

Ancak şimdi FastAPI 0.99.0 ve üzeri JSON Schema 2020-12 kullanan OpenAPI 3.1.0'ı ve Swagger UI 5.0.0 ve üzerini kullandığından, her şey daha tutarlıdır ve örnekler JSON Schema'ya dahil edilmektedir.

### Swagger UI ve OpenAPI'ye özgü `examples`

Şimdi, Swagger UI birden fazla JSON Schema örneğini desteklemediğinden (2023-08-26 itibarıyla), kullanıcıların belgelerde birden fazla örnek gösterme yolu yoktu.

Bunu çözmek için, FastAPI `0.103.0` aynı eski **OpenAPI'ye özgü** `examples` alanını yeni `openapi_examples` parametresiyle bildirme **desteği ekledi**. 🤓

### Özet

Eskiden tarihi çok sevmediğimi söylerdim... ve şimdi bana bakın "teknoloji tarihi" dersleri veriyorum. 😅

Kısacası, **FastAPI 0.99.0 veya üzerine yükseltin**, işler çok daha **basit, tutarlı ve sezgisel** ve tüm bu tarihsel ayrıntıları bilmenize gerek yok. 😎
