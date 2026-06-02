# İstemci Oluşturma

**FastAPI** OpenAPI spesifikasyonuna dayandığı için, otomatik API belgeleri (Swagger UI tarafından sağlanan) dahil olmak üzere birçok araçla otomatik uyumluluk elde edersiniz.

Mutlaka bariz olmayan özel bir avantaj, birçok farklı **programlama dili** için API'niz için **istemci oluşturabilmenizdir** (bazen <abbr title="Yazılım Geliştirme Kitleri">**SDK**</abbr> olarak da adlandırılır).

## OpenAPI İstemci Oluşturucuları

**OpenAPI**'den istemci oluşturmak için birçok araç vardır.

Yaygın bir araç <a href="https://openapi-generator.tech/" class="external-link" target="_blank">OpenAPI Generator</a>'dır.

Bir **frontend** oluşturuyorsanız, çok ilginç bir alternatif <a href="https://github.com/hey-api/openapi-ts" class="external-link" target="_blank">openapi-ts</a>'dir.

## İstemci ve SDK Oluşturucuları - Sponsor

OpenAPI (FastAPI) tabanlı bazı **şirket destekli** İstemci ve SDK oluşturucuları da vardır, bazı durumlarda yüksek kaliteli oluşturulan SDK'lar/istemcilerin üzerine **ek özellikler** sunabilirler.

Bazıları da ✨ [**FastAPI'yi sponsorlar**](../help-fastapi.md#sponsor-the-author){.internal-link target=_blank} ✨, bu FastAPI'nin sürekli ve sağlıklı **gelişimini** ve **ekosistemini** sağlar.

Ve FastAPI'ye ve **topluluğuna** (siz) olan gerçek bağlılıklarını gösterir, çünkü size yalnızca **iyi bir hizmet** sunmak istemekle kalmayıp, aynı zamanda **iyi ve sağlıklı bir framework**'ünüz olduğundan emin olmak isterler, FastAPI. 🙇

Örneğin, şunları denemek isteyebilirsiniz:

* <a href="https://speakeasy.com/?utm_source=fastapi+repo&utm_medium=github+sponsorship" class="external-link" target="_blank">Speakeasy</a>
* <a href="https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral" class="external-link" target="_blank">Stainless</a>
* <a href="https://developers.liblab.com/tutorials/sdk-for-fastapi/?utm_source=fastapi" class="external-link" target="_blank">liblab</a>

Çevrimiçi arayıp bulabileceğiniz benzer hizmetler sunan başka birçok şirket de var. 🤓

## TypeScript Frontend İstemcisi Oluşturma

Basit bir FastAPI uygulamasıyla başlayalım:

{* ../../docs_src/generate_clients/tutorial001_py39.py hl[7:9,12:13,16:17,21] *}

*Yol operasyonlarının*, istek yükü ve yanıt yükü için kullandıkları modelleri `Item` ve `ResponseMessage` modellerini kullanarak tanımladığına dikkat edin.

### API Belgeleri

API belgelerine giderseniz, isteklerde gönderilecek ve yanıtlarda alınacak veriler için **şemaları** göreceksiniz:

<img src="/img/tutorial/generate-clients/image01.png">

Uygulamadaki modellerle bildirildiği için bu şemaları görebilirsiniz.

Bu bilgi uygulamanın **OpenAPI şemasında** mevcuttur ve ardından API belgelerinde (Swagger UI tarafından) gösterilir.

Ve OpenAPI'de bulunan modellerden gelen aynı bilgi, **istemci kodunu oluşturmak** için kullanılabilir.

### TypeScript İstemcisi Oluşturma

Artık modellerle uygulamaya sahip olduğumuza göre, frontend için istemci kodunu oluşturabiliriz.

#### `openapi-ts`'yi yükleyin

Frontend kodunuza `openapi-ts`'yi şu şekilde yükleyebilirsiniz:

<div class="termy">

```console
$ npm install @hey-api/openapi-ts --save-dev

---> 100%
```

</div>

#### İstemci Kodu Oluşturma

İstemci kodunu oluşturmak için, artık yüklü olan `openapi-ts` komut satırı uygulamasını kullanabilirsiniz.

Yerel projede yüklü olduğundan, muhtemelen o komutu doğrudan çağıramazsınız, ama `package.json` dosyanıza koyarsınız.

Şöyle görünebilir:

```JSON  hl_lines="7"
{
  "name": "frontend-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "generate-client": "openapi-ts --input http://localhost:8000/openapi.json --output ./src/client --client axios"
  },
  "author": "",
  "license": "",
  "devDependencies": {
    "@hey-api/openapi-ts": "^0.27.38",
    "typescript": "^4.6.2"
  }
}
```

O NPM `generate-client` betiğine sahip olduktan sonra, şu şekilde çalıştırabilirsiniz:

<div class="termy">

```console
$ npm run generate-client

frontend-app@1.0.0 generate-client /home/user/code/frontend-app
> openapi-ts --input http://localhost:8000/openapi.json --output ./src/client --client axios
```

</div>

Bu komut `./src/client` içinde kod oluşturacak ve dahili olarak `axios`'u (frontend HTTP kütüphanesi) kullanacaktır.

### İstemci Kodunu Deneyin

Artık istemci kodunu içe aktarabilir ve kullanabilirsiniz, şöyle görünebilir, yöntemler için otomatik tamamlama aldığınıza dikkat edin:

<img src="/img/tutorial/generate-clients/image02.png">

Gönderilecek yük için de otomatik tamamlama alacaksınız:

<img src="/img/tutorial/generate-clients/image03.png">

/// tip

FastAPI uygulamasında `Item` modelinde tanımlanan `name` ve `price` için otomatik tamamlamaya dikkat edin.

///

Gönderdiğiniz veriler için satır içi hatalar alacaksınız:

<img src="/img/tutorial/generate-clients/image04.png">

Yanıt nesnesinde de otomatik tamamlama olacaktır:

<img src="/img/tutorial/generate-clients/image05.png">

## Etiketli FastAPI Uygulaması

Birçok durumda FastAPI uygulamanız daha büyük olacaktır ve muhtemelen farklı *yol operasyonu* gruplarını ayırmak için etiketler kullanacaksınız.

Örneğin, **öğeler** için bir bölüm ve **kullanıcılar** için başka bir bölüm olabilir ve bunlar etiketlerle ayrılabilir:

{* ../../docs_src/generate_clients/tutorial002_py39.py hl[21,26,34] *}

### Etiketlerle TypeScript İstemcisi Oluşturma

Etiketler kullanan bir FastAPI uygulaması için istemci oluşturursanız, normalde istemci kodunu da etiketlere göre ayıracaktır.

Bu şekilde istemci kodu için her şeyi doğru şekilde sıralanmış ve gruplandırılmış olarak elde edebilirsiniz:

<img src="/img/tutorial/generate-clients/image06.png">

Bu durumda şunlara sahipsiniz:

* `ItemsService`
* `UsersService`

### İstemci Yöntem Adları

Şu anda `createItemItemsPost` gibi oluşturulan yöntem adları çok temiz görünmüyor:

```TypeScript
ItemsService.createItemItemsPost({name: "Plumbus", price: 5})
```

...bunun nedeni istemci oluşturucunun her *yol operasyonu* için OpenAPI dahili **operasyon ID**'sini kullanmasıdır.

OpenAPI, her operasyon ID'sinin tüm *yol operasyonları* arasında benzersiz olmasını gerektirir, bu yüzden FastAPI operasyon ID'lerinin benzersiz olduğundan emin olmak için **fonksiyon adını**, **yolu** ve **HTTP yöntemini/operasyonunu** kullanarak o operasyon ID'sini oluşturur.

Ama sırada bunu nasıl geliştireceğinizi göstereceğim. 🤓

## Özel Operasyon ID'leri ve Daha İyi Yöntem Adları

Bu operasyon ID'lerinin **oluşturulma şeklini değiştirerek** bunları daha basit hale getirebilir ve istemcilerde **daha basit yöntem adlarına** sahip olabilirsiniz.

Bu durumda her operasyon ID'sinin başka bir şekilde **benzersiz** olduğundan emin olmanız gerekecektir.

Örneğin, her *yol operasyonunun* bir etikete sahip olduğundan emin olabilir ve ardından operasyon ID'sini **etiket** ve *yol operasyonu* **adına** (fonksiyon adı) göre oluşturabilirsiniz.

### Özel Benzersiz ID Fonksiyonu Oluşturma

FastAPI, her *yol operasyonu* için bir **benzersiz ID** kullanır, bu **operasyon ID**'si ve ayrıca istekler veya yanıtlar için gerekli özel modellerin adları için kullanılır.

Bu fonksiyonu özelleştirebilirsiniz. Bir `APIRoute` alır ve bir dize çıktısı verir.

Örneğin, burada ilk etiketi (muhtemelen yalnızca bir etiketiniz olacaktır) ve *yol operasyonu* adını (fonksiyon adı) kullanıyor.

Ardından bu özel fonksiyonu **FastAPI**'ye `generate_unique_id_function` parametresi olarak geçirebilirsiniz:

{* ../../docs_src/generate_clients/tutorial003_py39.py hl[6:7,10] *}

### Özel Operasyon ID'leriyle TypeScript İstemcisi Oluşturma

Şimdi istemciyi tekrar oluşturursanız, geliştirilmiş yöntem adlarına sahip olduğunu göreceksiniz:

<img src="/img/tutorial/generate-clients/image07.png">

Gördüğünüz gibi, yöntem adları artık etiketi ve ardından fonksiyon adını içeriyor, artık URL yolu ve HTTP operasyonundan bilgi içermiyorlar.

### İstemci Oluşturucu için OpenAPI Spesifikasyonunu Ön İşleme

Oluşturulan kod hala bazı **yinelenen bilgiler** içeriyor.

Bu yöntemin **öğelerle** ilgili olduğunu zaten biliyoruz çünkü o kelime `ItemsService`'de var (etiketten alınmış), ama yine de yöntem adında etiket adı ön ek olarak var. 😕

Genel olarak OpenAPI için muhtemelen bunu tutmak isteyeceğiz, çünkü bu operasyon ID'lerinin **benzersiz** olmasını sağlayacaktır.

Ama oluşturulan istemci için, istemcileri oluşturmadan hemen önce OpenAPI operasyon ID'lerini **değiştirebiliriz**, sadece bu yöntem adlarını daha güzel ve **temiz** yapmak için.

OpenAPI JSON'ını `openapi.json` dosyasına indirebilir ve ardından şu script ile **ön eki kaldırabiliriz**:

{* ../../docs_src/generate_clients/tutorial004.py *}

//// tab | Node.js

```Javascript
{!> ../../docs_src/generate_clients/tutorial004.js!}
```

////

Bununla, operasyon ID'leri `items-get_items` gibi şeylerden sadece `get_items`'a yeniden adlandırılacaktır, böylece istemci oluşturucu daha basit yöntem adları oluşturabilir.

### Ön İşlenmiş OpenAPI ile TypeScript İstemcisi Oluşturma

Şimdi son sonuç bir `openapi.json` dosyasında olduğundan, `package.json`'ı o yerel dosyayı kullanacak şekilde değiştirirsiniz, örneğin:

```JSON  hl_lines="7"
{
  "name": "frontend-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "generate-client": "openapi-ts --input ./openapi.json --output ./src/client --client axios"
  },
  "author": "",
  "license": "",
  "devDependencies": {
    "@hey-api/openapi-ts": "^0.27.38",
    "typescript": "^4.6.2"
  }
}
```

Yeni istemciyi oluşturduktan sonra, artık tüm **otomatik tamamlama**, **satır içi hatalar** vb. ile **temiz yöntem adlarına** sahip olacaksınız:

<img src="/img/tutorial/generate-clients/image08.png">

## Faydalar

Otomatik olarak oluşturulan istemcileri kullanırken şunlar için **otomatik tamamlama** alırsınız:

* Yöntemler.
* Gövdedeki istek yükleri, sorgu parametreleri vb.
* Yanıt yükleri.

Ayrıca her şey için **satır içi hatalara** sahip olursunuz.

Ve backend kodunu her güncellediğinizde ve frontend'i **yeniden oluşturduğunuzda**, yöntemler olarak mevcut yeni *yol operasyonlarına* sahip olacak, eskileri kaldırılmış olacak ve diğer değişiklikler oluşturulan kodda yansıtılmış olacaktır. 🤓

Bu ayrıca bir şey değiştiyse istemci kodunda otomatik olarak **yansıtılacağı** anlamına gelir. Ve istemciyi **oluşturursanız**, kullanılan verilerde herhangi bir **uyumsuzluk** varsa hata verecektir.

Böylece, hataların üretimdeki son kullanıcılarınıza gösterilmesini beklemek ve ardından sorunun nerede olduğunu bulmaya çalışmak yerine, geliştirme döngüsünün çok erken aşamalarında **birçok hatayı tespit edersiniz**. ✨
