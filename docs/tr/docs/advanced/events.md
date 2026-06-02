# Yaşam Döngüsü Olayları

Uygulama **başlamadan önce** çalıştırılması gereken mantığı (kodu) tanımlayabilirsiniz. Bu, bu kodun uygulama **istekleri almaya başlamadan önce**, **bir kez** çalıştırılacağı anlamına gelir.

Aynı şekilde, uygulama **kapanırken** çalıştırılması gereken mantığı (kodu) tanımlayabilirsiniz. Bu durumda, bu kod muhtemelen **birçok isteği** ele aldıktan **sonra**, **bir kez** çalıştırılacaktır.

Bu kod, uygulama istekleri almaya **başlamadan önce** ve istekleri ele almayı **bitirdikten hemen sonra** çalıştırıldığından, tüm uygulama **yaşam döngüsünü** kapsar ("yaşam döngüsü" kelimesi birazdan önemli olacak 😉).

Bu, tüm uygulama için kullanmanız gereken ve istekler arasında **paylaşılan** ve/veya sonrasında **temizlemeniz** gereken **kaynakları** ayarlamak için çok yararlı olabilir. Örneğin, bir veritabanı bağlantı havuzu veya paylaşılan bir makine öğrenimi modelinin yüklenmesi.

## Kullanım Senaryosu

Bir örnek **kullanım senaryosu** ile başlayalım ve ardından bunu nasıl çözeceğimizi görelim.

İstekleri ele almak için kullanmak istediğiniz bazı **makine öğrenimi modelleriniz** olduğunu hayal edelim. 🤖

Aynı modeller istekler arasında paylaşılır, yani istek başına bir model veya kullanıcı başına bir model ya da benzeri bir şey değildir.

Modeli yüklemenin **biraz zaman alabileceğini** hayal edelim, çünkü **diskten çok fazla veri** okuması gerekiyor. Bu yüzden her istek için bunu yapmak istemezsiniz.

Modülün/dosyanın en üst seviyesinde yükleyebilirsiniz, ama bu aynı zamanda basit bir otomatik test çalıştırıyor olsanız bile **modeli yükleyeceği** anlamına gelir, o zaman bu test **yavaş** olur çünkü kodun bağımsız bir bölümünü çalıştırabilmeden önce modelin yüklenmesini beklemesi gerekir.

İşte çözeceğimiz şey budur, modeli istekler ele alınmadan önce yükleyelim, ama yalnızca uygulama istekleri almaya başlamadan hemen önce, kod yüklenirken değil.

## Yaşam Döngüsü

Bu *başlatma* ve *kapatma* mantığını `FastAPI` uygulamasının `lifespan` parametresini ve bir "bağlam yöneticisi" (bunun ne olduğunu birazdan göstereceğim) kullanarak tanımlayabilirsiniz.

Bir örnekle başlayalım ve ardından ayrıntılı olarak görelim.

Şöyle bir `yield` ile asenkron `lifespan()` fonksiyonu oluşturuyoruz:

{* ../../docs_src/events/tutorial003.py hl[16,19] *}

Burada, model fonksiyonunu (sahte) `yield`'den önce makine öğrenimi modelleri sözlüğüne koyarak pahalı *başlatma* operasyonunu simüle ediyoruz. Bu kod, uygulama **istekleri almaya başlamadan önce**, *başlatma* sırasında çalıştırılacaktır.

Ve ardından, `yield`'den hemen sonra modeli kaldırıyoruz. Bu kod, uygulama **istekleri ele almayı bitirdikten sonra**, *kapatma*'dan hemen önce çalıştırılacaktır. Bu, örneğin bellek veya GPU gibi kaynakları serbest bırakabilir.

/// tip

`shutdown`, uygulamayı **durdurduğunuzda** gerçekleşir.

Belki yeni bir sürüm başlatmanız gerekiyor veya sadece çalıştırmaktan yoruldunuz. 🤷

///

### Yaşam döngüsü fonksiyonu

Dikkat edilecek ilk şey, `yield` ile bir asenkron fonksiyon tanımlıyoruz. Bu, `yield` ile Bağımlılıklara çok benzer.

{* ../../docs_src/events/tutorial003.py hl[14:19] *}

Fonksiyonun ilk kısmı, `yield`'den önce, uygulama başlamadan **önce** çalıştırılacaktır.

Ve `yield`'den sonraki kısım, uygulama bitirdikten **sonra** çalıştırılacaktır.

### Asenkron Bağlam Yöneticisi

Kontrol ederseniz, fonksiyon `@asynccontextmanager` ile dekore edilmiştir.

Bu, fonksiyonu "**asenkron bağlam yöneticisi**" adı verilen bir şeye dönüştürür.

{* ../../docs_src/events/tutorial003.py hl[1,13] *}

Python'da **bağlam yöneticisi**, `with` ifadesinde kullanabileceğiniz bir şeydir, örneğin `open()` bir bağlam yöneticisi olarak kullanılabilir:

```Python
with open("file.txt") as file:
    file.read()
```

Python'un son sürümlerinde bir de **asenkron bağlam yöneticisi** var. Bunu `async with` ile kullanırsınız:

```Python
async with lifespan(app):
    await do_stuff()
```

Yukarıdaki gibi bir bağlam yöneticisi veya asenkron bağlam yöneticisi oluşturduğunuzda, yaptığı şey `with` bloğuna girmeden önce `yield`'den önceki kodu çalıştırmak ve `with` bloğundan çıktıktan sonra `yield`'den sonraki kodu çalıştırmaktır.

Yukarıdaki kod örneğimizde, bunu doğrudan kullanmıyoruz, onu FastAPI'ye kullanması için veriyoruz.

`FastAPI` uygulamasının `lifespan` parametresi bir **asenkron bağlam yöneticisi** alır, bu yüzden yeni `lifespan` asenkron bağlam yöneticimizi ona geçirebiliriz.

{* ../../docs_src/events/tutorial003.py hl[22] *}

## Alternatif Olaylar (kullanımdan kaldırıldı)

/// warning

*Başlatma* ve *kapatma*'yı ele almanın önerilen yolu, yukarıda açıklandığı gibi `FastAPI` uygulamasının `lifespan` parametresini kullanmaktır. Bir `lifespan` parametresi sağlarsanız, `startup` ve `shutdown` olay işleyicileri artık çağrılmayacaktır. Ya tamamen `lifespan` ya da tamamen olaylar, ikisi birden değil.

Muhtemelen bu bölümü atlayabilirsiniz.

///

*Başlatma* sırasında ve *kapatma* sırasında çalıştırılması gereken mantığı tanımlamanın alternatif bir yolu var.

Uygulama başlamadan önce çalıştırılması gereken veya uygulama kapatılırken çalıştırılması gereken olay işleyicileri (fonksiyonlar) tanımlayabilirsiniz.

Bu fonksiyonlar `async def` veya normal `def` ile bildirilebilir.

### `startup` olayı

Uygulama başlamadan önce çalıştırılması gereken bir fonksiyon eklemek için, onu `"startup"` olayıyla bildirin:

{* ../../docs_src/events/tutorial001.py hl[8] *}

Bu durumda, `startup` olay işleyici fonksiyonu öğeler "veritabanını" (sadece bir `dict`) bazı değerlerle başlatacaktır.

Birden fazla olay işleyici fonksiyonu ekleyebilirsiniz.

Ve uygulamanız, tüm `startup` olay işleyicileri tamamlanana kadar istek almaya başlamayacaktır.

### `shutdown` olayı

Uygulama kapatılırken çalıştırılması gereken bir fonksiyon eklemek için, onu `"shutdown"` olayıyla bildirin:

{* ../../docs_src/events/tutorial002.py hl[6] *}

Burada, `shutdown` olay işleyici fonksiyonu `log.txt` dosyasına `"Application shutdown"` metin satırını yazacaktır.

/// info

`open()` fonksiyonunda, `mode="a"` "ekleme" anlamına gelir, bu yüzden satır, önceki içeriklerin üzerine yazmadan, dosyadaki mevcut içeriğin arkasına eklenecektir.

///

/// tip

Bu durumda, bir dosyayla etkileşime giren standart Python `open()` fonksiyonunu kullandığımıza dikkat edin.

Yani, şeylerin diske yazılmasını "beklemeyi" gerektiren I/O (girdi/çıktı) içerir.

Ama `open()` `async` ve `await` kullanmaz.

Bu yüzden, olay işleyici fonksiyonunu `async def` yerine standart `def` ile bildiriyoruz.

///

### `startup` ve `shutdown` birlikte

*Başlatma* ve *kapatma* mantığınızın bağlantılı olma ihtimali yüksektir, bir şeyi başlatmak ve sonra bitirmek, bir kaynak edinmek ve sonra serbest bırakmak isteyebilirsiniz, vb.

Bunu, mantık veya değişkenleri paylaşmayan ayrı fonksiyonlarda yapmak daha zordur çünkü değerleri global değişkenlerde veya benzer hilelerle saklamanız gerekir.

Bu nedenle, şimdi yukarıda açıklandığı gibi `lifespan`'ı kullanmanız önerilir.

## Teknik Detaylar

Meraklı bilgi meraklıları için sadece teknik bir ayrıntı. 🤓

Altta, ASGI teknik spesifikasyonunda, bu <a href="https://asgi.readthedocs.io/en/latest/specs/lifespan.html" class="external-link" target="_blank">Yaşam Döngüsü Protokolü</a>'nün bir parçasıdır ve `startup` ve `shutdown` adı verilen olayları tanımlar.

/// info

Starlette `lifespan` işleyicileri hakkında daha fazla bilgiyi <a href="https://www.starlette.io/lifespan/" class="external-link" target="_blank">Starlette'in Yaşam Döngüsü belgelerinde</a> okuyabilirsiniz.

Kodunuzun diğer alanlarında kullanılabilecek yaşam döngüsü durumunun nasıl ele alınacağı dahil.

///

## Alt Uygulamalar

🚨 Bu yaşam döngüsü olaylarının (başlatma ve kapatma) yalnızca ana uygulama için çalıştırılacağını, [Alt Uygulamalar - Bağlama](sub-applications.md){.internal-link target=_blank} için çalıştırılmayacağını unutmayın.
