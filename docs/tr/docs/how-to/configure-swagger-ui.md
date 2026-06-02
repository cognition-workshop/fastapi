# Swagger UI'ı Yapılandırma

Bazı ek <a href="https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/" class="external-link" target="_blank">Swagger UI parametrelerini</a> yapılandırabilirsiniz.

Bunları yapılandırmak için, `FastAPI()` uygulama nesnesini oluştururken veya `get_swagger_ui_html()` fonksiyonuna `swagger_ui_parameters` argümanını geçirin.

`swagger_ui_parameters`, yapılandırmaları doğrudan Swagger UI'a iletilen bir sözlük alır.

FastAPI, yapılandırmaları JavaScript ile uyumlu hale getirmek için **JSON**'a dönüştürür, çünkü Swagger UI'ın ihtiyacı budur.

## Söz Dizimi Vurgulamayı Devre Dışı Bırakma

Örneğin, Swagger UI'da söz dizimi vurgulamayı devre dışı bırakabilirsiniz.

Ayarları değiştirmeden, söz dizimi vurgulaması varsayılan olarak etkindir:

<img src="/img/tutorial/extending-openapi/image02.png">

Ama `syntaxHighlight`'ı `False` olarak ayarlayarak devre dışı bırakabilirsiniz:

{* ../../docs_src/configure_swagger_ui/tutorial001.py hl[3] *}

...ve Swagger UI artık söz dizimi vurgulamasını göstermeyecektir:

<img src="/img/tutorial/extending-openapi/image03.png">

## Temayı Değiştirme

Aynı şekilde, `"syntaxHighlight.theme"` anahtarıyla söz dizimi vurgulama temasını ayarlayabilirsiniz (ortasında bir nokta olduğuna dikkat edin):

{* ../../docs_src/configure_swagger_ui/tutorial002.py hl[3] *}

Bu yapılandırma söz dizimi vurgulama renk temasını değiştirecektir:

<img src="/img/tutorial/extending-openapi/image04.png">

## Varsayılan Swagger UI Parametrelerini Değiştirme

FastAPI, çoğu kullanım durumu için uygun bazı varsayılan yapılandırma parametreleri içerir.

Şu varsayılan yapılandırmaları içerir:

{* ../../fastapi/openapi/docs.py ln[8:23] hl[17:23] *}

`swagger_ui_parameters` argümanında farklı bir değer ayarlayarak bunlardan herhangi birini geçersiz kılabilirsiniz.

Örneğin, `deepLinking`'i devre dışı bırakmak için bu ayarları `swagger_ui_parameters`'a geçirebilirsiniz:

{* ../../docs_src/configure_swagger_ui/tutorial003.py hl[3] *}

## Diğer Swagger UI Parametreleri

Kullanabileceğiniz diğer tüm olası yapılandırmaları görmek için <a href="https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/" class="external-link" target="_blank">Swagger UI parametreleri için resmi belgeleri</a> okuyun.

## Yalnızca JavaScript ayarları

Swagger UI ayrıca diğer yapılandırmaların **yalnızca JavaScript** nesneleri olmasına izin verir (örneğin, JavaScript fonksiyonları).

FastAPI ayrıca bu yalnızca JavaScript `presets` ayarlarını da içerir:

```JavaScript
presets: [
    SwaggerUIBundle.presets.apis,
    SwaggerUIBundle.SwaggerUIStandalonePreset
]
```

Bunlar **JavaScript** nesneleridir, dizeler değil, bu yüzden onları Python kodundan doğrudan geçiremezsiniz.

Bunlar gibi yalnızca JavaScript yapılandırmalarını kullanmanız gerekiyorsa, yukarıdaki yöntemlerden birini kullanabilirsiniz. Tüm Swagger UI *yol operasyonunu* geçersiz kılın ve ihtiyacınız olan herhangi bir JavaScript'i manuel olarak yazın.
