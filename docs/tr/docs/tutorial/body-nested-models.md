# Gövde - İç İçe Modeller

**FastAPI** ile isteğe bağlı derinlikte iç içe geçmiş modelleri tanımlayabilir, doğrulayabilir, belgelendirebilir ve kullanabilirsiniz (Pydantic sayesinde).

## Liste alanları

Bir niteliği alt tip olarak tanımlayabilirsiniz. Örneğin, bir Python `list`:

{* ../../docs_src/body_nested_models/tutorial001_py310.py hl[12] *}

Bu, `tags`'i bir liste yapacaktır, ancak listenin elemanlarının tipini bildirmez.

## Tip parametreli liste alanları

Ancak Python'un dahili tipleri veya "tip parametreleri" ile listeleri bildirmek için özel bir yolu vardır:

### typing'den `List`'i içe aktarın

Python 3.9 ve üzerinde, aşağıda göreceğimiz gibi bu tip açıklamalarını bildirmek için standart `list`'i kullanabilirsiniz. 💡

Ancak Python 3.9'dan önceki sürümlerde (3.6 ve üzeri), önce standart Python'un `typing` modülünden `List`'i içe aktarmanız gerekir:

{* ../../docs_src/body_nested_models/tutorial002.py hl[1] *}

### Tip parametreli bir `list` bildirin

Tip parametreleri (dahili tipler) olan tipleri bildirmek için, örneğin `list`, `dict`, `tuple`:

* Python 3.9'dan düşük bir sürümdeyseniz, `typing` modülünden eşdeğer sürümlerini içe aktarın
* Dahili tip(ler)i köşeli parantezler kullanarak "tip parametreleri" olarak iletin: `[` ve `]`

Python 3.9'da şöyle olurdu:

```Python
my_list: list[str]
```

Python 3.9'dan önceki sürümlerde şöyle olurdu:

```Python
from typing import List

my_list: List[str]
```

Bu, tip bildirimleri için tamamen standart Python söz dizimidir.

Dahili tiplere sahip model nitelikleri için aynı standart söz dizimini kullanın.

Yani, örneğimizde `tags`'i özellikle bir "string listesi" yapabiliriz:

{* ../../docs_src/body_nested_models/tutorial002_py310.py hl[12] *}

## Set tipleri

Ancak sonra düşünüyoruz ve etiketlerin tekrarlanmaması gerektiğini, muhtemelen benzersiz stringler olacağını fark ediyoruz.

Ve Python'un benzersiz öğe kümeleri için özel bir veri tipi vardır: `set`.

O zaman `tags`'i bir string kümesi olarak bildirebiliriz:

{* ../../docs_src/body_nested_models/tutorial003_py310.py hl[12] *}

Bununla, yinelenen verilerle bir istek alsanız bile, benzersiz öğelerin bir kümesine dönüştürülecektir.

Ve bu veriyi çıktı olarak verdiğinizde, kaynak yinelenenlere sahip olsa bile, benzersiz öğelerin bir kümesi olarak çıktı verilecektir.

Ve buna göre açıklanacak / belgelendirilecektir.

## İç içe modeller

Bir Pydantic modelinin her niteliğinin bir tipi vardır.

Ancak bu tip kendisi başka bir Pydantic modeli olabilir.

Böylece, belirli nitelik adları, tipleri ve doğrulamaları olan derinlemesine iç içe geçmiş JSON "nesneleri" bildirebilirsiniz.

Tüm bunlar, isteğe bağlı derinlikte iç içe geçmiş.

### Bir alt model tanımlayın

Örneğin, bir `Image` modeli tanımlayabiliriz:

{* ../../docs_src/body_nested_models/tutorial004_py310.py hl[7:9] *}

### Alt modeli tip olarak kullanın

Ve sonra bunu bir niteliğin tipi olarak kullanabiliriz:

{* ../../docs_src/body_nested_models/tutorial004_py310.py hl[18] *}

Bu, **FastAPI**'nin şuna benzer bir gövde bekleyeceği anlamına gelir:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
```

Yine, sadece bu bildirimi yaparak, **FastAPI** ile şunları elde edersiniz:

* Editör desteği (tamamlama vb.), iç içe modeller için bile
* Veri dönüştürme
* Veri doğrulama
* Otomatik belgelendirme

## Özel tipler ve doğrulama

`str`, `int`, `float` vb. gibi normal tekil tiplerin yanı sıra, `str`'den miras alan daha karmaşık tekil tipler kullanabilirsiniz.

Sahip olduğunuz tüm seçenekleri görmek için <a href="https://docs.pydantic.dev/latest/concepts/types/" class="external-link" target="_blank">Pydantic'in Tip Genel Bakışı</a>'na bakın. Bir sonraki bölümde bazı örnekler göreceksiniz.

Örneğin, `Image` modelinde bir `url` alanımız olduğu gibi, bunu `str` yerine Pydantic'in `HttpUrl` örneği olarak bildirebiliriz:

{* ../../docs_src/body_nested_models/tutorial005_py310.py hl[2,8] *}

String'in geçerli bir URL olup olmadığı kontrol edilecek ve JSON Schema / OpenAPI'de bu şekilde belgelendirilecektir.

## Alt model listelerine sahip nitelikler

Pydantic modellerini `list`, `set` vb.'nin alt tipleri olarak da kullanabilirsiniz:

{* ../../docs_src/body_nested_models/tutorial006_py310.py hl[18] *}

Bu, şöyle bir JSON gövdesini bekleyecek (dönüştürecek, doğrulayacak, belgelendirecek vb.):

```JSON hl_lines="11"
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}
```

/// info

`images` anahtarının artık bir görüntü nesneleri listesine sahip olduğuna dikkat edin.

///

## Derinden iç içe modeller

İsteğe bağlı derinlikte iç içe geçmiş modeller tanımlayabilirsiniz:

{* ../../docs_src/body_nested_models/tutorial007_py310.py hl[7,12,18,21,25] *}

/// info

`Offer`'ın bir `Item` listesine sahip olduğuna ve bunların da isteğe bağlı bir `Image` listesine sahip olduğuna dikkat edin.

///

## Saf liste gövdeleri

Beklediğiniz JSON gövdesinin en üst düzey değeri bir JSON `array` (Python `list`) ise, Pydantic modellerinde olduğu gibi, fonksiyonun parametresinde tipi bildirebilirsiniz:

```Python
images: List[Image]
```

veya Python 3.9 ve üzerinde:

```Python
images: list[Image]
```

şöyle:

{* ../../docs_src/body_nested_models/tutorial008_py39.py hl[13] *}

## Her yerde editör desteği

Ve her yerde editör desteği alırsınız.

Listelerin içindeki öğeler için bile:

<img src="/img/tutorial/body-nested-models/image01.png">

Pydantic modelleri yerine doğrudan `dict` ile çalışsaydınız, bu tür editör desteğini alamazdınız.

Ancak onlar hakkında endişelenmenize de gerek yok, gelen dict'ler otomatik olarak dönüştürülür ve çıktınız da otomatik olarak JSON'a dönüştürülür.

## Rastgele `dict` gövdeleri

Ayrıca bir gövdeyi belirli bir tipteki anahtarlar ve başka bir tipteki değerlerle bir `dict` olarak bildirebilirsiniz.

Bu şekilde, geçerli alan/nitelik adlarının önceden ne olduğunu bilmenize gerek kalmaz (Pydantic modelleriyle olduğu gibi).

Bu, henüz bilmediğiniz anahtarları almak istediğinizde yararlı olacaktır.

---

Başka bir yararlı durum, başka bir tipteki anahtarlara sahip olmak istediğinizde (örneğin `int`).

Burada göreceğimiz şey budur.

Bu durumda, `int` anahtarları ve `float` değerleri olan herhangi bir `dict`'i kabul edersiniz:

{* ../../docs_src/body_nested_models/tutorial009_py39.py hl[7] *}

/// tip

JSON'un yalnızca `str`'yi anahtar olarak desteklediğini unutmayın.

Ancak Pydantic otomatik veri dönüştürme özelliğine sahiptir.

Bu, API istemcileriniz yalnızca anahtar olarak string gönderebilse de, bu stringler saf tamsayılar içerdiği sürece, Pydantic bunları dönüştürüp doğrulayacaktır.

Ve `weights` olarak aldığınız `dict` aslında `int` anahtarlara ve `float` değerlere sahip olacaktır.

///

## Özet

**FastAPI** ile, kodunuzu basit, kısa ve zarif tutarken Pydantic modellerinin sağladığı maksimum esnekliğe sahip olursunuz.

Ve tüm avantajlarla:

* Editör desteği (her yerde tamamlama!)
* Veri dönüştürme (diğer adıyla ayrıştırma / serileştirme)
* Veri doğrulama
* Şema belgelendirme
* Otomatik belgeler
