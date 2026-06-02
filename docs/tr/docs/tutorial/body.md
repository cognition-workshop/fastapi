# İstek Gövdesi

Bir istemciden (örneğin bir tarayıcıdan) API'nize veri göndermeniz gerektiğinde, bunu **istek gövdesi** olarak gönderirsiniz.

Bir **istek** gövdesi, istemci tarafından API'nize gönderilen veridir. Bir **yanıt** gövdesi ise API'nizin istemciye gönderdiği veridir.

API'niz neredeyse her zaman bir **yanıt** gövdesi göndermek zorundadır. Ancak istemcilerin her zaman **istek gövdesi** göndermesi gerekmez, bazen sadece bir yol ve belki bazı sorgu parametreleri ile istek yaparlar, ancak gövde göndermezler.

Bir **istek** gövdesi bildirmek için, tüm güçleri ve avantajlarıyla <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> modellerini kullanırsınız.

/// info

Veri göndermek için şunlardan birini kullanmalısınız: `POST` (en yaygın olanı), `PUT`, `DELETE` veya `PATCH`.

Bir `GET` isteği ile gövde göndermek, spesifikasyonlarda tanımsız bir davranışa sahiptir, yine de FastAPI tarafından yalnızca çok karmaşık/uç durumlar için desteklenir.

Önerilmediği için, Swagger UI ile etkileşimli belgeler `GET` kullanırken gövde için belgelendirme göstermez ve aradaki proxy'ler bunu desteklemeyebilir.

///

## Pydantic'in `BaseModel`'ini içe aktarın

Öncelikle, `pydantic`'ten `BaseModel`'i içe aktarmanız gerekir:

{* ../../docs_src/body/tutorial001_py310.py hl[2] *}

## Veri modelinizi oluşturun

Ardından veri modelinizi `BaseModel`'den miras alan bir sınıf olarak bildirirsiniz.

Tüm nitelikler için standart Python tiplerini kullanın:

{* ../../docs_src/body/tutorial001_py310.py hl[5:9] *}


Sorgu parametreleri bildirirken olduğu gibi, bir model niteliğinin varsayılan değeri varsa zorunlu değildir. Aksi takdirde zorunludur. Sadece isteğe bağlı yapmak için `None` kullanın.

Örneğin, yukarıdaki model şöyle bir JSON "`object`" (veya Python `dict`) bildirir:

```JSON
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

...`description` ve `tax` isteğe bağlı olduğundan (varsayılan değeri `None` ile), bu JSON "`object`" de geçerli olacaktır:

```JSON
{
    "name": "Foo",
    "price": 45.2
}
```

## Parametre olarak bildirin

*Yol operasyonunuza* eklemek için, yol ve sorgu parametrelerini bildirdiğiniz şekilde bildirin:

{* ../../docs_src/body/tutorial001_py310.py hl[16] *}

...ve tipini oluşturduğunuz model olan `Item` olarak bildirin.

## Sonuçlar

Sadece bu Python tip bildirimi ile **FastAPI** şunları yapacaktır:

* İsteğin gövdesini JSON olarak okur.
* İlgili tipleri dönüştürür (gerekirse).
* Veriyi doğrular.
    * Veri geçersizse, tam olarak nerede ve ne yanlış olduğunu gösteren güzel ve net bir hata döndürür.
* Alınan veriyi `item` parametresinde size verir.
    * Fonksiyonda `Item` tipinde olarak bildirdiğiniz için, tüm nitelikler ve tipleri için tüm editör desteğine (tamamlama vb.) de sahip olursunuz.
* Modeliniz için <a href="https://json-schema.org" class="external-link" target="_blank">JSON Schema</a> tanımları üretir, projeniz için mantıklıysa bunları başka yerlerde de kullanabilirsiniz.
* Bu şemalar üretilen OpenAPI şemasının bir parçası olacak ve otomatik belgelendirme <abbr title="Kullanıcı Arayüzleri">UI</abbr>'ları tarafından kullanılacaktır.

## Otomatik belgeler

Modellerinizin JSON Şemaları, OpenAPI tarafından üretilen şemanızın bir parçası olacak ve etkileşimli API belgelerinde gösterilecektir:

<img src="/img/tutorial/body/image01.png">

Ve ayrıca bunlara ihtiyaç duyan her *yol operasyonu* içindeki API belgelerinde de kullanılacaktır:

<img src="/img/tutorial/body/image02.png">

## Editör desteği

Editörünüzde, fonksiyonunuz içinde her yerde tip ipuçları ve tamamlama alırsınız (Pydantic modeli yerine bir `dict` alsaydınız bu olmazdı):

<img src="/img/tutorial/body/image03.png">

Ayrıca yanlış tip işlemleri için hata kontrolleri de alırsınız:

<img src="/img/tutorial/body/image04.png">

Bu tesadüf değildir, tüm framework bu tasarım etrafında inşa edilmiştir.

Ve herhangi bir uygulamadan önce, tasarım aşamasında tüm editörlerle çalışacağından emin olmak için kapsamlı şekilde test edilmiştir.

Bunu desteklemek için Pydantic'in kendisinde bile bazı değişiklikler yapılmıştır.

Önceki ekran görüntüleri <a href="https://code.visualstudio.com" class="external-link" target="_blank">Visual Studio Code</a> ile alınmıştır.

Ancak <a href="https://www.jetbrains.com/pycharm/" class="external-link" target="_blank">PyCharm</a> ve diğer Python editörlerinin çoğuyla da aynı editör desteğini alırsınız:

<img src="/img/tutorial/body/image05.png">

/// tip

Editörünüz olarak <a href="https://www.jetbrains.com/pycharm/" class="external-link" target="_blank">PyCharm</a> kullanıyorsanız, <a href="https://github.com/koxudaxi/pydantic-pycharm-plugin/" class="external-link" target="_blank">Pydantic PyCharm Eklentisi</a>'ni kullanabilirsiniz.

Pydantic modelleri için editör desteğini iyileştirir:

* otomatik tamamlama
* tip kontrolleri
* yeniden düzenleme
* arama
* denetimler

///

## Modeli kullanın

Fonksiyon içinde, model nesnesinin tüm niteliklerine doğrudan erişebilirsiniz:

{* ../../docs_src/body/tutorial002_py310.py *}

## İstek gövdesi + yol parametreleri

Yol parametrelerini ve istek gövdesini aynı anda bildirebilirsiniz.

**FastAPI**, yol parametreleriyle eşleşen fonksiyon parametrelerinin **yoldan alınması** gerektiğini ve Pydantic modeli olarak bildirilen fonksiyon parametrelerinin **istek gövdesinden alınması** gerektiğini anlayacaktır.

{* ../../docs_src/body/tutorial003_py310.py hl[15:16] *}


## İstek gövdesi + yol + sorgu parametreleri

Ayrıca **gövde**, **yol** ve **sorgu** parametrelerini aynı anda bildirebilirsiniz.

**FastAPI** her birini tanıyacak ve veriyi doğru yerden alacaktır.

{* ../../docs_src/body/tutorial004_py310.py hl[16] *}

Fonksiyon parametreleri şu şekilde tanınacaktır:

* Parametre aynı zamanda **yolda** bildirilmişse, yol parametresi olarak kullanılacaktır.
* Parametre **tekil bir tipte** ise (`int`, `float`, `str`, `bool` vb. gibi) **sorgu** parametresi olarak yorumlanacaktır.
* Parametre bir **Pydantic modeli** tipinde bildirilmişse, istek **gövdesi** olarak yorumlanacaktır.

/// note

FastAPI, `= None` varsayılan değeri nedeniyle `q` değerinin zorunlu olmadığını bilecektir.

`str | None` (Python 3.10+) veya `Union[str, None]` (Python 3.8+) içindeki `Union`, FastAPI tarafından değerin zorunlu olmadığını belirlemek için kullanılmaz, `= None` varsayılan değerine sahip olduğu için zorunlu olmadığını bilir.

Ancak tip açıklamalarını eklemek, editörünüzün size daha iyi destek vermesini ve hataları tespit etmesini sağlayacaktır.

///

## Pydantic olmadan

Pydantic modelleri kullanmak istemiyorsanız, **Body** parametrelerini de kullanabilirsiniz. Belgeler için bakın: [Gövde - Birden Fazla Parametre: Gövdede tekil değerler](body-multiple-params.md#govdede-tekil-degerler){.internal-link target=_blank}.
