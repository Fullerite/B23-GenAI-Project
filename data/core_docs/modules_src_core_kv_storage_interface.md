# Module src/core/kv-storage/interface
## Index

### Interfaces

* [AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html)
* [ClearFilter](../interfaces/src_core_kv_storage_interface.ClearFilter.html)
* [StorageEngine](../interfaces/src_core_kv_storage_interface.StorageEngine.html)
* [SyncStorage](../interfaces/src_core_kv_storage_interface.SyncStorage.html)
* [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html)

### Type aliases

* [AsyncStorageNamespace](src_core_kv_storage_interface.html#AsyncStorageNamespace)

## Type aliases

### AsyncStorageNamespace

AsyncStorageNamespace: { [ key in Exclude<keyof [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html), "get" | "clear">]: [ReturnPromise](index.html#ReturnPromise)<[SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html)[key]> } & { clear: any; get: any }

* Defined in [src/core/kv-storage/interface.ts:80](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/interface.ts#L80)