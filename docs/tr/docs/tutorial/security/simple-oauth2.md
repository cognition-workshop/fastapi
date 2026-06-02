# Şifre ve Bearer ile Basit OAuth2

Şimdi önceki bölümden devam edip eksik parçaları ekleyerek tam bir güvenlik akışına sahip olalım.

## `username` ve `password`'ü alın

`username` ve `password`'ü almak için **FastAPI** güvenlik yardımcı araçlarını kullanacağız.

OAuth2, "password akışını" (kullandığımız) kullanırken istemcinin/kullanıcının `username` ve `password` alanlarını form verisi olarak göndermesi gerektiğini belirtir.

Ve spesifikasyon, alanların tam olarak bu şekilde adlandırılması gerektiğini söyler. Bu yüzden `user-name` veya `email` çalışmaz.

Ama endişelenmeyin, frontend'de son kullanıcılarınıza istediğiniz gibi gösterebilirsiniz.

Ve veritabanı modelleriniz istediğiniz herhangi bir ad kullanabilir.

Ancak giriş *yol operasyonu* için, spesifikasyonla uyumlu olmak (ve örneğin, entegre API belge sistemini kullanabilmek) için bu adları kullanmamız gerekir.

Spesifikasyon ayrıca `username` ve `password`'ün form verisi olarak gönderilmesi gerektiğini belirtir (yani burada JSON yok).

### `scope`

Spesifikasyon ayrıca istemcinin başka bir form alanı "`scope`" gönderebileceğini söyler.

Form alanının adı `scope`'dur (tekil), ancak aslında boşluklarla ayrılmış "kapsamları" olan uzun bir dizedir.

Her "kapsam" sadece bir dizedir (boşluk olmadan).

Bunlar normalde belirli güvenlik izinlerini bildirmek için kullanılır, örneğin:

* `users:read` veya `users:write` yaygın örneklerdir.
* `instagram_basic` Facebook / Instagram tarafından kullanılır.
* `https://www.googleapis.com/auth/drive` Google tarafından kullanılır.

/// info

OAuth2'de bir "kapsam", belirli bir gerekli izni bildiren bir dizedir.

`:` veya URL gibi başka karakterler içerip içermediği önemli değildir.

Bu ayrıntılar uygulamaya özgüdür.

OAuth2 için bunlar sadece dizelerdir.

///

## `username` ve `password`'ü almak için kod

Şimdi bunu ele almak için **FastAPI** tarafından sağlanan yardımcı araçları kullanalım.

### `OAuth2PasswordRequestForm`

İlk olarak, `OAuth2PasswordRequestForm`'u içe aktarın ve `/token` için *yol operasyonunda* `Depends` ile bağımlılık olarak kullanın:

{* ../../docs_src/security/tutorial003_an_py310.py hl[4,78] *}

`OAuth2PasswordRequestForm`, şunlarla bir form gövdesi bildiren bir sınıf bağımlılığıdır:

* `username`.
* `password`.
* Boşluklarla ayrılmış dizelerden oluşan büyük bir dize olarak isteğe bağlı bir `scope` alanı.
* İsteğe bağlı bir `grant_type`.

/// tip

OAuth2 spesifikasyonu aslında sabit `password` değerine sahip bir `grant_type` alanı *gerektirir*, ancak `OAuth2PasswordRequestForm` bunu zorunlu kılmaz.

Bunu zorunlu kılmanız gerekiyorsa, `OAuth2PasswordRequestForm` yerine `OAuth2PasswordRequestFormStrict` kullanın.

///

* İsteğe bağlı bir `client_id` (örneğimiz için ihtiyacımız yok).
* İsteğe bağlı bir `client_secret` (örneğimiz için ihtiyacımız yok).

/// info

`OAuth2PasswordRequestForm`, `OAuth2PasswordBearer` gibi **FastAPI** için özel bir sınıf değildir.

`OAuth2PasswordBearer`, **FastAPI**'ye bunun bir güvenlik şeması olduğunu bildirir. Bu yüzden OpenAPI'ye bu şekilde eklenir.

Ancak `OAuth2PasswordRequestForm`, kendiniz de yazabilecek veya doğrudan `Form` parametreleri bildirebilecek bir sınıf bağımlılığıdır.

Ancak yaygın bir kullanım durumu olduğundan, kolaylaştırmak için doğrudan **FastAPI** tarafından sağlanır.

///

### Form verisini kullanın

/// tip

Bağımlılık sınıfı `OAuth2PasswordRequestForm`'un örneği, boşluklarla ayrılmış uzun dizeye sahip bir `scope` niteliğine sahip olmayacak, bunun yerine gönderilen her kapsam için gerçek dize listesine sahip bir `scopes` niteliğine sahip olacaktır.

Bu örnekte `scopes` kullanmıyoruz, ancak ihtiyacınız olursa işlevsellik orada.

///

Şimdi, form alanından `username` kullanarak (sahte) veritabanından kullanıcı verilerini alın.

Böyle bir kullanıcı yoksa, "Yanlış kullanıcı adı veya şifre" diyen bir hata döndürürüz.

Hata için `HTTPException` istisnasını kullanırız:

{* ../../docs_src/security/tutorial003_an_py310.py hl[3,79:81] *}

### Şifreyi kontrol edin

Bu noktada veritabanımızdan kullanıcı verilerine sahibiz, ancak şifreyi henüz kontrol etmedik.

Önce bu veriyi Pydantic `UserInDB` modeline koyalım.

Düz metin şifreleri asla kaydetmemelisiniz, bu yüzden (sahte) şifre karma sistemini kullanacağız.

Şifreler eşleşmezse, aynı hatayı döndürürüz.

#### Şifre karması

"Karma" (hashing), bazı içerikleri (bu durumda bir şifreyi) anlamsız görünen bir bayt dizisine (sadece bir dize) dönüştürmek anlamına gelir.

Tam olarak aynı içeriği (tam olarak aynı şifreyi) her geçirdiğinizde tam olarak aynı anlamsız diziyi alırsınız.

Ancak anlamsız diziden şifreye geri dönüştüremezsiniz.

##### Neden şifre karması kullanılır

Veritabanınız çalınırsa, hırsız kullanıcılarınızın düz metin şifrelerine değil, yalnızca karmalara sahip olacaktır.

Bu yüzden, hırsız aynı şifreleri başka bir sistemde kullanmaya çalışamayacaktır (birçok kullanıcı her yerde aynı şifreyi kullandığından, bu tehlikeli olurdu).

{* ../../docs_src/security/tutorial003_an_py310.py hl[82:85] *}

#### `**user_dict` hakkında

`UserInDB(**user_dict)` şu anlama gelir:

*`user_dict`'in anahtar ve değerlerini doğrudan anahtar-değer argümanları olarak iletin, eşdeğeri:*

```Python
UserInDB(
    username = user_dict["username"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    disabled = user_dict["disabled"],
    hashed_password = user_dict["hashed_password"],
)
```

/// info

`**user_dict` hakkında daha eksiksiz bir açıklama için [**Ekstra Modeller** belgelerine](../extra-models.md#about-user_indict){.internal-link target=_blank} bakın.

///

## Tokeni döndürün

`token` uç noktasının yanıtı bir JSON nesnesi olmalıdır.

Bir `token_type`'a sahip olmalıdır. Bizim durumumuzda, "Bearer" tokenları kullandığımız için, token tipi "`bearer`" olmalıdır.

Ve erişim tokenimizi içeren bir dize ile `access_token`'a sahip olmalıdır.

Bu basit örnek için, tamamen güvensiz olacağız ve aynı `username`'i token olarak döndüreceğiz.

/// tip

Bir sonraki bölümde, şifre karma ve <abbr title="JSON Web Tokens">JWT</abbr> tokenları ile gerçek güvenli bir uygulama göreceksiniz.

Ama şimdilik, ihtiyacımız olan belirli ayrıntılara odaklanalım.

///

{* ../../docs_src/security/tutorial003_an_py310.py hl[87] *}

/// tip

Spesifikasyona göre, bu örnekteki gibi bir `access_token` ve `token_type` ile bir JSON döndürmelisiniz.

Bu, kodunuzda kendiniz yapmanız ve bu JSON anahtarlarını kullandığınızdan emin olmanız gereken bir şeydir.

Spesifikasyonlarla uyumlu olmak için kendiniz doğru şekilde yapmayı hatırlamanız gereken neredeyse tek şey budur.

Geri kalan her şey için, **FastAPI** sizin için halleder.

///

## Bağımlılıkları güncelleyin

Şimdi bağımlılıklarımızı güncelleyeceğiz.

`current_user`'ı *yalnızca* bu kullanıcı aktifse almak istiyoruz.

Bu yüzden, sırayla bağımlılık olarak `get_current_user`'ı kullanan ek bir `get_current_active_user` bağımlılığı oluşturuyoruz.

Bu bağımlılıkların her ikisi de, kullanıcı yoksa veya aktif değilse bir HTTP hatası döndürecektir.

Bu yüzden, uç noktamızda yalnızca kullanıcı varsa, doğru şekilde kimlik doğrulaması yapılmışsa ve aktifse bir kullanıcı alacağız:

{* ../../docs_src/security/tutorial003_an_py310.py hl[58:66,69:74,94] *}

/// info

Burada döndürdüğümüz `Bearer` değerine sahip ek `WWW-Authenticate` başlığı da spesifikasyonun bir parçasıdır.

Herhangi bir HTTP (hata) durum kodu 401 "UNAUTHORIZED", ayrıca bir `WWW-Authenticate` başlığı döndürmelidir.

Bearer tokenları (bizim durumumuz) söz konusu olduğunda, bu başlığın değeri `Bearer` olmalıdır.

Aslında bu ek başlığı atlayabilirsiniz ve yine de çalışır.

Ama burada spesifikasyonlarla uyumlu olmak için sağlanmıştır.

Ayrıca, onu bekleyen ve kullanan araçlar (şimdi veya gelecekte) olabilir ve bu sizin veya kullanıcılarınız için şimdi veya gelecekte faydalı olabilir.

Standartların faydası budur...

///

## Çalışırken görün

Etkileşimli belgeleri açın: <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

### Kimlik doğrulama

"Authorize" butonuna tıklayın.

Kimlik bilgilerini kullanın:

Kullanıcı: `johndoe`

Şifre: `secret`

<img src="/img/tutorial/security/image04.png">

Sistemde kimlik doğrulamasından sonra, şöyle göreceksiniz:

<img src="/img/tutorial/security/image05.png">

### Kendi kullanıcı verilerinizi alın

Şimdi `/users/me` yoluyla `GET` operasyonunu kullanın.

Kullanıcı verilerinizi şöyle alacaksınız:

```JSON
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false,
  "hashed_password": "fakehashedsecret"
}
```

<img src="/img/tutorial/security/image06.png">

Kilit simgesine tıklayıp çıkış yaparsanız ve ardından aynı operasyonu tekrar denerseniz, şu HTTP 401 hatasını alırsınız:

```JSON
{
  "detail": "Not authenticated"
}
```

### Aktif olmayan kullanıcı

Şimdi aktif olmayan bir kullanıcıyla deneyin, şunlarla kimlik doğrulaması yapın:

Kullanıcı: `alice`

Şifre: `secret2`

Ve `/users/me` yoluyla `GET` operasyonunu kullanmayı deneyin.

Şöyle bir "Aktif olmayan kullanıcı" hatası alacaksınız:

```JSON
{
  "detail": "Inactive user"
}
```

## Özet

Artık API'niz için `username` ve `password`'e dayalı tam bir güvenlik sistemi uygulamak için araçlara sahipsiniz.

Bu araçları kullanarak, güvenlik sistemini herhangi bir veritabanı ve herhangi bir kullanıcı veya veri modeliyle uyumlu hale getirebilirsiniz.

Eksik olan tek ayrıntı, bunun henüz gerçekten "güvenli" olmamasıdır.

Bir sonraki bölümde güvenli bir şifre karma kütüphanesi ve <abbr title="JSON Web Tokens">JWT</abbr> tokenları kullanmayı göreceksiniz.
