# Module src/core/data/const
## Index

### Variables

* [connectCache](src_core_data_const.html#connectCache)
* [emitter](src_core_data_const.html#emitter)
* [instanceCache](src_core_data_const.html#instanceCache)
* [methodProperties](src_core_data_const.html#methodProperties)
* [namespace](src_core_data_const.html#namespace)
* [providers](src_core_data_const.html#providers)
* [queryMethods](src_core_data_const.html#queryMethods)
* [requestCache](src_core_data_const.html#requestCache)
* [urlProperties](src_core_data_const.html#urlProperties)

## Variables

### Const connectCache

connectCache: [Dictionary](../interfaces/index.Dictionary.html)<Promise<[Socket](src_core_socket_interface.html#Socket)>> = ...

* Defined in [src/core/data/const.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L31)

### Const emitter

emitter: EventEmitter2 = ...

* Defined in [src/core/data/const.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L22)

Global event emitter to broadcast provider events

### Const instanceCache

instanceCache: [Dictionary](../interfaces/index.Dictionary.html)<[Provider](../interfaces/src_core_data_interface.Provider.html)> = ...

* Defined in [src/core/data/const.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L29)

### Const methodProperties

methodProperties: string[] = ...

* Defined in [src/core/data/const.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L38)

### Const namespace

namespace: typeof [namespace](src_core_data_const.html#namespace) = ...

* Defined in [src/core/data/const.ts:16](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L16)

### Const providers

providers: [Dictionary](../interfaces/index.Dictionary.html)<[ProviderConstructor](../interfaces/src_core_data_interface_types.ProviderConstructor.html)> = ...

* Defined in [src/core/data/const.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L17)

### Const queryMethods

queryMethods: Pick<{ GET: boolean; HEAD: boolean }, "GET" | "HEAD"> = ...

* Defined in [src/core/data/const.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L33)

### Const requestCache

requestCache: [Dictionary](../interfaces/index.Dictionary.html)<[Dictionary](../interfaces/index.Dictionary.html)<[RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)>> = ...

* Defined in [src/core/data/const.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L30)

### Const urlProperties

urlProperties: string[] = ...

* Defined in [src/core/data/const.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/data/const.ts#L46)