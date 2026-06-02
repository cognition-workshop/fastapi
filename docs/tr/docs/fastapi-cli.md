# FastAPI CLI

**FastAPI CLI**, FastAPI uygulamanızı sunmak, FastAPI projenizi yönetmek ve daha fazlası için kullanabileceğiniz bir komut satırı programıdır.

FastAPI'yi yüklediğinizde (örn. `pip install "fastapi[standard]"` ile), `fastapi-cli` adlı bir paket de dahil edilir, bu paket terminalde `fastapi` komutunu sağlar.

FastAPI uygulamanızı geliştirme için çalıştırmak istediğinizde `fastapi dev` komutunu kullanabilirsiniz:

<div class="termy">

```console
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories with
             <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with the
             following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C to
             quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

</div>

`fastapi` adlı komut satırı programı **FastAPI CLI**'dir.

FastAPI CLI, Python programınızın yolunu alır (örn. `main.py`) ve `FastAPI` örneğini (genellikle `app` olarak adlandırılır) otomatik olarak algılar, doğru içe aktarma sürecini belirler ve ardından onu sunar.

Üretim için bunun yerine `fastapi run` kullanırsınız. 🚀

Dahili olarak, **FastAPI CLI** yüksek performanslı, üretime hazır bir ASGI sunucusu olan <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>'u kullanır. 😎

## `fastapi dev`

`fastapi dev` çalıştırmak geliştirme modunu başlatır.

Varsayılan olarak, **otomatik yeniden yükleme** etkindir ve kodunuzda değişiklik yaptığınızda sunucuyu otomatik olarak yeniden yükler. Bu kaynak yoğundur ve devre dışı bırakıldığında daha az kararlı olabilir. Bunu yalnızca geliştirme için kullanmalısınız. Ayrıca `127.0.0.1` IP adresini dinler, bu makinenizin yalnızca kendisiyle iletişim kurması için kullanılan IP'dir (`localhost`).

## `fastapi run`

`fastapi run` çalıştırmak, FastAPI'yi varsayılan olarak üretim modunda başlatır.

Varsayılan olarak, **otomatik yeniden yükleme** devre dışıdır. Ayrıca `0.0.0.0` IP adresini dinler, yani tüm kullanılabilir IP adreslerini, bu şekilde makineyle iletişim kurabilen herkes tarafından genel olarak erişilebilir olacaktır. Bu, onu normalde üretimde, örneğin bir konteynerde çalıştırma şeklinizdir.

Çoğu durumda, üstünüzde HTTPS'yi sizin için yöneten bir "sonlandırma proxy'si" olur (ve olmalıdır), bu uygulamanızı nasıl dağıttığınıza bağlı olacaktır, sağlayıcınız bunu sizin için yapabilir veya kendiniz kurmanız gerekebilir.

/// tip

Bunu [yayınlama belgelerinde](deployment/index.md){.internal-link target=_blank} daha fazla öğrenebilirsiniz.

///
