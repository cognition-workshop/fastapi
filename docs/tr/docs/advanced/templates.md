# Şablonlar

**FastAPI** ile istediğiniz herhangi bir şablon motorunu kullanabilirsiniz.

Yaygın bir tercih, Flask ve diğer araçlar tarafından da kullanılan Jinja2'dir.

Doğrudan **FastAPI** uygulamanızda kullanabileceğiniz kolayca yapılandırmak için yardımcı araçlar vardır (Starlette tarafından sağlanır).

## Bağımlılıkları yükleyin

[Sanal ortamınızı](../virtual-environments.md){.internal-link target=_blank} oluşturduğunuzdan, etkinleştirdiğinizden emin olun ve `jinja2`'yi yükleyin:

<div class="termy">

```console
$ pip install jinja2

---> 100%
```

</div>

## `Jinja2Templates` kullanma

* `Jinja2Templates`'i içe aktarın.
* Daha sonra yeniden kullanabileceğiniz bir `templates` nesnesi oluşturun.
* Bir şablon döndürecek *yol operasyonunda* bir `Request` parametresi bildirin.
* Oluşturduğunuz `templates`'i kullanarak bir `TemplateResponse` oluşturun ve döndürün, şablonun adını, istek nesnesini ve Jinja2 şablonunun içinde kullanılacak anahtar-değer çiftleri içeren bir "context" sözlüğü iletin.

{* ../../docs_src/templates/tutorial001.py hl[4,11,15:18] *}

/// note

FastAPI 0.108.0, Starlette 0.29.0'dan önce, `name` ilk parametreydi.

Ayrıca, ondan önce, önceki sürümlerde, `request` nesnesi Jinja2 için context'teki anahtar-değer çiftlerinin bir parçası olarak iletiliyordu.

///

/// tip

`response_class=HTMLResponse` bildirerek belge arayüzü yanıtın HTML olacağını bilecektir.

///

/// note | Teknik Detaylar

`from starlette.templating import Jinja2Templates` de kullanabilirsiniz.

**FastAPI**, geliştirici olarak sizin için bir kolaylık olarak aynı `starlette.templating`'i `fastapi.templating` olarak sağlar. Ancak mevcut yanıtların çoğu doğrudan Starlette'den gelir. `Request` ve `StaticFiles` için de aynı şey geçerlidir.

///

## Şablon yazma

Ardından `templates/item.html` adresinde bir şablon yazabilirsiniz, örneğin:

```jinja hl_lines="7"
{!../../docs_src/templates/templates/item.html!}
```

### Şablon Context Değerleri

Şunu içeren HTML'de:

{% raw %}

```jinja
Item ID: {{ id }}
```

{% endraw %}

...ilettiğiniz "context" `dict`'inden alınan `id`'yi gösterecektir:

```Python
{"id": id}
```

Örneğin, 42 ID'siyle bu şu şekilde oluşturulur:

```html
Item ID: 42
```

### Şablon `url_for` Argümanları

Şablonun içinde `url_for()` de kullanabilirsiniz, *yol operasyonu fonksiyonunuz* tarafından kullanılacak aynı argümanları alır.

Yani, şu bölüm:

{% raw %}

```jinja
<a href="{{ url_for('read_item', id=id) }}">
```

{% endraw %}

...`read_item(id=id)` *yol operasyonu fonksiyonu* tarafından ele alınacak aynı URL'ye bir bağlantı oluşturacaktır.

Örneğin, 42 ID'siyle bu şu şekilde oluşturulur:

```html
<a href="/items/42">
```

## Şablonlar ve statik dosyalar

Şablonun içinde `url_for()` de kullanabilirsiniz ve örneğin `name="static"` ile bağladığınız `StaticFiles` ile kullanabilirsiniz.

```jinja hl_lines="4"
{!../../docs_src/templates/templates/item.html!}
```

Bu örnekte, `static/styles.css` adresindeki bir CSS dosyasına şu şekilde bağlantı verecektir:

```CSS hl_lines="4"
{!../../docs_src/templates/static/styles.css!}
```

Ve `StaticFiles` kullandığınız için, o CSS dosyası **FastAPI** uygulamanız tarafından `/static/styles.css` URL'sinde otomatik olarak sunulacaktır.

## Daha fazla bilgi

Şablonları test etme dahil daha fazla ayrıntı için <a href="https://www.starlette.io/templates/" class="external-link" target="_blank">Starlette'in şablon belgelerine</a> bakın.
