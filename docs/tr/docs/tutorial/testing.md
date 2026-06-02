# Test Etme

<a href="https://www.starlette.io/testclient/" class="external-link" target="_blank">Starlette</a> sayesinde, **FastAPI** uygulamalarını test etmek kolay ve keyiflidir.

<a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a>'e dayanmaktadır, bu da Requests'e dayalı olarak tasarlanmıştır, bu yüzden çok tanıdık ve sezgiseldir.

Bununla, <a href="https://docs.pytest.org/" class="external-link" target="_blank">pytest</a>'i doğrudan **FastAPI** ile kullanabilirsiniz.

## `TestClient` kullanma

/// info

`TestClient` kullanmak için, önce <a href="https://www.python-httpx.org" class="external-link" target="_blank">`httpx`</a>'i yükleyin.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından yükleyin, örneğin:

```console
$ pip install httpx
```

///

`TestClient`'ı içe aktarın.

**FastAPI** uygulamanızı ileterek bir `TestClient` oluşturun.

Adı `test_` ile başlayan fonksiyonlar oluşturun (bu standart `pytest` kurallarıdır).

`TestClient` nesnesini `httpx` ile yaptığınız gibi kullanın.

Kontrol etmeniz gereken standart Python ifadeleriyle basit `assert` ifadeleri yazın (yine, standart `pytest`).

{* ../../docs_src/app_testing/tutorial001.py hl[2,12,15:18] *}

/// tip

Test fonksiyonlarının `async def` değil, normal `def` olduğuna dikkat edin.

Ve istemciye yapılan çağrılar da `await` kullanmayan normal çağrılardır.

Bu, `pytest`'i komplikasyonsuz doğrudan kullanmanıza olanak tanır.

///

/// note | Teknik Detaylar

`from starlette.testclient import TestClient` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.testclient`'ı `fastapi.testclient` olarak sağlar. Ancak doğrudan Starlette'den gelir.

///

/// tip

FastAPI uygulamanıza istek göndermenin yanı sıra testlerinizde `async` fonksiyonlar çağırmak istiyorsanız (ör. asenkron veritabanı fonksiyonları), gelişmiş eğitimdeki [Async Testler](../advanced/async-tests.md){.internal-link target=_blank}'e bakın.

///

## Testleri ayırma

Gerçek bir uygulamada, muhtemelen testlerinizi farklı bir dosyada bulundurursunuz.

Ve **FastAPI** uygulamanız da birçok dosya/modülden oluşabilir, vb.

### **FastAPI** uygulama dosyası

[Daha Büyük Uygulamalar](bigger-applications.md){.internal-link target=_blank}'da açıklandığı gibi bir dosya yapınız olduğunu varsayalım:

```
.
├── app
│   ├── __init__.py
│   └── main.py
```

`main.py` dosyasında **FastAPI** uygulamanız var:


{* ../../docs_src/app_testing/main.py *}

### Test dosyası

Ardından testlerinizle birlikte bir `test_main.py` dosyanız olabilir. Aynı Python paketinde (aynı dizinde bir `__init__.py` dosyasıyla) yaşayabilir:

``` hl_lines="5"
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

Bu dosya aynı pakette olduğundan, `main` modülünden (`main.py`) `app` nesnesini içe aktarmak için göreceli içe aktarmalar kullanabilirsiniz:

{* ../../docs_src/app_testing/test_main.py hl[3] *}


...ve testlerin kodu daha önce olduğu gibidir.

## Test etme: genişletilmiş örnek

Şimdi bu örneği genişletelim ve farklı bölümlerin nasıl test edileceğini görmek için daha fazla ayrıntı ekleyelim.

### Genişletilmiş **FastAPI** uygulama dosyası

Daha önce olduğu gibi aynı dosya yapısıyla devam edelim:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

Şimdi `main.py` dosyasının bazı başka **yol operasyonlarına** sahip olduğunu varsayalım.

Hata döndürebilecek bir `GET` operasyonu var.

Birçok hata döndürebilecek bir `POST` operasyonu var.

Her iki *yol operasyonu* da bir `X-Token` başlığı gerektirir.

//// tab | Python 3.10+

```Python
{!> ../../docs_src/app_testing/app_b_an_py310/main.py!}
```

////

//// tab | Python 3.9+

```Python
{!> ../../docs_src/app_testing/app_b_an_py39/main.py!}
```

////

//// tab | Python 3.8+

```Python
{!> ../../docs_src/app_testing/app_b_an/main.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
{!> ../../docs_src/app_testing/app_b_py310/main.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python
{!> ../../docs_src/app_testing/app_b/main.py!}
```

////

### Genişletilmiş test dosyası

Ardından `test_main.py`'yi genişletilmiş testlerle güncelleyebilirsiniz:

{* ../../docs_src/app_testing/app_b/test_main.py *}


İstemcinin istekte bilgi iletmesi gerektiğinde ve nasıl yapılacağını bilmediğinizde, `httpx`'te nasıl yapılacağını, hatta `requests`'te nasıl yapılacağını arayabilirsiniz (Google), çünkü HTTPX'in tasarımı Requests'in tasarımına dayanmaktadır.

Ardından testlerinizde aynı şeyi yaparsınız.

Örn.:

* Bir *yol* veya *sorgu* parametresi iletmek için, URL'nin kendisine ekleyin.
* Bir JSON gövdesi iletmek için, `json` parametresine bir Python nesnesi (ör. bir `dict`) iletin.
* JSON yerine *Form Verisi* göndermeniz gerekiyorsa, bunun yerine `data` parametresini kullanın.
* *Başlıklar* iletmek için, `headers` parametresinde bir `dict` kullanın.
* *Çerezler* için, `cookies` parametresinde bir `dict`.

Backend'e veri iletme hakkında daha fazla bilgi için (`httpx` veya `TestClient` kullanarak) <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX belgelerine</a> bakın.

/// info

`TestClient`'ın JSON'a dönüştürülebilen veri aldığını, Pydantic modelleri almadığını unutmayın.

Testinizde bir Pydantic modeliniz varsa ve test sırasında verilerini uygulamaya göndermek istiyorsanız, [JSON Uyumlu Kodlayıcı](encoder.md){.internal-link target=_blank}'da açıklanan `jsonable_encoder`'ı kullanabilirsiniz.

///

## Çalıştırın

Bundan sonra, sadece `pytest`'i yüklemeniz gerekir.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından yükleyin, örneğin:

<div class="termy">

```console
$ pip install pytest

---> 100%
```

</div>

Dosyaları ve testleri otomatik olarak algılayacak, çalıştıracak ve sonuçları size bildirecektir.

Testleri şu şekilde çalıştırın:

<div class="termy">

```console
$ pytest

================ test session starts ================
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/user/code/superawesome-cli/app
plugins: forked-1.1.3, xdist-1.31.0, cov-2.8.1
collected 6 items

---> 100%

test_main.py <span style="color: green; white-space: pre;">......                            [100%]</span>

<span style="color: green;">================= 1 passed in 0.03s =================</span>
```

</div>
