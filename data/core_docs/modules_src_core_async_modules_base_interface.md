# Module src/core/async/modules/base/interface
## Index

### Interfaces

* [AsyncCbOptions](../interfaces/src_core_async_modules_base_interface.AsyncCbOptions.html)
* [AsyncCbOptionsSingle](../interfaces/src_core_async_modules_base_interface.AsyncCbOptionsSingle.html)
* [AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html)
* [AsyncProxyOptions](../interfaces/src_core_async_modules_base_interface.AsyncProxyOptions.html)
* [BoundFn](../interfaces/src_core_async_modules_base_interface.BoundFn.html)
* [ClearFn](../interfaces/src_core_async_modules_base_interface.ClearFn.html)
* [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)
* [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)
* [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)
* [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)
* [IdObject](../interfaces/src_core_async_modules_base_interface.IdObject.html)
* [LocalCache](../interfaces/src_core_async_modules_base_interface.LocalCache.html)
* [Task](../interfaces/src_core_async_modules_base_interface.Task.html)

### Type aliases

* [AsyncCb](src_core_async_modules_base_interface.html#AsyncCb)
* [ClearReason](src_core_async_modules_base_interface.html#ClearReason)
* [Group](src_core_async_modules_base_interface.html#Group)
* [Join](src_core_async_modules_base_interface.html#Join)
* [Label](src_core_async_modules_base_interface.html#Label)
* [MarkReason](src_core_async_modules_base_interface.html#MarkReason)
* [ProxyCb](src_core_async_modules_base_interface.html#ProxyCb)
* [StrictClearOptions](src_core_async_modules_base_interface.html#StrictClearOptions)
* [StrictClearOptionsId](src_core_async_modules_base_interface.html#StrictClearOptionsId)
* [TaskCtx](src_core_async_modules_base_interface.html#TaskCtx)

## Type aliases

### AsyncCb

AsyncCb<CTX>: [ProxyCb](src_core_async_modules_base_interface.html#ProxyCb)<[TaskCtx](src_core_async_modules_base_interface.html#TaskCtx)<CTX>, void, CTX>

* Defined in [src/core/async/modules/base/interface.ts:147](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L147)

#### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)

### ClearReason

ClearReason: [MarkReason](src_core_async_modules_base_interface.html#MarkReason) | "muting" | "collision"

* Defined in [src/core/async/modules/base/interface.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L28)

Reason why a task can be killed (cleared)

### Group

Group: string

* Defined in [src/core/async/modules/base/interface.ts:12](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L12)

### Join

Join: boolean | "replace"

* Defined in [src/core/async/modules/base/interface.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L13)

### Label

Label: string | symbol

* Defined in [src/core/async/modules/base/interface.ts:11](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L11)

### MarkReason

MarkReason: "id" | "label" | "group" | "rgxp" | "all"

* Defined in [src/core/async/modules/base/interface.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L18)

Reason why a task can be marked

### ProxyCb

ProxyCb<A, R, CTX>: A extends never ? (this: CTX) => R : A extends any[] ? (this: CTX, ...args: A) => R : ((this: CTX, e: A) => R) | Function

* Defined in [src/core/async/modules/base/interface.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L139)

#### Type parameters

* #### A = unknown
* #### R = unknown
* #### CTX: object = [default](../classes/src_core_async.default.html)

### StrictClearOptions

StrictClearOptions: Omit<[ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html), "label"> | [Overwrite](index.html#Overwrite)<[ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html), { group: [Group](src_core_async_modules_base_interface.html#Group) | RegExp; label: [Label](src_core_async_modules_base_interface.html#Label) }>

* Defined in [src/core/async/modules/base/interface.ts:131](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L131)

### StrictClearOptionsId

StrictClearOptionsId<ID>: Omit<[ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<ID>, "label"> | [Overwrite](index.html#Overwrite)<[ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<ID>, { group: [Group](src_core_async_modules_base_interface.html#Group) | RegExp; label: [Label](src_core_async_modules_base_interface.html#Label) }>

* Defined in [src/core/async/modules/base/interface.ts:135](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L135)

#### Type parameters

* #### ID = any

### TaskCtx

TaskCtx<CTX>: { link: [Task](../interfaces/src_core_async_modules_base_interface.Task.html)<CTX>; reason?: [ClearReason](src_core_async_modules_base_interface.html#ClearReason); replacedBy?: [Task](../interfaces/src_core_async_modules_base_interface.Task.html)<CTX>; type: string } & [AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html) & [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)<unknown>

* Defined in [src/core/async/modules/base/interface.ts:222](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/interface.ts#L222)

Context of a task

#### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)