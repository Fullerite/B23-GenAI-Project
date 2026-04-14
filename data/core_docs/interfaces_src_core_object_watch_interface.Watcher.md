# Interface Watcher<T>
### Type parameters

* #### T: object = object

### Hierarchy

* Watcher

## Index

### Properties

* [proxy](src_core_object_watch_interface.Watcher.html#proxy)

### Methods

* [delete](src_core_object_watch_interface.Watcher.html#delete)
* [set](src_core_object_watch_interface.Watcher.html#set)
* [unwatch](src_core_object_watch_interface.Watcher.html#unwatch)

## Properties

### proxy

proxy: T

* Defined in [src/core/object/watch/interface.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L20)

A proxy object to watch

## Methods

### delete

* delete(path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath)): void

* + Defined in [src/core/object/watch/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L36)

  Deletes a watchable value from the proxy object by the specified path.
  To restore watching for this property, use `set`.

  #### Parameters

  + ##### path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath)

  #### Returns void

### set

* set(path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath), value: unknown): void

* + Defined in [src/core/object/watch/interface.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L28)

  Sets a new watchable value for the proxy object by the specified path

  #### Parameters

  + ##### path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath)
  + ##### value: unknown

  #### Returns void

### unwatch

* unwatch(): void

* + Defined in [src/core/object/watch/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L41)

  Cancels watching for the proxy object

  #### Returns void