# Arka Plan Görevleri

Bir yanıt döndürdükten *sonra* çalıştırılacak arka plan görevleri tanımlayabilirsiniz.

Bu, bir istekten sonra gerçekleşmesi gereken ancak istemcinin yanıtı almadan önce işlemin tamamlanmasını beklemesine gerek olmayan işlemler için kullanışlıdır.

Buna örnek olarak:

* Bir eylem gerçekleştirdikten sonra gönderilen e-posta bildirimleri:
    * Bir e-posta sunucusuna bağlanmak ve e-posta göndermek "yavaş" olma eğiliminde olduğundan (birkaç saniye), yanıtı hemen döndürüp e-posta bildirimini arka planda gönderebilirsiniz.
* Veri işleme:
    * Örneğin, yavaş bir süreçten geçmesi gereken bir dosya aldığınızı varsayalım, "Kabul Edildi" (HTTP 202) yanıtı döndürüp dosyayı arka planda işleyebilirsiniz.

## `BackgroundTasks` kullanımı

Öncelikle, `BackgroundTasks`'ı içe aktarın ve *yol operasyonu fonksiyonunuzda* `BackgroundTasks` tip bildirimi ile bir parametre tanımlayın:

{* ../../docs_src/background_tasks/tutorial001.py hl[1,13] *}

**FastAPI** sizin için `BackgroundTasks` tipinde nesneyi oluşturacak ve bu parametre olarak iletecektir.

## Bir görev fonksiyonu oluşturun

Arka plan görevi olarak çalıştırılacak bir fonksiyon oluşturun.

Bu, parametre alabilen standart bir fonksiyondur.

Bir `async def` veya normal `def` fonksiyonu olabilir, **FastAPI** bunu doğru şekilde nasıl ele alacağını bilecektir.

Bu durumda, görev fonksiyonu bir dosyaya yazacaktır (e-posta göndermeyi simüle ederek).

Ve yazma işlemi `async` ve `await` kullanmadığından, fonksiyonu normal `def` ile tanımlıyoruz:

{* ../../docs_src/background_tasks/tutorial001.py hl[6:9] *}

## Arka plan görevini ekleyin

*Yol operasyonu fonksiyonunuz* içinde, görev fonksiyonunuzu `.add_task()` metoduyla *arka plan görevleri* nesnesine iletin:

{* ../../docs_src/background_tasks/tutorial001.py hl[14] *}

`.add_task()` argüman olarak şunları alır:

* Arka planda çalıştırılacak bir görev fonksiyonu (`write_notification`).
* Görev fonksiyonuna sırayla iletilmesi gereken herhangi bir argüman dizisi (`email`).
* Görev fonksiyonuna iletilmesi gereken herhangi bir anahtar kelime argümanı (`message="some notification"`).

## Bağımlılık Enjeksiyonu

`BackgroundTasks` kullanmak bağımlılık enjeksiyon sistemiyle de çalışır, birden fazla seviyede `BackgroundTasks` tipinde bir parametre bildirebilirsiniz: bir *yol operasyonu fonksiyonunda*, bir bağımlılıkta, bir alt bağımlılıkta vb.

**FastAPI** her durumda ne yapacağını ve aynı nesneyi nasıl yeniden kullanacağını bilir, böylece tüm arka plan görevleri birleştirilir ve ardından arka planda çalıştırılır:


{* ../../docs_src/background_tasks/tutorial002_an_py310.py hl[13,15,22,25] *}


Bu örnekte, mesajlar yanıt gönderildikten *sonra* `log.txt` dosyasına yazılacaktır.

İstekte bir sorgu varsa, bir arka plan görevinde günlüğe yazılacaktır.

Ve ardından *yol operasyonu fonksiyonunda* oluşturulan başka bir arka plan görevi, `email` yol parametresini kullanarak bir mesaj yazacaktır.

## Teknik Detaylar

`BackgroundTasks` sınıfı doğrudan <a href="https://www.starlette.io/background/" class="external-link" target="_blank">`starlette.background`</a>'dan gelir.

Doğrudan FastAPI'ye içe aktarılır/dahil edilir, böylece onu `fastapi`'den içe aktarabilir ve yanlışlıkla `starlette.background`'dan alternatif `BackgroundTask`'ı (sonunda `s` olmadan) içe aktarmaktan kaçınabilirsiniz.

Yalnızca `BackgroundTasks` kullanarak (ve `BackgroundTask` değil), bunu bir *yol operasyonu fonksiyonu* parametresi olarak kullanmak ve **FastAPI**'nin gerisini halletmesini sağlamak mümkündür, tıpkı `Request` nesnesini doğrudan kullanırken olduğu gibi.

FastAPI'de `BackgroundTask`'ı tek başına kullanmak hâlâ mümkündür, ancak nesneyi kodunuzda oluşturmanız ve bunu içeren bir Starlette `Response` döndürmeniz gerekir.

Daha fazla detayı <a href="https://www.starlette.io/background/" class="external-link" target="_blank">Starlette'in Arka Plan Görevleri için resmi belgelerinde</a> görebilirsiniz.

## Uyarı

Ağır arka plan hesaplamaları yapmanız gerekiyorsa ve bunun aynı süreç tarafından çalıştırılmasına gerek yoksa (örneğin, bellek, değişkenler vb. paylaşmanıza gerek yoksa), <a href="https://docs.celeryq.dev" class="external-link" target="_blank">Celery</a> gibi daha büyük araçları kullanmaktan faydalanabilirsiniz.

Bunlar RabbitMQ veya Redis gibi bir mesaj/iş kuyruğu yöneticisi gerektiren daha karmaşık yapılandırmalara ihtiyaç duyma eğilimindedir, ancak arka plan görevlerini birden fazla süreçte ve özellikle birden fazla sunucuda çalıştırmanıza olanak tanır.

Ancak aynı **FastAPI** uygulamasından değişkenlere ve nesnelere erişmeniz gerekiyorsa veya küçük arka plan görevleri (bir e-posta bildirimi göndermek gibi) gerçekleştirmeniz gerekiyorsa, basitçe `BackgroundTasks` kullanabilirsiniz.

## Özet

Arka plan görevleri eklemek için *yol operasyonu fonksiyonlarında* ve bağımlılıklarda `BackgroundTasks`'ı parametrelerle içe aktarın ve kullanın.
