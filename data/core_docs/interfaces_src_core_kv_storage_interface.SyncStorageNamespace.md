# Interface SyncStorageNamespace
### Hierarchy

* SyncStorageNamespace
  + [SyncStorage](src_core_kv_storage_interface.SyncStorage.html)

## Index

### Methods

* [clear](src_core_kv_storage_interface.SyncStorageNamespace.html#clear)
* [get](src_core_kv_storage_interface.SyncStorageNamespace.html#get)
* [has](src_core_kv_storage_interface.SyncStorageNamespace.html#has)
* [remove](src_core_kv_storage_interface.SyncStorageNamespace.html#remove)
* [set](src_core_kv_storage_interface.SyncStorageNamespace.html#set)

## Methods

### clear

* clear<T>(filter?: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>, ...args: unknown[]): void

* + Defined in [src/core/kv-storage/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L66)

  Clears the storage by the specified filter and returns a list of removed keys.
  Notice, the method can take a list of additional parameters provided to the used storage' engine.

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### Optional filter: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>
  + ##### Rest ...args: unknown[]

  #### Returns void

### get

* get<T>(key: string, ...args: unknown[]): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/kv-storage/interface.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L34)

  Returns a value from the storage by the specified key.

  The returning value automatically parses by using `Object.parse` from a string to equivalent JS value, i.e.,
  `'1'` will be parsed to `1`, `'true'` to `true`, `'2021-07-09T08:15:57.753Z'` to `Date`, etc.

  Notice, the method can take a list of additional parameters provided to the used storage' engine.

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### has

* has(key: string, ...args: unknown[]): boolean

* + Defined in [src/core/kv-storage/interface.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L21)

  Returns true if a value by the specified key exists in the storage.
  Notice, the method can take a list of additional parameters provided to the used storage' engine.

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns boolean

### remove

* remove(key: string, ...args: unknown[]): void

* + Defined in [src/core/kv-storage/interface.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L57)

  Removes a value from the storage by the specified key.
  Notice, the method can take a list of additional parameters provided to the used storage' engine.

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns void

### set

* set(key: string, value: unknown, ...args: unknown[]): void

* + Defined in [src/core/kv-storage/interface.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L48)

  Saves a value to the storage by the specified key.

  The value to parse automatically serializes to a string by using `Object.trySerialize`, i.e.,
  arrays and dictionaries will be serialized to JSON, etc.

  Notice, the method can take a list of additional parameters provided to the used storage' engine.

  #### Parameters

  + ##### key: string
  + ##### value: unknown
  + ##### Rest ...args: unknown[]

  #### Returns void