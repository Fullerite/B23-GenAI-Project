# Interface ClearOptions
### Hierarchy

* ClearOptions
  + [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html)

## Index

### Properties

* [group](src_core_async_modules_base_interface.ClearOptions.html#group)
* [label](src_core_async_modules_base_interface.ClearOptions.html#label)
* [preventDefault](src_core_async_modules_base_interface.ClearOptions.html#preventDefault)

## Properties

### Optional group

group?: string | RegExp

* Defined in [src/core/async/modules/base/interface.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L109)

Group name of the task to clear

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

* Defined in [src/core/async/modules/base/interface.ts:104](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L104)

Label of the task to clear

### Optional preventDefault

preventDefault?: boolean

* Defined in [src/core/async/modules/base/interface.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L114)

If true, then a cleanup handler of the task is prevented