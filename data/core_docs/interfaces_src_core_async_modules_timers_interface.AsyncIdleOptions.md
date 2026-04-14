# Interface AsyncIdleOptions
### Hierarchy

* [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + AsyncIdleOptions

## Index

### Properties

* [group](src_core_async_modules_timers_interface.AsyncIdleOptions.html#group)
* [join](src_core_async_modules_timers_interface.AsyncIdleOptions.html#join)
* [label](src_core_async_modules_timers_interface.AsyncIdleOptions.html#label)
* [timeout](src_core_async_modules_timers_interface.AsyncIdleOptions.html#timeout)

## Properties

### Optional group

group?: string

Inherited from [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html).[group](src_core_async_modules_base_interface.AsyncOptions.html#group)

* Defined in [src/core/async/modules/base/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L46)

Group name of a task

### Optional join

join?: [Join](../modules/src_core_async_modules_base_interface.html#Join)

Inherited from [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html).[join](src_core_async_modules_base_interface.AsyncOptions.html#join)

* Defined in [src/core/async/modules/base/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L53)

Strategy to join competitive tasks (with the same labels):

1. `true` - all tasks are joined to the first;
2. `'replace'` - all tasks are joined (replaced) to the last (only for promises).

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html).[label](src_core_async_modules_base_interface.AsyncOptions.html#label)

* Defined in [src/core/async/modules/base/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L41)

Label of a task (the previous task with the same label will be canceled)

### Optional timeout

timeout?: number

* Defined in [src/core/async/modules/timers/interface.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/timers/interface.ts#L25)

Timeout value for the native requestIdleCallback function