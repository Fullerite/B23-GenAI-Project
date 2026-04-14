# Interface WrappedAsyncStorageNamespace
### Hierarchy

* WrappedAsyncStorageNamespace
  + [WrappedAsyncStorage](src_core_async_modules_wrappers_interface.WrappedAsyncStorage.html)

## Index

### Methods

* [clear](src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html#clear)
* [get](src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html#get)
* [has](src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html#has)
* [remove](src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html#remove)
* [set](src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html#set)

## Methods

### clear

* clear<T>(filter?: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>, opts?: unknown[]): Promise<void>
* clear<T>(filter?: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>, ...args: unknown[]): Promise<void>

* + Defined in [src/core/async/modules/wrappers/interface.ts:146](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L146)

  see
  :   [AsyncStorage.clear](src_core_kv_storage_interface.AsyncStorage.html#clear)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### Optional filter: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>
  + ##### Optional opts: unknown[]

  #### Returns Promise<void>
* + Defined in [src/core/async/modules/wrappers/interface.ts:147](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L147)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### Optional filter: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>
  + ##### Rest ...args: unknown[]

  #### Returns Promise<void>

### get

* get<T>(key: string, opts?: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)): Promise<[CanUndef](../modules/index.html#CanUndef)<T>>
* get<T>(key: string, ...args: unknown[]): Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

* + Defined in [src/core/async/modules/wrappers/interface.ts:134](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L134)

  see
  :   [AsyncStorage.get](src_core_kv_storage_interface.AsyncStorage.html#get)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### key: string
  + ##### Optional opts: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<T>>
* + Defined in [src/core/async/modules/wrappers/interface.ts:135](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L135)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

### has

* has(key: string, opts?: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)): Promise<boolean>
* has(key: string, ...args: unknown[]): Promise<boolean>

* + Defined in [src/core/async/modules/wrappers/interface.ts:130](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L130)

  see
  :   [AsyncStorage.has](src_core_kv_storage_interface.AsyncStorage.html#has)

  #### Parameters

  + ##### key: string
  + ##### Optional opts: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)

  #### Returns Promise<boolean>
* + Defined in [src/core/async/modules/wrappers/interface.ts:131](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L131)

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns Promise<boolean>

### remove

* remove(key: string, opts?: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)): Promise<void>
* remove(key: string, ...args: unknown[]): Promise<void>

* + Defined in [src/core/async/modules/wrappers/interface.ts:142](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L142)

  see
  :   [AsyncStorage.remove](src_core_kv_storage_interface.AsyncStorage.html#remove)

  #### Parameters

  + ##### key: string
  + ##### Optional opts: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)

  #### Returns Promise<void>
* + Defined in [src/core/async/modules/wrappers/interface.ts:143](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L143)

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns Promise<void>

### set

* set(key: string, value: unknown, opts?: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)): Promise<void>
* set(key: string, value: unknown, ...args: unknown[]): Promise<void>

* + Defined in [src/core/async/modules/wrappers/interface.ts:138](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L138)

  see
  :   [AsyncStorage.set](src_core_kv_storage_interface.AsyncStorage.html#set)

  #### Parameters

  + ##### key: string
  + ##### value: unknown
  + ##### Optional opts: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)

  #### Returns Promise<void>
* + Defined in [src/core/async/modules/wrappers/interface.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L139)

  #### Parameters

  + ##### key: string
  + ##### value: unknown
  + ##### Rest ...args: unknown[]

  #### Returns Promise<void>