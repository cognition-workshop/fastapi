# Yol Operasyonu Yapılandırması

*Yol operasyonu dekoratörünüze* yapılandırmak için iletebileceğiniz birçok parametre vardır.

/// warning

Bu parametrelerin doğrudan *yol operasyonu dekoratörüne* iletildiğine, *yol operasyonu fonksiyonunuza* değil, dikkat edin.

///

## Yanıt Durum Kodu

*Yol operasyonunuzun* yanıtında kullanılacak (HTTP) `status_code`'u tanımlayabilirsiniz.

Doğrudan `int` kodunu iletebilirsiniz, örneğin `404`.

Ancak her sayı kodunun ne için olduğunu hatırlamıyorsanız, `status`'taki kısayol sabitlerini kullanabilirsiniz:

{* ../../docs_src/path_operation_configuration/tutorial001_py310.py hl[1,15] *}

Bu durum kodu yanıtta kullanılacak ve OpenAPI şemasına eklenecektir.

/// note | Teknik Detaylar

`from starlette import status` ifadesini de kullanabilirsiniz.

**FastAPI**, geliştirici olarak size kolaylık sağlamak için aynı `starlette.status`'ı `fastapi.status` olarak sunar. Ancak doğrudan Starlette'ten gelir.

///

## Etiketler

*Yol operasyonunuza* etiketler ekleyebilirsiniz, `tags` parametresine bir `str` `list`'i iletin (genellikle sadece bir `str`):

{* ../../docs_src/path_operation_configuration/tutorial002_py310.py hl[15,20,25] *}

OpenAPI şemasına eklenecek ve otomatik belge arayüzleri tarafından kullanılacaktır:

<img src="/img/tutorial/path-operation-configuration/image01.png">

### Enum'larla etiketler

Büyük bir uygulamanız varsa, **birkaç etiket** biriktirebilirsiniz ve ilgili *yol operasyonları* için her zaman **aynı etiketi** kullandığınızdan emin olmak istersiniz.

Bu durumlarda, etiketleri bir `Enum`'da saklamak mantıklı olabilir.

**FastAPI** bunu düz stringlerle aynı şekilde destekler:

{* ../../docs_src/path_operation_configuration/tutorial002b.py hl[1,8:10,13,18] *}

## Özet ve açıklama

Bir `summary` ve `description` ekleyebilirsiniz:

{* ../../docs_src/path_operation_configuration/tutorial003_py310.py hl[18:19] *}

## Docstring'den açıklama

Açıklamalar uzun ve birden fazla satırı kapsama eğiliminde olduğundan, *yol operasyonu* açıklamasını fonksiyonun <abbr title="bir fonksiyonun içindeki ilk ifade olarak çok satırlı bir string (herhangi bir değişkene atanmamış), belgelendirme için kullanılır">docstring</abbr>'inde bildirebilirsiniz ve **FastAPI** onu oradan okuyacaktır.

Docstring'de <a href="https://en.wikipedia.org/wiki/Markdown" class="external-link" target="_blank">Markdown</a> yazabilirsiniz, doğru şekilde yorumlanacak ve görüntülenecektir (docstring girintisi dikkate alınarak).

{* ../../docs_src/path_operation_configuration/tutorial004_py310.py hl[17:25] *}

Etkileşimli belgelerde kullanılacaktır:

<img src="/img/tutorial/path-operation-configuration/image02.png">

## Yanıt açıklaması

`response_description` parametresiyle yanıt açıklamasını belirleyebilirsiniz:

{* ../../docs_src/path_operation_configuration/tutorial005_py310.py hl[19] *}

/// info

`response_description`'ın özellikle yanıta, `description`'ın ise genel olarak *yol operasyonuna* atıfta bulunduğuna dikkat edin.

///

/// check

OpenAPI, her *yol operasyonunun* bir yanıt açıklaması gerektirdiğini belirtir.

Bu yüzden, bir tane sağlamazsanız, **FastAPI** otomatik olarak "Başarılı yanıt" mesajı üretecektir.

///

<img src="/img/tutorial/path-operation-configuration/image03.png">

## Bir *yol operasyonunu* kullanımdan kaldırma

Bir *yol operasyonunu* kaldırmadan <abbr title="eskimiş, kullanılması önerilmeyen">kullanımdan kaldırılmış</abbr> olarak işaretlemeniz gerekiyorsa, `deprecated` parametresini iletin:

{* ../../docs_src/path_operation_configuration/tutorial006.py hl[16] *}

Etkileşimli belgelerde açıkça kullanımdan kaldırılmış olarak işaretlenecektir:

<img src="/img/tutorial/path-operation-configuration/image04.png">

Kullanımdan kaldırılmış ve kaldırılmamış *yol operasyonlarının* nasıl göründüğünü kontrol edin:

<img src="/img/tutorial/path-operation-configuration/image05.png">

## Özet

*Yol operasyonu dekoratörlerine* parametreler ileterek *yol operasyonlarınız* için kolayca meta veri yapılandırabilir ve ekleyebilirsiniz.
