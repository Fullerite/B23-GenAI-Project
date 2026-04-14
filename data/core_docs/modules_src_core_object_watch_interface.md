# Module src/core/object/watch/interface
## Index

### Interfaces

* [InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)
* [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)
* [PathModifier](../interfaces/src_core_object_watch_interface.PathModifier.html)
* [RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)
* [RawWatchHandlerParams](../interfaces/src_core_object_watch_interface.RawWatchHandlerParams.html)
* [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)
* [WatchHandler](../interfaces/src_core_object_watch_interface.WatchHandler.html)
* [WatchHandlerParams](../interfaces/src_core_object_watch_interface.WatchHandlerParams.html)
* [WatchHandlerParentParams](../interfaces/src_core_object_watch_interface.WatchHandlerParentParams.html)
* [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)
* [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)

### Type aliases

* [WatchDependencies](src_core_object_watch_interface.html#WatchDependencies)
* [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)
* [WatchPath](src_core_object_watch_interface.html#WatchPath)

## Type aliases

### WatchDependencies

WatchDependencies: [WatchPath](src_core_object_watch_interface.html#WatchPath)[] | [Dictionary](../interfaces/index.Dictionary.html)<[WatchPath](src_core_object_watch_interface.html#WatchPath)[]> | Map<[WatchPath](src_core_object_watch_interface.html#WatchPath), [CanArray](index.html#CanArray)<[WatchPath](src_core_object_watch_interface.html#WatchPath)>>

* Defined in [src/core/object/watch/interface.ts:11](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L11)

### WatchHandlersSet

WatchHandlersSet: Set<[RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)>

* Defined in [src/core/object/watch/interface.ts:459](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L459)

### WatchPath

WatchPath: [ObjectPropertyPath](index.html#ObjectPropertyPath)

* Defined in [src/core/object/watch/interface.ts:9](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L9)