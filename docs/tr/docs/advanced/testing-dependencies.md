# Geçersiz Kılmalarla Bağımlılıkları Test Etme

## Test sırasında bağımlılıkları geçersiz kılma

Test sırasında bir bağımlılığı geçersiz kılmak isteyebileceğiniz bazı senaryolar vardır.

Orijinal bağımlılığın (ve sahip olabileceği alt bağımlılıkların hiçbirinin) çalışmasını istemezsiniz.

Bunun yerine, yalnızca testler sırasında (muhtemelen yalnızca bazı belirli testlerde) kullanılacak ve orijinal bağımlılığın değerinin kullanıldığı yerde kullanılabilecek bir değer sağlayacak farklı bir bağımlılık sağlamak istiyorsunuz.

### Kullanım senaryoları: harici servis

Bir örnek, çağırmanız gereken harici bir kimlik doğrulama sağlayıcınız olabilir.

Ona bir token gönderirsiniz ve kimliği doğrulanmış bir kullanıcı döndürür.

Bu sağlayıcı istek başına ücret alıyor olabilir ve onu çağırmak, testler için sabit bir sahte kullanıcıya sahip olmanızdan daha fazla zaman alabilir.

Muhtemelen harici sağlayıcıyı bir kez test etmek istiyorsunuz, ancak çalışan her test için mutlaka çağırmak istemezsiniz.

Bu durumda, o sağlayıcıyı çağıran bağımlılığı geçersiz kılabilir ve yalnızca testleriniz için sahte bir kullanıcı döndüren özel bir bağımlılık kullanabilirsiniz.

### `app.dependency_overrides` niteliğini kullanın

Bu durumlar için, **FastAPI** uygulamanızda basit bir `dict` olan `app.dependency_overrides` niteliği vardır.

Test için bir bağımlılığı geçersiz kılmak üzere, anahtar olarak orijinal bağımlılığı (bir fonksiyon) ve değer olarak bağımlılık geçersiz kılmanızı (başka bir fonksiyon) koyarsınız.

Ve ardından **FastAPI**, orijinal bağımlılık yerine o geçersiz kılmayı çağıracaktır.

{* ../../docs_src/dependency_testing/tutorial001_an_py310.py hl[26:27,30] *}

/// tip

**FastAPI** uygulamanızda herhangi bir yerde kullanılan bir bağımlılık için geçersiz kılma ayarlayabilirsiniz.

Orijinal bağımlılık bir *yol operasyonu fonksiyonunda*, bir *yol operasyonu dekoratöründe* (dönüş değerini kullanmadığınızda), bir `.include_router()` çağrısında vb. kullanılmış olabilir.

FastAPI yine de onu geçersiz kılabilecektir.

///

Ardından `app.dependency_overrides`'ı boş bir `dict` olarak ayarlayarak geçersiz kılmalarınızı sıfırlayabilirsiniz (kaldırabilirsiniz):

```Python
app.dependency_overrides = {}
```

/// tip

Bir bağımlılığı yalnızca bazı testler sırasında geçersiz kılmak istiyorsanız, testin başında (test fonksiyonunun içinde) geçersiz kılmayı ayarlayabilir ve sonunda (test fonksiyonunun sonunda) sıfırlayabilirsiniz.

///
