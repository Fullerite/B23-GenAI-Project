# Interface ClearProxyOptions<ID>
### Type parameters

* #### ID = any

### Hierarchy

* [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html)<ID>
  + ClearProxyOptions
    - [FullClearOptions](src_core_async_interface.FullClearOptions.html)

## Index

### Properties

* [group](src_core_async_modules_base_interface.ClearProxyOptions.html#group)
* [id](src_core_async_modules_base_interface.ClearProxyOptions.html#id)
* [label](src_core_async_modules_base_interface.ClearProxyOptions.html#label)
* [name](src_core_async_modules_base_interface.ClearProxyOptions.html#name)
* [preventDefault](src_core_async_modules_base_interface.ClearProxyOptions.html#preventDefault)

## Properties

### Optional group

group?: string | RegExp

Inherited from [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html).[group](src_core_async_modules_base_interface.ClearOptionsId.html#group)

* Defined in [src/core/async/modules/base/interface.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L109)

Group name of the task to clear

### Optional id

id?: ID

Inherited from [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html).[id](src_core_async_modules_base_interface.ClearOptionsId.html#id)

* Defined in [src/core/async/modules/base/interface.ts:121](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L121)

Identifier of the task to clear

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html).[label](src_core_async_modules_base_interface.ClearOptionsId.html#label)

* Defined in [src/core/async/modules/base/interface.ts:104](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L104)

Label of the task to clear

### Optional name

name?: string

* Defined in [src/core/async/modules/base/interface.ts:128](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L128)

Namespace of the proxy to clear

### Optional preventDefault

preventDefault?: boolean

Inherited from [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html).[preventDefault](src_core_async_modules_base_interface.ClearOptionsId.html#preventDefault)

* Defined in [src/core/async/modules/base/interface.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L114)

If true, then a cleanup handler of the task is prevented