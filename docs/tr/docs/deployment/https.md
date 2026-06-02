# HTTPS Hakkında

HTTPS'nin sadece "etkinleştirilen" veya etkinleştirilmeyen bir şey olduğunu varsaymak kolaydır.

Ama bundan çok daha karmaşıktır.

/// tip

Aceleniz varsa veya umursamıyorsanız, farklı tekniklerle her şeyi kurmak için adım adım talimatlar içeren sonraki bölümlerle devam edin.

///

**HTTPS'nin temellerini** tüketici perspektifinden öğrenmek için <a href="https://howhttps.works/" class="external-link" target="_blank">https://howhttps.works/</a>'a göz atın.

Şimdi, bir **geliştirici perspektifinden**, HTTPS hakkında düşünürken akılda tutulması gereken birkaç şey:

* HTTPS için, **sunucunun** üçüncü bir taraf tarafından oluşturulmuş **"sertifikalara" sahip olması** gerekir.
    * Bu sertifikalar aslında üçüncü taraftan **alınır**, "oluşturulmaz".
* Sertifikaların bir **ömrü** vardır.
    * **Süreleri dolar**.
    * Ve ardından **yenilenmesi**, üçüncü taraftan **tekrar alınması** gerekir.
* Bağlantının şifrelemesi **TCP seviyesinde** gerçekleşir.
    * Bu, **HTTP'nin altındaki** bir katmandır.
    * Yani, **sertifika ve şifreleme işlemi** **HTTP'den önce** yapılır.
* **TCP "alan adlarını" bilmez**. Yalnızca IP adreslerini bilir.
    * İstenen **belirli alan adının** bilgisi **HTTP verilerinde** bulunur.
* **HTTPS sertifikaları** **belirli bir alan adını** "sertifikalandırır", ama protokol ve şifreleme, hangi alan adıyla ilgilenildiği **bilinmeden** TCP seviyesinde gerçekleşir.
* **Varsayılan olarak**, bu, **IP adresi başına yalnızca bir HTTPS sertifikanıza** sahip olabileceğiniz anlamına gelir.
    * Sunucunuzun ne kadar büyük olduğu veya üzerindeki her uygulamanın ne kadar küçük olabileceği önemli değildir.
    * Ancak bunun bir **çözümü** vardır.
* **TLS** protokolünün (TCP seviyesinde, HTTP'den önce şifrelemeyi yöneten protokol) **<a href="https://en.wikipedia.org/wiki/Server_Name_Indication" class="external-link" target="_blank"><abbr title="Server Name Indication">SNI</abbr></a>** adında bir **uzantısı** vardır.
    * Bu SNI uzantısı, tek bir sunucunun (tek bir **IP adresine** sahip) **birden fazla HTTPS sertifikasına** sahip olmasına ve **birden fazla HTTPS alan adı/uygulamaya** hizmet vermesine olanak tanır.
    * Bunun çalışması için, sunucuda çalışan **tek** bir bileşenin (program) **genel IP adresinde** dinlemesi ve sunucudaki **tüm HTTPS sertifikalarına** sahip olması gerekir.
* Güvenli bir bağlantı elde edildikten **sonra**, iletişim protokolü hala **HTTP**'dir.
    * **HTTP protokolü** ile gönderilmelerine rağmen, içerikler **şifrelenmiştir**.

Sunucuda (makine, host vb.) **bir program/HTTP sunucusu** çalıştırarak **tüm HTTPS işlerini yönetmek** yaygın bir uygulamadır: **şifrelenmiş HTTPS isteklerini** almak, **şifresi çözülmüş HTTP isteklerini** aynı sunucuda çalışan gerçek HTTP uygulamasına (bu durumda **FastAPI** uygulamasına) göndermek, uygulamadan **HTTP yanıtını** almak, uygun **HTTPS sertifikasını** kullanarak **şifrelemek** ve **HTTPS** kullanarak istemciye geri göndermek. Bu sunucu genellikle **<a href="https://en.wikipedia.org/wiki/TLS_termination_proxy" class="external-link" target="_blank">TLS Sonlandırma Proxy'si</a>** olarak adlandırılır.

TLS Sonlandırma Proxy'si olarak kullanabileceğiniz bazı seçenekler:

* Traefik (sertifika yenilemelerini de yönetebilir)
* Caddy (sertifika yenilemelerini de yönetebilir)
* Nginx
* HAProxy

## Let's Encrypt

Let's Encrypt'ten önce, bu **HTTPS sertifikaları** güvenilir üçüncü taraflarca satılıyordu.

Bu sertifikalardan birini edinme süreci zahmetliydi, oldukça fazla evrak gerektiriyordu ve sertifikalar oldukça pahalıydı.

Ama sonra **<a href="https://letsencrypt.org/" class="external-link" target="_blank">Let's Encrypt</a>** oluşturuldu.

Linux Vakfı'nın bir projesidir. Otomatik bir şekilde **ücretsiz HTTPS sertifikaları** sağlar. Bu sertifikalar tüm standart kriptografik güvenliği kullanır ve kısa ömürlüdür (yaklaşık 3 ay), bu yüzden kısaltılmış ömürleri nedeniyle **güvenlik aslında daha iyidir**.

Alan adları güvenli bir şekilde doğrulanır ve sertifikalar otomatik olarak oluşturulur. Bu ayrıca bu sertifikaların yenilenmesinin otomatikleştirilmesine de olanak tanır.

Fikir, bu sertifikaların edinilmesini ve yenilenmesini otomatikleştirmektir, böylece **sonsuza kadar ücretsiz güvenli HTTPS**'ye sahip olabilirsiniz.

## Geliştiriciler İçin HTTPS

İşte bir HTTPS API'nin nasıl görünebileceğine dair bir örnek, adım adım, ağırlıklı olarak geliştiriciler için önemli fikirlere dikkat ederek.

### Alan Adı

Her şey muhtemelen bir **alan adı edinmenizle** başlardı. Ardından onu bir DNS sunucusunda (muhtemelen aynı bulut sağlayıcınız) yapılandırırsınız.

Muhtemelen bir bulut sunucusu (sanal makine) veya benzeri bir şey edinirsiniz ve <abbr title="Değişmeyen">sabit</abbr> bir **genel IP adresine** sahip olur.

DNS sunucularında, **alan adınızı** sunucunuzun genel **IP adresine** yönlendirmek için bir kayıt ("`A kaydı`") yapılandırırsınız.

Bunu muhtemelen yalnızca bir kez, her şeyi ilk kurarken yaparsınız.

/// tip

Bu Alan Adı kısmı HTTPS'den çok öncedir, ama her şey alan adına ve IP adresine bağlı olduğundan, burada bahsetmeye değer.

///

### DNS

Şimdi gerçek HTTPS kısımlarına odaklanalım.

İlk olarak, tarayıcı **DNS sunucularıyla** alan adı için **IP'nin ne olduğunu** kontrol eder, bu durumda `someapp.example.com`.

DNS sunucuları tarayıcıya belirli bir **IP adresini** kullanmasını söyler. Bu, DNS sunucularında yapılandırdığınız, sunucunuz tarafından kullanılan genel IP adresi olur.

<img src="/img/deployment/https/https01.svg">

### TLS El Sıkışması Başlangıcı

Tarayıcı daha sonra o IP adresiyle **port 443**'te (HTTPS portu) iletişim kurar.

İletişimin ilk kısmı, istemci ve sunucu arasındaki bağlantıyı kurmak ve kullanacakları kriptografik anahtarları belirlemek vb. içindir.

<img src="/img/deployment/https/https02.svg">

İstemci ve sunucu arasındaki TLS bağlantısını kurmak için bu etkileşime **TLS el sıkışması** denir.

### SNI Uzantılı TLS

Belirli bir **IP adresindeki** belirli bir **portta** yalnızca **tek bir süreç** dinleyebilir. Aynı IP adresinde diğer portlarda dinleyen başka süreçler olabilir, ama her IP adresi ve port kombinasyonu için yalnızca bir tane.

TLS (HTTPS) varsayılan olarak `443` portunu kullanır. Yani ihtiyacımız olan port budur.

Bu portta yalnızca bir süreç dinleyebildiğinden, bunu yapacak süreç **TLS Sonlandırma Proxy'si** olacaktır.

TLS Sonlandırma Proxy'si bir veya daha fazla **TLS sertifikasına** (HTTPS sertifikaları) erişime sahip olacaktır.

Yukarıda tartışılan **SNI uzantısını** kullanarak, TLS Sonlandırma Proxy'si mevcut TLS (HTTPS) sertifikalarından hangisini bu bağlantı için kullanması gerektiğini kontrol edecektir, istemcinin beklediği alan adıyla eşleşeni kullanarak.

Bu durumda, `someapp.example.com` için sertifikayı kullanacaktır.

<img src="/img/deployment/https/https03.svg">

İstemci, o TLS sertifikasını oluşturan varlığa zaten **güvenmektedir** (bu durumda Let's Encrypt, ama bunu daha sonra göreceğiz), bu yüzden sertifikanın geçerli olduğunu **doğrulayabilir**.

Ardından, sertifikayı kullanarak, istemci ve TLS Sonlandırma Proxy'si geri kalan **TCP iletişimini nasıl şifreleyeceklerine karar verirler**. Bu, **TLS El Sıkışması** kısmını tamamlar.

Bundan sonra, istemci ve sunucu **şifrelenmiş bir TCP bağlantısına** sahip olur, TLS'nin sağladığı budur. Ve ardından bu bağlantıyı gerçek **HTTP iletişimini** başlatmak için kullanabilirler.

**HTTPS** de budur, saf (şifrelenmemiş) bir TCP bağlantısı yerine **güvenli bir TLS bağlantısı** içindeki düz **HTTP**'dir.

/// tip

İletişimin şifrelemesinin HTTP seviyesinde değil, **TCP seviyesinde** gerçekleştiğine dikkat edin.

///

### HTTPS İsteği

Artık istemci ve sunucu (özellikle tarayıcı ve TLS Sonlandırma Proxy'si) **şifrelenmiş bir TCP bağlantısına** sahip olduğuna göre, **HTTP iletişimini** başlatabilirler.

İstemci bir **HTTPS isteği** gönderir. Bu sadece şifrelenmiş bir TLS bağlantısı üzerinden yapılan bir HTTP isteğidir.

<img src="/img/deployment/https/https04.svg">

### İsteğin Şifresini Çözme

TLS Sonlandırma Proxy'si, **isteğin şifresini çözmek** için anlaşılan şifrelemeyi kullanır ve **düz (şifresi çözülmüş) HTTP isteğini** uygulamayı çalıştıran sürece (örneğin FastAPI uygulamasını çalıştıran Uvicorn ile bir sürece) iletir.

<img src="/img/deployment/https/https05.svg">

### HTTP Yanıtı

Uygulama isteği işler ve TLS Sonlandırma Proxy'sine **düz (şifrelenmemiş) bir HTTP yanıtı** gönderir.

<img src="/img/deployment/https/https06.svg">

### HTTPS Yanıtı

TLS Sonlandırma Proxy'si daha sonra daha önce anlaşılan kriptografiyi kullanarak (bu `someapp.example.com` sertifikası ile başlayan) **yanıtı şifreler** ve tarayıcıya geri gönderir.

Ardından, tarayıcı yanıtın geçerli olduğunu ve doğru kriptografik anahtarla şifrelendiğini doğrular vb. **Yanıtın şifresini çözer** ve işler.

<img src="/img/deployment/https/https07.svg">

İstemci (tarayıcı), yanıtın doğru sunucudan geldiğini bilecektir çünkü daha önce **HTTPS sertifikasını** kullanarak üzerinde anlaştıkları kriptografiyi kullanmaktadır.

### Birden Fazla Uygulama

Aynı sunucuda (veya sunucularda), **birden fazla uygulama** olabilir, örneğin diğer API programları veya bir veritabanı.

Yalnızca bir süreç belirli IP ve portu (örneğimizde TLS Sonlandırma Proxy'si) yönetebilir ama diğer uygulamalar/süreçler de sunucuda çalışabilir, aynı **genel IP ve port kombinasyonunu** kullanmaya çalışmadıkları sürece.

<img src="/img/deployment/https/https08.svg">

Bu şekilde, TLS Sonlandırma Proxy'si **birden fazla alan adı** için, birden fazla uygulama için HTTPS'yi ve sertifikaları yönetebilir ve ardından her durumda istekleri doğru uygulamaya iletebilir.

### Sertifika Yenileme

Gelecekte bir noktada, her sertifikanın **süresi dolacaktır** (edinildikten yaklaşık 3 ay sonra).

Ve ardından, Let's Encrypt ile konuşarak sertifika(lar)ı yenileyecek başka bir program olacaktır (bazı durumlarda başka bir programdır, bazı durumlarda aynı TLS Sonlandırma Proxy'si olabilir).

<img src="/img/deployment/https/https.svg">

**TLS sertifikaları**, bir IP adresiyle değil, **bir alan adıyla** ilişkilendirilir.

Bu yüzden, sertifikaları yenilemek için, yenileme programının yetkili kuruma (Let's Encrypt) gerçekten o alan adını **"sahiplendiğini" ve kontrol ettiğini kanıtlaması** gerekir.

Bunu yapmak ve farklı uygulama ihtiyaçlarını karşılamak için bunu yapmanın birkaç yolu vardır. Bazı popüler yollar:

* **Bazı DNS kayıtlarını değiştirmek**.
    * Bunun için, yenileme programının DNS sağlayıcısının API'lerini desteklemesi gerekir, bu yüzden kullandığınız DNS sağlayıcısına bağlı olarak bu bir seçenek olabilir veya olmayabilir.
* **Alan adıyla ilişkili genel IP adresinde bir sunucu olarak çalışmak** (en azından sertifika edinme sürecinde).
    * Yukarıda söylediğimiz gibi, belirli bir IP ve portta yalnızca bir süreç dinleyebilir.
    * Bu, aynı TLS Sonlandırma Proxy'sinin sertifika yenileme sürecini de üstlenmesinin çok yararlı olmasının nedenlerinden biridir.
    * Aksi takdirde, TLS Sonlandırma Proxy'sini geçici olarak durdurmanız, sertifikaları edinmek için yenileme programını başlatmanız, ardından bunları TLS Sonlandırma Proxy'si ile yapılandırmanız ve sonra TLS Sonlandırma Proxy'sini yeniden başlatmanız gerekebilir. Bu ideal değildir, çünkü TLS Sonlandırma Proxy'si kapalı olduğu süre boyunca uygulama(larınız) kullanılamaz olacaktır.

Bu yenileme sürecinin tamamı, uygulama sunmaya devam ederken, HTTPS'yi yönetmek için TLS sertifikalarını doğrudan uygulama sunucusuyla (örn. Uvicorn) kullanmak yerine bir TLS Sonlandırma Proxy'si ile **ayrı bir sisteme** sahip olmak istemenizin ana nedenlerinden biridir.

## Özet

**HTTPS**'ye sahip olmak çok önemlidir ve çoğu durumda oldukça **kritiktir**. Bir geliştirici olarak HTTPS hakkında çaba göstermeniz gereken şeylerin çoğu, yalnızca **bu kavramları anlamak** ve nasıl çalıştıklarıdır.

Ama **geliştiriciler için HTTPS**'nin temel bilgilerini öğrendikten sonra, her şeyi basit bir şekilde yönetmenize yardımcı olacak farklı araçları kolayca birleştirebilir ve yapılandırabilirsiniz.

Sonraki bölümlerde, **FastAPI** uygulamaları için **HTTPS**'nin nasıl kurulacağına dair birkaç somut örnek göstereceğim. 🔒
