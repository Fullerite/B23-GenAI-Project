# Class default<V>
### Type parameters

* #### V

### Hierarchy

* [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html)<V>
  + default

## Index

### Constructors

* [constructor](src_core_cache_decorators_persistent_engines_active.default.html#constructor)

### Properties

* [async](src_core_cache_decorators_persistent_engines_active.default.html#async)
* [pending](src_core_cache_decorators_persistent_engines_active.default.html#pending)
* [storage](src_core_cache_decorators_persistent_engines_active.default.html#storage)
* [ttlIndex](src_core_cache_decorators_persistent_engines_active.default.html#ttlIndex)

### Methods

* [execTask](src_core_cache_decorators_persistent_engines_active.default.html#execTask)
* [getCheckStorageState](src_core_cache_decorators_persistent_engines_active.default.html#getCheckStorageState)
* [getTTLFrom](src_core_cache_decorators_persistent_engines_active.default.html#getTTLFrom)
* [initCache](src_core_cache_decorators_persistent_engines_active.default.html#initCache)
* [normalizeTTL](src_core_cache_decorators_persistent_engines_active.default.html#normalizeTTL)
* [remove](src_core_cache_decorators_persistent_engines_active.default.html#remove)
* [removeTTLFrom](src_core_cache_decorators_persistent_engines_active.default.html#removeTTLFrom)
* [set](src_core_cache_decorators_persistent_engines_active.default.html#set)

## Constructors

### constructor

* new default<V>(storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)): [default](src_core_cache_decorators_persistent_engines_active.default.html)<V>

* Inherited from [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[constructor](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#constructor)

  + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L38)

  #### Type parameters

  + #### V

  #### Parameters

  + ##### storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

  #### Returns [default](src_core_cache_decorators_persistent_engines_active.default.html)<V>

## Properties

### Protected async

async: [default](src_core_async.default.html)<[default](src_core_async.default.html)<any>> = ...

Inherited from [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[async](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#async)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L26)

API for async operations

### Protected Readonly pending

pending: Map<string, Promise<unknown>> = ...

Inherited from [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[pending](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#pending)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L36)

Map of pending operations by keys

### Protected Readonly storage

storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

Inherited from [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[storage](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#storage)

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L31)

API to store data

### Protected ttlIndex

ttlIndex: [Dictionary](../interfaces/index.Dictionary.html)<number> = ...

* Defined in [src/core/cache/decorators/persistent/engines/active.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L19)

Index with keys and TTL-s of stored values

## Methods

### Protected execTask

* execTask<T>(key: string, task: () => [CanPromise](../modules/index.html#CanPromise)<T>): Promise<T>

* Inherited from [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[execTask](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#execTask)

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

### getCheckStorageState

* getCheckStorageState(): [CanPromise](../modules/index.html#CanPromise)<{ available: false; checked: boolean }>

* Overrides [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[getCheckStorageState](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#getCheckStorageState)

  + Defined in [src/core/cache/decorators/persistent/engines/active.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L83)

  #### Returns [CanPromise](../modules/index.html#CanPromise)<{ available: false; checked: boolean }>

### getTTLFrom

* getTTLFrom(key: string): Promise<[CanUndef](../modules/index.html#CanUndef)<number>>

* Overrides [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[getTTLFrom](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#getTTLFrom)

  + Defined in [src/core/cache/decorators/persistent/engines/active.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L70)

  Returns a value of the `persistentTTL` descriptor by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<number>>

### initCache

* initCache(cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>): Promise<void>

* Overrides [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[initCache](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#initCache)

  + Defined in [src/core/cache/decorators/persistent/engines/active.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L21)

  Initializes a new cache instance from the past one

  #### Parameters

  + ##### cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>

  #### Returns Promise<void>

### Protected normalizeTTL

* normalizeTTL(ttl: [Nullable](../modules/index.html#Nullable)<number>): number

* Inherited from [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[normalizeTTL](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#normalizeTTL)

  + Defined in [src/core/cache/decorators/persistent/engines/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L76)

  Normalized the given TTL value and returns it

  #### Parameters

  + ##### ttl: [Nullable](../modules/index.html#Nullable)<number>

  #### Returns number

### remove

* remove(key: string): Promise<void>

* Overrides [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[remove](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#remove)

  + Defined in [src/core/cache/decorators/persistent/engines/active.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L63)

  Removes a value from the storage by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<void>

### removeTTLFrom

* removeTTLFrom(key: string): Promise<boolean>

* Overrides [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[removeTTLFrom](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#removeTTLFrom)

  + Defined in [src/core/cache/decorators/persistent/engines/active.ts:74](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L74)

  Removes the `persistentTTL` descriptor from a cache item by the specified key.
  The method returns `true` if the operation has been successful, otherwise `false`
  (the requested item hasn't been found).

  #### Parameters

  + ##### key: string

  #### Returns Promise<boolean>

### set

* set(key: string, value: V, ttl?: number): Promise<void>

* Overrides [UncheckablePersistentEngine](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html).[set](src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html#set)

  + Defined in [src/core/cache/decorators/persistent/engines/active.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/active.ts#L52)

  Sets a value to the storage by the specified key and ttl

  #### Parameters

  + ##### key: string
  + ##### value: V
  + ##### Optional ttl: number

  #### Returns Promise<void>