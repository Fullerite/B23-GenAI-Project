# Interface AsyncPromisifyOnceOptions<E, R, CTX>
### Type parameters

* #### E = unknown
* #### R = unknown
* #### CTX: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + AsyncPromisifyOnceOptions

## Index

### Properties

* [group](src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html#group)
* [handler](src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html#handler)
* [join](src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html#join)
* [label](src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html#label)
* [options](src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html#options)

## Properties

### Optional group

group?: string

Inherited from [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html).[group](src_core_async_modules_base_interface.AsyncOptions.html#group)

* Defined in [src/core/async/modules/base/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L46)

Group name of a task

### Optional handler

handler?: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>

* Defined in [src/core/async/modules/events/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L76)

Event handler (the result of invoking is provided to a promise)

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

### Optional options

options?: [Dictionary](index.Dictionary.html)<unknown>

* Defined in [src/core/async/modules/events/interface.ts:81](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L81)

Additional options for the emitter