# Ekstra Modeller

Önceki örnekle devam edersek, birden fazla ilişkili modele sahip olmak yaygın olacaktır.

Bu özellikle kullanıcı modelleri için geçerlidir, çünkü:

* **Giriş modeli** bir parola içerebilmelidir.
* **Çıkış modeli** bir parola içermemelidir.
* **Veritabanı modeli** muhtemelen hashlenmiş bir parola içermelidir.

/// danger

Kullanıcıların düz metin parolalarını asla saklamayın. Her zaman doğrulayabileceğiniz "güvenli bir hash" saklayın.

Bilmiyorsanız, "parola hash'i"nin ne olduğunu [güvenlik bölümlerinde](security/simple-oauth2.md#password-hashing){.internal-link target=_blank} öğreneceksiniz.

///

## Birden fazla model

İşte modellerin parola alanları ve kullanıldıkları yerlerle nasıl görünebileceğine dair genel bir fikir:

{* ../../docs_src/extra_models/tutorial001_py310.py hl[7,9,14,20,22,27:28,31:33,38:39] *}


/// info

Pydantic v1'de metot `.dict()` olarak adlandırılıyordu, Pydantic v2'de kullanımdan kaldırıldı (ancak hâlâ destekleniyor) ve `.model_dump()` olarak yeniden adlandırıldı.

Buradaki örnekler Pydantic v1 ile uyumluluk için `.dict()` kullanır, ancak Pydantic v2 kullanabiliyorsanız bunun yerine `.model_dump()` kullanmalısınız.

///

### `**user_in.dict()` hakkında

#### Pydantic'in `.dict()`'i

`user_in`, `UserIn` sınıfının bir Pydantic modelidir.

Pydantic modelleri, modelin verisini içeren bir `dict` döndüren `.dict()` metoduna sahiptir.

Yani, şöyle bir Pydantic nesnesi `user_in` oluşturursak:

```Python
user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
```

ve sonra şunu çağırırsak:

```Python
user_dict = user_in.dict()
```

artık `user_dict` değişkeninde veriyi içeren bir `dict`'imiz var (Pydantic model nesnesi yerine bir `dict`).

Ve şunu çağırırsak:

```Python
print(user_dict)
```

şöyle bir Python `dict` alırız:

```Python
{
    'username': 'john',
    'password': 'secret',
    'email': 'john.doe@example.com',
    'full_name': None,
}
```

#### Bir `dict`'i açma

`user_dict` gibi bir `dict` alıp `**user_dict` ile bir fonksiyona (veya sınıfa) iletirsek, Python onu "açacaktır". `user_dict`'in anahtarlarını ve değerlerini doğrudan anahtar-değer argümanları olarak iletecektir.

Yani, yukarıdaki `user_dict` ile devam edersek, şunu yazmak:

```Python
UserInDB(**user_dict)
```

şuna eşdeğer bir sonuç üretecektir:

```Python
UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)
```

Veya daha kesin olarak, `user_dict`'i doğrudan kullanarak, gelecekte sahip olabileceği içeriklerle:

```Python
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)
```

#### Başka bir modelin içeriğinden bir Pydantic modeli

Yukarıdaki örnekte `user_dict`'i `user_in.dict()`'ten aldığımız gibi, bu kod:

```Python
user_dict = user_in.dict()
UserInDB(**user_dict)
```

şuna eşdeğer olacaktır:

```Python
UserInDB(**user_in.dict())
```

...çünkü `user_in.dict()` bir `dict`'tir ve sonra Python'un onu `**` ile `UserInDB`'ye ileterek "açmasını" sağlıyoruz.

Böylece, başka bir Pydantic modelindeki veriden bir Pydantic modeli elde ediyoruz.

#### Bir `dict`'i açma ve ekstra anahtar kelimeler

Ve ardından şöyle ekstra `hashed_password=hashed_password` anahtar kelime argümanı ekleme:

```Python
UserInDB(**user_in.dict(), hashed_password=hashed_password)
```

...şöyle olur:

```Python
UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    hashed_password = hashed_password,
)
```

/// warning

Destekleyici ek fonksiyonlar `fake_password_hasher` ve `fake_save_user`, verilerin olası akışını göstermek içindir, ancak elbette gerçek bir güvenlik sağlamıyorlar.

///

## Tekrarı azaltın

Kod tekrarını azaltmak **FastAPI**'nin temel fikirlerinden biridir.

Kod tekrarı, hata, güvenlik sorunları, kod senkronizasyon sorunları (bir yerde güncellediğinizde diğerlerinde güncellemediğinizde) vb. olasılıkları artırır.

Ve bu modeller çok fazla veriyi paylaşıyor ve nitelik adlarını ve tiplerini tekrarlıyor.

Daha iyisini yapabiliriz.

Diğer modellerimiz için temel olarak hizmet eden bir `UserBase` modeli bildirebiliriz. Ve sonra onun niteliklerini (tip bildirimleri, doğrulama vb.) miras alan alt sınıflar yapabiliriz.

Tüm veri dönüştürme, doğrulama, belgelendirme vb. normal şekilde çalışmaya devam edecektir.

Bu şekilde, modeller arasındaki yalnızca farkları bildirebiliriz (düz metin `password` ile, `hashed_password` ile ve parolasız):

{* ../../docs_src/extra_models/tutorial002_py310.py hl[7,13:14,17:18,21:22] *}

## `Union` veya `anyOf`

Bir yanıtı iki veya daha fazla tipin `Union`'ı olarak bildirebilirsiniz, bu da yanıtın bunlardan herhangi biri olabileceği anlamına gelir.

OpenAPI'de `anyOf` ile tanımlanacaktır.

Bunu yapmak için standart Python tip ipucu <a href="https://docs.python.org/3/library/typing.html#typing.Union" class="external-link" target="_blank">`typing.Union`</a>'ı kullanın:

/// note

Bir <a href="https://docs.pydantic.dev/latest/concepts/types/#unions" class="external-link" target="_blank">`Union`</a> tanımlarken, en spesifik tipi önce, ardından daha az spesifik tipi ekleyin. Aşağıdaki örnekte, daha spesifik `PlaneItem`, `Union[PlaneItem, CarItem]`'da `CarItem`'dan önce gelir.

///

{* ../../docs_src/extra_models/tutorial003_py310.py hl[1,14:15,18:20,33] *}


### Python 3.10'da `Union`

Bu örnekte `Union[PlaneItem, CarItem]`'ı `response_model` argümanının değeri olarak iletiyoruz.

Bunu bir **tip açıklamasına** koymak yerine bir **argümanın değeri** olarak ilettiğimiz için, Python 3.10'da bile `Union` kullanmamız gerekir.

Bir tip açıklamasında olsaydı, dikey çubuğu kullanabilirdik:

```Python
some_variable: PlaneItem | CarItem
```

Ancak bunu `response_model=PlaneItem | CarItem` atamasına koyarsak bir hata alırdık, çünkü Python bunu bir tip açıklaması olarak yorumlamak yerine `PlaneItem` ve `CarItem` arasında **geçersiz bir işlem** gerçekleştirmeye çalışırdı.

## Model listesi

Aynı şekilde, nesne listelerinden oluşan yanıtlar bildirebilirsiniz.

Bunun için standart Python `typing.List`'i (veya Python 3.9 ve üzerinde sadece `list`) kullanın:

{* ../../docs_src/extra_models/tutorial004_py39.py hl[18] *}


## Rastgele `dict` ile yanıt

Bir Pydantic modeli kullanmadan, yalnızca anahtarların ve değerlerin tipini bildirerek düz bir rastgele `dict` kullanarak da bir yanıt bildirebilirsiniz.

Bu, geçerli alan/nitelik adlarını önceden bilmediğinizde (ki bir Pydantic modeli için gerekli olurdu) kullanışlıdır.

Bu durumda `typing.Dict`'i (veya Python 3.9 ve üzerinde sadece `dict`) kullanabilirsiniz:

{* ../../docs_src/extra_models/tutorial005_py39.py hl[6] *}


## Özet

Birden fazla Pydantic modeli kullanın ve her durum için serbestçe miras alın.

Bir varlığın farklı "durumları" olabiliyorsa, varlık başına tek bir veri modeline sahip olmanız gerekmez. `password`, `password_hash` ve parola içermeyen bir durumu olan kullanıcı "varlığı" örneğinde olduğu gibi.
