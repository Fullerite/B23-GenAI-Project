# Interface WatchEngine
### Hierarchy

* WatchEngine

## Index

### Methods

* [set](src_core_object_watch_interface.WatchEngine.html#set)
* [unset](src_core_object_watch_interface.WatchEngine.html#unset)
* [watch](src_core_object_watch_interface.WatchEngine.html#watch)

## Methods

### set

* set(obj: object, path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath), value: unknown, handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)): void

* + Defined in [src/core/object/watch/interface.ts:371](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L371)

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath)
  + ##### value: unknown
  + ##### handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)

  #### Returns void

### unset

* unset(obj: object, path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath), handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)): void

* + Defined in [src/core/object/watch/interface.ts:372](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L372)

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath)
  + ##### handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)

  #### Returns void

### watch

* watch<T>(obj: T, path: [CanUndef](../modules/index.html#CanUndef)<unknown[]>, handler: [Nullable](../modules/index.html#Nullable)<[RawWatchHandler](src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>, handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet), opts?: [WatchOptions](src_core_object_watch_interface.WatchOptions.html)): [Watcher](src_core_object_watch_interface.Watcher.html)<T>
* watch<T>(obj: T, path: [CanUndef](../modules/index.html#CanUndef)<unknown[]>, handler: [Nullable](../modules/index.html#Nullable)<[RawWatchHandler](src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>, handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet), opts: [CanUndef](../modules/index.html#CanUndef)<[InternalWatchOptions](src_core_object_watch_interface.InternalWatchOptions.html)>, root: object, top: object): T

* + Defined in [src/core/object/watch/interface.ts:353](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L353)

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [CanUndef](../modules/index.html#CanUndef)<unknown[]>
  + ##### handler: [Nullable](../modules/index.html#Nullable)<[RawWatchHandler](src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>
  + ##### handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)
  + ##### Optional opts: [WatchOptions](src_core_object_watch_interface.WatchOptions.html)

  #### Returns [Watcher](src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/interface.ts:361](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L361)

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [CanUndef](../modules/index.html#CanUndef)<unknown[]>
  + ##### handler: [Nullable](../modules/index.html#Nullable)<[RawWatchHandler](src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>
  + ##### handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)
  + ##### opts: [CanUndef](../modules/index.html#CanUndef)<[InternalWatchOptions](src_core_object_watch_interface.InternalWatchOptions.html)>
  + ##### root: object
  + ##### top: object

  #### Returns T