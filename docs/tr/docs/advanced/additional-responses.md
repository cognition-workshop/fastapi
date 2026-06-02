# OpenAPI'de Ek Yanıtlar

/// warning

Bu oldukça ileri düzey bir konudur.

**FastAPI**'ye yeni başlıyorsanız, buna ihtiyacınız olmayabilir.

///

Ek durum kodları, medya türleri, açıklamalar vb. ile ek yanıtlar bildirebilirsiniz.

Bu ek yanıtlar OpenAPI şemasına dahil edilecektir, böylece API belgelerinde de görüneceklerdir.

Ama bu ek yanıtlar için, durum kodunuz ve içeriğinizle doğrudan `JSONResponse` gibi bir `Response` döndürdüğünüzden emin olmanız gerekir.

## `model` ile ek yanıt

*Yol operasyonu dekoratörlerinize* bir `responses` parametresi iletebilirsiniz.

Bir `dict` alır: anahtarlar her yanıt için durum kodlarıdır (`200` gibi) ve değerler her biri için bilgileri içeren başka `dict`'lerdir.

Bu yanıt `dict`'lerinin her biri, tıpkı `response_model` gibi bir Pydantic modeli içeren `model` anahtarına sahip olabilir.

**FastAPI** o modeli alacak, JSON Şemasını oluşturacak ve OpenAPI'de doğru yere dahil edecektir.

Örneğin, `404` durum kodu ve `Message` Pydantic modeli ile başka bir yanıt bildirmek için şunu yazabilirsiniz:

{* ../../docs_src/additional_responses/tutorial001.py hl[18,22] *}

/// note

`JSONResponse`'u doğrudan döndürmeniz gerektiğini unutmayın.

///

/// info

`model` anahtarı OpenAPI'nin bir parçası değildir.

**FastAPI** oradan Pydantic modelini alacak, JSON Şemasını oluşturacak ve doğru yere koyacaktır.

Doğru yer:

* `content` anahtarında, değeri olarak başka bir JSON nesnesi (`dict`) içeren:
    * Medya türü ile bir anahtar, örneğin `application/json`, değeri olarak başka bir JSON nesnesi içeren:
        * Modelden JSON Şemasına sahip `schema` anahtarı, doğru yer burasıdır.
            * **FastAPI** buraya JSON Şemasını doğrudan dahil etmek yerine OpenAPI'nizdeki başka bir yerdeki global JSON Şemalarına bir referans ekler. Bu şekilde, diğer uygulamalar ve istemciler bu JSON Şemalarını doğrudan kullanabilir, daha iyi kod oluşturma araçları sağlayabilir, vb.

///

Bu *yol operasyonu* için OpenAPI'deki oluşturulan yanıtlar şöyle olacaktır:

```JSON hl_lines="3-12"
{
    "responses": {
        "404": {
            "description": "Additional Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/Message"
                    }
                }
            }
        },
        "200": {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/Item"
                    }
                }
            }
        },
        "422": {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/HTTPValidationError"
                    }
                }
            }
        }
    }
}
```

Şemalar, OpenAPI şeması içindeki başka bir yerde referans alınır:

```JSON hl_lines="4-16"
{
    "components": {
        "schemas": {
            "Message": {
                "title": "Message",
                "required": [
                    "message"
                ],
                "type": "object",
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string"
                    }
                }
            },
            "Item": {
                "title": "Item",
                "required": [
                    "id",
                    "value"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "string"
                    },
                    "value": {
                        "title": "Value",
                        "type": "string"
                    }
                }
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "msg": {
                        "title": "Message",
                        "type": "string"
                    },
                    "type": {
                        "title": "Error Type",
                        "type": "string"
                    }
                }
            },
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        }
                    }
                }
            }
        }
    }
}
```

## Ana yanıt için ek medya türleri

Aynı ana yanıt için farklı medya türleri eklemek üzere aynı `responses` parametresini kullanabilirsiniz.

Örneğin, *yol operasyonunuzun* bir JSON nesnesi (`application/json` medya türüyle) veya bir PNG görüntüsü döndürebileceğini bildirerek `image/png` ek medya türü ekleyebilirsiniz:

{* ../../docs_src/additional_responses/tutorial002.py hl[19:24,28] *}

/// note

Görüntüyü doğrudan bir `FileResponse` kullanarak döndürmeniz gerektiğine dikkat edin.

///

/// info

`responses` parametrenizde açıkça farklı bir medya türü belirtmediğiniz sürece, FastAPI yanıtın ana yanıt sınıfıyla aynı medya türüne sahip olduğunu varsayacaktır (varsayılan `application/json`).

Ancak medya türü olarak `None` belirtilmiş özel bir yanıt sınıfı belirttiyseniz, FastAPI ilişkili bir modele sahip herhangi bir ek yanıt için `application/json` kullanacaktır.

///

## Bilgi birleştirme

`response_model`, `status_code` ve `responses` parametreleri dahil olmak üzere birden fazla yerden yanıt bilgilerini birleştirebilirsiniz.

Varsayılan `200` durum kodunu (veya ihtiyacınız varsa özel bir kodu) kullanarak bir `response_model` bildirebilir ve ardından aynı yanıt için `responses`'da doğrudan OpenAPI şemasında ek bilgiler bildirebilirsiniz.

**FastAPI**, `responses`'dan ek bilgileri tutacak ve modelinizdeki JSON Şemasıyla birleştirecektir.

Örneğin, bir Pydantic modeli kullanan ve özel bir `description`'a sahip `404` durum kodlu bir yanıt bildirebilirsiniz.

Ve `response_model`'inizi kullanan ama özel bir `example` içeren `200` durum kodlu bir yanıt:

{* ../../docs_src/additional_responses/tutorial003.py hl[20:31] *}

Hepsi birleştirilecek ve OpenAPI'nize dahil edilecek ve API belgelerinde gösterilecektir:

<img src="/img/tutorial/additional-responses/image01.png">

## Önceden tanımlanmış ve özel yanıtları birleştirme

Birçok *yol operasyonuna* uygulanan bazı önceden tanımlanmış yanıtlara sahip olmak isteyebilirsiniz, ancak bunları her *yol operasyonu* için gereken özel yanıtlarla birleştirmek isteyebilirsiniz.

Bu durumlarda, bir `dict`'i `**dict_to_unpack` ile "açma" Python tekniğini kullanabilirsiniz:

```Python
old_dict = {
    "old key": "old value",
    "second old key": "second old value",
}
new_dict = {**old_dict, "new key": "new value"}
```

Burada, `new_dict`, `old_dict`'teki tüm anahtar-değer çiftlerini artı yeni anahtar-değer çiftini içerecektir:

```Python
{
    "old key": "old value",
    "second old key": "second old value",
    "new key": "new value",
}
```

Bu tekniği, *yol operasyonlarınızda* bazı önceden tanımlanmış yanıtları yeniden kullanmak ve bunları ek özel yanıtlarla birleştirmek için kullanabilirsiniz.

Örneğin:

{* ../../docs_src/additional_responses/tutorial004.py hl[13:17,26] *}

## OpenAPI yanıtları hakkında daha fazla bilgi

Yanıtlara tam olarak neler dahil edebileceğinizi görmek için OpenAPI spesifikasyonundaki bu bölümlere bakabilirsiniz:

* <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#responses-object" class="external-link" target="_blank">OpenAPI Responses Object</a>, `Response Object`'i içerir.
* <a href="https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#response-object" class="external-link" target="_blank">OpenAPI Response Object</a>, `description`, `headers`, `content` (bunun içinde farklı medya türleri ve JSON Şemaları bildirirsiniz) ve `links` dahil olmak üzere bunlardan herhangi birini `responses` parametrenizdeki her yanıta doğrudan dahil edebilirsiniz.
