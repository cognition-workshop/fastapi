# WebSocket'ler

**FastAPI** ile <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API" class="external-link" target="_blank">WebSocket'leri</a> kullanabilirsiniz.

## `WebSockets`'i yükleyin

[Sanal ortamınızı](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve `websockets`'i yükleyin:

<div class="termy">

```console
$ pip install websockets

---> 100%
```

</div>

## WebSocket istemcisi

### Üretimde

Üretim sisteminizde, muhtemelen React, Vue.js veya Angular gibi modern bir framework ile oluşturulmuş bir frontend'iniz vardır.

Ve backend'inizle WebSocket'ler kullanarak iletişim kurmak için muhtemelen frontend'inizin yardımcı araçlarını kullanırsınız.

Veya WebSocket backend'inizle doğrudan yerel kodda iletişim kuran yerel bir mobil uygulamanız olabilir.

Veya WebSocket uç noktasıyla iletişim kurmanın başka bir yolunuz olabilir.

---

Ama bu örnek için, çok basit bir HTML belgesi ve biraz JavaScript kullanacağız, hepsi uzun bir dize içinde.

Bu, elbette optimal değildir ve üretimde kullanmazsınız.

Üretimde yukarıdaki seçeneklerden birine sahip olursunuz.

Ama WebSocket'lerin sunucu tarafına odaklanmanın ve çalışan bir örneğe sahip olmanın en basit yoludur:

{* ../../docs_src/websockets/tutorial001.py hl[2,6:38,41:43] *}

## Bir `websocket` oluşturun

**FastAPI** uygulamanızda bir `websocket` oluşturun:

{* ../../docs_src/websockets/tutorial001.py hl[1,46:47] *}

/// note | Teknik Detaylar

`from starlette.websockets import WebSocket` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `WebSocket`'i doğrudan sağlar. Ama doğrudan Starlette'den gelir.

///

## Mesajları bekleyin ve gönderin

WebSocket rotanızda mesajları `await` edebilir ve mesaj gönderebilirsiniz.

{* ../../docs_src/websockets/tutorial001.py hl[48:52] *}

İkili (binary), metin ve JSON verisi alabilir ve gönderebilirsiniz.

## Deneyin

Dosyanız `main.py` olarak adlandırılmışsa, uygulamanızı şu şekilde çalıştırın:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Tarayıcınızı <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> adresinde açın.

Basit bir sayfa göreceksiniz:

<img src="/img/tutorial/websockets/image01.png">

Giriş kutusuna mesajlar yazabilir ve gönderebilirsiniz:

<img src="/img/tutorial/websockets/image02.png">

Ve WebSocket'li **FastAPI** uygulamanız geri yanıt verecektir:

<img src="/img/tutorial/websockets/image03.png">

Birçok mesaj gönderebilir (ve alabilirsiniz):

<img src="/img/tutorial/websockets/image04.png">

Ve hepsi aynı WebSocket bağlantısını kullanacaktır.

## `Depends` ve diğerlerini kullanma

WebSocket uç noktalarında `fastapi`'den şunları içe aktarabilir ve kullanabilirsiniz:

* `Depends`
* `Security`
* `Cookie`
* `Header`
* `Path`
* `Query`

Diğer FastAPI uç noktaları/*yol operasyonları* için olduğu gibi aynı şekilde çalışırlar:

{* ../../docs_src/websockets/tutorial002_an_py310.py hl[68:69,82] *}

/// info

Bu bir WebSocket olduğundan, `HTTPException` yükseltmek gerçekten mantıklı değil, bunun yerine `WebSocketException` yükseltiyoruz.

<a href="https://tools.ietf.org/html/rfc6455#section-7.4.1" class="external-link" target="_blank">Spesifikasyonda tanımlanan geçerli kodlardan</a> bir kapatma kodu kullanabilirsiniz.

///

### Bağımlılıklar ile WebSocket'leri deneyin

Dosyanız `main.py` olarak adlandırılmışsa, uygulamanızı şu şekilde çalıştırın:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Tarayıcınızı <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> adresinde açın.

Orada şunları ayarlayabilirsiniz:

* Yolda kullanılan "Item ID".
* Sorgu parametresi olarak kullanılan "Token".

/// tip

Sorgu `token`'ının bir bağımlılık tarafından ele alınacağına dikkat edin.

///

Bununla WebSocket'e bağlanabilir ve ardından mesaj gönderip alabilirsiniz:

<img src="/img/tutorial/websockets/image05.png">

## Bağlantı kesintilerini ve birden fazla istemciyi ele alma

Bir WebSocket bağlantısı kapatıldığında, `await websocket.receive_text()` bir `WebSocketDisconnect` istisnası yükseltir ve bunu bu örnekteki gibi yakalayabilir ve ele alabilirsiniz.

{* ../../docs_src/websockets/tutorial003_py39.py hl[79:81] *}

Denemek için:

* Uygulamayı birkaç tarayıcı sekmesiyle açın.
* Onlardan mesajlar yazın.
* Sonra sekmelerden birini kapatın.

Bu, `WebSocketDisconnect` istisnasını yükseltir ve diğer tüm istemciler şöyle bir mesaj alır:

```
Client #1596980209979 left the chat
```

/// tip

Yukarıdaki uygulama, birkaç WebSocket bağlantısına mesaj göndermeyi ve yayınlamayı nasıl ele alacağınızı göstermek için minimal ve basit bir örnektir.

Ama her şeyin bellekte, tek bir listede ele alındığı için, yalnızca süreç çalışırken çalışacağını ve yalnızca tek bir süreçle çalışacağını unutmayın.

FastAPI ile kolayca entegre olabilecek ama daha sağlam, Redis, PostgreSQL veya diğerleri tarafından desteklenen bir şeye ihtiyacınız varsa, <a href="https://github.com/encode/broadcaster" class="external-link" target="_blank">encode/broadcaster</a>'a bakın.

///

## Daha fazla bilgi

Seçenekler hakkında daha fazla bilgi edinmek için Starlette'in belgelerine bakın:

* <a href="https://www.starlette.io/websockets/" class="external-link" target="_blank">`WebSocket` sınıfı</a>.
* <a href="https://www.starlette.io/endpoints/#websocketendpoint" class="external-link" target="_blank">Sınıf tabanlı WebSocket ele alma</a>.
