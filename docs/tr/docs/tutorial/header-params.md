# Header Parametreleri

Header parametrelerini `Query`, `Path` ve `Cookie` parametrelerini tanımladığınız şekilde tanımlayabilirsiniz.

## `Header`'ı içe aktarın

Öncelikle `Header`'ı içe aktarın:

{* ../../docs_src/header_params/tutorial001_an_py310.py hl[3] *}

## `Header` parametrelerini bildirin

Ardından header parametrelerini `Path`, `Query` ve `Cookie` ile aynı yapıyı kullanarak bildirin.

Varsayılan değeri ve tüm ek doğrulama veya açıklama parametrelerini tanımlayabilirsiniz:

{* ../../docs_src/header_params/tutorial001_an_py310.py hl[9] *}

/// note | Teknik Detaylar

`Header`, `Path`, `Query` ve `Cookie`'nin bir "kardeş" sınıfıdır. Aynı ortak `Param` sınıfından miras alır.

Ancak `fastapi`'den `Query`, `Path`, `Header` ve diğerlerini içe aktardığınızda, bunların aslında özel sınıflar döndüren fonksiyonlar olduğunu unutmayın.

///

/// info

Header'ları bildirmek için `Header` kullanmanız gerekir, aksi takdirde parametreler sorgu parametreleri olarak yorumlanır.

///

## Otomatik dönüştürme

`Header`, `Path`, `Query` ve `Cookie`'nin sağladığının üzerine biraz ek işlevselliğe sahiptir.

Standart header'ların çoğu "tire" karakteri ile ayrılır, "eksi sembolü" (`-`) olarak da bilinir.

Ancak `user-agent` gibi bir değişken Python'da geçersizdir.

Bu yüzden, varsayılan olarak `Header`, parametre adı karakterlerini alt çizgiden (`_`) tireye (`-`) dönüştürerek header'ları çıkarır ve belgeler.

Ayrıca, HTTP header'ları büyük/küçük harfe duyarsızdır, bu yüzden onları standart Python stili (aynı zamanda "snake_case" olarak da bilinir) ile bildirebilirsiniz.

Yani, `user_agent`'ı Python kodunda normalde kullandığınız gibi kullanabilirsiniz, ilk harfleri `User_Agent` veya benzeri şekilde büyük yazmanıza gerek yoktur.

Herhangi bir nedenle alt çizgilerin tirelere otomatik dönüştürülmesini devre dışı bırakmanız gerekiyorsa, `Header`'ın `convert_underscores` parametresini `False` olarak ayarlayın:

{* ../../docs_src/header_params/tutorial002_an_py310.py hl[10] *}

/// warning

`convert_underscores`'ı `False` olarak ayarlamadan önce, bazı HTTP proxy'lerin ve sunucuların alt çizgili header'ların kullanımını yasakladığını unutmayın.

///

## Yinelenen header'lar

Yinelenen header'lar almak mümkündür. Yani, aynı header'ın birden fazla değere sahip olması.

Bu durumları tip bildiriminde bir liste kullanarak tanımlayabilirsiniz.

Yinelenen header'daki tüm değerleri bir Python `list` olarak alacaksınız.

Örneğin, birden fazla kez görünebilen bir `X-Token` header'ı bildirmek için şunu yazabilirsiniz:

{* ../../docs_src/header_params/tutorial003_an_py310.py hl[9] *}

Bu *yol operasyonu* ile iki HTTP header'ı göndererek iletişim kurarsanız:

```
X-Token: foo
X-Token: bar
```

Yanıt şöyle olurdu:

```JSON
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
```

## Özet

Header'ları `Header` ile bildirin, `Query`, `Path` ve `Cookie` ile aynı ortak kalıbı kullanarak.

Ve değişkenlerinizdeki alt çizgiler konusunda endişelenmeyin, **FastAPI** onları dönüştürmeyi halledecektir.
