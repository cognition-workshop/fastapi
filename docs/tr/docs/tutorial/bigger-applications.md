# Daha Büyük Uygulamalar - Çoklu Dosyalar

Bir uygulama veya web API oluşturuyorsanız, her şeyi tek bir dosyaya koyabilmeniz nadiren mümkündür.

**FastAPI**, tüm esnekliği korurken uygulamanızı yapılandırmanız için kullanışlı bir araç sağlar.

/// info

Flask'tan geliyorsanız, bu Flask'ın Blueprint'lerinin karşılığı olurdu.

///

## Örnek dosya yapısı

Diyelim ki şöyle bir dosya yapınız var:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

/// tip

Her dizin veya alt dizinde birkaç `__init__.py` dosyası vardır.

Bu, bir dosyadan diğerine kod içe aktarmaya olanak tanır.

Örneğin, `app/main.py`'de şöyle bir satır olabilir:

```
from app.routers import items
```

///

* `app` dizini her şeyi içerir. Ve boş bir `app/__init__.py` dosyasına sahiptir, bu yüzden bir "Python paketi"dir ("Python modülleri"nin bir koleksiyonu): `app`.
* `app/main.py` dosyasını içerir. Bir Python paketinin içinde olduğundan (`__init__.py` dosyası olan bir dizin), o paketin bir "modülü"dür: `app.main`.
* `app/dependencies.py` dosyası da var, `app/main.py` gibi, bir "modül"dür: `app.dependencies`.
* `app/routers/` alt dizini başka bir `__init__.py` dosyasına sahiptir, bu yüzden bir "Python alt paketi"dir: `app.routers`.
* `app/routers/items.py` dosyası bir paketin içindedir, `app/routers/`, bu yüzden bir alt modüldür: `app.routers.items`.
* `app/routers/users.py` ile aynı, başka bir alt modüldür: `app.routers.users`.
* `app/internal/` alt dizini de başka bir `__init__.py` dosyasına sahiptir, bu yüzden başka bir "Python alt paketi"dir: `app.internal`.
* Ve `app/internal/admin.py` dosyası başka bir alt modüldür: `app.internal.admin`.

<img src="/img/tutorial/bigger-applications/package.svg">

Yorumlarla aynı dosya yapısı:

```
.
├── app                  # "app" bir Python paketidir
│   ├── __init__.py      # bu dosya "app"i bir "Python paketi" yapar
│   ├── main.py          # "main" modülü, ör. import app.main
│   ├── dependencies.py  # "dependencies" modülü, ör. import app.dependencies
│   └── routers          # "routers" bir "Python alt paketi"dir
│   │   ├── __init__.py  # "routers"ı bir "Python alt paketi" yapar
│   │   ├── items.py     # "items" alt modülü, ör. import app.routers.items
│   │   └── users.py     # "users" alt modülü, ör. import app.routers.users
│   └── internal         # "internal" bir "Python alt paketi"dir
│       ├── __init__.py  # "internal"ı bir "Python alt paketi" yapar
│       └── admin.py     # "admin" alt modülü, ör. import app.internal.admin
```

## `APIRouter`

Diyelim ki yalnızca kullanıcıları ele almaya adanmış dosya `/app/routers/users.py` konumundaki alt modüldür.

Kullanıcılarınızla ilgili *yol operasyonlarını* kodun geri kalanından ayırarak düzenli tutmak istiyorsunuz.

Ama yine de aynı **FastAPI** uygulamasının/web API'sinin bir parçasıdır (aynı "Python Paketi"nin parçasıdır).

Bu modül için *yol operasyonlarını* `APIRouter` kullanarak oluşturabilirsiniz.

### `APIRouter`'ı içe aktarın

`FastAPI` sınıfıyla yaptığınız gibi içe aktarır ve bir "örnek" oluşturursunuz:

```Python hl_lines="1  3" title="app/routers/users.py"
{!../../docs_src/bigger_applications/app/routers/users.py!}
```

### `APIRouter` ile *yol operasyonları*

Ve sonra *yol operasyonlarınızı* bildirmek için kullanırsınız.

`FastAPI` sınıfını kullandığınız gibi kullanın:

```Python hl_lines="6  11  16" title="app/routers/users.py"
{!../../docs_src/bigger_applications/app/routers/users.py!}
```

`APIRouter`'ı "mini `FastAPI`" sınıfı gibi düşünebilirsiniz.

Aynı seçeneklerin hepsi desteklenir.

Tüm aynı `parameters`, `responses`, `dependencies`, `tags`, vb.

/// tip

Bu örnekte, değişken `router` olarak adlandırılmıştır, ancak istediğiniz gibi adlandırabilirsiniz.

///

Bu `APIRouter`'ı ana `FastAPI` uygulamasına dahil edeceğiz, ama önce bağımlılıkları ve başka bir `APIRouter`'ı kontrol edelim.

## Bağımlılıklar

Uygulamanın çeşitli yerlerinde kullanılan bazı bağımlılıklara ihtiyacımız olacağını görüyoruz.

Bu yüzden onları kendi `dependencies` modülüne (`app/dependencies.py`) koyuyoruz.

Şimdi özel bir `X-Token` başlığını okumak için basit bir bağımlılık kullanacağız:

//// tab | Python 3.9+

```Python hl_lines="3  6-8" title="app/dependencies.py"
{!> ../../docs_src/bigger_applications/app_an_py39/dependencies.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="1  5-7" title="app/dependencies.py"
{!> ../../docs_src/bigger_applications/app_an/dependencies.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

```Python hl_lines="1  4-6" title="app/dependencies.py"
{!> ../../docs_src/bigger_applications/app/dependencies.py!}
```

////

/// tip

Bu örneği basitleştirmek için uydurma bir başlık kullanıyoruz.

Ama gerçek durumlarda, entegre [Güvenlik yardımcı araçlarını](security/index.md){.internal-link target=_blank} kullanarak daha iyi sonuçlar elde edeceksiniz.

///

## `APIRouter` ile başka bir modül

Diyelim ki uygulamanızda "öğeleri" ele almaya adanmış uç noktaları `app/routers/items.py` modülünde bulunuyor.

Şu *yol operasyonlarına* sahipsiniz:

* `/items/`
* `/items/{item_id}`

Hepsi `app/routers/users.py` ile aynı yapıdadır.

Ama daha akıllı olmak ve kodu biraz basitleştirmek istiyoruz.

Bu modüldeki tüm *yol operasyonlarının* aynı şeylere sahip olduğunu biliyoruz:

* Yol `prefix`'i: `/items`.
* `tags`: (sadece bir etiket: `items`).
* Ekstra `responses`.
* `dependencies`: hepsinin oluşturduğumuz `X-Token` bağımlılığına ihtiyacı var.

Bu yüzden, bunları her *yol operasyonuna* eklemek yerine, `APIRouter`'a ekleyebiliriz.

```Python hl_lines="5-10  16  21" title="app/routers/items.py"
{!../../docs_src/bigger_applications/app/routers/items.py!}
```

Her *yol operasyonunun* yolunun `/` ile başlaması gerektiğinden, şöyle:

```Python hl_lines="1"
@router.get("/{item_id}")
async def read_item(item_id: str):
    ...
```

...önek son `/` içermemelidir.

Bu durumda önek `/items`'dir.

Ayrıca bu yönlendiriciye dahil edilen tüm *yol operasyonlarına* uygulanacak `tags` listesi ve ekstra `responses` de ekleyebiliriz.

Ve yönlendiricideki tüm *yol operasyonlarına* eklenecek ve onlara yapılan her istek için yürütülecek/çözülecek bir `dependencies` listesi de ekleyebiliriz.

/// tip

[*Yol operasyonu dekoratörlerindeki bağımlılıklar*](dependencies/dependencies-in-path-operation-decorators.md){.internal-link target=_blank}'daki gibi, *yol operasyonu fonksiyonunuza* hiçbir değer iletilmeyeceğini unutmayın.

///

Sonuç olarak öğe yolları artık:

* `/items/`
* `/items/{item_id}`

...amaçladığımız gibi.

* Tek bir `"items"` dizesini içeren etiket listesiyle işaretlenecekler.
    * Bu "etiketler", otomatik etkileşimli belge sistemleri (OpenAPI kullanan) için özellikle kullanışlıdır.
* Hepsi önceden tanımlanmış `responses`'ı içerecek.
* Tüm bu *yol operasyonlarının* öncesinde `dependencies` listesi değerlendirilecek/yürütülecek.
    * Belirli bir *yol operasyonunda* da bağımlılıklar bildirirseniz, **onlar da yürütülecektir**.
    * Yönlendirici bağımlılıkları önce yürütülür, ardından [dekoratördeki `dependencies`](dependencies/dependencies-in-path-operation-decorators.md){.internal-link target=_blank} ve sonra normal parametre bağımlılıkları.
    * [`Security` bağımlılıklarını `scopes` ile](../advanced/security/oauth2-scopes.md){.internal-link target=_blank} de ekleyebilirsiniz.

/// tip

`APIRouter`'da `dependencies` bulundurmak, örneğin bir grup *yol operasyonu* için kimlik doğrulama gerektirmek için kullanılabilir. Her birine ayrı ayrı bağımlılık eklenmese bile.

///

/// check

`prefix`, `tags`, `responses` ve `dependencies` parametreleri (birçok diğer durumda olduğu gibi) kod tekrarından kaçınmanıza yardımcı olmak için sadece **FastAPI**'nin bir özelliğidir.

///

### Bağımlılıkları içe aktarın

Bu kod `app.routers.items` modülünde, `app/routers/items.py` dosyasında yaşar.

Ve bağımlılık fonksiyonunu `app.dependencies` modülünden, `app/dependencies.py` dosyasından almamız gerekiyor.

Bu yüzden bağımlılıklar için `..` ile göreceli içe aktarma kullanıyoruz:

```Python hl_lines="3" title="app/routers/items.py"
{!../../docs_src/bigger_applications/app/routers/items.py!}
```

#### Göreceli içe aktarmalar nasıl çalışır

/// tip

İçe aktarmaların nasıl çalıştığını tam olarak biliyorsanız, aşağıdaki sonraki bölüme devam edin.

///

Tek bir nokta `.`, şöyle:

```Python
from .dependencies import get_token_header
```

şu anlama gelir:

* Bu modülün (dosya `app/routers/items.py`) bulunduğu aynı paketten (dizin `app/routers/`) başlayarak...
* `dependencies` modülünü bulun (`app/routers/dependencies.py` konumundaki hayali bir dosya)...
* ve ondan `get_token_header` fonksiyonunu içe aktarın.

Ama bu dosya mevcut değil, bağımlılıklarımız `app/dependencies.py` konumundaki bir dosyada.

Uygulama/dosya yapımızın nasıl göründüğünü hatırlayın:

<img src="/img/tutorial/bigger-applications/package.svg">

---

İki nokta `..`, şöyle:

```Python
from ..dependencies import get_token_header
```

şu anlama gelir:

* Bu modülün (dosya `app/routers/items.py`) bulunduğu aynı paketten (dizin `app/routers/`) başlayarak...
* üst pakete (dizin `app/`) gidin...
* ve orada, `dependencies` modülünü (`app/dependencies.py` konumundaki dosya) bulun...
* ve ondan `get_token_header` fonksiyonunu içe aktarın.

Bu doğru çalışıyor! 🎉

---

Aynı şekilde, üç nokta `...` kullanmış olsaydık, şöyle:

```Python
from ...dependencies import get_token_header
```

bu şu anlama gelirdi:

* Bu modülün (dosya `app/routers/items.py`) bulunduğu aynı paketten (dizin `app/routers/`) başlayarak...
* üst pakete (dizin `app/`) gidin...
* sonra o paketin üstüne gidin (üst paket yok, `app` en üst seviye 😱)...
* ve orada, `dependencies` modülünü (`app/dependencies.py` konumundaki dosya) bulun...
* ve ondan `get_token_header` fonksiyonunu içe aktarın.

Bu, `app/`'in üstünde, kendi `__init__.py` dosyası olan bir pakete atıfta bulunurdu. Ama bizim bunu yok. Bu yüzden, örneğimizde hata fırlatırdı. 🚨

Ama şimdi nasıl çalıştığını biliyorsunuz, böylece ne kadar karmaşık olursa olsun kendi uygulamalarınızda göreceli içe aktarmaları kullanabilirsiniz. 🤓

### Bazı özel `tags`, `responses` ve `dependencies` ekleyin

Her *yol operasyonuna* `/items` önekini veya `tags=["items"]`'ı eklemiyoruz çünkü bunları `APIRouter`'a ekledik.

Ama yine de belirli bir *yol operasyonuna* uygulanacak _daha fazla_ `tags` ve ayrıca o *yol operasyonuna* özgü bazı ekstra `responses` ekleyebiliriz:

```Python hl_lines="30-31" title="app/routers/items.py"
{!../../docs_src/bigger_applications/app/routers/items.py!}
```

/// tip

Bu son yol operasyonu, etiketlerin birleşimini alacaktır: `["items", "custom"]`.

Ve belgede her ikisine de sahip olacaktır, biri `404` ve biri `403` için yanıtlar.

///

## Ana `FastAPI`

Şimdi, `app/main.py`'deki modüle bakalım.

Burada `FastAPI` sınıfını içe aktarır ve kullanırsınız.

Bu, uygulamanızda her şeyi birbirine bağlayan ana dosya olacaktır.

Ve mantığınızın çoğu artık kendi özel modülünde yaşayacağından, ana dosya oldukça basit olacaktır.

### `FastAPI`'yi içe aktarın

Normalde olduğu gibi bir `FastAPI` sınıfını içe aktarır ve oluşturursunuz.

Ve her `APIRouter` için bağımlılıklarla birleştirilecek [global bağımlılıklar](dependencies/global-dependencies.md){.internal-link target=_blank} bile bildirebiliriz:

```Python hl_lines="1  3  7" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

### `APIRouter`'ı içe aktarın

Şimdi `APIRouter`'lara sahip diğer alt modülleri içe aktarıyoruz:

```Python hl_lines="4-5" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

`app/routers/users.py` ve `app/routers/items.py` dosyaları aynı Python paketi `app`'in parçası olan alt modüller olduğundan, bunları "göreceli içe aktarmalar" kullanarak tek bir nokta `.` ile içe aktarabiliriz.

### İçe aktarma nasıl çalışır

Şu bölüm:

```Python
from .routers import items, users
```

şu anlama gelir:

* Bu modülün (dosya `app/main.py`) bulunduğu aynı paketten (dizin `app/`) başlayarak...
* `routers` alt paketini (dizin `app/routers/`) bulun...
* ve ondan `items` alt modülünü (`app/routers/items.py` dosyası) ve `users`'ı (`app/routers/users.py` dosyası) içe aktarın...

`items` modülü bir `router` değişkenine (`items.router`) sahip olacaktır. Bu, `app/routers/items.py` dosyasında oluşturduğumuz aynı değişkendir, bir `APIRouter` nesnesidir.

Ve sonra `users` modülü için aynı şeyi yapıyoruz.

Bunları şöyle de içe aktarabilirdik:

```Python
from app.routers import items, users
```

/// info

İlk sürüm bir "göreceli içe aktarma"dır:

```Python
from .routers import items, users
```

İkinci sürüm bir "mutlak içe aktarma"dır:

```Python
from app.routers import items, users
```

Python Paketleri ve Modüller hakkında daha fazla bilgi edinmek için <a href="https://docs.python.org/3/tutorial/modules.html" class="external-link" target="_blank">resmi Python belgesini Modüller hakkında</a> okuyun.

///

### Ad çakışmalarından kaçının

`items` alt modülünü doğrudan içe aktarıyoruz, sadece `router` değişkenini içe aktarmak yerine.

Bunun nedeni, `users` alt modülünde de `router` adında başka bir değişkenimiz olmasıdır.

Birini diğerinden sonra içe aktarmış olsaydık, şöyle:

```Python
from .routers.items import router
from .routers.users import router
```

`users`'dan gelen `router`, `items`'dan geleni geçersiz kılardı ve ikisini aynı anda kullanamayacaktık.

Bu yüzden, aynı dosyada her ikisini de kullanabilmek için alt modülleri doğrudan içe aktarıyoruz:

```Python hl_lines="5" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

### `users` ve `items` için `APIRouter`'ları dahil edin

Şimdi, `users` ve `items` alt modüllerinden `router`'ları dahil edelim:

```Python hl_lines="10-11" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

/// info

`users.router`, `app/routers/users.py` dosyasının içindeki `APIRouter`'ı içerir.

Ve `items.router`, `app/routers/items.py` dosyasının içindeki `APIRouter`'ı içerir.

///

`app.include_router()` ile her `APIRouter`'ı ana `FastAPI` uygulamasına ekleyebiliriz.

O yönlendiricideki tüm rotaları kendisinin bir parçası olarak dahil edecektir.

/// note | Teknik Detaylar

Aslında dahili olarak `APIRouter`'da bildirilen her *yol operasyonu* için bir *yol operasyonu* oluşturacaktır.

Bu yüzden, perde arkasında, aslında her şey aynı tek uygulamıymış gibi çalışacaktır.

///

/// check

Yönlendiricileri dahil ederken performans konusunda endişelenmenize gerek yok.

Bu mikrosaniyeler sürecek ve yalnızca başlangıçta gerçekleşecektir.

Bu yüzden performansı etkilemeyecektir. ⚡

///

### Özel bir `prefix`, `tags`, `responses` ve `dependencies` ile bir `APIRouter` dahil edin

Şimdi, kuruluşunuzun size `app/internal/admin.py` dosyasını verdiğini hayal edin.

Kuruluşunuzun birçok proje arasında paylaştığı bazı yönetici *yol operasyonlarıyla* bir `APIRouter` içerir.

Bu örnek için çok basit olacaktır. Ama diyelim ki kuruluştaki diğer projelerle paylaşıldığı için, onu değiştiremeyiz ve doğrudan `APIRouter`'a bir `prefix`, `dependencies`, `tags`, vb. ekleyemeyiz:

```Python hl_lines="3" title="app/internal/admin.py"
{!../../docs_src/bigger_applications/app/internal/admin.py!}
```

Ama yine de `APIRouter`'ı dahil ederken, tüm *yol operasyonlarının* `/admin` ile başlaması için özel bir `prefix` ayarlamak, bu proje için zaten sahip olduğumuz `dependencies` ile güvence altına almak ve `tags` ve `responses` eklemek istiyoruz.

Bu parametreleri `app.include_router()`'a ileterek orijinal `APIRouter`'ı değiştirmek zorunda kalmadan hepsini bildirebiliriz:

```Python hl_lines="14-17" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

Bu şekilde, orijinal `APIRouter` değiştirilmeden kalacaktır, böylece aynı `app/internal/admin.py` dosyasını kuruluştaki diğer projelerle paylaşmaya devam edebiliriz.

Sonuç olarak, uygulamamızda `admin` modülünden her *yol operasyonu* şunlara sahip olacaktır:

* `/admin` öneki.
* `admin` etiketi.
* `get_token_header` bağımlılığı.
* `418` yanıtı. 🍵

Ama bu, yalnızca uygulamamızdaki o `APIRouter`'ı etkileyecektir, onu kullanan başka hiçbir kodda değil.

Böylece, örneğin diğer projeler aynı `APIRouter`'ı farklı bir kimlik doğrulama yöntemiyle kullanabilir.

### Bir *yol operasyonu* dahil edin

*Yol operasyonlarını* doğrudan `FastAPI` uygulamasına da ekleyebiliriz.

Burada bunu yapıyoruz... sadece yapabildiğimizi göstermek için 🤷:

```Python hl_lines="21-23" title="app/main.py"
{!../../docs_src/bigger_applications/app/main.py!}
```

ve `app.include_router()` ile eklenen tüm diğer *yol operasyonlarıyla* birlikte doğru şekilde çalışacaktır.

/// info | Çok Teknik Detaylar

**Not**: bu muhtemelen **atlayabileceğiniz** çok teknik bir ayrıntıdır.

---

`APIRouter`'lar "monte" edilmez, uygulamanın geri kalanından izole değildirler.

Bunun nedeni, *yol operasyonlarını* OpenAPI şemasına ve kullanıcı arayüzlerine dahil etmek istememizdir.

Onları izole edemeyip geri kalanından bağımsız olarak "monte edemeyeceğimiz" için, *yol operasyonları* doğrudan dahil edilmek yerine "klonlanır" (yeniden oluşturulur).

///

## Otomatik API belgelerini kontrol edin

Şimdi, uygulamanızı çalıştırın:

<div class="termy">

```console
$ fastapi dev app/main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Ve belgeleri <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> adresinde açın.

Doğru yolları (ve önekleri) ve doğru etiketleri kullanan tüm alt modüllerden yolları içeren otomatik API belgelerini göreceksiniz:

<img src="/img/tutorial/bigger-applications/image01.png">

## Aynı yönlendiriciyi farklı `prefix` ile birden çok kez dahil edin

Ayrıca farklı önekler kullanarak aynı yönlendiriciyle `.include_router()` kullanabilirsiniz.

Bu, örneğin aynı API'yi farklı önekler altında göstermek için yararlı olabilir, ör. `/api/v1` ve `/api/latest`.

Bu, gerçekten ihtiyacınız olmayabilecek gelişmiş bir kullanımdır, ama ihtiyacınız olursa diye oradadır.

## Bir `APIRouter`'ı başka birinin içine dahil edin

Bir `APIRouter`'ı bir `FastAPI` uygulamasına dahil edebildiğiniz gibi, bir `APIRouter`'ı başka bir `APIRouter`'a da dahil edebilirsiniz:

```Python
router.include_router(other_router)
```

Bunu `router`'ı `FastAPI` uygulamasına dahil etmeden önce yaptığınızdan emin olun, böylece `other_router`'dan gelen *yol operasyonları* da dahil edilir.
