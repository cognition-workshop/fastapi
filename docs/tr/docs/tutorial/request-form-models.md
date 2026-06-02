# Form Modelleri

FastAPI'de **form alanlarını** bildirmek için **Pydantic modellerini** kullanabilirsiniz.

/// info

Formları kullanmak için önce <a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a>'ı yükleyin.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden ve ardından yüklediğinizden emin olun, örneğin:

```console
$ pip install python-multipart
```

///

/// note

Bu, FastAPI `0.113.0` sürümünden beri desteklenmektedir. 🤓

///

## Formlar için Pydantic Modelleri

**Form alanları** olarak almak istediğiniz alanları içeren bir **Pydantic modeli** bildirmeniz ve ardından parametreyi `Form` olarak bildirmeniz yeterlidir:

{* ../../docs_src/request_form_models/tutorial001_an_py39.py hl[9:11,15] *}

**FastAPI**, istekteki **form verilerinden** **her alan** için verileri **çıkaracak** ve size tanımladığınız Pydantic modelini verecektir.

## Belgeleri kontrol edin

Bunu `/docs` adresindeki belge arayüzünde doğrulayabilirsiniz:

<div class="screenshot">
<img src="/img/tutorial/request-form-models/image01.png">
</div>

## Ek Form Alanlarını Yasaklama

Bazı özel kullanım durumlarında (muhtemelen çok yaygın değil), form alanlarını yalnızca Pydantic modelinde bildirilenlerle **kısıtlamak** isteyebilirsiniz. Ve herhangi bir **ek** alanı **yasaklayabilirsiniz**.

/// note

Bu, FastAPI `0.114.0` sürümünden beri desteklenmektedir. 🤓

///

Herhangi bir `extra` alanı `forbid` etmek için Pydantic'in model yapılandırmasını kullanabilirsiniz:

{* ../../docs_src/request_form_models/tutorial002_an_py39.py hl[12] *}

Bir istemci ek veri göndermeye çalışırsa, bir **hata** yanıtı alacaktır.

Örneğin, istemci form alanlarını göndermeye çalışırsa:

* `username`: `Rick`
* `password`: `Portal Gun`
* `extra`: `Mr. Poopybutthole`

`extra` alanının izin verilmediğini söyleyen bir hata yanıtı alacaktır:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["body", "extra"],
            "msg": "Extra inputs are not permitted",
            "input": "Mr. Poopybutthole"
        }
    ]
}
```

## Özet

FastAPI'de form alanlarını bildirmek için Pydantic modellerini kullanabilirsiniz. 😎
