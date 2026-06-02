# Bağımlılık Olarak Sınıflar

**Bağımlılık Enjeksiyonu** sistemine daha derinlemesine dalmadan önce, önceki örneği geliştirelim.

## Önceki örnekteki `dict`

Önceki örnekte, bağımlılığımızdan ("bağımlı olunabilir") bir `dict` döndürüyorduk:

{* ../../docs_src/dependencies/tutorial001_an_py310.py hl[9] *}

Ama sonra *yol operasyonu fonksiyonunun* `commons` parametresinde bir `dict` alıyoruz.

Ve editörlerin `dict`'ler için çok fazla destek sağlayamadığını biliyoruz (otomatik tamamlama gibi), çünkü anahtar ve değer tiplerini bilemezler.

Daha iyisini yapabiliriz...

## Bir bağımlılığı ne yapar

Şimdiye kadar fonksiyon olarak bildirilen bağımlılıklar gördünüz.

Ama bağımlılıkları bildirmenin tek yolu bu değildir (muhtemelen daha yaygın olan yöntem olsa da).

Kilit faktör, bir bağımlılığın "çağrılabilir" olması gerektiğidir.

Python'da **"çağrılabilir"**, Python'un bir fonksiyon gibi "çağırabildiği" herhangi bir şeydir.

Bu yüzden, bir `something` nesneniz varsa (bir fonksiyon _olmayabilir_) ve onu şöyle "çağırabiliyorsanız" (çalıştırabiliyorsanız):

```Python
something()
```

veya

```Python
something(some_argument, some_keyword_argument="foo")
```

o zaman "çağrılabilir"dir.

## Bağımlılık olarak sınıflar

Bir Python sınıfının örneğini oluşturmak için aynı sözdizimini kullandığınızı fark edebilirsiniz.

Örneğin:

```Python
class Cat:
    def __init__(self, name: str):
        self.name = name


fluffy = Cat(name="Mr Fluffy")
```

Bu durumda, `fluffy`, `Cat` sınıfının bir örneğidir.

Ve `fluffy`'yi oluşturmak için `Cat`'i "çağırıyorsunuz".

Yani, bir Python sınıfı da bir **çağrılabilir**dir.

O halde, **FastAPI**'de bir Python sınıfını bağımlılık olarak kullanabilirsiniz.

FastAPI'nin gerçekten kontrol ettiği şey, bunun bir "çağrılabilir" (fonksiyon, sınıf veya başka herhangi bir şey) olması ve tanımlanan parametrelerdir.

**FastAPI**'de bir "çağrılabilir"'ı bağımlılık olarak iletirseniz, o "çağrılabilir" için parametreleri analiz edecek ve *yol operasyonu fonksiyonu* için parametrelerle aynı şekilde işleyecektir. Alt bağımlılıklar dahil.

Bu, hiç parametresi olmayan çağrılabilirler için de geçerlidir. Hiç parametresi olmayan *yol operasyonu fonksiyonları* için olduğu gibi.

O zaman, yukarıdaki `common_parameters` bağımlılığını ("bağımlı olunabilir") `CommonQueryParams` sınıfına değiştirebiliriz:

{* ../../docs_src/dependencies/tutorial002_an_py310.py hl[11:15] *}

Sınıfın örneğini oluşturmak için kullanılan `__init__` metoduna dikkat edin:

{* ../../docs_src/dependencies/tutorial002_an_py310.py hl[12] *}

...önceki `common_parameters` ile aynı parametrelere sahiptir:

{* ../../docs_src/dependencies/tutorial001_an_py310.py hl[8] *}

Bu parametreler, **FastAPI**'nin bağımlılığı "çözmek" için kullanacağı şeydir.

Her iki durumda da şunlara sahip olacaktır:

* Varsayılan olarak `0` olan, `int` tipinde bir `skip` sorgu parametresi.
* Varsayılan olarak `100` olan, `int` tipinde bir `limit` sorgu parametresi.
* `str` olan isteğe bağlı bir `q` sorgu parametresi.

Her iki durumda da veri dönüştürülecek, doğrulanacak, OpenAPI şemasında belgelenecek, vb.

## Kullanın

Şimdi bu sınıfı kullanarak bağımlılığınızı bildirebilirsiniz.

{* ../../docs_src/dependencies/tutorial002_an_py310.py hl[19] *}

**FastAPI**, `CommonQueryParams` sınıfını çağırır. Bu, o sınıfın bir "örneğini" oluşturur ve örnek, fonksiyonunuza `commons` parametresi olarak iletilir.

## Tip açıklaması vs `Depends`

Yukarıdaki kodda `CommonQueryParams`'ı iki kez nasıl yazdığımıza dikkat edin:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

Son `CommonQueryParams`, şurada:

```Python
... Depends(CommonQueryParams)
```

...**FastAPI**'nin bağımlılığın ne olduğunu bilmek için gerçekten kullanacağı şeydir.

FastAPI'nin bildirilen parametreleri çıkaracağı ve gerçekten çağıracağı şey budur.

---

Bu durumda, ilk `CommonQueryParams`, şurada:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, ...
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
commons: CommonQueryParams ...
```

////

...**FastAPI** için özel bir anlamı yoktur. FastAPI bunu veri dönüşümü, doğrulama vb. için kullanmayacaktır (bunun için `Depends(CommonQueryParams)` kullanır).

Aslında sadece şunu yazabilirsiniz:

//// tab | Python 3.8+

```Python
commons: Annotated[Any, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
commons = Depends(CommonQueryParams)
```

////

...şurada olduğu gibi:

{* ../../docs_src/dependencies/tutorial003_an_py310.py hl[19] *}

Ancak tipi bildirmek teşvik edilir çünkü bu şekilde editörünüz `commons` parametresi olarak neyin iletileceğini bilecek ve ardından kod tamamlama, tip kontrolleri vb. ile size yardımcı olabilecektir:

<img src="/img/tutorial/dependencies/image02.png">

## Kısayol

Ancak burada bazı kod tekrarı olduğunu görüyorsunuz, `CommonQueryParams`'ı iki kez yazıyoruz:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

**FastAPI**, bağımlılığın *özellikle* **FastAPI**'nin sınıfın kendisinin bir örneğini oluşturmak için "çağıracağı" bir sınıf olduğu bu durumlar için bir kısayol sağlar.

Bu özel durumlar için şunları yapabilirsiniz:

Şunu yazmak yerine:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
commons: CommonQueryParams = Depends(CommonQueryParams)
```

////

...şunu yazarsınız:

//// tab | Python 3.8+

```Python
commons: Annotated[CommonQueryParams, Depends()]
```

////

//// tab | Python 3.8 non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
commons: CommonQueryParams = Depends()
```

////

Bağımlılığı parametrenin tipi olarak bildirirsiniz ve `Depends(CommonQueryParams)` içinde tam sınıfı *tekrar* yazmak yerine herhangi bir parametre olmadan `Depends()` kullanırsınız.

Aynı örnek şöyle görünecektir:

{* ../../docs_src/dependencies/tutorial004_an_py310.py hl[19] *}

...ve **FastAPI** ne yapacağını bilecektir.

/// tip

Bu yardımcı olmaktan çok kafa karıştırıcı görünüyorsa, görmezden gelin, buna *ihtiyacınız* yok.

Bu sadece bir kısayol. Çünkü **FastAPI** kod tekrarını en aza indirmenize yardımcı olmayı önemsiyor.

///
