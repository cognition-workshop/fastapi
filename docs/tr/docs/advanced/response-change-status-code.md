# Yanıt - Durum Kodunu Değiştirme

Muhtemelen daha önce varsayılan bir [Yanıt Durum Kodu](../tutorial/response-status-code.md){.internal-link target=_blank} ayarlayabileceğinizi okudunuz.

Ancak bazı durumlarda varsayılandan farklı bir durum kodu döndürmeniz gerekir.

## Kullanım senaryosu

Örneğin, varsayılan olarak "OK" `200` HTTP durum kodu döndürmek istediğinizi hayal edin.

Ancak veri mevcut değilse, onu oluşturmak ve "CREATED" `201` HTTP durum kodu döndürmek istiyorsunuz.

Ama yine de döndürdüğünüz verileri bir `response_model` ile filtreleyip dönüştürebilmek istiyorsunuz.

Bu durumlar için bir `Response` parametresi kullanabilirsiniz.

## Bir `Response` parametresi kullanın

*Yol operasyonu fonksiyonunuzda* `Response` tipinde bir parametre bildirebilirsiniz (çerezler ve başlıklar için yapabildiğiniz gibi).

Ve ardından o *geçici* yanıt nesnesinde `status_code`'u ayarlayabilirsiniz.

{* ../../docs_src/response_change_status_code/tutorial001.py hl[1,9,12] *}

Ve ardından normalde yaptığınız gibi ihtiyacınız olan herhangi bir nesneyi döndürebilirsiniz (bir `dict`, bir veritabanı modeli, vb).

Ve bir `response_model` bildirdiyseniz, döndürdüğünüz nesneyi filtrelemek ve dönüştürmek için yine de kullanılacaktır.

**FastAPI**, durum kodunu (ayrıca çerezleri ve başlıkları) çıkarmak için o *geçici* yanıtı kullanacak ve herhangi bir `response_model` tarafından filtrelenmiş döndürdüğünüz değeri içeren son yanıta koyacaktır.

`Response` parametresini bağımlılıklarda da bildirebilir ve durum kodunu onlarda ayarlayabilirsiniz. Ancak en son ayarlananın kazanacağını unutmayın.
