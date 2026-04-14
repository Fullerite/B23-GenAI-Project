# Class default<T, V>
### Type parameters

* #### T: [default](../interfaces/src_core_cache_interface.default.html)<V, string>
* #### V = unknown

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_cache_decorators_persistent_wrapper.default.html#constructor)

### Properties

* [cache](src_core_cache_decorators_persistent_wrapper.default.html#cache)
* [engine](src_core_cache_decorators_persistent_wrapper.default.html#engine)
* [fetchedItems](src_core_cache_decorators_persistent_wrapper.default.html#fetchedItems)
* [ttl](src_core_cache_decorators_persistent_wrapper.default.html#ttl)
* [wrappedCache](src_core_cache_decorators_persistent_wrapper.default.html#wrappedCache)

### Methods

* [checkItemInStorage](src_core_cache_decorators_persistent_wrapper.default.html#checkItemInStorage)
* [getDefaultImplementation](src_core_cache_decorators_persistent_wrapper.default.html#getDefaultImplementation)
* [getInstance](src_core_cache_decorators_persistent_wrapper.default.html#getInstance)
* [implementAPI](src_core_cache_decorators_persistent_wrapper.default.html#implementAPI)

## Constructors

### constructor

* new default<T, V>(cache: T, storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace), opts?: [PersistentOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentOptions.html)): [default](src_core_cache_decorators_persistent_wrapper.default.html)<T, V>

* + Defined in [src/core/cache/decorators/persistent/wrapper.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L52)

  #### Type parameters

  + #### T: [default](../interfaces/src_core_cache_interface.default.html)<V, string, T>
  + #### V = unknown

  #### Parameters

  + ##### cache: T

    cache object to wrap
  + ##### storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

    storage object to save cache items
  + ##### Optional opts: [PersistentOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentOptions.html)

  #### Returns [default](src_core_cache_decorators_persistent_wrapper.default.html)<T, V>

## Properties

### Protected Readonly cache

cache: T

* Defined in [src/core/cache/decorators/persistent/wrapper.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L30)

Original cache object

### Protected Readonly engine

engine: [PersistentEngine](../modules/src_core_cache_decorators_persistent_engines_interface.html#PersistentEngine)<unknown>

* Defined in [src/core/cache/decorators/persistent/wrapper.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L40)

Engine to save cache items within a storage

### Protected Readonly fetchedItems

fetchedItems: Set<string> = ...

* Defined in [src/core/cache/decorators/persistent/wrapper.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L45)

Object that stores keys of all properties that have already been fetched from the storage

### Protected Optional Readonly ttl

ttl?: number

* Defined in [src/core/cache/decorators/persistent/wrapper.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L25)

Default TTL to store items

### Protected Readonly wrappedCache

wrappedCache: [PersistentCache](../modules/src_core_cache_decorators_persistent_interface.html#PersistentCache)<V, string, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, string, [default](../interfaces/src_core_cache_interface.default.html)<V, string>>>

* Defined in [src/core/cache/decorators/persistent/wrapper.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L35)

Wrapped cache object

## Methods

### Protected checkItemInStorage

* checkItemInStorage(key: string): Promise<void>

* + Defined in [src/core/cache/decorators/persistent/wrapper.ts:170](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L170)

  Checks a cache item by the specified key in the persistent storage

  #### Parameters

  + ##### key: string

  #### Returns Promise<void>

### Protected getDefaultImplementation

* getDefaultImplementation(method: "has"): (key: string) => Promise<boolean>
* getDefaultImplementation(method: "get"): (key: string) => Promise<[CanUndef](../modules/index.html#CanUndef)<V>>

* + Defined in [src/core/cache/decorators/persistent/wrapper.ts:144](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L144)

  Returns the default implementation for the specified cache method with adding a feature of persistent storing

  #### Parameters

  + ##### method: "has"

  #### Returns (key: string) => Promise<boolean>

  + - (key: string): Promise<boolean>
    - Returns the default implementation for the specified cache method with adding a feature of persistent storing

      #### Parameters

      * ##### key: string

      #### Returns Promise<boolean>
* + Defined in [src/core/cache/decorators/persistent/wrapper.ts:145](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L145)

  #### Parameters

  + ##### method: "get"

  #### Returns (key: string) => Promise<[CanUndef](../modules/index.html#CanUndef)<V>>

  + - (key: string): Promise<[CanUndef](../modules/index.html#CanUndef)<V>>
    - #### Parameters

      * ##### key: string

      #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<V>>

### getInstance

* getInstance(): Promise<[PersistentCache](../modules/src_core_cache_decorators_persistent_interface.html#PersistentCache)<V, string, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, string, [default](../interfaces/src_core_cache_interface.default.html)<V, string>>>>

* + Defined in [src/core/cache/decorators/persistent/wrapper.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L64)

  Returns an instance of the wrapped cache

  #### Returns Promise<[PersistentCache](../modules/src_core_cache_decorators_persistent_interface.html#PersistentCache)<V, string, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, string, [default](../interfaces/src_core_cache_interface.default.html)<V, string>>>>

### Protected implementAPI

* implementAPI(): void

* + Defined in [src/core/cache/decorators/persistent/wrapper.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/wrapper.ts#L76)

  Implements API of the wrapped cache object

  #### Returns void