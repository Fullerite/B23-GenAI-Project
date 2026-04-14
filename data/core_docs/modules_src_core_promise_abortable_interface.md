# Module src/core/promise/abortable/interface
## Index

### Enumerations

* [State](../enums/src_core_promise_abortable_interface.State.html)

### Interfaces

* [ConstrAbortHandler](../interfaces/src_core_promise_abortable_interface.ConstrAbortHandler.html)
* [ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)
* [ConstrResolveHandler](../interfaces/src_core_promise_abortable_interface.ConstrResolveHandler.html)
* [Executor](../interfaces/src_core_promise_abortable_interface.Executor.html)

### Type aliases

* [ExecutableValue](src_core_promise_abortable_interface.html#ExecutableValue)
* [RejectHandler](src_core_promise_abortable_interface.html#RejectHandler)
* [ResolveHandler](src_core_promise_abortable_interface.html#ResolveHandler)
* [Value](src_core_promise_abortable_interface.html#Value)

## Type aliases

### ExecutableValue

ExecutableValue<T>: (() => T) | [Value](src_core_promise_abortable_interface.html#Value)<T>

* Defined in [src/core/promise/abortable/interface.ts:16](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/interface.ts#L16)

#### Type parameters

* #### T = unknown

### RejectHandler

RejectHandler<T>: [ResolveHandler](src_core_promise_abortable_interface.html#ResolveHandler)<unknown, T>

* Defined in [src/core/promise/abortable/interface.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/interface.ts#L39)

#### Type parameters

* #### T = unknown

### ResolveHandler

ResolveHandler<V, R>: Function | ((value: V) => [Value](src_core_promise_abortable_interface.html#Value)<R>)

* Defined in [src/core/promise/abortable/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/interface.ts#L38)

#### Type parameters

* #### V = unknown
* #### R = V

### Value

Value<T>: [CanPromiseLike](index.html#CanPromiseLike)<T>

* Defined in [src/core/promise/abortable/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/interface.ts#L15)

#### Type parameters

* #### T = unknown