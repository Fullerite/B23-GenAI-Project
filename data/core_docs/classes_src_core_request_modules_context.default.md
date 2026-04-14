# Class default<D>
Context of a request

### Type parameters

* #### D = unknown

  response data

### Hierarchy

* [default](src_core_request_modules_context_modules_middlewares.default.html)<D>
  + default

## Index

### Constructors

* [constructor](src_core_request_modules_context.default.html#constructor)

### Properties

* [cache](src_core_request_modules_context.default.html#cache)
* [cacheTimeoutId](src_core_request_modules_context.default.html#cacheTimeoutId)
* [canCache](src_core_request_modules_context.default.html#canCache)
* [isReady](src_core_request_modules_context.default.html#isReady)
* [params](src_core_request_modules_context.default.html#params)
* [parent](src_core_request_modules_context.default.html#parent)
* [pendingCache](src_core_request_modules_context.default.html#pendingCache)
* [withoutBody](src_core_request_modules_context.default.html#withoutBody)

### Accessors

* [cacheKey](src_core_request_modules_context.default.html#cacheKey)
* [decoders](src_core_request_modules_context.default.html#decoders)
* [encoders](src_core_request_modules_context.default.html#encoders)
* [headers](src_core_request_modules_context.default.html#headers)
* [query](src_core_request_modules_context.default.html#query)
* [streamDecoders](src_core_request_modules_context.default.html#streamDecoders)

### Methods

* [dropCache](src_core_request_modules_context.default.html#dropCache)
* [getRequestKey](src_core_request_modules_context.default.html#getRequestKey)
* [resolveAPI](src_core_request_modules_context.default.html#resolveAPI)
* [resolveRequest](src_core_request_modules_context.default.html#resolveRequest)
* [resolveURL](src_core_request_modules_context.default.html#resolveURL)
* [saveCache](src_core_request_modules_context.default.html#saveCache)
* [wrapAsResponse](src_core_request_modules_context.default.html#wrapAsResponse)
* [wrapRequest](src_core_request_modules_context.default.html#wrapRequest)
* [decorateContext](src_core_request_modules_context.default.html#decorateContext)

## Constructors

### constructor

* new default<D>(params?: [NormalizedCreateRequestOptions](../modules/src_core_request_interface.html#NormalizedCreateRequestOptions)<D>): [default](src_core_request_modules_context.default.html)<D>

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[constructor](src_core_request_modules_context_modules_middlewares.default.html#constructor)

  + Defined in [src/core/request/modules/context/modules/params.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L169)

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional params: [NormalizedCreateRequestOptions](../modules/src_core_request_interface.html#NormalizedCreateRequestOptions)<D>

  #### Returns [default](src_core_request_modules_context.default.html)<D>

## Properties

### Readonly cache

cache: [default](../interfaces/src_core_cache_interface.default.html)<[Nullable](../modules/index.html#Nullable)<D>, string>

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[cache](src_core_request_modules_context_modules_middlewares.default.html#cache)

* Defined in [src/core/request/modules/context/modules/params.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L79)

Storage to cache the resolved request

### Protected Optional cacheTimeoutId

cacheTimeoutId?: number

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[cacheTimeoutId](src_core_request_modules_context_modules_middlewares.default.html#cacheTimeoutId)

* Defined in [src/core/request/modules/context/modules/params.ts:164](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L164)

Cache TTL identifier

### Readonly canCache

canCache: boolean

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[canCache](src_core_request_modules_context_modules_middlewares.default.html#canCache)

* Defined in [src/core/request/modules/context/modules/params.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L60)

True if the request can be cached

### Readonly isReady

isReady: Promise<void>

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[isReady](src_core_request_modules_context_modules_middlewares.default.html#isReady)

* Defined in [src/core/request/modules/context/modules/params.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L55)

Promise that resolves when the instance is already initialized

### Readonly params

params: [NormalizedCreateRequestOptions](../modules/src_core_request_interface.html#NormalizedCreateRequestOptions)<D>

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[params](src_core_request_modules_context_modules_middlewares.default.html#params)

* Defined in [src/core/request/modules/context/modules/params.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L96)

Request parameters

### parent

parent: [default](src_core_promise_abortable.default.html)<unknown>

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[parent](src_core_request_modules_context_modules_middlewares.default.html#parent)

* Defined in [src/core/request/modules/context/modules/params.ts:159](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L159)

Link to a parent operation promise

### Readonly pendingCache

pendingCache: [default](../interfaces/src_core_cache_interface.default.html)<[RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D> | [ControllablePromise](../modules/src_core_promise_interface.html#ControllablePromise)<[RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>>, string> = ...

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[pendingCache](src_core_request_modules_context_modules_middlewares.default.html#pendingCache)

* Defined in [src/core/request/modules/context/modules/params.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L84)

Storage to cache the request while it is pending a response

### Readonly withoutBody

withoutBody: boolean

Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[withoutBody](src_core_request_modules_context_modules_middlewares.default.html#withoutBody)

* Defined in [src/core/request/modules/context/modules/params.ts:91](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L91)

True if the request can provide parameters only as a query string

## Accessors

### cacheKey

* get cacheKey(): [CanUndef](../modules/index.html#CanUndef)<string>
* set cacheKey(value: [CanUndef](../modules/index.html#CanUndef)<string>): void

* Inherited from Super.cacheKey

  + Defined in [src/core/request/modules/context/modules/params.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L65)

  String key to cache the request

  #### Returns [CanUndef](../modules/index.html#CanUndef)<string>
* Inherited from Super.cacheKey

  + Defined in [src/core/request/modules/context/modules/params.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L72)

  Sets a new string key to cache the request

  #### Parameters

  + ##### value: [CanUndef](../modules/index.html#CanUndef)<string>

  #### Returns void

### decoders

* get decoders(): [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)
* set decoders(value: [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)): void

* Inherited from Super.decoders

  + Defined in [src/core/request/modules/context/modules/params.ts:131](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L131)

  Sequence of response data decoders

  #### Returns [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)
* Inherited from Super.decoders

  + Defined in [src/core/request/modules/context/modules/params.ts:138](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L138)

  Sets a new sequence of response data decoders

  #### Parameters

  + ##### value: [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)

  #### Returns void

### encoders

* get encoders(): [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)
* set encoders(value: [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)): void

* Inherited from Super.encoders

  + Defined in [src/core/request/modules/context/modules/params.ts:117](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L117)

  Sequence of request data encoders

  #### Returns [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)
* Inherited from Super.encoders

  + Defined in [src/core/request/modules/context/modules/params.ts:124](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L124)

  Sets a new sequence of request data encoders

  #### Parameters

  + ##### value: [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)

  #### Returns void

### headers

* get headers(): [default](src_core_request_headers.default.html)

* Inherited from Super.headers

  + Defined in [src/core/request/modules/context/modules/params.ts:110](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L110)

  Alias for `params.headers`

  alias

  #### Returns [default](src_core_request_headers.default.html)

### query

* get query(): [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)

* Inherited from Super.query

  + Defined in [src/core/request/modules/context/modules/params.ts:102](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L102)

  Alias for `params.query`

  alias

  #### Returns [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)

### streamDecoders

* get streamDecoders(): [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)
* set streamDecoders(value: [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)): void

* Inherited from Super.streamDecoders

  + Defined in [src/core/request/modules/context/modules/params.ts:145](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L145)

  Sequence of response data decoders

  #### Returns [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)
* Inherited from Super.streamDecoders

  + Defined in [src/core/request/modules/context/modules/params.ts:152](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/params.ts#L152)

  Sets a new sequence of response data decoders

  #### Parameters

  + ##### value: [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)

  #### Returns void

## Methods

### dropCache

* dropCache(): void

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[dropCache](src_core_request_modules_context_modules_middlewares.default.html#dropCache)

  + Defined in [src/core/request/modules/context/modules/methods.ts:211](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/methods.ts#L211)

  Drops the request cache

  #### Returns void

### getRequestKey

* getRequestKey(url: string): string

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[getRequestKey](src_core_request_modules_context_modules_middlewares.default.html#getRequestKey)

  + Defined in [src/core/request/modules/context/modules/methods.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/methods.ts#L26)

  Generates a string cache key for specified URL and returns it

  #### Parameters

  + ##### url: string

  #### Returns string

### resolveAPI

* resolveAPI(apiURL?: [Nullable](../modules/index.html#Nullable)<string>): string

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[resolveAPI](src_core_request_modules_context_modules_middlewares.default.html#resolveAPI)

  + Defined in [src/core/request/modules/context/modules/methods.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/methods.ts#L39)

  Returns an absolute URL for the request API

  #### Parameters

  + ##### apiURL: [Nullable](../modules/index.html#Nullable)<string> = globalOpts.api

  #### Returns string

### resolveRequest

* resolveRequest(url?: [Nullable](../modules/index.html#Nullable)<string>): string

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[resolveRequest](src_core_request_modules_context_modules_middlewares.default.html#resolveRequest)

  + Defined in [src/core/request/modules/context/modules/methods.ts:150](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/methods.ts#L150)

  Resolves request parameters and returns an absolute URL for the request

  #### Parameters

  + ##### Optional url: [Nullable](../modules/index.html#Nullable)<string>

  #### Returns string

### resolveURL

* resolveURL(url?: [Nullable](../modules/index.html#Nullable)<string>): string

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[resolveURL](src_core_request_modules_context_modules_middlewares.default.html#resolveURL)

  + Defined in [src/core/request/modules/context/modules/methods.ts:204](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/methods.ts#L204)

  Returns an absolute URL for the request

  see
  :   [[RequestContext.resolveRequest]]

  #### Parameters

  + ##### Optional url: [Nullable](../modules/index.html#Nullable)<string>

  #### Returns string

### saveCache

* saveCache(resObj: [RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>): Promise<[RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>>

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[saveCache](src_core_request_modules_context_modules_middlewares.default.html#saveCache)

  + Defined in [src/core/request/modules/context/modules/middlewares.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/middlewares.ts#L71)

  Middleware to cache a response object

  #### Parameters

  + ##### resObj: [RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>

    response object

  #### Returns Promise<[RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>>

### wrapAsResponse

* wrapAsResponse(value: [ResponseTypeValue](../modules/src_core_request_response_interface.html#ResponseTypeValue) | [default](src_core_request_response.default.html)<D>): [RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[wrapAsResponse](src_core_request_modules_context_modules_middlewares.default.html#wrapAsResponse)

  + Defined in [src/core/request/modules/context/modules/middlewares.ts:127](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/middlewares.ts#L127)

  A middleware to wrap the specified response value with `RequestResponseObject`.
  Use it when wrapping some raw data as the `core/request` response.

  #### Parameters

  + ##### value: [ResponseTypeValue](../modules/src_core_request_response_interface.html#ResponseTypeValue) | [default](src_core_request_response.default.html)<D>

  #### Returns [RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>

### wrapRequest

* wrapRequest(promise: [RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>): [RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>

* Inherited from [default](src_core_request_modules_context_modules_middlewares.default.html).[wrapRequest](src_core_request_modules_context_modules_middlewares.default.html#wrapRequest)

  + Defined in [src/core/request/modules/context/modules/middlewares.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/modules/middlewares.ts#L25)

  Wraps the specified promise: attaches the pending cache, etc.

  #### Parameters

  + ##### promise: [RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>

  #### Returns [RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>

### Static decorateContext

* decorateContext<CTX>(ctx: CTX, path: string, resolver?: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<unknown, unknown[]>, ...args: unknown[]): CTX

* + Defined in [src/core/request/modules/context/index.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/context/index.ts#L48)

  Forks the specified request context and decorates it with additional parameters

  #### Type parameters

  + #### CTX: [default](src_core_request_modules_context.default.html)<any, CTX>

  #### Parameters

  + ##### ctx: CTX
  + ##### path: string

    request path URL
  + ##### Optional resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<unknown, unknown[]>

    function to resolve a request
  + ##### Rest ...args: unknown[]

    additional arguments for the resolver

  #### Returns CTX