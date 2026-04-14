# Module src/core/object/watch/engines/proxy
## Index

### Functions

* [set](src_core_object_watch_engines_proxy.html#set)
* [unset](src_core_object_watch_engines_proxy.html#unset)
* [watch](src_core_object_watch_engines_proxy.html#watch)

## Functions

### set

* set(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), value: unknown, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): void

* + Defined in [src/core/object/watch/engines/proxy.ts:434](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/proxy.ts#L434)

  Sets a new watchable value for an object by the specified path

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### value: unknown
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers

  #### Returns void

### unset

* unset(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): void

* + Defined in [src/core/object/watch/engines/proxy.ts:495](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/proxy.ts#L495)

  Deletes a watchable value for an object by the specified path

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers

  #### Returns void

### watch

* watch<T>(obj: T, path: [CanUndef](index.html#CanUndef)<unknown[]>, handler: [Nullable](index.html#Nullable)<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), opts?: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* watch<T>(obj: T, path: [CanUndef](index.html#CanUndef)<unknown[]>, handler: [Nullable](index.html#Nullable)<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)<unknown, unknown>>, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), opts: [CanUndef](index.html#CanUndef)<[InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)>, root: object, top: object): T

* + Defined in [src/core/object/watch/engines/proxy.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/proxy.ts#L59)

  Watches for changes of the specified object by using Proxy objects

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
* + Defined in [src/core/object/watch/engines/proxy.ts:78](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/proxy.ts#L78)

  Watches for changes of the specified object by using Proxy objects

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