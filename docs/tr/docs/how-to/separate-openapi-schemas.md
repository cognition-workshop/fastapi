# Giriş ve Çıkış İçin Ayrı OpenAPI Şemaları veya Değil

**Pydantic v2** kullanırken, oluşturulan OpenAPI öncekine göre biraz daha kesin ve **doğrudur**. 😎

Hatta bazı durumlarda, aynı Pydantic modeli için OpenAPI'de **iki JSON Şeması** olacaktır, giriş ve çıkış için, **varsayılan değerlere** sahip olup olmadıklarına bağlı olarak.

Bunun nasıl çalıştığını ve gerekirse nasıl değiştireceğinizi görelim.

## Giriş ve Çıkış İçin Pydantic Modelleri

Şunun gibi varsayılan değerlere sahip bir Pydantic modeliniz olduğunu varsayalım:

{* ../../docs_src/separate_openapi_schemas/tutorial001_py310.py ln[1:7] hl[7] *}

### Giriş İçin Model

Bu modeli buradaki gibi bir giriş olarak kullanırsanız:

{* ../../docs_src/separate_openapi_schemas/tutorial001_py310.py ln[1:15] hl[14] *}

...o zaman `description` alanı **zorunlu olmayacaktır**. Çünkü `None` varsayılan değerine sahiptir.

### Belgelerde Giriş Modeli

Bunu belgelerde doğrulayabilirsiniz, `description` alanında **kırmızı yıldız** yoktur, zorunlu olarak işaretlenmemiştir:

<div class="screenshot">
<img src="/img/tutorial/separate-openapi-schemas/image01.png">
</div>

### Çıkış İçin Model

Ama aynı modeli buradaki gibi bir çıkış olarak kullanırsanız:

{* ../../docs_src/separate_openapi_schemas/tutorial001_py310.py hl[19] *}

...o zaman `description` bir varsayılan değere sahip olduğundan, o alan için **hiçbir şey döndürmezseniz**, yine de o **varsayılan değere** sahip olacaktır.

### Çıkış Yanıt Verileri İçin Model

Belgelerle etkileşime girerseniz ve yanıtı kontrol ederseniz, kod `description` alanlarından birine hiçbir şey eklememiş olsa bile, JSON yanıtı varsayılan değeri (`null`) içerir:

<div class="screenshot">
<img src="/img/tutorial/separate-openapi-schemas/image02.png">
</div>

Bu, **her zaman bir değere sahip olacağı** anlamına gelir, sadece bazen değer `None` (veya JSON terimlerinde `null`) olabilir.

Bu, API'nizi kullanan istemcilerin değerin var olup olmadığını kontrol etmek zorunda olmadığı anlamına gelir, alanın **her zaman orada olacağını varsayabilirler**, sadece bazı durumlarda varsayılan `None` değerine sahip olacaktır.

Bunu OpenAPI'de tanımlamanın yolu, o alanı **zorunlu** olarak işaretlemektir, çünkü her zaman orada olacaktır.

Bu nedenle, bir model için JSON Şeması **giriş veya çıkış** için kullanılmasına bağlı olarak farklı olabilir:

* **giriş** için `description` **zorunlu olmayacaktır**
* **çıkış** için **zorunlu** olacaktır (ve muhtemelen `None` veya JSON terimlerinde `null`)

### Belgelerde Çıkış Modeli

Belgelerde çıkış modelini de kontrol edebilirsiniz, **hem** `name` hem de `description` **kırmızı yıldızla** **zorunlu** olarak işaretlenmiştir:

<div class="screenshot">
<img src="/img/tutorial/separate-openapi-schemas/image03.png">
</div>

### Belgelerde Giriş ve Çıkış Modeli

Ve OpenAPI'deki tüm mevcut Şemaları (JSON Şemaları) kontrol ederseniz, iki tane olduğunu göreceksiniz, bir `Item-Input` ve bir `Item-Output`.

`Item-Input` için `description` **zorunlu değildir**, kırmızı yıldızı yoktur.

Ama `Item-Output` için `description` **zorunludur**, kırmızı yıldızı vardır.

<div class="screenshot">
<img src="/img/tutorial/separate-openapi-schemas/image04.png">
</div>

**Pydantic v2**'den gelen bu özellik ile API belgeleriniz daha **kesin** olur ve otomatik oluşturulmuş istemcileriniz ve SDK'larınız varsa, onlar da daha kesin olur, daha iyi bir **geliştirici deneyimi** ve tutarlılıkla. 🎉

## Şemaları Ayırma

Şimdi, **giriş ve çıkış için aynı şemayı** kullanmak isteyebileceğiniz bazı durumlar vardır.

Muhtemelen bunun ana kullanım durumu, zaten bazı otomatik oluşturulmuş istemci kodu/SDK'larınız varsa ve tüm otomatik oluşturulmuş istemci kodunu/SDK'ları henüz güncellemek istemiyorsanızdır, muhtemelen bir noktada yapacaksınızdır, ama belki şimdi değil.

Bu durumda, bu özelliği **FastAPI**'de `separate_input_output_schemas=False` parametresiyle devre dışı bırakabilirsiniz.

/// info

`separate_input_output_schemas` desteği FastAPI `0.102.0`'da eklenmiştir. 🤓

///

{* ../../docs_src/separate_openapi_schemas/tutorial002_py310.py hl[10] *}

### Belgelerde Giriş ve Çıkış Modelleri İçin Aynı Şema

Ve şimdi giriş ve çıkış için modelin tek bir şeması olacak, yalnızca `Item`, ve `description` **zorunlu olmayan** olarak gösterilecektir:

<div class="screenshot">
<img src="/img/tutorial/separate-openapi-schemas/image05.png">
</div>

Bu, Pydantic v1'deki davranışla aynıdır. 🤓
