# İlk Adımlar

En basit FastAPI dosyası şöyle görünebilir:

{* ../../docs_src/first_steps/tutorial001.py *}

Bunu bir `main.py` dosyasına kopyalayın.

Canlı sunucuyu çalıştırın:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

Çıktıda şöyle bir satır var:

```hl_lines="4"
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Bu satır, uygulamanızın yerel makinenizde sunulduğu URL'yi gösterir.

### Kontrol edin

Tarayıcınızı <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a> adresinde açın.

JSON yanıtını şöyle göreceksiniz:

```JSON
{"message": "Hello World"}
```

### Etkileşimli API belgeleri

Şimdi <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> adresine gidin.

Otomatik etkileşimli API belgelerini göreceksiniz (<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a> tarafından sağlanan):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternatif API belgeleri

Şimdi <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> adresine gidin.

Alternatif otomatik belgeleri göreceksiniz (<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> tarafından sağlanan):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### OpenAPI

**FastAPI**, API'leri tanımlamak için **OpenAPI** standardını kullanarak tüm API'nizin bir "şemasını" oluşturur.

#### "Şema"

Bir "şema", bir şeyin tanımı veya açıklamasıdır. Onu uygulayan kod değil, sadece soyut bir açıklama.

#### API "şeması"

Bu durumda, <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a>, API'nizin şemasının nasıl tanımlanacağını belirleyen bir spesifikasyondur.

Bu şema tanımı, API yollarınızı, aldıkları olası parametreleri vb. içerir.

#### Veri "şeması"

"Şema" terimi, JSON içeriği gibi bazı verilerin şekline de atıfta bulunabilir.

Bu durumda, JSON niteliklerini ve sahip oldukları veri tiplerini vb. ifade eder.

#### OpenAPI ve JSON Schema

OpenAPI, API'niz için bir API şeması tanımlar. Ve bu şema, JSON veri şemaları standardı olan **JSON Schema** kullanılarak API'niz tarafından gönderilen ve alınan verilerin tanımlarını (veya "şemalarını") içerir.

#### `openapi.json`'ı kontrol edin

Ham OpenAPI şemasının nasıl göründüğünü merak ediyorsanız, FastAPI tüm API'nizin açıklamalarını içeren bir JSON (şema) otomatik olarak oluşturur.

Doğrudan şu adreste görebilirsiniz: <a href="http://127.0.0.1:8000/openapi.json" class="external-link" target="_blank">http://127.0.0.1:8000/openapi.json</a>.

Şöyle başlayan bir JSON gösterecektir:

```JSON
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...
```

#### OpenAPI ne işe yarar

OpenAPI şeması, dahil edilen iki etkileşimli belgelendirme sistemini besleyen şeydir.

Ve hepsi OpenAPI'ye dayalı düzinelerce alternatif vardır. **FastAPI** ile oluşturulmuş uygulamanıza bu alternatiflerden herhangi birini kolayca ekleyebilirsiniz.

Ayrıca API'nizle iletişim kuran istemciler için otomatik olarak kod üretmek için de kullanabilirsiniz. Örneğin, ön yüz, mobil veya IoT uygulamaları.

## Özet, adım adım

### Adım 1: `FastAPI`'yi içe aktarın

{* ../../docs_src/first_steps/tutorial001.py hl[1] *}

`FastAPI`, API'niz için tüm işlevselliği sağlayan bir Python sınıfıdır.

/// note | Teknik Detaylar

`FastAPI`, doğrudan `Starlette`'ten miras alan bir sınıftır.

Tüm <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> işlevselliğini **FastAPI** ile de kullanabilirsiniz.

///

### Adım 2: bir `FastAPI` "örneği" oluşturun

{* ../../docs_src/first_steps/tutorial001.py hl[3] *}

Burada `app` değişkeni `FastAPI` sınıfının bir "örneği" olacaktır.

Bu, tüm API'nizi oluşturmak için ana etkileşim noktası olacaktır.

### Adım 3: bir *yol operasyonu* oluşturun

#### Yol

Buradaki "Yol", URL'nin ilk `/`'den başlayan son kısmını ifade eder.

Yani, şöyle bir URL'de:

```
https://example.com/items/foo
```

...yol şu olurdu:

```
/items/foo
```

/// info

Bir "yol", yaygın olarak "endpoint" veya "route" olarak da adlandırılır.

///

Bir API oluştururken, "yol" "kaygıları" ve "kaynakları" ayırmanın ana yoludur.

#### Operasyon

Buradaki "Operasyon", HTTP "metotlarından" birini ifade eder.

Bunlardan biri:

* `POST`
* `GET`
* `PUT`
* `DELETE`

...ve daha nadir olanlar:

* `OPTIONS`
* `HEAD`
* `PATCH`
* `TRACE`

HTTP protokolünde, bu "metotlardan" birini (veya birkaçını) kullanarak her yol ile iletişim kurabilirsiniz.

---

API'ler oluştururken, belirli bir eylemi gerçekleştirmek için normalde bu belirli HTTP metotlarını kullanırsınız.

Normalde şunları kullanırsınız:

* `POST`: veri oluşturmak için.
* `GET`: veri okumak için.
* `PUT`: veri güncellemek için.
* `DELETE`: veri silmek için.

Yani, OpenAPI'de HTTP metotlarının her birine bir "operasyon" denir.

Biz de onlara "**operasyonlar**" diyeceğiz.

#### Bir *yol operasyonu dekoratörü* tanımlayın

{* ../../docs_src/first_steps/tutorial001.py hl[6] *}

`@app.get("/")`, **FastAPI**'ye aşağıdaki fonksiyonun şu istekleri karşılamakla sorumlu olduğunu söyler:

* `/` yolu
* <abbr title="bir HTTP GET metodu"><code>get</code> operasyonunu</abbr> kullanarak

/// info | `@decorator` Bilgisi

Python'daki `@bir_şey` söz dizisine "dekoratör" denir.

Onu bir fonksiyonun üstüne koyarsınız. Güzel bir dekoratif şapka gibi (sanırım terim buradan geldi).

Bir "dekoratör" aşağıdaki fonksiyonu alır ve onunla bir şey yapar.

Bizim durumumuzda, bu dekoratör **FastAPI**'ye aşağıdaki fonksiyonun `/` **yolu** ile `get` **operasyonuna** karşılık geldiğini söyler.

Bu "**yol operasyonu dekoratörü**"dür.

///

Diğer operasyonları da kullanabilirsiniz:

* `@app.post()`
* `@app.put()`
* `@app.delete()`

Ve daha nadir olanları:

* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

/// tip

Her operasyonu (HTTP metodu) istediğiniz gibi kullanmakta özgürsünüz.

**FastAPI** herhangi bir özel anlam dayatmaz.

Buradaki bilgiler bir kılavuz olarak sunulur, zorunluluk olarak değil.

Örneğin, GraphQL kullanırken normalde tüm eylemleri yalnızca `POST` operasyonlarını kullanarak gerçekleştirirsiniz.

///

### Adım 4: **yol operasyonu fonksiyonunu** tanımlayın

Bu bizim "**yol operasyonu fonksiyonumuz**"dur:

* **yol**: `/`.
* **operasyon**: `get`.
* **fonksiyon**: "dekoratör"ün altındaki fonksiyondur (`@app.get("/")`'nin altında).

{* ../../docs_src/first_steps/tutorial001.py hl[7] *}

Bu bir Python fonksiyonudur.

**FastAPI** tarafından `GET` operasyonu kullanılarak "`/`" URL'sine her istek geldiğinde çağrılacaktır.

Bu durumda, bir `async` fonksiyondur.

---

Bunu `async def` yerine normal bir fonksiyon olarak da tanımlayabilirsiniz:

{* ../../docs_src/first_steps/tutorial003.py hl[7] *}

/// note

Farkı bilmiyorsanız, [Async: *"Aceleniz mi var?"*](../async.md#in-a-hurry){.internal-link target=_blank} bölümüne bakın.

///

### Adım 5: içeriği döndürün

{* ../../docs_src/first_steps/tutorial001.py hl[8] *}

Bir `dict`, `list`, tekil değerler olarak `str`, `int` vb. döndürebilirsiniz.

Ayrıca Pydantic modelleri de döndürebilirsiniz (daha sonra bunun hakkında daha fazla bilgi edineceksiniz).

JSON'a otomatik olarak dönüştürülecek birçok başka nesne ve model vardır (ORM'ler dahil). Favorilerinizi kullanmayı deneyin, büyük olasılıkla zaten desteklenmektedirler.

## Özet

* `FastAPI`'yi içe aktarın.
* Bir `app` örneği oluşturun.
* `@app.get("/")` gibi dekoratörler kullanarak bir **yol operasyonu dekoratörü** yazın.
* Bir **yol operasyonu fonksiyonu** tanımlayın; örneğin, `def root(): ...`.
* `fastapi dev` komutunu kullanarak geliştirme sunucusunu çalıştırın.
