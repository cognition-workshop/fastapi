# Statik Dosyalar

`StaticFiles` kullanarak bir dizinden statik dosyaları otomatik olarak sunabilirsiniz.

## `StaticFiles` Kullanımı

* `StaticFiles`'ı içe aktarın.
* Belirli bir yola bir `StaticFiles()` örneğini "bağlayın".

{* ../../docs_src/static_files/tutorial001.py hl[2,6] *}

/// note | Teknik Detaylar

`from starlette.staticfiles import StaticFiles` ifadesini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için aynı `starlette.staticfiles`'ı `fastapi.staticfiles` olarak sunar. Ancak aslında doğrudan Starlette'ten gelir.

///

### "Bağlama" nedir

"Bağlama", belirli bir yola tamamen "bağımsız" bir uygulama eklemek anlamına gelir ve ardından tüm alt yolların işlenmesiyle ilgilenir.

Bu, bağlanmış bir uygulama tamamen bağımsız olduğu için `APIRouter` kullanmaktan farklıdır. Ana uygulamanızın OpenAPI ve belgeleri, bağlanmış uygulamadan hiçbir şey içermeyecektir, vb.

Bununla ilgili daha fazla bilgiyi [Gelişmiş Kullanıcı Kılavuzu](../advanced/index.md){.internal-link target=_blank}'nda okuyabilirsiniz.

## Detaylar

İlk `"/static"`, bu "alt uygulamanın" "bağlanacağı" alt yolu ifade eder. Bu nedenle, `"/static"` ile başlayan herhangi bir yol onun tarafından işlenecektir.

`directory="static"`, statik dosyalarınızı içeren dizinin adını ifade eder.

`name="static"`, **FastAPI** tarafından dahili olarak kullanılabilecek bir ad verir.

Tüm bu parametreler "`static`"ten farklı olabilir, bunları kendi uygulamanızın ihtiyaçlarına ve özel detaylarına göre ayarlayın.

## Daha fazla bilgi

Daha fazla detay ve seçenek için <a href="https://www.starlette.io/staticfiles/" class="external-link" target="_blank">Starlette'in Statik Dosyalar belgelerine</a> bakın.
