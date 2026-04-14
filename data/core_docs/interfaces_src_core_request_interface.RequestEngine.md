# Interface RequestEngine
### Hierarchy

* RequestEngine

### Callable

* RequestEngine(request: [RequestOptions](src_core_request_interface.RequestOptions.html), params: [MiddlewareParams](src_core_request_interface.MiddlewareParams.html)<unknown>): [default](../classes/src_core_promise_abortable.default.html)<[default](../classes/src_core_request_response.default.html)<unknown>>

* + Defined in [src/core/request/interface.ts:687](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L687)

  Request engine

  #### Parameters

  + ##### request: [RequestOptions](src_core_request_interface.RequestOptions.html)
  + ##### params: [MiddlewareParams](src_core_request_interface.MiddlewareParams.html)<unknown>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<[default](../classes/src_core_request_response.default.html)<unknown>>

## Index

### Properties

* [pendingCache](src_core_request_interface.RequestEngine.html#pendingCache)

## Properties

### Optional pendingCache

pendingCache?: boolean

* Defined in [src/core/request/interface.ts:693](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L693)

A flag indicates that the active requests with the same request hash can be merged

default
:   `true`