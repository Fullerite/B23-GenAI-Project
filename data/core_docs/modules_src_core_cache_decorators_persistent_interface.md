# Module src/core/cache/decorators/persistent/interface
## Index

### Interfaces

* [PersistentOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentOptions.html)
* [PersistentTTLDecoratorOptions](../interfaces/src_core_cache_decorators_persistent_interface.PersistentTTLDecoratorOptions.html)

### Type aliases

* [PersistentCache](src_core_cache_decorators_persistent_interface.html#PersistentCache)

## Type aliases

### PersistentCache

PersistentCache<V, K, T>: { [ key in Exclude<keyof [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, K>, "set" | "size" | typeof [eventEmitter](src_core_cache_decorators_helpers_add_emitter_const.html#eventEmitter)>]: [ReturnPromise](index.html#ReturnPromise)<[CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, K>[key]> } & { eventEmitter: T[typeof [eventEmitter](src_core_cache_decorators_helpers_add_emitter_const.html#eventEmitter)]; size: [T["size"]]; removePersistentTTLFrom: any; set: any }

* Defined in [src/core/cache/decorators/persistent/interface.ts:12](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/interface.ts#L12)

#### Type parameters

* #### V = unknown
* #### K = string
* #### T: [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, K> = [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, K>