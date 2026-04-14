# Interface FullClearOptions<ID>
### Type parameters

* #### ID = any

### Hierarchy

* [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html)<ID>
  + FullClearOptions

## Index

### Properties

* [group](src_core_async_interface.FullClearOptions.html#group)
* [id](src_core_async_interface.FullClearOptions.html#id)
* [label](src_core_async_interface.FullClearOptions.html#label)
* [name](src_core_async_interface.FullClearOptions.html#name)
* [preventDefault](src_core_async_interface.FullClearOptions.html#preventDefault)
* [promise](src_core_async_interface.FullClearOptions.html#promise)
* [reason](src_core_async_interface.FullClearOptions.html#reason)
* [replacedBy](src_core_async_interface.FullClearOptions.html#replacedBy)

## Properties

### Optional group

group?: string | RegExp

Inherited from [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html).[group](src_core_async_modules_base_interface.ClearProxyOptions.html#group)

* Defined in [src/core/async/modules/base/interface.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L109)

Group name of the task to clear

### Optional id

id?: ID

Inherited from [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html).[id](src_core_async_modules_base_interface.ClearProxyOptions.html#id)

* Defined in [src/core/async/modules/base/interface.ts:121](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L121)

Identifier of the task to clear

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html).[label](src_core_async_modules_base_interface.ClearProxyOptions.html#label)

* Defined in [src/core/async/modules/base/interface.ts:104](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L104)

Label of the task to clear

### name

name: string

Overrides [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html).[name](src_core_async_modules_base_interface.ClearProxyOptions.html#name)

* Defined in [src/core/async/interface.ts:245](https://github.com/V4Fire/Core/blob/master/src/core/async/interface.ts#L245)

Namespace of the task to clear

### Optional preventDefault

preventDefault?: boolean

Inherited from [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html).[preventDefault](src_core_async_modules_base_interface.ClearProxyOptions.html#preventDefault)

* Defined in [src/core/async/modules/base/interface.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L114)

If true, then a cleanup handler of the task is prevented

### Optional promise

promise?: boolean

* Defined in [src/core/async/interface.ts:255](https://github.com/V4Fire/Core/blob/master/src/core/async/interface.ts#L255)

If true, the operation was registered as a promise

### Optional reason

reason?: "id" | "group" | "label" | "rgxp" | "all" | "muting" | "collision"

* Defined in [src/core/async/interface.ts:250](https://github.com/V4Fire/Core/blob/master/src/core/async/interface.ts#L250)

Reason to clear or mark the task

### Optional replacedBy

replacedBy?: [Task](src_core_async_modules_base_interface.Task.html)<[default](../classes/src_core_async.default.html)<[default](../classes/src_core_async.default.html)<any>>>

* Defined in [src/core/async/interface.ts:260](https://github.com/V4Fire/Core/blob/master/src/core/async/interface.ts#L260)

Link to a task that replaces the current