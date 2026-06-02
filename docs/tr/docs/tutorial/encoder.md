# JSON Uyumlu Kodlayıcı

Bir veri tipini (Pydantic modeli gibi) JSON ile uyumlu bir şeye (bir `dict`, `list` vb. gibi) dönüştürmeniz gerekebilecek bazı durumlar vardır.

Örneğin, bir veritabanında saklamanız gerekiyorsa.

Bunun için **FastAPI** bir `jsonable_encoder()` fonksiyonu sağlar.

## `jsonable_encoder` kullanımı

Yalnızca JSON uyumlu veri alan bir `fake_db` veritabanınız olduğunu hayal edin.

Örneğin, `datetime` nesnelerini kabul etmez çünkü bunlar JSON ile uyumlu değildir.

Bu yüzden, bir `datetime` nesnesi <a href="https://en.wikipedia.org/wiki/ISO_8601" class="external-link" target="_blank">ISO formatında</a> veriyi içeren bir `str`'ye dönüştürülmelidir.

Aynı şekilde, bu veritabanı bir Pydantic modeli (niteliklere sahip bir nesne) almaz, yalnızca bir `dict` alır.

Bunun için `jsonable_encoder` kullanabilirsiniz.

Bir Pydantic modeli gibi bir nesne alır ve JSON uyumlu bir sürümünü döndürür:

{* ../../docs_src/encoder/tutorial001_py310.py hl[4,21] *}

Bu örnekte, Pydantic modelini bir `dict`'e ve `datetime`'ı bir `str`'ye dönüştürecektir.

Çağırmanın sonucu, Python standart <a href="https://docs.python.org/3/library/json.html#json.dumps" class="external-link" target="_blank">`json.dumps()`</a> ile kodlanabilecek bir şeydir.

JSON formatındaki veriyi içeren büyük bir `str` (string olarak) döndürmez. Değerleri ve alt değerleri JSON ile uyumlu olan bir Python standart veri yapısı (örneğin bir `dict`) döndürür.

/// note

`jsonable_encoder` aslında **FastAPI** tarafından dahili olarak veri dönüştürmek için kullanılır. Ancak birçok başka senaryoda da kullanışlıdır.

///
