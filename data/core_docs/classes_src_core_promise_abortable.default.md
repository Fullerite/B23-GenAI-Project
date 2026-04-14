# Class default<T>
Class wraps promise-like objects and adds to them some extra functionality,
such as possibility of cancellation, etc.

### Type parameters

* #### T = unknown

  promise resolved value

### Hierarchy

* default

### Implements

* Promise<T>

## Index

### Constructors

* [constructor](src_core_promise_abortable.default.html#constructor)

### Properties

* [[toStringTag]](src_core_promise_abortable.default.html#_toStringTag_)
* [aborted](src_core_promise_abortable.default.html#aborted)
* [onAbort](src_core_promise_abortable.default.html#onAbort)
* [onReject](src_core_promise_abortable.default.html#onReject)
* [onResolve](src_core_promise_abortable.default.html#onResolve)
* [pendingChildren](src_core_promise_abortable.default.html#pendingChildren)
* [promise](src_core_promise_abortable.default.html#promise)
* [state](src_core_promise_abortable.default.html#state)
* [value](src_core_promise_abortable.default.html#value)

### Accessors

* [isPending](src_core_promise_abortable.default.html#isPending)

### Methods

* [abort](src_core_promise_abortable.default.html#abort)
* [call](src_core_promise_abortable.default.html#call)
* [catch](src_core_promise_abortable.default.html#catch)
* [finally](src_core_promise_abortable.default.html#finally)
* [then](src_core_promise_abortable.default.html#then)
* [all](src_core_promise_abortable.default.html#all)
* [allSettled](src_core_promise_abortable.default.html#allSettled)
* [any](src_core_promise_abortable.default.html#any)
* [race](src_core_promise_abortable.default.html#race)
* [reject](src_core_promise_abortable.default.html#reject)
* [resolve](src_core_promise_abortable.default.html#resolve)
* [resolveAndCall](src_core_promise_abortable.default.html#resolveAndCall)
* [wrapReasonToIgnore](src_core_promise_abortable.default.html#wrapReasonToIgnore)

## Constructors

### constructor

* new default<T>(executor: [Executor](../interfaces/src_core_promise_abortable_interface.Executor.html)<T>, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<T>

* + Defined in [src/core/promise/abortable/index.ts:407](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L407)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### executor: [Executor](../interfaces/src_core_promise_abortable_interface.Executor.html)<T>

    executor function
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<T>

## Properties

### Readonly [toStringTag]

[toStringTag]: "Promise"

Implementation of Promise.\_\_@toStringTag@751

* Defined in [src/core/promise/abortable/index.ts:354](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L354)

override

### Protected aborted

aborted: boolean = false

* Defined in [src/core/promise/abortable/index.ts:381](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L381)

If true, then the promise was aborted

### Protected onAbort

onAbort: [ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)

* Defined in [src/core/promise/abortable/index.ts:401](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L401)

Handler of the native promise rejection that was raised by a reason of abort

### Protected onReject

onReject: [ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)

* Defined in [src/core/promise/abortable/index.ts:396](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L396)

Handler of the native promise rejection

### Protected onResolve

onResolve: [ConstrResolveHandler](../interfaces/src_core_promise_abortable_interface.ConstrResolveHandler.html)<T>

* Defined in [src/core/promise/abortable/index.ts:391](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L391)

Handler of the native promise resolving

### Protected pendingChildren

pendingChildren: number = 0

* Defined in [src/core/promise/abortable/index.ts:366](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L366)

Number of pending child promises

### Protected promise

promise: Promise<T>

* Defined in [src/core/promise/abortable/index.ts:386](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L386)

Internal native promise instance

### Protected state

state: [State](../enums/src_core_promise_abortable_interface.State.html) = State.pending

* Defined in [src/core/promise/abortable/index.ts:371](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L371)

Actual promise state

### Protected value

value: unknown

* Defined in [src/core/promise/abortable/index.ts:376](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L376)

Resolved promise value

## Accessors

### isPending

* get isPending(): boolean

* + Defined in [src/core/promise/abortable/index.ts:359](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L359)

  True if the current promise is pending

  #### Returns boolean

## Methods

### abort

* abort(reason?: unknown): boolean

* + Defined in [src/core/promise/abortable/index.ts:617](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L617)

  Aborts the current promise (the promise will be rejected)

  #### Parameters

  + ##### Optional reason: unknown

  #### Returns boolean

### Protected call

* call<A, V>(fn: [Nullable](../modules/index.html#Nullable)<Function>, args?: A[], onError?: [ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html), onValue?: [AnyOneArgFunction](../interfaces/index.AnyOneArgFunction.html)<V, any>): void

* + Defined in [src/core/promise/abortable/index.ts:649](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L649)

  Executes a function with the specified parameters

  #### Type parameters

  + #### A = unknown
  + #### V = unknown

  #### Parameters

  + ##### fn: [Nullable](../modules/index.html#Nullable)<Function>
  + ##### args: A[] = []

    arguments for the function
  + ##### Optional onError: [ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)
  + ##### Optional onValue: [AnyOneArgFunction](../interfaces/index.AnyOneArgFunction.html)<V, any>

  #### Returns void

### catch

* catch<R>(onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>): [default](src_core_promise_abortable.default.html)<R>
* catch(onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<T>>): [default](src_core_promise_abortable.default.html)<T>

* Implementation of Promise.catch

  + Defined in [src/core/promise/abortable/index.ts:566](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L566)

  Attaches a handler for the promise' rejected state.
  The method returns a new promise that will be resolved with a value that returns from the passed handler.

  #### Type parameters

  + #### R

  #### Parameters

  + ##### onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>

  #### Returns [default](src_core_promise_abortable.default.html)<R>
* Implementation of Promise.catch

  + Defined in [src/core/promise/abortable/index.ts:567](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L567)

  #### Parameters

  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<T>>

  #### Returns [default](src_core_promise_abortable.default.html)<T>

### finally

* finally(cb?: [Nullable](../modules/index.html#Nullable)<Function>): [default](src_core_promise_abortable.default.html)<T>

* Implementation of Promise.finally

  + Defined in [src/core/promise/abortable/index.ts:596](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L596)

  Attaches a common callback for the promise fulfilled and rejected states.
  The method returns a new promise with the state and value from the current.
  A value from the passed callback will be ignored unless it equals a rejected promise or exception.

  #### Parameters

  + ##### Optional cb: [Nullable](../modules/index.html#Nullable)<Function>

  #### Returns [default](src_core_promise_abortable.default.html)<T>

### then

* then<R>(onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, T>>, onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](src_core_promise_abortable.default.html)<T | R>
* then<V>(onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, V>, onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<V>>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](src_core_promise_abortable.default.html)<V>
* then<V, R>(onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, V>, onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](src_core_promise_abortable.default.html)<V | R>
* then(onFulfilled?: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, T>>, onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<T>>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](src_core_promise_abortable.default.html)<T>

* Implementation of Promise.then

  + Defined in [src/core/promise/abortable/index.ts:499](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L499)

  Attaches handlers for the promise fulfilled and/or rejected states.
  The method returns a new promise that will be resolved with a value that returns from the passed handlers.

  #### Type parameters

  + #### R

  #### Parameters

  + ##### onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, T>>
  + ##### onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](src_core_promise_abortable.default.html)<T | R>
* Implementation of Promise.then

  + Defined in [src/core/promise/abortable/index.ts:505](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L505)

  #### Type parameters

  + #### V

  #### Parameters

  + ##### onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, V>
  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<V>>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](src_core_promise_abortable.default.html)<V>
* Implementation of Promise.then

  + Defined in [src/core/promise/abortable/index.ts:511](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L511)

  #### Type parameters

  + #### V
  + #### R

  #### Parameters

  + ##### onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, V>
  + ##### onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](src_core_promise_abortable.default.html)<V | R>
* Implementation of Promise.then

  + Defined in [src/core/promise/abortable/index.ts:517](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L517)

  #### Parameters

  + ##### Optional onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<T, T>>
  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<T>>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](src_core_promise_abortable.default.html)<T>

### Static all

* all<T>(values: T, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<{ [ K in string | number | symbol]: Awaited<T[K]> }>
* all<T>(values: T, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<(T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? V : unknown)[]>

* + Defined in [src/core/promise/abortable/index.ts:127](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L127)

  Takes an iterable of promises and returns a single AbortablePromise that resolves to an array of the results
  of the input promises. This returned promise will resolve when all the input's promises have been resolved or
  if the input iterable contains no promises. It rejects immediately upon any of the input promises rejecting or
  non-promises throwing an error and will reject with this first rejection message/error.

  #### Type parameters

  + #### T: any[] | []

  #### Parameters

  + ##### values: T
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<{ [ K in string | number | symbol]: Awaited<T[K]> }>
* + Defined in [src/core/promise/abortable/index.ts:132](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L132)

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<(T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? V : unknown)[]>

### Static allSettled

* allSettled<T>(values: T, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<{ [ K in string | number | symbol]: PromiseSettledResult<Awaited<T[K]>> }>
* allSettled<T>(values: T, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<(T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? PromiseSettledResult<V> : PromiseSettledResult<unknown>)[]>

* + Defined in [src/core/promise/abortable/index.ts:195](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L195)

  Returns a promise that resolves after all the given promises have either been fulfilled or rejected,
  with an array of objects describing each promise's outcome.

  It is typically used when you have multiple asynchronous tasks that are not dependent on one another to
  complete successfully, or you'd always like to know the result of each promise.

  In comparison, the AbortablePromise returned by `AbortablePromise.all()` may be more appropriate
  if the tasks are dependent on each other / if you'd like to reject upon any of them reject immediately.

  #### Type parameters

  + #### T: any[] | []

  #### Parameters

  + ##### values: T
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<{ [ K in string | number | symbol]: PromiseSettledResult<Awaited<T[K]>> }>
* + Defined in [src/core/promise/abortable/index.ts:200](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L200)

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<(T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? PromiseSettledResult<V> : PromiseSettledResult<unknown>)[]>

### Static any

* any<T>(values: T, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? V : unknown>

* + Defined in [src/core/promise/abortable/index.ts:313](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L313)

  Creates a promise that is resolved when any of the provided promises are resolved or
  rejected if the provided all promises are rejected

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? V : unknown>

### Static race

* race<T>(values: T, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? V : unknown>

* + Defined in [src/core/promise/abortable/index.ts:276](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L276)

  Creates an abortable promise that is resolved or rejected when any of the provided promises are resolved or
  rejected

  #### Type parameters

  + #### T: Iterable<unknown, T>

  #### Parameters

  + ##### values: T
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<T extends Iterable<[Value](../modules/src_core_promise_abortable_interface.html#Value)<V>> ? V : unknown>

### Static reject

* reject<T>(reason?: unknown, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<T>

* + Defined in [src/core/promise/abortable/index.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L114)

  Returns an AbortablePromise object that is rejected with a given reason

  #### Type parameters

  + #### T = never

  #### Parameters

  + ##### Optional reason: unknown
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<T>

### Static resolve

* resolve<T>(value: [Value](../modules/src_core_promise_abortable_interface.html#Value)<T>, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<T>
* resolve(): [default](src_core_promise_abortable.default.html)<void>

* + Defined in [src/core/promise/abortable/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L65)

  Returns an AbortablePromise object that is resolved with a given value.

  If the value is a promise, that promise is returned; if the value is a thenable (i.e., has a "then" method),
  the returned promise will "follow" that thenable, adopting its eventual state; otherwise,
  the returned promise will be fulfilled with the value.

  This function flattens nested layers of promise-like objects
  (e.g., a promise that resolves to a promise that resolves to something) into a single layer.

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### value: [Value](../modules/src_core_promise_abortable_interface.html#Value)<T>
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<T>
* + Defined in [src/core/promise/abortable/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L70)

  Returns a new resolved AbortablePromise object with an undefined value

  #### Returns [default](src_core_promise_abortable.default.html)<void>

### Static resolveAndCall

* resolveAndCall<T>(value: [ExecutableValue](../modules/src_core_promise_abortable_interface.html#ExecutableValue)<T>, parent?: [default](src_core_promise_abortable.default.html)<unknown>): [default](src_core_promise_abortable.default.html)<T>
* resolveAndCall(): [default](src_core_promise_abortable.default.html)<void>

* + Defined in [src/core/promise/abortable/index.ts:98](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L98)

  Returns an AbortablePromise object that is resolved with a given value.
  If the resolved value is a function, it will be invoked.
  The result of the invoking will be provided as a value of the promise.

  If the value is a promise, that promise is returned; if the value is a thenable (i.e., has a "then" method),
  the returned promise will "follow" that thenable, adopting its eventual state; otherwise,
  the returned promise will be fulfilled with the value.

  This function flattens nested layers of promise-like objects
  (e.g., a promise that resolves to a promise that resolves to something) into a single layer.

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### value: [ExecutableValue](../modules/src_core_promise_abortable_interface.html#ExecutableValue)<T>
  + ##### Optional parent: [default](src_core_promise_abortable.default.html)<unknown>

  #### Returns [default](src_core_promise_abortable.default.html)<T>
* + Defined in [src/core/promise/abortable/index.ts:103](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L103)

  Returns a new resolved AbortablePromise object with an undefined value

  #### Returns [default](src_core_promise_abortable.default.html)<void>

### Static wrapReasonToIgnore

* wrapReasonToIgnore<T>(reason: T): T

* + Defined in [src/core/promise/abortable/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L47)

  The method wraps the specified abort reason to ignore with tied promises,
  i.e., this reason won't reject all child promises

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### reason: T

  #### Returns T