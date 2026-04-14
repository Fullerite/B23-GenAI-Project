# Interface RequestResolver<D, ARGS>
### Type parameters

* #### D = unknown
* #### ARGS: any[] = unknown[]

### Hierarchy

* RequestResolver

### Callable

* RequestResolver(url: string, params: [MiddlewareParams](src_core_request_interface.MiddlewareParams.html)<D>, ...args: ARGS): [ResolverResult](../modules/src_core_request_interface.html#ResolverResult)

* + Defined in [src/core/request/interface.ts:159](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L159)

  #### Parameters

  + ##### url: string
  + ##### params: [MiddlewareParams](src_core_request_interface.MiddlewareParams.html)<D>
  + ##### Rest ...args: ARGS

  #### Returns [ResolverResult](../modules/src_core_request_interface.html#ResolverResult)