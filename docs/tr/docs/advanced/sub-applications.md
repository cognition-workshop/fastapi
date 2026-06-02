# Alt Uygulamalar - Bağlamalar

İki bağımsız FastAPI uygulamasına, kendi bağımsız OpenAPI'leri ve kendi belge arayüzleriyle ihtiyacınız varsa, bir ana uygulamaya sahip olabilir ve bir (veya daha fazla) alt uygulama(ları) "bağlayabilirsiniz".

## Bir **FastAPI** uygulamasını bağlama

"Bağlama", belirli bir yola tamamen "bağımsız" bir uygulama eklemek anlamına gelir, bu uygulama daha sonra o alt uygulamada bildirilen _yol operasyonlarıyla_ o yolun altındaki her şeyi ele alır.

### Üst düzey uygulama

İlk olarak, ana, üst düzey **FastAPI** uygulamasını ve *yol operasyonlarını* oluşturun:

{* ../../docs_src/sub_applications/tutorial001.py hl[3, 6:8] *}

### Alt uygulama

Ardından, alt uygulamanızı ve *yol operasyonlarını* oluşturun.

Bu alt uygulama başka bir standart FastAPI uygulamasıdır, ancak "bağlanacak" olan budur:

{* ../../docs_src/sub_applications/tutorial001.py hl[11, 14:16] *}

### Alt uygulamayı bağlayın

Üst düzey uygulamanızda, `app`'de, alt uygulamayı, `subapi`'yi bağlayın.

Bu durumda, `/subapi` yoluna bağlanacaktır:

{* ../../docs_src/sub_applications/tutorial001.py hl[11, 19] *}

### Otomatik API belgelerini kontrol edin

Şimdi, dosyanızla `fastapi` komutunu çalıştırın:

<div class="termy">

```console
$ fastapi dev main.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

Ve belgeleri <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> adresinde açın.

Yalnızca kendi _yol operasyonlarını_ içeren ana uygulama için otomatik API belgelerini göreceksiniz:

<img src="/img/tutorial/sub-applications/image01.png">

Ve ardından, <a href="http://127.0.0.1:8000/subapi/docs" class="external-link" target="_blank">http://127.0.0.1:8000/subapi/docs</a> adresinde alt uygulama için belgeleri açın.

Yalnızca kendi _yol operasyonlarını_ içeren, hepsi doğru alt yol öneki `/subapi` altında olan alt uygulama için otomatik API belgelerini göreceksiniz:

<img src="/img/tutorial/sub-applications/image02.png">

İki kullanıcı arayüzünden herhangi biriyle etkileşim kurmayı denerseniz, doğru şekilde çalışacaklardır, çünkü tarayıcı her belirli uygulama veya alt uygulamayla konuşabilecektir.

### Teknik Detaylar: `root_path`

Yukarıda açıklandığı gibi bir alt uygulamayı bağladığınızda, FastAPI ASGI spesifikasyonundaki `root_path` adlı bir mekanizma kullanarak alt uygulama için bağlama yolunu iletmeyi halleder.

Bu şekilde, alt uygulama belge arayüzü için o yol önekini kullanmayı bilecektir.

Ve alt uygulama da kendi bağlanmış alt uygulamalarına sahip olabilir ve her şey doğru çalışır, çünkü FastAPI tüm bu `root_path`'leri otomatik olarak yönetir.

`root_path` ve onu açıkça nasıl kullanacağınız hakkında daha fazla bilgiyi [Bir Proxy Arkasında](behind-a-proxy.md){.internal-link target=_blank} bölümünde öğreneceksiniz.
