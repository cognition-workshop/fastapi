# OAuth2 kapsamları

OAuth2 kapsamlarını doğrudan **FastAPI** ile kullanabilirsiniz, sorunsuz çalışacak şekilde entegre edilmişlerdir.

Bu, OAuth2 standardını takip eden, OpenAPI uygulamanıza (ve API belgelerine) entegre edilmiş daha ayrıntılı bir izin sistemine sahip olmanızı sağlar.

Kapsamlı OAuth2, Facebook, Google, GitHub, Microsoft, Twitter vb. gibi birçok büyük kimlik doğrulama sağlayıcısı tarafından kullanılan mekanizmadır. Bunu, kullanıcılara ve uygulamalara belirli izinler sağlamak için kullanırlar.

Facebook, Google, GitHub, Microsoft, Twitter ile her "giriş yaptığınızda", o uygulama kapsamlı OAuth2 kullanmaktadır.

Bu bölümde, **FastAPI** uygulamanızda aynı kapsamlı OAuth2 ile kimlik doğrulama ve yetkilendirmeyi nasıl yöneteceğinizi göreceksiniz.

/// warning

Bu az çok ileri düzey bir bölümdür. Yeni başlıyorsanız, atlayabilirsiniz.

OAuth2 kapsamlarına mutlaka ihtiyacınız yoktur ve kimlik doğrulama ile yetkilendirmeyi istediğiniz şekilde yönetebilirsiniz.

Ama kapsamlı OAuth2, API'nize (OpenAPI ile) ve API belgelerinize güzelce entegre edilebilir.

Yine de, bu kapsamları veya diğer güvenlik/yetkilendirme gereksinimlerini kodunuzda ihtiyacınız olan şekilde uygularsınız.

Birçok durumda, kapsamlı OAuth2 gereğinden fazla olabilir.

Ama ihtiyacınız olduğunu biliyorsanız veya merak ediyorsanız, okumaya devam edin.

///

## OAuth2 kapsamları ve OpenAPI

OAuth2 spesifikasyonu "kapsamları" boşluklarla ayrılmış dizelerin bir listesi olarak tanımlar.

Bu dizelerin her birinin içeriği herhangi bir biçimde olabilir, ancak boşluk içermemelidir.

Bu kapsamlar "izinleri" temsil eder.

OpenAPI'de (örneğin API belgelerinde) "güvenlik şemaları" tanımlayabilirsiniz.

Bu güvenlik şemalarından biri OAuth2 kullanıyorsa, kapsamları da bildirebilir ve kullanabilirsiniz.

Her "kapsam" sadece bir dizedir (boşluksuz).

Normalde belirli güvenlik izinlerini bildirmek için kullanılırlar, örneğin:

* `users:read` veya `users:write` yaygın örneklerdir.
* `instagram_basic` Facebook / Instagram tarafından kullanılır.
* `https://www.googleapis.com/auth/drive` Google tarafından kullanılır.

/// info

OAuth2'de bir "kapsam", belirli bir gerekli izni bildiren sadece bir dizedir.

`:` gibi başka karakterler içerip içermediği veya bir URL olup olmadığı önemli değildir.

Bu ayrıntılar uygulamaya özgüdür.

OAuth2 için bunlar sadece dizelerdir.

///

## Genel bakış

Önce, [Parola (ve hashleme) ile OAuth2, JWT token'lı Bearer](../../tutorial/security/oauth2-jwt.md){.internal-link target=_blank} ana **Öğretici - Kullanıcı Kılavuzu**'ndaki örneklerden değişen kısımları hızlıca görelim. Şimdi OAuth2 kapsamlarını kullanarak:

{* ../../docs_src/security/tutorial005_an_py310.py hl[5,9,13,47,65,106,108:116,122:125,129:135,140,156] *}

Şimdi bu değişiklikleri adım adım inceleyelim.

## OAuth2 Güvenlik şeması

İlk değişiklik, şimdi OAuth2 güvenlik şemasını iki mevcut kapsamla, `me` ve `items`, bildirmemizdir.

`scopes` parametresi, her kapsamı anahtar ve açıklamayı değer olarak içeren bir `dict` alır:

{* ../../docs_src/security/tutorial005_an_py310.py hl[63:66] *}

Şimdi bu kapsamları bildirdiğimiz için, giriş yaptığınızda/yetkilendirdiğinizde API belgelerinde görüneceklerdir.

Ve hangi kapsamlara erişim vermek istediğinizi seçebilirsiniz: `me` ve `items`.

Bu, Facebook, Google, GitHub vb. ile giriş yaparken izin verdiğinizde kullanılan aynı mekanizmadır:

<img src="/img/tutorial/security/image11.png">

## Kapsamlı JWT token

Şimdi, istenen kapsamları döndürmek için token *yol operasyonunu* değiştirin.

Hala aynı `OAuth2PasswordRequestForm`'u kullanıyoruz. İstekte aldığı her kapsamla birlikte `str`'lerden oluşan bir `list` içeren `scopes` özelliğini içerir.

Ve kapsamları JWT token'ının bir parçası olarak döndürüyoruz.

/// danger

Basitlik için, burada alınan kapsamları doğrudan token'a ekliyoruz.

Ama uygulamanızda, güvenlik açısından, yalnızca kullanıcının gerçekten sahip olabileceği kapsamları veya önceden tanımladığınız kapsamları eklediğinizden emin olmalısınız.

///

{* ../../docs_src/security/tutorial005_an_py310.py hl[156] *}

## *Yol operasyonlarında* ve bağımlılıklarda kapsamları bildirme

Şimdi `/users/me/items/` *yol operasyonunun* `items` kapsamını gerektirdiğini bildiriyoruz.

Bunun için `fastapi`'den `Security`'yi içe aktarıp kullanıyoruz.

`Security`'yi bağımlılıkları bildirmek için kullanabilirsiniz (tıpkı `Depends` gibi), ama `Security` ayrıca kapsamların (dizelerin) bir listesiyle bir `scopes` parametresi alır.

Bu durumda, `Security`'ye bir bağımlılık fonksiyonu `get_current_active_user` geçiriyoruz (`Depends` ile yapacağımız gibi).

Ama ayrıca bir `list` kapsam da geçiriyoruz, bu durumda tek bir kapsamla: `items` (daha fazla olabilir).

Ve `get_current_active_user` bağımlılık fonksiyonu da yalnızca `Depends` ile değil `Security` ile de alt bağımlılıklar bildirebilir. Kendi alt bağımlılık fonksiyonunu (`get_current_user`) ve daha fazla kapsam gereksinimi bildirerek.

Bu durumda, `me` kapsamını gerektirir (birden fazla kapsam gerektirebilir).

/// note

Farklı yerlere farklı kapsamlar eklemeniz gerekmez.

Bunu burada **FastAPI**'nin farklı seviyelerde bildirilen kapsamları nasıl ele aldığını göstermek için yapıyoruz.

///

{* ../../docs_src/security/tutorial005_an_py310.py hl[5,140,171] *}

/// info | Teknik Detaylar

`Security` aslında `Depends`'in bir alt sınıfıdır ve sonra göreceğimiz yalnızca bir ekstra parametresi vardır.

Ama `Depends` yerine `Security` kullanarak, **FastAPI** güvenlik kapsamlarını bildirebileceğini, dahili olarak kullanabileceğini ve API'yi OpenAPI ile belgeleyebileceğini bilecektir.

Ama `fastapi`'den `Query`, `Path`, `Depends`, `Security` ve diğerlerini içe aktardığınızda, bunlar aslında özel sınıflar döndüren fonksiyonlardır.

///

## `SecurityScopes` kullanma

Şimdi `get_current_user` bağımlılığını güncelleyin.

Yukarıdaki bağımlılıklar tarafından kullanılan budur.

Burada daha önce oluşturduğumuz aynı OAuth2 şemasını kullanıyoruz, onu bir bağımlılık olarak bildiriyoruz: `oauth2_scheme`.

Bu bağımlılık fonksiyonunun kendisi herhangi bir kapsam gereksinimine sahip olmadığından, güvenlik kapsamları belirtmemiz gerekmediğinde `Security` yerine `Depends` ile `oauth2_scheme`'i kullanabiliriz.

Ayrıca `fastapi.security`'den içe aktarılan `SecurityScopes` türünde özel bir parametre bildiriyoruz.

Bu `SecurityScopes` sınıfı `Request`'e benzer (`Request` istek nesnesini doğrudan almak için kullanılıyordu).

{* ../../docs_src/security/tutorial005_an_py310.py hl[9,106] *}

## `scopes`'u kullanma

`security_scopes` parametresi `SecurityScopes` türünde olacaktır.

Kendisi ve bu bağımlılığı alt bağımlılık olarak kullanan tüm bağımlılıklar tarafından gereken tüm kapsamları içeren bir listeyle bir `scopes` özelliğine sahip olacaktır. Yani, tüm "bağımlılar"... bu kafa karıştırıcı gelebilir, aşağıda tekrar açıklanmaktadır.

`security_scopes` nesnesi (`SecurityScopes` sınıfından) ayrıca bu kapsamları boşluklarla ayrılmış tek bir dize içeren bir `scope_str` özniteliği sağlar (bunu kullanacağız).

Daha sonra birkaç noktada yeniden kullanabileceğimiz (`raise`) bir `HTTPException` oluşturuyoruz.

Bu istisnada, gerekli kapsamları (varsa) boşluklarla ayrılmış bir dize olarak (`scope_str` kullanarak) dahil ediyoruz. Bu kapsamları içeren dizeyi `WWW-Authenticate` başlığına koyuyoruz (bu spesifikasyonun bir parçasıdır).

{* ../../docs_src/security/tutorial005_an_py310.py hl[106,108:116] *}

## `username` ve veri şeklini doğrulama

Bir `username` aldığımızı doğruluyor ve kapsamları çıkarıyoruz.

Ve ardından verileri Pydantic modeliyle doğruluyoruz (`ValidationError` istisnasını yakalayarak) ve JWT token'ını okurken veya verileri Pydantic ile doğrularken bir hata alırsak, daha önce oluşturduğumuz `HTTPException`'ı yükseltiyoruz.

Bunun için, Pydantic modeli `TokenData`'yı yeni bir `scopes` özelliğiyle güncelliyoruz.

Verileri Pydantic ile doğrulayarak, örneğin kapsamlarla birlikte tam olarak bir `str` `list`'i ve `username` ile bir `str`'ye sahip olduğumuzdan emin olabiliriz.

Örneğin, bir `dict` veya başka bir şey yerine, çünkü bu uygulamayı daha sonraki bir noktada bozabilir ve güvenlik riski oluşturabilir.

Ayrıca o kullanıcı adına sahip bir kullanıcımız olduğunu doğruluyoruz ve yoksa, daha önce oluşturduğumuz aynı istisnayı yükseltiyoruz.

{* ../../docs_src/security/tutorial005_an_py310.py hl[47,117:128] *}

## `scopes`'u doğrulama

Şimdi bu bağımlılık ve tüm bağımlılar (*yol operasyonları* dahil) tarafından gereken tüm kapsamların, alınan token'da sağlanan kapsamlara dahil olduğunu doğruluyoruz, aksi takdirde bir `HTTPException` yükseltiyoruz.

Bunun için, tüm bu kapsamları `str` olarak içeren bir `list` içeren `security_scopes.scopes`'u kullanıyoruz.

{* ../../docs_src/security/tutorial005_an_py310.py hl[129:135] *}

## Bağımlılık ağacı ve kapsamlar

Bu bağımlılık ağacını ve kapsamları tekrar inceleyelim.

`get_current_active_user` bağımlılığı `get_current_user` üzerinde bir alt bağımlılığa sahip olduğundan, `get_current_active_user`'da bildirilen `"me"` kapsamı, `get_current_user`'a iletilen `security_scopes.scopes` içindeki gerekli kapsamlar listesine dahil edilecektir.

*Yol operasyonunun* kendisi de bir kapsam bildirir, `"items"`, bu yüzden bu da `get_current_user`'a iletilen `security_scopes.scopes` listesinde olacaktır.

İşte bağımlılıkların ve kapsamların hiyerarşisi şöyle görünür:

* *Yol operasyonu* `read_own_items`:
    * Gerekli kapsamlar `["items"]` bağımlılıkla:
    * `get_current_active_user`:
        * `get_current_active_user` bağımlılık fonksiyonu:
            * Gerekli kapsamlar `["me"]` bağımlılıkla:
            * `get_current_user`:
                * `get_current_user` bağımlılık fonksiyonu:
                    * Kendisi tarafından gerekli kapsam yok.
                    * `oauth2_scheme` kullanan bir bağımlılık.
                    * `SecurityScopes` türünde bir `security_scopes` parametresi:
                        * Bu `security_scopes` parametresinin, yukarıda bildirilen tüm bu kapsamları içeren bir `list` ile `scopes` özelliği vardır, yani:
                            * `security_scopes.scopes`, *yol operasyonu* `read_own_items` için `["me", "items"]` içerecektir.
                            * `security_scopes.scopes`, `get_current_active_user` bağımlılığında bildirildiği için *yol operasyonu* `read_users_me` için `["me"]` içerecektir.
                            * `security_scopes.scopes`, herhangi bir `scopes` ile `Security` bildirmediği ve bağımlılığı `get_current_user` da herhangi bir `scopes` bildirmediği için *yol operasyonu* `read_system_status` için `[]` (hiçbir şey) içerecektir.

/// tip

Buradaki önemli ve "sihirli" şey, `get_current_user`'ın her *yol operasyonu* için kontrol edilecek farklı bir `scopes` listesine sahip olacağıdır.

Hepsi, her *yol operasyonunda* ve o belirli *yol operasyonu* için bağımlılık ağacındaki her bağımlılıkta bildirilen `scopes`'a bağlıdır.

///

## `SecurityScopes` hakkında daha fazla ayrıntı

`SecurityScopes`'u herhangi bir noktada ve birden fazla yerde kullanabilirsiniz, "kök" bağımlılıkta olmak zorunda değildir.

Her zaman geçerli `Security` bağımlılıklarında ve **o belirli** *yol operasyonu* ve **o belirli** bağımlılık ağacı için tüm bağımlılarda bildirilen güvenlik kapsamlarına sahip olacaktır.

`SecurityScopes` bağımlılar tarafından bildirilen tüm kapsamlara sahip olacağından, bunu merkezi bir bağımlılık fonksiyonunda bir token'ın gerekli kapsamlara sahip olduğunu doğrulamak için kullanabilir ve ardından farklı *yol operasyonlarında* farklı kapsam gereksinimleri bildirebilirsiniz.

Her *yol operasyonu* için bağımsız olarak kontrol edileceklerdir.

## Kontrol edin

API belgelerini açarsanız, kimlik doğrulaması yapabilir ve hangi kapsamları yetkilendirmek istediğinizi belirleyebilirsiniz.

<img src="/img/tutorial/security/image11.png">

Herhangi bir kapsam seçmezseniz, "kimliğiniz doğrulanmış" olacaksınız, ama `/users/me/` veya `/users/me/items/`'a erişmeye çalıştığınızda yeterli izniniz olmadığını söyleyen bir hata alacaksınız. Yine de `/status/`'a erişebileceksiniz.

Ve `me` kapsamını seçip `items` kapsamını seçmezseniz, `/users/me/`'ye erişebilecek ama `/users/me/items/`'a erişemeyeceksiniz.

Üçüncü taraf bir uygulamanın, bir kullanıcı tarafından sağlanan bir token'la bu *yol operasyonlarından* birine erişmeye çalışması durumunda olan budur, kullanıcının uygulamaya ne kadar izin verdiğine bağlı olarak.

## Üçüncü taraf entegrasyonları hakkında

Bu örnekte OAuth2 "parola" akışını kullanıyoruz.

Bu, muhtemelen kendi frontend'imizle kendi uygulamamıza giriş yaparken uygundur.

Çünkü onu kontrol ettiğimiz için `username` ve `password`'ü alması konusunda güvenebiliriz.

Ama başkalarının bağlanacağı bir OAuth2 uygulaması oluşturuyorsanız (yani Facebook, Google, GitHub vb.'ye eşdeğer bir kimlik doğrulama sağlayıcısı oluşturuyorsanız) diğer akışlardan birini kullanmalısınız.

En yaygın olanı örtük akıştır.

En güvenli olanı kod akışıdır, ama daha fazla adım gerektirdiği için uygulaması daha karmaşıktır. Daha karmaşık olduğundan, birçok sağlayıcı örtük akışı önermektedir.

/// note

Her kimlik doğrulama sağlayıcısının akışlarını markalarının bir parçası yapmak için farklı şekilde adlandırması yaygındır.

Ama sonunda, aynı OAuth2 standardını uyguluyorlar.

///

**FastAPI**, `fastapi.security.oauth2`'de tüm bu OAuth2 kimlik doğrulama akışları için yardımcı araçlar içerir.

## Dekoratör `dependencies`'de `Security`

Dekoratörün `dependencies` parametresinde bir `Depends` `list`'i tanımlayabildiğiniz gibi ([Yol operasyonu dekoratörlerindeki bağımlılıklar](../../tutorial/dependencies/dependencies-in-path-operation-decorators.md){.internal-link target=_blank}'da açıklandığı gibi), orada `scopes` ile `Security`'yi de kullanabilirsiniz.
