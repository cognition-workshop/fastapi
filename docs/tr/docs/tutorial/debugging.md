# Hata Ayıklama

Editörünüzde hata ayıklayıcıya bağlanabilirsiniz, örneğin Visual Studio Code veya PyCharm ile.

## `uvicorn`'u çağırın

FastAPI uygulamanızda, `uvicorn`'u doğrudan içe aktarın ve çalıştırın:

{* ../../docs_src/debugging/tutorial001.py hl[1,15] *}

### `__name__ == "__main__"` hakkında

`__name__ == "__main__"`'in asıl amacı, dosyanız şu şekilde çağrıldığında çalıştırılan bazı kodlara sahip olmaktır:

<div class="termy">

```console
$ python myapp.py
```

</div>

ancak başka bir dosya onu içe aktardığında çağrılmaz, örneğin:

```Python
from myapp import app
```

#### Daha fazla detay

Diyelim ki dosyanızın adı `myapp.py`.

Şu şekilde çalıştırırsanız:

<div class="termy">

```console
$ python myapp.py
```

</div>

o zaman Python tarafından otomatik olarak oluşturulan dosyanızdaki dahili `__name__` değişkeni, değer olarak `"__main__"` stringine sahip olacaktır.

Yani, şu bölüm:

```Python
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

çalışacaktır.

---

Bu, o modülü (dosyayı) içe aktarırsanız gerçekleşmez.

Yani, şuna sahip başka bir `importer.py` dosyanız varsa:

```Python
from myapp import app

# Daha fazla kod
```

bu durumda, `myapp.py` içinde otomatik olarak oluşturulan `__name__` değişkeni `"__main__"` değerine sahip olmayacaktır.

Yani, şu satır:

```Python
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

çalıştırılmayacaktır.

/// info

Daha fazla bilgi için <a href="https://docs.python.org/3/library/__main__.html" class="external-link" target="_blank">resmi Python belgelerine</a> bakın.

///

## Kodunuzu hata ayıklayıcınızla çalıştırın

Uvicorn sunucusunu doğrudan kodunuzdan çalıştırdığınız için, Python programınızı (FastAPI uygulamanızı) doğrudan hata ayıklayıcıdan çağırabilirsiniz.

---

Örneğin, Visual Studio Code'da:

* "Debug" paneline gidin.
* "Add configuration..." seçin.
* "Python" seçin.
* "`Python: Current File (Integrated Terminal)`" seçeneğiyle hata ayıklayıcıyı çalıştırın.

Ardından sunucuyu **FastAPI** kodunuzla başlatacak, kesme noktalarınızda duracak vb.

İşte nasıl görünebileceği:

<img src="/img/tutorial/debugging/image01.png">

---

PyCharm kullanıyorsanız:

* "Run" menüsünü açın.
* "Debug..." seçeneğini seçin.
* Ardından bir bağlam menüsü görünür.
* Hata ayıklanacak dosyayı seçin (bu durumda `main.py`).

Ardından sunucuyu **FastAPI** kodunuzla başlatacak, kesme noktalarınızda duracak vb.

İşte nasıl görünebileceği:

<img src="/img/tutorial/debugging/image02.png">
