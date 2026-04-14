# Interface WrapParams
### Hierarchy

* [WrapOptions](src_core_object_watch_wrap_interface.WrapOptions.html)
  + WrapParams

## Index

### Properties

* [fromProto](src_core_object_watch_wrap_interface.WrapParams.html#fromProto)
* [handlers](src_core_object_watch_wrap_interface.WrapParams.html#handlers)
* [original](src_core_object_watch_wrap_interface.WrapParams.html#original)
* [path](src_core_object_watch_wrap_interface.WrapParams.html#path)
* [root](src_core_object_watch_wrap_interface.WrapParams.html#root)
* [top](src_core_object_watch_wrap_interface.WrapParams.html#top)
* [watchOpts](src_core_object_watch_wrap_interface.WrapParams.html#watchOpts)

## Properties

### Optional fromProto

fromProto?: boolean

Inherited from [WrapOptions](src_core_object_watch_wrap_interface.WrapOptions.html).[fromProto](src_core_object_watch_wrap_interface.WrapOptions.html#fromProto)

* Defined in [src/core/object/watch/wrap/interface.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L32)

True if the property to watch is taken from a prototype

default
:   `false`

### handlers

handlers: [WatchHandlersSet](../modules/src_core_object_watch_interface.html#WatchHandlersSet)

* Defined in [src/core/object/watch/wrap/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L42)

### original

original: Function

* Defined in [src/core/object/watch/wrap/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L41)

### path

path: unknown[]

Inherited from [WrapOptions](src_core_object_watch_wrap_interface.WrapOptions.html).[path](src_core_object_watch_wrap_interface.WrapOptions.html#path)

* Defined in [src/core/object/watch/wrap/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L26)

Base path to object properties

### root

root: object

Inherited from [WrapOptions](src_core_object_watch_wrap_interface.WrapOptions.html).[root](src_core_object_watch_wrap_interface.WrapOptions.html#root)

* Defined in [src/core/object/watch/wrap/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L15)

Link to the root object of watching

### Optional top

top?: object

Inherited from [WrapOptions](src_core_object_watch_wrap_interface.WrapOptions.html).[top](src_core_object_watch_wrap_interface.WrapOptions.html#top)

* Defined in [src/core/object/watch/wrap/interface.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L21)

Link to the top object of watching
(the first level property of the root)

### watchOpts

watchOpts: [WatchOptions](src_core_object_watch_interface.WatchOptions.html)

Inherited from [WrapOptions](src_core_object_watch_wrap_interface.WrapOptions.html).[watchOpts](src_core_object_watch_wrap_interface.WrapOptions.html#watchOpts)

* Defined in [src/core/object/watch/wrap/interface.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/interface.ts#L37)

Watch options