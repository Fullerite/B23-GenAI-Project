# Class default
Implementation of persistent asynchronous key-value storage based on IndexedDB

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#constructor)

### Properties

* [db](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#db)
* [storeName](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#storeName)

### Methods

* [clear](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#clear)
* [get](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#get)
* [getStore](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#getStore)
* [keys](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#keys)
* [remove](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#remove)
* [set](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html#set)

## Constructors

### constructor

* new default(\_\_namedParameters?: [AsyncEngineOptions](../interfaces/src_core_kv_storage_engines_browser_indexeddb_interface.AsyncEngineOptions.html)): [default](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html)

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L24)

  #### Parameters

  + ##### \_\_namedParameters: [AsyncEngineOptions](../interfaces/src_core_kv_storage_engines_browser_indexeddb_interface.AsyncEngineOptions.html) = {}

  #### Returns [default](src_core_kv_storage_engines_browser_indexeddb_async_engine.default.html)

## Properties

### Protected db

db: Promise<IDBDatabase>

* Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L20)

### Protected storeName

storeName: string

* Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L22)

## Methods

### clear

* clear(): Promise<void>

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:91](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L91)

  #### Returns Promise<void>

### get

* get(key: IDBValidKey): Promise<unknown>

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L46)

  #### Parameters

  + ##### key: IDBValidKey

  #### Returns Promise<unknown>

### Protected getStore

* getStore(mode: [StoreMode](../modules/src_core_kv_storage_engines_browser_indexeddb_interface.html#StoreMode)): Promise<IDBObjectStore>

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L96)

  #### Parameters

  + ##### mode: [StoreMode](../modules/src_core_kv_storage_engines_browser_indexeddb_interface.html#StoreMode)

  #### Returns Promise<IDBObjectStore>

### keys

* keys(): Promise<IDBValidKey[]>

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L61)

  #### Returns Promise<IDBValidKey[]>

### remove

* remove(key: IDBValidKey): Promise<void>

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L56)

  #### Parameters

  + ##### key: IDBValidKey

  #### Returns Promise<void>

### set

* set(key: IDBValidKey, value: unknown): Promise<void>

* + Defined in [src/core/kv-storage/engines/browser-indexeddb/async-engine.ts:51](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/engines/browser-indexeddb/async-engine.ts#L51)

  #### Parameters

  + ##### key: IDBValidKey
  + ##### value: unknown

  #### Returns Promise<void>