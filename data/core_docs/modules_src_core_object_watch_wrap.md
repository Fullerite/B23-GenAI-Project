# Module src/core/object/watch/wrap
## Index

### References

* [StructureWrapper](src_core_object_watch_wrap.html#StructureWrapper)
* [StructureWrappers](src_core_object_watch_wrap.html#StructureWrappers)
* [WrapMethod](src_core_object_watch_wrap.html#WrapMethod)
* [WrapMethodObject](src_core_object_watch_wrap.html#WrapMethodObject)
* [WrapOptions](src_core_object_watch_wrap.html#WrapOptions)
* [WrapParams](src_core_object_watch_wrap.html#WrapParams)
* [WrapResult](src_core_object_watch_wrap.html#WrapResult)

### Functions

* [bindMutationHooks](src_core_object_watch_wrap.html#bindMutationHooks)

## References

### StructureWrapper

Re-exports [StructureWrapper](../interfaces/src_core_object_watch_wrap_interface.StructureWrapper.html)

### StructureWrappers

Re-exports [StructureWrappers](src_core_object_watch_wrap_interface.html#StructureWrappers)

### WrapMethod

Re-exports [WrapMethod](../interfaces/src_core_object_watch_wrap_interface.WrapMethod.html)

### WrapMethodObject

Re-exports [WrapMethodObject](../interfaces/src_core_object_watch_wrap_interface.WrapMethodObject.html)

### WrapOptions

Re-exports [WrapOptions](../interfaces/src_core_object_watch_wrap_interface.WrapOptions.html)

### WrapParams

Re-exports [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)

### WrapResult

Re-exports [WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)

## Functions

### bindMutationHooks

* bindMutationHooks<T>(obj: T, opts: [WrapOptions](../interfaces/src_core_object_watch_wrap_interface.WrapOptions.html), handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): T
* bindMutationHooks<T>(obj: T, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): T

* + Defined in [src/core/object/watch/wrap/index.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/index.ts#L26)

  Wraps mutation methods of the specified object that they be able to emit events about mutations

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### opts: [WrapOptions](../interfaces/src_core_object_watch_wrap_interface.WrapOptions.html)

    additional options
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of callbacks that are invoked on every mutation hooks

  #### Returns T
* + Defined in [src/core/object/watch/wrap/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/index.ts#L34)

  Wraps mutation methods of the specified object that they be able to emit events about mutations

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of callbacks that are invoked on every mutation hooks

  #### Returns T