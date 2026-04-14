# Interface AsyncStorage
API for an asynchronous storage

### Hierarchy

* [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)
  + AsyncStorage

## Index

### Properties

* [has](src_core_kv_storage_interface.AsyncStorage.html#has)
* [remove](src_core_kv_storage_interface.AsyncStorage.html#remove)
* [set](src_core_kv_storage_interface.AsyncStorage.html#set)

### Methods

* [clear](src_core_kv_storage_interface.AsyncStorage.html#clear)
* [get](src_core_kv_storage_interface.AsyncStorage.html#get)
* [namespace](src_core_kv_storage_interface.AsyncStorage.html#namespace)

## Properties

### has

has: [ReturnPromise](../modules/index.html#ReturnPromise)<(key: string, ...args: unknown[]) => boolean>

Inherited from AsyncStorageNamespace.has

### remove

remove: [ReturnPromise](../modules/index.html#ReturnPromise)<(key: string, ...args: unknown[]) => void>

Inherited from AsyncStorageNamespace.remove

### set

set: [ReturnPromise](../modules/index.html#ReturnPromise)<(key: string, value: unknown, ...args: unknown[]) => void>

Inherited from AsyncStorageNamespace.set

## Methods

### clear

* clear<T>(filter?: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>, ...args: unknown[]): Promise<void>

* Inherited from AsyncStorageNamespace.clear

  + Defined in [src/core/kv-storage/interface.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L84)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### Optional filter: [ClearFilter](src_core_kv_storage_interface.ClearFilter.html)<T>
  + ##### Rest ...args: unknown[]

  #### Returns Promise<void>

### get

* get<T>(key: string, ...args: unknown[]): Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

* Inherited from AsyncStorageNamespace.get

  + Defined in [src/core/kv-storage/interface.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L83)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### key: string
  + ##### Rest ...args: unknown[]

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

### namespace

* namespace(name: string): [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)

* + Defined in [src/core/kv-storage/interface.ts:95](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L95)

  Returns an async storage object by the specified namespace

  #### Parameters

  + ##### name: string

  #### Returns [AsyncStorageNamespace](../modules/src_core_kv_storage_interface.html#AsyncStorageNamespace)