# Interface Task<CTX>
Registered task object

### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* Task

## Index

### Properties

* [clearFn](src_core_async_modules_base_interface.Task.html#clearFn)
* [group](src_core_async_modules_base_interface.Task.html#group)
* [id](src_core_async_modules_base_interface.Task.html#id)
* [label](src_core_async_modules_base_interface.Task.html#label)
* [muted](src_core_async_modules_base_interface.Task.html#muted)
* [obj](src_core_async_modules_base_interface.Task.html#obj)
* [objName](src_core_async_modules_base_interface.Task.html#objName)
* [onClear](src_core_async_modules_base_interface.Task.html#onClear)
* [onComplete](src_core_async_modules_base_interface.Task.html#onComplete)
* [paused](src_core_async_modules_base_interface.Task.html#paused)
* [queue](src_core_async_modules_base_interface.Task.html#queue)
* [unregister](src_core_async_modules_base_interface.Task.html#unregister)

## Properties

### Optional clearFn

clearFn?: [ClearFn](src_core_async_modules_base_interface.ClearFn.html)<[default](../classes/src_core_async.default.html)<[default](../classes/src_core_async.default.html)<any>>>

* Defined in [src/core/async/modules/base/interface.ts:216](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L216)

Function to clear the task

### Optional group

group?: string

* Defined in [src/core/async/modules/base/interface.ts:172](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L172)

Group name the task

### id

id: unknown

* Defined in [src/core/async/modules/base/interface.ts:157](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L157)

Task unique identifier

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

* Defined in [src/core/async/modules/base/interface.ts:177](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L177)

Label of the task

### muted

muted: boolean

* Defined in [src/core/async/modules/base/interface.ts:187](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L187)

True if the task is muted

### obj

obj: unknown

* Defined in [src/core/async/modules/base/interface.ts:162](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L162)

Raw task object

### Optional objName

objName?: string

* Defined in [src/core/async/modules/base/interface.ts:167](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L167)

Name of the raw task object

### onClear

onClear: (Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void))[]

* Defined in [src/core/async/modules/base/interface.ts:206](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L206)

List of clear handlers

### onComplete

onComplete: [BoundFn](src_core_async_modules_base_interface.BoundFn.html)<CTX>[][]

* Defined in [src/core/async/modules/base/interface.ts:201](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L201)

List of complete handlers:

[0] - onFulfilled
[1] - onRejected

### paused

paused: boolean

* Defined in [src/core/async/modules/base/interface.ts:182](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L182)

True if the task is paused

### queue

queue: Function[]

* Defined in [src/core/async/modules/base/interface.ts:193](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L193)

Queue of pending handlers
(if the task is paused)

### unregister

unregister: Function

* Defined in [src/core/async/modules/base/interface.ts:211](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L211)

Unregisters the task