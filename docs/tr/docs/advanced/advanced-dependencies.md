# Gelişmiş Bağımlılıklar

## Parametreli bağımlılıklar

Şimdiye kadar gördüğümüz tüm bağımlılıklar sabit bir fonksiyon veya sınıftır.

Ancak birçok farklı fonksiyon veya sınıf bildirmek zorunda kalmadan bağımlılığa parametreler ayarlayabilmek istediğiniz durumlar olabilir.

Sorgu parametresi `q`'nun sabit bir içerik içerip içermediğini kontrol eden bir bağımlılığımız olmasını istediğimizi düşünelim.

Ama o sabit içeriği parametreleştirebilmek istiyoruz.

## Bir "çağrılabilir" örnek

Python'da bir sınıf örneğini "çağrılabilir" yapmanın bir yolu vardır.

Sınıfın kendisi değil (zaten bir çağrılabilirdir), o sınıfın bir örneği.

Bunu yapmak için bir `__call__` metodu bildiririz:

{* ../../docs_src/dependencies/tutorial011_an_py39.py hl[12] *}

Bu durumda, bu `__call__`, **FastAPI**'nin ek parametreleri ve alt bağımlılıkları kontrol etmek için kullanacağı şeydir ve daha sonra *yol operasyonu fonksiyonunuzdaki* parametreye bir değer iletmek için çağrılacak olan şeydir.

## Örneği parametreleştirin

Ve şimdi, bağımlılığı "parametreleştirmek" için kullanabileceğimiz örneğin parametrelerini bildirmek üzere `__init__`'i kullanabiliriz:

{* ../../docs_src/dependencies/tutorial011_an_py39.py hl[9] *}

Bu durumda, **FastAPI** `__init__`'e hiç dokunmayacak veya umursamayacaktır, onu doğrudan kodumuzda kullanacağız.

## Bir örnek oluşturun

Bu sınıfın bir örneğini şu şekilde oluşturabiliriz:

{* ../../docs_src/dependencies/tutorial011_an_py39.py hl[18] *}

Ve bu şekilde bağımlılığımızı "parametreleştirebiliriz", artık `checker.fixed_content` niteliği olarak içinde `"bar"` var.

## Örneği bağımlılık olarak kullanın

Ardından, `Depends(FixedContentQueryChecker)` yerine `Depends(checker)` içinde bu `checker`'ı kullanabiliriz, çünkü bağımlılık sınıfın kendisi değil, `checker` örneğidir.

Ve bağımlılığı çözerken, **FastAPI** bu `checker`'ı şöyle çağıracaktır:

```Python
checker(q="somequery")
```

...ve bunun döndürdüğü her şeyi *yol operasyonu fonksiyonumuzda* `fixed_content_included` parametresi olarak bağımlılığın değeri olarak iletecektir:

{* ../../docs_src/dependencies/tutorial011_an_py39.py hl[22] *}

/// tip

Tüm bunlar karmaşık görünebilir. Ve henüz nasıl yararlı olduğu çok açık olmayabilir.

Bu örnekler kasıtlı olarak basittir, ancak her şeyin nasıl çalıştığını gösterir.

Güvenlik hakkındaki bölümlerde, tam olarak bu şekilde uygulanan yardımcı fonksiyonlar vardır.

Tüm bunları anladıysanız, güvenlik için kullanılan yardımcı araçların altta nasıl çalıştığını zaten biliyorsunuz.

///
