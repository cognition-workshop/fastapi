# Çerez Parametre Modelleri

Birbiriyle ilişkili bir grup **çereziniz** varsa, bunları bildirmek için bir **Pydantic modeli** oluşturabilirsiniz. 🍪

Bu, **modeli** **birden fazla yerde** **yeniden kullanmanıza** ve ayrıca tüm parametreler için doğrulamaları ve meta verileri tek seferde bildirmenize olanak tanır. 😎

/// note

Bu, FastAPI `0.115.0` sürümünden itibaren desteklenmektedir. 🤓

///

/// tip

Aynı teknik `Query`, `Cookie` ve `Header` için de geçerlidir. 😎

///

## Pydantic Modeli ile çerezler

İhtiyacınız olan **çerez** parametrelerini bir **Pydantic modelinde** bildirin ve ardından parametreyi `Cookie` olarak bildirin:

{* ../../docs_src/cookie_param_models/tutorial001_an_py310.py hl[9:12,16] *}

**FastAPI**, istekte alınan **çerezlerden** **her alan** için veriyi **çıkaracak** ve size tanımladığınız Pydantic modelini verecektir.

## Belgeleri kontrol edin

Tanımlanan çerezleri `/docs` adresindeki belgeler arayüzünde görebilirsiniz:

<div class="screenshot">
<img src="/img/tutorial/cookie-param-models/image01.png">
</div>

/// info

**Tarayıcıların çerezleri** özel yollarla ve arka planda işlediğini, **JavaScript**'in bunlara kolayca dokunmasına **izin vermediğini** unutmayın.

`/docs` adresindeki **API belgeleri arayüzüne** giderseniz, *yol operasyonlarınız* için çerezlerin **belgelerini** görebilirsiniz.

Ancak **veriyi doldursa** ve "Çalıştır"a tıklasanız bile, belgeler arayüzü **JavaScript** ile çalıştığından çerezler gönderilmeyecek ve hiçbir değer yazmamışsınız gibi bir **hata** mesajı göreceksiniz.

///

## Ekstra çerezleri yasaklayın

Bazı özel kullanım durumlarında (muhtemelen çok yaygın değildir), almak istediğiniz çerezleri **kısıtlamak** isteyebilirsiniz.

API'niz artık kendi <abbr title="Bu bir şaka, her ihtimale karşı. Çerez onaylarıyla hiçbir ilgisi yok, ama API'nin bile zavallı çerezleri reddedebilmesi komik. Bir çerez alın. 🍪">çerez onayını</abbr> kontrol etme gücüne sahiptir. 🤪🍪

Herhangi bir `extra` alanı `forbid` etmek için Pydantic'in model yapılandırmasını kullanabilirsiniz:

{* ../../docs_src/cookie_param_models/tutorial002_an_py39.py hl[10] *}

Bir istemci bazı **ekstra çerezler** göndermeye çalışırsa, bir **hata** yanıtı alacaktır.

Zavallı çerez banner'ları, <abbr title="Bu başka bir şaka. Bana aldırmayın. Çereziniz için biraz kahve alın. ☕">API'nin reddetmesi</abbr> için onayınızı almak adına gösterdikleri tüm çabalarıyla. 🍪

Örneğin, istemci `good-list-please` değerine sahip bir `santa_tracker` çerezi göndermeye çalışırsa, istemci `santa_tracker` <abbr title="Noel Baba çerez eksikliğini onaylamıyor. 🎅 Tamam, artık çerez şakası yok.">çerezine izin verilmediğini</abbr> söyleyen bir **hata** yanıtı alacaktır:

```json
{
    "detail": [
        {
            "type": "extra_forbidden",
            "loc": ["cookie", "santa_tracker"],
            "msg": "Extra inputs are not permitted",
            "input": "good-list-please",
        }
    ]
}
```

## Özet

**FastAPI**'de <abbr title="Gitmeden önce son bir çerez alın. 🍪">**çerezleri**</abbr> bildirmek için **Pydantic modelleri** kullanabilirsiniz. 😎
