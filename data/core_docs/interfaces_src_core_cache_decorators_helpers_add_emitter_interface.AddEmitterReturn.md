# Interface AddEmitterReturn<T, V, K>
### Type parameters

* #### T: [default](src_core_cache_interface.default.html)<V, K>
* #### V = unknown
* #### K: string = string

### Hierarchy

* AddEmitterReturn

## Index

### Properties

* [clear](src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html#clear)
* [remove](src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html#remove)
* [set](src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html#set)

### Methods

* [subscribe](src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html#subscribe)

## Properties

### clear

clear: T["clear"]

* Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L49)

see
:   [[Cache.clear]]

### remove

remove: T["remove"]

* Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L46)

see
:   [[Cache.remove]]

### set

set: T["set"]

* Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L43)

see
:   [[Cache.set]]

## Methods

### subscribe

* subscribe<M>(method: M, obj: object, cb: [MutationHandler](src_core_cache_decorators_helpers_add_emitter_interface.MutationHandler.html)<T[M]>): void

* + Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L58)

  Subscribes for mutations of the specified cache object

  #### Type parameters

  + #### M: [MethodsToWrap](../modules/src_core_cache_decorators_helpers_add_emitter_interface.html#MethodsToWrap)

  #### Parameters

  + ##### method: M

    mutation method to subscribe
  + ##### obj: object

    object whose mutations we are handling
  + ##### cb: [MutationHandler](src_core_cache_decorators_helpers_add_emitter_interface.MutationHandler.html)<T[M]>

    callback that invokes when occurring mutations

  #### Returns void