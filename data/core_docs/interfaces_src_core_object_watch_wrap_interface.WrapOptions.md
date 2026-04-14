# Interface WrapOptions
### Hierarchy

* WrapOptions
  + [WrapParams](src_core_object_watch_wrap_interface.WrapParams.html)

## Index

### Properties

* [fromProto](src_core_object_watch_wrap_interface.WrapOptions.html#fromProto)
* [path](src_core_object_watch_wrap_interface.WrapOptions.html#path)
* [root](src_core_object_watch_wrap_interface.WrapOptions.html#root)
* [top](src_core_object_watch_wrap_interface.WrapOptions.html#top)
* [watchOpts](src_core_object_watch_wrap_interface.WrapOptions.html#watchOpts)

## Properties

### Optional fromProto

fromProto?: boolean

* Defined in [src/core/object/watch/wrap/interface.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L32)

True if the property to watch is taken from a prototype

default
:   `false`

### path

path: unknown[]

* Defined in [src/core/object/watch/wrap/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L26)

Base path to object properties

### root

root: object

* Defined in [src/core/object/watch/wrap/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L15)

Link to the root object of watching

### Optional top

top?: object

* Defined in [src/core/object/watch/wrap/interface.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L21)

Link to the top object of watching
(the first level property of the root)

### watchOpts

watchOpts: [WatchOptions](src_core_object_watch_interface.WatchOptions.html)

* Defined in [src/core/object/watch/wrap/interface.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L37)

Watch options