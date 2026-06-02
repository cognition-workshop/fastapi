# Header Parametre Modelleri

Birbirine bağlı bir grup **header parametreniz** varsa, bunları bildirmek için bir **Pydantic modeli** oluşturabilirsiniz.

Bu, **modeli** **birden fazla yerde** **yeniden kullanmanıza** ve ayrıca tüm parametreler için doğrulama ve meta verileri bir seferde bildirmenize olanak tanır. 😎

/// note

Bu, FastAPI `0.115.0` sürümünden beri desteklenmektedir. 🤓

///

## Pydantic Modeli ile Header Parametreleri

İhtiyacınız olan **header parametrelerini** bir **Pydantic modelinde** bildirin, ardından parametreyi `Header` olarak bildirin:

{* ../../docs_src/header_param_models/tutorial001_an_py310.py hl[9:14,18] *}

**FastAPI**, istekteki **header'lardan** **her alan** için verileri **çıkaracak** ve size tanımladığınız Pydantic modelini verecektir.

## Belgeleri kontrol edin

Gerekli header'ları `/docs` adresindeki belge arayüzünde görebilirsiniz:

<div class="screenshot">
<img src="/img/tutorial/header-param-models/image01.png">
</div>

## Ek Header'ları yasaklama

Bazı özel kullanım durumlarında (muhtemelen çok yaygın değil), almak istediğiniz header'ları **kısıtlamak** isteyebilirsiniz.

Herhangi bir `extra` alanı `forbid` etmek için Pydantic'in model yapılandırmasını kullanabilirsiniz:

{* ../../docs_src/header_param_models/tutorial002_an_py310.py hl[10] *}

Bir istemci bazı **ek header'lar** göndermeye çalışırsa, bir **hata** yanıtı alacaktır.

Örneğin, istemci `plumbus` değerine sahip bir `tool` header'ı göndermeye çalışırsa, `tool` header parametresinin izin verilmediğini söyleyen bir **hata** yanıtı alacaktır:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["header", "tool"],
            "msg": "Extra inputs are not permitted",
            "input": "plumbus",
        }
    ]
}
```

## Alt Çizgi Dönüştürmeyi Devre Dışı Bırakma

Normal header parametrelerinde olduğu gibi, parametre adlarında alt çizgi karakterleri olduğunda, bunlar **otomatik olarak tirelere dönüştürülür**.

Örneğin, kodda `save_data` header parametreniz varsa, beklenen HTTP header'ı `save-data` olacaktır ve belgelerde de bu şekilde görünecektir.

Herhangi bir nedenle bu otomatik dönüştürmeyi devre dışı bırakmanız gerekiyorsa, bunu header parametreleri için Pydantic modelleri ile de yapabilirsiniz.

{* ../../docs_src/header_param_models/tutorial003_an_py310.py hl[19] *}

/// warning

`convert_underscores`'ı `False` olarak ayarlamadan önce, bazı HTTP proxy'lerin ve sunucuların alt çizgili header'ların kullanımını yasakladığını unutmayın.

///

## Özet

**FastAPI**'de **header'ları** bildirmek için **Pydantic modellerini** kullanabilirsiniz. 😎
