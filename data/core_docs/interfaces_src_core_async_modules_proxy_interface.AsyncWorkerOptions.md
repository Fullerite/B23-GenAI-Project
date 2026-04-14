# Interface AsyncWorkerOptions<CTX>
### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html)<CTX>
  + AsyncWorkerOptions

## Index

### Properties

* [clearFn](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#clearFn)
* [destructor](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#destructor)
* [group](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#group)
* [join](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#join)
* [label](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#label)
* [name](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#name)
* [onClear](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#onClear)
* [onMerge](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#onMerge)
* [onMutedCall](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#onMutedCall)
* [promise](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#promise)
* [single](src_core_async_modules_proxy_interface.AsyncWorkerOptions.html#single)

## Properties

### Optional clearFn

clearFn?: [ClearFn](src_core_async_modules_base_interface.ClearFn.html)<CTX>

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[clearFn](src_core_async_modules_base_interface.AsyncProxyOptions.html#clearFn)

* Defined in [src/core/async/modules/base/interface.ts:97](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L97)

Function to clear memory of the proxy

### Optional destructor

destructor?: string

* Defined in [src/core/async/modules/proxy/interface.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/interface.ts#L55)

Name of a destructor method

### Optional group

group?: string

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[group](src_core_async_modules_base_interface.AsyncProxyOptions.html#group)

* Defined in [src/core/async/modules/base/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L46)

Group name of a task

### Optional join

join?: [Join](../modules/src_core_async_modules_base_interface.html#Join)

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[join](src_core_async_modules_base_interface.AsyncProxyOptions.html#join)

* Defined in [src/core/async/modules/base/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L53)

Strategy to join competitive tasks (with the same labels):

1. `true` - all tasks are joined to the first;
2. `'replace'` - all tasks are joined (replaced) to the last (only for promises).

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[label](src_core_async_modules_base_interface.AsyncProxyOptions.html#label)

* Defined in [src/core/async/modules/base/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L41)

Label of a task (the previous task with the same label will be canceled)

### Optional name

name?: string

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[name](src_core_async_modules_base_interface.AsyncProxyOptions.html#name)

* Defined in [src/core/async/modules/base/interface.ts:92](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L92)

Namespace of the proxy

### Optional onClear

onClear?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[onClear](src_core_async_modules_base_interface.AsyncProxyOptions.html#onClear)

* Defined in [src/core/async/modules/base/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L66)

Handler/s of task clearing

### Optional onMerge

onMerge?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[onMerge](src_core_async_modules_base_interface.AsyncProxyOptions.html#onMerge)

* Defined in [src/core/async/modules/base/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L71)

Handler/s of task merging: a task should merge to another task with the same label and with "join: true" strategy

### Optional onMutedCall

onMutedCall?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[onMutedCall](src_core_async_modules_base_interface.AsyncProxyOptions.html#onMutedCall)

* Defined in [src/core/async/modules/base/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L77)

Handler/s of muted task calling.
These handlers are invoked when occurring calling the task if it is muted.

### Optional promise

promise?: boolean

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[promise](src_core_async_modules_base_interface.AsyncProxyOptions.html#promise)

* Defined in [src/core/async/modules/base/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L61)

If true, then a task namespace is marked as promisified

default
:   `false`

### Optional single

single?: boolean

Inherited from [AsyncProxyOptions](src_core_async_modules_base_interface.AsyncProxyOptions.html).[single](src_core_async_modules_base_interface.AsyncProxyOptions.html#single)

* Defined in [src/core/async/modules/base/interface.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L85)

If false, then the proxy supports multiple callings

default
:   `true`