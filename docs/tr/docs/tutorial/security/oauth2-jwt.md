# Şifre (ve karma) ile OAuth2, JWT tokenları ile Bearer

Artık tüm güvenlik akışına sahip olduğumuza göre, <abbr title="JSON Web Tokens">JWT</abbr> tokenları ve güvenli şifre karması kullanarak uygulamayı gerçekten güvenli hale getirelim.

Bu kod, uygulamanızda gerçekten kullanabileceğiniz bir koddur, şifre karmalarını veritabanınıza kaydedin, vb.

Önceki bölümde kaldığımız yerden başlayıp artıracağız.

## JWT Hakkında

JWT, "JSON Web Tokens" anlamına gelir.

Bir JSON nesnesini boşluksuz uzun yoğun bir dize halinde kodlamak için bir standarttır. Şöyle görünür:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Şifrelenmemiştir, bu yüzden herkes içeriklerden bilgiyi kurtarabilir.

Ancak imzalanmıştır. Bu yüzden, yayınladığınız bir tokeni aldığınızda, gerçekten siz yayınladığınızı doğrulayabilirsiniz.

Bu şekilde, diyelim ki 1 haftalık bir son kullanma süresiyle bir token oluşturabilirsiniz. Ve ardından kullanıcı ertesi gün tokenle geri geldiğinde, o kullanıcının sisteminize hala giriş yapmış olduğunu bilirsiniz.

Bir hafta sonra, token sona erecek ve kullanıcı yetkilendirilmeyecek ve yeni bir token almak için tekrar giriş yapmak zorunda kalacaktır. Ve kullanıcı (veya üçüncü bir taraf) son kullanma süresini değiştirmek için tokeni değiştirmeye çalışırsa, imzalar eşleşmeyeceği için bunu keşfedebilirsiniz.

JWT tokenlarıyla oynamak ve nasıl çalıştığını görmek istiyorsanız, <a href="https://jwt.io/" class="external-link" target="_blank">https://jwt.io</a> adresini kontrol edin.

## `PyJWT` yükleyin

Python'da JWT tokenlarını oluşturmak ve doğrulamak için `PyJWT` yüklememiz gerekiyor.

Bir [sanal ortam](../../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından `pyjwt`'yi yükleyin:

<div class="termy">

```console
$ pip install pyjwt

---> 100%
```

</div>

/// info

RSA veya ECDSA gibi dijital imza algoritmaları kullanmayı planlıyorsanız, kriptografi kütüphanesi bağımlılığı `pyjwt[crypto]`'yu yüklemelisiniz.

Daha fazla bilgiyi <a href="https://pyjwt.readthedocs.io/en/latest/installation.html" class="external-link" target="_blank">PyJWT Kurulum belgelerinde</a> okuyabilirsiniz.

///

## Şifre karması

"Karma" (hashing), bazı içerikleri (bu durumda bir şifreyi) anlamsız görünen bir bayt dizisine (sadece bir dize) dönüştürmek anlamına gelir.

Tam olarak aynı içeriği (tam olarak aynı şifreyi) her geçirdiğinizde tam olarak aynı anlamsız diziyi alırsınız.

Ancak anlamsız diziden şifreye geri dönüştüremezsiniz.

### Neden şifre karması kullanılır

Veritabanınız çalınırsa, hırsız kullanıcılarınızın düz metin şifrelerine değil, yalnızca karmalara sahip olacaktır.

Bu yüzden, hırsız o şifreyi başka bir sistemde kullanmaya çalışamayacaktır (birçok kullanıcı her yerde aynı şifreyi kullandığından, bu tehlikeli olurdu).

## `passlib` yükleyin

PassLib, şifre karmalarını ele almak için harika bir Python paketidir.

Birçok güvenli karma algoritmasını ve bunlarla çalışmak için yardımcı araçları destekler.

Önerilen algoritma "Bcrypt"tir.

Bir [sanal ortam](../../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından PassLib'i Bcrypt ile yükleyin:

<div class="termy">

```console
$ pip install "passlib[bcrypt]"

---> 100%
```

</div>

/// tip

`passlib` ile, **Django**, bir **Flask** güvenlik eklentisi veya diğer birçoğu tarafından oluşturulan şifreleri okuyabilecek şekilde bile yapılandırabilirsiniz.

Böylece, örneğin bir Django uygulamasındaki aynı verileri bir veritabanında bir FastAPI uygulamasıyla paylaşabilirsiniz. Veya aynı veritabanını kullanarak bir Django uygulamasını kademeli olarak taşıyabilirsiniz.

Ve kullanıcılarınız Django uygulamanızdan veya **FastAPI** uygulamanızdan aynı anda giriş yapabilir.

///

## Şifreleri karma ve doğrulama

İhtiyacımız olan araçları `passlib`'den içe aktarın.

Bir PassLib "bağlamı" oluşturun. Bu, şifreleri karma ve doğrulamak için kullanılacak olan şeydir.

/// tip

PassLib bağlamı ayrıca farklı karma algoritmalarını kullanma işlevselliğine de sahiptir, yalnızca bunları doğrulamaya izin vermek için kullanımdan kaldırılmış eskilerini de dahil eder, vb.

Örneğin, başka bir sistem (Django gibi) tarafından oluşturulan şifreleri okumak ve doğrulamak için kullanabilir, ancak yeni şifreleri Bcrypt gibi farklı bir algoritmayla karma yapabilirsiniz.

Ve hepsiyle aynı anda uyumlu olabilirsiniz.

///

Kullanıcıdan gelen bir şifreyi karma yapmak için bir yardımcı fonksiyon oluşturun.

Ve alınan şifrenin saklanan karma ile eşleşip eşleşmediğini doğrulamak için bir tane daha.

Ve bir kullanıcıyı doğrulamak ve döndürmek için bir tane daha.

{* ../../docs_src/security/tutorial004_an_py310.py hl[8,49,56:57,60:61,70:76] *}

/// note

Yeni (sahte) veritabanı `fake_users_db`'yi kontrol ederseniz, karma şifrenin şimdi nasıl göründüğünü göreceksiniz: `"$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"`.

///

## JWT tokenlarını ele alma

Yüklenen modülleri içe aktarın.

JWT tokenlarını imzalamak için kullanılacak rastgele bir gizli anahtar oluşturun.

Güvenli rastgele bir gizli anahtar oluşturmak için şu komutu kullanın:

<div class="termy">

```console
$ openssl rand -hex 32

09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
```

</div>

Ve çıktıyı `SECRET_KEY` değişkenine kopyalayın (örnektekini kullanmayın).

JWT tokenını imzalamak için kullanılan algoritma ile bir `ALGORITHM` değişkeni oluşturun ve `"HS256"` olarak ayarlayın.

Tokenin sona ermesi için bir değişken oluşturun.

Token uç noktasında yanıt için kullanılacak bir Pydantic Modeli tanımlayın.

Yeni bir erişim tokeni oluşturmak için bir yardımcı fonksiyon oluşturun.

{* ../../docs_src/security/tutorial004_an_py310.py hl[4,7,13:15,29:31,79:87] *}

## Bağımlılıkları güncelleyin

`get_current_user`'ı daha önce olduğu gibi aynı tokeni alacak şekilde güncelleyin, ancak bu sefer JWT tokenları kullanarak.

Alınan tokeni çözün, doğrulayın ve geçerli kullanıcıyı döndürün.

Token geçersizse, hemen bir HTTP hatası döndürün.

{* ../../docs_src/security/tutorial004_an_py310.py hl[90:107] *}

## `/token` *yol operasyonunu* güncelleyin

Tokenin sona erme süresiyle bir `timedelta` oluşturun.

Gerçek bir JWT erişim tokeni oluşturun ve döndürün.

{* ../../docs_src/security/tutorial004_an_py310.py hl[118:133] *}

### JWT "konu" `sub` hakkında teknik detaylar

JWT spesifikasyonu, tokenin konusuyla bir `sub` anahtarı olduğunu söyler.

Kullanmak isteğe bağlıdır, ancak kullanıcının kimliğini koyacağınız yer orasıdır, bu yüzden burada kullanıyoruz.

JWT, bir kullanıcıyı tanımlamanın ve doğrudan API'nizde işlemler gerçekleştirmesine izin vermenin yanı sıra başka şeyler için de kullanılabilir.

Örneğin, bir "araba" veya bir "blog yazısı" tanımlayabilirsiniz.

Ardından o varlık hakkında izinler ekleyebilirsiniz, "sür" (araba için) veya "düzenle" (blog yazısı için) gibi.

Ve ardından, o JWT tokenini bir kullanıcıya (veya bota) verebilirsiniz ve onlar bir hesaba sahip olmaya bile gerek kalmadan, sadece API'nizin o amaçla oluşturduğu JWT tokeniyle bu eylemleri (arabayı sürmek veya blog yazısını düzenlemek) gerçekleştirmek için kullanabilirler.

Bu fikirleri kullanarak, JWT çok daha sofistike senaryolar için kullanılabilir.

Bu durumlarda, bu varlıklardan birçoğu aynı ID'ye sahip olabilir, diyelim ki `foo` (bir kullanıcı `foo`, bir araba `foo` ve bir blog yazısı `foo`).

Bu yüzden, ID çakışmalarından kaçınmak için, kullanıcı için JWT tokeni oluştururken, `sub` anahtarının değerine bir önek ekleyebilirsiniz, örneğin `username:`. Yani bu örnekte, `sub`'un değeri şu olabilirdi: `username:johndoe`.

Akılda tutulması gereken önemli şey, `sub` anahtarının tüm uygulama genelinde benzersiz bir tanımlayıcıya sahip olması ve bir dize olması gerektiğidir.

## Kontrol edin

Sunucuyu çalıştırın ve belgelere gidin: <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Kullanıcı arayüzünü şöyle göreceksiniz:

<img src="/img/tutorial/security/image07.png">

Uygulamayı daha önce olduğu gibi yetkilendirin.

Kimlik bilgilerini kullanarak:

Kullanıcı adı: `johndoe`
Şifre: `secret`

/// check

Kodun hiçbir yerinde düz metin şifre "`secret`"in olmadığına dikkat edin, yalnızca karma versiyonuna sahibiz.

///

<img src="/img/tutorial/security/image08.png">

`/users/me/` uç noktasını çağırın, yanıtı şöyle alacaksınız:

```JSON
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false
}
```

<img src="/img/tutorial/security/image09.png">

Geliştirici araçlarını açarsanız, gönderilen verilerin yalnızca tokeni içerdiğini görebilirsiniz, şifre yalnızca kullanıcının kimliğini doğrulamak ve o erişim tokenini almak için ilk istekte gönderilir, sonrasında gönderilmez:

<img src="/img/tutorial/security/image10.png">

/// note

`Authorization` başlığına dikkat edin, değeri `Bearer ` ile başlar.

///

## `scopes` ile gelişmiş kullanım

OAuth2'nin "kapsamlar" kavramı vardır.

Bunları bir JWT tokenine belirli bir izin seti eklemek için kullanabilirsiniz.

Ardından bu tokeni bir kullanıcıya doğrudan veya üçüncü bir tarafa, bir dizi kısıtlamayla API'nizle etkileşim kurmaları için verebilirsiniz.

Bunları nasıl kullanacağınızı ve **FastAPI**'ye nasıl entegre edildiklerini **Gelişmiş Kullanıcı Kılavuzu**'nda öğrenebilirsiniz.

## Özet

Şimdiye kadar gördüklerinizle, OAuth2 ve JWT gibi standartları kullanarak güvenli bir **FastAPI** uygulaması kurabilirsiniz.

Hemen hemen her framework'te güvenliği ele almak oldukça hızlı bir şekilde karmaşık bir konu haline gelir.

Bunu çok basitleştiren birçok paket, veri modeli, veritabanı ve mevcut özelliklerle birçok ödün vermek zorundadır. Ve işleri çok fazla basitleştiren bu paketlerden bazıları aslında altında güvenlik açıkları barındırır.

---

**FastAPI**, herhangi bir veritabanı, veri modeli veya araçla herhangi bir ödün vermez.

Projenize en uygun olanları seçmeniz için size tüm esnekliği verir.

Ve `passlib` ve `PyJWT` gibi iyi bakılan ve yaygın olarak kullanılan birçok paketi doğrudan kullanabilirsiniz, çünkü **FastAPI** harici paketleri entegre etmek için herhangi bir karmaşık mekanizma gerektirmez.

Ancak size esneklik, sağlamlık veya güvenlikten ödün vermeden süreci mümkün olduğunca basitleştirmek için araçlar sağlar.

Ve OAuth2 gibi güvenli, standart protokolleri nispeten basit bir şekilde kullanabilir ve uygulayabilirsiniz.
