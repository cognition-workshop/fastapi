# CORS (Çapraz Kaynak Paylaşımı)

<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS" class="external-link" target="_blank">CORS veya "Çapraz Kaynak Paylaşımı"</a>, bir tarayıcıda çalışan ön yüzün bir arka uçla iletişim kuran JavaScript koduna sahip olduğu ve arka ucun ön yüzden farklı bir "kaynak"ta olduğu durumları ifade eder.

## Kaynak

Bir kaynak, protokol (`http`, `https`), alan adı (`myapp.com`, `localhost`, `localhost.tiangolo.com`) ve port (`80`, `443`, `8080`) kombinasyonudur.

Yani, bunların hepsi farklı kaynaklardır:

* `http://localhost`
* `https://localhost`
* `http://localhost:8080`

Hepsi `localhost`'ta olsalar bile, farklı protokoller veya portlar kullandıkları için farklı "kaynaklar"dır.

## Adımlar

Diyelim ki `http://localhost:8080` adresinde bir tarayıcıda çalışan bir ön yüzünüz var ve JavaScript'i `http://localhost` adresinde çalışan bir arka uçla iletişim kurmaya çalışıyor (bir port belirtmediğimiz için tarayıcı varsayılan port olan `80`'i varsayacaktır).

Ardından, tarayıcı `:80`-arka ucuna bir HTTP `OPTIONS` isteği gönderecek ve eğer arka uç bu farklı kaynaktan (`http://localhost:8080`) iletişime izin veren uygun başlıkları gönderirse, `:8080`-tarayıcı ön yüzdeki JavaScript'in `:80`-arka ucuna isteğini göndermesine izin verecektir.

Bunu başarmak için, `:80`-arka ucunun bir "izin verilen kaynaklar" listesine sahip olması gerekir.

Bu durumda, `:8080`-ön yüzün doğru çalışması için listede `http://localhost:8080` bulunmalıdır.

## Joker karakterler

Listeyi `"*"` (bir "joker karakter") olarak bildirmek de mümkündür, bu da hepsine izin verildiğini söyler.

Ancak bu, yalnızca belirli iletişim türlerine izin verecek ve kimlik bilgilerini içeren her şeyi hariç tutacaktır: Çerezler, Bearer Token'larla kullanılanlar gibi Authorization başlıkları vb.

Bu yüzden her şeyin doğru çalışması için, izin verilen kaynakları açıkça belirtmek daha iyidir.

## `CORSMiddleware` kullanın

**FastAPI** uygulamanızda `CORSMiddleware` kullanarak yapılandırabilirsiniz.

* `CORSMiddleware`'i içe aktarın.
* İzin verilen kaynakların bir listesini (string olarak) oluşturun.
* Bunu **FastAPI** uygulamanıza bir "middleware" olarak ekleyin.

Ayrıca arka ucunuzun şunlara izin verip vermediğini belirtebilirsiniz:

* Kimlik bilgileri (Authorization başlıkları, Çerezler vb.).
* Belirli HTTP yöntemleri (`POST`, `PUT`) veya joker karakter `"*"` ile hepsi.
* Belirli HTTP başlıkları veya joker karakter `"*"` ile hepsi.

{* ../../docs_src/cors/tutorial001.py hl[2,6:11,13:19] *}


`CORSMiddleware` uygulaması tarafından kullanılan varsayılan parametreler varsayılan olarak kısıtlayıcıdır, bu yüzden tarayıcıların bunları Çapraz Alan bağlamında kullanmasına izin vermek için belirli kaynakları, yöntemleri veya başlıkları açıkça etkinleştirmeniz gerekecektir.

Aşağıdaki argümanlar desteklenir:

* `allow_origins` - Çapraz kaynak istekleri yapmaya izin verilmesi gereken kaynakların listesi. Örn. `['https://example.org', 'https://www.example.org']`. Herhangi bir kaynağa izin vermek için `['*']` kullanabilirsiniz.
* `allow_origin_regex` - Çapraz kaynak istekleri yapmaya izin verilmesi gereken kaynaklarla eşleşecek bir regex dizesi. Örn. `'https://.*\.example\.org'`.
* `allow_methods` - Çapraz kaynak istekleri için izin verilmesi gereken HTTP yöntemlerinin listesi. Varsayılan `['GET']`'dir. Tüm standart yöntemlere izin vermek için `['*']` kullanabilirsiniz.
* `allow_headers` - Çapraz kaynak istekleri için desteklenmesi gereken HTTP istek başlıklarının listesi. Varsayılan `[]`'dir. Tüm başlıklara izin vermek için `['*']` kullanabilirsiniz. `Accept`, `Accept-Language`, `Content-Language` ve `Content-Type` başlıkları <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests" class="external-link" rel="noopener" target="_blank">basit CORS istekleri</a> için her zaman izin verilir.
* `allow_credentials` - Çapraz kaynak istekleri için çerezlerin desteklenmesi gerektiğini belirtir. Varsayılan `False`'tur. Ayrıca, kimlik bilgilerine izin verilmesi için `allow_origins` `['*']` olarak ayarlanamaz, kaynaklar belirtilmelidir.
* `expose_headers` - Tarayıcıya erişilebilir olması gereken yanıt başlıklarını belirtir. Varsayılan `[]`'dir.
* `max_age` - Tarayıcıların CORS yanıtlarını önbelleğe alması için maksimum süreyi saniye cinsinden ayarlar. Varsayılan `600`'dür.

Middleware, iki özel HTTP istek türüne yanıt verir...

### CORS ön kontrol istekleri

Bunlar `Origin` ve `Access-Control-Request-Method` başlıklarına sahip herhangi bir `OPTIONS` isteğidir.

Bu durumda middleware, gelen isteği yakalayacak ve bilgilendirme amacıyla uygun CORS başlıklarıyla birlikte bir `200` veya `400` yanıtı ile yanıt verecektir.

### Basit istekler

`Origin` başlığına sahip herhangi bir istek. Bu durumda middleware, isteği normal şekilde geçirecek, ancak yanıta uygun CORS başlıklarını ekleyecektir.

## Daha fazla bilgi

<abbr title="Çapraz Kaynak Paylaşımı">CORS</abbr> hakkında daha fazla bilgi için <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS" class="external-link" target="_blank">Mozilla CORS belgelerine</a> bakın.

/// note | Teknik Detaylar

`from starlette.middleware.cors import CORSMiddleware` da kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin kolaylığınız için `fastapi.middleware` içinde birkaç middleware sağlar. Ancak mevcut middleware'lerin çoğu doğrudan Starlette'ten gelir.

///
