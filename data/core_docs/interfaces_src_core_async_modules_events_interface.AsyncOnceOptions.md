# Interface AsyncOnceOptions<T>
### Type parameters

* #### T: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html)<T>
  + AsyncOnceOptions

## Index

### Properties

* [group](src_core_async_modules_events_interface.AsyncOnceOptions.html#group)
* [join](src_core_async_modules_events_interface.AsyncOnceOptions.html#join)
* [label](src_core_async_modules_events_interface.AsyncOnceOptions.html#label)
* [onClear](src_core_async_modules_events_interface.AsyncOnceOptions.html#onClear)
* [onMerge](src_core_async_modules_events_interface.AsyncOnceOptions.html#onMerge)
* [onMutedCall](src_core_async_modules_events_interface.AsyncOnceOptions.html#onMutedCall)
* [options](src_core_async_modules_events_interface.AsyncOnceOptions.html#options)
* [promise](src_core_async_modules_events_interface.AsyncOnceOptions.html#promise)

## Properties

### Optional group

group?: string

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[group](src_core_async_modules_base_interface.AsyncCbOptions.html#group)

* Defined in [src/core/async/modules/base/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L46)

Group name of a task

### Optional join

join?: [Join](../modules/src_core_async_modules_base_interface.html#Join)

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[join](src_core_async_modules_base_interface.AsyncCbOptions.html#join)

* Defined in [src/core/async/modules/base/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L53)

Strategy to join competitive tasks (with the same labels):

1. `true` - all tasks are joined to the first;
2. `'replace'` - all tasks are joined (replaced) to the last (only for promises).

### Optional label

label?: [Label](../modules/src_core_async_modules_base_interface.html#Label)

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[label](src_core_async_modules_base_interface.AsyncCbOptions.html#label)

* Defined in [src/core/async/modules/base/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L41)

Label of a task (the previous task with the same label will be canceled)

### Optional onClear

onClear?: [CanArray](../modules/index.html#CanArray)<Function | ((this: T, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<T>) => void)>

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[onClear](src_core_async_modules_base_interface.AsyncCbOptions.html#onClear)

* Defined in [src/core/async/modules/base/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L66)

Handler/s of task clearing

### Optional onMerge

onMerge?: [CanArray](../modules/index.html#CanArray)<Function | ((this: T, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<T>) => void)>

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[onMerge](src_core_async_modules_base_interface.AsyncCbOptions.html#onMerge)

* Defined in [src/core/async/modules/base/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L71)

Handler/s of task merging: a task should merge to another task with the same label and with "join: true" strategy

### Optional onMutedCall

onMutedCall?: [CanArray](../modules/index.html#CanArray)<Function | ((this: T, e: [TaskCtx](../modules/src_core_async_modules_base_interface.html#TaskCtx)<T>) => void)>

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[onMutedCall](src_core_async_modules_base_interface.AsyncCbOptions.html#onMutedCall)

* Defined in [src/core/async/modules/base/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L77)

Handler/s of muted task calling.
These handlers are invoked when occurring calling the task if it is muted.

### Optional options

options?: [Dictionary](index.Dictionary.html)<unknown>

* Defined in [src/core/async/modules/events/interface.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L65)

Additional options for the emitter

### Optional promise

promise?: boolean

Inherited from [AsyncCbOptions](src_core_async_modules_base_interface.AsyncCbOptions.html).[promise](src_core_async_modules_base_interface.AsyncCbOptions.html#promise)

* Defined in [src/core/async/modules/base/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L61)

If true, then a task namespace is marked as promisified

default
:   `false`