# Geçerli Kullanıcıyı Alma

Önceki bölümde güvenlik sistemi (bağımlılık enjeksiyonu sistemine dayanan), *yol operasyonu fonksiyonuna* bir `str` olarak `token` veriyordu:

{* ../../docs_src/security/tutorial001_an_py39.py hl[12] *}

Ancak bu hala çok kullanışlı değil.

Hadi bize geçerli kullanıcıyı versin.

## Bir kullanıcı modeli oluşturun

Önce, bir Pydantic kullanıcı modeli oluşturalım.

Gövdeleri bildirmek için Pydantic'i kullandığımız gibi, başka herhangi bir yerde de kullanabiliriz:

{* ../../docs_src/security/tutorial002_an_py310.py hl[5,12:6] *}

## `get_current_user` bağımlılığı oluşturun

Bir `get_current_user` bağımlılığı oluşturalım.

Bağımlılıkların alt bağımlılıklara sahip olabileceğini hatırlıyor musunuz?

`get_current_user`, daha önce oluşturduğumuz aynı `oauth2_scheme` ile bir bağımlılığa sahip olacaktır.

Daha önce doğrudan *yol operasyonunda* yaptığımız gibi, yeni bağımlılığımız `get_current_user`, alt bağımlılık `oauth2_scheme`'den bir `str` olarak `token` alacaktır:

{* ../../docs_src/security/tutorial002_an_py310.py hl[25] *}

## Kullanıcıyı alın

`get_current_user`, bir tokeni `str` olarak alan ve Pydantic `User` modelimizi döndüren (sahte) bir yardımcı fonksiyon kullanacaktır:

{* ../../docs_src/security/tutorial002_an_py310.py hl[19:22,26:27] *}

## Geçerli kullanıcıyı enjekte edin

Şimdi *yol operasyonunda* `get_current_user` ile aynı `Depends`'i kullanabiliriz:

{* ../../docs_src/security/tutorial002_an_py310.py hl[31] *}

`current_user`'ın tipini Pydantic modeli `User` olarak bildirdiğimize dikkat edin.

Bu, fonksiyonun içinde tüm tamamlama ve tip kontrolleriyle bize yardımcı olacaktır.

/// tip

İstek gövdelerinin de Pydantic modelleriyle bildirildiğini hatırlıyor olabilirsiniz.

Burada **FastAPI**, `Depends` kullandığınız için kafası karışmayacaktır.

///

/// check

Bu bağımlılık sisteminin tasarlanma şekli, hepsinin bir `User` modeli döndüren farklı bağımlılıklara (farklı "bağımlı olunabilirler") sahip olmamıza olanak tanır.

O veri tipini döndürebilecek yalnızca bir bağımlılığa sahip olmakla sınırlı değiliz.

///

## Diğer modeller

Artık geçerli kullanıcıyı doğrudan *yol operasyonu fonksiyonlarında* alabilir ve güvenlik mekanizmalarıyla `Depends` kullanarak **Bağımlılık Enjeksiyonu** seviyesinde ilgilenebilirsiniz.

Ve güvenlik gereksinimleri için herhangi bir model veya veri kullanabilirsiniz (bu durumda, bir Pydantic modeli `User`).

Ancak belirli bir veri modeli, sınıf veya tip kullanmakla sınırlı değilsiniz.

Modelinizde bir `id` ve `email` olmasını ve herhangi bir `username` olmamasını mı istiyorsunuz? Elbette. Aynı araçları kullanabilirsiniz.

Sadece bir `str` mi istiyorsunuz? Veya sadece bir `dict`? Veya doğrudan bir veritabanı sınıfı model örneği? Hepsi aynı şekilde çalışır.

Aslında uygulamanıza giriş yapan kullanıcılarınız yok mu, sadece erişim tokenine sahip robotlar, botlar veya diğer sistemler mi var? Yine, hepsi aynı şekilde çalışır.

Uygulamanız için ihtiyacınız olan herhangi bir model, herhangi bir sınıf, herhangi bir veritabanı kullanın. **FastAPI** bağımlılık enjeksiyonu sistemiyle sizi destekler.

## Kod boyutu

Bu örnek ayrıntılı görünebilir. Güvenlik, veri modelleri, yardımcı fonksiyonlar ve *yol operasyonlarını* aynı dosyada karıştırdığımızı unutmayın.

Ama işte kilit nokta.

Güvenlik ve bağımlılık enjeksiyonu kodu bir kez yazılır.

Ve istediğiniz kadar karmaşık yapabilirsiniz. Ve yine de, tek bir yerde, yalnızca bir kez yazılmış olarak kalır. Tüm esneklikle birlikte.

Ancak aynı güvenlik sistemini kullanan binlerce uç noktanız (*yol operasyonları*) olabilir.

Ve hepsi (veya istediğiniz herhangi bir kısmı), bu bağımlılıkları veya oluşturduğunuz diğer bağımlılıkları yeniden kullanmanın avantajından yararlanabilir.

Ve tüm bu binlerce *yol operasyonu* 3 satır kadar küçük olabilir:

{* ../../docs_src/security/tutorial002_an_py310.py hl[30:32] *}

## Özet

Artık geçerli kullanıcıyı doğrudan *yol operasyonu fonksiyonunuzda* alabilirsiniz.

Zaten yarı yoldayız.

Sadece kullanıcının/istemcinin gerçekten `username` ve `password` göndermesi için bir *yol operasyonu* eklememiz gerekiyor.

Bu bir sonraki adımda gelecek.
