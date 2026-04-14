# Class default<V>
### Type parameters

* #### V

### Hierarchy

* [default](src_core_cache_decorators_persistent_engines_lazy.default.html)<V>
  + default

## Index

### Constructors

* [constructor](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#constructor)

### Properties

* [async](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#async)
* [pending](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#pending)
* [storage](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#storage)

### Methods

* [execTask](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#execTask)
* [get](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#get)
* [getCheckStorageState](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#getCheckStorageState)
* [getTTLFrom](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#getTTLFrom)
* [initCache](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#initCache)
* [normalizeTTL](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#normalizeTTL)
* [remove](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#remove)
* [removeTTLFrom](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#removeTTLFrom)
* [set](src_core_cache_decorators_persistent_engines_lazy_offline.default.html#set)

## Constructors

### constructor

* new default<V>(storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)): [default](src_core_cache_decorators_persistent_engines_lazy_offline.default.html)<V>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[constructor](src_core_cache_decorators_persistent_engines_lazy.default.html#constructor)

  + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L38)

  #### Type parameters

  + #### V

  #### Parameters

  + ##### storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

  #### Returns [default](src_core_cache_decorators_persistent_engines_lazy_offline.default.html)<V>

## Properties

### Protected async

async: [default](src_core_async.default.html)<[default](src_core_async.default.html)<any>> = ...

Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[async](src_core_cache_decorators_persistent_engines_lazy.default.html#async)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L26)

API for async operations

### Protected Readonly pending

pending: Map<string, Promise<unknown>> = ...

Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[pending](src_core_cache_decorators_persistent_engines_lazy.default.html#pending)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L36)

Map of pending operations by keys

### Protected Readonly storage

storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[storage](src_core_cache_decorators_persistent_engines_lazy.default.html#storage)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L31)

API to store data

## Methods

### Protected execTask

* execTask<T>(key: string, task: () => [CanPromise](../modules/index.html#CanPromise)<T>): Promise<T>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[execTask](src_core_cache_decorators_persistent_engines_lazy.default.html#execTask)

  + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:93](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L93)

  Registers a task to update a cache item by the specified key

  #### Type parameters

  + #### T

  #### Parameters

  + ##### key: string
  + ##### task: () => [CanPromise](../modules/index.html#CanPromise)<T>

    function that doing something with the storage

    - * (): [CanPromise](../modules/index.html#CanPromise)<T>
      * #### Returns [CanPromise](../modules/index.html#CanPromise)<T>

  #### Returns Promise<T>

### get

* get<T>(key: string): Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[get](src_core_cache_decorators_persistent_engines_lazy.default.html#get)

  + Defined in [src/core/cache/decorators/persistent/engines/lazy.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/lazy.ts#L15)

  Returns a value from the storage by the specified key.
  Before checking the storage, the method will ask `getCheckStorageState` for permissions to do it.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### key: string

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

### getCheckStorageState

* getCheckStorageState(): Promise<[StorageCheckState](../modules/src_core_cache_decorators_persistent_engines_interface.html#StorageCheckState)>

* Overrides [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[getCheckStorageState](src_core_cache_decorators_persistent_engines_lazy.default.html#getCheckStorageState)

  + Defined in [src/core/cache/decorators/persistent/engines/lazy-offline.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/lazy-offline.ts#L15)

  This method is called before every operation that checks data from the storage, like, `has` or `get`

  #### Returns Promise<[StorageCheckState](../modules/src_core_cache_decorators_persistent_engines_interface.html#StorageCheckState)>

### getTTLFrom

* getTTLFrom(key: string): Promise<[CanUndef](../modules/index.html#CanUndef)<number>>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[getTTLFrom](src_core_cache_decorators_persistent_engines_lazy.default.html#getTTLFrom)

  + Defined in [src/core/cache/decorators/persistent/engines/lazy.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/lazy.ts#L46)

  Returns a value of the `persistentTTL` descriptor by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<number>>

### Optional initCache

* initCache(cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>): [CanPromise](../modules/index.html#CanPromise)<void>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[initCache](src_core_cache_decorators_persistent_engines_lazy.default.html#initCache)

  + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L19)

  Initializes a new cache instance from the past one

  #### Parameters

  + ##### cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>

  #### Returns [CanPromise](../modules/index.html#CanPromise)<void>

### Protected normalizeTTL

* normalizeTTL(ttl: [Nullable](../modules/index.html#Nullable)<number>): number

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[normalizeTTL](src_core_cache_decorators_persistent_engines_lazy.default.html#normalizeTTL)

  + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L76)

  Normalized the given TTL value and returns it

  #### Parameters

  + ##### ttl: [Nullable](../modules/index.html#Nullable)<number>

  #### Returns number

### remove

* remove(key: string): Promise<void>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[remove](src_core_cache_decorators_persistent_engines_lazy.default.html#remove)

  + Defined in [src/core/cache/decorators/persistent/engines/lazy.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/lazy.ts#L35)

  Removes a value from the storage by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<void>

### removeTTLFrom

* removeTTLFrom(key: string): Promise<boolean>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[removeTTLFrom](src_core_cache_decorators_persistent_engines_lazy.default.html#removeTTLFrom)

  + Defined in [src/core/cache/decorators/persistent/engines/lazy.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/lazy.ts#L50)

  Removes the `persistentTTL` descriptor from a cache item by the specified key.
  The method returns `true` if the operation has been successful, otherwise `false`
  (the requested item hasn't been found).

  #### Parameters

  + ##### key: string

  #### Returns Promise<boolean>

### set

* set(key: string, value: V, ttl?: number): Promise<void>

* Inherited from [default](src_core_cache_decorators_persistent_engines_lazy.default.html).[set](src_core_cache_decorators_persistent_engines_lazy.default.html#set)

  + Defined in [src/core/cache/decorators/persistent/engines/lazy.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/lazy.ts#L19)

  Sets a value to the storage by the specified key and ttl

  #### Parameters

  + ##### key: string
  + ##### value: V
  + ##### Optional ttl: number

  #### Returns Promise<void>