# Sunucuyu Manuel Olarak Çalıştırma

## `fastapi run` Komutunu Kullanma

Kısaca, FastAPI uygulamanızı sunmak için `fastapi run` komutunu kullanın:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> run <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting production server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000/docs</u></font>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>2306215</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
```

</div>

Bu çoğu durumda işe yarayacaktır. 😎

Örneğin bu komutu **FastAPI** uygulamanızı bir konteynerde, bir sunucuda vb. başlatmak için kullanabilirsiniz.

## ASGI Sunucuları

Detaylara biraz daha derinlemesine bakalım.

FastAPI, Python web framework'leri ve sunucuları oluşturmak için kullanılan <abbr title="Asynchronous Server Gateway Interface">ASGI</abbr> adlı bir standart kullanır. FastAPI bir ASGI web framework'üdür.

Bir **FastAPI** uygulamasını (veya herhangi bir ASGI uygulamasını) uzak bir sunucu makinesinde çalıştırmak için ihtiyacınız olan ana şey, **Uvicorn** gibi bir ASGI sunucu programıdır, bu `fastapi` komutunda varsayılan olarak gelen sunucudur.

Birkaç alternatif vardır:

* <a href="https://www.uvicorn.org/" class="external-link" target="_blank">Uvicorn</a>: yüksek performanslı bir ASGI sunucusu.
* <a href="https://hypercorn.readthedocs.io/" class="external-link" target="_blank">Hypercorn</a>: HTTP/2 ve Trio gibi özelliklerle uyumlu bir ASGI sunucusu.
* <a href="https://github.com/django/daphne" class="external-link" target="_blank">Daphne</a>: Django Channels için oluşturulan ASGI sunucusu.
* <a href="https://github.com/emmett-framework/granian" class="external-link" target="_blank">Granian</a>: Python uygulamaları için bir Rust HTTP sunucusu.
* <a href="https://unit.nginx.org/howto/fastapi/" class="external-link" target="_blank">NGINX Unit</a>: NGINX Unit, hafif ve çok yönlü bir web uygulama çalışma zamanıdır.

## Sunucu Makinesi ve Sunucu Programı

İsimler hakkında akılda tutulması gereken küçük bir ayrıntı var. 💡

"**Sunucu**" kelimesi genellikle hem uzak/bulut bilgisayarı (fiziksel veya sanal makine) hem de o makinede çalışan programı (örn. Uvicorn) ifade etmek için kullanılır.

Genel olarak "sunucu" diye okuduğunuzda, bu iki şeyden birine atıfta bulunabileceğini aklınızda tutun.

Uzak makineyi ifade ederken, genellikle **sunucu** olarak adlandırılır, ama ayrıca **makine**, **VM** (sanal makine), **düğüm** de denir. Bunların hepsi, genellikle Linux çalıştıran, programları çalıştırdığınız bir tür uzak makineye atıfta bulunur.

## Sunucu Programını Yükleme

FastAPI'yi yüklediğinizde, üretim sunucusu Uvicorn ile birlikte gelir ve `fastapi run` komutuyla başlatabilirsiniz.

Ama bir ASGI sunucusunu manuel olarak da yükleyebilirsiniz.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve ardından sunucu uygulamasını yükleyebilirsiniz.

Örneğin, Uvicorn'u yüklemek için:

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

Benzer bir süreç diğer herhangi bir ASGI sunucu programı için de geçerli olacaktır.

/// tip

`standard` ekleyerek, Uvicorn bazı önerilen ek bağımlılıkları yükleyip kullanacaktır.

Bu, `asyncio` için büyük eşzamanlılık performans artışı sağlayan yüksek performanslı yedek olan `uvloop`'u içerir.

FastAPI'yi `pip install "fastapi[standard]"` gibi bir şeyle yüklediğinizde, `uvicorn[standard]`'ı da zaten alırsınız.

///

## Sunucu Programını Çalıştırma

Bir ASGI sunucusunu manuel olarak yüklediyseniz, normalde FastAPI uygulamanızı içe aktarmak için özel bir biçimde bir içe aktarma dizesi iletmeniz gerekir:

<div class="termy">

```console
$ uvicorn main:app --host 0.0.0.0 --port 80

<span style="color: green;">INFO</span>:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

</div>

/// note

`uvicorn main:app` komutu şunu ifade eder:

* `main`: `main.py` dosyası (Python "modülü").
* `app`: `main.py` içinde `app = FastAPI()` satırıyla oluşturulan nesne.

Bu şuna eşdeğerdir:

```Python
from main import app
```

///

Her alternatif ASGI sunucu programının benzer bir komutu olacaktır, kendi belgelerinde daha fazlasını okuyabilirsiniz.

/// warning

Uvicorn ve diğer sunucular, geliştirme sırasında yararlı olan bir `--reload` seçeneğini destekler.

`--reload` seçeneği çok daha fazla kaynak tüketir, daha kararsızdır vb.

**Geliştirme** sırasında çok yardımcı olur, ama **üretimde** kullanmamalısınız.

///

## Yayınlama Kavramları

Bu örnekler sunucu programını (örn. Uvicorn) çalıştırır, önceden tanımlanmış bir portta (örn. `80`) tüm IP'lerde (`0.0.0.0`) dinleyen **tek bir süreç** başlatır.

Bu temel fikirdir. Ama muhtemelen birkaç ek şeyle ilgilenmek isteyeceksiniz, örneğin:

* Güvenlik - HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* Replikasyon (çalışan süreç sayısı)
* Bellek
* Başlamadan önceki adımlar

Sonraki bölümlerde bu kavramların her biri hakkında daha fazla bilgi vereceğim, bunlar hakkında nasıl düşüneceğinizi ve bunları ele almak için stratejilerle bazı somut örnekler göstereceğim. 🚀
