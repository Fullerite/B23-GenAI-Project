# Module src/core/prelude/object/helpers
## Index

### Functions

* [canExtendProto](src_core_prelude_object_helpers.html#canExtendProto)
* [getSameAs](src_core_prelude_object_helpers.html#getSameAs)
* [getType](src_core_prelude_object_helpers.html#getType)
* [isContainer](src_core_prelude_object_helpers.html#isContainer)

## Functions

### canExtendProto

* canExtendProto(value: unknown): boolean

* + Defined in [src/core/prelude/object/helpers.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/helpers.ts#L31)

  Returns true if the specified value has a prototype that can be extended

  #### Parameters

  + ##### value: unknown

  #### Returns boolean

### getSameAs

* getSameAs<T>(value: T): [Nullable](index.html#Nullable)<T>

* + Defined in [src/core/prelude/object/helpers.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/helpers.ts#L83)

  Returns a new instance of the specified value or null

  #### Type parameters

  + #### T

  #### Parameters

  + ##### value: T

  #### Returns [Nullable](index.html#Nullable)<T>

### getType

* getType(value: unknown): [GetTypeType](src_core_prelude_object_interface.html#GetTypeType)

* + Defined in [src/core/prelude/object/helpers.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/helpers.ts#L47)

  Returns a type of the specified value

  #### Parameters

  + ##### value: unknown

  #### Returns [GetTypeType](src_core_prelude_object_interface.html#GetTypeType)

### isContainer

* isContainer(value: unknown): boolean

* + Defined in [src/core/prelude/object/helpers.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/prelude/object/helpers.ts#L15)

  Returns true if the specified value is a container structure

  #### Parameters

  + ##### value: unknown

  #### Returns boolean