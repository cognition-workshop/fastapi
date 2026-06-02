# Sunucu İşçileri - Uvicorn ile İşçiler

Daha önceki yayınlama kavramlarını tekrar gözden geçirelim:

* Güvenlik - HTTPS
* Başlangıçta çalıştırma
* Yeniden başlatmalar
* **Replikasyon (çalışan süreç sayısı)**
* Bellek
* Başlamadan önceki adımlar

Bu noktaya kadar, belgelerdeki tüm öğreticilerde, muhtemelen Uvicorn'u çalıştıran `fastapi` komutunu kullanarak **tek bir süreçte** bir **sunucu programı** çalıştırıyordunuz.

Uygulamaları yayınlarken, **birden fazla çekirdeğin** avantajından yararlanmak ve daha fazla isteği karşılayabilmek için muhtemelen bazı **süreç replikasyonlarına** sahip olmak isteyeceksiniz.

Önceki bölümde [Yayınlama Kavramları](concepts.md){.internal-link target=_blank}'nda gördüğünüz gibi, kullanabileceğiniz birden fazla strateji vardır.

Burada size `fastapi` komutu veya doğrudan `uvicorn` komutu kullanarak **işçi süreçleriyle** **Uvicorn**'un nasıl kullanılacağını göstereceğim.

/// info

Konteynerler kullanıyorsanız, örneğin Docker veya Kubernetes ile, bunu sonraki bölümde anlatacağım: [Konteynerlerde FastAPI - Docker](docker.md){.internal-link target=_blank}.

Özellikle **Kubernetes** üzerinde çalışırken muhtemelen işçileri kullanmak **istemeyeceksiniz**, bunun yerine **konteyner başına tek bir Uvicorn süreci** çalıştıracaksınız, ama bunu o bölümde anlatacağım.

///

## Birden Fazla İşçi

`--workers` komut satırı seçeneği ile birden fazla işçi başlatabilirsiniz:

//// tab | `fastapi`

`fastapi` komutunu kullanıyorsanız:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> run --workers 4 <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting production server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with the
             following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000/docs</u></font>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://0.0.0.0:8000</u></font> <b>(</b>Press CTRL+C to
             quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started parent process <b>[</b><font color="#34E2E2"><b>27365</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27368</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27369</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27370</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>27367</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

////

//// tab | `uvicorn`

Doğrudan `uvicorn` komutunu kullanmayı tercih ediyorsanız:

<div class="termy">

```console
$ uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
<font color="#A6E22E">INFO</font>:     Uvicorn running on <b>http://0.0.0.0:8080</b> (Press CTRL+C to quit)
<font color="#A6E22E">INFO</font>:     Started parent process [<font color="#A1EFE4"><b>27365</b></font>]
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27368</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27369</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27370</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
<font color="#A6E22E">INFO</font>:     Started server process [<font color="#A1EFE4">27367</font>]
<font color="#A6E22E">INFO</font>:     Waiting for application startup.
<font color="#A6E22E">INFO</font>:     Application startup complete.
```

</div>

////

Buradaki tek yeni seçenek `--workers`'dır ve Uvicorn'a 4 işçi süreci başlatmasını söyler.

Ayrıca her sürecin **PID**'sini gösterdiğini görebilirsiniz, ana süreç için `27365` (bu **süreç yöneticisi**dir) ve her işçi süreci için birer tane: `27368`, `27369`, `27370` ve `27367`.

## Yayınlama Kavramları

Burada uygulamanın çalışmasını **paralelleştirmek**, CPU'daki **birden fazla çekirdeğin** avantajını kullanmak ve **daha fazla isteği** karşılayabilmek için birden fazla **işçiyi** nasıl kullanacağınızı gördünüz.

Yukarıdaki yayınlama kavramları listesinden, işçileri kullanmak ağırlıklı olarak **replikasyon** kısmına yardımcı olacaktır ve biraz da **yeniden başlatmalara**, ama yine de diğerleriyle ilgilenmeniz gerekecektir:

* **Güvenlik - HTTPS**
* **Başlangıçta çalıştırma**
* ***Yeniden başlatmalar***
* Replikasyon (çalışan süreç sayısı)
* **Bellek**
* **Başlamadan önceki adımlar**

## Konteynerler ve Docker

Sonraki bölüm [Konteynerlerde FastAPI - Docker](docker.md){.internal-link target=_blank}'da diğer **yayınlama kavramlarını** ele almak için kullanabileceğiniz bazı stratejileri açıklayacağım.

Tek bir Uvicorn süreci çalıştırmak için **sıfırdan kendi imajınızı nasıl oluşturacağınızı** göstereceğim. Bu basit bir süreçtir ve muhtemelen **Kubernetes** gibi dağıtık konteyner yönetim sistemi kullanırken yapmak isteyeceğiniz şeydir.

## Özet

Birden fazla **işçi süreci** ile `fastapi` veya `uvicorn` komutlarının `--workers` CLI seçeneğini kullanarak **çok çekirdekli CPU'ların** avantajını kullanabilir ve **birden fazla süreci paralel olarak** çalıştırabilirsiniz.

Bu araçları ve fikirleri, diğer yayınlama kavramlarını kendiniz ele alarak **kendi yayınlama sisteminizi** kuruyorsanız kullanabilirsiniz.

Konteynerlerle (örn. Docker ve Kubernetes) **FastAPI** hakkında bilgi edinmek için sonraki bölüme göz atın. Bu araçların diğer **yayınlama kavramlarını** da ele almanın basit yollarına sahip olduğunu göreceksiniz. ✨
