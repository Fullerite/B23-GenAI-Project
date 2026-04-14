# Interface AsyncPromiseOptions
### Hierarchy

* [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + AsyncPromiseOptions

## Index

### Properties

* [destructor](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html#destructor)
* [group](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html#group)
* [join](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html#join)
* [label](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html#label)
* [name](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html#name)
* [onMutedResolve](src_core_async_modules_proxy_interface.AsyncPromiseOptions.html#onMutedResolve)

## Properties

### Optional destructor

destructor?: string

* Defined in [src/core/async/modules/proxy/interface.ts:67](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/interface.ts#L67)

Name of a destructor method

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

### Optional name

name?: string

* Defined in [src/core/async/modules/proxy/interface.ts:62](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/interface.ts#L62)

Namespace of the proxy

### Optional onMutedResolve

onMutedResolve?: [CanArray](../modules/index.html#CanArray)<Function | ((this: [default](../classes/src_core_async.default.html)<[default](../classes/src_core_async.default.html)<any>>, e: [AnyFunction](index.AnyFunction.html)<any[], any>) => [AnyFunction](index.AnyFunction.html)<any[], any>)>

* Defined in [src/core/async/modules/proxy/interface.ts:73](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/interface.ts#L73)

Handler/s of muted promise resolving.
These handlers are invoked when occurring resolving the promise if it is muted.