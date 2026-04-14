# Module src/core/prelude/structures/sync-promise/interface
## Index

### Enumerations

* [State](../enums/src_core_prelude_structures_sync_promise_interface.State.html)

### Interfaces

* [ConstrRejectHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrRejectHandler.html)
* [ConstrResolveHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrResolveHandler.html)
* [Executor](../interfaces/src_core_prelude_structures_sync_promise_interface.Executor.html)

### Type aliases

* [RejectHandler](src_core_prelude_structures_sync_promise_interface.html#RejectHandler)
* [ResolveHandler](src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)
* [Value](src_core_prelude_structures_sync_promise_interface.html#Value)

## Type aliases

### RejectHandler

RejectHandler<T>: [ResolveHandler](src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<unknown, T>

* Defined in [src/core/prelude/structures/sync-promise/interface.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/interface.ts#L30)

#### Type parameters

* #### T = unknown

### ResolveHandler

ResolveHandler<V, R>: Function | ((value: V) => [Value](src_core_prelude_structures_sync_promise_interface.html#Value)<R>)

* Defined in [src/core/prelude/structures/sync-promise/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/interface.ts#L29)

#### Type parameters

* #### V = unknown
* #### R = V

### Value

Value<T>: [CanPromiseLike](index.html#CanPromiseLike)<T>

* Defined in [src/core/prelude/structures/sync-promise/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/interface.ts#L15)

#### Type parameters

* #### T = unknown