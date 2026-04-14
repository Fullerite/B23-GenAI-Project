# Module src/core/request/interface
## Index

### Interfaces

* [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)
* [Decoder](../interfaces/src_core_request_interface.Decoder.html)
* [Encoder](../interfaces/src_core_request_interface.Encoder.html)
* [GlobalOptions](../interfaces/src_core_request_interface.GlobalOptions.html)
* [Middleware](../interfaces/src_core_request_interface.Middleware.html)
* [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)
* [RequestAPI](../interfaces/src_core_request_interface.RequestAPI.html)
* [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html)
* [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)
* [RequestOptions](../interfaces/src_core_request_interface.RequestOptions.html)
* [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)
* [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)
* [RequestResponseChunk](../interfaces/src_core_request_interface.RequestResponseChunk.html)
* [RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)
* [RetryOptions](../interfaces/src_core_request_interface.RetryOptions.html)
* [StreamDecoder](../interfaces/src_core_request_interface.StreamDecoder.html)
* [WrappedCreateRequestOptions](../interfaces/src_core_request_interface.WrappedCreateRequestOptions.html)
* [WrappedDecoder](../interfaces/src_core_request_interface.WrappedDecoder.html)
* [WrappedEncoder](../interfaces/src_core_request_interface.WrappedEncoder.html)
* [WrappedStreamDecoder](../interfaces/src_core_request_interface.WrappedStreamDecoder.html)

### Type aliases

* [CacheStrategy](src_core_request_interface.html#CacheStrategy)
* [CacheType](src_core_request_interface.html#CacheType)
* [Decoders](src_core_request_interface.html#Decoders)
* [Encoders](src_core_request_interface.html#Encoders)
* [Middlewares](src_core_request_interface.html#Middlewares)
* [NormalizedCreateRequestOptions](src_core_request_interface.html#NormalizedCreateRequestOptions)
* [NormalizedRequestBody](src_core_request_interface.html#NormalizedRequestBody)
* [OkStatuses](src_core_request_interface.html#OkStatuses)
* [RequestAPIValue](src_core_request_interface.html#RequestAPIValue)
* [RequestBody](src_core_request_interface.html#RequestBody)
* [RequestMethod](src_core_request_interface.html#RequestMethod)
* [RequestQuery](src_core_request_interface.html#RequestQuery)
* [RequestResponse](src_core_request_interface.html#RequestResponse)
* [ResolverResult](src_core_request_interface.html#ResolverResult)
* [StreamDecoders](src_core_request_interface.html#StreamDecoders)
* [WrappedDecoders](src_core_request_interface.html#WrappedDecoders)
* [WrappedEncoders](src_core_request_interface.html#WrappedEncoders)
* [WrappedStreamDecoders](src_core_request_interface.html#WrappedStreamDecoders)

## Type aliases

### CacheStrategy

CacheStrategy: "queue" | "forever" | "never" | [default](../interfaces/src_core_cache_interface.default.html) | Promise<[default](../interfaces/src_core_cache_interface.default.html)>

* Defined in [src/core/request/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L38)

### CacheType

CacheType: "memory" | "offline"

* Defined in [src/core/request/interface.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L45)

### Decoders

Decoders: Iterable<[Decoder](../interfaces/src_core_request_interface.Decoder.html)>

* Defined in [src/core/request/interface.ts:111](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L111)

### Encoders

Encoders: Iterable<[Encoder](../interfaces/src_core_request_interface.Encoder.html)>

* Defined in [src/core/request/interface.ts:100](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L100)

### Middlewares

Middlewares<D>: [Dictionary](../interfaces/index.Dictionary.html)<[Middleware](../interfaces/src_core_request_interface.Middleware.html)<D>> | Iterable<[Middleware](../interfaces/src_core_request_interface.Middleware.html)<D>>

* Defined in [src/core/request/interface.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L88)

#### Type parameters

* #### D = unknown

### NormalizedCreateRequestOptions

NormalizedCreateRequestOptions<D>: typeof [defaultRequestOpts](src_core_request_const.html#defaultRequestOpts) & [WrappedCreateRequestOptions](../interfaces/src_core_request_interface.WrappedCreateRequestOptions.html)<D>

* Defined in [src/core/request/interface.ts:657](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L657)

#### Type parameters

* #### D = unknown

### NormalizedRequestBody

NormalizedRequestBody: Exclude<[RequestBody](src_core_request_interface.html#RequestBody), number | boolean | [Dictionary](../interfaces/index.Dictionary.html)>

* Defined in [src/core/request/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L63)

### OkStatuses

OkStatuses: [default](../classes/src_core_range.default.html)<number> | [StatusCodes](../enums/src_core_status_codes_interface.StatusCodes.html) | [StatusCodes](../enums/src_core_status_codes_interface.StatusCodes.html)[]

* Defined in [src/core/request/interface.ts:68](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L68)

### RequestAPIValue

RequestAPIValue<T>: [Nullable](index.html#Nullable)<T> | (() => [Nullable](index.html#Nullable)<T>)

* Defined in [src/core/request/interface.ts:562](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L562)

#### Type parameters

* #### T = string

### RequestBody

RequestBody: string | number | boolean | [Dictionary](../interfaces/index.Dictionary.html) | FormData | ArrayBuffer | Blob

* Defined in [src/core/request/interface.ts:54](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L54)

### RequestMethod

RequestMethod: "GET" | "POST" | "PUT" | "DELETE" | "PATCH" | "HEAD" | "CONNECT" | "OPTIONS" | "TRACE"

* Defined in [src/core/request/interface.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L27)

### RequestQuery

RequestQuery: [Dictionary](../interfaces/index.Dictionary.html) | unknown[] | string

* Defined in [src/core/request/interface.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L49)

### RequestResponse

RequestResponse<D>: [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)<D>>

* Defined in [src/core/request/interface.ts:145](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L145)

#### Type parameters

* #### D = unknown

### ResolverResult

ResolverResult: [CanUndef](index.html#CanUndef)<[CanArray](index.html#CanArray)<string>>

* Defined in [src/core/request/interface.ts:162](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L162)

### StreamDecoders

StreamDecoders: Iterable<[StreamDecoder](../interfaces/src_core_request_interface.StreamDecoder.html)>

* Defined in [src/core/request/interface.ts:122](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L122)

### WrappedDecoders

WrappedDecoders: Iterable<[WrappedDecoder](../interfaces/src_core_request_interface.WrappedDecoder.html)>

* Defined in [src/core/request/interface.ts:112](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L112)

### WrappedEncoders

WrappedEncoders: Iterable<[WrappedEncoder](../interfaces/src_core_request_interface.WrappedEncoder.html)>

* Defined in [src/core/request/interface.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L101)

### WrappedStreamDecoders

WrappedStreamDecoders: Iterable<[WrappedStreamDecoder](../interfaces/src_core_request_interface.WrappedStreamDecoder.html)>

* Defined in [src/core/request/interface.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L123)