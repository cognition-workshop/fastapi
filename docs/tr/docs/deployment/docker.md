# Konteynerlerde FastAPI - Docker

FastAPI uygulamalarını yayınlarken yaygın bir yaklaşım **Linux konteyner imajı** oluşturmaktır. Normalde <a href="https://www.docker.com/" class="external-link" target="_blank">**Docker**</a> kullanılarak yapılır. Ardından o konteyner imajını birkaç olası yoldan biriyle yayınlayabilirsiniz.

Linux konteynerleri kullanmanın **güvenlik**, **tekrarlanabilirlik**, **basitlik** ve diğerleri dahil birçok avantajı vardır.

/// tip

Aceleniz varsa ve bunları zaten biliyorsanız? [`Dockerfile`'a aşağıdan atlayın 👇](#fastapi-icin-bir-docker-imaji-olusturma).

///

<details>
<summary>Dockerfile Önizlemesi 👀</summary>

```Dockerfile
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]
```

</details>

## Konteyner Nedir

Konteynerler (esas olarak Linux konteynerleri), uygulamaları tüm bağımlılıkları ve gerekli dosyalarıyla birlikte paketlemenin çok **hafif** bir yoludur, aynı sistemdeki diğer konteynerlerden (diğer uygulamalar veya bileşenler) izole tutulurken.

Linux konteynerleri, ana bilgisayarın (makine, sanal makine, bulut sunucusu vb.) aynı Linux çekirdeğini kullanarak çalışır. Bu, çok hafif olduklarını gösterir (tam işletim sistemi öykünmesi yapan sanal makinelere kıyasla).

Bu şekilde, konteynerler **az kaynak** tüketir, süreçleri doğrudan çalıştırmakla karşılaştırılabilir bir miktar (sanal makine çok daha fazla tüketir).

Konteynerlerin ayrıca kendi **izole** çalışan süreçleri (genellikle yalnızca tek bir süreç), dosya sistemi ve ağı vardır, bu da yayınlamayı, güvenliği, geliştirmeyi vb. basitleştirir.

## Konteyner İmajı Nedir

Bir **konteyner**, bir **konteyner imajından** çalıştırılır.

Konteyner imajı, bir konteynerde bulunması gereken tüm dosyaların, ortam değişkenlerinin ve varsayılan komutun/programın **statik** bir sürümüdür. Buradaki **Statik**, konteyner **imajının** çalışmadığı, yürütülmediği, yalnızca paketlenmiş dosyalar ve meta veriler olduğu anlamına gelir.

Depolanan statik içerikler olan "**konteyner imajı**"nın aksine, bir "**konteyner**" normalde çalışan örneğe, **yürütülen** şeye atıfta bulunur.

**Konteyner** başlatıldığında ve çalışırken (**konteyner imajından** başlatılır) dosyalar oluşturabilir veya değiştirebilir, ortam değişkenleri vb. Bu değişiklikler yalnızca o konteynerde var olacaktır, ama temel konteyner imajında kalıcı olmayacaktır (diske kaydedilmeyecektir).

Bir konteyner imajı **program** dosyası ve içeriklerine karşılaştırılabilir, örn. `python` ve bir `main.py` dosyası.

Ve **konteyner** (**konteyner imajının** aksine) imajın gerçek çalışan örneğidir, bir **sürece** karşılaştırılabilir. Aslında, bir konteyner yalnızca **çalışan bir süreci** olduğunda çalışır (ve normalde yalnızca tek bir süreçtir). Konteyner, içinde çalışan süreç olmadığında durur.

## Konteyner İmajları

Docker, **konteyner imajları** ve **konteynerler** oluşturma ve yönetme araçlarından başlıcası olmuştur.

Ve önceden yapılmış **resmi konteyner imajlarıyla** halka açık bir <a href="https://hub.docker.com/" class="external-link" target="_blank">Docker Hub</a> vardır, birçok araç, ortam, veritabanı ve uygulama için.

Örneğin, resmi bir <a href="https://hub.docker.com/_/python" class="external-link" target="_blank">Python İmajı</a> vardır.

Ve farklı şeyler için birçok başka imaj vardır, veritabanları için örneğin:

* <a href="https://hub.docker.com/_/postgres" class="external-link" target="_blank">PostgreSQL</a>
* <a href="https://hub.docker.com/_/mysql" class="external-link" target="_blank">MySQL</a>
* <a href="https://hub.docker.com/_/mongo" class="external-link" target="_blank">MongoDB</a>
* <a href="https://hub.docker.com/_/redis" class="external-link" target="_blank">Redis</a>, vb.

Önceden yapılmış bir konteyner imajı kullanarak farklı araçları **birleştirmek** ve kullanmak çok kolaydır. Örneğin, yeni bir veritabanını denemek için. Çoğu durumda, **resmi imajları** kullanabilir ve onları yalnızca ortam değişkenleriyle yapılandırabilirsiniz.

Bu şekilde, birçok durumda konteynerler ve Docker hakkında bilgi edinebilir ve bu bilgiyi birçok farklı araç ve bileşenle yeniden kullanabilirsiniz.

Bu yüzden, farklı şeylerle **birden fazla konteyner** çalıştırırsınız, bir veritabanı gibi, bir Python uygulaması, React frontend uygulaması olan bir web sunucusu gibi ve bunları dahili ağları aracılığıyla birbirine bağlarsınız.

Tüm konteyner yönetim sistemleri (Docker veya Kubernetes gibi) bu ağ özelliklerini entegre olarak sunar.

## Konteynerler ve Süreçler

Bir **konteyner imajı** normalde meta verilerinde **konteyner** başlatıldığında çalıştırılması gereken varsayılan programı veya komutu ve o programa iletilecek parametreleri içerir. Komut satırında olsaydı ne olacağına çok benzer.

Bir **konteyner** başlatıldığında, o komutu/programı çalıştıracaktır (ancak onu farklı bir komut/program çalıştırmaya geçersiz kılabilirsiniz).

Konteyner, **ana süreç** (komut veya program) çalıştığı sürece çalışır.

Bir konteynerin normalde **tek bir süreci** olur, ama ana süreçten alt süreçler başlatmak da mümkündür ve bu şekilde aynı konteynerde **birden fazla süreciniz** olur.

Ama **en az bir çalışan süreç** olmadan çalışan bir konteynere sahip olmak mümkün değildir. Ana süreç durursa, konteyner durur.

## FastAPI İçin Bir Docker İmajı Oluşturma

Tamam, şimdi bir şeyler oluşturalım! 🚀

**Resmi Python** imajına dayalı olarak, **sıfırdan** FastAPI için bir **Docker imajını** nasıl oluşturacağınızı göstereceğim.

Bu, **çoğu durumda** yapmak isteyeceğiniz şeydir, örneğin:

* **Kubernetes** veya benzeri araçlar kullanırken
* Bir **Raspberry Pi** üzerinde çalıştırırken
* Sizin için bir konteyner imajı çalıştıracak bir bulut hizmeti kullanırken vb.

### Paket Gereksinimleri

Uygulamanız için **paket gereksinimlerinizi** normalde bir dosyada bulundurursunuz.

Bu, o gereksinimleri **yüklemek** için kullandığınız araca bağlı olacaktır.

Bunu yapmanın en yaygın yolu, paket adlarını ve sürümlerini satır başına bir tane olacak şekilde bir `requirements.txt` dosyasına sahip olmaktır.

Sürüm aralıklarını ayarlamak için elbette [FastAPI sürümleri hakkında](versions.md){.internal-link target=_blank}'da okuduğunuz aynı fikirleri kullanırsınız.

Örneğin, `requirements.txt` dosyanız şöyle görünebilir:

```
fastapi[standard]>=0.113.0,<0.114.0
pydantic>=2.7.0,<3.0.0
```

Ve normalde bu paket bağımlılıklarını `pip` ile yüklersiniz, örneğin:

<div class="termy">

```console
$ pip install -r requirements.txt
---> 100%
Successfully installed fastapi pydantic
```

</div>

/// info

Paket bağımlılıklarını tanımlamak ve yüklemek için başka biçimler ve araçlar da vardır.

///

### **FastAPI** Kodunu Oluşturma

* Bir `app` dizini oluşturun ve içine girin.
* Boş bir `__init__.py` dosyası oluşturun.
* Bir `main.py` dosyası oluşturun:

```Python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

### Dockerfile

Şimdi aynı proje dizininde bir `Dockerfile` dosyası oluşturun:

```{ .dockerfile .annotate }
# (1)!
FROM python:3.9

# (2)!
WORKDIR /code

# (3)!
COPY ./requirements.txt /code/requirements.txt

# (4)!
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# (5)!
COPY ./app /code/app

# (6)!
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
```

1. Resmi Python temel imajından başlayın.

2. Geçerli çalışma dizinini `/code` olarak ayarlayın.

    `requirements.txt` dosyasını ve `app` dizinini buraya koyacağız.

3. Gereksinimleri içeren dosyayı `/code` dizinine kopyalayın.

    Önce **yalnızca** gereksinimleri içeren dosyayı kopyalayın, kodun geri kalanını değil.

    Bu dosya **sık değişmediğinden**, Docker bunu algılayacak ve bu adım için **önbelleği** kullanacak, sonraki adım için de önbelleği etkinleştirecektir.

4. Gereksinimler dosyasındaki paket bağımlılıklarını yükleyin.

    `--no-cache-dir` seçeneği `pip`'e indirilen paketleri yerel olarak kaydetmemesini söyler, çünkü bu yalnızca `pip` aynı paketleri yeniden yüklemek için tekrar çalıştırılacaksa geçerlidir, ama konteynerlerle çalışırken durum böyle değildir.

    /// note

    `--no-cache-dir` yalnızca `pip` ile ilgilidir, Docker veya konteynerlerle hiçbir ilgisi yoktur.

    ///

    `--upgrade` seçeneği `pip`'e paketleri zaten yüklüyse yükseltmesini söyler.

    Dosyayı kopyalayan önceki adım **Docker önbelleği** tarafından algılanabildiğinden, bu adım da mümkün olduğunda **Docker önbelleğini kullanacaktır**.

    Bu adımda önbelleği kullanmak, geliştirme sırasında imajı tekrar tekrar oluştururken, tüm bağımlılıkları **her seferinde** **indirip yüklemek** yerine size **çok fazla zaman** kazandıracaktır.

5. `./app` dizinini `/code` dizininin içine kopyalayın.

    Bu, **en sık değişen** tüm kodu içerdiğinden, Docker **önbelleği** bu veya sonraki **adımlar** için kolayca kullanılmayacaktır.

    Bu yüzden, konteyner imajı oluşturma sürelerini optimize etmek için bunu `Dockerfile`'ın **sonuna yakın** koymak önemlidir.

6. **Komutu** altında Uvicorn kullanan `fastapi run` kullanacak şekilde ayarlayın.

    `CMD` bir dizeler listesi alır, bu dizelerin her biri komut satırında boşluklarla ayırarak yazacağınız şeydir.

    Bu komut, yukarıda `WORKDIR /code` ile ayarladığınız aynı `/code` dizini olan **geçerli çalışma dizininden** çalıştırılacaktır.

/// tip

Koddaki her numara balonuna tıklayarak her satırın ne yaptığını gözden geçirin. 👆

///

/// warning

`CMD` talimatının her zaman aşağıda açıklandığı gibi **exec biçimini** kullandığınızdan emin olun.

///

#### `CMD` Kullanımı - Exec Biçimi

`CMD` Docker talimatı doğrudan yazılabilir (exec biçimi):

```Dockerfile
# ✅ Bunu yapın
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
```

Bazı Docker rehberleri bunu **kabuk biçiminde** yazmanızı gösterir:

```Dockerfile
# ⛔️ Bunu yapmayın
CMD "fastapi run app/main.py --port 80"
```

Onun yerine **exec biçimini** kullandığınızdan emin olun. 🤓

#### Dizin Yapısı

Artık şöyle bir dizin yapınız olmalı:

```
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt
```

#### Docker Önbelleği

Bu `Dockerfile`'da önemli bir püf noktası var, önce kodun geri kalanını değil, **yalnızca bağımlılıkları içeren dosyayı** kopyalıyoruz. Bunun nedenini anlatayım.

```Dockerfile
COPY ./requirements.txt /code/requirements.txt
```

Docker ve diğer araçlar bu konteyner imajlarını **artımlı olarak** oluşturur, `Dockerfile`'ın en üstünden başlayarak **bir katmanı diğerinin üstüne** ekler ve `Dockerfile`'ın her talimatı tarafından oluşturulan dosyaları ekler.

Docker ve benzeri araçlar ayrıca imajı oluştururken bir **dahili önbellek** kullanır, konteyner imajının son oluşturulmasından bu yana bir dosya değişmediyse, dosyayı tekrar kopyalayıp sıfırdan yeni bir katman oluşturmak yerine, en son oluşturulan **aynı katmanı yeniden kullanır**.

Sadece dosyaların kopyalanmasından kaçınmak işleri çok fazla iyileştirmeyebilir, ama o adım için önbelleği kullandığından, **sonraki adım için önbelleği kullanabilir**. Örneğin, bağımlılıkları yükleyen talimat için önbelleği kullanabilir:

```Dockerfile
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
```

Paket gereksinimleri dosyası **sık değişmez**. Bu yüzden, yalnızca o dosyayı kopyalayarak, Docker o adım için **önbelleği kullanabilecektir**.

Ve ardından, Docker o bağımlılıkları indirip yükleyen **sonraki adım için önbelleği kullanabilecektir**. Ve işte burada **çok zaman kazanırız**. ✨ ...ve sıkılmaktan kaçınırız. 😪😆

Paket bağımlılıklarını indirip yüklemek **dakikalar** sürebilir, ama **önbellek** kullanmak en fazla **saniyeler** sürer.

Ve geliştirme sırasında kod değişikliklerinizin çalışıp çalışmadığını kontrol etmek için konteyner imajını tekrar tekrar oluşturacağınız için, bunun kazandıracağı çok fazla birikmiş zaman vardır.

Ardından, `Dockerfile`'ın sonuna yakın bir yerde tüm kodu kopyalarız. Bu, **en sık değişen** şey olduğundan, onu sona yakın koyarız, çünkü neredeyse her zaman bundan sonraki herhangi bir şey önbelleği kolayca kullanamayacaktır.

```Dockerfile
COPY ./app /code/app
```

### Docker İmajını Oluşturma

Artık tüm dosyalar yerinde olduğuna göre, konteyner imajını oluşturalım.

* Proje dizinine gidin (`Dockerfile`'ınızın olduğu, `app` dizininizi içeren yere).
* FastAPI imajınızı oluşturun:

<div class="termy">

```console
$ docker build -t myimage .

---> 100%
```

</div>

/// tip

Sondaki `.`'ye dikkat edin, `./` ile eşdeğerdir, Docker'a konteyner imajını oluşturmak için kullanılacak dizini söyler.

Bu durumda, aynı geçerli dizindir (`.`).

///

### Docker Konteynerini Başlatma

* İmajınıza dayalı bir konteyner çalıştırın:

<div class="termy">

```console
$ docker run -d --name mycontainer -p 80:80 myimage
```

</div>

## Kontrol edin

Docker konteynerinizin URL'sinde kontrol edebilmeniz gerekir, örneğin: <a href="http://192.168.99.100/items/5?q=somequery" class="external-link" target="_blank">http://192.168.99.100/items/5?q=somequery</a> veya <a href="http://127.0.0.1/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1/items/5?q=somequery</a> (veya eşdeğeri, Docker ana bilgisayarınızı kullanarak).

Şöyle bir şey göreceksiniz:

```JSON
{"item_id": 5, "q": "somequery"}
```

## Etkileşimli API belgeleri

Şimdi <a href="http://192.168.99.100/docs" class="external-link" target="_blank">http://192.168.99.100/docs</a> veya <a href="http://127.0.0.1/docs" class="external-link" target="_blank">http://127.0.0.1/docs</a>'a (veya eşdeğeri, Docker ana bilgisayarınızı kullanarak) gidebilirsiniz.

Otomatik etkileşimli API belgelerini göreceksiniz (<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a> tarafından sağlanan):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

## Alternatif API belgeleri

Ayrıca <a href="http://192.168.99.100/redoc" class="external-link" target="_blank">http://192.168.99.100/redoc</a> veya <a href="http://127.0.0.1/redoc" class="external-link" target="_blank">http://127.0.0.1/redoc</a>'a (veya eşdeğeri, Docker ana bilgisayarınızı kullanarak) gidebilirsiniz.

Alternatif otomatik belgeleri göreceksiniz (<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> tarafından sağlanan):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Tek Dosyalı FastAPI ile Docker İmajı Oluşturma

FastAPI'niz `./app` dizini olmadan `main.py` gibi tek bir dosyaysa, dosya yapınız şöyle görünebilir:

```
.
├── Dockerfile
├── main.py
└── requirements.txt
```

O zaman yalnızca dosyayı `Dockerfile` içinde kopyalamak için ilgili yolları değiştirmeniz gerekir:

```{ .dockerfile .annotate hl_lines="10  13" }
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# (1)!
COPY ./main.py /code/

# (2)!
CMD ["fastapi", "run", "main.py", "--port", "80"]
```

1. `main.py` dosyasını doğrudan `/code` dizinine kopyalayın (herhangi bir `./app` dizini olmadan).

2. Tek dosya `main.py`'deki uygulamanızı sunmak için `fastapi run` kullanın.

Dosyayı `fastapi run`'a ilettiğinizde, bunun tek bir dosya olduğunu ve bir paketin parçası olmadığını otomatik olarak algılayacak ve nasıl içe aktarıp FastAPI uygulamanızı sunacağını bilecektir. 😎

## Yayınlama Kavramları

Konteynerler açısından aynı [Yayınlama Kavramları](concepts.md){.internal-link target=_blank}'ndan tekrar bahsedelim.

Konteynerler esas olarak bir uygulamayı **oluşturma ve yayınlama** sürecini basitleştirmek için bir araçtır, ama bu **yayınlama kavramlarını** ele almak için belirli bir yaklaşımı zorlamazlar ve birkaç olası strateji vardır.

**İyi haber** şu ki, her farklı stratejide tüm yayınlama kavramlarını karşılamanın bir yolu vardır. 🎉

Bu **yayınlama kavramlarını** konteynerler açısından inceleyelim:

* HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* Replikasyon (çalışan süreç sayısı)
* Bellek
* Başlamadan önceki adımlar

## HTTPS

Yalnızca FastAPI uygulaması için **konteyner imajına** (ve sonra çalışan **konteynere**) odaklanırsak, HTTPS normalde başka bir araç tarafından **dışarıdan** yönetilir.

Bu, **HTTPS**'yi ve **otomatik** sertifika edinimini yöneten başka bir konteyner olabilir, örneğin <a href="https://traefik.io/" class="external-link" target="_blank">Traefik</a> ile.

/// tip

Traefik, Docker, Kubernetes ve diğerleriyle entegrasyonlara sahiptir, bu yüzden konteynerleriniz için HTTPS'yi kurup yapılandırmak çok kolaydır.

///

Alternatif olarak, HTTPS hizmetlerinden biri olarak bir bulut sağlayıcı tarafından yönetilebilir (uygulamayı bir konteynerde çalıştırmaya devam ederken).

## Başlangıçta Çalıştırma ve Yeniden Başlatmalar

Normalde konteynerinizi **başlatma ve çalıştırma** sorumluluğunu üstlenen başka bir araç vardır.

Bu doğrudan **Docker**, **Docker Compose**, **Kubernetes**, bir **bulut hizmeti** vb. olabilir.

Çoğu (veya tüm) durumda, konteyneri başlangıçta çalıştırmayı ve hatalarda yeniden başlatmayı etkinleştirmek için basit bir seçenek vardır. Örneğin, Docker'da bu, `--restart` komut satırı seçeneğidir.

Konteynerler kullanmadan, uygulamaların başlangıçta çalışmasını ve yeniden başlamasını sağlamak zahmetli ve zor olabilir. Ama **konteynerlerle çalışırken** çoğu durumda bu işlevsellik varsayılan olarak dahildir. ✨

## Replikasyon - Süreç Sayısı

Birden fazla makinede dağıtılmış konteynerleri yönetmek için **Kubernetes**, Docker Swarm Mode, Nomad veya başka bir benzer karmaşık sistemle bir <abbr title="Birbirine bağlanmak ve birlikte çalışmak üzere yapılandırılmış bir makine grubu.">küme</abbr> makineniz varsa, muhtemelen her konteynerde bir **süreç yöneticisi** (işçilerle Uvicorn gibi) kullanmak yerine **replikasyonu** **küme seviyesinde** yönetmek isteyeceksiniz.

Kubernetes gibi dağıtık konteyner yönetim sistemlerinden birinin normalde gelen istekler için **yük dengelemeyi** desteklerken **konteynerlerin replikasyonunu** yönetmenin entegre bir yolu vardır. Hepsi **küme seviyesinde**.

Bu durumlarda, muhtemelen [yukarıda açıklandığı gibi](#fastapi-icin-bir-docker-imaji-olusturma) **sıfırdan bir Docker imajı** oluşturmak, bağımlılıklarınızı yüklemek ve birden fazla Uvicorn işçisi kullanmak yerine **tek bir Uvicorn süreci** çalıştırmak isteyeceksiniz.

### Yük Dengeleyici

Konteynerler kullanırken, normalde **ana portta** dinleyen bir bileşen olur. Bu muhtemelen **HTTPS**'yi yönetmek için bir **TLS Sonlandırma Proxy'si** olan veya benzeri bir araç olan başka bir konteyner olabilir.

Bu bileşen isteklerin **yükünü** alacak ve (umarız) **dengeli** bir şekilde işçilere dağıtacağından, genellikle **Yük Dengeleyici** olarak da adlandırılır.

/// tip

HTTPS için kullanılan aynı **TLS Sonlandırma Proxy'si** bileşeni muhtemelen bir **Yük Dengeleyici** de olacaktır.

///

Ve konteynerlerle çalışırken, onları başlatmak ve yönetmek için kullandığınız aynı sistem, o **yük dengeleyiciden** (aynı zamanda bir **TLS Sonlandırma Proxy'si** de olabilir) uygulamanızla konteyner(ler)e **ağ iletişimini** iletmek (örn. HTTP istekleri) için dahili araçlara sahip olacaktır.

### Bir Yük Dengeleyici - Birden Fazla İşçi Konteyneri

**Kubernetes** veya benzeri dağıtık konteyner yönetim sistemleriyle çalışırken, dahili ağ mekanizmalarını kullanmak, ana **portta** dinleyen tek **yük dengeleyicinin** uygulamanızı çalıştıran muhtemelen **birden fazla konteynere** iletişimi (istekleri) iletmesine olanak tanır.

Uygulamanızı çalıştıran bu konteynerlerin her birinde normalde **yalnızca tek bir süreç** olacaktır (örn. FastAPI uygulamanızı çalıştıran bir Uvicorn süreci). Hepsi **aynı konteynerler** olacaktır, aynı şeyi çalıştıran, ama her biri kendi süreci, belleği vb. ile. Bu şekilde CPU'nun **farklı çekirdeklerinde** ve hatta **farklı makinelerde** **paralelleştirmeden** yararlanırsınız.

Ve **yük dengeleyici** ile dağıtık konteyner sistemi, istekleri uygulamanızla her bir konteynere **sırayla** dağıtır. Böylece, her istek uygulamanızı çalıştıran birden fazla **replike edilmiş konteynerden** biri tarafından karşılanabilir.

Ve normalde bu **yük dengeleyici**, kümenizdeki *diğer* uygulamalara (örn. farklı bir alan adına veya farklı bir URL yol öneki altına) giden istekleri de yönetebilir ve iletişimi kümenizdeki *o diğer* uygulama için çalışan doğru konteynerlere iletir.

### Konteyner Başına Tek Süreç

Bu tür senaryolarda, muhtemelen **konteyner başına tek bir (Uvicorn) sürece** sahip olmak istersiniz, çünkü replikasyonu zaten küme seviyesinde yönetiyor olursunuz.

Bu yüzden, bu durumda, konteynerde birden fazla işçiye sahip olmak **istemezsiniz**, örneğin `--workers` komut satırı seçeneği ile. Konteyner başına yalnızca **tek bir Uvicorn sürecine** sahip olmak isteyeceksiniz (ama muhtemelen birden fazla konteyner).

Konteyner içinde başka bir süreç yöneticisine sahip olmak (birden fazla işçi ile olacağı gibi) yalnızca muhtemelen küme sisteminizle zaten ilgilendiğiniz **gereksiz karmaşıklık** ekler.

### Birden Fazla Süreçli Konteynerler ve Özel Durumlar

Elbette, içinde birden fazla **Uvicorn işçi süreci** bulunan **bir konteynere** sahip olmak isteyebileceğiniz **özel durumlar** vardır.

Bu durumlarda, çalıştırmak istediğiniz işçi sayısını ayarlamak için `--workers` komut satırı seçeneğini kullanabilirsiniz:

```{ .dockerfile .annotate }
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# (1)!
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--workers", "4"]
```

1. Burada işçi sayısını 4 olarak ayarlamak için `--workers` komut satırı seçeneğini kullanıyoruz.

İşte bunun mantıklı olabileceği bazı örnekler:

#### Basit Bir Uygulama

Uygulamanız **yeterince basitse** ve bir küme değil, **tek bir sunucuda** çalıştırabiliyorsanız konteynerde bir süreç yöneticisi isteyebilirsiniz.

#### Docker Compose

**Docker Compose** ile **tek bir sunucuya** (küme değil) yayınlama yapıyor olabilirsiniz, bu yüzden paylaşılan ağı ve **yük dengelemeyi** korurken konteynerlerin replikasyonunu (Docker Compose ile) yönetmenin kolay bir yolunuz olmayabilir.

O zaman, içinde birden fazla **işçi süreci** başlatan bir **süreç yöneticisine** sahip **tek bir konteynere** sahip olmak isteyebilirsiniz.

---

Ana nokta şudur, bunların **hiçbiri** körü körüne takip etmeniz gereken **taşa yazılmış kurallar** değildir. Bu fikirleri kendi kullanım durumunuzu **değerlendirmek** ve sisteminiz için en iyi yaklaşımın ne olduğuna karar vermek için kullanabilirsiniz, kavramları nasıl yöneteceğinizi kontrol ederek:

* Güvenlik - HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* Replikasyon (çalışan süreç sayısı)
* Bellek
* Başlamadan önceki adımlar

## Bellek

**Konteyner başına tek bir süreç** çalıştırırsanız, her bir konteynerin (replike edilmişlerse birden fazla) tükettiği az çok iyi tanımlanmış, kararlı ve sınırlı miktarda belleğe sahip olursunuz.

Ve ardından, konteyner yönetim sisteminiz için (örneğin **Kubernetes**) yapılandırmalarınızda aynı bellek limitleri ve gereksinimlerini ayarlayabilirsiniz. Bu şekilde, **mevcut makinelerde** konteynerleri, ihtiyaç duydukları bellek miktarını ve kümedeki makinelerde mevcut olan miktarı dikkate alarak **replike edebilecektir**.

Uygulamanız **basitse**, bu muhtemelen **sorun olmayacaktır** ve sabit bellek limitleri belirtmeniz gerekmeyebilir. Ama **çok fazla bellek** kullanıyorsanız (örneğin **makine öğrenimi** modelleri ile), ne kadar bellek tükettiğinizi kontrol etmeli ve **her makinede** çalışan **konteyner sayısını** ayarlamalısınız (ve belki kümenize daha fazla makine eklemelisiniz).

**Konteyner başına birden fazla süreç** çalıştırırsanız, başlatılan süreç sayısının mevcut olandan **daha fazla bellek** tüketmediğinden emin olmanız gerekir.

## Başlamadan Önceki Adımlar ve Konteynerler

Konteynerler kullanıyorsanız (örn. Docker, Kubernetes), kullanabileceğiniz iki ana yaklaşım vardır.

### Birden Fazla Konteyner

**Birden fazla konteyneriniz** varsa, her biri muhtemelen **tek bir süreç** çalıştırıyorsa (örneğin, bir **Kubernetes** kümesinde), replike edilmiş işçi konteynerlerini çalıştırmadan **önce**, tek bir konteynerde, tek bir süreç çalıştırarak **önceki adımların** işini yapan **ayrı bir konteynere** sahip olmak isteyeceksiniz.

/// info

Kubernetes kullanıyorsanız, bu muhtemelen bir <a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/" class="external-link" target="_blank">Init Container</a> olacaktır.

///

Kullanım durumunuzda bu önceki adımları **birden çok kez paralel olarak** çalıştırmada sorun yoksa (örneğin veritabanı geçişleri değil de yalnızca veritabanının hazır olup olmadığını kontrol ediyorsanız), ana süreci başlatmadan hemen önce bunları her konteynere de koyabilirsiniz.

### Tek Konteyner

Birden fazla **işçi süreci** (veya yalnızca tek bir süreç) başlatan **tek bir konteynere** sahip basit bir kurulumunuz varsa, bu önceki adımları uygulamayla aynı konteynerde, süreçten hemen önce çalıştırabilirsiniz.

### Temel Docker İmajı

Eskiden resmi bir FastAPI Docker imajı vardı: <a href="https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker" class="external-link" target="_blank">tiangolo/uvicorn-gunicorn-fastapi</a>. Ama artık kullanımdan kaldırılmıştır. ⛔️

Muhtemelen bu temel Docker imajını (veya benzer herhangi birini) kullanmamalısınız.

**Kubernetes** (veya benzeri) kullanıyorsanız ve birden fazla **konteynerle** küme seviyesinde zaten **replikasyonu** ayarlıyorsanız, yukarıda açıklandığı gibi **sıfırdan bir imaj oluşturmanız** daha iyidir: [FastAPI İçin Bir Docker İmajı Oluşturma](#fastapi-icin-bir-docker-imaji-olusturma).

Ve birden fazla işçiye ihtiyacınız varsa, sadece `--workers` komut satırı seçeneğini kullanabilirsiniz.

/// note | Teknik Detaylar

Docker imajı, Uvicorn ölü işçileri yönetmeyi ve yeniden başlatmayı desteklemediği zamanlar için oluşturulmuştu, bu yüzden Gunicorn'u Uvicorn ile kullanmak gerekiyordu, bu da sadece Gunicorn'un Uvicorn işçi süreçlerini yönetip yeniden başlatmasını sağlamak için oldukça fazla karmaşıklık ekliyordu.

Ama artık Uvicorn (ve `fastapi` komutu) `--workers` kullanmayı desteklediğinden, kendi imajınızı oluşturmak yerine bir temel Docker imajı kullanmanın hiçbir nedeni yoktur (neredeyse aynı miktarda kod 😅).

///

## Konteyner İmajını Yayınlama

Bir Konteyner (Docker) İmajına sahip olduktan sonra, onu yayınlamanın birkaç yolu vardır.

Örneğin:

* Tek bir sunucuda **Docker Compose** ile
* Bir **Kubernetes** kümesiyle
* Bir Docker Swarm Mode kümesiyle
* Nomad gibi başka bir araçla
* Konteyner imajınızı alıp yayınlayan bir bulut hizmetiyle

## `uv` ile Docker İmajı

Projenizi yüklemek ve yönetmek için <a href="https://github.com/astral-sh/uv" class="external-link" target="_blank">uv</a> kullanıyorsanız, onların <a href="https://docs.astral.sh/uv/guides/integration/docker/" class="external-link" target="_blank">uv Docker kılavuzunu</a> takip edebilirsiniz.

## Özet

Konteyner sistemleri (örn. **Docker** ve **Kubernetes** ile) kullanarak tüm **yayınlama kavramlarını** yönetmek oldukça basit hale gelir:

* HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* Replikasyon (çalışan süreç sayısı)
* Bellek
* Başlamadan önceki adımlar

Çoğu durumda, muhtemelen herhangi bir temel imaj kullanmak istemeyeceksiniz, bunun yerine resmi Python Docker imajına dayalı **sıfırdan bir konteyner imajı oluşturacaksınız**.

`Dockerfile`'daki talimatların **sırasına** ve **Docker önbelleğine** dikkat ederek **oluşturma sürelerini en aza indirebilir**, üretkenliğinizi en üst düzeye çıkarabilirsiniz (ve sıkılmaktan kaçınabilirsiniz). 😎
