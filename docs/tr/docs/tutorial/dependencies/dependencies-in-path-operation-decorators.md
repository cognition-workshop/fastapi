# Yol operasyonu dekoratörlerinde bağımlılıklar

Bazı durumlarda, *yol operasyonu fonksiyonunuz* içinde bir bağımlılığın dönüş değerine gerçekten ihtiyacınız yoktur.

Veya bağımlılık bir değer döndürmez.

Ama yine de çalıştırılması/çözülmesi gerekir.

Bu durumlar için, bir *yol operasyonu fonksiyon* parametresini `Depends` ile bildirmek yerine, *yol operasyonu dekoratörüne* bir `dependencies` `list`'i ekleyebilirsiniz.

## *Yol operasyonu dekoratörüne* `dependencies` ekleme

*Yol operasyonu dekoratörü* isteğe bağlı bir `dependencies` argümanı alır.

Bu, bir `Depends()` `list`'i olmalıdır:

{* ../../docs_src/dependencies/tutorial006_an_py39.py hl[19] *}

Bu bağımlılıklar, normal bağımlılıklarla aynı şekilde çalıştırılacak/çözülecektir. Ancak değerleri (döndürürlerse) *yol operasyonu fonksiyonunuza* iletilmeyecektir.

/// tip

Bazı editörler kullanılmayan fonksiyon parametrelerini kontrol eder ve bunları hata olarak gösterir.

Bu `dependencies`'ı *yol operasyonu dekoratöründe* kullanarak, editör/araç hatalarından kaçınırken bunların çalıştırılmasını sağlayabilirsiniz.

Ayrıca, kodunuzda kullanılmayan bir parametre gören ve bunun gereksiz olduğunu düşünebilecek yeni geliştiriciler için karışıklığı önlemeye de yardımcı olabilir.

///

/// info

Bu örnekte, uydurulmuş özel başlıklar `X-Key` ve `X-Token` kullanıyoruz.

Ancak gerçek durumlarda, güvenlik uygularken, entegre [Güvenlik yardımcı araçlarını (bir sonraki bölüm)](../security/index.md){.internal-link target=_blank} kullanmaktan daha fazla fayda elde edersiniz.

///

## Bağımlılık hataları ve dönüş değerleri

Normalde kullandığınız aynı bağımlılık *fonksiyonlarını* kullanabilirsiniz.

### Bağımlılık gereksinimleri

İstek gereksinimleri (başlıklar gibi) veya diğer alt bağımlılıkları bildirebilirler:

{* ../../docs_src/dependencies/tutorial006_an_py39.py hl[8,13] *}

### İstisna fırlatma

Bu bağımlılıklar, normal bağımlılıklarla aynı şekilde istisna `raise` edebilir:

{* ../../docs_src/dependencies/tutorial006_an_py39.py hl[10,15] *}

### Dönüş değerleri

Ve değer döndürebilir veya döndürmeyebilirler, değerler kullanılmayacaktır.

Bu yüzden, başka bir yerde zaten kullandığınız normal bir bağımlılığı (değer döndüren) yeniden kullanabilirsiniz ve değer kullanılmayacak olsa bile bağımlılık çalıştırılacaktır:

{* ../../docs_src/dependencies/tutorial006_an_py39.py hl[11,16] *}

## Bir grup *yol operasyonu* için bağımlılıklar

Daha sonra, daha büyük uygulamaların nasıl yapılandırılacağını ([Daha Büyük Uygulamalar - Birden Fazla Dosya](../../tutorial/bigger-applications.md){.internal-link target=_blank}) okurken, muhtemelen birden fazla dosyayla, bir grup *yol operasyonu* için tek bir `dependencies` parametresi bildirmeyi öğreneceksiniz.

## Global Bağımlılıklar

Ardından, her *yol operasyonuna* uygulanacak şekilde tüm `FastAPI` uygulamasına bağımlılıkların nasıl ekleneceğini göreceğiz.
