# HTTP Temel Kimlik Doğrulama

En basit durumlar için HTTP Temel Kimlik Doğrulamayı kullanabilirsiniz.

HTTP Temel Kimlik Doğrulamada, uygulama kullanıcı adı ve şifre içeren bir başlık bekler.

Bunu almazsa, HTTP 401 "Unauthorized" hatası döndürür.

Ve `Basic` değerine ve isteğe bağlı bir `realm` parametresine sahip bir `WWW-Authenticate` başlığı döndürür.

Bu, tarayıcıya kullanıcı adı ve şifre için entegre istemi göstermesini söyler.

Ardından, kullanıcı adı ve şifreyi yazdığınızda, tarayıcı bunları başlıkta otomatik olarak gönderir.

## Basit HTTP Temel Kimlik Doğrulama

* `HTTPBasic` ve `HTTPBasicCredentials`'ı içe aktarın.
* `HTTPBasic` kullanarak bir "`security` şeması" oluşturun.
* *Yol operasyonunuzda* bu `security`'yi bir bağımlılıkla kullanın.
* `HTTPBasicCredentials` tipinde bir nesne döndürür:
    * Gönderilen `username` ve `password`'ü içerir.

{* ../../docs_src/security/tutorial006_an_py39.py hl[4,8,12] *}

URL'yi ilk kez açmaya çalıştığınızda (veya belgelerdeki "Execute" düğmesine tıkladığınızda) tarayıcı sizden kullanıcı adınızı ve şifrenizi isteyecektir:

<img src="/img/tutorial/security/image12.png">

## Kullanıcı adını kontrol edin

İşte daha eksiksiz bir örnek.

Kullanıcı adı ve şifrenin doğru olup olmadığını kontrol etmek için bir bağımlılık kullanın.

Bunun için Python standart modülü <a href="https://docs.python.org/3/library/secrets.html" class="external-link" target="_blank">`secrets`</a>'ı kullanarak kullanıcı adı ve şifreyi kontrol edin.

`secrets.compare_digest()` yalnızca ASCII karakterleri (İngilizce'dekiler) içeren `bytes` veya `str` almayı gerektirir, bu da `á` gibi karakterlerle çalışmayacağı anlamına gelir, örneğin `Sebastián`'da olduğu gibi.

Bunu ele almak için, önce `username` ve `password`'ü UTF-8 ile kodlayarak `bytes`'a dönüştürüyoruz.

Ardından `credentials.username`'in `"stanleyjobson"` ve `credentials.password`'ün `"swordfish"` olduğundan emin olmak için `secrets.compare_digest()`'i kullanabiliriz.

{* ../../docs_src/security/tutorial007_an_py39.py hl[1,12:24] *}

Bu şuna benzer olurdu:

```Python
if not (credentials.username == "stanleyjobson") or not (credentials.password == "swordfish"):
    # Bir hata döndür
    ...
```

Ancak `secrets.compare_digest()` kullanarak, "zamanlama saldırıları" adı verilen bir tür saldırıya karşı güvenli olacaktır.

### Zamanlama Saldırıları

Peki "zamanlama saldırısı" nedir?

Bazı saldırganların kullanıcı adı ve şifreyi tahmin etmeye çalıştığını hayal edelim.

Ve `johndoe` kullanıcı adı ve `love123` şifresiyle bir istek gönderiyorlar.

O zaman uygulamanızdaki Python kodu şöyle bir şeye eşdeğer olurdu:

```Python
if "johndoe" == "stanleyjobson" and "love123" == "swordfish":
    ...
```

Ama tam Python `johndoe`'daki ilk `j`'yi `stanleyjobson`'daki ilk `s` ile karşılaştırdığı anda, `False` döndürecektir, çünkü bu iki dizenin aynı olmadığını zaten bilir, "harflerin geri kalanını karşılaştırmak için daha fazla hesaplamayı boşa harcamaya gerek yok" diye düşünür. Ve uygulamanız "Yanlış kullanıcı adı veya şifre" diyecektir.

Ama sonra saldırganlar `stanleyjobsox` kullanıcı adı ve `love123` şifresiyle denerler.

Ve uygulama kodunuz şöyle bir şey yapar:

```Python
if "stanleyjobsox" == "stanleyjobson" and "love123" == "swordfish":
    ...
```

Python, her iki dizenin de aynı olmadığını anlamadan önce `stanleyjobsox` ve `stanleyjobson`'daki tüm `stanleyjobso`'yu karşılaştırmak zorunda kalacaktır. Bu yüzden "Yanlış kullanıcı adı veya şifre" yanıtını vermek birkaç mikrosaniye daha uzun sürecektir.

#### Yanıt süresi saldırganlara yardımcı olur

Bu noktada, sunucunun "Yanlış kullanıcı adı veya şifre" yanıtını göndermek için birkaç mikrosaniye daha uzun sürdüğünü fark ederek, saldırganlar _bir şeyi_ doğru yaptıklarını, başlangıç harflerinin bazılarının doğru olduğunu bileceklerdir.

Ve sonra bunun muhtemelen `johndoe`'dan çok `stanleyjobsox`'a daha benzediğini bilerek tekrar deneyebilirler.

#### "Profesyonel" bir saldırı

Tabii ki, saldırganlar tüm bunları elle denemezler, bunu yapmak için bir program yazarlardı, muhtemelen saniyede binlerce veya milyonlarca testle. Ve her seferinde yalnızca bir ekstra doğru harf elde ederlerdi.

Ama bunu yaparak, birkaç dakika veya saatte saldırganlar doğru kullanıcı adını ve şifreyi tahmin etmiş olurlar, uygulamamızın yalnızca yanıt vermek için harcadığı sürenin "yardımıyla".

#### `secrets.compare_digest()` ile düzeltin

Ama kodumuzda aslında `secrets.compare_digest()` kullanıyoruz.

Kısacası, `stanleyjobsox`'u `stanleyjobson` ile karşılaştırmak, `johndoe`'yu `stanleyjobson` ile karşılaştırmakla aynı süreyi alacaktır. Ve şifre için de aynı şey geçerlidir.

Bu şekilde, uygulama kodunuzda `secrets.compare_digest()` kullanarak, bu tüm güvenlik saldırıları yelpazesine karşı güvenli olacaksınız.

### Hatayı döndürün

Kimlik bilgilerinin yanlış olduğunu tespit ettikten sonra, 401 durum koduna sahip bir `HTTPException` döndürün (kimlik bilgileri sağlanmadığında döndürülenle aynı) ve tarayıcının giriş istemini tekrar göstermesi için `WWW-Authenticate` başlığını ekleyin:

{* ../../docs_src/security/tutorial007_an_py39.py hl[26:30] *}
