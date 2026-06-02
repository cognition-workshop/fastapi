# Yol Parametreleri

Python format stringleri tarafından kullanılan aynı söz dizimi ile yol "parametreleri" veya "değişkenleri" bildirebilirsiniz:

{* ../../docs_src/path_params/tutorial001.py hl[6:7] *}

`item_id` yol parametresinin değeri, fonksiyonunuza `item_id` argümanı olarak iletilecektir.

Bu örneği çalıştırıp <a href="http://127.0.0.1:8000/items/foo" class="external-link" target="_blank">http://127.0.0.1:8000/items/foo</a> adresine giderseniz, şöyle bir yanıt göreceksiniz:

```JSON
{"item_id":"foo"}
```

## Tipli yol parametreleri

Standart Python tip açıklamalarını kullanarak fonksiyonda bir yol parametresinin tipini bildirebilirsiniz:

{* ../../docs_src/path_params/tutorial002.py hl[7] *}

Bu durumda, `item_id` bir `int` olarak bildirilmiştir.

/// check

Bu, fonksiyonunuz içinde hata kontrolleri, tamamlama vb. ile editör desteği sağlayacaktır.

///

## Veri <abbr title="serileştirme, ayrıştırma, marshalling olarak da bilinir">dönüştürme</abbr>

Bu örneği çalıştırıp tarayıcınızı <a href="http://127.0.0.1:8000/items/3" class="external-link" target="_blank">http://127.0.0.1:8000/items/3</a> adresinde açarsanız, şöyle bir yanıt göreceksiniz:

```JSON
{"item_id":3}
```

/// check

Fonksiyonunuzun aldığı (ve döndürdüğü) değerin `3` olduğuna dikkat edin, bir Python `int` olarak, string `"3"` değil.

Yani, bu tip bildirimi ile **FastAPI** size otomatik istek <abbr title="HTTP isteğinden gelen stringi Python verisine dönüştürme">"ayrıştırma"</abbr> sağlar.

///

## Veri doğrulama

Ancak tarayıcıda <a href="http://127.0.0.1:8000/items/foo" class="external-link" target="_blank">http://127.0.0.1:8000/items/foo</a> adresine giderseniz, güzel bir HTTP hatası göreceksiniz:

```JSON
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "foo",
      "url": "https://errors.pydantic.dev/2.1/v/int_parsing"
    }
  ]
}
```

çünkü `item_id` yol parametresi `"foo"` değerine sahipti ve bu bir `int` değildir.

`int` yerine bir `float` verseniz de aynı hata görünürdü: <a href="http://127.0.0.1:8000/items/4.2" class="external-link" target="_blank">http://127.0.0.1:8000/items/4.2</a>

/// check

Yani, aynı Python tip bildirimi ile **FastAPI** size veri doğrulama sağlar.

Hatanın ayrıca doğrulamanın tam olarak nerede geçmediğini açıkça belirttiğine dikkat edin.

Bu, API'nizle etkileşimde bulunan kodu geliştirirken ve hata ayıklarken inanılmaz derecede yardımcıdır.

///

## Belgelendirme

Tarayıcınızı <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> adresinde açtığınızda, otomatik, etkileşimli bir API belgelendirmesi göreceksiniz:

<img src="/img/tutorial/path-params/image01.png">

/// check

Yine, aynı Python tip bildirimi ile **FastAPI** size otomatik, etkileşimli belgelendirme sağlar (Swagger UI'ı entegre ederek).

Yol parametresinin bir tamsayı olarak bildirildiğine dikkat edin.

///

## Standartlara dayalı avantajlar, alternatif belgelendirme

Oluşturulan şema <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md" class="external-link" target="_blank">OpenAPI</a> standardından geldiği için birçok uyumlu araç vardır.

Bu nedenle, **FastAPI**'nin kendisi <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> adresinden erişebileceğiniz bir alternatif API belgelendirmesi (ReDoc kullanarak) sağlar:

<img src="/img/tutorial/path-params/image02.png">

Aynı şekilde, birçok uyumlu araç vardır. Birçok dil için kod oluşturma araçları dahil.

## Pydantic

Tüm veri doğrulama, arka planda <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> tarafından gerçekleştirilir, böylece onun tüm avantajlarından yararlanırsınız. Ve emin ellerde olduğunuzu bilirsiniz.

Aynı tip bildirimlerini `str`, `float`, `bool` ve diğer birçok karmaşık veri tipiyle kullanabilirsiniz.

Bunlardan birkaçı öğreticinin sonraki bölümlerinde incelenmektedir.

## Sıralama önemlidir

*Yol operasyonları* oluştururken, sabit bir yola sahip olduğunuz durumlarla karşılaşabilirsiniz.

`/users/me` gibi, diyelim ki mevcut kullanıcı hakkında veri almak için.

Ve sonra bir kullanıcı ID'si ile belirli bir kullanıcı hakkında veri almak için `/users/{user_id}` yoluna da sahip olabilirsiniz.

*Yol operasyonları* sırayla değerlendirildiği için, `/users/me` yolunun `/users/{user_id}` yolundan önce bildirildiğinden emin olmanız gerekir:

{* ../../docs_src/path_params/tutorial003.py hl[6,11] *}

Aksi takdirde, `/users/{user_id}` yolu `/users/me` için de eşleşir ve `"me"` değerine sahip bir `user_id` parametresi aldığını "düşünür".

Benzer şekilde, bir yol operasyonunu yeniden tanımlayamazsınız:

{* ../../docs_src/path_params/tutorial003b.py hl[6,11] *}

Yol ilk olarak eşleştiği için her zaman ilki kullanılacaktır.

## Önceden tanımlanmış değerler

Bir *yol parametresi* alan bir *yol operasyonunuz* varsa, ancak olası geçerli *yol parametresi* değerlerinin önceden tanımlanmış olmasını istiyorsanız, standart bir Python <abbr title="Numaralandırma">`Enum`</abbr> kullanabilirsiniz.

### Bir `Enum` sınıfı oluşturun

`Enum`'u içe aktarın ve `str` ile `Enum`'dan miras alan bir alt sınıf oluşturun.

`str`'den miras alarak API belgeleri değerlerin `string` tipinde olması gerektiğini bilecek ve doğru şekilde görüntüleyebilecektir.

Ardından sabit değerlere sahip sınıf nitelikleri oluşturun, bunlar mevcut geçerli değerler olacaktır:

{* ../../docs_src/path_params/tutorial005.py hl[1,6:9] *}

/// info

<a href="https://docs.python.org/3/library/enum.html" class="external-link" target="_blank">Numaralandırmalar (veya enum'lar) Python'da</a> 3.4 sürümünden beri mevcuttur.

///

/// tip

Merak ediyorsanız, "AlexNet", "ResNet" ve "LeNet" sadece Makine Öğrenmesi <abbr title="Teknik olarak, Derin Öğrenme model mimarileri">modelleri</abbr>nin isimleridir.

///

### Bir *yol parametresi* bildirin

Ardından oluşturduğunuz enum sınıfını (`ModelName`) kullanarak bir tip açıklaması ile bir *yol parametresi* oluşturun:

{* ../../docs_src/path_params/tutorial005.py hl[16] *}

### Belgeleri kontrol edin

*Yol parametresi* için mevcut değerler önceden tanımlandığından, etkileşimli belgeler bunları güzel bir şekilde gösterebilir:

<img src="/img/tutorial/path-params/image03.png">

### Python *numaralandırmalarıyla* çalışma

*Yol parametresinin* değeri bir *numaralandırma üyesi* olacaktır.

#### *Numaralandırma üyelerini* karşılaştırın

Bunu oluşturduğunuz enum `ModelName`'deki *numaralandırma üyesi* ile karşılaştırabilirsiniz:

{* ../../docs_src/path_params/tutorial005.py hl[17] *}

#### *Numaralandırma değerini* alın

Gerçek değeri (bu durumda bir `str`) `model_name.value` kullanarak veya genel olarak `your_enum_member.value` ile alabilirsiniz:

{* ../../docs_src/path_params/tutorial005.py hl[20] *}

/// tip

`"lenet"` değerine `ModelName.lenet.value` ile de erişebilirsiniz.

///

#### *Numaralandırma üyelerini* döndürün

*Yol operasyonunuzdan*, hatta bir JSON gövdesinin içinde iç içe (örneğin bir `dict`) *enum üyeleri* döndürebilirsiniz.

İstemciye döndürmeden önce karşılık gelen değerlerine (bu durumda stringler) dönüştürüleceklerdir:

{* ../../docs_src/path_params/tutorial005.py hl[18,21,23] *}

İstemcinizde şöyle bir JSON yanıtı alacaksınız:

```JSON
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```

## Yol içeren yol parametreleri

Diyelim ki `/files/{file_path}` yoluna sahip bir *yol operasyonunuz* var.

Ancak `file_path`'in kendisinin `home/johndoe/myfile.txt` gibi bir *yol* içermesine ihtiyacınız var.

Yani, bu dosyanın URL'si şöyle bir şey olurdu: `/files/home/johndoe/myfile.txt`.

### OpenAPI desteği

OpenAPI, bir *yol parametresini* içinde bir *yol* içerecek şekilde bildirmenin bir yolunu desteklemez çünkü bu, test edilmesi ve tanımlanması zor senaryolara yol açabilir.

Yine de, bunu **FastAPI**'de Starlette'in dahili araçlarından birini kullanarak yapabilirsiniz.

Ve belgeler yine de çalışır, ancak parametrenin bir yol içermesi gerektiğini söyleyen herhangi bir belgelendirme eklemez.

### Yol dönüştürücü

Starlette'ten doğrudan bir seçenek kullanarak, şöyle bir URL ile bir *yol* içeren bir *yol parametresi* bildirebilirsiniz:

```
/files/{file_path:path}
```

Bu durumda, parametrenin adı `file_path`'tir ve son kısım `:path`, parametrenin herhangi bir *yol* ile eşleşmesi gerektiğini söyler.

Yani, bunu şu şekilde kullanabilirsiniz:

{* ../../docs_src/path_params/tutorial004.py hl[6] *}

/// tip

Parametrenin `/home/johndoe/myfile.txt` içermesine, baştaki eğik çizgi (`/`) ile ihtiyacınız olabilir.

Bu durumda, URL şöyle olurdu: `/files//home/johndoe/myfile.txt`, `files` ve `home` arasında çift eğik çizgi (`//`) ile.

///

## Özet

**FastAPI** ile kısa, sezgisel ve standart Python tip bildirimleri kullanarak şunları elde edersiniz:

* Editör desteği: hata kontrolleri, otomatik tamamlama vb.
* Veri "<abbr title="HTTP isteğinden gelen stringi Python verisine dönüştürme">ayrıştırma</abbr>"
* Veri doğrulama
* API açıklaması ve otomatik belgelendirme

Ve bunları yalnızca bir kez bildirmeniz gerekir.

Bu, alternatif framework'lere kıyasla muhtemelen **FastAPI**'nin ana görünür avantajıdır (ham performans dışında).
