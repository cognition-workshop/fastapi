# Sorgu Parametre Modelleri

Birbirine bağlı bir grup **sorgu parametreniz** varsa, bunları bildirmek için bir **Pydantic modeli** oluşturabilirsiniz.

Bu, **modeli** **birden fazla yerde** **yeniden kullanmanıza** ve ayrıca tüm parametreler için doğrulama ve meta verileri bir seferde bildirmenize olanak tanır. 😎

/// note

Bu, FastAPI `0.115.0` sürümünden beri desteklenmektedir. 🤓

///

## Pydantic Modeli ile Sorgu Parametreleri

İhtiyacınız olan **sorgu parametrelerini** bir **Pydantic modelinde** bildirin, ardından parametreyi `Query` olarak bildirin:

{* ../../docs_src/query_param_models/tutorial001_an_py310.py hl[9:13,17] *}

**FastAPI**, istekteki **sorgu parametrelerinden** **her alan** için verileri **çıkaracak** ve size tanımladığınız Pydantic modelini verecektir.

## Belgeleri kontrol edin

Sorgu parametrelerini `/docs` adresindeki belge arayüzünde görebilirsiniz:

<div class="screenshot">
<img src="/img/tutorial/query-param-models/image01.png">
</div>

## Ek Sorgu Parametrelerini Yasaklama

Bazı özel kullanım durumlarında (muhtemelen çok yaygın değil), almak istediğiniz sorgu parametrelerini **kısıtlamak** isteyebilirsiniz.

Herhangi bir `extra` alanı `forbid` etmek için Pydantic'in model yapılandırmasını kullanabilirsiniz:

{* ../../docs_src/query_param_models/tutorial002_an_py310.py hl[10] *}

Bir istemci **sorgu parametrelerinde** bazı **ek** veri göndermeye çalışırsa, bir **hata** yanıtı alacaktır.

Örneğin, istemci `plumbus` değerine sahip bir `tool` sorgu parametresi göndermeye çalışırsa:

```http
https://example.com/items/?limit=10&tool=plumbus
```

`tool` sorgu parametresinin izin verilmediğini söyleyen bir **hata** yanıtı alacaktır:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["query", "tool"],
            "msg": "Extra inputs are not permitted",
            "input": "plumbus"
        }
    ]
}
```

## Özet

**FastAPI**'de **sorgu parametrelerini** bildirmek için **Pydantic modellerini** kullanabilirsiniz. 😎

/// tip

Spoiler uyarısı: Pydantic modellerini çerezleri ve header'ları bildirmek için de kullanabilirsiniz, ancak bunu öğreticinin ilerleyen kısımlarında okuyacaksınız. 🤫

///
