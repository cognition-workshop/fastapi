# İstek Dosyaları

`File` kullanarak istemci tarafından yüklenecek dosyaları tanımlayabilirsiniz.

/// info

Yüklenen dosyaları almak için önce <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a>'ı yükleyin.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden ve ardından yüklediğinizden emin olun, örneğin:

```console
$ pip install python-multipart
```

Bu, yüklenen dosyaların "form verisi" olarak gönderilmesinden kaynaklanır.

///

## `File`'ı içe aktarın

`fastapi`'den `File` ve `UploadFile`'ı içe aktarın:

{* ../../docs_src/request_files/tutorial001_an_py39.py hl[3] *}

## `File` Parametrelerini Tanımlayın

Dosya parametrelerini `Body` veya `Form` için yaptığınız gibi oluşturun:

{* ../../docs_src/request_files/tutorial001_an_py39.py hl[9] *}

/// info

`File`, doğrudan `Form`'dan miras alan bir sınıftır.

Ancak `fastapi`'den `Query`, `Path`, `File` ve diğerlerini içe aktardığınızda, bunların aslında özel sınıflar döndüren fonksiyonlar olduğunu unutmayın.

///

/// tip

Dosya gövdelerini bildirmek için `File` kullanmanız gerekir, çünkü onsuz parametreler sorgu parametreleri veya gövde (JSON) parametreleri olarak yorumlanır.

///

Dosyalar "form verisi" olarak yüklenecektir.

*Yol operasyonu fonksiyon* parametrenizin tipini `bytes` olarak bildirirseniz, **FastAPI** dosyayı sizin için okuyacak ve içeriği `bytes` olarak alacaksınız.

Bunun, tüm içeriğin bellekte depolanacağı anlamına geldiğini unutmayın. Bu, küçük dosyalar için iyi çalışacaktır.

Ancak `UploadFile` kullanmanın faydalı olabileceği birçok durum vardır.

## `UploadFile` ile Dosya Parametreleri

Bir dosya parametresini `UploadFile` tipiyle tanımlayın:

{* ../../docs_src/request_files/tutorial001_an_py39.py hl[14] *}

`UploadFile` kullanmanın `bytes`'a göre birçok avantajı vardır:

* Parametrenin varsayılan değerinde `File()` kullanmanız gerekmez.
* "Spool" edilmiş bir dosya kullanır:
    * Maksimum boyut sınırına kadar bellekte depolanan bir dosya, ve bu sınır aşıldıktan sonra diske depolanacaktır.
* Bu, tüm belleği tüketmeden resimler, videolar, büyük ikili dosyalar vb. gibi büyük dosyalar için iyi çalışacağı anlamına gelir.
* Yüklenen dosyadan meta veri alabilirsiniz.
* <a href="https://docs.python.org/3/glossary.html#term-file-like-object" class="external-link" target="_blank">Dosya benzeri</a> bir `async` arayüzüne sahiptir.
* Dosya benzeri bir nesne bekleyen diğer kütüphanelere doğrudan iletebileceğiniz gerçek bir Python <a href="https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile" class="external-link" target="_blank">`SpooledTemporaryFile`</a> nesnesi sunar.

### `UploadFile`

`UploadFile` şu niteliklere sahiptir:

* `filename`: Yüklenen orijinal dosya adını içeren bir `str` (örn. `myimage.jpg`).
* `content_type`: İçerik tipini (MIME tipi / medya tipi) içeren bir `str` (örn. `image/jpeg`).
* `file`: Bir <a href="https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile" class="external-link" target="_blank">`SpooledTemporaryFile`</a> (<a href="https://docs.python.org/3/glossary.html#term-file-like-object" class="external-link" target="_blank">dosya benzeri</a> bir nesne). Bu, "dosya benzeri" bir nesne bekleyen diğer fonksiyonlara veya kütüphanelere doğrudan iletebileceğiniz gerçek Python dosya nesnesidir.

`UploadFile` şu `async` metotlara sahiptir. Hepsi alttan ilgili dosya metotlarını çağırır (dahili `SpooledTemporaryFile` kullanarak).

* `write(data)`: Dosyaya `data` (`str` veya `bytes`) yazar.
* `read(size)`: Dosyanın `size` (`int`) bayt/karakterini okur.
* `seek(offset)`: Dosyadaki `offset` (`int`) bayt konumuna gider.
    * Örn., `await myfile.seek(0)` dosyanın başına gider.
    * Bu, `await myfile.read()` komutunu bir kez çalıştırıp ardından içeriği tekrar okumanız gerektiğinde özellikle kullanışlıdır.
* `close()`: Dosyayı kapatır.

Tüm bu metotlar `async` metotlar olduğundan, onları "await" etmeniz gerekir.

Örneğin, bir `async` *yol operasyonu fonksiyonu* içinde içeriği şu şekilde alabilirsiniz:

```Python
contents = await myfile.read()
```

Normal bir `def` *yol operasyonu fonksiyonu* içindeyseniz, `UploadFile.file`'a doğrudan erişebilirsiniz, örneğin:

```Python
contents = myfile.file.read()
```

/// note | `async` Teknik Detaylar

`async` metotları kullandığınızda, **FastAPI** dosya metotlarını bir iş parçacığı havuzunda çalıştırır ve onları bekler.

///

/// note | Starlette Teknik Detaylar

**FastAPI**'nin `UploadFile`'ı doğrudan **Starlette**'in `UploadFile`'ından miras alır, ancak **Pydantic** ve FastAPI'nin diğer parçalarıyla uyumlu hale getirmek için bazı gerekli kısımlar ekler.

///

## "Form Verisi" nedir

HTML formlarının (`<form></form>`) verileri sunucuya gönderme şekli normalde bu veriler için "özel" bir kodlama kullanır, JSON'dan farklıdır.

**FastAPI**, bu verileri JSON yerine doğru yerden okumayı sağlayacaktır.

/// note | Teknik Detaylar

Formlardan gelen veriler, dosya içermediğinde normalde `application/x-www-form-urlencoded` "medya tipi" kullanılarak kodlanır.

Ancak form dosyalar içerdiğinde, `multipart/form-data` olarak kodlanır. `File` kullanırsanız, **FastAPI** dosyaları gövdenin doğru bölümünden alması gerektiğini bilecektir.

Bu kodlamalar ve form alanları hakkında daha fazla bilgi edinmek istiyorsanız, <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST" class="external-link" target="_blank"><abbr title="Mozilla Developer Network">MDN</abbr> web belgelerinde <code>POST</code></a> sayfasına gidin.

///

/// warning

Bir *yol operasyonunda* birden fazla `File` ve `Form` parametresi bildirebilirsiniz, ancak JSON olarak almayı beklediğiniz `Body` alanlarını da bildiremezsiniz, çünkü istek gövdesi `application/json` yerine `multipart/form-data` kullanılarak kodlanmış olacaktır.

Bu **FastAPI**'nin bir sınırlaması değil, HTTP protokolünün bir parçasıdır.

///

## İsteğe Bağlı Dosya Yükleme

Standart tip açıklamalarını kullanarak ve varsayılan değeri `None` olarak ayarlayarak bir dosyayı isteğe bağlı yapabilirsiniz:

{* ../../docs_src/request_files/tutorial001_02_an_py310.py hl[9,17] *}

## Ek Meta Verili `UploadFile`

Ek meta veri ayarlamak için `UploadFile` ile `File()`'ı da kullanabilirsiniz:

{* ../../docs_src/request_files/tutorial001_03_an_py39.py hl[9,15] *}

## Birden Fazla Dosya Yükleme

Aynı anda birden fazla dosya yüklemek mümkündür.

Bunlar "form verisi" kullanılarak gönderilen aynı "form alanı" ile ilişkilendirilecektir.

Bunu kullanmak için, `bytes` veya `UploadFile` listesi bildirin:

{* ../../docs_src/request_files/tutorial002_an_py39.py hl[10,15] *}

Bildirildiği gibi, bir `bytes` veya `UploadFile` `list`'i alacaksınız.

/// note | Teknik Detaylar

`from starlette.responses import HTMLResponse` ifadesini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için aynı `starlette.responses`'ı `fastapi.responses` olarak sunar. Ancak mevcut yanıtların çoğu doğrudan Starlette'ten gelir.

///

### Ek Meta Verili Birden Fazla Dosya Yükleme

Ve daha önce olduğu gibi, `UploadFile` için bile ek parametreler ayarlamak için `File()`'ı kullanabilirsiniz:

{* ../../docs_src/request_files/tutorial003_an_py39.py hl[11,18:20] *}

## Özet

İstekte form verisi olarak yüklenecek dosyaları bildirmek için `File`, `bytes` ve `UploadFile` kullanın.
