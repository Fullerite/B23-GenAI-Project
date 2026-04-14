# Module src/core/async/modules/wrappers/interface
## Index

### Interfaces

* [EventEmitterWrapper](../interfaces/src_core_async_modules_wrappers_interface.EventEmitterWrapper.html)
* [ReadonlyEventEmitterWrapper](../interfaces/src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html)
* [WrappedAsyncStorage](../interfaces/src_core_async_modules_wrappers_interface.WrappedAsyncStorage.html)
* [WrappedAsyncStorageNamespace](../interfaces/src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html)

### Type aliases

* [AsyncOptionsForWrappers](src_core_async_modules_wrappers_interface.html#AsyncOptionsForWrappers)
* [DataProviderBodyMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderBodyMethodsToReplace)
* [DataProviderMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderMethodsToReplace)
* [DataProviderQueryMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderQueryMethodsToReplace)
* [EventEmitterOverwritten](src_core_async_modules_wrappers_interface.html#EventEmitterOverwritten)
* [WrappedDataProvider](src_core_async_modules_wrappers_interface.html#WrappedDataProvider)

## Type aliases

### AsyncOptionsForWrappers

AsyncOptionsForWrappers: Pick<[AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html), "group">

* Defined in [src/core/async/modules/wrappers/interface.ts:126](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L126)

### DataProviderBodyMethodsToReplace

DataProviderBodyMethodsToReplace: "post" | "add" | "upd" | "del"

* Defined in [src/core/async/modules/wrappers/interface.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L18)

### DataProviderMethodsToReplace

DataProviderMethodsToReplace: [DataProviderQueryMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderQueryMethodsToReplace) | [DataProviderBodyMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderBodyMethodsToReplace)

* Defined in [src/core/async/modules/wrappers/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L19)

### DataProviderQueryMethodsToReplace

DataProviderQueryMethodsToReplace: "get" | "peek"

* Defined in [src/core/async/modules/wrappers/interface.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L17)

### EventEmitterOverwritten

EventEmitterOverwritten<T>: [Overwrite](index.html#Overwrite)<T, { addEventListener: T["addEventListener"] extends (...args: any[]) => any ? AddEventListenerLikeFunctionMapper<T["addEventListener"]> : never; addListener: T["addListener"] extends (...args: any[]) => any ? AddEventListenerLikeFunctionMapper<T["addListener"]> : never }>

* Defined in [src/core/async/modules/wrappers/interface.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L114)

#### Type parameters

* #### T: [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html)

### WrappedDataProvider

WrappedDataProvider: [Overwrite](index.html#Overwrite)<[Provider](../interfaces/src_core_data_interface.Provider.html), { emitter: [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html); add: any; del: any; get: any; peek: any; post: any; upd: any }>

* Defined in [src/core/async/modules/wrappers/interface.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L21)