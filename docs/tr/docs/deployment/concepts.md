# Yayınlama Kavramları

Bir **FastAPI** uygulamasını veya aslında herhangi bir web API türünü yayınlarken, muhtemelen önem verdiğiniz birkaç kavram vardır ve bunları kullanarak **uygulamanızı yayınlamanın** **en uygun** yolunu bulabilirsiniz.

Önemli kavramlardan bazıları şunlardır:

* Güvenlik - HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* Replikasyon (çalışan süreç sayısı)
* Bellek
* Başlamadan önceki adımlar

Bunların **yayınlamaları** nasıl etkileyeceğini göreceğiz.

Sonuç olarak, nihai hedef **API istemcilerinize** **güvenli** bir şekilde hizmet edebilmek, **kesintileri önlemek** ve **hesaplama kaynaklarını** (örneğin uzak sunucular/sanal makineler) mümkün olduğunca verimli kullanmaktır. 🚀

Bu **kavramlar** hakkında burada biraz daha bilgi vereceğim ve bu, çok farklı ortamlarda, hatta gelecekte henüz var olmayan ortamlarda API'nizi yayınlama kararları vermeniz için gereken **sezgiyi** size verecektir.

Bu kavramları göz önünde bulundurarak, **kendi API'lerinizi** yayınlamanın en iyi yolunu **değerlendirebilir ve tasarlayabileceksiniz**.

Sonraki bölümlerde, FastAPI uygulamalarını yayınlamak için size daha fazla **somut tarifler** vereceğim.

Ama şimdilik, bu önemli **kavramsal fikirleri** kontrol edelim. Bu kavramlar diğer herhangi bir web API türü için de geçerlidir. 💡

## Güvenlik - HTTPS

[Önceki HTTPS hakkındaki bölümde](https.md){.internal-link target=_blank} HTTPS'nin API'niz için nasıl şifreleme sağladığını öğrendik.

Ayrıca HTTPS'nin normalde uygulama sunucunuzun **dışında** bir bileşen, bir **TLS Sonlandırma Proxy'si** tarafından sağlandığını gördük.

Ve sertifikaların aynı bileşen veya farklı bir bileşen olabilecek, **HTTPS sertifikalarını yenilemekle** sorumlu bir şeyin olması gerektiğini gördük.

### HTTPS İçin Örnek Araçlar

TLS Sonlandırma Proxy'si olarak kullanabileceğiniz araçlardan bazıları:

* Traefik
    * Otomatik olarak sertifika yenilemelerini yönetir ✨
* Caddy
    * Otomatik olarak sertifika yenilemelerini yönetir ✨
* Nginx
    * Sertifika yenilemeleri için Certbot gibi harici bir bileşenle
* HAProxy
    * Sertifika yenilemeleri için Certbot gibi harici bir bileşenle
* Nginx ile bir Ingress Controller'a sahip Kubernetes
    * Sertifika yenilemeleri için cert-manager gibi harici bir bileşenle
* Hizmetlerinin bir parçası olarak bir bulut sağlayıcı tarafından dahili olarak yönetilir (aşağıyı okuyun 👇)

Başka bir seçenek, HTTPS kurulumu da dahil olmak üzere işin çoğunu yapan bir **bulut hizmeti** kullanmaktır. Bazı kısıtlamaları olabilir veya size daha fazla ücretlendirebilir vb. Ama bu durumda, kendiniz bir TLS Sonlandırma Proxy'si kurmanız gerekmeyecektir.

Sonraki bölümlerde size bazı somut örnekler göstereceğim.

---

Sonra dikkate alınacak kavramlar, gerçek API'nizi çalıştıran programla (örn. Uvicorn) ilgili olan kavramlardır.

## Program ve Süreç

Çalışan "**süreç**" hakkında çok konuşacağız, bu yüzden ne anlama geldiği ve "**program**" kelimesiyle farkı hakkında netliğe sahip olmak yararlıdır.

### Program Nedir

**Program** kelimesi genellikle birçok şeyi tanımlamak için kullanılır:

* Yazdığınız **kod**, **Python dosyaları**.
* İşletim sistemi tarafından **çalıştırılabilen** **dosya**, örneğin: `python`, `python.exe` veya `uvicorn`.
* İşletim sisteminde **çalışırken** belirli bir program, CPU'yu kullanarak ve bellekte şeyler depolayarak. Bu aynı zamanda **süreç** olarak da adlandırılır.

### Süreç Nedir

**Süreç** kelimesi normalde daha spesifik bir şekilde kullanılır, yalnızca işletim sisteminde çalışan şeye atıfta bulunarak (yukarıdaki son nokta gibi):

* İşletim sisteminde **çalışan** belirli bir program.
    * Bu dosyaya veya koda atıfta bulunmaz, **özellikle** işletim sistemi tarafından **yürütülen** ve yönetilen şeye atıfta bulunur.
* Herhangi bir program, herhangi bir kod, **yalnızca yürütülürken şeyler yapabilir**. Bu yüzden, bir **çalışan süreç** olduğunda.
* Süreç siz veya işletim sistemi tarafından **sonlandırılabilir** (veya "öldürülebilir"). Bu noktada, çalışmayı/yürütülmeyi durdurur ve artık **şeyler yapamaz**.
* Bilgisayarınızda çalıştırdığınız her uygulamanın arkasında bir süreç vardır, çalışan her program, her pencere vb. Ve bir bilgisayar açıkken normalde birçok süreç **aynı anda** çalışır.
* **Aynı programın** **birden fazla süreci** aynı anda çalışabilir.

İşletim sisteminizde "görev yöneticisi" veya "sistem monitörü" (veya benzer araçlar) kontrol ederseniz, çalışan bu süreçlerin birçoğunu görebileceksiniz.

Ve örneğin, muhtemelen aynı tarayıcı programının (Firefox, Chrome, Edge vb.) birden fazla süreç çalıştırdığını göreceksiniz. Normalde sekme başına bir süreç çalıştırırlar, artı bazı ekstra süreçler.

<img class="shadow" src="/img/deployment/concepts/image01.png">

---

Şimdi **süreç** ve **program** terimleri arasındaki farkı bildiğimize göre, yayınlamalar hakkında konuşmaya devam edelim.

## Başlangıçta Çalıştırma

Çoğu durumda, bir web API oluşturduğunuzda, bunun **her zaman çalışır**, kesintisiz olmasını istersiniz, böylece istemcileriniz her zaman ona erişebilir. Bu elbette, yalnızca belirli durumlarda çalışmasını istemeniz için özel bir nedeniniz olmadığı sürece geçerlidir, ama çoğu zaman sürekli çalışmasını ve **erişilebilir** olmasını istersiniz.

### Uzak Bir Sunucuda

Bir uzak sunucu (bulut sunucusu, sanal makine vb.) kurduğunuzda, yapabileceğiniz en basit şey, yerel geliştirme yaparken yaptığınız gibi `fastapi run` (Uvicorn'u kullanan) veya benzeri bir şeyi manuel olarak kullanmaktır.

Ve çalışacak ve **geliştirme sırasında** yararlı olacaktır.

Ama sunucuyla bağlantınız kaybolursa, **çalışan süreç** muhtemelen ölecektir.

Ve sunucu yeniden başlatılırsa (örneğin güncellemelerden sonra veya bulut sağlayıcıdan geçişlerden sonra) muhtemelen **fark etmeyeceksiniz**. Ve bu nedenle, süreci manuel olarak yeniden başlatmanız gerektiğini bile bilmeyeceksiniz. Böylece, API'niz sadece ölü kalacaktır. 😱

### Başlangıçta Otomatik Çalıştırma

Genel olarak, sunucu programının (örn. Uvicorn) sunucu başlangıcında otomatik olarak başlatılmasını, **insan müdahalesi** gerektirmeden, API'nizle birlikte her zaman çalışan bir süreç olmasını isteyeceksiniz (örn. FastAPI uygulamanızı çalıştıran Uvicorn).

### Ayrı Program

Bunu başarmak için, normalde uygulamanızın başlangıçta çalıştırılmasını sağlayacak **ayrı bir programa** sahip olursunuz. Ve birçok durumda, diğer bileşenlerin veya uygulamaların da çalıştırılmasını sağlar, örneğin bir veritabanı.

### Başlangıçta Çalıştırmak İçin Örnek Araçlar

Bu işi yapabilen araçlardan bazı örnekler:

* Docker
* Kubernetes
* Docker Compose
* Swarm Modunda Docker
* Systemd
* Supervisor
* Hizmetlerinin bir parçası olarak bir bulut sağlayıcı tarafından dahili olarak yönetilir
* Diğerleri...

Sonraki bölümlerde size daha somut örnekler vereceğim.

## Yeniden Başlatmalar

Uygulamanızın başlangıçta çalıştırıldığından emin olmaya benzer şekilde, muhtemelen hatalardan sonra **yeniden başlatılmasını** da istersiniz.

### Hata Yaparız

Biz insanlar **hata yaparız**, her zaman. Yazılımda neredeyse her zaman farklı yerlerde gizli **hatalar** bulunur. 🐛

Ve biz geliştiriciler olarak bu hataları bulduğumuzda ve yeni özellikler uyguladığımızda kodu iyileştirmeye devam ederiz (muhtemelen yeni hatalar da ekleriz 😅).

### Otomatik Olarak Yönetilen Küçük Hatalar

FastAPI ile web API'leri oluştururken, kodumuzda bir hata varsa, FastAPI normalde onu hatayı tetikleyen tek istekle sınırlar. 🛡

İstemci o istek için bir **500 Internal Server Error** alacak, ama uygulama tamamen çökmek yerine sonraki istekler için çalışmaya devam edecektir.

### Daha Büyük Hatalar - Çökmeler

Yine de, **tüm uygulamayı çökerterek** Uvicorn'un ve Python'un çökmesine neden olan kod yazdığımız durumlar olabilir. 💥

Ve yine de, bir yerdeki hata nedeniyle uygulamanın ölü kalmasını muhtemelen istemezsiniz, muhtemelen bozuk olmayan *yol operasyonları* için en azından **çalışmaya devam etmesini** istersiniz.

### Çökmeden Sonra Yeniden Başlatma

Ama çalışan **süreci** çökerterek çok kötü hatalar olan durumlarda, süreci **yeniden başlatmakla** sorumlu harici bir bileşen isteyeceksiniz, en az birkaç kez...

/// tip

...Tüm uygulama sadece **anında çöküyorsa** muhtemelen onu sonsuza kadar yeniden başlatmaya devam etmenin bir anlamı yoktur. Ama bu durumlarda, muhtemelen geliştirme sırasında veya en azından yayınlamadan hemen sonra fark edeceksiniz.

Bu yüzden, gelecekte bazı belirli durumlarda **tamamen çökebileceği** ve yeniden başlatmanın hala mantıklı olduğu ana durumlara odaklanalım.

///

Muhtemelen uygulamanızı yeniden başlatmaktan sorumlu olan şeyin **harici bir bileşen** olmasını isteyeceksiniz, çünkü o noktada, Uvicorn ve Python ile aynı uygulama zaten çökmüştür, bu yüzden aynı uygulamanın aynı kodunda bununla ilgili yapabilecek hiçbir şey yoktur.

### Otomatik Yeniden Başlatma İçin Örnek Araçlar

Çoğu durumda, **programı başlangıçta çalıştırmak** için kullanılan aynı araç otomatik **yeniden başlatmaları** yönetmek için de kullanılır.

Örneğin, bu şunlar tarafından yönetilebilir:

* Docker
* Kubernetes
* Docker Compose
* Swarm Modunda Docker
* Systemd
* Supervisor
* Hizmetlerinin bir parçası olarak bir bulut sağlayıcı tarafından dahili olarak yönetilir
* Diğerleri...

## Replikasyon - Süreçler ve Bellek

Bir FastAPI uygulamasıyla, Uvicorn'u çalıştıran `fastapi` komutu gibi bir sunucu programı kullanarak, onu **tek bir süreçte** bir kez çalıştırmak birden fazla istemciye aynı anda hizmet verebilir.

Ama birçok durumda, aynı anda birkaç işçi süreci çalıştırmak isteyeceksiniz.

### Birden Fazla Süreç - İşçiler

Tek bir sürecin başa çıkabileceğinden daha fazla istemciniz varsa (örneğin sanal makine çok büyük değilse) ve sunucunun CPU'sunda **birden fazla çekirdeğiniz** varsa, aynı anda aynı uygulamayla çalışan **birden fazla sürece** sahip olabilir ve tüm istekleri aralarında dağıtabilirsiniz.

Aynı API programının **birden fazla sürecini** çalıştırdığınızda, bunlara genellikle **işçiler** denir.

### İşçi Süreçleri ve Portlar

[HTTPS Hakkında](https.md){.internal-link target=_blank} belgelerinden, bir sunucuda yalnızca bir sürecin bir port ve IP adresi kombinasyonunda dinleyebildiğini hatırlıyor musunuz?

Bu hala geçerlidir.

Bu yüzden, aynı anda **birden fazla sürece** sahip olmak için, bir portta dinleyen **tek bir sürecin** olması ve ardından iletişimi her işçi sürecine bir şekilde iletmesi gerekir.

### Süreç Başına Bellek

Şimdi, program belleğe şeyler yüklediğinde, örneğin bir makine öğrenimi modelini bir değişkende veya büyük bir dosyanın içeriğini bir değişkende, bunların hepsi sunucunun **biraz belleğini (RAM) tüketir**.

Ve birden fazla süreç normalde **hiçbir belleği paylaşmaz**. Bu, çalışan her sürecin kendi şeylerine, değişkenlerine ve belleğine sahip olduğu anlamına gelir. Ve kodunuzda büyük miktarda bellek tüketiyorsanız, **her süreç** eşdeğer miktarda bellek tüketecektir.

### Sunucu Belleği

Örneğin, kodunuz **1 GB boyutunda** bir Makine Öğrenimi modeli yüklüyorsa, API'nizle bir süreç çalıştırdığınızda en az 1 GB RAM tüketecektir. Ve **4 süreç** (4 işçi) başlatırsanız, her biri 1 GB RAM tüketecektir. Yani toplamda, API'niz **4 GB RAM** tüketecektir.

Ve uzak sunucunuz veya sanal makineniz yalnızca 3 GB RAM'e sahipse, 4 GB'dan fazla RAM yüklemeye çalışmak sorunlara neden olacaktır. 🚨

### Birden Fazla Süreç - Bir Örnek

Bu örnekte, iki **İşçi Sürecini** başlatan ve kontrol eden bir **Yönetici Süreci** vardır.

Bu Yönetici Süreci muhtemelen IP'deki **portta** dinleyen süreç olacaktır. Ve tüm iletişimi işçi süreçlerine iletecektir.

Bu işçi süreçleri uygulamanızı çalıştıran süreçler olacaktır, bir **isteği** almak ve bir **yanıt** döndürmek için ana hesaplamaları gerçekleştirecek ve RAM'de değişkenlere koyduğunuz her şeyi yükleyeceklerdir.

<img src="/img/deployment/concepts/process-ram.svg">

Ve elbette, aynı makinede uygulamanızın yanı sıra muhtemelen çalışan **başka süreçler** de olacaktır.

İlginç bir ayrıntı, her süreç tarafından kullanılan **CPU yüzdesinin** zaman içinde **çok değişebilmesi**, ama **belleğin (RAM)** normalde az çok **sabit** kalmasıdır.

Her seferinde benzer miktarda hesaplama yapan bir API'niz varsa ve çok sayıda istemciniz varsa, **CPU kullanımı** da muhtemelen *sabit olacaktır* (sürekli hızla yukarı aşağı gitmek yerine).

### Replikasyon Araçları ve Stratejileri Örnekleri

Bunu başarmak için birkaç yaklaşım olabilir ve sonraki bölümlerde, örneğin Docker ve konteynerler hakkında konuşurken size belirli stratejiler hakkında daha fazla bilgi vereceğim.

Dikkate alınacak ana kısıtlama, **genel IP'deki** **portu** yöneten **tek** bir bileşenin olması gerektiğidir. Ve ardından iletişimi replike edilmiş **süreçlere/işçilere** **iletmenin** bir yoluna sahip olması gerekir.

İşte olası kombinasyonlar ve stratejilerden bazıları:

* `--workers` ile **Uvicorn**
    * Bir Uvicorn **süreç yöneticisi** **IP** ve **portta** dinler ve **birden fazla Uvicorn işçi sürecini** başlatır.
* **Kubernetes** ve diğer dağıtık **konteyner sistemleri**
    * **Kubernetes** katmanındaki bir şey **IP** ve **portta** dinler. Replikasyon, her birinde **tek bir Uvicorn süreci** çalışan **birden fazla konteynere** sahip olmak şeklinde olur.
* Bu işi sizin için yapan **bulut hizmetleri**
    * Bulut hizmeti muhtemelen **replikasyonu sizin için yönetecektir**. Muhtemelen **çalıştırılacak bir süreç** veya kullanılacak bir **konteyner imajı** tanımlamanıza izin verir, her durumda, muhtemelen **tek bir Uvicorn süreci** olacaktır ve bulut hizmeti onu replike etmekle sorumlu olacaktır.

/// tip

**Konteynerler**, Docker veya Kubernetes hakkındaki bu maddelerden bazıları henüz çok anlamlı gelmiyorsa endişelenmeyin.

Konteyner imajları, Docker, Kubernetes vb. hakkında gelecek bir bölümde daha fazla bilgi vereceğim: [Konteynerlerde FastAPI - Docker](docker.md){.internal-link target=_blank}.

///

## Başlamadan Önceki Adımlar

Uygulamanızı **başlatmadan önce** bazı adımlar gerçekleştirmek istediğiniz birçok durum vardır.

Örneğin, **veritabanı geçişlerini** çalıştırmak isteyebilirsiniz.

Ama çoğu durumda, bu adımları yalnızca **bir kez** gerçekleştirmek isteyeceksiniz.

Bu yüzden, uygulamayı başlatmadan önce bu **önceki adımları** gerçekleştiren **tek bir sürece** sahip olmak isteyeceksiniz.

Ve eğer daha sonra uygulamanın kendisi için **birden fazla süreç** (birden fazla işçi) başlatsanız bile, bu önceki adımları çalıştıranın tek bir süreç olduğundan emin olmanız gerekir. Bu adımlar **birden fazla süreç** tarafından çalıştırılsaydı, işi **paralel olarak** çalıştırarak **çoğaltırlardı** ve adımlar veritabanı geçişi gibi hassas bir şeyse, birbirleriyle çakışmalara neden olabilirlerdi.

Elbette, önceki adımları birden çok kez çalıştırmanın sorun olmadığı durumlar da vardır, bu durumda yönetmek çok daha kolaydır.

/// tip

Ayrıca, kurulumunuza bağlı olarak, bazı durumlarda uygulamanızı başlatmadan önce **herhangi bir önceki adıma bile ihtiyacınız olmayabileceğini** aklınızda bulundurun.

Bu durumda, bunların hiçbiri hakkında endişelenmenize gerek kalmaz. 🤷

///

### Önceki Adımlar Stratejileri Örnekleri

Bu büyük ölçüde **sisteminizi yayınlama** şeklinize **bağlı olacaktır** ve muhtemelen programları başlatma, yeniden başlatmaları yönetme vb. şeklinizle bağlantılı olacaktır.

İşte bazı olası fikirler:

* Uygulama konteynerinizden önce çalışan Kubernetes'te bir "Init Container"
* Önceki adımları çalıştıran ve ardından uygulamanızı başlatan bir bash betiği
    * *O* bash betiğini başlatmanın/yeniden başlatmanın, hataları tespit etmenin vb. bir yoluna yine de ihtiyacınız olacaktır.

/// tip

Konteynerlerlbe bunu yapmak için size daha somut örnekler vereceğim gelecek bir bölümde: [Konteynerlerde FastAPI - Docker](docker.md){.internal-link target=_blank}.

///

## Kaynak Kullanımı

Sunucunuz(lar) bir **kaynaktır**, programlarınızla CPU'lardaki hesaplama süresini ve mevcut RAM belleğini tüketebilir veya **kullanabilirsiniz**.

Sistem kaynaklarının ne kadarını tüketmek/kullanmak istiyorsunuz? "Çok fazla değil" diye düşünmek kolay olabilir, ama gerçekte muhtemelen **çökmeden mümkün olduğunca fazla** tüketmek isteyeceksiniz.

3 sunucu için ödeme yapıyor ama RAM'lerinin ve CPU'larının yalnızca küçük bir kısmını kullanıyorsanız, muhtemelen **para israf ediyorsunuzdur** 💸 ve muhtemelen **sunucu elektrik gücünü israf ediyorsunuzdur** 🌎 vb.

Bu durumda, yalnızca 2 sunucuya sahip olmak ve kaynaklarının (CPU, bellek, disk, ağ bant genişliği vb.) daha yüksek bir yüzdesini kullanmak daha iyi olabilir.

Öte yandan, 2 sunucunuz varsa ve **CPU ve RAM'lerinin %100'ünü** kullanıyorsanız, bir noktada bir süreç daha fazla bellek isteyecek ve sunucu diski "bellek" olarak kullanmak zorunda kalacak (bu binlerce kat daha yavaş olabilir) veya hatta **çökecektir**. Veya bir sürecin bir hesaplama yapması gerekecek ve CPU tekrar serbest kalana kadar beklemek zorunda kalacaktır.

Bu durumda, **bir ekstra sunucu** almak ve üzerinde bazı süreçler çalıştırmak daha iyi olacaktır, böylece hepsi **yeterli RAM ve CPU zamanına** sahip olur.

Ayrıca bir nedenden ötürü API'nizin kullanımında bir **artış** olma ihtimali de vardır. Belki viral olmuştur veya belki başka hizmetler veya botlar onu kullanmaya başlamıştır. Ve bu durumlarda güvende olmak için ekstra kaynaklara sahip olmak isteyebilirsiniz.

Hedeflemek için **rastgele bir sayı** koyabilirsiniz, örneğin kaynak kullanımının **%50 ile %90** arasında bir şey. Mesele şu ki, bunlar muhtemelen ölçmek ve yayınlamalarınızı ayarlamak için kullanmak isteyeceğiniz ana şeylerdir.

Sunucunuzdaki CPU ve RAM kullanımını veya her süreç tarafından kullanılan miktarı görmek için `htop` gibi basit araçları kullanabilirsiniz. Veya sunucular arasında dağıtılmış olabilen daha karmaşık izleme araçlarını kullanabilirsiniz.

## Özet

Uygulamanızı nasıl yayınlayacağınıza karar verirken muhtemelen aklınızda tutmanız gereken ana kavramlardan bazılarını burada okuyordunuz:

* Güvenlik - HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* Replikasyon (çalışan süreç sayısı)
* Bellek
* Başlamadan önceki adımlar

Bu fikirleri anlamak ve nasıl uygulanacağını bilmek, yayınlamalarınızı yapılandırmak ve ayarlamak için gereken herhangi bir kararı vermek için gerekli sezgiyi size vermelidir. 🤓

Sonraki bölümlerde, takip edebileceğiniz olası stratejilerin daha somut örneklerini vereceğim. 🚀
