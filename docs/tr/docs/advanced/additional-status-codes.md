# Ek Durum Kodları

Varsayılan olarak, **FastAPI** yanıtları bir `JSONResponse` kullanarak döndürecek ve *yol operasyonunuzdan* döndürdüğünüz içeriği o `JSONResponse`'un içine koyacaktır.

Varsayılan durum kodunu veya *yol operasyonunuzda* ayarladığınız kodu kullanacaktır.

## Ek durum kodları

Ana kodun yanı sıra ek durum kodları döndürmek istiyorsanız, bunu doğrudan bir `Response` döndürerek yapabilirsiniz, örneğin bir `JSONResponse`, ve ek durum kodunu doğrudan ayarlayabilirsiniz.

Örneğin, öğeleri güncellemeye izin veren ve başarılı olduğunda 200 "OK" HTTP durum kodu döndüren bir *yol operasyonunuz* olsun.

Ama ayrıca yeni öğeleri de kabul etmesini istiyorsunuz. Ve öğeler daha önce mevcut değilse, onları oluşturup 201 "Created" HTTP durum kodu döndürsün.

Bunu başarmak için `JSONResponse`'u içe aktarın ve içeriğinizi doğrudan orada döndürün, istediğiniz `status_code`'u ayarlayarak:

{* ../../docs_src/additional_status_codes/tutorial001_an_py310.py hl[4,25] *}

/// warning

Yukarıdaki örnekte olduğu gibi doğrudan bir `Response` döndürdüğünüzde, doğrudan döndürülecektir.

Bir modelle serileştirilmeyecektir, vb.

İstediğiniz verilere sahip olduğundan ve değerlerin geçerli JSON olduğundan emin olun (`JSONResponse` kullanıyorsanız).

///

/// note | Teknik Detaylar

`from starlette.responses import JSONResponse` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.responses`'ı `fastapi.responses` olarak sağlar. Ancak mevcut yanıtların çoğu doğrudan Starlette'den gelir. `status` için de aynı şey geçerlidir.

///

## OpenAPI ve API belgeleri

Ek durum kodlarını ve yanıtları doğrudan döndürürseniz, bunlar OpenAPI şemasına (API belgeleri) dahil edilmeyecektir, çünkü FastAPI neyi döndüreceğinizi önceden bilmenin bir yoluna sahip değildir.

Ama bunu kodunuzda belgeleyebilirsiniz: [Ek Yanıtlar](additional-responses.md){.internal-link target=_blank} kullanarak.
