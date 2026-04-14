# Class default<CTX>
### Type parameters

* #### CTX: object = [default](src_core_async_modules_proxy.default.html)<any>

### Hierarchy

* [default](src_core_async_modules_base.default.html)<CTX>
  + default
    - [default](src_core_async_modules_timers.default.html)

## Index

### Constructors

* [constructor](src_core_async_modules_proxy.default.html#constructor)

### Properties

* [cache](src_core_async_modules_proxy.default.html#cache)
* [context](src_core_async_modules_proxy.default.html#context)
* [ctx](src_core_async_modules_proxy.default.html#ctx)
* [idsMap](src_core_async_modules_proxy.default.html#idsMap)
* [locked](src_core_async_modules_proxy.default.html#locked)
* [usedNamespaces](src_core_async_modules_proxy.default.html#usedNamespaces)
* [workerCache](src_core_async_modules_proxy.default.html#workerCache)
* [linkNames](src_core_async_modules_proxy.default.html#linkNames)
* [namespaces](src_core_async_modules_proxy.default.html#namespaces)

### Accessors

* [linkNames](src_core_async_modules_proxy.default.html#linkNames-1)
* [namespaces](src_core_async_modules_proxy.default.html#namespaces-1)

### Methods

* [cancelIterable](src_core_async_modules_proxy.default.html#cancelIterable)
* [cancelPromise](src_core_async_modules_proxy.default.html#cancelPromise)
* [cancelProxy](src_core_async_modules_proxy.default.html#cancelProxy)
* [cancelRequest](src_core_async_modules_proxy.default.html#cancelRequest)
* [cancelTask](src_core_async_modules_proxy.default.html#cancelTask)
* [clearAll](src_core_async_modules_proxy.default.html#clearAll)
* [clearAsync](src_core_async_modules_proxy.default.html#clearAsync)
* [clearIterable](src_core_async_modules_proxy.default.html#clearIterable)
* [clearPromise](src_core_async_modules_proxy.default.html#clearPromise)
* [clearProxy](src_core_async_modules_proxy.default.html#clearProxy)
* [clearRequest](src_core_async_modules_proxy.default.html#clearRequest)
* [clearWorker](src_core_async_modules_proxy.default.html#clearWorker)
* [debounce](src_core_async_modules_proxy.default.html#debounce)
* [getBaseIterator](src_core_async_modules_proxy.default.html#getBaseIterator)
* [getCache](src_core_async_modules_proxy.default.html#getCache)
* [initCache](src_core_async_modules_proxy.default.html#initCache)
* [iterable](src_core_async_modules_proxy.default.html#iterable-2)
* [markAllTasks](src_core_async_modules_proxy.default.html#markAllTasks)
* [markAsync](src_core_async_modules_proxy.default.html#markAsync)
* [markPromise](src_core_async_modules_proxy.default.html#markPromise)
* [markTask](src_core_async_modules_proxy.default.html#markTask)
* [muteAll](src_core_async_modules_proxy.default.html#muteAll)
* [muteIterable](src_core_async_modules_proxy.default.html#muteIterable)
* [mutePromise](src_core_async_modules_proxy.default.html#mutePromise)
* [muteProxy](src_core_async_modules_proxy.default.html#muteProxy)
* [muteRequest](src_core_async_modules_proxy.default.html#muteRequest)
* [onPromiseClear](src_core_async_modules_proxy.default.html#onPromiseClear)
* [onPromiseMerge](src_core_async_modules_proxy.default.html#onPromiseMerge)
* [promise](src_core_async_modules_proxy.default.html#promise-2)
* [promiseDestructor](src_core_async_modules_proxy.default.html#promiseDestructor)
* [proxy](src_core_async_modules_proxy.default.html#proxy-2)
* [registerTask](src_core_async_modules_proxy.default.html#registerTask)
* [request](src_core_async_modules_proxy.default.html#request-2)
* [setAsync](src_core_async_modules_proxy.default.html#setAsync)
* [suspendAll](src_core_async_modules_proxy.default.html#suspendAll)
* [suspendIterable](src_core_async_modules_proxy.default.html#suspendIterable)
* [suspendPromise](src_core_async_modules_proxy.default.html#suspendPromise)
* [suspendProxy](src_core_async_modules_proxy.default.html#suspendProxy)
* [suspendRequest](src_core_async_modules_proxy.default.html#suspendRequest)
* [terminateWorker](src_core_async_modules_proxy.default.html#terminateWorker)
* [throttle](src_core_async_modules_proxy.default.html#throttle)
* [unmuteAll](src_core_async_modules_proxy.default.html#unmuteAll)
* [unmuteIterable](src_core_async_modules_proxy.default.html#unmuteIterable)
* [unmutePromise](src_core_async_modules_proxy.default.html#unmutePromise)
* [unmuteProxy](src_core_async_modules_proxy.default.html#unmuteProxy)
* [unmuteRequest](src_core_async_modules_proxy.default.html#unmuteRequest)
* [unsuspendAll](src_core_async_modules_proxy.default.html#unsuspendAll)
* [unsuspendIterable](src_core_async_modules_proxy.default.html#unsuspendIterable)
* [unsuspendPromise](src_core_async_modules_proxy.default.html#unsuspendPromise)
* [unsuspendProxy](src_core_async_modules_proxy.default.html#unsuspendProxy)
* [unsuspendRequest](src_core_async_modules_proxy.default.html#unsuspendRequest)
* [worker](src_core_async_modules_proxy.default.html#worker-2)
* [workerDestructor](src_core_async_modules_proxy.default.html#workerDestructor)

## Constructors

### constructor

* new default<CTX>(ctx?: CTX): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[constructor](src_core_async_modules_base.default.html#constructor)

  + Defined in [src/core/async/modules/base/index.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L114)

  #### Type parameters

  + #### CTX: object = [default](src_core_async_modules_proxy.default.html)<any>

  #### Parameters

  + ##### Optional ctx: CTX

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

## Properties

### Protected Readonly cache

cache: [Dictionary](../interfaces/index.Dictionary.html)<[GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)> = ...

Inherited from [default](src_core_async_modules_base.default.html).[cache](src_core_async_modules_base.default.html#cache)

* Defined in [src/core/async/modules/base/index.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L60)

Cache for async operations

### Protected Readonly context

context: CTX

Inherited from [default](src_core_async_modules_base.default.html).[context](src_core_async_modules_base.default.html#context)

* Defined in [src/core/async/modules/base/index.ts:81](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L81)

deprecated

see
:   [[Async.ctx]]

### Protected Readonly ctx

ctx: CTX

Inherited from [default](src_core_async_modules_base.default.html).[ctx](src_core_async_modules_base.default.html#ctx)

* Defined in [src/core/async/modules/base/index.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L75)

Context of applying for async handlers

### Protected Readonly idsMap

idsMap: WeakMap<object, object> = ...

Inherited from [default](src_core_async_modules_base.default.html).[idsMap](src_core_async_modules_base.default.html#idsMap)

* Defined in [src/core/async/modules/base/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L70)

Map for task identifiers

### locked

locked: boolean = false

Inherited from [default](src_core_async_modules_base.default.html).[locked](src_core_async_modules_base.default.html#locked)

* Defined in [src/core/async/modules/base/index.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L55)

The lock status.
If true, then all new tasks won't be registered.

### Protected Readonly usedNamespaces

usedNamespaces: Set<string> = ...

Inherited from [default](src_core_async_modules_base.default.html).[usedNamespaces](src_core_async_modules_base.default.html#usedNamespaces)

* Defined in [src/core/async/modules/base/index.ts:86](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L86)

Set of used async namespaces

### Protected Readonly workerCache

workerCache: WeakMap<object, boolean> = ...

Inherited from [default](src_core_async_modules_base.default.html).[workerCache](src_core_async_modules_base.default.html#workerCache)

* Defined in [src/core/async/modules/base/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L65)

Cache for initialized workers

### Static linkNames

linkNames: { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" } = namespaces

Inherited from [default](src_core_async_modules_base.default.html).[linkNames](src_core_async_modules_base.default.html#linkNames)

* Defined in [src/core/async/modules/base/index.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L49)

deprecated

see
:   Async.namespaces

#### Type declaration

* ##### eventListener: "eventListener"
* ##### eventListenerPromise: "eventListenerPromise"
* ##### idleCallback: "idleCallback"
* ##### idleCallbackPromise: "idleCallbackPromise"
* ##### immediate: "immediate"
* ##### immediatePromise: "immediatePromise"
* ##### interval: "interval"
* ##### intervalPromise: "intervalPromise"
* ##### iterable: "iterable"
* ##### promise: "promise"
* ##### proxy: "proxy"
* ##### proxyPromise: "proxyPromise"
* ##### request: "request"
* ##### timeout: "timeout"
* ##### timeoutPromise: "timeoutPromise"
* ##### worker: "worker"

### Static namespaces

namespaces: { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" } = namespaces

Inherited from [default](src_core_async_modules_base.default.html).[namespaces](src_core_async_modules_base.default.html#namespaces)

* Defined in [src/core/async/modules/base/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L43)

Map of namespaces for async operations

#### Type declaration

* ##### eventListener: "eventListener"
* ##### eventListenerPromise: "eventListenerPromise"
* ##### idleCallback: "idleCallback"
* ##### idleCallbackPromise: "idleCallbackPromise"
* ##### immediate: "immediate"
* ##### immediatePromise: "immediatePromise"
* ##### interval: "interval"
* ##### intervalPromise: "intervalPromise"
* ##### iterable: "iterable"
* ##### promise: "promise"
* ##### proxy: "proxy"
* ##### proxyPromise: "proxyPromise"
* ##### request: "request"
* ##### timeout: "timeout"
* ##### timeoutPromise: "timeoutPromise"
* ##### worker: "worker"

## Accessors

### Protected linkNames

* get linkNames(): { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" }

* Inherited from Super.linkNames

  + Defined in [src/core/async/modules/base/index.ts:106](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L106)

  deprecated

  see
  :   [[Async.namespaces]]

  #### Returns { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" }

  + ##### eventListener: "eventListener"
  + ##### eventListenerPromise: "eventListenerPromise"
  + ##### idleCallback: "idleCallback"
  + ##### idleCallbackPromise: "idleCallbackPromise"
  + ##### immediate: "immediate"
  + ##### immediatePromise: "immediatePromise"
  + ##### interval: "interval"
  + ##### intervalPromise: "intervalPromise"
  + ##### iterable: "iterable"
  + ##### promise: "promise"
  + ##### proxy: "proxy"
  + ##### proxyPromise: "proxyPromise"
  + ##### request: "request"
  + ##### timeout: "timeout"
  + ##### timeoutPromise: "timeoutPromise"
  + ##### worker: "worker"

### Protected namespaces

* get namespaces(): { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" }

* Inherited from Super.namespaces

  + Defined in [src/core/async/modules/base/index.ts:91](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L91)

  Link to `Async.namespaces`

  #### Returns { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" }

  + ##### eventListener: "eventListener"
  + ##### eventListenerPromise: "eventListenerPromise"
  + ##### idleCallback: "idleCallback"
  + ##### idleCallbackPromise: "idleCallbackPromise"
  + ##### immediate: "immediate"
  + ##### immediatePromise: "immediatePromise"
  + ##### interval: "interval"
  + ##### intervalPromise: "intervalPromise"
  + ##### iterable: "iterable"
  + ##### promise: "promise"
  + ##### proxy: "proxy"
  + ##### proxyPromise: "proxyPromise"
  + ##### request: "request"
  + ##### timeout: "timeout"
  + ##### timeoutPromise: "timeoutPromise"
  + ##### worker: "worker"

## Methods

### cancelIterable

* cancelIterable(id?: AsyncIterable<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* cancelIterable(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:556](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L556)

  Cancels the specified iterable object.
  Notice that cancellation affects only objects that have already been activated by invoking the `next` method.
  So, for example, canceled iterable will throw an error on the next invoking of `next`.

  alias

  #### Parameters

  + ##### Optional id: AsyncIterable<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:566](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L566)

  Cancels the specified iterable or a group of iterable.
  Notice that cancellation affects only objects that have already been activated by invoking the `next` method.
  So, for example, canceled iterable will throw an error on the next invoking of `next`.

  alias

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### cancelPromise

* cancelPromise(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* cancelPromise(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:807](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L807)

  Cancels the specified promise.
  The canceled promise will be automatically rejected.

  alias

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:816](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L816)

  Cancels the specified promise or a group of promises.
  The canceled promises will be automatically rejected.

  alias

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### cancelProxy

* cancelProxy(id?: Function): [default](src_core_async_modules_proxy.default.html)<CTX>
* cancelProxy(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:219](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L219)

  Cancels the specified proxy function

  alias

  #### Parameters

  + ##### Optional id: Function

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:227](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L227)

  Cancels the specified proxy function or a group of functions

  alias

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### cancelRequest

* cancelRequest(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* cancelRequest(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:353](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L353)

  Cancels the specified request.
  The canceled promise will be automatically rejected.

  alias

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:362](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L362)

  Cancels the specified request or a group of requests.
  The canceled promises will be automatically rejected.

  alias

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### Protected cancelTask

* cancelTask(task: any, name?: string): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[cancelTask](src_core_async_modules_base.default.html#cancelTask)

  + Defined in [src/core/async/modules/base/index.ts:449](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L449)

  Cancels a task (or a group of tasks) from the specified namespace

  #### Parameters

  + ##### task: any

    operation options or task link
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### clearAll

* clearAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[clearAll](src_core_async_modules_base.default.html#clearAll)

  + Defined in [src/core/async/modules/base/index.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L123)

  Clears all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### Protected clearAsync

* clearAsync(opts: any, name?: string): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[clearAsync](src_core_async_modules_base.default.html#clearAsync)

  + Defined in [src/core/async/modules/base/index.ts:578](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L578)

  deprecated

  see
  :   [[Async.cancelTask]]

  #### Parameters

  + ##### opts: any
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### clearIterable

* clearIterable(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* clearIterable(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:578](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L578)

  Cancels the specified iterable object.
  Notice that cancellation affects only objects that have already been activated by invoking the `next` method.
  So, for example, canceled iterable will throw an error on the next invoking of `next`.

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:587](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L587)

  Cancels the specified iterable object.
  Notice that cancellation affects only objects that have already been activated by invoking the `next` method.
  So, for example, canceled iterable will throw an error on the next invoking of `next`.

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### clearPromise

* clearPromise(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* clearPromise(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:827](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L827)

  Cancels the specified promise.
  The canceled promise will be automatically rejected.

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:835](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L835)

  Cancels the specified promise or a group of promises.
  The canceled promises will be automatically rejected.

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### clearProxy

* clearProxy(id?: Function): [default](src_core_async_modules_proxy.default.html)<CTX>
* clearProxy(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:236](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L236)

  Cancels the specified proxy function

  #### Parameters

  + ##### Optional id: Function

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:242](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L242)

  Cancels the specified proxy function or a group of functions

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### clearRequest

* clearRequest(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* clearRequest(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:373](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L373)

  Cancels the specified request.
  The canceled promise will be automatically rejected.

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:381](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L381)

  Cancels the specified request or a group of requests.
  The canceled promises will be automatically rejected.

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### clearWorker

* clearWorker(id?: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)): [default](src_core_async_modules_proxy.default.html)<CTX>
* clearWorker(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<[WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:140](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L140)

  Terminates the specified worker

  #### Parameters

  + ##### Optional id: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:146](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L146)

  Terminates the specified worker or a group of workers

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<[WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### debounce

* debounce<F, C>(fn: F, delay: number, opts?: [AsyncCbOptions](../interfaces/src_core_async_modules_base_interface.AsyncCbOptions.html)<C>): [AnyFunction](../interfaces/index.AnyFunction.html)<Parameters<F>, void>

* + Defined in [src/core/async/modules/proxy/index.ts:190](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L190)

  Returns a new function that allows invoking the passed function only with the specified delay.
  The next invocation of the function will cancel the previous.

  #### Type parameters

  + #### F: [BoundFn](../interfaces/src_core_async_modules_base_interface.BoundFn.html)<C, F>
  + #### C: object = CTX

  #### Parameters

  + ##### fn: F
  + ##### delay: number
  + ##### Optional opts: [AsyncCbOptions](../interfaces/src_core_async_modules_base_interface.AsyncCbOptions.html)<C>

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)<Parameters<F>, void>

### Protected getBaseIterator

* getBaseIterator<T>(iterable: Iterable<T> | AsyncIterable<T>): [CanUndef](../modules/index.html#CanUndef)<IterableIterator<T> | AsyncIterableIterator<T>>

* + Defined in [src/core/async/modules/proxy/index.ts:1085](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L1085)

  Returns an iterator from the passed iterable object.
  Notice, an asynchronous iterator has more priority.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### iterable: Iterable<T> | AsyncIterable<T>

  #### Returns [CanUndef](../modules/index.html#CanUndef)<IterableIterator<T> | AsyncIterableIterator<T>>

### Protected getCache

* getCache(name: string, promise?: boolean): [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

* Inherited from [default](src_core_async_modules_base.default.html).[getCache](src_core_async_modules_base.default.html#getCache)

  + Defined in [src/core/async/modules/base/index.ts:218](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L218)

  Returns a cache object by the specified name

  #### Parameters

  + ##### name: string
  + ##### Optional promise: boolean

  #### Returns [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

### Protected initCache

* initCache(name: string, promise?: boolean): [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

* Inherited from [default](src_core_async_modules_base.default.html).[initCache](src_core_async_modules_base.default.html#initCache)

  + Defined in [src/core/async/modules/base/index.ts:236](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L236)

  deprecated

  see
  :   [[Async.getCache]]

  #### Parameters

  + ##### name: string
  + ##### Optional promise: boolean

  #### Returns [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

### iterable

* iterable<T>(iterable: Iterable<T> | AsyncIterable<T>, opts?: [AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html)): AsyncIterable<T> | (AsyncIterable<T> & Iterable<T>)

* + Defined in [src/core/async/modules/proxy/index.ts:470](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L470)

  Creates a new asynchronous iterable object from the specified iterable and returns it.
  If the passed iterable doesn't have `Symbol.asyncIterator`, it will be created from a synchronous object iterator
  (the synchronous iterator will also be preserved).

  Notice, until the created promise object isn't executed by invoking the `next` method,
  any async operations won't be registered.

  example
  :   ```
      const async = new Async();  
        
      for await (const el of async.iterable([1, 2, 3, 4])) {  
        console.log(el);  
      }
      ```

  #### Type parameters

  + #### T

  #### Parameters

  + ##### iterable: Iterable<T> | AsyncIterable<T>
  + ##### Optional opts: [AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html)

  #### Returns AsyncIterable<T> | (AsyncIterable<T> & Iterable<T>)

### Protected markAllTasks

* markAllTasks(label: string, opts: [FullClearOptions](../interfaces/src_core_async_interface.FullClearOptions.html)<any>): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[markAllTasks](src_core_async_modules_base.default.html#markAllTasks)

  + Defined in [src/core/async/modules/base/index.ts:723](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L723)

  Marks all async tasks from the namespace by the specified label

  #### Parameters

  + ##### label: string
  + ##### opts: [FullClearOptions](../interfaces/src_core_async_interface.FullClearOptions.html)<any>

    operation options

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### Protected markAsync

* markAsync(label: string, opts: any, name?: string): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[markAsync](src_core_async_modules_base.default.html#markAsync)

  + Defined in [src/core/async/modules/base/index.ts:713](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L713)

  deprecated

  see
  :   [[Async.markTask]]

  #### Parameters

  + ##### label: string
  + ##### opts: any
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### Protected markPromise

* markPromise(label: string, id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* markPromise(label: string, opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:1047](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L1047)

  Marks a promise with the specified label

  #### Parameters

  + ##### label: string
  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:1055](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L1055)

  Marks a promise or group of promises with the specified label

  #### Parameters

  + ##### label: string
  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    additional options

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### Protected markTask

* markTask(label: string, task: any, name?: string): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[markTask](src_core_async_modules_base.default.html#markTask)

  + Defined in [src/core/async/modules/base/index.ts:589](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L589)

  Marks a task (or a group of tasks) from the namespace by the specified label

  #### Parameters

  + ##### label: string
  + ##### task: any

    operation options or a link to the task
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### muteAll

* muteAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[muteAll](src_core_async_modules_base.default.html#muteAll)

  + Defined in [src/core/async/modules/base/index.ts:144](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L144)

  Mutes all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### muteIterable

* muteIterable(id?: AsyncIterable<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* muteIterable(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:599](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L599)

  Mutes the specified iterable object.
  Elements that are consumed during the object is muted will be ignored.
  Notice that muting affects only objects that have already been activated by invoking the `next` method.

  #### Parameters

  + ##### Optional id: AsyncIterable<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:608](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L608)

  Mutes the specified iterable object or a group of iterable objects.
  Elements, that are consumed during the object is muted will be ignored.
  Notice that muting affects only objects that have already been activated by invoking the `next` method.

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### mutePromise

* mutePromise(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* mutePromise(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:865](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L865)

  Mutes the specified promise.
  If the promise is resolved during it muted, the promise wrapper will be rejected.

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:873](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L873)

  Mutes the specified promise or a group of promises.
  If the promises are resolved during muted, the promise wrappers will be rejected.

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### muteProxy

* muteProxy(id?: Function): [default](src_core_async_modules_proxy.default.html)<CTX>
* muteProxy(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:251](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L251)

  Mutes the specified proxy function

  #### Parameters

  + ##### Optional id: Function

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:257](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L257)

  Mutes the specified proxy function or a group of functions

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### muteRequest

* muteRequest(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* muteRequest(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:392](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L392)

  Mutes the specified request.
  If the request is resolved during it muted, the promise wrapper will be rejected.

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:400](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L400)

  Mutes the specified request or a group of requests.
  If the requests are resolved during muted, the promise wrappers will be rejected.

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### onPromiseClear

* onPromiseClear(resolve: Function, reject: Function): Function

* + Defined in [src/core/async/modules/proxy/index.ts:1007](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L1007)

  Factory to create promise clear handlers

  #### Parameters

  + ##### resolve: Function
  + ##### reject: Function

  #### Returns Function

### onPromiseMerge

* onPromiseMerge(resolve: Function, reject: Function): Function

* + Defined in [src/core/async/modules/proxy/index.ts:1037](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L1037)

  Factory to create promise merge handlers

  #### Parameters

  + ##### resolve: Function
  + ##### reject: Function

  #### Returns Function

### promise

* promise<T>(promise: [PromiseLikeP](../modules/src_core_async_modules_proxy_interface.html#PromiseLikeP)<T>, opts?: [AsyncPromiseOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncPromiseOptions.html)): Promise<T>

* + Defined in [src/core/async/modules/proxy/index.ts:684](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L684)

  Creates a new promise that wraps the passed promise and returns it.

  This method doesn't attach any hook or listeners to the object,
  but if we cancel the operation by using one of Async's methods, like, "cancelPromise",
  the promise will be rejected.

  The promise can be provided as it is or as a function, that returns a promise.

  example
  :   ```
      const  
        async = new Async();  
        
      async.promise(new Promise(() => {  
        // ...  
      }))
      ```

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### promise: [PromiseLikeP](../modules/src_core_async_modules_proxy_interface.html#PromiseLikeP)<T>
  + ##### Optional opts: [AsyncPromiseOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncPromiseOptions.html)

  #### Returns Promise<T>

### promiseDestructor

* promiseDestructor(destructor: [CanUndef](../modules/index.html#CanUndef)<string>, promise: PromiseLike<unknown> | [CancelablePromise](../interfaces/src_core_async_modules_proxy_interface.CancelablePromise.html)<unknown>): void

* + Defined in [src/core/async/modules/proxy/index.ts:974](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L974)

  Terminates the specified promise

  #### Parameters

  + ##### destructor: [CanUndef](../modules/index.html#CanUndef)<string>

    name of the destructor method
  + ##### promise: PromiseLike<unknown> | [CancelablePromise](../interfaces/src_core_async_modules_proxy_interface.CancelablePromise.html)<unknown>

  #### Returns void

### proxy

* proxy<F, C>(fn: F, opts?: [AsyncProxyOptions](../interfaces/src_core_async_modules_base_interface.AsyncProxyOptions.html)<C>): F

* + Defined in [src/core/async/modules/proxy/index.ts:171](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L171)

  Creates a new function that wraps the original and returns it.

  This method doesn't attach any hook or listeners to the object,
  but if we cancel the operation by using one of Async's methods, like, `cancelProxy`,
  the target function won't be invoked.

  example
  :   ```
      const  
        async = new Async();  
        
      myImage.onload = async.proxy(() => {  
        // ...  
      });
      ```

  #### Type parameters

  + #### F: [BoundFn](../interfaces/src_core_async_modules_base_interface.BoundFn.html)<C, F>
  + #### C: object = CTX

  #### Parameters

  + ##### fn: F
  + ##### Optional opts: [AsyncProxyOptions](../interfaces/src_core_async_modules_base_interface.AsyncProxyOptions.html)<C>

  #### Returns F

### Protected registerTask

* registerTask<R>(task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<any>): null | R

* Inherited from [default](src_core_async_modules_base.default.html).[registerTask](src_core_async_modules_base.default.html#registerTask)

  + Defined in [src/core/async/modules/base/index.ts:244](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L244)

  Registers the specified async task

  #### Type parameters

  + #### R = unknown

  #### Parameters

  + ##### task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<any>

  #### Returns null | R

### request

* request<T>(request: (() => PromiseLike<T>) | PromiseLike<T>, opts?: [AsyncRequestOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncRequestOptions.html)): Promise<T>

* + Defined in [src/core/async/modules/proxy/index.ts:342](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L342)

  Creates a promise that wraps the passed request and returns it.

  This method doesn't attach any hook or listeners to the object,
  but if we cancel the operation by using one of Async's methods, like, "cancelRequest",
  the promise will be rejected.

  The request can be provided as a promise or function, that returns a promise.
  Notice, the method uses `Async.promise`, but with a different namespace: `request` instead of `promise`.

  example
  :   ```
      const async = new Async();  
      async.request(fetch('foo/bla'));
      ```

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### request: (() => PromiseLike<T>) | PromiseLike<T>
  + ##### Optional opts: [AsyncRequestOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncRequestOptions.html)

  #### Returns Promise<T>

### Protected setAsync

* setAsync<R>(task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<[default](src_core_async.default.html)<[default](src_core_async.default.html)<any>>>): null | R

* Inherited from [default](src_core_async_modules_base.default.html).[setAsync](src_core_async_modules_base.default.html#setAsync)

  + Defined in [src/core/async/modules/base/index.ts:439](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L439)

  deprecated

  see
  :   [[Async.registerTask]]

  #### Type parameters

  + #### R = unknown

  #### Parameters

  + ##### task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<[default](src_core_async.default.html)<[default](src_core_async.default.html)<any>>>

  #### Returns null | R

### suspendAll

* suspendAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[suspendAll](src_core_async_modules_base.default.html#suspendAll)

  + Defined in [src/core/async/modules/base/index.ts:180](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L180)

  Suspends all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### suspendIterable

* suspendIterable(id?: AsyncIterable<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* suspendIterable(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:634](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L634)

  Suspends the specified iterable object.
  Notice that suspending affects only objects that have already been activated by invoking the `next` method.

  #### Parameters

  + ##### Optional id: AsyncIterable<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:642](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L642)

  Suspends the specified iterable or a group of iterable objects.
  Notice that suspending affects only objects that have already been activated by invoking the `next` method.

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### suspendPromise

* suspendPromise(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* suspendPromise(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:897](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L897)

  Suspends the specified promise

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:903](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L903)

  Suspends the specified promise or a group of promises

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### suspendProxy

* suspendProxy(id?: Function): [default](src_core_async_modules_proxy.default.html)<CTX>
* suspendProxy(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:289](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L289)

  Suspends the specified proxy function

  #### Parameters

  + ##### Optional id: Function

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:295](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L295)

  Suspends the specified proxy function or a group of functions

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### suspendRequest

* suspendRequest(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* suspendRequest(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:424](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L424)

  Suspends the specified request

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:430](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L430)

  Suspends the specified request or a group of requests

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### terminateWorker

* terminateWorker(id?: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)): [default](src_core_async_modules_proxy.default.html)<CTX>
* terminateWorker(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<[WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L123)

  Terminates the specified worker

  alias

  #### Parameters

  + ##### Optional id: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:131](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L131)

  Terminates the specified worker or a group of workers

  alias

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<[WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### throttle

* throttle<F, C>(fn: F, delay: number, opts?: [AsyncCbOptions](../interfaces/src_core_async_modules_base_interface.AsyncCbOptions.html)<C>): [AnyFunction](../interfaces/index.AnyFunction.html)<Parameters<F>, void>

* + Defined in [src/core/async/modules/proxy/index.ts:205](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L205)

  Returns a new function that allows invoking the passed function not more often than the specified delay

  #### Type parameters

  + #### F: [BoundFn](../interfaces/src_core_async_modules_base_interface.BoundFn.html)<C, F>
  + #### C: object = CTX

  #### Parameters

  + ##### fn: F
  + ##### delay: number
  + ##### Optional opts: [AsyncCbOptions](../interfaces/src_core_async_modules_base_interface.AsyncCbOptions.html)<C>

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)<Parameters<F>, void>

### unmuteAll

* unmuteAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[unmuteAll](src_core_async_modules_base.default.html#unmuteAll)

  + Defined in [src/core/async/modules/base/index.ts:162](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L162)

  Unmutes all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unmuteIterable

* unmuteIterable(id?: AsyncIterable<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* unmuteIterable(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:617](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L617)

  Unmutes the specified iterable object

  #### Parameters

  + ##### Optional id: AsyncIterable<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:623](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L623)

  Unmutes the specified iterable function or a group of iterable objects

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unmutePromise

* unmutePromise(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* unmutePromise(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:882](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L882)

  Unmutes the specified promise

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:888](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L888)

  Unmutes the specified promise or a group of promises

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unmuteProxy

* unmuteProxy(id?: Function): [default](src_core_async_modules_proxy.default.html)<CTX>
* unmuteProxy(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:270](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L270)

  Unmutes the specified proxy function

  #### Parameters

  + ##### Optional id: Function

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:276](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L276)

  Unmutes the specified proxy function or a group of functions

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unmuteRequest

* unmuteRequest(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* unmuteRequest(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:409](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L409)

  Unmutes the specified request

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:415](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L415)

  Unmutes the specified request or a group of requests

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unsuspendAll

* unsuspendAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_proxy.default.html)<CTX>

* Inherited from [default](src_core_async_modules_base.default.html).[unsuspendAll](src_core_async_modules_base.default.html#unsuspendAll)

  + Defined in [src/core/async/modules/base/index.ts:198](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L198)

  Unsuspends all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unsuspendIterable

* unsuspendIterable(id?: AsyncIterable<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* unsuspendIterable(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:651](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L651)

  Unsuspends the specified iterable object

  #### Parameters

  + ##### Optional id: AsyncIterable<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:657](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L657)

  Unsuspends the specified iterable or a group of iterable objects

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<AsyncIterable<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unsuspendPromise

* unsuspendPromise(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* unsuspendPromise(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:912](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L912)

  Unsuspends the specified promise

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:918](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L918)

  Unsuspends the specified promise or a group of promises

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unsuspendProxy

* unsuspendProxy(id?: Function): [default](src_core_async_modules_proxy.default.html)<CTX>
* unsuspendProxy(opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:308](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L308)

  Unsuspends the specified proxy function

  #### Parameters

  + ##### Optional id: Function

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:314](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L314)

  Unsuspends the specified proxy function or a group of functions

  #### Parameters

  + ##### opts: [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)<Function>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### unsuspendRequest

* unsuspendRequest(id?: Promise<unknown>): [default](src_core_async_modules_proxy.default.html)<CTX>
* unsuspendRequest(opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>): [default](src_core_async_modules_proxy.default.html)<CTX>

* + Defined in [src/core/async/modules/proxy/index.ts:439](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L439)

  Unsuspends the specified request

  #### Parameters

  + ##### Optional id: Promise<unknown>

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>
* + Defined in [src/core/async/modules/proxy/index.ts:445](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L445)

  Unsuspends the specified request or a group of requests

  #### Parameters

  + ##### opts: [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<Promise<unknown>>

    options for the operation

  #### Returns [default](src_core_async_modules_proxy.default.html)<CTX>

### worker

* worker<T>(worker: T, opts?: [AsyncWorkerOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncWorkerOptions.html)<CTX>): T

* + Defined in [src/core/async/modules/proxy/index.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L83)

  Wraps the specified worker object.

  This method doesn't attach any hook or listeners to the object,
  but every time the same object is registered, Async will increment the number of links that relate to this object.
  After, when we try to destroy the worker by using one of Async's methods, like, `terminateWorker`,
  it will de-increment values of links. When the number of links is equal to zero,
  Async will try to call a "real" object destructor by using one of the possible destructor methods from
  the whitelist or by the specified destructor name, also if the worker is a function,
  it is interpreted as the destructor.

  example
  :   ```
      const  
        async = new Async(),  
        el = document.createElement('div');  
        
      $el.appendChild(el);  
        
      // This function will work as the worker destructor  
      async.worker(() => el.remove());  
        
      const  
        myWorker = new Worker('my-worker.js');  
        
      async.worker(myWorker);  
        
      async.clearAll();
      ```

  #### Type parameters

  + #### T: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)

  #### Parameters

  + ##### worker: T
  + ##### Optional opts: [AsyncWorkerOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncWorkerOptions.html)<CTX>

  #### Returns T

### workerDestructor

* workerDestructor(destructor: [CanUndef](../modules/index.html#CanUndef)<string>, worker: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)): void

* + Defined in [src/core/async/modules/proxy/index.ts:929](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/index.ts#L929)

  Terminates the specified worker

  #### Parameters

  + ##### destructor: [CanUndef](../modules/index.html#CanUndef)<string>

    name of the destructor method
  + ##### worker: [WorkerLikeP](../modules/src_core_async_modules_proxy_interface.html#WorkerLikeP)

  #### Returns void