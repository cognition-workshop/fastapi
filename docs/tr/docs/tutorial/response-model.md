# Yanıt Modeli - Dönüş Tipi

*Yol operasyonu fonksiyonunun* **dönüş tipini** açıklayarak yanıt için kullanılan tipi bildirebilirsiniz.

Fonksiyon **parametrelerindeki** giriş verileri için **tip açıklamalarını** kullandığınız gibi, Pydantic modelleri, listeler, sözlükler, tamsayılar, boolean'lar vb. gibi skaler değerler de kullanabilirsiniz.

{* ../../docs_src/response_model/tutorial001_01_py310.py hl[16,21] *}

FastAPI bu dönüş tipini şunlar için kullanacaktır:

* Döndürülen verileri **doğrulama**.
    * Veri geçersizse (örn. bir alan eksikse), bu *sizin* uygulama kodunuzun bozuk olduğu, olması gerekeni döndürmediği anlamına gelir ve yanlış veri döndürmek yerine bir sunucu hatası döndürür. Bu şekilde siz ve müşterileriniz beklenen veriyi ve veri şeklini alacağınızdan emin olabilirsiniz.
* Yanıt için OpenAPI *yol operasyonuna* bir **JSON Schema** ekleme.
    * Bu, **otomatik belgeler** tarafından kullanılacaktır.
    * Ayrıca otomatik istemci kodu oluşturma araçları tarafından da kullanılacaktır.

Ancak en önemlisi:

* Çıktı verilerini dönüş tipinde tanımlananlarla **sınırlama ve filtreleme**.
    * Bu özellikle **güvenlik** için önemlidir, aşağıda daha fazlasını göreceğiz.

## `response_model` Parametresi

Tipin bildirdiği şeyin tam olarak olmayan bazı verileri döndürmeniz veya döndürmek istemeniz gereken durumlar vardır.

Örneğin, bir **sözlük** veya veritabanı nesnesi **döndürmek** isteyebilir, ancak **onu bir Pydantic modeli olarak bildirebilirsiniz**. Bu şekilde Pydantic modeli, döndürdüğünüz nesne (örn. bir sözlük veya veritabanı nesnesi) için tüm veri belgelendirmesini, doğrulamayı vb. yapacaktır.

Dönüş tipi açıklamasını eklediyseniz, araçlar ve editörler fonksiyonunuzun bildirdiğinizden (örn. bir Pydantic modeli) farklı bir tip (örn. bir dict) döndürdüğünü söyleyen (doğru) bir hatayla şikayet edecektir.

Bu durumlarda, dönüş tipi yerine *yol operasyonu dekoratörü* parametresi `response_model` kullanabilirsiniz.

`response_model` parametresini herhangi bir *yol operasyonunda* kullanabilirsiniz:

* `@app.get()`
* `@app.post()`
* `@app.put()`
* `@app.delete()`
* vb.

{* ../../docs_src/response_model/tutorial001_py310.py hl[17,22,24:27] *}

/// note

`response_model`'in "dekoratör" metodunun (`get`, `post`, vb.) bir parametresi olduğuna dikkat edin. Tüm parametreler ve gövde gibi *yol operasyonu fonksiyonunuzun* değil.

///

`response_model`, bir Pydantic model alanı için bildireceğiniz aynı tipi alır, bu yüzden bir Pydantic modeli olabilir, ama aynı zamanda `List[Item]` gibi bir Pydantic modelleri `list`'i de olabilir.

FastAPI bu `response_model`'i tüm veri belgelendirmesi, doğrulama vb. için ve ayrıca **çıktı verilerini tip bildirimine dönüştürmek ve filtrelemek** için kullanacaktır.

/// tip

Editörünüzde, mypy vb.'de katı tip kontrolleri varsa, fonksiyon dönüş tipini `Any` olarak bildirebilirsiniz.

Bu şekilde editöre kasıtlı olarak herhangi bir şey döndürdüğünüzü söylersiniz. Ancak FastAPI yine de `response_model` ile veri belgelendirme, doğrulama, filtreleme vb. yapacaktır.

///

### `response_model` Önceliği

Hem bir dönüş tipi hem de bir `response_model` bildirirseniz, `response_model` öncelik alacak ve FastAPI tarafından kullanılacaktır.

Bu şekilde, yanıt modelinden farklı bir tip döndürürken bile fonksiyonlarınıza doğru tip açıklamaları ekleyebilirsiniz, editör ve mypy gibi araçlar tarafından kullanılmak üzere. Ve yine de FastAPI'nin `response_model` kullanarak veri doğrulama, belgelendirme vb. yapmasını sağlayabilirsiniz.

Ayrıca o *yol operasyonu* için bir yanıt modeli oluşturmayı devre dışı bırakmak için `response_model=None` kullanabilirsiniz, geçerli Pydantic alanları olmayan şeyler için tip açıklamaları ekliyorsanız buna ihtiyacınız olabilir, aşağıdaki bölümlerden birinde bunun bir örneğini göreceksiniz.

## Aynı giriş verisini döndürme

Burada bir `UserIn` modeli bildiriyoruz, düz metin şifre içerecektir:

{* ../../docs_src/response_model/tutorial002_py310.py hl[7,9] *}

/// info

`EmailStr` kullanmak için önce <a href="https://github.com/JoshData/python-email-validator" class="external-link" target="_blank">`email-validator`</a>'ı yükleyin.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden ve ardından yüklediğinizden emin olun, örneğin:

```console
$ pip install email-validator
```

veya:

```console
$ pip install "pydantic[email]"
```

///

Ve aynı modeli girişimizi ve çıkışımızı bildirmek için kullanıyoruz:

{* ../../docs_src/response_model/tutorial002_py310.py hl[16] *}

Şimdi, bir tarayıcı şifreyle bir kullanıcı oluşturduğunda, API aynı şifreyi yanıtta döndürecektir.

Bu durumda, sorun olmayabilir, çünkü şifreyi gönderen aynı kullanıcıdır.

Ancak aynı modeli başka bir *yol operasyonu* için kullanırsak, kullanıcılarımızın şifrelerini her istemciye gönderiyor olabiliriz.

/// danger

Bir kullanıcının düz şifresini asla saklamayın veya bunun gibi bir yanıtta göndermeyin, tüm uyarıları bilmediğiniz ve ne yaptığınızı bilmediğiniz sürece.

///

## Çıktı modeli ekleme

Bunun yerine düz metin şifreli bir giriş modeli ve onsuz bir çıktı modeli oluşturabiliriz:

{* ../../docs_src/response_model/tutorial003_py310.py hl[9,11,16] *}

Burada, *yol operasyonu fonksiyonumuz* şifreyi içeren aynı giriş kullanıcısını döndürse de:

{* ../../docs_src/response_model/tutorial003_py310.py hl[24] *}

...`response_model`'i şifreyi içermeyen `UserOut` modelimiz olarak bildirdik:

{* ../../docs_src/response_model/tutorial003_py310.py hl[22] *}

Bu yüzden, **FastAPI** çıktı modelinde bildirilmeyen tüm verileri filtrelemeye özen gösterecektir (Pydantic kullanarak).

### `response_model` veya Dönüş Tipi

Bu durumda, iki model farklı olduğundan, fonksiyon dönüş tipini `UserOut` olarak açıklasaydık, editör ve araçlar farklı sınıflar olduğundan geçersiz bir tip döndürdüğümüzü söyleyen bir şikayette bulunurdu.

Bu yüzden bu örnekte `response_model` parametresinde bildirmemiz gerekiyor.

...ama bunu nasıl aşacağınızı görmek için aşağıyı okumaya devam edin.

## Dönüş Tipi ve Veri Filtreleme

Önceki örnekten devam edelim. Fonksiyonu **bir tiple açıklamak** istiyorduk, ancak fonksiyondan aslında **daha fazla veri** içeren bir şey döndürebilmek istiyorduk.

FastAPI'nin yanıt modelini kullanarak verileri **filtrelemeye** devam etmesini istiyoruz. Böylece fonksiyon daha fazla veri döndürse bile, yanıt yalnızca yanıt modelinde bildirilen alanları içerecektir.

Önceki örnekte, sınıflar farklı olduğundan, `response_model` parametresini kullanmak zorundaydık. Ama bu da editör ve araçların fonksiyon dönüş tipini kontrol etme desteğini alamadığımız anlamına gelir.

Ancak buna benzer bir şey yapmamız gereken çoğu durumda, modelin bu örnekteki gibi sadece bazı verileri **filtrelemesini/kaldırmasını** istiyoruz.

Ve bu durumlarda, editör ve araçlarda daha iyi destek almak için fonksiyon **tip açıklamalarından** yararlanmak üzere sınıfları ve kalıtımı kullanabilir, ve yine de FastAPI **veri filtrelemesini** elde edebiliriz.

{* ../../docs_src/response_model/tutorial003_01_py310.py hl[7:10,13:14,18] *}

Bununla, editörlerden ve mypy'den araç desteği alırız çünkü bu kod tipler açısından doğrudur, ama aynı zamanda FastAPI'den veri filtrelemesi de alırız.

Bu nasıl çalışıyor? Bunu kontrol edelim. 🤓

### Tip Açıklamaları ve Araçlar

Önce editörlerin, mypy'nin ve diğer araçların bunu nasıl göreceğine bakalım.

`BaseUser` temel alanlara sahiptir. Ardından `UserIn`, `BaseUser`'dan miras alır ve `password` alanını ekler, böylece her iki modelden tüm alanları içerecektir.

Fonksiyon dönüş tipini `BaseUser` olarak açıklıyoruz, ancak aslında bir `UserIn` örneği döndürüyoruz.

Editör, mypy ve diğer araçlar bundan şikayet etmeyecektir çünkü, tipleme açısından, `UserIn`, `BaseUser`'ın bir alt sınıfıdır, bu da beklenen `BaseUser` olan herhangi bir şey olduğunda *geçerli* bir tip olduğu anlamına gelir.

### FastAPI Veri Filtreleme

Şimdi, FastAPI için dönüş tipini görecek ve döndürdüğünüz şeyin **yalnızca** tipte bildirilen alanları içerdiğinden emin olacaktır.

FastAPI, Pydantic ile dahili olarak birkaç şey yaparak sınıf kalıtımının aynı kurallarının döndürülen veri filtrelemesi için kullanılmamasını sağlar, aksi takdirde beklediğinizden çok daha fazla veri döndürebilirsiniz.

Bu şekilde, her iki dünyanın da en iyisini elde edebilirsiniz: **araç desteği** ile tip açıklamaları ve **veri filtreleme**.

## Belgelerde görün

Otomatik belgeleri gördüğünüzde, giriş modeli ve çıktı modelinin her ikisinin de kendi JSON Schema'sına sahip olduğunu kontrol edebilirsiniz:

<img src="/img/tutorial/response-model/image01.png">

Ve her iki model de etkileşimli API belgeleri için kullanılacaktır:

<img src="/img/tutorial/response-model/image02.png">

## Diğer Dönüş Tipi Açıklamaları

Geçerli bir Pydantic tipi olmayan bir şey döndürdüğünüz ve bunu fonksiyonda yalnızca araçların (editör, mypy, vb.) sağladığı desteği almak için açıkladığınız durumlar olabilir.

### Doğrudan Yanıt Döndürme

En yaygın durum [ileri düzey belgelerde daha sonra açıklandığı gibi doğrudan bir Yanıt döndürmek](../advanced/response-directly.md){.internal-link target=_blank} olacaktır.

{* ../../docs_src/response_model/tutorial003_02.py hl[8,10:11] *}

Bu basit durum FastAPI tarafından otomatik olarak ele alınır çünkü dönüş tipi açıklaması `Response` sınıfıdır (veya onun bir alt sınıfı).

Ve araçlar da mutlu olacaktır çünkü hem `RedirectResponse` hem de `JSONResponse`, `Response`'un alt sınıflarıdır, yani tip açıklaması doğrudur.

### Bir Yanıt Alt Sınıfını Açıklama

Tip açıklamasında `Response`'un bir alt sınıfını da kullanabilirsiniz:

{* ../../docs_src/response_model/tutorial003_03.py hl[8:9] *}

Bu da çalışacaktır çünkü `RedirectResponse`, `Response`'un bir alt sınıfıdır ve FastAPI bu basit durumu otomatik olarak ele alacaktır.

### Geçersiz Dönüş Tipi Açıklamaları

Ancak geçerli bir Pydantic tipi olmayan (örn. bir veritabanı nesnesi) başka bir rastgele nesne döndürdüğünüzde ve bunu fonksiyonda bu şekilde açıkladığınızda, FastAPI o tip açıklamasından bir Pydantic yanıt modeli oluşturmaya çalışacak ve başarısız olacaktır.

Aynı şey, bir veya daha fazlası geçerli Pydantic tipleri olmayan farklı tipler arasında bir <abbr title='Birden fazla tip arasında birleşim "bu tiplerden herhangi biri" anlamına gelir.'>birleşim</abbr> varsa da olur, örneğin bu başarısız olur 💥:

{* ../../docs_src/response_model/tutorial003_04_py310.py hl[8] *}

...bu başarısız olur çünkü tip açıklaması bir Pydantic tipi değildir ve sadece tek bir `Response` sınıfı veya alt sınıfı değildir, bir `Response` ve bir `dict` arasında bir birleşimdir (ikisinden herhangi biri).

### Yanıt Modelini Devre Dışı Bırakma

Yukarıdaki örnekten devam ederek, FastAPI tarafından gerçekleştirilen varsayılan veri doğrulama, belgelendirme, filtreleme vb.'yi istemeyebilirsiniz.

Ancak editörler ve tip denetleyiciler (örn. mypy) gibi araçlardan destek almak için fonksiyonda dönüş tipi açıklamasını tutmak isteyebilirsiniz.

Bu durumda, `response_model=None` ayarlayarak yanıt modeli oluşturmayı devre dışı bırakabilirsiniz:

{* ../../docs_src/response_model/tutorial003_05_py310.py hl[7] *}

Bu, FastAPI'nin yanıt modeli oluşturmayı atlamasını sağlayacak ve bu şekilde FastAPI uygulamanızı etkilemeden ihtiyacınız olan herhangi bir dönüş tipi açıklamasına sahip olabilirsiniz. 🤓

## Yanıt Modeli kodlama parametreleri

Yanıt modeliniz varsayılan değerlere sahip olabilir, örneğin:

{* ../../docs_src/response_model/tutorial004_py310.py hl[9,11:12] *}

* `description: Union[str, None] = None` (veya Python 3.10'da `str | None = None`) varsayılanı `None`'dır.
* `tax: float = 10.5` varsayılanı `10.5`'tir.
* `tags: List[str] = []` varsayılanı boş bir liste: `[]`'dir.

ancak gerçekte saklanmadılarsa onları sonuçtan çıkarmak isteyebilirsiniz.

Örneğin, bir NoSQL veritabanında birçok isteğe bağlı özelliğe sahip modelleriniz varsa, ancak varsayılan değerlerle dolu çok uzun JSON yanıtları göndermek istemiyorsanız.

### `response_model_exclude_unset` parametresini kullanın

*Yol operasyonu dekoratörü* parametresini `response_model_exclude_unset=True` olarak ayarlayabilirsiniz:

{* ../../docs_src/response_model/tutorial004_py310.py hl[22] *}

ve bu varsayılan değerler yanıta dahil edilmeyecek, yalnızca gerçekten ayarlanan değerler dahil edilecektir.

Bu yüzden, `foo` ID'sine sahip öğe için o *yol operasyonuna* bir istek gönderirseniz, yanıt (varsayılan değerleri içermeyen) şöyle olacaktır:

```JSON
{
    "name": "Foo",
    "price": 50.2
}
```

/// info

Pydantic v1'de metot `.dict()` olarak adlandırılıyordu, Pydantic v2'de kullanımdan kaldırıldı (ancak hala destekleniyor) ve `.model_dump()` olarak yeniden adlandırıldı.

Buradaki örnekler Pydantic v1 ile uyumluluk için `.dict()` kullanıyor, ancak Pydantic v2 kullanabiliyorsanız bunun yerine `.model_dump()` kullanmalısınız.

///

/// info

FastAPI bunu başarmak için Pydantic modelinin `.dict()`'ini <a href="https://docs.pydantic.dev/1.10/usage/exporting_models/#modeldict" class="external-link" target="_blank">`exclude_unset` parametresiyle</a> kullanır.

///

/// info

Ayrıca şunları da kullanabilirsiniz:

* `response_model_exclude_defaults=True`
* `response_model_exclude_none=True`

<a href="https://docs.pydantic.dev/1.10/usage/exporting_models/#modeldict" class="external-link" target="_blank">Pydantic belgelerinde</a> `exclude_defaults` ve `exclude_none` için açıklandığı gibi.

///

#### Varsayılan değerlere sahip alanlar için değerli veriler

Ancak verileriniz modelin varsayılan değerlere sahip alanları için değerler içeriyorsa, `bar` ID'sine sahip öğe gibi:

```Python hl_lines="3  5"
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}
```

bunlar yanıta dahil edilecektir.

#### Varsayılanlarla aynı değerlere sahip veriler

Veriler varsayılanlarla aynı değerlere sahipse, `baz` ID'sine sahip öğe gibi:

```Python hl_lines="3  5-6"
{
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}
```

FastAPI yeterince akıllıdır (aslında Pydantic yeterince akıllıdır) `description`, `tax` ve `tags`'in varsayılanlarla aynı değerlere sahip olmasına rağmen, bunların açıkça ayarlandığını (varsayılanlardan alınmak yerine) fark eder.

Bu yüzden, JSON yanıtına dahil edileceklerdir.

/// tip

Varsayılan değerlerin yalnızca `None` değil, herhangi bir şey olabileceğine dikkat edin.

Bir liste (`[]`), `10.5`'lik bir `float` vb. olabilirler.

///

### `response_model_include` ve `response_model_exclude`

*Yol operasyonu dekoratörü* parametreleri `response_model_include` ve `response_model_exclude`'u da kullanabilirsiniz.

Dahil edilecek (geri kalanını atlayarak) veya hariç tutulacak (geri kalanını dahil ederek) özelliklerin adlarını içeren bir `str` `set`'i alırlar.

Yalnızca bir Pydantic modeliniz varsa ve çıktıdan bazı verileri kaldırmak istiyorsanız, bu hızlı bir kısayol olarak kullanılabilir.

/// tip

Ancak bu parametreler yerine, yukarıdaki fikirleri, birden fazla sınıf kullanarak kullanmanız hala önerilir.

Bunun nedeni, `response_model_include` veya `response_model_exclude` kullanarak bazı özellikleri atlasanız bile, uygulamanızın OpenAPI'sinde (ve belgelerde) oluşturulan JSON Schema'nın yine de tam model için olacağıdır.

Bu, benzer şekilde çalışan `response_model_by_alias` için de geçerlidir.

///

{* ../../docs_src/response_model/tutorial005_py310.py hl[29,35] *}

/// tip

`{"name", "description"}` sözdizimi bu iki değerle bir `set` oluşturur.

`set(["name", "description"])` ile eşdeğerdir.

///

#### `set`'ler yerine `list`'ler kullanma

Bir `set` kullanmayı unutur ve bunun yerine bir `list` veya `tuple` kullanırsanız, FastAPI yine de onu bir `set`'e dönüştürecek ve doğru şekilde çalışacaktır:

{* ../../docs_src/response_model/tutorial006_py310.py hl[29,35] *}

## Özet

Yanıt modellerini tanımlamak ve özellikle özel verilerin filtrelenmesini sağlamak için *yol operasyonu dekoratörünün* `response_model` parametresini kullanın.

Yalnızca açıkça ayarlanan değerleri döndürmek için `response_model_exclude_unset` kullanın.
