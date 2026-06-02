# Form Verileri

JSON yerine form alanları almanız gerektiğinde `Form` kullanabilirsiniz.

/// info

Formları kullanmak için önce <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a>'ı yükleyin.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden ve ardından yüklediğinizden emin olun, örneğin:

```console
$ pip install python-multipart
```

///

## `Form`'u içe aktarın

`fastapi`'den `Form`'u içe aktarın:

{* ../../docs_src/request_forms/tutorial001_an_py39.py hl[3] *}

## `Form` parametrelerini tanımlayın

Form parametrelerini `Body` veya `Query` için yaptığınız gibi oluşturun:

{* ../../docs_src/request_forms/tutorial001_an_py39.py hl[9] *}

Örneğin, OAuth2 spesifikasyonunun kullanılabileceği yollardan birinde ("password flow" olarak adlandırılır) bir `username` ve `password`'ü form alanları olarak göndermeniz gerekir.

<abbr title="spesifikasyon">Spec</abbr>, alanların tam olarak `username` ve `password` olarak adlandırılmasını ve JSON olarak değil form alanları olarak gönderilmesini gerektirir.

`Form` ile `Body` (ve `Query`, `Path`, `Cookie`) ile aynı yapılandırmaları bildirebilirsiniz, doğrulama, örnekler, bir takma ad (örneğin `username` yerine `user-name`) vb. dahil.

/// info

`Form`, doğrudan `Body`'den miras alan bir sınıftır.

///

/// tip

Form gövdelerini bildirmek için `Form`'u açıkça kullanmanız gerekir, çünkü onsuz parametreler sorgu parametreleri veya gövde (JSON) parametreleri olarak yorumlanır.

///

## "Form Alanları" hakkında

HTML formlarının (`<form></form>`) verileri sunucuya gönderme şekli normalde bu veriler için "özel" bir kodlama kullanır, JSON'dan farklıdır.

**FastAPI**, bu verileri JSON yerine doğru yerden okumayı sağlayacaktır.

/// note | Teknik Detaylar

Formlardan gelen veriler normalde `application/x-www-form-urlencoded` "medya tipi" kullanılarak kodlanır.

Ancak form dosyalar içerdiğinde, `multipart/form-data` olarak kodlanır. Dosyaları işleme hakkında bir sonraki bölümde okuyacaksınız.

Bu kodlamalar ve form alanları hakkında daha fazla bilgi edinmek istiyorsanız, <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST" class="external-link" target="_blank"><abbr title="Mozilla Developer Network">MDN</abbr> web belgelerinde <code>POST</code></a> sayfasına gidin.

///

/// warning

Bir *yol operasyonunda* birden fazla `Form` parametresi bildirebilirsiniz, ancak JSON olarak almayı beklediğiniz `Body` alanlarını da bildiremezsiniz, çünkü istek gövdesi `application/json` yerine `application/x-www-form-urlencoded` kullanılarak kodlanmış olacaktır.

Bu **FastAPI**'nin bir sınırlaması değil, HTTP protokolünün bir parçasıdır.

///

## Özet

Form veri girişi parametrelerini bildirmek için `Form` kullanın.
