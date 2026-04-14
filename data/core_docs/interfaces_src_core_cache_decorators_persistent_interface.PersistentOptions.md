# Interface PersistentOptions
### Hierarchy

* PersistentOptions

## Index

### Properties

* [loadFromStorage](src_core_cache_decorators_persistent_interface.PersistentOptions.html#loadFromStorage)
* [persistentTTL](src_core_cache_decorators_persistent_interface.PersistentOptions.html#persistentTTL)

## Properties

### Optional loadFromStorage

loadFromStorage?: "onInit" | "onDemand" | "onOfflineDemand"

* Defined in [src/core/cache/decorators/persistent/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/interface.ts#L63)

How to load cache items from the persistent storage:

1. `'onInit'` - the whole stored data will be loaded during the cache initialization;
2. `'onDemand'` - each stored item will be loaded from the cache only on the first touch, i.e. on-demand or lazily;
3. `'onOfflineDemand'` - each stored item will be loaded from the cache only on the first touch and only if
   there is no internet connection (the strategy is useful to create net-first offline storages)

default
:   `'onDemand'`

### Optional persistentTTL

persistentTTL?: number

* Defined in [src/core/cache/decorators/persistent/interface.ts:51](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/interface.ts#L51)

Default time to expire a cache item in the persistent storage