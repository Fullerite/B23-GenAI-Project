# Module src/core/prelude/object/compare
## Index

### Functions

* [createSerializer](src_core_prelude_object_compare.html#createSerializer)

## Functions

### createSerializer

* createSerializer(a: unknown, b: unknown, funcMap: WeakMap<Function, string>): [JSONCb](../interfaces/index.JSONCb.html)

* + Defined in [src/core/prelude/object/compare/index.ts:142](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/compare/index.ts#L142)

  Returns a function to serialize object values into strings

  #### Parameters

  + ##### a: unknown

    first object to serialize
  + ##### b: unknown

    second object to serialize
  + ##### funcMap: WeakMap<Function, string>

    map to store functions

  #### Returns [JSONCb](../interfaces/index.JSONCb.html)