# Gövde - Alanlar

*Yol operasyonu fonksiyonu* parametrelerinde `Query`, `Path` ve `Body` ile ek doğrulama ve meta veri bildirebildiğiniz gibi, Pydantic'in `Field` kullanarak Pydantic modelleri içinde doğrulama ve meta veri bildirebilirsiniz.

## `Field`'ı içe aktarın

Öncelikle, onu içe aktarmanız gerekir:

{* ../../docs_src/body_fields/tutorial001_an_py310.py hl[4] *}


/// warning

`Field`'ın `fastapi`'den değil, doğrudan `pydantic`'ten içe aktarıldığına dikkat edin (diğer tüm `Query`, `Path`, `Body` vb. `fastapi`'den içe aktarılır).

///

## Model niteliklerini bildirin

Ardından `Field`'ı model nitelikleriyle kullanabilirsiniz:

{* ../../docs_src/body_fields/tutorial001_an_py310.py hl[11:14] *}

`Field`, `Query`, `Path` ve `Body` ile aynı şekilde çalışır, aynı parametrelere vb. sahiptir.

/// note | Teknik Detaylar

Aslında, `Query`, `Path` ve sonra göreceğiniz diğerleri, ortak bir `Param` sınıfının alt sınıflarının nesnelerini oluşturur; bu sınıf da Pydantic'in `FieldInfo` sınıfının bir alt sınıfıdır.

Ve Pydantic'in `Field`'ı da bir `FieldInfo` örneği döndürür.

`Body` da doğrudan `FieldInfo`'nun bir alt sınıfının nesnelerini döndürür. Ve daha sonra göreceğiniz, `Body` sınıfının alt sınıfları olan başkaları da vardır.

`fastapi`'den `Query`, `Path` ve diğerlerini içe aktardığınızda, bunların aslında özel sınıflar döndüren fonksiyonlar olduğunu unutmayın.

///

/// tip

Her modelin tip, varsayılan değer ve `Field` ile olan niteliğinin, `Field` yerine `Path`, `Query` ve `Body` ile bir *yol operasyonu fonksiyonunun* parametresiyle aynı yapıya sahip olduğuna dikkat edin.

///

## Ek bilgi ekleyin

`Field`, `Query`, `Body` vb. içinde ek bilgi bildirebilirsiniz. Ve bu, oluşturulan JSON Şemasına dahil edilecektir.

Belgelerde daha sonra örnekler bildirmeyi öğrenirken ek bilgi ekleme hakkında daha fazla bilgi edineceksiniz.

/// warning

`Field`'a iletilen ekstra anahtarlar, uygulamanız için oluşturulan OpenAPI şemasında da bulunacaktır.
Bu anahtarlar OpenAPI spesifikasyonunun bir parçası olmayabileceğinden, bazı OpenAPI araçları, örneğin [OpenAPI doğrulayıcısı](https://validator.swagger.io/), oluşturulan şemanızla çalışmayabilir.

///

## Özet

Model nitelikleri için ek doğrulamalar ve meta veri bildirmek üzere Pydantic'in `Field`'ını kullanabilirsiniz.

Ayrıca ek JSON Schema meta verisi iletmek için ekstra anahtar kelime argümanlarını da kullanabilirsiniz.
