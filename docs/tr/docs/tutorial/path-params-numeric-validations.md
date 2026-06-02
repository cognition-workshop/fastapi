# Yol Parametreleri ve Sayısal Doğrulamalar

Sorgu parametreleri için `Query` ile daha fazla doğrulama ve meta veri bildirebildiğiniz gibi, yol parametreleri için de `Path` ile aynı tür doğrulamaları ve meta verileri bildirebilirsiniz.

## Path'i içe aktarın

Önce, `fastapi`'den `Path`'i ve `Annotated`'ı içe aktarın:

{* ../../docs_src/path_params_numeric_validations/tutorial001_an_py310.py hl[1,3] *}

/// info

FastAPI, 0.95.0 sürümünde `Annotated` desteği ekledi (ve önermeye başladı).

Eski bir sürümünüz varsa, `Annotated` kullanmaya çalışırken hatalar alırsınız.

`Annotated` kullanmadan önce [FastAPI sürümünü](../deployment/versions.md#upgrading-the-fastapi-versions){.internal-link target=_blank} en az 0.95.1'e yükselttiğinizden emin olun.

///

## Meta veri bildirme

`Query` için olduğu gibi aynı parametrelerin tümünü bildirebilirsiniz.

Örneğin, `item_id` yol parametresi için bir `title` meta veri değeri bildirmek için şunu yazabilirsiniz:

{* ../../docs_src/path_params_numeric_validations/tutorial001_an_py310.py hl[10] *}

/// note

Bir yol parametresi, yolun bir parçası olmak zorunda olduğu için her zaman gereklidir. `None` ile bildirilse veya bir varsayılan değer ayarlansa bile, hiçbir şeyi etkilemez, yine de her zaman gerekli olacaktır.

///

## Parametreleri ihtiyacınıza göre sıralayın

/// tip

`Annotated` kullanıyorsanız bu muhtemelen o kadar önemli veya gerekli değildir.

///

Diyelim ki `q` sorgu parametresini gerekli bir `str` olarak bildirmek istiyorsunuz.

Ve bu parametre için başka bir şey bildirmenize gerek yok, bu yüzden `Query` kullanmanıza gerçekten gerek yok.

Ancak `item_id` yol parametresi için yine de `Path` kullanmanız gerekiyor. Ve herhangi bir nedenle `Annotated` kullanmak istemiyorsunuz.

Python, "varsayılanı" olmayan bir değerden önce "varsayılana" sahip bir değer koyarsanız şikayet edecektir.

Ancak onları yeniden sıralayabilir ve varsayılanı olmayan değeri (sorgu parametresi `q`) ilk sıraya koyabilirsiniz.

**FastAPI** için önemli değildir. Parametreleri adlarına, tiplerine ve varsayılan bildirimlerine (`Query`, `Path`, vb.) göre algılayacaktır, sırayı umursamaz.

Bu yüzden, fonksiyonunuzu şu şekilde bildirebilirsiniz:

//// tab | Python 3.8 non-Annotated

/// tip

Mümkünse `Annotated` sürümünü kullanmayı tercih edin.

///

{* ../../docs_src/path_params_numeric_validations/tutorial002.py hl[7] *}

////

Ancak `Annotated` kullanırsanız bu sorunu yaşamayacağınızı unutmayın, `Query()` veya `Path()` için fonksiyon parametre varsayılan değerlerini kullanmadığınız için önemli olmayacaktır.

{* ../../docs_src/path_params_numeric_validations/tutorial002_an_py39.py *}

## Parametreleri ihtiyacınıza göre sıralayın, püf noktalar

/// tip

`Annotated` kullanıyorsanız bu muhtemelen o kadar önemli veya gerekli değildir.

///

İşte işe yarayabilecek **küçük bir püf noktası**, ancak çok sık ihtiyacınız olmayacak.

Şunları yapmak istiyorsanız:

* `q` sorgu parametresini `Query` veya herhangi bir varsayılan değer olmadan bildirmek
* `Path` kullanarak `item_id` yol parametresini bildirmek
* Onları farklı bir sırada tutmak
* `Annotated` kullanmamak

...Python'un bunun için küçük bir özel sözdizimi var.

Fonksiyonun ilk parametresi olarak `*` iletin.

Python o `*` ile hiçbir şey yapmayacaktır, ancak sonraki tüm parametrelerin anahtar kelime argümanları (anahtar-değer çiftleri) olarak çağrılması gerektiğini bilecektir, bunlar <abbr title="Kaynak: K-ey W-ord Arg-uments"><code>kwargs</code></abbr> olarak da bilinir. Varsayılan değerleri olmasa bile.

{* ../../docs_src/path_params_numeric_validations/tutorial003.py hl[7] *}

### `Annotated` ile daha iyi

`Annotated` kullanırsanız, fonksiyon parametre varsayılan değerlerini kullanmadığınız için bu sorunu yaşamayacağınızı ve muhtemelen `*` kullanmanıza gerek olmayacağını unutmayın.

{* ../../docs_src/path_params_numeric_validations/tutorial003_an_py39.py hl[10] *}

## Sayısal doğrulamalar: büyük veya eşit

`Query` ve `Path` (ve daha sonra göreceğiniz diğerleri) ile sayı kısıtlamaları bildirebilirsiniz.

Burada, `ge=1` ile, `item_id`'nin `1`'e "`g`reater than or `e`qual" (büyük veya eşit) bir tamsayı olması gerekecektir.

{* ../../docs_src/path_params_numeric_validations/tutorial004_an_py39.py hl[10] *}

## Sayısal doğrulamalar: büyük ve küçük veya eşit

Aynı şey şunlar için de geçerlidir:

* `gt`: `g`reater `t`han (büyük)
* `le`: `l`ess than or `e`qual (küçük veya eşit)

{* ../../docs_src/path_params_numeric_validations/tutorial005_an_py39.py hl[10] *}

## Sayısal doğrulamalar: ondalık sayılar, büyük ve küçük

Sayısal doğrulamalar `float` değerleri için de çalışır.

İşte burada sadece <abbr title="büyük veya eşit"><code>ge</code></abbr> değil, <abbr title="büyük"><code>gt</code></abbr> bildirmenin önemli olduğu yer burasıdır. Bununla, örneğin, bir değerin `0`'dan büyük olmasını gerektirebilirsiniz, `1`'den küçük olsa bile.

Yani, `0.5` geçerli bir değer olacaktır. Ancak `0.0` veya `0` olmayacaktır.

Ve <abbr title="küçük"><code>lt</code></abbr> için de aynısı geçerlidir.

{* ../../docs_src/path_params_numeric_validations/tutorial006_an_py39.py hl[13] *}

## Özet

`Query`, `Path` (ve henüz görmediğiniz diğerleri) ile [Sorgu Parametreleri ve String Doğrulamaları](query-params-str-validations.md){.internal-link target=_blank}'ndaki ile aynı şekillerde meta veri ve string doğrulamaları bildirebilirsiniz.

Ve ayrıca sayısal doğrulamalar da bildirebilirsiniz:

* `gt`: `g`reater `t`han (büyük)
* `ge`: `g`reater than or `e`qual (büyük veya eşit)
* `lt`: `l`ess `t`han (küçük)
* `le`: `l`ess than or `e`qual (küçük veya eşit)

/// info

`Query`, `Path` ve daha sonra göreceğiniz diğer sınıflar, ortak bir `Param` sınıfının alt sınıflarıdır.

Hepsi, gördüğünüz ek doğrulama ve meta veriler için aynı parametreleri paylaşır.

///

/// note | Teknik Detaylar

`fastapi`'den `Query`, `Path` ve diğerlerini içe aktardığınızda, bunlar aslında fonksiyonlardır.

Çağrıldıklarında, aynı isimde sınıfların örneklerini döndürürler.

Yani, bir fonksiyon olan `Query`'yi içe aktarırsınız. Ve çağırdığınızda, aynı zamanda `Query` olarak adlandırılan bir sınıfın örneğini döndürür.

Bu fonksiyonlar (sınıfları doğrudan kullanmak yerine) editörünüzün tipleri hakkında hata işaretlememesi için vardır.

Bu şekilde, bu hataları görmezden gelmek için özel yapılandırmalar eklemek zorunda kalmadan normal editörünüzü ve kodlama araçlarınızı kullanabilirsiniz.

///
