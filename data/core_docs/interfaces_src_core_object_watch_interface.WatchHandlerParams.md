# Interface WatchHandlerParams
Extended parameters of a mutation event

### Hierarchy

* [RawWatchHandlerParams](src_core_object_watch_interface.RawWatchHandlerParams.html)
  + WatchHandlerParams

## Index

### Properties

* [fromProto](src_core_object_watch_interface.WatchHandlerParams.html#fromProto)
* [obj](src_core_object_watch_interface.WatchHandlerParams.html#obj)
* [originalPath](src_core_object_watch_interface.WatchHandlerParams.html#originalPath)
* [parent](src_core_object_watch_interface.WatchHandlerParams.html#parent)
* [path](src_core_object_watch_interface.WatchHandlerParams.html#path)
* [root](src_core_object_watch_interface.WatchHandlerParams.html#root)
* [top](src_core_object_watch_interface.WatchHandlerParams.html#top)

## Properties

### fromProto

fromProto: boolean

Inherited from [RawWatchHandlerParams](src_core_object_watch_interface.RawWatchHandlerParams.html).[fromProto](src_core_object_watch_interface.RawWatchHandlerParams.html#fromProto)

* Defined in [src/core/object/watch/interface.ts:408](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L408)

True if the mutation has occurred on a prototype of the watched object

### obj

obj: object

Inherited from [RawWatchHandlerParams](src_core_object_watch_interface.RawWatchHandlerParams.html).[obj](src_core_object_watch_interface.RawWatchHandlerParams.html#obj)

* Defined in [src/core/object/watch/interface.ts:392](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L392)

Link to the object that is watched

### originalPath

originalPath: unknown[]

* Defined in [src/core/object/watch/interface.ts:444](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L444)

The original path to a property that was changed.

example
:   ```
    function pathModifier(path) {  
      return path.map((chunk) => chunk.replace(/^_/, ''));  
    }  
      
    const {proxy} = watch(a: 1, b: 2, _a: 1}, 'a', {pathModifier}, (mutations) => {  
      mutations.forEach(([value, oldValue, info]) => {  
        console.log(value, oldValue, info.path, info.originalPath);  
      });  
    });  
      
    // 2 1 ['a'], ['_a']  
    proxy._a = 2;
    ```

### Optional parent

parent?: [WatchHandlerParentParams](src_core_object_watch_interface.WatchHandlerParentParams.html)

* Defined in [src/core/object/watch/interface.ts:423](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L423)

Information about the parent mutation event

### path

path: unknown[]

Inherited from [RawWatchHandlerParams](src_core_object_watch_interface.RawWatchHandlerParams.html).[path](src_core_object_watch_interface.RawWatchHandlerParams.html#path)

* Defined in [src/core/object/watch/interface.ts:413](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L413)

Path to a property that was changed

### root

root: object

Inherited from [RawWatchHandlerParams](src_core_object_watch_interface.RawWatchHandlerParams.html).[root](src_core_object_watch_interface.RawWatchHandlerParams.html#root)

* Defined in [src/core/object/watch/interface.ts:397](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L397)

Link to the root object of watching

### Optional top

top?: object

Inherited from [RawWatchHandlerParams](src_core_object_watch_interface.RawWatchHandlerParams.html).[top](src_core_object_watch_interface.RawWatchHandlerParams.html#top)

* Defined in [src/core/object/watch/interface.ts:403](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L403)

Link to the top property of watching
(the first level property of the root)