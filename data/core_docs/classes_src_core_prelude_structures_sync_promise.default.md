# Class default<T>
Class is similar to the native promise class but works synchronously

### Type parameters

* #### T = unknown

### Hierarchy

* default
  + [Option](src_core_prelude_structures_helpers.Option.html)
  + [Result](src_core_prelude_structures_helpers.Result.html)

### Implements

* Promise<T>

## Index

### Constructors

* [constructor](src_core_prelude_structures_sync_promise.default.html#constructor)

### Properties

* [[toStringTag]](src_core_prelude_structures_sync_promise.default.html#_toStringTag_)
* [fulfillHandlers](src_core_prelude_structures_sync_promise.default.html#fulfillHandlers)
* [rejectHandlers](src_core_prelude_structures_sync_promise.default.html#rejectHandlers)
* [state](src_core_prelude_structures_sync_promise.default.html#state)
* [value](src_core_prelude_structures_sync_promise.default.html#value)

### Accessors

* [isPending](src_core_prelude_structures_sync_promise.default.html#isPending)

### Methods

* [call](src_core_prelude_structures_sync_promise.default.html#call)
* [catch](src_core_prelude_structures_sync_promise.default.html#catch)
* [finally](src_core_prelude_structures_sync_promise.default.html#finally)
* [then](src_core_prelude_structures_sync_promise.default.html#then)
* [unwrap](src_core_prelude_structures_sync_promise.default.html#unwrap)
* [all](src_core_prelude_structures_sync_promise.default.html#all)
* [allSettled](src_core_prelude_structures_sync_promise.default.html#allSettled)
* [any](src_core_prelude_structures_sync_promise.default.html#any)
* [race](src_core_prelude_structures_sync_promise.default.html#race)
* [reject](src_core_prelude_structures_sync_promise.default.html#reject)
* [resolve](src_core_prelude_structures_sync_promise.default.html#resolve)

## Constructors

### constructor

* new default<T>(executor: [Executor](../interfaces/src_core_prelude_structures_sync_promise_interface.Executor.html)<unknown>): [default](src_core_prelude_structures_sync_promise.default.html)<T>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:291](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L291)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### executor: [Executor](../interfaces/src_core_prelude_structures_sync_promise_interface.Executor.html)<unknown>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T>

## Properties

### Readonly [toStringTag]

[toStringTag]: "Promise"

Implementation of Promise.\_\_@toStringTag@751

* Defined in [src/core/prelude/structures/sync-promise/index.ts:262](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L262)

override

### Protected fulfillHandlers

fulfillHandlers: [ConstrResolveHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrResolveHandler.html)<unknown>[] = []

* Defined in [src/core/prelude/structures/sync-promise/index.ts:284](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L284)

List of handlers to handle the promise fulfilling

### Protected rejectHandlers

rejectHandlers: [ConstrRejectHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrRejectHandler.html)[] = []

* Defined in [src/core/prelude/structures/sync-promise/index.ts:289](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L289)

List of handlers to handle the promise rejection

### Protected state

state: [State](../enums/src_core_prelude_structures_sync_promise_interface.State.html) = State.pending

* Defined in [src/core/prelude/structures/sync-promise/index.ts:274](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L274)

Actual promise state

### Protected value

value: unknown

* Defined in [src/core/prelude/structures/sync-promise/index.ts:279](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L279)

Resolved promise value

## Accessors

### isPending

* get isPending(): boolean

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:267](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L267)

  True if the current promise is pending

  #### Returns boolean

## Methods

### Protected call

* call<A, V>(fn: [Nullable](../modules/index.html#Nullable)<Function>, args?: A[], onError?: [ConstrRejectHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrRejectHandler.html), onValue?: [AnyOneArgFunction](../interfaces/index.AnyOneArgFunction.html)<V, any>): void

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:504](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L504)

  Executes a function with the specified parameters

  #### Type parameters

  + #### A = unknown
  + #### V = unknown

  #### Parameters

  + ##### fn: [Nullable](../modules/index.html#Nullable)<Function>
  + ##### args: A[] = []

    arguments for the function
  + ##### Optional onError: [ConstrRejectHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrRejectHandler.html)
  + ##### Optional onValue: [AnyOneArgFunction](../interfaces/index.AnyOneArgFunction.html)<V, any>

  #### Returns void

### catch

* catch<R>(onRejected: [RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<R>): [default](src_core_prelude_structures_sync_promise.default.html)<R>
* catch(onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<T>>): [default](src_core_prelude_structures_sync_promise.default.html)<T>

* Implementation of Promise.catch

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:424](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L424)

  Attaches a handler for the promise' rejected state.
  The method returns a new promise that will be resolved with a value that returns from the passed handler.

  #### Type parameters

  + #### R

  #### Parameters

  + ##### onRejected: [RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<R>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<R>
* Implementation of Promise.catch

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:425](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L425)

  #### Parameters

  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<T>>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T>

### finally

* finally(cb?: [Nullable](../modules/index.html#Nullable)<Function>): [default](src_core_prelude_structures_sync_promise.default.html)<T>

* Implementation of Promise.finally

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:448](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L448)

  Attaches a common callback for the promise fulfilled and rejected states.
  The method returns a new promise with the state and value from the current.
  A value from the passed callback will be ignored unless it equals a rejected promise or exception.

  #### Parameters

  + ##### Optional cb: [Nullable](../modules/index.html#Nullable)<Function>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T>

### then

* then<R>(onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, T>>, onRejected: [RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<R>): [default](src_core_prelude_structures_sync_promise.default.html)<T | R>
* then<V>(onFulfilled: [ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, V>, onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<V>>): [default](src_core_prelude_structures_sync_promise.default.html)<V>
* then<V, R>(onFulfilled: [ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, V>, onRejected: [RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<R>): [default](src_core_prelude_structures_sync_promise.default.html)<V | R>
* then(onFulfilled?: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, T>>, onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<T>>): [default](src_core_prelude_structures_sync_promise.default.html)<T>

* Implementation of Promise.then

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:376](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L376)

  Attaches handlers for the promise fulfilled and/or rejected states.
  The method returns a new promise that will be resolved with a value that returns from the passed handlers.

  #### Type parameters

  + #### R

  #### Parameters

  + ##### onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, T>>
  + ##### onRejected: [RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<R>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T | R>
* Implementation of Promise.then

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:381](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L381)

  #### Type parameters

  + #### V

  #### Parameters

  + ##### onFulfilled: [ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, V>
  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<V>>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<V>
* Implementation of Promise.then

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:386](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L386)

  #### Type parameters

  + #### V
  + #### R

  #### Parameters

  + ##### onFulfilled: [ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, V>
  + ##### onRejected: [RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<R>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<V | R>
* Implementation of Promise.then

  + Defined in [src/core/prelude/structures/sync-promise/index.ts:391](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L391)

  #### Parameters

  + ##### Optional onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)<T, T>>
  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_prelude_structures_sync_promise_interface.html#RejectHandler)<T>>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T>

### unwrap

* unwrap(): T

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:351](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L351)

  Returns the promise' value if it is fulfilled, otherwise throws an exception

  #### Returns T

### Static all

* all<T>(values: T): [default](src_core_prelude_structures_sync_promise.default.html)<{ [ K in string | number | symbol]: Awaited<T[K]> }>
* all<T>(values: T): [default](src_core_prelude_structures_sync_promise.default.html)<(T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? V : unknown)[]>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L75)

  Takes an iterable of promises and returns a single SyncPromise that resolves to an array of the results
  of the input promises. This returned promise will resolve when all the input's promises have been resolved or
  if the input iterable contains no promises. It rejects immediately upon any of the input promises rejecting or
  non-promises throwing an error and will reject with this first rejection message/error.

  #### Type parameters

  + #### T: any[] | []

  #### Parameters

  + ##### values: T

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<{ [ K in string | number | symbol]: Awaited<T[K]> }>
* + Defined in [src/core/prelude/structures/sync-promise/index.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L79)

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<(T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? V : unknown)[]>

### Static allSettled

* allSettled<T>(values: T): [default](src_core_prelude_structures_sync_promise.default.html)<{ [ K in string | number | symbol]: PromiseSettledResult<Awaited<T[K]>> }>
* allSettled<T>(values: T): [default](src_core_prelude_structures_sync_promise.default.html)<(T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? PromiseSettledResult<V> : PromiseSettledResult<unknown>)[]>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:132](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L132)

  Returns a promise that resolves after all the given promises have either been fulfilled or rejected,
  with an array of objects describing each promise's outcome.

  It is typically used when you have multiple asynchronous tasks that are not dependent on one another to
  complete successfully, or you'd always like to know the result of each promise.

  In comparison, the SyncPromise returned by `SyncPromise.all()` may be more appropriate
  if the tasks are dependent on each other / if you'd like to reject upon any of them reject immediately.

  #### Type parameters

  + #### T: any[] | []

  #### Parameters

  + ##### values: T

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<{ [ K in string | number | symbol]: PromiseSettledResult<Awaited<T[K]>> }>
* + Defined in [src/core/prelude/structures/sync-promise/index.ts:136](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L136)

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<(T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? PromiseSettledResult<V> : PromiseSettledResult<unknown>)[]>

### Static any

* any<T>(values: T): [default](src_core_prelude_structures_sync_promise.default.html)<T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? V : unknown>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:228](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L228)

  Takes an iterable of SyncPromise objects and, as soon as one of the promises in the iterable fulfills,
  returns a single promise that resolves with the value from that promise. If no promises in the iterable fulfill
  (if all the given promises are rejected), then the returned promise is rejected with an AggregateError,
  a new subclass of Error that groups together individual errors.

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? V : unknown>

### Static race

* race<T>(values: T): [default](src_core_prelude_structures_sync_promise.default.html)<T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? V : unknown>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:198](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L198)

  Returns a promise that fulfills or rejects as soon as one of the promises from the iterable fulfills or rejects,
  with the value or reason from that promise

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T extends Iterable<[Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<V>> ? V : unknown>

### Static reject

* reject<T>(reason?: unknown): [default](src_core_prelude_structures_sync_promise.default.html)<T>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:62](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L62)

  Returns a SyncPromise object that is rejected with a given reason

  #### Type parameters

  + #### T = never

  #### Parameters

  + ##### Optional reason: unknown

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T>

### Static resolve

* resolve<T>(value: [Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<T>): [default](src_core_prelude_structures_sync_promise.default.html)<T>
* resolve(): [default](src_core_prelude_structures_sync_promise.default.html)<void>

* + Defined in [src/core/prelude/structures/sync-promise/index.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L41)

  Returns a SyncPromise object that is resolved with a given value.

  If the value is a promise, that promise is returned; if the value is a thenable (i.e., has a "then" method),
  the returned promise will "follow" that thenable, adopting its eventual state; otherwise,
  the returned promise will be fulfilled with the value.

  This function flattens nested layers of promise-like objects
  (e.g., a promise that resolves to a promise that resolves to something) into a single layer.

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### value: [Value](../modules/src_core_prelude_structures_sync_promise_interface.html#Value)<T>

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<T>
* + Defined in [src/core/prelude/structures/sync-promise/index.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/prelude/structures/sync-promise/index.ts#L46)

  Returns a new resolved SyncPromise object with an undefined value

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<void>