# Module src/core/prelude/object/clone
## Index

### Functions

* [createParser](src_core_prelude_object_clone.html#createParser)
* [createSerializer](src_core_prelude_object_clone.html#createSerializer)

## Functions

### createParser

* createParser(base: unknown, valMap: [ValMap](src_core_prelude_object_clone_interface.html#ValMap), reviver?: false | [JSONCb](../interfaces/index.JSONCb.html)): [JSONCb](../interfaces/index.JSONCb.html)

* + Defined in [src/core/prelude/object/clone/index.ts:211](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/clone/index.ts#L211)

  Returns a function to parse object values from strings

  #### Parameters

  + ##### base: unknown

    base object
  + ##### valMap: [ValMap](src_core_prelude_object_clone_interface.html#ValMap)

    map that stores non-clone values
  + ##### Optional reviver: false | [JSONCb](../interfaces/index.JSONCb.html)

    additional reviewer

  #### Returns [JSONCb](../interfaces/index.JSONCb.html)

### createSerializer

* createSerializer(base: unknown, valMap: [ValMap](src_core_prelude_object_clone_interface.html#ValMap), replacer?: [JSONCb](../interfaces/index.JSONCb.html)): [JSONCb](../interfaces/index.JSONCb.html)

* + Defined in [src/core/prelude/object/clone/index.ts:178](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/clone/index.ts#L178)

  Returns a function to serialize object values into strings

  #### Parameters

  + ##### base: unknown

    base object
  + ##### valMap: [ValMap](src_core_prelude_object_clone_interface.html#ValMap)

    map to store non-clone values
  + ##### Optional replacer: [JSONCb](../interfaces/index.JSONCb.html)

    additional replacer

  #### Returns [JSONCb](../interfaces/index.JSONCb.html)