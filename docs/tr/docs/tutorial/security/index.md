# Güvenlik

Güvenlik, kimlik doğrulama ve yetkilendirmeyi ele almanın birçok yolu vardır.

Ve bu normalde karmaşık ve "zor" bir konudur.

Birçok framework ve sistemde güvenlik ve kimlik doğrulamayı ele almak büyük miktarda çaba ve kod gerektirir (birçok durumda yazılan tüm kodun %50'si veya daha fazlası olabilir).

**FastAPI**, tüm güvenlik spesifikasyonlarını öğrenmek ve incelemek zorunda kalmadan, standart bir şekilde, kolayca, hızlıca **Güvenlik** ile başa çıkmanıza yardımcı olacak çeşitli araçlar sağlar.

Ama önce, bazı küçük kavramları kontrol edelim.

## Aceleniz mi var?

Bu terimlerin hiçbirini umursamıyorsanız ve sadece *hemen şimdi* kullanıcı adı ve şifreye dayalı kimlik doğrulama ile güvenlik eklemeniz gerekiyorsa, sonraki bölümlere atlayın.

## OAuth2

OAuth2, kimlik doğrulama ve yetkilendirmeyi ele almanın çeşitli yollarını tanımlayan bir spesifikasyondur.

Oldukça kapsamlı bir spesifikasyondur ve birçok karmaşık kullanım durumunu kapsar.

Bir "üçüncü taraf" kullanarak kimlik doğrulama yollarını içerir.

"Facebook, Google, Twitter, GitHub ile giriş yap" kullanan tüm sistemlerin altta kullandığı şey budur.

### OAuth 1

OAuth2'den çok farklı olan ve iletişimin nasıl şifreleneceği hakkında doğrudan spesifikasyonlar içerdiğinden daha karmaşık olan bir OAuth 1 vardı.

Günümüzde çok popüler değildir veya kullanılmamaktadır.

OAuth2, iletişimin nasıl şifreleneceğini belirtmez, uygulamanızın HTTPS ile sunulmasını bekler.

/// tip

**Dağıtım** bölümünde, Traefik ve Let's Encrypt kullanarak ücretsiz HTTPS kurulumunu göreceksiniz.

///

## OpenID Connect

OpenID Connect, **OAuth2**'ye dayanan başka bir spesifikasyondur.

OAuth2'de nispeten belirsiz olan bazı şeyleri belirterek onu genişletir, daha birlikte çalışabilir hale getirmeye çalışır.

Örneğin, Google girişi OpenID Connect kullanır (altında OAuth2 kullanır).

Ancak Facebook girişi OpenID Connect'i desteklemez. Kendi OAuth2 varyasyonuna sahiptir.

### OpenID ("OpenID Connect" değil)

Bir de "OpenID" spesifikasyonu vardı. **OpenID Connect** ile aynı şeyi çözmeye çalışıyordu, ancak OAuth2'ye dayanmıyordu.

Bu yüzden, tamamen ek bir sistemdi.

Günümüzde çok popüler değildir veya kullanılmamaktadır.

## OpenAPI

OpenAPI (daha önce Swagger olarak biliniyordu), API'ler oluşturmak için açık spesifikasyondur (artık Linux Foundation'ın bir parçasıdır).

**FastAPI**, **OpenAPI**'ye dayanmaktadır.

Birden fazla otomatik etkileşimli belge arayüzü, kod üretimi vb.'ye sahip olmayı mümkün kılan şey budur.

OpenAPI'nin birden fazla güvenlik "şemasını" tanımlama yolu vardır.

Bunları kullanarak, bu etkileşimli belge sistemleri dahil, tüm bu standart tabanlı araçlardan yararlanabilirsiniz.

OpenAPI aşağıdaki güvenlik şemalarını tanımlar:

* `apiKey`: şunlardan gelebilen uygulamaya özgü bir anahtar:
    * Bir sorgu parametresi.
    * Bir başlık.
    * Bir çerez.
* `http`: standart HTTP kimlik doğrulama sistemleri, şunlar dahil:
    * `bearer`: bir `Authorization` başlığı, değeri `Bearer ` artı bir token. Bu, OAuth2'den miras alınmıştır.
    * HTTP Basic kimlik doğrulama.
    * HTTP Digest, vb.
* `oauth2`: güvenliği ele almanın tüm OAuth2 yolları ("akışlar" olarak adlandırılır).
    * Bu akışlardan birçoğu bir OAuth 2.0 kimlik doğrulama sağlayıcısı oluşturmak için uygundur (Google, Facebook, Twitter, GitHub vb. gibi):
        * `implicit`
        * `clientCredentials`
        * `authorizationCode`
    * Ancak aynı uygulamada doğrudan kimlik doğrulamayı ele almak için mükemmel şekilde kullanılabilecek belirli bir "akış" vardır:
        * `password`: sonraki bazı bölümler bunun örneklerini kapsayacaktır.
* `openIdConnect`: OAuth2 kimlik doğrulama verilerinin otomatik olarak nasıl keşfedileceğini tanımlama yolu vardır.
    * Bu otomatik keşif, OpenID Connect spesifikasyonunda tanımlanan şeydir.


/// tip

Google, Facebook, Twitter, GitHub vb. gibi diğer kimlik doğrulama/yetkilendirme sağlayıcılarını entegre etmek de mümkün ve nispeten kolaydır.

En karmaşık sorun, bunlar gibi bir kimlik doğrulama/yetkilendirme sağlayıcısı oluşturmaktır, ancak **FastAPI** size ağır yükü sizin için kaldırırken bunu kolayca yapmak için araçlar verir.

///

## **FastAPI** yardımcı araçları

FastAPI, bu güvenlik mekanizmalarını kullanmayı basitleştiren `fastapi.security` modülünde bu güvenlik şemalarının her biri için çeşitli araçlar sağlar.

Sonraki bölümlerde **FastAPI** tarafından sağlanan bu araçları kullanarak API'nize nasıl güvenlik ekleyeceğinizi göreceksiniz.

Ve ayrıca bunun etkileşimli belge sistemine nasıl otomatik olarak entegre olduğunu da göreceksiniz.
