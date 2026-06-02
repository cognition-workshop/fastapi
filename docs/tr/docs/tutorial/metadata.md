# Meta Veriler ve Belge URL'leri

**FastAPI** uygulamanızda birçok meta veri yapılandırmasını özelleştirebilirsiniz.

## API için Meta Veriler

OpenAPI spesifikasyonunda ve otomatik API belgeleri arayüzlerinde kullanılan aşağıdaki alanları ayarlayabilirsiniz:

| Parametre | Tip | Açıklama |
|------------|------|-------------|
| `title` | `str` | API'nin başlığı. |
| `summary` | `str` | API'nin kısa bir özeti. <small>OpenAPI 3.1.0, FastAPI 0.99.0'dan beri mevcuttur.</small> |
| `description` | `str` | API'nin kısa bir açıklaması. Markdown kullanabilir. |
| `version` | `string` | API'nin sürümü. Bu, OpenAPI'nin değil, kendi uygulamanızın sürümüdür. Örneğin `2.5.0`. |
| `terms_of_service` | `str` | API'nin Hizmet Şartları URL'si. Sağlanırsa, bu bir URL olmalıdır. |
| `contact` | `dict` | Sunulan API için iletişim bilgileri. Birkaç alan içerebilir. <details><summary><code>contact</code> alanları</summary><table><thead><tr><th>Parametre</th><th>Tip</th><th>Açıklama</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>str</code></td><td>İletişim kişisinin/kuruluşunun tanımlayıcı adı.</td></tr><tr><td><code>url</code></td><td><code>str</code></td><td>İletişim bilgilerine yönlendiren URL. URL formatında OLMALIDIR.</td></tr><tr><td><code>email</code></td><td><code>str</code></td><td>İletişim kişisinin/kuruluşunun e-posta adresi. E-posta adresi formatında OLMALIDIR.</td></tr></tbody></table></details> |
| `license_info` | `dict` | Sunulan API için lisans bilgileri. Birkaç alan içerebilir. <details><summary><code>license_info</code> alanları</summary><table><thead><tr><th>Parametre</th><th>Tip</th><th>Açıklama</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>str</code></td><td><strong>GEREKLİ</strong> (<code>license_info</code> ayarlandıysa). API için kullanılan lisans adı.</td></tr><tr><td><code>identifier</code></td><td><code>str</code></td><td>API için bir <a href="https://spdx.org/licenses/" class="external-link" target="_blank">SPDX</a> lisans ifadesi. <code>identifier</code> alanı <code>url</code> alanı ile karşılıklı olarak birbirini dışlar. <small>OpenAPI 3.1.0, FastAPI 0.99.0'dan beri mevcuttur.</small></td></tr><tr><td><code>url</code></td><td><code>str</code></td><td>API için kullanılan lisansın URL'si. URL formatında OLMALIDIR.</td></tr></tbody></table></details> |

Bunları şu şekilde ayarlayabilirsiniz:

{* ../../docs_src/metadata/tutorial001.py hl[3:16, 19:32] *}

/// tip

`description` alanında Markdown yazabilirsiniz ve çıktıda işlenecektir.

///

Bu yapılandırma ile otomatik API belgeleri şöyle görünecektir:

<img src="/img/tutorial/metadata/image01.png">

## Lisans tanımlayıcısı

OpenAPI 3.1.0 ve FastAPI 0.99.0'dan beri, `license_info`'yu bir `url` yerine bir `identifier` ile de ayarlayabilirsiniz.

Örneğin:

{* ../../docs_src/metadata/tutorial001_1.py hl[31] *}

## Etiketler için meta veriler

Yol operasyonlarınızı gruplandırmak için kullanılan farklı etiketler için `openapi_tags` parametresiyle ek meta veriler de ekleyebilirsiniz.

Her etiket için bir sözlük içeren bir liste alır.

Her sözlük şunları içerebilir:

* `name` (**gerekli**): *yol operasyonlarınızdaki* ve `APIRouter`'larınızdaki `tags` parametresinde kullandığınız aynı etiket adına sahip bir `str`.
* `description`: etiket için kısa bir açıklama içeren bir `str`. Markdown içerebilir ve belge arayüzünde gösterilecektir.
* `externalDocs`: harici belgeleri açıklayan bir `dict`:
    * `description`: harici belgeler için kısa bir açıklama içeren bir `str`.
    * `url` (**gerekli**): harici belgelerin URL'sini içeren bir `str`.

### Etiketler için meta veri oluşturma

`users` ve `items` için etiketlerle bir örnekte deneyelim.

Etiketleriniz için meta veri oluşturun ve bunu `openapi_tags` parametresine iletin:

{* ../../docs_src/metadata/tutorial004.py hl[3:16,18] *}

Açıklamaların içinde Markdown kullanabileceğinize dikkat edin, örneğin "login" kalın (**login**) ve "fancy" italik (_fancy_) gösterilecektir.

/// tip

Kullandığınız tüm etiketler için meta veri eklemeniz gerekmez.

///

### Etiketlerinizi kullanın

*Yol operasyonlarınız* (ve `APIRouter`'larınız) ile `tags` parametresini kullanarak onları farklı etiketlere atayın:

{* ../../docs_src/metadata/tutorial004.py hl[21,26] *}

/// info

Etiketler hakkında daha fazla bilgiyi [Yol Operasyonu Yapılandırması](path-operation-configuration.md#tags){.internal-link target=_blank} bölümünde okuyun.

///

### Belgeleri kontrol edin

Şimdi, belgeleri kontrol ederseniz, tüm ek meta verileri gösterecektir:

<img src="/img/tutorial/metadata/image02.png">

### Etiketlerin sırası

Her etiket meta verisi sözlüğünün sırası, belge arayüzünde gösterilen sırayı da tanımlar.

Örneğin, `users` alfabetik sırada `items`'tan sonra gelse de, meta verilerini listedeki ilk sözlük olarak eklediğimiz için onlardan önce gösterilir.

## OpenAPI URL'si

Varsayılan olarak, OpenAPI şeması `/openapi.json` adresinde sunulur.

Ancak bunu `openapi_url` parametresiyle yapılandırabilirsiniz.

Örneğin, `/api/v1/openapi.json` adresinde sunulmasını ayarlamak için:

{* ../../docs_src/metadata/tutorial002.py hl[3] *}

OpenAPI şemasını tamamen devre dışı bırakmak istiyorsanız `openapi_url=None` ayarlayabilirsiniz, bu da onu kullanan belge kullanıcı arayüzlerini de devre dışı bırakacaktır.

## Belge URL'leri

Dahil edilen iki belge kullanıcı arayüzünü yapılandırabilirsiniz:

* **Swagger UI**: `/docs` adresinde sunulur.
    * URL'sini `docs_url` parametresiyle ayarlayabilirsiniz.
    * `docs_url=None` ayarlayarak devre dışı bırakabilirsiniz.
* **ReDoc**: `/redoc` adresinde sunulur.
    * URL'sini `redoc_url` parametresiyle ayarlayabilirsiniz.
    * `redoc_url=None` ayarlayarak devre dışı bırakabilirsiniz.

Örneğin, Swagger UI'ı `/documentation` adresinde sunulacak şekilde ayarlamak ve ReDoc'u devre dışı bırakmak için:

{* ../../docs_src/metadata/tutorial003.py hl[3] *}
