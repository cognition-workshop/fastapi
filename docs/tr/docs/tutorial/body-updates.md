# Gövde - Güncellemeler

## `PUT` ile değiştirerek güncelleme

Bir öğeyi güncellemek için <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT" class="external-link" target="_blank">HTTP `PUT`</a> işlemini kullanabilirsiniz.

Girdi verisini JSON olarak saklanabilecek veriye dönüştürmek için `jsonable_encoder`'ı kullanabilirsiniz (örneğin bir NoSQL veritabanı ile). Örneğin, `datetime`'ı `str`'ye dönüştürme.

{* ../../docs_src/body_updates/tutorial001_py310.py hl[28:33] *}

`PUT`, mevcut veriyi değiştirecek veriyi almak için kullanılır.

### Değiştirme uyarısı

Bu, `bar` öğesini `PUT` kullanarak şu gövdeyle güncellemek istediğinizde:

```Python
{
    "name": "Barz",
    "price": 3,
    "description": None,
}
```

zaten kayıtlı olan `"tax": 20.2` niteliğini içermediğinden, girdi modeli `"tax": 10.5` varsayılan değerini alacaktır.

Ve veri bu "yeni" `tax` değeri olan `10.5` ile kaydedilecektir.

## `PATCH` ile kısmi güncellemeler

Veriyi *kısmen* güncellemek için <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH" class="external-link" target="_blank">HTTP `PATCH`</a> işlemini de kullanabilirsiniz.

Bu, yalnızca güncellemek istediğiniz veriyi gönderebileceğiniz, geri kalanını olduğu gibi bırakabileceğiniz anlamına gelir.

/// note

`PATCH`, `PUT`'tan daha az yaygın kullanılır ve bilinir.

Ve birçok takım, kısmi güncellemeler için bile yalnızca `PUT` kullanır.

Bunları istediğiniz gibi kullanmakta **özgürsünüz**, **FastAPI** herhangi bir kısıtlama getirmez.

Ancak bu kılavuz, az çok nasıl kullanılmaları gerektiğini gösterir.

///

### Pydantic'in `exclude_unset` parametresini kullanma

Kısmi güncellemeler almak istiyorsanız, Pydantic'in modelinin `.model_dump()` metodundaki `exclude_unset` parametresini kullanmak çok yararlıdır.

`item.model_dump(exclude_unset=True)` gibi.

/// info

Pydantic v1'de metot `.dict()` olarak adlandırılıyordu, Pydantic v2'de kullanımdan kaldırıldı (ancak hâlâ destekleniyor) ve `.model_dump()` olarak yeniden adlandırıldı.

Buradaki örnekler Pydantic v1 ile uyumluluk için `.dict()` kullanır, ancak Pydantic v2 kullanabiliyorsanız bunun yerine `.model_dump()` kullanmalısınız.

///

Bu, `item` modeli oluşturulurken yalnızca ayarlanan verilerle bir `dict` üretecek, varsayılan değerleri hariç tutacaktır.

Ardından bunu, yalnızca ayarlanan (istekte gönderilen) verilerle, varsayılan değerleri atlayarak bir `dict` oluşturmak için kullanabilirsiniz:

{* ../../docs_src/body_updates/tutorial002_py310.py hl[32] *}

### Pydantic'in `update` parametresini kullanma

Şimdi, `.model_copy()` kullanarak mevcut modelin bir kopyasını oluşturabilir ve güncellenecek verileri içeren bir `dict` ile `update` parametresini iletebilirsiniz.

/// info

Pydantic v1'de metot `.copy()` olarak adlandırılıyordu, Pydantic v2'de kullanımdan kaldırıldı (ancak hâlâ destekleniyor) ve `.model_copy()` olarak yeniden adlandırıldı.

Buradaki örnekler Pydantic v1 ile uyumluluk için `.copy()` kullanır, ancak Pydantic v2 kullanabiliyorsanız bunun yerine `.model_copy()` kullanmalısınız.

///

`stored_item_model.model_copy(update=update_data)` gibi:

{* ../../docs_src/body_updates/tutorial002_py310.py hl[33] *}

### Kısmi güncellemeler özeti

Özetle, kısmi güncellemeler uygulamak için:

* (İsteğe bağlı olarak) `PUT` yerine `PATCH` kullanın.
* Kayıtlı veriyi alın.
* Bu veriyi bir Pydantic modeline koyun.
* Girdi modelinden varsayılan değerler olmadan bir `dict` oluşturun (`exclude_unset` kullanarak).
    * Bu şekilde, modelinizdeki varsayılan değerlerle zaten kayıtlı değerleri geçersiz kılmak yerine, yalnızca kullanıcı tarafından gerçekten ayarlanan değerleri güncelleyebilirsiniz.
* Kayıtlı modelin bir kopyasını oluşturun, niteliklerini alınan kısmi güncellemelerle güncelleyin (`update` parametresini kullanarak).
* Kopyalanan modeli veritabanınızda saklanabilecek bir şeye dönüştürün (örneğin, `jsonable_encoder` kullanarak).
    * Bu, modelin `.model_dump()` metodunu tekrar kullanmaya benzer, ancak değerlerin JSON'a dönüştürülebilecek veri tiplerine dönüştürüldüğünden (ve dönüştürdüğünden) emin olur, örneğin `datetime`'ı `str`'ye.
* Veriyi veritabanınıza kaydedin.
* Güncellenen modeli döndürün.

{* ../../docs_src/body_updates/tutorial002_py310.py hl[28:35] *}

/// tip

Aslında aynı tekniği bir HTTP `PUT` işlemiyle de kullanabilirsiniz.

Ancak buradaki örnek `PATCH` kullanır çünkü bu kullanım durumları için oluşturulmuştur.

///

/// note

Girdi modelinin hâlâ doğrulandığına dikkat edin.

Bu nedenle, tüm nitelikleri atlayabilecek kısmi güncellemeler almak istiyorsanız, tüm niteliklerin isteğe bağlı olarak işaretlendiği (varsayılan değerler veya `None` ile) bir modele sahip olmanız gerekir.

**Güncellemeler** için tüm isteğe bağlı değerlere sahip modellerle **oluşturma** için zorunlu değerlere sahip modelleri ayırt etmek için [Ekstra Modeller](extra-models.md){.internal-link target=_blank} bölümünde açıklanan fikirleri kullanabilirsiniz.

///
