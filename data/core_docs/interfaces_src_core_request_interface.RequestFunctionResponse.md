# Interface RequestFunctionResponse<D, ARGS>
### Type parameters

* #### D = unknown
* #### ARGS: any[] = unknown[]

### Hierarchy

* RequestFunctionResponse

### Callable

* RequestFunctionResponse(...args: ARGS extends V[] ? V[] : unknown[]): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/request/interface.ts:155](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L155)

  #### Parameters

  + ##### Rest ...args: ARGS extends V[] ? V[] : unknown[]

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>