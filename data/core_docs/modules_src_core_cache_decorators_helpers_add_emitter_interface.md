# Module src/core/cache/decorators/helpers/add-emitter/interface
## Index

### Interfaces

* [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)
* [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)
* [MutationEvent](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.MutationEvent.html)
* [MutationHandler](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.MutationHandler.html)

### Type aliases

* [AddEmitter](src_core_cache_decorators_helpers_add_emitter_interface.html#AddEmitter)
* [MethodsToWrap](src_core_cache_decorators_helpers_add_emitter_interface.html#MethodsToWrap)

## Type aliases

### AddEmitter

AddEmitter: <T, V, K>(cache: T) => [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)<T>

* Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L38)

#### Type declaration

* + <T, V, K>(cache: T): [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)<T>
  + #### Type parameters

    - #### T: [default](../interfaces/src_core_cache_interface.default.html)<V, K>
    - #### V = unknown
    - #### K: string = string

    #### Parameters

    - ##### cache: T

    #### Returns [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)<T>

### MethodsToWrap

MethodsToWrap: "set" | "remove" | "clear"

* Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L14)