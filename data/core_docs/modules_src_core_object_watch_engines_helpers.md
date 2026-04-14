# Module src/core/object/watch/engines/helpers
## Index

### Functions

* [getOrCreateLabelValueByHandlers](src_core_object_watch_engines_helpers.html#getOrCreateLabelValueByHandlers)
* [getProxyType](src_core_object_watch_engines_helpers.html#getProxyType)
* [getProxyValue](src_core_object_watch_engines_helpers.html#getProxyValue)
* [isProxy](src_core_object_watch_engines_helpers.html#isProxy)
* [unwrap](src_core_object_watch_engines_helpers.html#unwrap)

## Functions

### getOrCreateLabelValueByHandlers

* getOrCreateLabelValueByHandlers<T>(obj: object, label: string | symbol, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)): [CanUndef](index.html#CanUndef)<T>
* getOrCreateLabelValueByHandlers<T>(obj: object, label: string | symbol, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), def: unknown): T

* + Defined in [src/core/object/watch/engines/helpers.ts:105](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/helpers.ts#L105)

  Returns a value from an object by the specified label and handlers

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: object
  + ##### label: string | symbol
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

  #### Returns [CanUndef](index.html#CanUndef)<T>
* + Defined in [src/core/object/watch/engines/helpers.ts:119](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/helpers.ts#L119)

  Returns a value from an object by the specified label and handlers

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: object
  + ##### label: string | symbol
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)
  + ##### def: unknown

    default value (can be declared as a function that will be invoked)

  #### Returns T

### getProxyType

* getProxyType(obj: unknown): [Nullable](index.html#Nullable)<string>

* + Defined in [src/core/object/watch/engines/helpers.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/helpers.ts#L39)

  Returns a type of data to watch or false

  #### Parameters

  + ##### obj: unknown

  #### Returns [Nullable](index.html#Nullable)<string>

### getProxyValue

* getProxyValue(rawValue: unknown, key: unknown, path: [CanUndef](index.html#CanUndef)<unknown[]>, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), root: object, top?: object, opts?: [InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)): unknown

* + Defined in [src/core/object/watch/engines/helpers.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/helpers.ts#L70)

  Returns a value to the proxy from the specified raw value

  #### Parameters

  + ##### rawValue: unknown
  + ##### key: unknown

    property key for a value
  + ##### path: [CanUndef](index.html#CanUndef)<unknown[]>

    base path to object properties: it is provided to a watch handler with parameters
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

    set of registered handlers
  + ##### root: object

    link to the root object of watching
  + ##### Optional top: object
  + ##### Optional opts: [InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)

  #### Returns unknown

### isProxy

* isProxy(value: unknown): value is object

* + Defined in [src/core/object/watch/engines/helpers.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/helpers.ts#L18)

  Returns true if the specified value is a watch proxy

  #### Parameters

  + ##### value: unknown

  #### Returns value is object

### unwrap

* unwrap(value: unknown): [CanUndef](index.html#CanUndef)<object>

* + Defined in [src/core/object/watch/engines/helpers.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/engines/helpers.ts#L30)

  Unwraps the specified value to watch and returns the raw object

  #### Parameters

  + ##### value: unknown

  #### Returns [CanUndef](index.html#CanUndef)<object>