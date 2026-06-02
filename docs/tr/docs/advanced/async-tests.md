# Asenkron Testler

**FastAPI** uygulamalarınızı sağlanan `TestClient` ile nasıl test edeceğinizi zaten gördünüz. Şimdiye kadar, `async` fonksiyonları kullanmadan yalnızca senkron testlerin nasıl yazılacağını gördünüz.

Testlerinizde asenkron fonksiyonları kullanabilmek yararlı olabilir, örneğin veritabanınızı asenkron olarak sorguladığınızda. FastAPI uygulamanıza istek göndermeyi test etmek ve ardından bir asenkron veritabanı kütüphanesi kullanırken backend'inizin doğru veriyi veritabanına başarıyla yazdığını doğrulamak istediğinizi hayal edin.

Bunu nasıl çalıştırabileceğimize bakalım.

## pytest.mark.anyio

Testlerimizde asenkron fonksiyonları çağırmak istiyorsak, test fonksiyonlarımızın asenkron olması gerekir. AnyIO bunun için düzgün bir eklenti sağlar ve bazı test fonksiyonlarının asenkron olarak çağrılması gerektiğini belirtmemize olanak tanır.

## HTTPX

**FastAPI** uygulamanız normal `def` fonksiyonları kullanıyor olsa bile `async def` yerine, altta yine de bir `async` uygulamadır.

`TestClient`, standart pytest kullanarak normal `def` test fonksiyonlarınızda asenkron FastAPI uygulamasını çağırmak için içeride biraz sihir yapar. Ama asenkron fonksiyonlar içinde kullandığımızda bu sihir artık çalışmaz. Testlerimizi asenkron olarak çalıştırarak, test fonksiyonlarımız içinde artık `TestClient`'ı kullanamayız.

`TestClient`, <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a>'e dayanmaktadır ve neyse ki, API'yi test etmek için onu doğrudan kullanabiliriz.

## Örnek

Basit bir örnek için, [Daha Büyük Uygulamalar](../tutorial/bigger-applications.md){.internal-link target=_blank} ve [Test Etme](../tutorial/testing.md){.internal-link target=_blank}'de açıklanan dosya yapısına benzer bir yapıyı düşünelim:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
```

`main.py` dosyası şunu içerir:

{* ../../docs_src/async_tests/main.py *}

`test_main.py` dosyası `main.py` için testleri içerir, şimdi şöyle görünebilir:

{* ../../docs_src/async_tests/test_main.py *}

## Çalıştırın

Testlerinizi her zamanki gibi şu şekilde çalıştırabilirsiniz:

<div class="termy">

```console
$ pytest

---> 100%
```

</div>

## Ayrıntılı

`@pytest.mark.anyio` işaretçisi pytest'e bu test fonksiyonunun asenkron olarak çağrılması gerektiğini söyler:

{* ../../docs_src/async_tests/test_main.py hl[7] *}

/// tip

Test fonksiyonunun artık `TestClient`'ı kullanırken olduğu gibi sadece `def` değil `async def` olduğuna dikkat edin.

///

Ardından uygulama ile bir `AsyncClient` oluşturabilir ve `await` kullanarak ona asenkron istekler gönderebiliriz.

{* ../../docs_src/async_tests/test_main.py hl[9:12] *}

Bu şunun eşdeğeridir:

```Python
response = client.get('/')
```

...`TestClient` ile isteklerimizi yapmak için kullandığımız.

/// tip

Yeni `AsyncClient` ile async/await kullandığımıza dikkat edin - istek asenkrondur.

///

/// warning

Uygulamanız yaşam döngüsü olaylarına dayanıyorsa, `AsyncClient` bu olayları tetiklemeyecektir. Tetiklenmelerini sağlamak için <a href="https://github.com/florimondmanca/asgi-lifespan#usage" class="external-link" target="_blank">florimondmanca/asgi-lifespan</a>'dan `LifespanManager` kullanın.

///

## Diğer Asenkron Fonksiyon Çağrıları

Test fonksiyonu artık asenkron olduğundan, testlerinizde FastAPI uygulamanıza istek göndermenin yanı sıra diğer `async` fonksiyonları da çağırabilir (ve `await` edebilirsiniz), tam da kodunuzda başka herhangi bir yerde çağıracağınız gibi.

/// tip

Testlerinizde asenkron fonksiyon çağrılarını entegre ederken `RuntimeError: Task attached to a different loop` hatasıyla karşılaşırsanız (örneğin <a href="https://stackoverflow.com/questions/41584243/runtimeerror-task-attached-to-a-different-loop" class="external-link" target="_blank">MongoDB'nin MotorClient'ını</a> kullanırken), bir olay döngüsüne ihtiyaç duyan nesneleri yalnızca asenkron fonksiyonlar içinde örneklemeyi unutmayın, örneğin bir `'@app.on_event("startup")` geri çağrısında.

///
