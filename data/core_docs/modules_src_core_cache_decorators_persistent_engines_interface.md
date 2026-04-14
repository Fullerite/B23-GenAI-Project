# Module src/core/cache/decorators/persistent/engines/interface
## Index

### Classes

* [AbstractPersistentEngine](../classes/src_core_cache_decorators_persistent_engines_interface.AbstractPersistentEngine.html)
* [CheckablePersistentEngine](../classes/src_core_cache_decorators_persistent_engines_interface.CheckablePersistentEngine.html)
* [UncheckablePersistentEngine](../classes/src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html)

### Type aliases

* [PersistentEngine](src_core_cache_decorators_persistent_engines_interface.html#PersistentEngine)
* [StorageCheckState](src_core_cache_decorators_persistent_engines_interface.html#StorageCheckState)

## Type aliases

### PersistentEngine

PersistentEngine<V>: [CheckablePersistentEngine](../classes/src_core_cache_decorators_persistent_engines_interface.CheckablePersistentEngine.html)<V> | [UncheckablePersistentEngine](../classes/src_core_cache_decorators_persistent_engines_interface.UncheckablePersistentEngine.html)<V>

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:160](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L160)

Engine to provide the persistent feature

#### Type parameters

* #### V = unknown

### StorageCheckState

StorageCheckState: { available: false; checked: boolean } | { available: true; checked: true }

* Defined in [src/core/cache/decorators/persistent/engines/interface.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/persistent/engines/interface.ts#L169)

Available checking state of a storage item:

1. `available: false; checked: false` - don't need to check the storage, don't mark the item as checked;
2. `available: false; checked: true` - don't need to check the storage, mark the item as checked;
3. `available: true; checked: true` - check the storage, mark the item is checked.