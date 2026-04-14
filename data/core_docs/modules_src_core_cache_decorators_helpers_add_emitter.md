# Module src/core/cache/decorators/helpers/add-emitter
[# core/cache/decorators/helpers/add-emitter](#corecachedecoratorshelpersadd-emitter)

This module provides a helper for [Cache](src_core_cache.html#Cache) decorators to add a feature of emitting mutation events caused by side effects.

```
import addEmitter from 'core/cache/decorators/helpers/add-emitter';  
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
// `originalRemove` doesn't emit events  
const {remove: originalRemove, subscribe} = addEmitter(cache);  
  
// Now cache.eventEmitter emit event 'remove' with args [cache(instance what call emit), [...args]]  
cache.remove('foo');  
  
// (eventName, instanceOfListener, callback) - callback invoked only if emit was made by children of instanceOfListener;  
subscribe('remove', cache, (key) => {  
  console.log(key);  
});
```

## Index

### References

* [AddEmitter](src_core_cache_decorators_helpers_add_emitter.html#AddEmitter)
* [AddEmitterReturn](src_core_cache_decorators_helpers_add_emitter.html#AddEmitterReturn)
* [CacheWithEmitter](src_core_cache_decorators_helpers_add_emitter.html#CacheWithEmitter)
* [MethodsToWrap](src_core_cache_decorators_helpers_add_emitter.html#MethodsToWrap)
* [MutationEvent](src_core_cache_decorators_helpers_add_emitter.html#MutationEvent)
* [MutationHandler](src_core_cache_decorators_helpers_add_emitter.html#MutationHandler)
* [eventEmitter](src_core_cache_decorators_helpers_add_emitter.html#eventEmitter)

### Variables

* [$$](src_core_cache_decorators_helpers_add_emitter.html#__)

### Functions

* [default](src_core_cache_decorators_helpers_add_emitter.html#default)

## References

### AddEmitter

Re-exports [AddEmitter](src_core_cache_decorators_helpers_add_emitter_interface.html#AddEmitter)

### AddEmitterReturn

Re-exports [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)

### CacheWithEmitter

Re-exports [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)

### MethodsToWrap

Re-exports [MethodsToWrap](src_core_cache_decorators_helpers_add_emitter_interface.html#MethodsToWrap)

### MutationEvent

Re-exports [MutationEvent](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.MutationEvent.html)

### MutationHandler

Re-exports [MutationHandler](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.MutationHandler.html)

### eventEmitter

Re-exports [eventEmitter](src_core_cache_decorators_helpers_add_emitter_const.html#eventEmitter)

## Variables

### Const $$

$$: [StrictDictionary](../interfaces/index.StrictDictionary.html)<symbol> = ...

* Defined in [src/core/cache/decorators/helpers/add-emitter/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/index.ts#L34)

## Functions

### default

* default<T, V, K>(cache: T): [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)<T, unknown, string>

* + Defined in [src/core/cache/decorators/helpers/add-emitter/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/index.ts#L43)

  Adds an event emitter to the provided cache object and wraps all mutation events to emit events, i.e.,
  it mutates the original object. The function returns an object with the original unwrapped methods and
  a method to subscribe to these events.

  #### Type parameters

  + #### T: [default](../interfaces/src_core_cache_interface.default.html)<V, K, T>
  + #### V = unknown
  + #### K: string = string

  #### Parameters

  + ##### cache: T

  #### Returns [AddEmitterReturn](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.AddEmitterReturn.html)<T, unknown, string>