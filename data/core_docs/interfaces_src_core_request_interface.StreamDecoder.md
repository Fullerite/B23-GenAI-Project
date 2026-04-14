# Interface StreamDecoder<I, O>
### Type parameters

* #### I = unknown
* #### O = unknown

### Hierarchy

* StreamDecoder

### Callable

* StreamDecoder(data: [AnyIterable](../modules/index.html#AnyIterable)<I>, params: [MiddlewareParams](src_core_request_interface.MiddlewareParams.html)<unknown>, response: [default](../classes/src_core_request_response.default.html)<unknown>): [AnyIterable](../modules/index.html#AnyIterable)<O>

* + Defined in [src/core/request/interface.ts:115](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L115)

  #### Parameters

  + ##### data: [AnyIterable](../modules/index.html#AnyIterable)<I>
  + ##### params: [MiddlewareParams](src_core_request_interface.MiddlewareParams.html)<unknown>
  + ##### response: [default](../classes/src_core_request_response.default.html)<unknown>

  #### Returns [AnyIterable](../modules/index.html#AnyIterable)<O>