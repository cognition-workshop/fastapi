# SQL (İlişkisel) Veritabanları

**FastAPI**, bir SQL (ilişkisel) veritabanı kullanmanızı gerektirmez. Ancak istediğiniz **herhangi bir veritabanını** kullanabilirsiniz.

Burada <a href="https://sqlmodel.tiangolo.com/" class="external-link" target="_blank">SQLModel</a> kullanan bir örnek göreceğiz.

**SQLModel**, <a href="https://www.sqlalchemy.org/" class="external-link" target="_blank">SQLAlchemy</a> ve Pydantic üzerine inşa edilmiştir. **SQL veritabanları** kullanması gereken FastAPI uygulamaları için mükemmel uyum sağlamak üzere **FastAPI**'nin aynı yazarı tarafından yapılmıştır.

/// tip

İstediğiniz başka herhangi bir SQL veya NoSQL veritabanı kütüphanesini kullanabilirsiniz (bazı durumlarda <abbr title="Object Relational Mapper, bazı sınıfların SQL tablolarını ve örneklerin bu tablolardaki satırları temsil ettiği bir kütüphane için süslü bir terim">"ORM"</abbr> olarak adlandırılır), FastAPI sizi hiçbir şeyi kullanmaya zorlamaz. 😎

///

SQLModel, SQLAlchemy'ye dayandığından, SQLAlchemy tarafından **desteklenen herhangi bir veritabanını** kolayca kullanabilirsiniz (bu da onları SQLModel tarafından da desteklenen yapar), örneğin:

* PostgreSQL
* MySQL
* SQLite
* Oracle
* Microsoft SQL Server, vb.

Bu örnekte **SQLite** kullanacağız, çünkü tek bir dosya kullanır ve Python'un entegre desteği vardır. Böylece, bu örneği kopyalayıp olduğu gibi çalıştırabilirsiniz.

Daha sonra, üretim uygulamanız için **PostgreSQL** gibi bir veritabanı sunucusu kullanmak isteyebilirsiniz.

/// tip

**FastAPI** ve **PostgreSQL** ile birlikte frontend ve daha fazla araç içeren resmi bir proje oluşturucu vardır: <a href="https://github.com/fastapi/full-stack-fastapi-template" class="external-link" target="_blank">https://github.com/fastapi/full-stack-fastapi-template</a>

///

Bu çok basit ve kısa bir öğreticidir, veritabanları hakkında genel olarak, SQL hakkında veya daha gelişmiş özellikler hakkında bilgi edinmek istiyorsanız, <a href="https://sqlmodel.tiangolo.com/" class="external-link" target="_blank">SQLModel belgelerine</a> gidin.

## `SQLModel` yükleyin

İlk olarak, [sanal ortamınızı](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından `sqlmodel`'i yükleyin:

<div class="termy">

```console
$ pip install sqlmodel
---> 100%
```

</div>

## Tek Modelle Uygulamayı Oluşturun

İlk olarak uygulamanın en basit ilk versiyonunu tek bir **SQLModel** modeliyle oluşturacağız.

Daha sonra aşağıda **çoklu modeller** ile güvenliği ve çok yönlülüğü artırarak geliştirecegiz. 🤓

### Modelleri Oluşturun

`SQLModel`'i içe aktarın ve bir veritabanı modeli oluşturun:

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[1:11] hl[7:11] *}

`Hero` sınıfı bir Pydantic modeline çok benzer (aslında, altta aslında *bir Pydantic modeli*dir).

Birkaç fark var:

* `table=True`, SQLModel'e bunun bir *tablo modeli* olduğunu söyler, SQL veritabanında bir **tabloyu** temsil etmelidir, yalnızca bir *veri modeli* değildir (diğer normal Pydantic sınıfları gibi olurdu).

* `Field(primary_key=True)`, SQLModel'e `id`'nin SQL veritabanındaki **birincil anahtar** olduğunu söyler (SQL birincil anahtarları hakkında daha fazla bilgiyi SQLModel belgelerinde bulabilirsiniz).

    Tipi `int | None` olarak belirlenerek, SQLModel bu sütunun SQL veritabanında `INTEGER` olması ve `NULLABLE` olması gerektiğini bilecektir.

* `Field(index=True)`, SQLModel'e bu sütun için bir **SQL indeksi** oluşturması gerektiğini söyler, bu da veritabanında bu sütuna göre filtrelenmiş verileri okurken daha hızlı aramalar yapılmasını sağlar.

    SQLModel, `str` olarak bildirilen bir şeyin `TEXT` (veya veritabanına bağlı olarak `VARCHAR`) tipinde bir SQL sütunu olacağını bilecektir.

### Bir Motor Oluşturun

Bir SQLModel `engine` (altta aslında bir SQLAlchemy `engine`'dir) veritabanına olan **bağlantıları tutan** şeydir.

Aynı veritabanına bağlanmak için tüm kodunuz için **tek bir `engine` nesneniz** olurdu.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[14:18] hl[14:15,17:18] *}

`check_same_thread=False` kullanmak, FastAPI'nin aynı SQLite veritabanını farklı iş parçacıklarında kullanmasına olanak tanır. **Tek bir istek** birden **fazla iş parçacığı** kullanabileceğinden (örneğin bağımlılıklarda) bu gereklidir.

Endişelenmeyin, kodun yapılandırılma şekliyle, daha sonra **istek başına tek bir SQLModel *oturumu*** kullandığımızdan emin olacağız, aslında `check_same_thread`'in başarmaya çalıştığı şey budur.

### Tabloları Oluşturun

Ardından tüm *tablo modelleri* için **tabloları oluşturmak** üzere `SQLModel.metadata.create_all(engine)` kullanan bir fonksiyon ekliyoruz.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[21:22] hl[21:22] *}

### Bir Oturum Bağımlılığı Oluşturun

Bir **`Session`**, **nesneleri bellekte saklayan** ve verideki gerekli değişiklikleri takip eden, ardından veritabanıyla iletişim kurmak için **`engine`'i kullanan** şeydir.

Her istek için yeni bir `Session` sağlayacak `yield` ile bir FastAPI **bağımlılığı** oluşturacağız. İstek başına tek bir oturum kullandığımızdan emin olan şey budur. 🤓

Ardından bu bağımlılığı kullanacak kodun geri kalanını basitleştirmek için bir `Annotated` bağımlılığı `SessionDep` oluşturuyoruz.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[25:30]  hl[25:27,30] *}

### Başlangıçta Veritabanı Tablolarını Oluşturun

Uygulama başladığında veritabanı tablolarını oluşturacağız.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[32:37] hl[35:37] *}

Burada bir uygulama başlatma olayında tabloları oluşturuyoruz.

Üretim için muhtemelen uygulamanızı başlatmadan önce çalışan bir göç betiği kullanırsınız. 🤓

/// tip

SQLModel'in Alembic'i saran göç yardımcı araçları olacak, ancak şimdilik <a href="https://alembic.sqlalchemy.org/en/latest/" class="external-link" target="_blank">Alembic</a>'i doğrudan kullanabilirsiniz.

///

### Bir Kahraman Oluşturun

Her SQLModel modeli aynı zamanda bir Pydantic modeli olduğundan, Pydantic modellerini kullanabileceğiniz aynı **tip açıklamalarında** kullanabilirsiniz.

Örneğin, `Hero` tipinde bir parametre bildirirseniz, **JSON gövdesinden** okunacaktır.

Aynı şekilde, fonksiyonun **dönüş tipi** olarak bildirebilirsiniz ve ardından verinin şekli otomatik API belgeleri arayüzünde görünecektir.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[40:45] hl[40:45] *}

Burada yeni `Hero`'yu `Session` örneğine eklemek, veritabanındaki değişiklikleri kaydetmek, `hero`'daki verileri yenilemek ve ardından döndürmek için `SessionDep` bağımlılığını (bir `Session`) kullanıyoruz.

### Kahramanları Oku

Veritabanından `Hero`'ları bir `select()` kullanarak **okuyabiliriz**. Sonuçları sayfalamak için bir `limit` ve `offset` ekleyebiliriz.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[48:55] hl[51:52,54] *}

### Tek Bir Kahramanı Oku

Tek bir `Hero`'yu **okuyabiliriz**.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[58:63] hl[60] *}

### Bir Kahramanı Sil

Ayrıca bir `Hero`'yu **silebiliriz**.

{* ../../docs_src/sql_databases/tutorial001_an_py310.py ln[66:73] hl[71] *}

### Uygulamayı Çalıştırın

Uygulamayı çalıştırabilirsiniz:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Ardından `/docs` arayüzüne gidin, **FastAPI**'nin bu **modelleri** kullanarak API'yi **belgelediğini** göreceksiniz ve verileri **serileştirmek** ve **doğrulamak** için de kullanacaktır.

<div class="screenshot">
<img src="/img/tutorial/sql-databases/image01.png">
</div>

## Uygulamayı Çoklu Modellerle Güncelleyin

Şimdi **güvenliği** ve **çok yönlülüğü** artırmak için bu uygulamayı biraz **yeniden yapılandıralım**.

Önceki uygulamayı kontrol ederseniz, arayüzde şimdiye kadar istemcinin oluşturulacak `Hero`'nun `id`'sini belirlemesine izin verdiğini göreceksiniz. 😱

Bunun olmasına izin vermemeliyiz, veritabanında zaten atanmış bir `id`'yi geçersiz kılabilirler. `id`'yi belirlemek **backend** veya **veritabanı** tarafından yapılmalıdır, **istemci tarafından değil**.

Ek olarak, kahraman için bir `secret_name` oluşturuyoruz, ancak şimdiye kadar onu her yerde döndürüyoruz, bu pek **gizli** değil... 😅

Bunları birkaç **ekstra model** ekleyerek düzelteceğiz. SQLModel'in parlayacağı yer burasıdır. ✨

### Çoklu Modeller Oluşturun

**SQLModel**'de, `table=True`'ya sahip herhangi bir model sınıfı bir **tablo modelidir**.

Ve `table=True`'ya sahip olmayan herhangi bir model sınıfı bir **veri modelidir**, bunlar aslında sadece Pydantic modelleridir (birkaç küçük ekstra özellikle). 🤓

SQLModel ile, tüm alanları her durumda **tekrarlamaktan kaçınmak** için **kalıtım** kullanabiliriz.

#### `HeroBase` - temel sınıf

Tüm modeller tarafından **paylaşılan tüm alanlara** sahip bir `HeroBase` modeliyle başlayalım:

* `name`
* `age`

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[7:9] hl[7:9] *}

#### `Hero` - *tablo modeli*

Ardından, diğer modellerde her zaman olmayan **ekstra alanlarla** gerçek *tablo modeli* `Hero`'yu oluşturalım:

* `id`
* `secret_name`

`Hero`, `HeroBase`'den miras aldığı için, `HeroBase`'de bildirilen **alanları** da **içerir**, bu yüzden `Hero`'nun tüm alanları:

* `id`
* `name`
* `age`
* `secret_name`

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[7:14] hl[12:14] *}

#### `HeroPublic` - genel *veri modeli*

Sonra, API istemcilerine **döndürülecek** olan bir `HeroPublic` modeli oluşturuyoruz.

`HeroBase` ile aynı alanlara sahiptir, bu yüzden `secret_name`'i içermeyecektir.

Sonunda, kahramanlarımızın kimliği korunuyor! 🥷

Ayrıca `id: int`'i yeniden bildirir. Bunu yaparak, API istemcileriyle bir **sözleşme** yapıyoruz, böylece `id`'nin her zaman orada olacağını ve her zaman `int` olacağını (asla `None` olmayacağını) bekleyebilirler.

/// tip

Dönüş modelinin bir değerin her zaman mevcut olduğunu ve her zaman `int` (`None` değil) olduğunu garanti etmesi, API istemcileri için çok kullanışlıdır, bu kesinlikle çok daha basit kod yazabilirler.

Ayrıca, **otomatik oluşturulan istemciler** daha basit arayüzlere sahip olacaktır, böylece API'nizle iletişim kuran geliştiriciler API'nizle çalışırken çok daha iyi bir deneyim yaşayabilir. 😎

///

`HeroPublic`'teki tüm alanlar `HeroBase`'dekiyle aynıdır, `id` `int` olarak bildirilmiştir (`None` değil):

* `id`
* `name`
* `age`

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[7:18] hl[17:18] *}

#### `HeroCreate` - bir kahraman oluşturmak için *veri modeli*

Şimdi istemcilerden gelen verileri **doğrulayacak** bir `HeroCreate` modeli oluşturuyoruz.

`HeroBase` ile aynı alanlara sahiptir ve ayrıca `secret_name`'i de içerir.

Artık istemciler **yeni bir kahraman oluştururken**, `secret_name`'i gönderecekler, veritabanında saklanacaktır, ancak bu gizli adlar API'de istemcilere döndürülmeyecektir.

/// tip

**Şifreleri** bu şekilde ele alırsınız. Alırsınız, ancak API'de döndürmezsiniz.

Ayrıca şifrelerin değerlerini saklamadan önce **karma** yaparsınız, **asla düz metin olarak saklamazsınız**.

///

`HeroCreate`'in alanları:

* `name`
* `age`
* `secret_name`

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[7:22] hl[21:22] *}

#### `HeroUpdate` - bir kahramanı güncellemek için *veri modeli*

Uygulamanın önceki sürümünde bir **kahramanı güncellemenin** bir yolu yoktu, ama şimdi **çoklu modellerle** bunu yapabiliriz. 🎉

`HeroUpdate` *veri modeli* biraz özeldir, yeni bir kahraman oluşturmak için gerekli olan **tüm aynı alanlara** sahiptir, ancak tüm alanlar **isteğe bağlıdır** (hepsinin bir varsayılan değeri vardır). Bu şekilde, bir kahramanı güncellediğinizde, yalnızca güncellemek istediğiniz alanları gönderebilirsiniz.

Tüm **alanlar gerçekten değiştiği** için (tip artık `None`'ı içerir ve şimdi varsayılan değeri `None`'dır), bunları **yeniden bildirmemiz** gerekir.

`HeroBase`'den miras almamıza gerçekten gerek yok çünkü tüm alanları yeniden bildiriyoruz. Tutarlılık için miras bırakacağım, ama bu gerekli değil. Bu daha çok kişisel tercih meselesidir. 🤷

`HeroUpdate`'in alanları:

* `name`
* `age`
* `secret_name`

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[7:28] hl[25:28] *}

### `HeroCreate` ile oluşturun ve `HeroPublic` döndürün

Artık **çoklu modellerimiz** olduğuna göre, bunları kullanan uygulamanın bölümlerini güncelleyebiliriz.

İstekte bir `HeroCreate` *veri modeli* alıyoruz ve ondan bir `Hero` *tablo modeli* oluşturuyoruz.

Bu yeni *tablo modeli* `Hero`, istemci tarafından gönderilen alanlara sahip olacak ve ayrıca veritabanı tarafından oluşturulan bir `id`'ye sahip olacaktır.

Ardından fonksiyondan aynı *tablo modeli* `Hero`'yu olduğu gibi döndürüyoruz. Ancak `response_model`'i `HeroPublic` *veri modeli* olarak bildirdiğimiz için, **FastAPI** verileri doğrulamak ve serileştirmek için `HeroPublic`'i kullanacaktır.

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[56:62] hl[56:58] *}

/// tip

Şimdi **dönüş tipi açıklaması** `-> HeroPublic` yerine `response_model=HeroPublic` kullanıyoruz çünkü döndürdüğümüz değer aslında `HeroPublic` *değil*.

`-> HeroPublic` bildirmiş olsaydık, editörünüz ve linter'ınız (haklı olarak) `HeroPublic` yerine `Hero` döndürdüğünüzden şikayet ederdi.

Bunu `response_model`'de bildirerek **FastAPI**'ye işini yapmasını söylüyoruz, tip açıklamalarına ve editörünüz ile diğer araçlardan gelen yardıma müdahale etmeden.

///

### `HeroPublic` ile Kahramanları Oku

`Hero`'ları **okumak** için daha önce olduğu gibi aynı şeyi yapabiliriz, yine verilerin doğru şekilde doğrulanıp serileştirildiğinden emin olmak için `response_model=list[HeroPublic]` kullanıyoruz.

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[65:72] hl[65] *}

### `HeroPublic` ile Tek Bir Kahramanı Oku

Tek bir kahramanı **okuyabiliriz**:

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[75:80] hl[77] *}

### `HeroUpdate` ile Bir Kahramanı Güncelle

Bir kahramanı **güncelleyebiliriz**. Bunun için bir HTTP `PATCH` operasyonu kullanıyoruz.

Ve kodda, istemci tarafından gönderilen tüm verileri içeren bir `dict` alıyoruz, **yalnızca istemci tarafından gönderilen verileri**, sadece varsayılan değerler olması nedeniyle orada olacak değerleri hariç tutarak. Bunu yapmak için `exclude_unset=True` kullanıyoruz. Bu ana numara budur. 🪄

Ardından `hero_db`'yi `hero_data`'daki verilerle güncellemek için `hero_db.sqlmodel_update(hero_data)` kullanıyoruz.

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[83:93] hl[83:84,88:89] *}

### Bir Kahramanı Tekrar Sil

Bir kahramanı **silmek** hemen hemen aynı kalır.

Bu sefer her şeyi yeniden yapılandırma isteğini karşılamayacağız. 😅

{* ../../docs_src/sql_databases/tutorial002_an_py310.py ln[96:103] hl[101] *}

### Uygulamayı Tekrar Çalıştırın

Uygulamayı tekrar çalıştırabilirsiniz:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

`/docs` API arayüzüne giderseniz, artık güncellenmiş olduğunu göreceksiniz ve bir kahraman oluştururken istemciden `id` almayı beklemeyecektir, vb.

<div class="screenshot">
<img src="/img/tutorial/sql-databases/image02.png">
</div>

## Özet

Bir SQL veritabanıyla etkileşim kurmak ve *veri modelleri* ve *tablo modelleri* ile kodu basitleştirmek için <a href="https://sqlmodel.tiangolo.com/" class="external-link" target="_blank">**SQLModel**</a>'i kullanabilirsiniz.

Daha fazla bilgi edinmek için **SQLModel belgelerine** gidebilirsiniz, daha büyük bir eğitici kılavuzu da dahil olmak üzere daha fazla bilgi bulabilirsiniz. 🚀
