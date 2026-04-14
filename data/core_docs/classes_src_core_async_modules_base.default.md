# Class default<CTX>
### Type parameters

* #### CTX: object = [default](src_core_async_modules_base.default.html)<any>

### Hierarchy

* default
  + [default](src_core_async_modules_proxy.default.html)

## Index

### Constructors

* [constructor](src_core_async_modules_base.default.html#constructor)

### Properties

* [cache](src_core_async_modules_base.default.html#cache)
* [context](src_core_async_modules_base.default.html#context)
* [ctx](src_core_async_modules_base.default.html#ctx)
* [idsMap](src_core_async_modules_base.default.html#idsMap)
* [locked](src_core_async_modules_base.default.html#locked)
* [usedNamespaces](src_core_async_modules_base.default.html#usedNamespaces)
* [workerCache](src_core_async_modules_base.default.html#workerCache)
* [linkNames](src_core_async_modules_base.default.html#linkNames)
* [namespaces](src_core_async_modules_base.default.html#namespaces)

### Accessors

* [linkNames](src_core_async_modules_base.default.html#linkNames-1)
* [namespaces](src_core_async_modules_base.default.html#namespaces-1)

### Methods

* [cancelTask](src_core_async_modules_base.default.html#cancelTask)
* [clearAll](src_core_async_modules_base.default.html#clearAll)
* [clearAsync](src_core_async_modules_base.default.html#clearAsync)
* [getCache](src_core_async_modules_base.default.html#getCache)
* [initCache](src_core_async_modules_base.default.html#initCache)
* [markAllTasks](src_core_async_modules_base.default.html#markAllTasks)
* [markAsync](src_core_async_modules_base.default.html#markAsync)
* [markTask](src_core_async_modules_base.default.html#markTask)
* [muteAll](src_core_async_modules_base.default.html#muteAll)
* [registerTask](src_core_async_modules_base.default.html#registerTask)
* [setAsync](src_core_async_modules_base.default.html#setAsync)
* [suspendAll](src_core_async_modules_base.default.html#suspendAll)
* [unmuteAll](src_core_async_modules_base.default.html#unmuteAll)
* [unsuspendAll](src_core_async_modules_base.default.html#unsuspendAll)

## Constructors

### constructor

* new default<CTX>(ctx?: CTX): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L114)

  #### Type parameters

  + #### CTX: object = [default](src_core_async_modules_base.default.html)<any>

  #### Parameters

  + ##### Optional ctx: CTX

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

## Properties

### Protected Readonly cache

cache: [Dictionary](../interfaces/index.Dictionary.html)<[GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)> = ...

* Defined in [src/core/async/modules/base/index.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L60)

Cache for async operations

### Protected Readonly context

context: CTX

* Defined in [src/core/async/modules/base/index.ts:81](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L81)

deprecated

see
:   [[Async.ctx]]

### Protected Readonly ctx

ctx: CTX

* Defined in [src/core/async/modules/base/index.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L75)

Context of applying for async handlers

### Protected Readonly idsMap

idsMap: WeakMap<object, object> = ...

* Defined in [src/core/async/modules/base/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L70)

Map for task identifiers

### locked

locked: boolean = false

* Defined in [src/core/async/modules/base/index.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L55)

The lock status.
If true, then all new tasks won't be registered.

### Protected Readonly usedNamespaces

usedNamespaces: Set<string> = ...

* Defined in [src/core/async/modules/base/index.ts:86](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L86)

Set of used async namespaces

### Protected Readonly workerCache

workerCache: WeakMap<object, boolean> = ...

* Defined in [src/core/async/modules/base/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L65)

Cache for initialized workers

### Static linkNames

linkNames: { eventListener: "eventListener"; eventListenerPromise: "eventListenerPromise"; idleCallback: "idleCallback"; idleCallbackPromise: "idleCallbackPromise"; immediate: "immediate"; immediatePromise: "immediatePromise"; interval: "interval"; intervalPromise: "intervalPromise"; iterable: "iterable"; promise: "promise"; proxy: "proxy"; proxyPromise: "proxyPromise"; request: "request"; timeout: "timeout"; timeoutPromise: "timeoutPromise"; worker: "worker" } = namespaces

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

* + Defined in [src/core/async/modules/base/index.ts:106](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L106)

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

* + Defined in [src/core/async/modules/base/index.ts:91](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L91)

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

### Protected cancelTask

* cancelTask(task: any, name?: string): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:449](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L449)

  Cancels a task (or a group of tasks) from the specified namespace

  #### Parameters

  + ##### task: any

    operation options or task link
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### clearAll

* clearAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L123)

  Clears all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### Protected clearAsync

* clearAsync(opts: any, name?: string): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:578](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L578)

  deprecated

  see
  :   [[Async.cancelTask]]

  #### Parameters

  + ##### opts: any
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### Protected getCache

* getCache(name: string, promise?: boolean): [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

* + Defined in [src/core/async/modules/base/index.ts:218](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L218)

  Returns a cache object by the specified name

  #### Parameters

  + ##### name: string
  + ##### Optional promise: boolean

  #### Returns [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

### Protected initCache

* initCache(name: string, promise?: boolean): [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

* + Defined in [src/core/async/modules/base/index.ts:236](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L236)

  deprecated

  see
  :   [[Async.getCache]]

  #### Parameters

  + ##### name: string
  + ##### Optional promise: boolean

  #### Returns [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

### Protected markAllTasks

* markAllTasks(label: string, opts: [FullClearOptions](../interfaces/src_core_async_interface.FullClearOptions.html)<any>): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:723](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L723)

  Marks all async tasks from the namespace by the specified label

  #### Parameters

  + ##### label: string
  + ##### opts: [FullClearOptions](../interfaces/src_core_async_interface.FullClearOptions.html)<any>

    operation options

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### Protected markAsync

* markAsync(label: string, opts: any, name?: string): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:713](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L713)

  deprecated

  see
  :   [[Async.markTask]]

  #### Parameters

  + ##### label: string
  + ##### opts: any
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### Protected markTask

* markTask(label: string, task: any, name?: string): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:589](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L589)

  Marks a task (or a group of tasks) from the namespace by the specified label

  #### Parameters

  + ##### label: string
  + ##### task: any

    operation options or a link to the task
  + ##### Optional name: string

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### muteAll

* muteAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:144](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L144)

  Mutes all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### Protected registerTask

* registerTask<R>(task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<any>): null | R

* + Defined in [src/core/async/modules/base/index.ts:244](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L244)

  Registers the specified async task

  #### Type parameters

  + #### R = unknown

  #### Parameters

  + ##### task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<any>

  #### Returns null | R

### Protected setAsync

* setAsync<R>(task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<[default](src_core_async.default.html)<[default](src_core_async.default.html)<any>>>): null | R

* + Defined in [src/core/async/modules/base/index.ts:439](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L439)

  deprecated

  see
  :   [[Async.registerTask]]

  #### Type parameters

  + #### R = unknown

  #### Parameters

  + ##### task: [FullAsyncOptions](../modules/src_core_async_interface.html#FullAsyncOptions)<[default](src_core_async.default.html)<[default](src_core_async.default.html)<any>>>

  #### Returns null | R

### suspendAll

* suspendAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:180](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L180)

  Suspends all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### unmuteAll

* unmuteAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:162](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L162)

  Unmutes all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>

### unsuspendAll

* unsuspendAll(opts?: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)): [default](src_core_async_modules_base.default.html)<CTX>

* + Defined in [src/core/async/modules/base/index.ts:198](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/index.ts#L198)

  Unsuspends all async tasks

  #### Parameters

  + ##### Optional opts: [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

  #### Returns [default](src_core_async_modules_base.default.html)<CTX>