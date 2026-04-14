# Module src/core/object/proxy-clone/helpers
## Index

### Classes

* [Descriptor](../classes/src_core_object_proxy_clone_helpers.Descriptor.html)

### Functions

* [getRawValueFromStore](src_core_object_proxy_clone_helpers.html#getRawValueFromStore)
* [resolveTarget](src_core_object_proxy_clone_helpers.html#resolveTarget)

## Functions

### getRawValueFromStore

* getRawValueFromStore(key: PropertyKey, valStore: [CanUndef](index.html#CanUndef)<Map<unknown, unknown>>): unknown

* + Defined in [src/core/object/proxy-clone/helpers.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/helpers.ts#L71)

  Returns a raw value by a key from the specified store

  #### Parameters

  + ##### key: PropertyKey
  + ##### valStore: [CanUndef](index.html#CanUndef)<Map<unknown, unknown>>

  #### Returns unknown

### resolveTarget

* resolveTarget<T>(target: T, store: [Store](src_core_object_proxy_clone_interface.html#Store)): [ResolvedTarget](../interfaces/src_core_object_proxy_clone_interface.ResolvedTarget.html)<T>

* + Defined in [src/core/object/proxy-clone/helpers.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/helpers.ts#L88)

  Resolves the specified target by a value from the store and returns it

  #### Type parameters

  + #### T

  #### Parameters

  + ##### target: T
  + ##### store: [Store](src_core_object_proxy_clone_interface.html#Store)

  #### Returns [ResolvedTarget](../interfaces/src_core_object_proxy_clone_interface.ResolvedTarget.html)<T>