# Çerez Parametreleri

Çerez parametrelerini `Query` ve `Path` parametrelerini tanımladığınız şekilde tanımlayabilirsiniz.

## `Cookie`'yi içe aktarın

Öncelikle `Cookie`'yi içe aktarın:

{* ../../docs_src/cookie_params/tutorial001_an_py310.py hl[3] *}

## `Cookie` parametrelerini bildirin

Ardından çerez parametrelerini `Path` ve `Query` ile aynı yapıyı kullanarak bildirin.

Varsayılan değeri ve tüm ek doğrulama veya açıklama parametrelerini tanımlayabilirsiniz:

{* ../../docs_src/cookie_params/tutorial001_an_py310.py hl[9] *}

/// note | Teknik Detaylar

`Cookie`, `Path` ve `Query`'nin bir "kardeş" sınıfıdır. Aynı ortak `Param` sınıfından miras alır.

Ancak `fastapi`'den `Query`, `Path`, `Cookie` ve diğerlerini içe aktardığınızda, bunların aslında özel sınıflar döndüren fonksiyonlar olduğunu unutmayın.

///

/// info

Çerezleri bildirmek için `Cookie` kullanmanız gerekir, aksi takdirde parametreler sorgu parametreleri olarak yorumlanır.

///

## Özet

Çerezleri `Cookie` ile bildirin, `Query` ve `Path` ile aynı ortak kalıbı kullanarak.
