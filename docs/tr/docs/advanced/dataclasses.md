# Dataclass'ları Kullanma

FastAPI, **Pydantic** üzerine inşa edilmiştir ve size istekleri ve yanıtları bildirmek için Pydantic modellerini nasıl kullanacağınızı gösteriyordum.

Ancak FastAPI, <a href="https://docs.python.org/3/library/dataclasses.html" class="external-link" target="_blank">`dataclasses`</a>'ı da aynı şekilde kullanmayı destekler:

{* ../../docs_src/dataclasses/tutorial001.py hl[1,7:12,19:20] *}

Bu hala **Pydantic** sayesinde desteklenmektedir, çünkü <a href="https://docs.pydantic.dev/latest/concepts/dataclasses/#use-of-stdlib-dataclasses-with-basemodel" class="external-link" target="_blank">`dataclasses` için dahili desteği</a> vardır.

Yani, yukarıdaki kodda Pydantic'i açıkça kullanmasa bile, FastAPI bu standart dataclass'ları Pydantic'in kendi dataclass çeşidine dönüştürmek için Pydantic'i kullanmaktadır.

Ve tabii ki aynı şeyleri destekler:

* veri doğrulama
* veri serileştirme
* veri belgeleme, vb.

Bu, Pydantic modelleriyle aynı şekilde çalışır. Ve aslında altta aynı şekilde, Pydantic kullanılarak gerçekleştirilir.

/// info

Dataclass'ların Pydantic modellerinin yapabildiği her şeyi yapamayacağını unutmayın.

Bu yüzden, hala Pydantic modellerini kullanmanız gerekebilir.

Ama elinizde bir sürü dataclass varsa, bunları FastAPI kullanarak bir web API'sini güçlendirmek için kullanmak güzel bir numaradır. 🤓

///

## `response_model`'de Dataclass'lar

`response_model` parametresinde de `dataclasses` kullanabilirsiniz:

{* ../../docs_src/dataclasses/tutorial002.py hl[1,7:13,19] *}

Dataclass otomatik olarak bir Pydantic dataclass'ına dönüştürülecektir.

Bu şekilde, şeması API belgeleri kullanıcı arayüzünde görünecektir:

<img src="/img/tutorial/dataclasses/image01.png">

## İç İçe Veri Yapılarında Dataclass'lar

İç içe veri yapıları oluşturmak için `dataclasses`'ı diğer tip açıklamalarıyla da birleştirebilirsiniz.

Bazı durumlarda, Pydantic'in `dataclasses` versiyonunu kullanmanız gerekebilir. Örneğin, otomatik olarak oluşturulan API belgelerinde hatalarınız varsa.

Bu durumda, standart `dataclasses`'ı `pydantic.dataclasses` ile kolayca değiştirebilirsiniz, bu birebir değiştirmedir:

{* ../../docs_src/dataclasses/tutorial003.py hl[1,5,8:11,14:17,23:25,28] *}

1. Hala standart `dataclasses`'dan `field`'ı içe aktarıyoruz.

2. `pydantic.dataclasses`, `dataclasses` için birebir değiştirmedir.

3. `Author` dataclass'ı bir `Item` dataclass'ları listesi içerir.

4. `Author` dataclass'ı `response_model` parametresi olarak kullanılır.

5. İstek gövdesi olarak dataclass'larla diğer standart tip açıklamalarını kullanabilirsiniz.

    Bu durumda, bir `Item` dataclass'ları listesidir.

6. Burada `items` içeren bir sözlük döndürüyoruz, bu bir dataclass'lar listesidir.

    FastAPI hala veriyi JSON'a <abbr title="veriyi iletilebilecek bir biçime dönüştürme">serileştirme</abbr> yeteneğine sahiptir.

7. Burada `response_model`, bir `Author` dataclass'ları listesinin tip açıklamasını kullanıyor.

    Yine, `dataclasses`'ı standart tip açıklamalarıyla birleştirebilirsiniz.

8. Bu *yol operasyonu fonksiyonunun* `async def` yerine normal `def` kullandığına dikkat edin.

    Her zamanki gibi, FastAPI'de `def` ve `async def`'i gerektiği gibi birleştirebilirsiniz.

    Hangisini ne zaman kullanacağınız hakkında bir hatırlatmaya ihtiyacınız varsa, [`async` ve `await`](../async.md#in-a-hurry){.internal-link target=_blank} hakkındaki belgelerdeki _"Aceleniz mi var?"_ bölümüne bakın.

9. Bu *yol operasyonu fonksiyonu* dataclass döndürmüyor (döndürebilse de), dahili verilerle bir sözlük listesi döndürüyor.

    FastAPI, yanıtı dönüştürmek için `response_model` parametresini (dataclass'ları içeren) kullanacaktır.

Birçok farklı kombinasyonda karmaşık veri yapıları oluşturmak için `dataclasses`'ı diğer tip açıklamalarıyla birleştirebilirsiniz.

Daha fazla spesifik ayrıntı için yukarıdaki kod içi açıklama ipuçlarına bakın.

## Daha Fazla Bilgi

`dataclasses`'ı diğer Pydantic modelleriyle de birleştirebilir, onlardan miras alabilir, kendi modellerinize dahil edebilirsiniz, vb.

Daha fazla bilgi için <a href="https://docs.pydantic.dev/latest/concepts/dataclasses/" class="external-link" target="_blank">Pydantic'in dataclass'lar hakkındaki belgelerine</a> bakın.

## Sürüm

Bu, FastAPI `0.67.0` sürümünden itibaren kullanılabilir. 🔖
