# Interface RawWatchHandlerParams
Parameters of a mutation event

### Hierarchy

* RawWatchHandlerParams
  + [WatchHandlerParams](src_core_object_watch_interface.WatchHandlerParams.html)

## Index

### Properties

* [fromProto](src_core_object_watch_interface.RawWatchHandlerParams.html#fromProto)
* [obj](src_core_object_watch_interface.RawWatchHandlerParams.html#obj)
* [path](src_core_object_watch_interface.RawWatchHandlerParams.html#path)
* [root](src_core_object_watch_interface.RawWatchHandlerParams.html#root)
* [top](src_core_object_watch_interface.RawWatchHandlerParams.html#top)

## Properties

### fromProto

fromProto: boolean

* Defined in [src/core/object/watch/interface.ts:408](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L408)

True if the mutation has occurred on a prototype of the watched object

### obj

obj: object

* Defined in [src/core/object/watch/interface.ts:392](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L392)

Link to the object that is watched

### path

path: unknown[]

* Defined in [src/core/object/watch/interface.ts:413](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L413)

Path to a property that was changed

### root

root: object

* Defined in [src/core/object/watch/interface.ts:397](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L397)

Link to the root object of watching

### Optional top

top?: object

* Defined in [src/core/object/watch/interface.ts:403](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L403)

Link to the top property of watching
(the first level property of the root)