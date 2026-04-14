# Interface AsyncOptions
### Hierarchy

* AsyncOptions
  + [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html)
  + [AsyncPromisifyOnceOptions](src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html)
  + [AsyncRequestOptions](src_core_async_modules_proxy_interface.AsyncRequestOptions.html)
  + [AsyncPromiseOptions](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html)
  + [AsyncWaitOptions](src_core_async_modules_timers_interface.AsyncWaitOptions.html)
  + [AsyncIdleOptions](src_core_async_modules_timers_interface.AsyncIdleOptions.html)

## Index

### Properties

* [group](src_core_async_modules_base_interface.AsyncOptions.html#group)
* [join](src_core_async_modules_base_interface.AsyncOptions.html#join)
* [label](src_core_async_modules_base_interface.AsyncOptions.html#label)

## Properties

### Optional group

group?: string

* Defined in [src/core/async/modules/base/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L46)

Group name of a task

### Optional join

join?: [Join](../modules/src_core_async_modules_base_interface.html#Join)

* Defined in [src/core/async/modules/base/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L53)

Strategy to join competitive tasks (with the same labels):

1. `true` - all tasks are joined to the first;
2. `'replace'` - all tasks are joined (replaced) to the last (only for promises).

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

* Defined in [src/core/async/modules/base/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L41)

Label of a task (the previous task with the same label will be canceled)