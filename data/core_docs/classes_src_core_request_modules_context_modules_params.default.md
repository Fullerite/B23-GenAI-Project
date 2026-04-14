# Class default<D>
### Type parameters

* #### D = unknown

### Hierarchy

* default
  + [default](src_core_request_modules_context_modules_methods.default.html)

## Index

### Constructors

* [constructor](src_core_request_modules_context_modules_params.default.html#constructor)

### Properties

* [cache](src_core_request_modules_context_modules_params.default.html#cache)
* [cacheTimeoutId](src_core_request_modules_context_modules_params.default.html#cacheTimeoutId)
* [canCache](src_core_request_modules_context_modules_params.default.html#canCache)
* [isReady](src_core_request_modules_context_modules_params.default.html#isReady)
* [params](src_core_request_modules_context_modules_params.default.html#params)
* [parent](src_core_request_modules_context_modules_params.default.html#parent)
* [pendingCache](src_core_request_modules_context_modules_params.default.html#pendingCache)
* [withoutBody](src_core_request_modules_context_modules_params.default.html#withoutBody)

### Accessors

* [cacheKey](src_core_request_modules_context_modules_params.default.html#cacheKey)
* [decoders](src_core_request_modules_context_modules_params.default.html#decoders)
* [encoders](src_core_request_modules_context_modules_params.default.html#encoders)
* [headers](src_core_request_modules_context_modules_params.default.html#headers)
* [query](src_core_request_modules_context_modules_params.default.html#query)
* [streamDecoders](src_core_request_modules_context_modules_params.default.html#streamDecoders)

## Constructors

### constructor

* new default<D>(params?: [NormalizedCreateRequestOptions](../modules/src_core_request_interface.html#NormalizedCreateRequestOptions)<D>): [default](src_core_request_modules_context_modules_params.default.html)<D>

* + Defined in [src/core/request/modules/context/modules/params.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L169)

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional params: [NormalizedCreateRequestOptions](../modules/src_core_request_interface.html#NormalizedCreateRequestOptions)<D>

  #### Returns [default](src_core_request_modules_context_modules_params.default.html)<D>

## Properties

### Readonly cache

cache: [default](../interfaces/src_core_cache_interface.default.html)<[Nullable](../modules/index.html#Nullable)<D>, string>

* Defined in [src/core/request/modules/context/modules/params.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L79)

Storage to cache the resolved request

### Protected Optional cacheTimeoutId

cacheTimeoutId?: number

* Defined in [src/core/request/modules/context/modules/params.ts:164](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L164)

Cache TTL identifier

### Readonly canCache

canCache: boolean

* Defined in [src/core/request/modules/context/modules/params.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L60)

True if the request can be cached

### Readonly isReady

isReady: Promise<void>

* Defined in [src/core/request/modules/context/modules/params.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L55)

Promise that resolves when the instance is already initialized

### Readonly params

params: [NormalizedCreateRequestOptions](../modules/src_core_request_interface.html#NormalizedCreateRequestOptions)<D>

* Defined in [src/core/request/modules/context/modules/params.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L96)

Request parameters

### parent

parent: [default](src_core_promise_abortable.default.html)<unknown>

* Defined in [src/core/request/modules/context/modules/params.ts:159](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L159)

Link to a parent operation promise

### Readonly pendingCache

pendingCache: [default](../interfaces/src_core_cache_interface.default.html)<[RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D> | [ControllablePromise](../modules/src_core_promise_interface.html#ControllablePromise)<[RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>>, string> = ...

* Defined in [src/core/request/modules/context/modules/params.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L84)

Storage to cache the request while it is pending a response

### Readonly withoutBody

withoutBody: boolean

* Defined in [src/core/request/modules/context/modules/params.ts:91](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L91)

True if the request can provide parameters only as a query string

## Accessors

### cacheKey

* get cacheKey(): [CanUndef](../modules/index.html#CanUndef)<string>
* set cacheKey(value: [CanUndef](../modules/index.html#CanUndef)<string>): void

* + Defined in [src/core/request/modules/context/modules/params.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L65)

  String key to cache the request

  #### Returns [CanUndef](../modules/index.html#CanUndef)<string>
* + Defined in [src/core/request/modules/context/modules/params.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L72)

  Sets a new string key to cache the request

  #### Parameters

  + ##### value: [CanUndef](../modules/index.html#CanUndef)<string>

  #### Returns void

### decoders

* get decoders(): [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)
* set decoders(value: [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)): void

* + Defined in [src/core/request/modules/context/modules/params.ts:131](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L131)

  Sequence of response data decoders

  #### Returns [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)
* + Defined in [src/core/request/modules/context/modules/params.ts:138](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L138)

  Sets a new sequence of response data decoders

  #### Parameters

  + ##### value: [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)

  #### Returns void

### encoders

* get encoders(): [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)
* set encoders(value: [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)): void

* + Defined in [src/core/request/modules/context/modules/params.ts:117](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L117)

  Sequence of request data encoders

  #### Returns [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)
* + Defined in [src/core/request/modules/context/modules/params.ts:124](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L124)

  Sets a new sequence of request data encoders

  #### Parameters

  + ##### value: [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)

  #### Returns void

### headers

* get headers(): [default](src_core_request_headers.default.html)

* + Defined in [src/core/request/modules/context/modules/params.ts:110](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L110)

  Alias for `params.headers`

  alias

  #### Returns [default](src_core_request_headers.default.html)

### query

* get query(): [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)

* + Defined in [src/core/request/modules/context/modules/params.ts:102](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L102)

  Alias for `params.query`

  alias

  #### Returns [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)

### streamDecoders

* get streamDecoders(): [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)
* set streamDecoders(value: [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)): void

* + Defined in [src/core/request/modules/context/modules/params.ts:145](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L145)

  Sequence of response data decoders

  #### Returns [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)
* + Defined in [src/core/request/modules/context/modules/params.ts:152](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L152)

  Sets a new sequence of response data decoders

  #### Parameters

  + ##### value: [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)

  #### Returns void