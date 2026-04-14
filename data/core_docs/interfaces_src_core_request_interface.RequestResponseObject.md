# Interface RequestResponseObject<D>
### Type parameters

* #### D = unknown

### Hierarchy

* RequestResponseObject

## Index

### Properties

* [cache](src_core_request_interface.RequestResponseObject.html#cache)
* [ctx](src_core_request_interface.RequestResponseObject.html#ctx)
* [data](src_core_request_interface.RequestResponseObject.html#data)
* [emitter](src_core_request_interface.RequestResponseObject.html#emitter)
* [response](src_core_request_interface.RequestResponseObject.html#response)
* [stream](src_core_request_interface.RequestResponseObject.html#stream)

### Methods

* [[asyncIterator]](src_core_request_interface.RequestResponseObject.html#_asyncIterator_)
* [dropCache](src_core_request_interface.RequestResponseObject.html#dropCache)

## Properties

### Optional cache

cache?: [CacheType](../modules/src_core_request_interface.html#CacheType)

* Defined in [src/core/request/interface.ts:141](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L141)

### ctx

ctx: Readonly<[default](../classes/src_core_request_modules_context.default.html)<D>>

* Defined in [src/core/request/interface.ts:132](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L132)

### data

data: Promise<[Nullable](../modules/index.html#Nullable)<D>>

* Defined in [src/core/request/interface.ts:135](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L135)

### emitter

emitter: EventEmitter2

* Defined in [src/core/request/interface.ts:138](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L138)

### response

response: [default](../classes/src_core_request_response.default.html)<D>

* Defined in [src/core/request/interface.ts:133](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L133)

### stream

stream: AsyncIterableIterator<unknown>

* Defined in [src/core/request/interface.ts:136](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L136)

## Methods

### [asyncIterator]

* [asyncIterator](): AsyncIterableIterator<[RequestResponseChunk](src_core_request_interface.RequestResponseChunk.html)>

* + Defined in [src/core/request/interface.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L139)

  #### Returns AsyncIterableIterator<[RequestResponseChunk](src_core_request_interface.RequestResponseChunk.html)>

### dropCache

* dropCache(): void

* + Defined in [src/core/request/interface.ts:142](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L142)

  #### Returns void