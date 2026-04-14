# Module src/core/object/watch/engines/accessors
## Index

### Functions

* [set](src_core_object_watch_engines_accessors.html#set)
* [setWatchAccessors](src_core_object_watch_engines_accessors.html#setWatchAccessors)
* [unset](src_core_object_watch_engines_accessors.html#unset)
* [watch](src_core_object_watch_engines_accessors.html#watch)

## Functions

### set

* set(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), value: unknown, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): void

* + Defined in [src/core/object/watch/engines/accessors.ts:264](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/accessors.ts#L264)

  Sets a new watchable value for an object by the specified path

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### value: unknown
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers

  #### Returns void

### setWatchAccessors

* setWatchAccessors(obj: object, key: string, path: [CanUndef](index.html#CanUndef)<unknown[]>, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), root: object, top?: object, opts?: [InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)): [Dictionary](../interfaces/index.Dictionary.html)

* + Defined in [src/core/object/watch/engines/accessors.ts:440](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/accessors.ts#L440)

  Sets a pair of accessors to watch the specified property and returns a proxy object

  #### Parameters

  + ##### obj: object

    object to watch
  + ##### key: string

    property key to watch
  + ##### path: [CanUndef](index.html#CanUndef)<unknown[]>

    path to the object to watch from the root object
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers
  + ##### root: object

    link to the root object of watching
  + ##### Optional top: object
  + ##### Optional opts: [InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)

  #### Returns [Dictionary](../interfaces/index.Dictionary.html)

### unset

* unset(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): void

* + Defined in [src/core/object/watch/engines/accessors.ts:364](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/accessors.ts#L364)

  Unsets a watchable value for an object by the specified path

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers

  #### Returns void

### watch

* watch<T>(obj: T, path: [CanUndef](index.html#CanUndef)<unknown[]>, handler: [Nullable](index.html#Nullable)<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), opts?: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* watch<T>(obj: T, path: [CanUndef](index.html#CanUndef)<unknown[]>, handler: [Nullable](index.html#Nullable)<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), opts: [CanUndef](index.html#CanUndef)<[InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)>, root: object, top: object): T

* + Defined in [src/core/object/watch/engines/accessors.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/accessors.ts#L57)

  Watches for changes of the specified object by using accessors

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [CanUndef](index.html#CanUndef)<unknown[]>

    base path to object properties: it is provided to a watch handler with parameters
  + ##### handler: [Nullable](index.html#Nullable)<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>

    callback that is invoked on every mutation hook
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers
  + ##### Optional opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/engines/accessors.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/accessors.ts#L76)

  Watches for changes of the specified object by using accessors

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [CanUndef](index.html#CanUndef)<unknown[]>

    base path to object properties: it is provided to a watch handler with parameters
  + ##### handler: [Nullable](index.html#Nullable)<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>

    callback that is invoked on every mutation hook
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers
  + ##### opts: [CanUndef](index.html#CanUndef)<[InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)>

    additional options
  + ##### root: object

    link to the root object of watching
  + ##### top: object

    link to the top object of watching

  #### Returns T