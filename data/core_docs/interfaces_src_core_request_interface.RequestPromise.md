# Interface RequestPromise<D>
### Type parameters

* #### D = unknown

### Hierarchy

* [RequestResponse](../modules/src_core_request_interface.html#RequestResponse)<D>
  + RequestPromise

## Index

### Properties

* [[toStringTag]](src_core_request_interface.RequestPromise.html#_toStringTag_)
* [aborted](src_core_request_interface.RequestPromise.html#aborted)
* [data](src_core_request_interface.RequestPromise.html#data)
* [emitter](src_core_request_interface.RequestPromise.html#emitter)
* [onAbort](src_core_request_interface.RequestPromise.html#onAbort)
* [onReject](src_core_request_interface.RequestPromise.html#onReject)
* [onResolve](src_core_request_interface.RequestPromise.html#onResolve)
* [pendingChildren](src_core_request_interface.RequestPromise.html#pendingChildren)
* [promise](src_core_request_interface.RequestPromise.html#promise)
* [state](src_core_request_interface.RequestPromise.html#state)
* [stream](src_core_request_interface.RequestPromise.html#stream)
* [value](src_core_request_interface.RequestPromise.html#value)

### Accessors

* [isPending](src_core_request_interface.RequestPromise.html#isPending)

### Methods

* [[asyncIterator]](src_core_request_interface.RequestPromise.html#_asyncIterator_)
* [abort](src_core_request_interface.RequestPromise.html#abort)
* [call](src_core_request_interface.RequestPromise.html#call)
* [catch](src_core_request_interface.RequestPromise.html#catch)
* [finally](src_core_request_interface.RequestPromise.html#finally)
* [then](src_core_request_interface.RequestPromise.html#then)

## Properties

### Readonly [toStringTag]

[toStringTag]: "Promise"

Inherited from RequestResponse.\_\_@toStringTag@751

* Defined in [src/core/promise/abortable/index.ts:354](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L354)

override

### Protected aborted

aborted: boolean = false

Inherited from RequestResponse.aborted

* Defined in [src/core/promise/abortable/index.ts:381](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L381)

If true, then the promise was aborted

### data

data: Promise<[Nullable](../modules/index.html#Nullable)<D>>

* Defined in [src/core/request/interface.ts:148](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L148)

### emitter

emitter: EventEmitter2

* Defined in [src/core/request/interface.ts:150](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L150)

### Protected onAbort

onAbort: [ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)

Inherited from RequestResponse.onAbort

* Defined in [src/core/promise/abortable/index.ts:401](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L401)

Handler of the native promise rejection that was raised by a reason of abort

### Protected onReject

onReject: [ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)

Inherited from RequestResponse.onReject

* Defined in [src/core/promise/abortable/index.ts:396](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L396)

Handler of the native promise rejection

### Protected onResolve

onResolve: [ConstrResolveHandler](src_core_promise_abortable_interface.ConstrResolveHandler.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

Inherited from RequestResponse.onResolve

* Defined in [src/core/promise/abortable/index.ts:391](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L391)

Handler of the native promise resolving

### Protected pendingChildren

pendingChildren: number = 0

Inherited from RequestResponse.pendingChildren

* Defined in [src/core/promise/abortable/index.ts:366](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L366)

Number of pending child promises

### Protected promise

promise: Promise<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

Inherited from RequestResponse.promise

* Defined in [src/core/promise/abortable/index.ts:386](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L386)

Internal native promise instance

### Protected state

state: [State](../enums/src_core_promise_abortable_interface.State.html) = State.pending

Inherited from RequestResponse.state

* Defined in [src/core/promise/abortable/index.ts:371](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L371)

Actual promise state

### stream

stream: AsyncIterableIterator<unknown>

* Defined in [src/core/request/interface.ts:149](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L149)

### Protected value

value: unknown

Inherited from RequestResponse.value

* Defined in [src/core/promise/abortable/index.ts:376](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L376)

Resolved promise value

## Accessors

### isPending

* get isPending(): boolean

* Inherited from RequestResponse.isPending

  + Defined in [src/core/promise/abortable/index.ts:359](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L359)

  True if the current promise is pending

  #### Returns boolean

## Methods

### [asyncIterator]

* [asyncIterator](): AsyncIterableIterator<[RequestResponseChunk](src_core_request_interface.RequestResponseChunk.html)>

* + Defined in [src/core/request/interface.ts:151](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L151)

  #### Returns AsyncIterableIterator<[RequestResponseChunk](src_core_request_interface.RequestResponseChunk.html)>

### abort

* abort(reason?: unknown): boolean

* Inherited from RequestResponse.abort

  + Defined in [src/core/promise/abortable/index.ts:617](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L617)

  Aborts the current promise (the promise will be rejected)

  #### Parameters

  + ##### Optional reason: unknown

  #### Returns boolean

### Protected call

* call<A, V>(fn: [Nullable](../modules/index.html#Nullable)<Function>, args?: A[], onError?: [ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html), onValue?: [AnyOneArgFunction](index.AnyOneArgFunction.html)<V, any>): void

* Inherited from RequestResponse.call

  + Defined in [src/core/promise/abortable/index.ts:649](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L649)

  Executes a function with the specified parameters

  #### Type parameters

  + #### A = unknown
  + #### V = unknown

  #### Parameters

  + ##### fn: [Nullable](../modules/index.html#Nullable)<Function>
  + ##### args: A[] = []

    arguments for the function
  + ##### Optional onError: [ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)
  + ##### Optional onValue: [AnyOneArgFunction](index.AnyOneArgFunction.html)<V, any>

  #### Returns void

### catch

* catch<R>(onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>): [default](../classes/src_core_promise_abortable.default.html)<R>
* catch(onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>): [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

* Inherited from RequestResponse.catch

  + Defined in [src/core/promise/abortable/index.ts:566](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L566)

  Attaches a handler for the promise' rejected state.
  The method returns a new promise that will be resolved with a value that returns from the passed handler.

  #### Type parameters

  + #### R

  #### Parameters

  + ##### onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<R>
* Inherited from RequestResponse.catch

  + Defined in [src/core/promise/abortable/index.ts:567](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L567)

  #### Parameters

  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

### finally

* finally(cb?: [Nullable](../modules/index.html#Nullable)<Function>): [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

* Inherited from RequestResponse.finally

  + Defined in [src/core/promise/abortable/index.ts:596](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L596)

  Attaches a common callback for the promise fulfilled and rejected states.
  The method returns a new promise with the state and value from the current.
  A value from the passed callback will be ignored unless it equals a rejected promise or exception.

  #### Parameters

  + ##### Optional cb: [Nullable](../modules/index.html#Nullable)<Function>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

### then

* then<R>(onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, [RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>, onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D> | R>
* then<V>(onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, V>, onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<V>>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](../classes/src_core_promise_abortable.default.html)<V>
* then<V, R>(onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, V>, onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](../classes/src_core_promise_abortable.default.html)<V | R>
* then(onFulfilled?: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, [RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>, onRejected?: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>, onAbort?: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>): [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>

* Inherited from RequestResponse.then

  + Defined in [src/core/promise/abortable/index.ts:499](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L499)

  Attaches handlers for the promise fulfilled and/or rejected states.
  The method returns a new promise that will be resolved with a value that returns from the passed handlers.

  #### Type parameters

  + #### R

  #### Parameters

  + ##### onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, [RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>
  + ##### onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D> | R>
* Inherited from RequestResponse.then

  + Defined in [src/core/promise/abortable/index.ts:505](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L505)

  #### Type parameters

  + #### V

  #### Parameters

  + ##### onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, V>
  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<V>>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<V>
* Inherited from RequestResponse.then

  + Defined in [src/core/promise/abortable/index.ts:511](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L511)

  #### Type parameters

  + #### V
  + #### R

  #### Parameters

  + ##### onFulfilled: [ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, V>
  + ##### onRejected: [RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<R>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<V | R>
* Inherited from RequestResponse.then

  + Defined in [src/core/promise/abortable/index.ts:517](https://github.com/V4Fire/Core/blob/master/src/core/promise/abortable/index.ts#L517)

  #### Parameters

  + ##### Optional onFulfilled: [Nullable](../modules/index.html#Nullable)<[ResolveHandler](../modules/src_core_promise_abortable_interface.html#ResolveHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>, [RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>
  + ##### Optional onRejected: [Nullable](../modules/index.html#Nullable)<[RejectHandler](../modules/src_core_promise_abortable_interface.html#RejectHandler)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>>
  + ##### Optional onAbort: [Nullable](../modules/index.html#Nullable)<[ConstrRejectHandler](src_core_promise_abortable_interface.ConstrRejectHandler.html)>

  #### Returns [default](../classes/src_core_promise_abortable.default.html)<[RequestResponseObject](src_core_request_interface.RequestResponseObject.html)<D>>