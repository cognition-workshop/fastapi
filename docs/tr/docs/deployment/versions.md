# FastAPI sürümleri hakkında

**FastAPI** zaten birçok uygulama ve sistemde üretimde kullanılmaktadır. Ve test kapsamı %100'de tutulmaktadır. Ama gelişimi hala hızlı bir şekilde devam etmektedir.

Yeni özellikler sık sık eklenir, hatalar düzenli olarak düzeltilir ve kod sürekli olarak iyileştirilmektedir.

Bu yüzden mevcut sürümler hala `0.x.x`'tir, bu her sürümün potansiyel olarak uyumsuz değişiklikler içerebileceğini yansıtır. Bu, <a href="https://semver.org/" class="external-link" target="_blank">Semantic Versioning</a> kurallarını takip eder.

Şu anda **FastAPI** ile üretim uygulamaları oluşturabilirsiniz (ve muhtemelen bir süredir yapıyorsunuz da), sadece kodunuzun geri kalanıyla doğru şekilde çalışan bir sürüm kullandığınızdan emin olmanız gerekir.

## `fastapi` sürümünüzü sabitleyin

Yapmanız gereken ilk şey, kullandığınız **FastAPI** sürümünü uygulamanız için doğru çalıştığını bildiğiniz belirli en son sürüme "sabitlemek"tir.

Örneğin, uygulamanızda `0.112.0` sürümünü kullandığınızı varsayalım.

Bir `requirements.txt` dosyası kullanıyorsanız sürümü şöyle belirtebilirsiniz:

```txt
fastapi[standard]==0.112.0
```

bu, tam olarak `0.112.0` sürümünü kullanacağınız anlamına gelir.

Veya şöyle de sabitleyebilirsiniz:

```txt
fastapi[standard]>=0.112.0,<0.113.0
```

bu, `0.112.0` ve üstü ama `0.113.0`'dan düşük sürümleri kullanacağınız anlamına gelir, örneğin `0.112.2` sürümü yine de kabul edilecektir.

Yüklemelerinizi yönetmek için `uv`, Poetry, Pipenv veya diğerleri gibi başka bir araç kullanıyorsanız, hepsinin paketleriniz için belirli sürümleri tanımlayabileceğiniz bir yolu vardır.

## Mevcut sürümler

Mevcut sürümleri (örneğin geçerli en son sürümü kontrol etmek için) [Sürüm Notları](../release-notes.md){.internal-link target=_blank}'nda görebilirsiniz.

## Sürümler hakkında

Semantic Versioning kurallarını takip ederek, `1.0.0`'ın altındaki herhangi bir sürüm potansiyel olarak uyumsuz değişiklikler ekleyebilir.

FastAPI ayrıca herhangi bir "PATCH" sürüm değişikliğinin hata düzeltmeleri ve uyumsuz olmayan değişiklikler için olduğu kuralını da takip eder.

/// tip

"PATCH" son sayıdır, örneğin `0.2.3`'te PATCH sürümü `3`'tür.

///

Bu yüzden, şöyle bir sürüme sabitleyebilmeniz gerekir:

```txt
fastapi>=0.45.0,<0.46.0
```

Uyumsuz değişiklikler ve yeni özellikler "MINOR" sürümlerde eklenir.

/// tip

"MINOR" ortadaki sayıdır, örneğin `0.2.3`'te MINOR sürümü `2`'dir.

///

## FastAPI sürümlerini yükseltme

Uygulamanız için testler eklemelisiniz.

**FastAPI** ile bu çok kolaydır (Starlette sayesinde), belgeleri kontrol edin: [Test Etme](../tutorial/testing.md){.internal-link target=_blank}

Testleriniz olduktan sonra, **FastAPI** sürümünü daha yeni bir sürüme yükseltebilir ve testlerinizi çalıştırarak tüm kodunuzun doğru çalıştığından emin olabilirsiniz.

Her şey çalışıyorsa veya gerekli değişiklikleri yaptıktan sonra ve tüm testleriniz geçiyorsa, `fastapi`'nizi o yeni güncel sürüme sabitleyebilirsiniz.

## Starlette hakkında

`starlette`'in sürümünü sabitlememelisiniz.

**FastAPI**'nin farklı sürümleri Starlette'in belirli bir daha yeni sürümünü kullanacaktır.

Bu yüzden, **FastAPI**'nin doğru Starlette sürümünü kullanmasına izin verebilirsiniz.

## Pydantic hakkında

Pydantic, **FastAPI** için testleri kendi testleriyle birlikte içerir, bu yüzden Pydantic'in yeni sürümleri (`1.0.0`'ın üstündeki) her zaman FastAPI ile uyumludur.

Pydantic'i sizin için çalışan `1.0.0`'ın üstündeki herhangi bir sürüme sabitleyebilirsiniz.

Örneğin:

```txt
pydantic>=2.7.0,<3.0.0
```
