# Interface AsyncOnOptions<CTX>
### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html)<CTX>
  + AsyncOnOptions

## Index

### Properties

* [group](src_core_async_modules_events_interface.AsyncOnOptions.html#group)
* [join](src_core_async_modules_events_interface.AsyncOnOptions.html#join)
* [label](src_core_async_modules_events_interface.AsyncOnOptions.html#label)
* [onClear](src_core_async_modules_events_interface.AsyncOnOptions.html#onClear)
* [onMerge](src_core_async_modules_events_interface.AsyncOnOptions.html#onMerge)
* [onMutedCall](src_core_async_modules_events_interface.AsyncOnOptions.html#onMutedCall)
* [options](src_core_async_modules_events_interface.AsyncOnOptions.html#options)
* [promise](src_core_async_modules_events_interface.AsyncOnOptions.html#promise)
* [single](src_core_async_modules_events_interface.AsyncOnOptions.html#single)

## Properties

### Optional group

group?: string

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[group](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#group)

* Defined in [src/core/async/modules/base/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L46)

Group name of a task

### Optional join

join?: [Join](../modules/src_core_async_modules_base_interface.html#Join)

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[join](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#join)

* Defined in [src/core/async/modules/base/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L53)

Strategy to join competitive tasks (with the same labels):

1. `true` - all tasks are joined to the first;
2. `'replace'` - all tasks are joined (replaced) to the last (only for promises).

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[label](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#label)

* Defined in [src/core/async/modules/base/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L41)

Label of a task (the previous task with the same label will be canceled)

### Optional onClear

onClear?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[onClear](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#onClear)

* Defined in [src/core/async/modules/base/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L66)

Handler/s of task clearing

### Optional onMerge

onMerge?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[onMerge](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#onMerge)

* Defined in [src/core/async/modules/base/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L71)

Handler/s of task merging: a task should merge to another task with the same label and with "join: true" strategy

### Optional onMutedCall

onMutedCall?: [CanArray](../modules/index.html#CanArray)<Function | ((this: CTX, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<CTX>) => void)>

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[onMutedCall](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#onMutedCall)

* Defined in [src/core/async/modules/base/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L77)

Handler/s of muted task calling.
These handlers are invoked when occurring calling the task if it is muted.

### Optional options

options?: [Dictionary](index.Dictionary.html)<unknown>

* Defined in [src/core/async/modules/events/interface.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L58)

Additional options for the emitter

### Optional promise

promise?: boolean

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[promise](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#promise)

* Defined in [src/core/async/modules/base/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L61)

If true, then a task namespace is marked as promisified

default
:   `false`

### Optional single

single?: boolean

Inherited from [AsyncCbOptionsSingle](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html).[single](src_core_async_modules_base_interface.AsyncCbOptionsSingle.html#single)

* Defined in [src/core/async/modules/base/interface.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L85)

If false, then the proxy supports multiple callings

default
:   `true`