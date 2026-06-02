# Global Bağımlılıklar

Bazı uygulama türleri için tüm uygulamaya bağımlılıklar eklemek isteyebilirsiniz.

[*Yol operasyonu dekoratörlerine* `dependencies` ekleme](dependencies-in-path-operation-decorators.md){.internal-link target=_blank} yöntemine benzer şekilde, bunları `FastAPI` uygulamasına ekleyebilirsiniz.

Bu durumda, uygulamadaki tüm *yol operasyonlarına* uygulanacaktır:

{* ../../docs_src/dependencies/tutorial012_an_py39.py hl[16] *}


Ve [*yol operasyonu dekoratörlerine* `dependencies` ekleme](dependencies-in-path-operation-decorators.md){.internal-link target=_blank} bölümündeki tüm fikirler hala geçerlidir, ancak bu durumda uygulamadaki tüm *yol operasyonları* için.

## *Yol operasyonu* grupları için bağımlılıklar

Daha sonra, daha büyük uygulamaların nasıl yapılandırılacağını ([Daha Büyük Uygulamalar - Birden Fazla Dosya](../../tutorial/bigger-applications.md){.internal-link target=_blank}) okurken, muhtemelen birden fazla dosyayla, bir grup *yol operasyonu* için tek bir `dependencies` parametresi bildirmeyi öğreneceksiniz.
