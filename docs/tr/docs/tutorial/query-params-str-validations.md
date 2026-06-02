# Sorgu Parametreleri ve String Doğrulamaları

**FastAPI**, parametreleriniz için ek bilgi ve doğrulama bildirmenize olanak tanır.

Bu uygulamayı örnek olarak alalım:

{* ../../docs_src/query_params_str_validations/tutorial001_py310.py hl[7] *}

Sorgu parametresi `q`, `str | None` tipindedir, bu da `str` tipinde olduğu ancak `None` da olabileceği anlamına gelir ve varsayılan değeri `None`'dır, bu yüzden FastAPI bunun gerekli olmadığını bilecektir.

/// note

FastAPI, `= None` varsayılan değeri nedeniyle `q` değerinin gerekli olmadığını bilecektir.

`str | None` kullanmak, editörünüzün size daha iyi destek vermesine ve hataları tespit etmesine olanak tanır.

///

## Ek doğrulama

`q` isteğe bağlı olsa bile, sağlandığında **uzunluğunun 50 karakteri aşmamasını** zorunlu kılacağız.

### `Query` ve `Annotated`'ı içe aktarın

Bunu başarmak için önce şunları içe aktarın:

* `fastapi`'den `Query`
* `typing`'den `Annotated`

{* ../../docs_src/query_params_str_validations/tutorial002_an_py310.py hl[1,3] *}

/// info

FastAPI, 0.95.0 sürümünde `Annotated` desteği ekledi (ve önermeye başladı).

Eski bir sürümünüz varsa, `Annotated` kullanmaya çalışırken hatalar alırsınız.

`Annotated` kullanmadan önce [FastAPI sürümünü](../deployment/versions.md#upgrading-the-fastapi-versions){.internal-link target=_blank} en az 0.95.1'e yükselttiğinizden emin olun.

///

## `q` parametresinin tipinde `Annotated` kullanın

Daha önce [Python Tipleri Giriş](../python-types.md#type-hints-with-metadata-annotations){.internal-link target=_blank} bölümünde `Annotated`'ın parametrelerinize meta veri eklemek için kullanılabileceğini söylediğimi hatırlıyor musunuz?

Şimdi onu FastAPI ile kullanma zamanı. 🚀

Bu tip açıklamamız vardı:

//// tab | Python 3.10+

```Python
q: str | None = None
```

////

//// tab | Python 3.8+

```Python
q: Union[str, None] = None
```

////

Yapacağımız şey bunu `Annotated` ile sarmak, böylece şöyle olur:

//// tab | Python 3.10+

```Python
q: Annotated[str | None] = None
```

////

//// tab | Python 3.8+

```Python
q: Annotated[Union[str, None]] = None
```

////

Her iki sürüm de aynı anlama gelir, `q` bir `str` veya `None` olabilen bir parametredir ve varsayılan olarak `None`'dır.

Şimdi eğlenceli kısıma geçelim. 🎉

## `q` parametresinde `Annotated`'a `Query` ekleyin

Artık daha fazla bilgi koyabileceğimiz (bu durumda bazı ek doğrulamalar) bu `Annotated`'a sahip olduğumuza göre, `Annotated` içine `Query` ekleyin ve `max_length` parametresini `50` olarak ayarlayın:

{* ../../docs_src/query_params_str_validations/tutorial002_an_py310.py hl[9] *}

Varsayılan değerin hala `None` olduğuna dikkat edin, bu yüzden parametre hala isteğe bağlıdır.

Ancak şimdi, `Annotated` içinde `Query(max_length=50)` olmasıyla, FastAPI'ye bu değer için **ek doğrulama** istediğimizi, maksimum 50 karakter olmasını istediğimizi söylüyoruz. 😎

/// tip

Burada `Query()` kullanıyoruz çünkü bu bir **sorgu parametresi**. Daha sonra `Path()`, `Body()`, `Header()` ve `Cookie()` gibi diğerlerini göreceğiz, bunlar da `Query()` ile aynı argümanları kabul eder.

///

FastAPI şimdi şunları yapacaktır:

* Verileri **doğrulama** yaparak maksimum uzunluğun 50 karakter olduğundan emin olma
* Veri geçerli olmadığında istemci için **net bir hata** gösterme
* Parametreyi OpenAPI şeması *yol operasyonunda* **belgeleme** (böylece **otomatik belge arayüzünde** görünecektir)

## Alternatif (eski): Varsayılan değer olarak `Query`

FastAPI'nin önceki sürümleri (<abbr title="2023-03'ten önce">0.95.0'dan önce</abbr>) `Annotated`'a koymak yerine `Query`'yi parametrenizin varsayılan değeri olarak kullanmanızı gerektiriyordu, bunu kullanan kod göreceksiniz, bu yüzden size açıklayacağım.

/// tip

Yeni kod ve mümkün olduğunda, yukarıda açıklandığı gibi `Annotated` kullanın. Birden fazla avantajı vardır (aşağıda açıklanmıştır) ve dezavantajı yoktur. 🍰

///

`Query()` fonksiyon parametrenizin varsayılan değeri olarak nasıl kullanacağınız, `max_length` parametresini `50` olarak ayarlayarak:

{* ../../docs_src/query_params_str_validations/tutorial002_py310.py hl[7] *}

Bu durumda (`Annotated` kullanmadan) fonksiyondaki varsayılan `None` değerini `Query()` ile değiştirmemiz gerektiğinden, şimdi varsayılan değeri `Query(default=None)` parametresiyle ayarlamamız gerekiyor, bu da aynı varsayılan değeri tanımlama amacına hizmet eder (en azından FastAPI için).

Yani:

```Python
q: str | None = Query(default=None)
```

...parametreyi isteğe bağlı yapar, varsayılan değeri `None` ile, aynı şekilde:

```Python
q: str | None = None
```

Ancak `Query` sürümü bunu açıkça bir sorgu parametresi olarak bildirir.

Ardından, `Query`'ye daha fazla parametre iletebiliriz. Bu durumda, stringlere uygulanan `max_length` parametresi:

```Python
q: str | None = Query(default=None, max_length=50)
```

Bu, verileri doğrulayacak, veri geçerli olmadığında net bir hata gösterecek ve parametreyi OpenAPI şeması *yol operasyonunda* belgeleyecektir.

### Varsayılan değer olarak `Query` veya `Annotated` içinde

`Annotated` içinde `Query` kullanırken `Query`'nin `default` parametresini kullanamayacağınızı unutmayın.

Bunun yerine, fonksiyon parametresinin gerçek varsayılan değerini kullanın. Aksi takdirde tutarsız olurdu.

Örneğin, buna izin verilmez:

```Python
q: Annotated[str, Query(default="rick")] = "morty"
```

...çünkü varsayılan değerin `"rick"` mi yoksa `"morty"` mi olması gerektiği belli değildir.

Bu yüzden, şunu kullanırsınız (tercihen):

```Python
q: Annotated[str, Query()] = "rick"
```

...veya eski kod tabanlarında şunu bulacaksınız:

```Python
q: str = Query(default="rick")
```

### `Annotated`'ın avantajları

Fonksiyon parametrelerindeki varsayılan değer yerine **`Annotated` kullanılması önerilir**, birden fazla nedenden dolayı **daha iyidir**. 🤓

**Fonksiyon parametresinin** **varsayılan** değeri **gerçek varsayılan** değerdir, bu genel olarak Python ile daha sezgiseldir. 😌

Aynı fonksiyonu FastAPI olmadan **başka yerlerde** **çağırabilirsiniz** ve **beklendiği gibi çalışacaktır**. **Gerekli** bir parametre varsa (varsayılan değeri olmayan), **editörünüz** size bir hatayla bildirecektir, **Python** da gerekli parametreyi iletmeden çalıştırırsanız şikayet edecektir.

`Annotated` kullanmadığınızda ve bunun yerine **(eski) varsayılan değer stili** kullandığınızda, o fonksiyonu FastAPI olmadan **başka yerlerde** çağırırsanız, doğru çalışması için fonksiyona argümanları iletmeyi **hatırlamanız** gerekir, aksi takdirde değerler beklediğinizden farklı olacaktır (örn. `str` yerine `QueryInfo` veya benzeri bir şey). Ve editörünüz şikayet etmeyecek, Python da o fonksiyonu çalıştırırken şikayet etmeyecek, yalnızca içindeki işlemler hata verdiğinde.

`Annotated` birden fazla meta veri açıklamasına sahip olabildiğinden, artık aynı fonksiyonu <a href="https://typer.tiangolo.com/" class="external-link" target="_blank">Typer</a> gibi diğer araçlarla bile kullanabilirsiniz. 🚀

## Daha fazla doğrulama ekleme

Bir `min_length` parametresi de ekleyebilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial003_an_py310.py hl[10] *}

## Düzenli ifadeler ekleme

Parametrenin eşleşmesi gereken bir <abbr title="Düzenli ifade, regex veya regexp, stringler için bir arama deseni tanımlayan bir karakter dizisidir.">düzenli ifade</abbr> `pattern` tanımlayabilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial004_an_py310.py hl[11] *}

Bu özel düzenli ifade deseni, alınan parametre değerinin şu şekilde olduğunu kontrol eder:

* `^`: aşağıdaki karakterlerle başlar, önünde karakter yoktur.
* `fixedquery`: tam olarak `fixedquery` değerine sahiptir.
* `$`: burada biter, `fixedquery`'den sonra başka karakter yoktur.

Tüm bu **"düzenli ifade"** fikirleriyle kaybolduğunuzu hissediyorsanız endişelenmeyin. Bunlar birçok kişi için zor bir konudur. Henüz düzenli ifadelere ihtiyaç duymadan birçok şey yapabilirsiniz.

Artık ihtiyaç duyduğunuzda bunları **FastAPI**'de kullanabileceğinizi biliyorsunuz.

### Pydantic v1'de `pattern` yerine `regex`

Pydantic sürüm 2 ve FastAPI 0.100.0'dan önce, parametre `pattern` yerine `regex` olarak adlandırılıyordu, ancak artık kullanımdan kaldırılmıştır.

Hala onu kullanan kod görebilirsiniz:

//// tab | Pydantic v1

{* ../../docs_src/query_params_str_validations/tutorial004_regex_an_py310.py hl[11] *}

////

Ancak bunun kullanımdan kaldırıldığını ve yeni `pattern` parametresini kullanmak üzere güncellenmesi gerektiğini bilin. 🤓

## Varsayılan değerler

Elbette, `None` dışında varsayılan değerler de kullanabilirsiniz.

Diyelim ki `q` sorgu parametresini `min_length` `3` ile ve varsayılan değeri `"fixedquery"` olarak bildirmek istiyorsunuz:

{* ../../docs_src/query_params_str_validations/tutorial005_an_py39.py hl[9] *}

/// note

`None` dahil herhangi bir tipte varsayılan değere sahip olmak, parametreyi isteğe bağlı (gerekli değil) yapar.

///

## Gerekli parametreler

Daha fazla doğrulama veya meta veri bildirmemiz gerekmediğinde, `q` sorgu parametresini yalnızca varsayılan değer bildirmeyerek gerekli yapabiliriz:

```Python
q: str
```

yerine:

```Python
q: str | None = None
```

Ancak şimdi onu `Query` ile bildiriyoruz, örneğin:

//// tab | Annotated

```Python
q: Annotated[str | None, Query(min_length=3)] = None
```

////

Bu yüzden, `Query` kullanırken bir değeri gerekli olarak bildirmeniz gerektiğinde, varsayılan değer bildirmeyebilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial006_an_py39.py hl[9] *}

### Gerekli, `None` olabilir

Bir parametrenin `None` kabul edebileceğini, ancak yine de gerekli olduğunu bildirebilirsiniz. Bu, istemcileri bir değer göndermeye zorlar, değer `None` olsa bile.

Bunu yapmak için, `None`'ın geçerli bir tip olduğunu bildirebilir ancak varsayılan değer bildirmeyebilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial006c_an_py310.py hl[9] *}

## Sorgu parametresi listesi / birden fazla değer

Bir sorgu parametresini `Query` ile açıkça tanımladığınızda, onu bir değer listesi almak üzere, başka bir deyişle birden fazla değer almak üzere de bildirebilirsiniz.

Örneğin, URL'de birden fazla kez görünebilecek bir `q` sorgu parametresi bildirmek için:

{* ../../docs_src/query_params_str_validations/tutorial011_an_py310.py hl[9] *}

Ardından, şöyle bir URL ile:

```
http://localhost:8000/items/?q=foo&q=bar
```

birden fazla `q` *sorgu parametrelerinin* değerlerini (`foo` ve `bar`) *yol operasyonu fonksiyonunuzun* içinde, *fonksiyon parametresi* `q`'da bir Python `list` içinde alırsınız.

Bu URL'ye yanıt şöyle olacaktır:

```JSON
{
  "q": [
    "foo",
    "bar"
  ]
}
```

/// tip

`list` tipinde bir sorgu parametresi bildirmek için, yukarıdaki örnekteki gibi, açıkça `Query` kullanmanız gerekir, aksi takdirde bir istek gövdesi olarak yorumlanır.

///

Etkileşimli API belgeleri buna göre güncellenerek birden fazla değere izin verecektir:

<img src="/img/tutorial/query-params-str-validations/image02.png">

### Varsayılanlarla sorgu parametresi listesi / birden fazla değer

Hiçbiri sağlanmadığında varsayılan bir `list` değeri de tanımlayabilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial012_an_py39.py hl[9] *}

Şuraya giderseniz:

```
http://localhost:8000/items/
```

`q`'nun varsayılanı: `["foo", "bar"]` olacak ve yanıtınız şöyle olacaktır:

```JSON
{
  "q": [
    "foo",
    "bar"
  ]
}
```

#### Sadece `list` kullanma

`list[str]` yerine doğrudan `list` de kullanabilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial013_an_py39.py hl[9] *}

/// note

Bu durumda FastAPI'nin listenin içeriğini kontrol etmeyeceğini unutmayın.

Örneğin, `list[int]` listenin içeriğinin tamsayı olduğunu kontrol eder (ve belgeler). Ancak tek başına `list` kontrol etmez.

///

## Daha fazla meta veri bildirme

Parametre hakkında daha fazla bilgi ekleyebilirsiniz.

Bu bilgi, oluşturulan OpenAPI'ye dahil edilecek ve belge kullanıcı arayüzleri ve harici araçlar tarafından kullanılacaktır.

/// note

Farklı araçların farklı düzeylerde OpenAPI desteğine sahip olabileceğini unutmayın.

Bazıları henüz bildirilen tüm ek bilgileri göstermeyebilir, ancak çoğu durumda eksik özellik zaten geliştirme için planlanmıştır.

///

Bir `title` ekleyebilirsiniz:

{* ../../docs_src/query_params_str_validations/tutorial007_an_py310.py hl[10] *}

Ve bir `description`:

{* ../../docs_src/query_params_str_validations/tutorial008_an_py310.py hl[14] *}

## Takma ad parametreleri

Parametrenin `item-query` olmasını istediğinizi düşünün.

Şöyle:

```
http://127.0.0.1:8000/items/?item-query=foobaritems
```

Ancak `item-query` geçerli bir Python değişken adı değildir.

En yakını `item_query` olurdu.

Ama yine de tam olarak `item-query` olmasına ihtiyacınız var...

O zaman bir `alias` bildirebilirsiniz ve bu takma ad parametre değerini bulmak için kullanılacaktır:

{* ../../docs_src/query_params_str_validations/tutorial009_an_py310.py hl[9] *}

## Parametreleri kullanımdan kaldırma

Şimdi diyelim ki bu parametreyi artık beğenmiyorsunuz.

Onu kullanan istemciler olduğu için bir süre orada bırakmanız gerekiyor, ancak belgelerin onu açıkça <abbr title="eskimiş, kullanılması önerilmeyen">kullanımdan kaldırılmış</abbr> olarak göstermesini istiyorsunuz.

O zaman `Query`'ye `deprecated=True` parametresini iletin:

{* ../../docs_src/query_params_str_validations/tutorial010_an_py310.py hl[19] *}

Belgeler şöyle gösterecektir:

<img src="/img/tutorial/query-params-str-validations/image01.png">

## Parametreleri OpenAPI'den hariç tutma

Bir sorgu parametresini oluşturulan OpenAPI şemasından (ve dolayısıyla otomatik belge sistemlerinden) hariç tutmak için, `Query`'nin `include_in_schema` parametresini `False` olarak ayarlayın:

{* ../../docs_src/query_params_str_validations/tutorial014_an_py310.py hl[10] *}

## Özel Doğrulama

Yukarıda gösterilen parametrelerle yapılamayan bazı **özel doğrulama** yapmanız gereken durumlar olabilir.

Bu durumlarda, normal doğrulamadan sonra (örn. değerin bir `str` olduğunun doğrulanmasından sonra) uygulanan bir **özel doğrulayıcı fonksiyon** kullanabilirsiniz.

Bunu, `Annotated` içinde <a href="https://docs.pydantic.dev/latest/concepts/validators/#field-after-validator" class="external-link" target="_blank">Pydantic'in `AfterValidator`</a>'ını kullanarak başarabilirsiniz.

/// tip

Pydantic'in <a href="https://docs.pydantic.dev/latest/concepts/validators/#field-before-validator" class="external-link" target="_blank">`BeforeValidator`</a>'u ve diğerleri de vardır. 🤓

///

Örneğin, bu özel doğrulayıcı öğe ID'sinin bir <abbr title="ISBN, Uluslararası Standart Kitap Numarası anlamına gelir">ISBN</abbr> kitap numarası için `isbn-` ile veya bir <abbr title="IMDB (Internet Movie Database) filmler hakkında bilgi içeren bir web sitesidir">IMDB</abbr> film URL ID'si için `imdb-` ile başlayıp başlamadığını kontrol eder:

{* ../../docs_src/query_params_str_validations/tutorial015_an_py310.py hl[5,16:19,24] *}

/// info

Bu, Pydantic sürüm 2 veya üzeri ile kullanılabilir. 😎

///

/// tip

Herhangi bir **harici bileşen** ile iletişim gerektiren herhangi bir doğrulama yapmanız gerekiyorsa, örneğin bir veritabanı veya başka bir API, bunun yerine **FastAPI Bağımlılıkları** kullanmalısınız, bunları daha sonra öğreneceksiniz.

Bu özel doğrulayıcılar, istekte sağlanan **yalnızca** **aynı verilerle** kontrol edilebilecek şeyler içindir.

///

### Bu Kodu Anlayın

Önemli nokta sadece **`Annotated` içinde bir fonksiyonla `AfterValidator` kullanmaktır**. Bu kısmı atlamaktan çekinmeyin. 🤸

---

Ancak bu özel kod örneği hakkında merak ediyorsanız ve hala eğleniyorsanız, işte bazı ek ayrıntılar.

#### `value.startswith()` ile string

Fark ettiniz mi? `value.startswith()` kullanan bir string bir tuple alabilir ve tuple'daki her değeri kontrol eder:

{* ../../docs_src/query_params_str_validations/tutorial015_an_py310.py ln[16:19] hl[17] *}

#### Rastgele bir öğe

`data.items()` ile her sözlük öğesi için anahtar ve değer içeren tuple'lar içeren bir <abbr title="For döngüsüyle üzerinde yinelenebilen bir şey, liste, küme vb. gibi">yinelenebilir nesne</abbr> elde ederiz.

Bu yinelenebilir nesneyi `list(data.items())` ile düzgün bir `list`'e dönüştürürüz.

Ardından `random.choice()` ile listeden **rastgele bir değer** alırız, böylece `(id, name)` ile bir tuple elde ederiz. `("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy")` gibi bir şey olacaktır.

Ardından tuple'ın bu iki değerini `id` ve `name` değişkenlerine **atarız**.

Yani, kullanıcı bir öğe ID'si sağlamadıysa, yine de rastgele bir öneri alacaktır.

...bunu hepsini **tek basit bir satırda** yapıyoruz. 🤯 Python'u sevmiyor musunuz? 🐍

{* ../../docs_src/query_params_str_validations/tutorial015_an_py310.py ln[22:30] hl[29] *}

## Özet

Parametreleriniz için ek doğrulamalar ve meta veriler bildirebilirsiniz.

Genel doğrulamalar ve meta veriler:

* `alias`
* `title`
* `description`
* `deprecated`

Stringlere özgü doğrulamalar:

* `min_length`
* `max_length`
* `pattern`

`AfterValidator` kullanarak özel doğrulamalar.

Bu örneklerde `str` değerleri için doğrulamaları nasıl bildireceğinizi gördünüz.

Sayılar gibi diğer tipler için doğrulamaları nasıl bildireceğinizi öğrenmek için sonraki bölümlere bakın.
