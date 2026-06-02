# Öğretici - Kullanıcı Kılavuzu

Bu öğretici, **FastAPI**'nin çoğu özelliğini adım adım nasıl kullanacağınızı gösterir.

Her bölüm kademeli olarak önceki bölümlerin üzerine inşa edilir, ancak konuları ayıracak şekilde yapılandırılmıştır, böylece belirli API ihtiyaçlarınızı çözmek için doğrudan herhangi bir konuya gidebilirsiniz.

Ayrıca gelecekte referans olarak kullanılmak üzere tasarlanmıştır, böylece geri dönüp tam olarak neye ihtiyacınız olduğunu görebilirsiniz.

## Kodu çalıştırın

Tüm kod blokları kopyalanabilir ve doğrudan kullanılabilir (bunlar aslında test edilmiş Python dosyalarıdır).

Herhangi bir örneği çalıştırmak için kodu `main.py` dosyasına kopyalayın ve `fastapi dev` ile başlatın:

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

Kodu yazmanız veya kopyalamanız, düzenlemeniz ve yerel olarak çalıştırmanız **ŞİDDETLE tavsiye edilir**.

Editörünüzde kullanmak, FastAPI'nin gerçek faydalarını gösterir; ne kadar az kod yazmanız gerektiğini, tüm tip kontrollerini, otomatik tamamlamayı vb. görebilirsiniz.

---

## FastAPI'yi yükleyin

İlk adım FastAPI'yi yüklemektir.

Bir [sanal ortam](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden ve ardından **FastAPI'yi yüklediğinizden** emin olun:

<div class="termy">

```console
$ pip install "fastapi[standard]"

---> 100%
```

</div>

/// note

`pip install "fastapi[standard]"` ile yüklediğinizde, bazı varsayılan isteğe bağlı standart bağımlılıklarla birlikte gelir.

Bu isteğe bağlı bağımlılıkları istemiyorsanız, bunun yerine `pip install fastapi` ile yükleyebilirsiniz.

///

## Gelişmiş Kullanıcı Kılavuzu

Bu **Öğretici - Kullanıcı Kılavuzu**'ndan sonra okuyabileceğiniz bir **Gelişmiş Kullanıcı Kılavuzu** da vardır.

**Gelişmiş Kullanıcı Kılavuzu** bu kılavuzun üzerine inşa edilir, aynı kavramları kullanır ve size bazı ek özellikler öğretir.

Ancak önce **Öğretici - Kullanıcı Kılavuzu**'nu (şu anda okuduğunuz) okumalısınız.

Sadece **Öğretici - Kullanıcı Kılavuzu** ile eksiksiz bir uygulama oluşturabilecek ve ardından **Gelişmiş Kullanıcı Kılavuzu**'ndaki ek fikirlerden bazılarını kullanarak ihtiyaçlarınıza göre farklı şekillerde genişletebilecek şekilde tasarlanmıştır.
