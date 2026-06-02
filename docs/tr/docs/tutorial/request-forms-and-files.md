# İstek Formları ve Dosyalar

`File` ve `Form` kullanarak dosyaları ve form alanlarını aynı anda tanımlayabilirsiniz.

/// info

Yüklenen dosyaları ve/veya form verilerini almak için önce <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a>'ı yükleyin.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden ve ardından yüklediğinizden emin olun, örneğin:

```console
$ pip install python-multipart
```

///

## `File` ve `Form`'u içe aktarın

{* ../../docs_src/request_forms_and_files/tutorial001_an_py39.py hl[3] *}

## `File` ve `Form` parametrelerini tanımlayın

Dosya ve form parametrelerini `Body` veya `Query` için yaptığınız gibi oluşturun:

{* ../../docs_src/request_forms_and_files/tutorial001_an_py39.py hl[10:12] *}

Dosyalar ve form alanları form verisi olarak yüklenecek ve dosyaları ve form alanlarını alacaksınız.

Ve dosyaların bazılarını `bytes` olarak, bazılarını `UploadFile` olarak bildirebilirsiniz.

/// warning

Bir *yol operasyonunda* birden fazla `File` ve `Form` parametresi bildirebilirsiniz, ancak JSON olarak almayı beklediğiniz `Body` alanlarını da bildiremezsiniz, çünkü istek gövdesi `application/json` yerine `multipart/form-data` kullanılarak kodlanmış olacaktır.

Bu **FastAPI**'nin bir sınırlaması değil, HTTP protokolünün bir parçasıdır.

///

## Özet

Aynı istekte veri ve dosyaları almanız gerektiğinde `File` ve `Form`'u birlikte kullanın.
