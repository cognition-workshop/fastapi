# Sorgu Parametreleri

Yol parametrelerinin bir parçası olmayan diğer fonksiyon parametrelerini bildirdiğinizde, bunlar otomatik olarak "sorgu" parametreleri olarak yorumlanır.

{* ../../docs_src/query_params/tutorial001.py hl[9] *}

Sorgu, URL'de `?` işaretinden sonra gelen ve `&` karakterleriyle ayrılan anahtar-değer çiftleri kümesidir.

Örneğin, şu URL'de:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

...sorgu parametreleri şunlardır:

* `skip`: `0` değerine sahip
* `limit`: `10` değerine sahip

URL'nin bir parçası oldukları için "doğal olarak" stringdirler.

Ancak Python tipleriyle bildirdiğinizde (yukarıdaki örnekte `int` olarak), o tipe dönüştürülür ve ona göre doğrulanır.

Yol parametreleri için geçerli olan aynı süreç sorgu parametreleri için de geçerlidir:

* Editör desteği (açıkçası)
* Veri <abbr title="HTTP isteğinden gelen stringi Python verisine dönüştürme">"ayrıştırma"</abbr>
* Veri doğrulama
* Otomatik belgelendirme

## Varsayılanlar

Sorgu parametreleri yolun sabit bir parçası olmadığından, isteğe bağlı olabilir ve varsayılan değerlere sahip olabilir.

Yukarıdaki örnekte `skip=0` ve `limit=10` varsayılan değerlerine sahiptirler.

Yani, şu URL'ye gitmek:

```
http://127.0.0.1:8000/items/
```

şu URL'ye gitmekle aynı olurdu:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

Ancak örneğin şu adrese giderseniz:

```
http://127.0.0.1:8000/items/?skip=20
```

Fonksiyonunuzdaki parametre değerleri şöyle olacaktır:

* `skip=20`: çünkü URL'de ayarladınız
* `limit=10`: çünkü bu varsayılan değerdi

## İsteğe bağlı parametreler

Aynı şekilde, varsayılanlarını `None` olarak ayarlayarak isteğe bağlı sorgu parametreleri bildirebilirsiniz:

{* ../../docs_src/query_params/tutorial002_py310.py hl[7] *}

Bu durumda, `q` fonksiyon parametresi isteğe bağlı olacak ve varsayılan olarak `None` olacaktır.

/// check

Ayrıca **FastAPI**'nin `item_id` yol parametresinin bir yol parametresi olduğunu ve `q`'nun olmadığını, dolayısıyla bir sorgu parametresi olduğunu fark edecek kadar akıllı olduğuna dikkat edin.

///

## Sorgu parametresi tip dönüşümü

`bool` tipleri de bildirebilirsiniz ve bunlar dönüştürülecektir:

{* ../../docs_src/query_params/tutorial003_py310.py hl[7] *}

Bu durumda, şu adrese giderseniz:

```
http://127.0.0.1:8000/items/foo?short=1
```

veya

```
http://127.0.0.1:8000/items/foo?short=True
```

veya

```
http://127.0.0.1:8000/items/foo?short=true
```

veya

```
http://127.0.0.1:8000/items/foo?short=on
```

veya

```
http://127.0.0.1:8000/items/foo?short=yes
```

veya herhangi bir başka büyük/küçük harf varyasyonunda (büyük harf, ilk harf büyük vb.), fonksiyonunuz `short` parametresini `True` `bool` değeriyle görecektir. Aksi takdirde `False` olarak.


## Birden fazla yol ve sorgu parametresi

Birden fazla yol parametresi ve sorgu parametresini aynı anda bildirebilirsiniz, **FastAPI** hangisinin hangisi olduğunu bilir.

Ve bunları belirli bir sırada bildirmeniz gerekmez.

İsimlerine göre tespit edilecektir:

{* ../../docs_src/query_params/tutorial004_py310.py hl[6,8] *}

## Zorunlu sorgu parametreleri

Yol olmayan parametreler için bir varsayılan değer bildirdiğinizde (şu anda yalnızca sorgu parametrelerini gördük), o zaman zorunlu değildir.

Belirli bir değer eklemek istemeyip sadece isteğe bağlı yapmak istiyorsanız, varsayılanı `None` olarak ayarlayın.

Ancak bir sorgu parametresini zorunlu yapmak istediğinizde, herhangi bir varsayılan değer bildirmeyebilirsiniz:

{* ../../docs_src/query_params/tutorial005.py hl[6:7] *}

Burada `needy` sorgu parametresi, `str` tipinde zorunlu bir sorgu parametresidir.

Tarayıcınızda şöyle bir URL açarsanız:

```
http://127.0.0.1:8000/items/foo-item
```

...zorunlu `needy` parametresini eklemeden, şöyle bir hata göreceksiniz:

```JSON
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "needy"
      ],
      "msg": "Field required",
      "input": null,
      "url": "https://errors.pydantic.dev/2.1/v/missing"
    }
  ]
}
```

`needy` zorunlu bir parametre olduğundan, URL'de ayarlamanız gerekir:

```
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
```

...bu çalışır:

```JSON
{
    "item_id": "foo-item",
    "needy": "sooooneedy"
}
```

Ve elbette, bazı parametreleri zorunlu, bazılarını varsayılan değere sahip ve bazılarını tamamen isteğe bağlı olarak tanımlayabilirsiniz:

{* ../../docs_src/query_params/tutorial006_py310.py hl[8] *}

Bu durumda, 3 sorgu parametresi vardır:

* `needy`, zorunlu bir `str`.
* `skip`, varsayılan değeri `0` olan bir `int`.
* `limit`, isteğe bağlı bir `int`.

/// tip

`Enum`'ları da [Yol Parametreleri](path-params.md#onceden-tanimlanmis-degerler){.internal-link target=_blank} ile aynı şekilde kullanabilirsiniz.

///
