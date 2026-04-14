# Module src/core/cache/decorators/persistent
[# core/cache/decorators/persistent](#corecachedecoratorspersistent)

This module provides a wrapper for [Cache](src_core_cache.html#Cache) data structures to add a feature of persistent data storing.
To describe how long should keep an item in the persistent cache, use the `persistentTTL` parameter.
The value for `persistentTTL` should be provided in milliseconds.

[## Example](#example)

```
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
const  
  opts = {loadFromStorage: 'onInit'},  
  persistentCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
  
await persistentCache.set('foo', 'bar', {persistentTTL: (2).seconds()});  
await persistentCache.set('foo2', 'bar2');  
  
// Cause we use the same instance for the local data storing,  
// this cache will have all values from the previous (it will be loaded from the storage during initialization)  
  
const  
  copyOfCache = await addPersistent(new SimpleCache(), asyncLocal, opts);
```

[## Options](#options)
[### persistentTTL](#persistentttl)

The option specifies the default TTL to keep items within the persistent storage in milliseconds.
This value is used when you don't provide the `persistentTTL` parameter when saving an item.

```
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
const persistentCache = await addPersistent(new SimpleCache(), asyncLocal, {  
  persistentTTL: (60).seconds()  
});  
  
// If we "reload" the cache from the storage by using the browser reloading or another way,  
// these saved values can be "restored" from the storage only for the next 60 seconds  
await persistentCache.set('foo', 'bar');  
await persistentCache.set('foo2', 'bar2');
```

[### loadFromStorage](#loadfromstorage)

There is more than one way to initialize a cache from persistent storage.
The most obvious way to do it is to load all data from the storage to RAM during the cache's initialization.
This strategy is simple but not effective cause if we can have a huge amount of data in the storage,
so we have to load it all at the same time. This can be very expensive. We need another way.
But what if we load an item from the cache only when it is requested the first time.
In that case, we haven't to load the whole stored data on cache initialization,
but all cache methods will change API - they will become return promises instead of the raw results.
Some consumers cannot be ready for changing API, so there is no silver bullet. We have to keep both strategies.

[#### onInit](#oninit)

The whole stored data will be loaded during the cache initialization
Notice, cause the loading from the storage is an asynchronous operation, `addPersistent` will return a promise
if used the `onInit` strategy.

```
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
const  
  opts = {loadFromStorage: 'onInit'};  
  persistentCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
  
await persistentCache.set('foo', 'bar');  
await persistentCache.set('foo2', 'bar2');  
  
// All properties already in our `Simple` cache  
const copyOfCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
  
console.log(copyOfCache.get('foo') === 'bar');
```

[#### onDemand](#ondemand)

Each stored item will be loaded from the cache only on the first touch, i.e. on-demand or lazily.
This is the default strategy.

```
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
const persistentCache = await addPersistent(new SimpleCache(), asyncLocal);  
  
await persistentCache.set('foo', 'bar');  
await persistentCache.set('foo2', 'bar2');  
  
const copyOfCache = await addPersistent(new SimpleCache(), asyncLocal);  
  
console.log(await copyOfCache.get('foo') === 'bar');
```

[#### onOfflineDemand](#onofflinedemand)

Each stored item will be loaded from the cache only on the first touch and only if there is no internet connection.
The strategy is useful to create net-first offline storages.

```
import { isOnline } from 'core/net';  
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
const  
  opts = {loadFromStorage: 'onOfflineDemand'},  
  persistentCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
  
await persistentCache.set('foo', 'bar');  
await persistentCache.set('foo2', 'bar2');  
  
const copyOfCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
  
if ((await isOnline()).status) {  
  console.log(await copyOfCache.get('foo') !== 'bar');  
  
} else {  
  console.log(await copyOfCache.get('foo') === 'bar');  
}
```

## Index

### References

* [PersistentCache](src_core_cache_decorators_persistent.html#PersistentCache)
* [PersistentOptions](src_core_cache_decorators_persistent.html#PersistentOptions)
* [PersistentTTLDecoratorOptions](src_core_cache_decorators_persistent.html#PersistentTTLDecoratorOptions)

### Functions

* [default](src_core_cache_decorators_persistent.html#default)

## References

### PersistentCache

Re-exports [PersistentCache](src_core_cache_decorators_persistent_interface.html#PersistentCache)

### PersistentOptions

Re-exports [PersistentOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentOptions.html)

### PersistentTTLDecoratorOptions

Re-exports [PersistentTTLDecoratorOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentTTLDecoratorOptions.html)

## Functions

### default

* default<V>(cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>, storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](src_core_kv_storage_interface.html#AsyncStorageNamespace), opts?: [PersistentOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentOptions.html)): Promise<[PersistentCache](src_core_cache_decorators_persistent_interface.html#PersistentCache)<V, string, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, string, [default](../interfaces/src_core_cache_interface.default.html)<V, string>>>>

* + Defined in [src/core/cache/decorators/persistent/index.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/index.ts#L52)

  Wraps the specified cache object to add a feature of persistent data storing

  example
  :   ```
      import { asyncLocal } from 'core/kv-storage';  
        
      import addPersistent from 'core/cache/decorators/persistent';  
      import SimpleCache from 'core/cache/simple';  
        
      const  
        opts = {loadFromStorage: 'onInit'},  
        persistentCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
        
      await persistentCache.set('foo', 'bar', {persistentTTL: (2).seconds()});  
      await persistentCache.set('foo2', 'bar2');  
        
      // Because we use the same instance for the local data storing,  
      // this cache will have all values from the previous (it will be loaded from the storage during initialization)  
        
      const  
        copyOfCache = await addPersistent(new SimpleCache(), asyncLocal, opts);
      ```

  #### Type parameters

  + #### V

    value type of the cache object

  #### Parameters

  + ##### cache: [default](../interfaces/src_core_cache_interface.default.html)<V, string>

    cache object to wrap
  + ##### storage: [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html) | [AsyncStorageNamespace](src_core_kv_storage_interface.html#AsyncStorageNamespace)

    storage to save data
  + ##### Optional opts: [PersistentOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentOptions.html)

  #### Returns Promise<[PersistentCache](src_core_cache_decorators_persistent_interface.html#PersistentCache)<V, string, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, string, [default](../interfaces/src_core_cache_interface.default.html)<V, string>>>>