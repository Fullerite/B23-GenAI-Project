# Class AbstractPersistentEngine<V>
### Type parameters

* #### V = unknown

### Hierarchy

* AbstractPersistentEngine
  + [CheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.CheckablePersistentEngine.html)
  + [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html)

## Index

### Constructors

* [constructor](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#constructor)

### Properties

* [async](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#async)
* [pending](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#pending)
* [storage](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#storage)

### Methods

* [execTask](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#execTask)
* [getTTLFrom](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#getTTLFrom)
* [initCache](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#initCache)
* [normalizeTTL](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#normalizeTTL)
* [remove](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#remove)
* [removeTTLFrom](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#removeTTLFrom)
* [set](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html#set)

## Constructors

### constructor

* new AbstractPersistentEngine<V>(storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)): [AbstractPersistentEngine](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html)<V>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L38)

  #### Type parameters

  + #### V = unknown

  #### Parameters

  + ##### storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

  #### Returns [AbstractPersistentEngine](src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html)<V>

## Properties

### Protected async

async: [default](src_core_async.default.html)<[default](src_core_async.default.html)<any>> = ...

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L26)

API for async operations

### Protected Readonly pending

pending: Map<string, Promise<unknown>> = ...

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L36)

Map of pending operations by keys

### Protected Readonly storage

storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L31)

API to store data

## Methods

### Protected execTask

* execTask<T>(key: string, task: () => [CanPromise](../modules/index.html#CanPromise)<T>): Promise<T>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:93](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L93)

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

### Abstract getTTLFrom

* getTTLFrom(key: string): Promise<[CanUndef](../modules/index.html#CanUndef)<number>>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L61)

  Returns a value of the `persistentTTL` descriptor by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<number>>

### Optional initCache

* initCache(cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>): [CanPromise](../modules/index.html#CanPromise)<void>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L19)

  Initializes a new cache instance from the past one

  #### Parameters

  + ##### cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>

  #### Returns [CanPromise](../modules/index.html#CanPromise)<void>

### Protected normalizeTTL

* normalizeTTL(ttl: [Nullable](../modules/index.html#Nullable)<number>): number

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L76)

  Normalized the given TTL value and returns it

  #### Parameters

  + ##### ttl: [Nullable](../modules/index.html#Nullable)<number>

  #### Returns number

### Abstract remove

* remove(key: string): Promise<void>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L55)

  Removes a value from the storage by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<void>

### Abstract removeTTLFrom

* removeTTLFrom(key: string): Promise<boolean>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L70)

  Removes the `persistentTTL` descriptor from a cache item by the specified key.
  The method returns `true` if the operation has been successful, otherwise `false`
  (the requested item hasn't been found).

  #### Parameters

  + ##### key: string

  #### Returns Promise<boolean>

### Abstract set

* set(key: string, value: V, ttl?: number): Promise<void>

* + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L49)

  Sets a value to the storage by the specified key and ttl

  #### Parameters

  + ##### key: string
  + ##### value: V
  + ##### Optional ttl: number

  #### Returns Promise<void>