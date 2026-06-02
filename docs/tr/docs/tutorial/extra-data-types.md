# Ekstra Veri Tipleri

Şimdiye kadar yaygın veri tiplerini kullanıyordunuz, örneğin:

* `int`
* `float`
* `str`
* `bool`

Ancak daha karmaşık veri tiplerini de kullanabilirsiniz.

Ve şimdiye kadar gördüğünüz aynı özelliklere sahip olmaya devam edeceksiniz:

* Harika editör desteği.
* Gelen isteklerden veri dönüştürme.
* Yanıt verisi için veri dönüştürme.
* Veri doğrulama.
* Otomatik açıklama ve belgelendirme.

## Diğer veri tipleri

Kullanabileceğiniz bazı ek veri tipleri şunlardır:

* `UUID`:
    * Birçok veritabanı ve sistemde ID olarak yaygın olan standart bir "Evrensel Benzersiz Tanımlayıcı".
    * İsteklerde ve yanıtlarda bir `str` olarak temsil edilecektir.
* `datetime.datetime`:
    * Bir Python `datetime.datetime`.
    * İsteklerde ve yanıtlarda ISO 8601 formatında bir `str` olarak temsil edilecektir, örneğin: `2008-09-15T15:53:00+05:00`.
* `datetime.date`:
    * Python `datetime.date`.
    * İsteklerde ve yanıtlarda ISO 8601 formatında bir `str` olarak temsil edilecektir, örneğin: `2008-09-15`.
* `datetime.time`:
    * Bir Python `datetime.time`.
    * İsteklerde ve yanıtlarda ISO 8601 formatında bir `str` olarak temsil edilecektir, örneğin: `14:23:55.003`.
* `datetime.timedelta`:
    * Bir Python `datetime.timedelta`.
    * İsteklerde ve yanıtlarda toplam saniye sayısı olarak `float` şeklinde temsil edilecektir.
    * Pydantic bunu "ISO 8601 zaman farkı kodlaması" olarak da temsil etmeye izin verir, <a href="https://docs.pydantic.dev/latest/concepts/serialization/#custom-serializers" class="external-link" target="_blank">daha fazla bilgi için belgelere bakın</a>.
* `frozenset`:
    * İsteklerde ve yanıtlarda, bir `set` ile aynı şekilde işlenir:
        * İsteklerde, bir liste okunacak, yinelenenler kaldırılacak ve bir `set`'e dönüştürülecektir.
        * Yanıtlarda, `set` bir `list`'e dönüştürülecektir.
        * Oluşturulan şema, `set` değerlerinin benzersiz olduğunu belirtecektir (JSON Schema'nın `uniqueItems` özelliğini kullanarak).
* `bytes`:
    * Standart Python `bytes`.
    * İsteklerde ve yanıtlarda `str` olarak işlenecektir.
    * Oluşturulan şema, bunun `binary` "formatında" bir `str` olduğunu belirtecektir.
* `Decimal`:
    * Standart Python `Decimal`.
    * İsteklerde ve yanıtlarda, bir `float` ile aynı şekilde işlenir.
* Tüm geçerli Pydantic veri tiplerini buradan kontrol edebilirsiniz: <a href="https://docs.pydantic.dev/latest/usage/types/types/" class="external-link" target="_blank">Pydantic veri tipleri</a>.

## Örnek

İşte yukarıdaki tiplerden bazılarını kullanan parametrelere sahip bir örnek *yol operasyonu*.

{* ../../docs_src/extra_data_types/tutorial001_an_py310.py hl[1,3,12:16] *}

Fonksiyon içindeki parametrelerin doğal veri tiplerine sahip olduğuna ve örneğin normal tarih işlemleri yapabildiğinize dikkat edin:

{* ../../docs_src/extra_data_types/tutorial001_an_py310.py hl[18:19] *}
