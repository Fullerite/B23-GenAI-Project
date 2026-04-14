# Interface AsyncCbOptions<CTX>
### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + AsyncCbOptions
    - [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html)
    - [AsyncOnceOptions](src_core_async_modules_events_interface.AsyncOnceOptions.html)
    - [AsyncRequestIdleCallbackOptions](src_core_async_modules_timers_interface.AsyncRequestIdleCallbackOptions.html)

## Index

### Properties

* [group](src_core_async_modules_base_interface.AsyncCbOptions.html#group)
* [join](src_core_async_modules_base_interface.AsyncCbOptions.html#join)
* [label](src_core_async_modules_base_interface.AsyncCbOptions.html#label)
* [onClear](src_core_async_modules_base_interface.AsyncCbOptions.html#onClear)
* [onMerge](src_core_async_modules_base_interface.AsyncCbOptions.html#onMerge)
* [onMutedCall](src_core_async_modules_base_interface.AsyncCbOptions.html#onMutedCall)
* [promise](src_core_async_modules_base_interface.AsyncCbOptions.html#promise)

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

### Optional onClear

onClear?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

* Defined in [src/core/async/modules/base/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L66)

Handler/s of task clearing

### Optional onMerge

onMerge?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

* Defined in [src/core/async/modules/base/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L71)

Handler/s of task merging: a task should merge to another task with the same label and with "join: true" strategy

### Optional onMutedCall

onMutedCall?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

* Defined in [src/core/async/modules/base/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L77)

Handler/s of muted task calling.
These handlers are invoked when occurring calling the task if it is muted.

### Optional promise

promise?: boolean

* Defined in [src/core/async/modules/base/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L61)

If true, then a task namespace is marked as promisified

default
:   `false`