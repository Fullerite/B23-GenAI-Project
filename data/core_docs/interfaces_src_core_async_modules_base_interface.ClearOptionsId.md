# Interface ClearOptionsId<ID>
### Type parameters

* #### ID = any

### Hierarchy

* [ClearOptions](src_core_async_modules_base_interface.ClearOptions.html)
  + ClearOptionsId
    - [ClearProxyOptions](src_core_async_modules_base_interface.ClearProxyOptions.html)

## Index

### Properties

* [group](src_core_async_modules_base_interface.ClearOptionsId.html#group)
* [id](src_core_async_modules_base_interface.ClearOptionsId.html#id)
* [label](src_core_async_modules_base_interface.ClearOptionsId.html#label)
* [preventDefault](src_core_async_modules_base_interface.ClearOptionsId.html#preventDefault)

## Properties

### Optional group

group?: string | RegExp

Inherited from [ClearOptions](src_core_async_modules_base_interface.ClearOptions.html).[group](src_core_async_modules_base_interface.ClearOptions.html#group)

* Defined in [src/core/async/modules/base/interface.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L109)

Group name of the task to clear

### Optional id

id?: ID

* Defined in [src/core/async/modules/base/interface.ts:121](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L121)

Identifier of the task to clear

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [ClearOptions](src_core_async_modules_base_interface.ClearOptions.html).[label](src_core_async_modules_base_interface.ClearOptions.html#label)

* Defined in [src/core/async/modules/base/interface.ts:104](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L104)

Label of the task to clear

### Optional preventDefault

preventDefault?: boolean

Inherited from [ClearOptions](src_core_async_modules_base_interface.ClearOptions.html).[preventDefault](src_core_async_modules_base_interface.ClearOptions.html#preventDefault)

* Defined in [src/core/async/modules/base/interface.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L114)

If true, then a cleanup handler of the task is prevented