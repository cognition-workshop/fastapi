# Güvenlik - İlk Adımlar

**Backend** API'nizin bir etki alanında olduğunu hayal edelim.

Ve başka bir etki alanında veya aynı etki alanının farklı bir yolunda (ya da bir mobil uygulamada) bir **frontend**'iniz var.

Ve frontend'in bir **kullanıcı adı** ve **şifre** kullanarak backend ile kimlik doğrulaması yapmasının bir yolunu istiyorsunuz.

Bunu **FastAPI** ile **OAuth2** kullanarak oluşturabiliriz.

Ama sadece ihtiyacınız olan küçük bilgi parçalarını bulmak için uzun spesifikasyonu tamamen okuma zahmetinden sizi kurtaralım.

Güvenliği ele almak için **FastAPI** tarafından sağlanan araçları kullanalım.

## Nasıl görünüyor

Önce kodu kullanıp nasıl çalıştığını görelim, sonra ne olduğunu anlamak için geri dönelim.

## `main.py` oluşturun

Örneği bir `main.py` dosyasına kopyalayın:

{* ../../docs_src/security/tutorial001_an_py39.py *}

## Çalıştırın

/// info

<a href="https://github.com/Kludex/python-multipart" class="external-link" target="_blank">`python-multipart`</a> paketi, `pip install "fastapi[standard]"` komutunu çalıştırdığınızda **FastAPI** ile birlikte otomatik olarak yüklenir.

Ancak, `pip install fastapi` komutunu kullanırsanız, `python-multipart` paketi varsayılan olarak dahil edilmez.

Manuel olarak yüklemek için, bir [sanal ortam](../../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından şu şekilde yükleyin:

```console
$ pip install python-multipart
```

Bunun nedeni, **OAuth2**'nin `username` ve `password` göndermek için "form verisi" kullanmasıdır.

///

Örneği şu şekilde çalıştırın:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

## Kontrol edin

Etkileşimli belgelere gidin: <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Şuna benzer bir şey göreceksiniz:

<img src="/img/tutorial/security/image01.png">

/// check | Authorize butonu!

Zaten parlak yeni bir "Authorize" butonunuz var.

Ve *yol operasyonunuzda* sağ üst köşede tıklayabileceğiniz küçük bir kilit var.

///

Ve tıklarsanız, bir `username` ve `password` (ve diğer isteğe bağlı alanları) yazmak için küçük bir yetkilendirme formu görürsünüz:

<img src="/img/tutorial/security/image02.png">

/// note

Formda ne yazdığınız önemli değil, henüz çalışmayacak. Ama oraya varacağız.

///

Bu elbette son kullanıcılar için frontend değildir, ancak tüm API'nizi etkileşimli olarak belgelemek için harika bir otomatik araçtır.

Frontend ekibi tarafından kullanılabilir (siz de olabilirsiniz).

Üçüncü taraf uygulamalar ve sistemler tarafından kullanılabilir.

Ve aynı uygulamayı hata ayıklamak, kontrol etmek ve test etmek için kendiniz tarafından da kullanılabilir.

## `password` akışı

Şimdi biraz geri dönelim ve tüm bunların ne olduğunu anlayalım.

`password` "akışı", güvenlik ve kimlik doğrulamayı ele almak için OAuth2'de tanımlanan yollardan ("akışlar") biridir.

OAuth2, backend veya API'nin kullanıcıyı doğrulayan sunucudan bağımsız olabilmesi için tasarlanmıştır.

Ancak bu durumda, aynı **FastAPI** uygulaması hem API'yi hem de kimlik doğrulamayı ele alacaktır.

Öyleyse, bunu bu basitleştirilmiş bakış açısından inceleyelim:

* Kullanıcı frontend'de `username` ve `password` yazar ve `Enter`'a basar.
* Frontend (kullanıcının tarayıcısında çalışan), bu `username` ve `password`'ü API'mizdeki belirli bir URL'ye gönderir (`tokenUrl="token"` ile bildirilmiş).
* API, bu `username` ve `password`'ü kontrol eder ve bir "token" ile yanıt verir (bunların hiçbirini henüz uygulamadık).
    * Bir "token", bu kullanıcıyı doğrulamak için daha sonra kullanabileceğimiz bazı içeriğe sahip bir dizedir.
    * Normalde, bir token bir süre sonra sona erecek şekilde ayarlanır.
        * Bu yüzden, kullanıcı daha sonra bir noktada tekrar giriş yapmak zorunda kalacaktır.
        * Ve token çalınırsa, risk daha azdır. Sonsuza kadar çalışacak kalıcı bir anahtar gibi değildir (çoğu durumda).
* Frontend bu tokeni geçici olarak bir yerde saklar.
* Kullanıcı frontend web uygulamasının başka bir bölümüne gitmek için frontend'de tıklar.
* Frontend'in API'den daha fazla veri çekmesi gerekir.
    * Ancak o belirli uç nokta için kimlik doğrulama gerekir.
    * Bu yüzden, API'mizle kimlik doğrulaması yapmak için değeri `Bearer ` artı token olan bir `Authorization` başlığı gönderir.
    * Token `foobar` içeriyorsa, `Authorization` başlığının içeriği şu olacaktır: `Bearer foobar`.

## **FastAPI**'nin `OAuth2PasswordBearer`'ı

**FastAPI**, bu güvenlik özelliklerini uygulamak için farklı soyutlama seviyelerinde çeşitli araçlar sağlar.

Bu örnekte **OAuth2**'yi, **Password** akışıyla, bir **Bearer** token kullanarak kullanacağız. Bunu `OAuth2PasswordBearer` sınıfını kullanarak yapıyoruz.

/// info

Bir "bearer" tokeni tek seçenek değildir.

Ancak kullanım durumumuz için en iyisidir.

Ve bir OAuth2 uzmanı olmadığınız ve başka bir seçeneğin ihtiyaçlarınıza daha uygun olduğunu tam olarak bilmediğiniz sürece, çoğu kullanım durumu için en iyisi olabilir.

Bu durumda, **FastAPI** size onu oluşturmak için araçlar da sağlar.

///

`OAuth2PasswordBearer` sınıfının bir örneğini oluşturduğumuzda `tokenUrl` parametresini geçiyoruz. Bu parametre, istemcinin (kullanıcının tarayıcısında çalışan frontend) bir token almak için `username` ve `password`'ü göndermek için kullanacağı URL'yi içerir.

{* ../../docs_src/security/tutorial001_an_py39.py hl[8] *}

/// tip

Burada `tokenUrl="token"`, henüz oluşturmadığımız göreceli bir `token` URL'sine atıfta bulunur. Göreceli bir URL olduğu için, `./token`'a eşdeğerdir.

Göreceli bir URL kullandığımız için, API'niz `https://example.com/` adresindeyse, `https://example.com/token` adresine atıfta bulunacaktır. Ancak API'niz `https://example.com/api/v1/` adresindeyse, `https://example.com/api/v1/token` adresine atıfta bulunacaktır.

Göreceli URL kullanmak, uygulamanızın [Proxy Arkasında](../../advanced/behind-a-proxy.md){.internal-link target=_blank} gibi gelişmiş bir kullanım durumunda bile çalışmaya devam etmesini sağlamak için önemlidir.

///

Bu parametre o uç noktayı / *yol operasyonunu* oluşturmaz, ancak `/token` URL'sinin istemcinin tokeni almak için kullanması gereken URL olduğunu bildirir. Bu bilgi OpenAPI'de ve ardından etkileşimli API belge sistemlerinde kullanılır.

Yakında gerçek yol operasyonunu da oluşturacağız.

/// info

Çok katı bir "Pythonista" iseniz, `token_url` yerine `tokenUrl` parametre adı stilini beğenmeyebilirsiniz.

Bunun nedeni, OpenAPI spesifikasyonuyla aynı adı kullanmasıdır. Böylece bu güvenlik şemalarından herhangi biri hakkında daha fazla araştırma yapmanız gerekirse, hakkında daha fazla bilgi bulmak için kopyalayıp yapıştırabilirsiniz.

///

`oauth2_scheme` değişkeni, `OAuth2PasswordBearer`'ın bir örneğidir, ancak aynı zamanda "çağrılabilir"dir.

Şu şekilde çağrılabilir:

```Python
oauth2_scheme(some, parameters)
```

Bu yüzden, `Depends` ile kullanılabilir.

### Kullanın

Şimdi bu `oauth2_scheme`'yi `Depends` ile bir bağımlılıkta iletebilirsiniz.

{* ../../docs_src/security/tutorial001_an_py39.py hl[12] *}

Bu bağımlılık, *yol operasyonu fonksiyonunun* `token` parametresine atanan bir `str` sağlayacaktır.

**FastAPI**, OpenAPI şemasında (ve otomatik API belgelerinde) bir "güvenlik şeması" tanımlamak için bu bağımlılığı kullanabileceğini bilecektir.

/// info | Teknik Detaylar

**FastAPI**, güvenlik şemasını OpenAPI'de tanımlamak için `OAuth2PasswordBearer` sınıfını (bir bağımlılıkta bildirilmiş) kullanabileceğini bilecektir çünkü `fastapi.security.oauth2.OAuth2`'den miras alır, bu da `fastapi.security.base.SecurityBase`'den miras alır.

OpenAPI ile entegre olan (ve otomatik API belgeleri) tüm güvenlik yardımcı araçları `SecurityBase`'den miras alır, **FastAPI**'nin bunları OpenAPI'ye nasıl entegre edeceğini bilmesini sağlayan şey budur.

///

## Ne yapar

İstekte o `Authorization` başlığını arayacak, değerin `Bearer ` artı bir token olup olmadığını kontrol edecek ve tokeni `str` olarak döndürecektir.

Bir `Authorization` başlığı görmezse veya değerde bir `Bearer ` tokeni yoksa, doğrudan 401 durum kodu hatası (`UNAUTHORIZED`) ile yanıt verecektir.

Bir hata döndürmek için tokenin var olup olmadığını bile kontrol etmeniz gerekmez. Fonksiyonunuz çalıştırıldığında, o tokende bir `str` olacağından emin olabilirsiniz.

Bunu zaten etkileşimli belgelerde deneyebilirsiniz:

<img src="/img/tutorial/security/image03.png">

Tokenin geçerliliğini henüz doğrulamıyoruz, ama bu zaten bir başlangıç.

## Özet

Yani, sadece 3 veya 4 ekstra satırla, zaten ilkel bir güvenlik biçimine sahipsiniz.
