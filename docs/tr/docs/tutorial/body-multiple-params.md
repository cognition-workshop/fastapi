# Gövde - Birden Fazla Parametre

`Path` ve `Query`'yi nasıl kullanacağımızı gördüğümüze göre, şimdi istek gövdesi bildirimlerinin daha gelişmiş kullanımlarını görelim.

## `Path`, `Query` ve gövde parametrelerini karıştırın

Öncelikle, elbette, `Path`, `Query` ve istek gövdesi parametre bildirimlerini serbestçe karıştırabilirsiniz ve **FastAPI** ne yapacağını bilecektir.

Ayrıca varsayılan değeri `None` olarak ayarlayarak gövde parametrelerini isteğe bağlı olarak bildirebilirsiniz:

{* ../../docs_src/body_multiple_params/tutorial001_an_py310.py hl[18:20] *}

/// note

Bu durumda, gövdeden alınacak `item`'ın isteğe bağlı olduğuna dikkat edin. `None` varsayılan değerine sahip olduğu için.

///

## Birden fazla gövde parametresi

Önceki örnekte, *yol operasyonları* bir `Item`'ın niteliklerine sahip bir JSON gövdesi beklerdi, örneğin:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

Ancak birden fazla gövde parametresi de bildirebilirsiniz, örneğin `item` ve `user`:

{* ../../docs_src/body_multiple_params/tutorial002_py310.py hl[20] *}


Bu durumda, **FastAPI** fonksiyonda birden fazla gövde parametresi olduğunu fark edecektir (Pydantic modeli olan iki parametre vardır).

Bu yüzden parametre adlarını gövdede anahtar (alan adları) olarak kullanacak ve şöyle bir gövde bekleyecektir:

```JSON
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

/// note

`item`'ın daha önce olduğu gibi bildirilmiş olmasına rağmen, artık gövde içinde `item` anahtarıyla bulunmasının beklendiğine dikkat edin.

///

**FastAPI** istekten otomatik dönüşüm yapacaktır, böylece `item` parametresi kendi içeriğini alır ve `user` için de aynısı geçerlidir.

Bileşik verinin doğrulamasını yapacak ve OpenAPI şeması ve otomatik belgeler için bunu belgelendirecektir.

## Gövdede tekil değerler

Sorgu ve yol parametreleri için ek veri tanımlamak üzere `Query` ve `Path` olduğu gibi, **FastAPI** eşdeğer bir `Body` sağlar.

Örneğin, önceki modeli genişleterek, `item` ve `user`'ın yanı sıra aynı gövdede başka bir `importance` anahtarı isteyebilirsiniz.

Olduğu gibi bildirirseniz, tekil bir değer olduğu için **FastAPI** bunun bir sorgu parametresi olduğunu varsayacaktır.

Ancak **FastAPI**'ye `Body` kullanarak bunu başka bir gövde anahtarı olarak işlemesini söyleyebilirsiniz:

{* ../../docs_src/body_multiple_params/tutorial003_an_py310.py hl[23] *}


Bu durumda, **FastAPI** şöyle bir gövde bekleyecektir:

```JSON
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

Yine, veri tiplerini dönüştürecek, doğrulayacak, belgelendirecek vb.

## Birden fazla gövde parametresi ve sorgu

Elbette, herhangi bir gövde parametresine ek olarak, ihtiyaç duyduğunuzda ek sorgu parametreleri de bildirebilirsiniz.

Varsayılan olarak, tekil değerler sorgu parametreleri olarak yorumlandığından, açıkça bir `Query` eklemenize gerek yoktur, sadece şunu yapabilirsiniz:

```Python
q: Union[str, None] = None
```

Veya Python 3.10 ve üzerinde:

```Python
q: str | None = None
```

Örneğin:

{* ../../docs_src/body_multiple_params/tutorial004_an_py310.py hl[28] *}


/// info

`Body` da `Query`, `Path` ve daha sonra göreceğiniz diğerleriyle aynı ek doğrulama ve meta veri parametrelerine sahiptir.

///

## Tek bir gövde parametresini gömün

Diyelim ki bir Pydantic modeli `Item`'dan yalnızca tek bir `item` gövde parametreniz var.

Varsayılan olarak, **FastAPI** gövdesini doğrudan bekleyecektir.

Ancak ek gövde parametreleri bildirdiğinizde olduğu gibi, bir `item` anahtarı içinde model içeriğinin bulunduğu bir JSON beklemesini istiyorsanız, özel `Body` parametresi `embed`'i kullanabilirsiniz:

```Python
item: Item = Body(embed=True)
```

şöyle:

{* ../../docs_src/body_multiple_params/tutorial005_an_py310.py hl[17] *}


Bu durumda **FastAPI** şöyle bir gövde bekleyecektir:

```JSON hl_lines="2"
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

şunun yerine:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

## Özet

Bir istek yalnızca tek bir gövdeye sahip olabilse de, *yol operasyonu fonksiyonunuza* birden fazla gövde parametresi ekleyebilirsiniz.

Ancak **FastAPI** bunu halledecek, fonksiyonunuzda doğru veriyi verecek ve *yol operasyonunda* doğru şemayı doğrulayıp belgelendirecektir.

Ayrıca gövdenin bir parçası olarak alınacak tekil değerler de bildirebilirsiniz.

Ve yalnızca tek bir parametre bildirilmiş olsa bile **FastAPI**'ye gövdeyi bir anahtarın içine gömmesini söyleyebilirsiniz.
