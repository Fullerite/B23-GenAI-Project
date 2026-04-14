# Module src/core/request/response/interface
## Index

### Interfaces

* [ResponseChunk](../interfaces/src_core_request_response_interface.ResponseChunk.html)
* [ResponseOptions](../interfaces/src_core_request_response_interface.ResponseOptions.html)

### Type aliases

* [JSONLikeValue](src_core_request_response_interface.html#JSONLikeValue)
* [NormalizedResponseOptions](src_core_request_response_interface.html#NormalizedResponseOptions)
* [ResponseModeType](src_core_request_response_interface.html#ResponseModeType)
* [ResponseType](src_core_request_response_interface.html#ResponseType)
* [ResponseTypeValue](src_core_request_response_interface.html#ResponseTypeValue)
* [ResponseTypeValueP](src_core_request_response_interface.html#ResponseTypeValueP)

## Type aliases

### JSONLikeValue

JSONLikeValue: string | number | boolean | null | unknown[] | [Dictionary](../interfaces/index.Dictionary.html)

* Defined in [src/core/request/response/interface.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L55)

### NormalizedResponseOptions

NormalizedResponseOptions: typeof [defaultResponseOpts](src_core_request_response_const.html#defaultResponseOpts) & [ResponseOptions](../interfaces/src_core_request_response_interface.ResponseOptions.html)

* Defined in [src/core/request/response/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L89)

### ResponseModeType

ResponseModeType: "basic" | "cors" | "default" | "error" | "opaque" | "opaqueredirect"

* Defined in [src/core/request/response/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L29)

### ResponseType

ResponseType: [DataType](src_core_mime_type_interface.html#DataType) | "object"

* Defined in [src/core/request/response/interface.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L37)

### ResponseTypeValue

ResponseTypeValue: string | object | ArrayBuffer | Buffer | Document | FormData | null | undefined

* Defined in [src/core/request/response/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L41)

### ResponseTypeValueP

ResponseTypeValueP: [CanPromise](index.html#CanPromise)<[ResponseTypeValue](src_core_request_response_interface.html#ResponseTypeValue)> | (() => [CanPromise](index.html#CanPromise)<[ResponseTypeValue](src_core_request_response_interface.html#ResponseTypeValue)>)

* Defined in [src/core/request/response/interface.ts:51](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L51)