# GraphQL

**FastAPI**, **ASGI** standardına dayandığından, ASGI ile de uyumlu herhangi bir **GraphQL** kütüphanesini entegre etmek çok kolaydır.

Normal FastAPI *yol operasyonlarını* GraphQL ile aynı uygulamada birleştirebilirsiniz.

/// tip

**GraphQL** çok spesifik kullanım durumlarını çözer.

Yaygın **web API'leriyle** karşılaştırıldığında **avantajları** ve **dezavantajları** vardır.

Kullanım durumunuz için **faydaların** **dezavantajları** telafi edip etmediğini değerlendirdiğinizden emin olun. 🤓

///

## GraphQL Kütüphaneleri

İşte **ASGI** desteğine sahip bazı **GraphQL** kütüphaneleri. Bunları **FastAPI** ile kullanabilirsiniz:

* <a href="https://strawberry.rocks/" class="external-link" target="_blank">Strawberry</a> 🍓
    * <a href="https://strawberry.rocks/docs/integrations/fastapi" class="external-link" target="_blank">FastAPI için belgeleriyle</a>
* <a href="https://ariadnegraphql.org/" class="external-link" target="_blank">Ariadne</a>
    * <a href="https://ariadnegraphql.org/docs/fastapi-integration" class="external-link" target="_blank">FastAPI için belgeleriyle</a>
* <a href="https://tartiflette.io/" class="external-link" target="_blank">Tartiflette</a>
    * ASGI entegrasyonu sağlayan <a href="https://tartiflette.github.io/tartiflette-asgi/" class="external-link" target="_blank">Tartiflette ASGI</a> ile
* <a href="https://graphene-python.org/" class="external-link" target="_blank">Graphene</a>
    * <a href="https://github.com/ciscorn/starlette-graphene3" class="external-link" target="_blank">starlette-graphene3</a> ile

## Strawberry ile GraphQL

**GraphQL** ile çalışmanız gerekiyorsa veya istiyorsanız, <a href="https://strawberry.rocks/" class="external-link" target="_blank">**Strawberry**</a> **önerilen** kütüphanedir çünkü **FastAPI'nin** tasarımına en yakın tasarıma sahiptir, hepsi **tür açıklamalarına** dayanır.

Kullanım durumunuza bağlı olarak, farklı bir kütüphaneyi tercih edebilirsiniz, ama bana sorarsanız, muhtemelen **Strawberry**'yi denemenizi öneririm.

İşte Strawberry'yi FastAPI ile nasıl entegre edebileceğinize dair küçük bir önizleme:

{* ../../docs_src/graphql/tutorial001.py hl[3,22,25] *}

Strawberry hakkında daha fazla bilgiyi <a href="https://strawberry.rocks/" class="external-link" target="_blank">Strawberry belgelerinde</a> bulabilirsiniz.

Ve ayrıca <a href="https://strawberry.rocks/docs/integrations/fastapi" class="external-link" target="_blank">Strawberry ile FastAPI</a> hakkındaki belgeleri de inceleyebilirsiniz.

## Starlette'den Eski `GraphQLApp`

Starlette'in önceki sürümleri <a href="https://graphene-python.org/" class="external-link" target="_blank">Graphene</a> ile entegrasyon için bir `GraphQLApp` sınıfı içeriyordu.

Starlette'den kullanımdan kaldırıldı, ama onu kullanan kodunuz varsa, aynı kullanım durumunu kapsayan ve **neredeyse aynı arayüze** sahip <a href="https://github.com/ciscorn/starlette-graphene3" class="external-link" target="_blank">starlette-graphene3</a>'e kolayca **geçiş** yapabilirsiniz.

/// tip

GraphQL'e ihtiyacınız varsa, özel sınıflar ve türler yerine tür açıklamalarına dayandığından <a href="https://strawberry.rocks/" class="external-link" target="_blank">Strawberry</a>'ye göz atmanızı yine de öneririm.

///

## Daha Fazla Bilgi

**GraphQL** hakkında daha fazla bilgiyi <a href="https://graphql.org/" class="external-link" target="_blank">resmi GraphQL belgelerinde</a> öğrenebilirsiniz.

Ayrıca yukarıda açıklanan kütüphanelerin her biri hakkında bağlantılarından daha fazla bilgi edinebilirsiniz.
