# Module src/core/object/watch/wrap/const
## Index

### Variables

* [clearMethods](src_core_object_watch_wrap_const.html#clearMethods)
* [deleteMethods](src_core_object_watch_wrap_const.html#deleteMethods)
* [iterators](src_core_object_watch_wrap_const.html#iterators)
* [structureWrappers](src_core_object_watch_wrap_const.html#structureWrappers)
* [weakMapMethods](src_core_object_watch_wrap_const.html#weakMapMethods)
* [weakSetMethods](src_core_object_watch_wrap_const.html#weakSetMethods)

## Variables

### Const clearMethods

clearMethods: { clear: (target: Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)> } = ...

* Defined in [src/core/object/watch/wrap/const.ts:116](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L116)

#### Type declaration

* ##### clear: (target: Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

  + - (target: Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)): [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
    - #### Parameters

      * ##### target: Set<unknown>
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)

      #### Returns [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

### Const deleteMethods

deleteMethods: { delete: (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)> } = ...

* Defined in [src/core/object/watch/wrap/const.ts:102](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L102)

#### Type declaration

* ##### delete: (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

  + - (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown): [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
    - #### Parameters

      * ##### target: Map<unknown, unknown> | Set<unknown>
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)
      * ##### key: unknown

      #### Returns [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

### Const iterators

iterators: { [iterator]: { type: string; value: (target: unknown[]) => IterableIterator<unknown> }; entries: { type: string; value: any }; keys: { type: string; value: any }; values: { type: string; value: any } } = ...

* Defined in [src/core/object/watch/wrap/const.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L14)

#### Type declaration

* ##### [iterator]: { type: string; value: (target: unknown[]) => IterableIterator<unknown> }

  + ##### type: string
  + ##### value: (target: unknown[]) => IterableIterator<unknown>

    - * (target: unknown[]): IterableIterator<unknown>
      * #### Parameters

        + ##### target: unknown[]

        #### Returns IterableIterator<unknown>
* ##### entries: { type: string; value: any }

  + ##### type: string
  + ##### value:function

    - value(target: unknown[], opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)): IterableIterator<[unknown, unknown]>
    - * Defined in [src/core/object/watch/wrap/const.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L42)

      #### Parameters

      * ##### target: unknown[]
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)

      #### Returns IterableIterator<[unknown, unknown]>
* ##### keys: { type: string; value: any }

  + ##### type: string
  + ##### value:function

    - value(target: unknown[], opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)): IterableIterator<unknown>
    - * Defined in [src/core/object/watch/wrap/const.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L17)

      #### Parameters

      * ##### target: unknown[]
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)

      #### Returns IterableIterator<unknown>
* ##### values: { type: string; value: any }

  + ##### type: string
  + ##### value:function

    - value(target: unknown[]): IterableIterator<unknown>
    - * Defined in [src/core/object/watch/wrap/const.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L72)

      #### Parameters

      * ##### target: unknown[]

      #### Returns IterableIterator<unknown>

### Const structureWrappers

structureWrappers: Pick<[StructureWrappers](src_core_object_watch_wrap_interface.html#StructureWrappers), keyof [StructureWrappers](src_core_object_watch_wrap_interface.html#StructureWrappers)> = ...

* Defined in [src/core/object/watch/wrap/const.ts:155](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L155)

### Const weakMapMethods

weakMapMethods: { delete: (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>; get: { type: string; value: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => unknown }; set: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown, value: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)> } = ...

* Defined in [src/core/object/watch/wrap/const.ts:126](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L126)

#### Type declaration

* ##### delete: (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

  + - (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown): [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
    - #### Parameters

      * ##### target: Map<unknown, unknown> | Set<unknown>
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)
      * ##### key: unknown

      #### Returns [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
* ##### get: { type: string; value: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => unknown }

  + ##### type: string
  + ##### value: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => unknown

    - * (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown): unknown
      * #### Parameters

        + ##### target: WeakMap<any, any>
        + ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)
        + ##### key: unknown

        #### Returns unknown
* ##### set: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown, value: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

  + - (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown, value: unknown): [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
    - #### Parameters

      * ##### target: WeakMap<any, any>
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)
      * ##### key: unknown
      * ##### value: unknown

      #### Returns [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

### Const weakSetMethods

weakSetMethods: { add: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), value: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>; delete: (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)> } = ...

* Defined in [src/core/object/watch/wrap/const.ts:143](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/wrap/const.ts#L143)

#### Type declaration

* ##### add: (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), value: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

  + - (target: WeakMap<any, any>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), value: unknown): [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
    - #### Parameters

      * ##### target: WeakMap<any, any>
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)
      * ##### value: unknown

      #### Returns [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
* ##### delete: (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown) => [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>

  + - (target: Map<unknown, unknown> | Set<unknown>, opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html), key: unknown): [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>
    - #### Parameters

      * ##### target: Map<unknown, unknown> | Set<unknown>
      * ##### opts: [WrapParams](../interfaces/src_core_object_watch_wrap_interface.WrapParams.html)
      * ##### key: unknown

      #### Returns [Nullable](index.html#Nullable)<[WrapResult](src_core_object_watch_wrap_interface.html#WrapResult)>