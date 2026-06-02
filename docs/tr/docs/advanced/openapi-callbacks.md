# OpenAPI Geri Çağrıları

Başka biri (muhtemelen API'nizi *kullanan* geliştirici) tarafından oluşturulan bir *harici API*'ye istek tetikleyebilecek bir *yol operasyonu* olan bir API oluşturabilirsiniz.

API uygulamanızın *harici API*'yi çağırması sürecine "geri çağrı" denir. Çünkü harici geliştirinin yazdığı yazılım API'nize bir istek gönderir ve ardından API'niz *geri çağırarak*, *harici API*'ye (muhtemelen aynı geliştirici tarafından oluşturulan) bir istek gönderir.

Bu durumda, harici API'nin nasıl *görünmesi gerektiğini* belgelemek isteyebilirsiniz. Hangi *yol operasyonuna* sahip olması gerektiğini, hangi gövdeyi beklemesi gerektiğini, hangi yanıtı döndürmesi gerektiğini, vb.

## Geri çağrılı bir uygulama

Tüm bunları bir örnekle görelim.

Fatura oluşturmaya izin veren bir uygulama geliştirdiğinizi hayal edin.

Bu faturaların bir `id`, `title` (isteğe bağlı), `customer` ve `total` alanı olacaktır.

API'nizin kullanıcısı (harici geliştirici), API'nizde bir POST isteği ile fatura oluşturacaktır.

Ardından API'niz (hayal edelim):

* Faturayı harici geliştiricinin bir müşterisine gönderecektir.
* Parayı tahsil edecektir.
* API kullanıcısına (harici geliştiriciye) bir bildirim geri gönderecektir.
    * Bu, harici geliştirici tarafından sağlanan bazı *harici API*'ye bir POST isteği göndererek (*API'nizden*) yapılacaktır (bu "geri çağrı"dır).

## Normal **FastAPI** uygulaması

Önce geri çağrıyı eklemeden önce normal API uygulamasının nasıl görüneceğini görelim.

Bir `Invoice` gövdesi alacak ve geri çağrı URL'sini içerecek bir `callback_url` sorgu parametresine sahip bir *yol operasyonu* olacaktır.

Bu kısım oldukça normal, kodun çoğu muhtemelen size zaten tanıdık geliyordur:

{* ../../docs_src/openapi_callbacks/tutorial001.py hl[9:13,36:53] *}

/// tip

`callback_url` sorgu parametresi bir Pydantic <a href="https://docs.pydantic.dev/latest/api/networks/" class="external-link" target="_blank">Url</a> tipi kullanır.

///

Tek yeni şey, *yol operasyonu dekoratörüne* argüman olarak `callbacks=invoices_callback_router.routes`'tur. Bunun ne olduğunu birazdan göreceğiz.

## Geri çağrıyı belgeleme

Gerçek geri çağrı kodu büyük ölçüde kendi API uygulamanıza bağlı olacaktır.

Ve muhtemelen bir uygulamadan diğerine çok farklılık gösterecektir.

Sadece bir veya iki satır kod olabilir, örneğin:

```Python
callback_url = "https://example.com/api/v1/invoices/events/"
httpx.post(callback_url, json={"description": "Invoice paid", "paid": True})
```

Ama muhtemelen geri çağrının en önemli kısmı, API kullanıcınızın (harici geliştiricinin) *harici API*'yi doğru şekilde uyguladığından emin olmaktır; *API'nizin* geri çağrının istek gövdesinde göndereceği verilere göre, vb.

Bu yüzden yapacağımız bir sonraki şey, *API'nizden* geri çağrıyı almak için *harici API*'nin nasıl görünmesi gerektiğini belgelemek için kodu eklemektir.

Bu belge, API'nizdeki `/docs` adresindeki Swagger UI'da görünecek ve harici geliştiricilere *harici API*'yi nasıl oluşturacaklarını bilmelerini sağlayacaktır.

Bu örnek geri çağrının kendisini uygulamaz (bu sadece bir satır kod olabilir), yalnızca belgeleme kısmını uygular.

/// tip

Gerçek geri çağrı sadece bir HTTP isteğidir.

Geri çağrıyı kendiniz uygularken, <a href="https://www.python-httpx.org" class="external-link" target="_blank">HTTPX</a> veya <a href="https://requests.readthedocs.io/" class="external-link" target="_blank">Requests</a> gibi bir şey kullanabilirsiniz.

///

## Geri çağrı belgeleme kodunu yazın

Bu kod uygulamanızda çalıştırılmayacaktır, yalnızca *harici API*'nin nasıl görünmesi gerektiğini *belgelemek* için ihtiyacımız var.

Ama, **FastAPI** ile bir API için otomatik belgelemenin nasıl kolayca oluşturulacağını zaten biliyorsunuz.

Bu yüzden, *harici API*'nin nasıl görünmesi gerektiğini belgelemek için aynı bilgiyi kullanacağız... harici API'nin uygulaması gereken *yol operasyonu(larını)* oluşturarak (API'nizin çağıracağı olanlar).

/// tip

Geri çağrıyı belgelemek için kodu yazarken, kendinizi o *harici geliştirici* olarak hayal etmek yararlı olabilir. Ve şu anda *API'nizi* değil, *harici API*'yi uyguladığınızı düşünün.

Bu bakış açısını (*harici geliştiricinin*) geçici olarak benimsemek, parametrelerin, gövde için Pydantic modelinin, yanıt için modelin, vb. *harici API* için nereye konulacağını daha belirgin hissetmenize yardımcı olabilir.

///

### Bir geri çağrı `APIRouter`'ı oluşturun

Önce bir veya daha fazla geri çağrıyı içerecek yeni bir `APIRouter` oluşturun.

{* ../../docs_src/openapi_callbacks/tutorial001.py hl[3,25] *}

### Geri çağrı *yol operasyonunu* oluşturun

Geri çağrı *yol operasyonunu* oluşturmak için yukarıda oluşturduğunuz `APIRouter`'ı kullanın.

Normal bir FastAPI *yol operasyonu* gibi görünmelidir:

* Muhtemelen alması gereken gövdenin bir bildirimi olmalıdır, örneğin `body: InvoiceEvent`.
* Ve döndürmesi gereken yanıtın bir bildirimi de olabilir, örneğin `response_model=InvoiceEventReceived`.

{* ../../docs_src/openapi_callbacks/tutorial001.py hl[16:18,21:22,28:32] *}

Normal bir *yol operasyonundan* 2 ana fark vardır:

* Herhangi bir gerçek kodu olması gerekmez, çünkü uygulamanız bu kodu asla çağırmayacaktır. Yalnızca *harici API*'yi belgelemek için kullanılır. Bu yüzden fonksiyon sadece `pass` içerebilir.
* *Yol*, parametreleri ve *API'nize* gönderilen orijinal isteğin parçalarıyla değişkenler kullanabileceği bir <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#key-expression" class="external-link" target="_blank">OpenAPI 3 ifadesi</a> (aşağıda daha fazla bilgi) içerebilir.

### Geri çağrı yol ifadesi

Geri çağrı *yolu*, *API'nize* gönderilen orijinal isteğin parçalarını içerebilen bir <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#key-expression" class="external-link" target="_blank">OpenAPI 3 ifadesi</a> içerebilir.

Bu durumda, bu `str`:

```Python
"{$callback_url}/invoices/{$request.body.id}"
```

Yani, API kullanıcınız (harici geliştirici) *API'nize* şu adrese bir istek gönderirse:

```
https://yourapi.com/invoices/?callback_url=https://www.external.org/events
```

JSON gövdesiyle:

```JSON
{
    "id": "2expen51ve",
    "customer": "Mr. Richie Rich",
    "total": "9999"
}
```

o zaman *API'niz* faturayı işleyecek ve bir noktada `callback_url`'ye (*harici API*) bir geri çağrı isteği gönderecektir:

```
https://www.external.org/events/invoices/2expen51ve
```

şöyle bir JSON gövdesiyle:

```JSON
{
    "description": "Payment celebration",
    "paid": true
}
```

ve *harici API*'den şöyle bir JSON gövdesiyle bir yanıt bekleyecektir:

```JSON
{
    "ok": true
}
```

/// tip

Kullanılan geri çağrı URL'sinin, sorgu parametresi olarak `callback_url`'de alınan URL'yi (`https://www.external.org/events`) ve ayrıca JSON gövdesinin içindeki fatura `id`'sini (`2expen51ve`) içerdiğine dikkat edin.

///

### Geri çağrı yönlendiricisini ekleyin

Bu noktada, yukarıda oluşturduğunuz geri çağrı yönlendiricisinde ihtiyaç duyulan geri çağrı *yol operasyonu(ları)* (*harici geliştiricinin* *harici API*'de uygulaması gerekenler) hazırdır.

Şimdi *API'nizin yol operasyonu dekoratöründeki* `callbacks` parametresini kullanarak, o geri çağrı yönlendiricisinden `.routes` özniteliğini (aslında sadece rotaların/*yol operasyonlarının* bir `list`'i) iletin:

{* ../../docs_src/openapi_callbacks/tutorial001.py hl[35] *}

/// tip

Yönlendiricinin kendisini (`invoices_callback_router`) `callback=`'a değil, `.routes` özniteliğini, yani `invoices_callback_router.routes`'u ilettiğinize dikkat edin.

///

### Belgeleri kontrol edin

Şimdi uygulamanızı başlatabilir ve <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> adresine gidebilirsiniz.

Belgelerinizi, *yol operasyonunuz* için *harici API*'nin nasıl görünmesi gerektiğini gösteren bir "Callbacks" bölümü dahil olarak göreceksiniz:

<img src="/img/tutorial/openapi-callbacks/image01.png">
