# Module src/core/prelude/number/helpers
## Index

### Functions

* [createMsFunction](src_core_prelude_number_helpers.html#createMsFunction)
* [createRoundingFunction](src_core_prelude_number_helpers.html#createRoundingFunction)
* [createStaticMsFunction](src_core_prelude_number_helpers.html#createStaticMsFunction)
* [createStaticRoundingFunction](src_core_prelude_number_helpers.html#createStaticRoundingFunction)
* [createStringTypeGetter](src_core_prelude_number_helpers.html#createStringTypeGetter)
* [repeatString](src_core_prelude_number_helpers.html#repeatString)

## Functions

### createMsFunction

* createMsFunction(offset: number): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/number/helpers.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/helpers.ts#L64)

  Factory for functions that converts milliseconds by the specified offset

  #### Parameters

  + ##### offset: number

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createRoundingFunction

* createRoundingFunction(method: [AnyFunction](../interfaces/index.AnyFunction.html)<any[], any>): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/number/helpers.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/helpers.ts#L13)

  Factory to create rounding methods

  #### Parameters

  + ##### method: [AnyFunction](../interfaces/index.AnyFunction.html)<any[], any>

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createStaticMsFunction

* createStaticMsFunction(offset: number): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/number/helpers.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/helpers.ts#L77)

  Factory for static functions that converts milliseconds by the specified offset

  #### Parameters

  + ##### offset: number

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createStaticRoundingFunction

* createStaticRoundingFunction(method: string): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/number/helpers.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/helpers.ts#L37)

  Factory to create static rounding methods

  #### Parameters

  + ##### method: string

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createStringTypeGetter

* createStringTypeGetter(type: string): PropertyDescriptor

* + Defined in [src/core/prelude/number/helpers.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/helpers.ts#L52)

  Returns a descriptor for a getter that returns a string with attaching the specified type

  #### Parameters

  + ##### type: string

  #### Returns PropertyDescriptor

### repeatString

* repeatString(str: string, num: number): string

* + Defined in [src/core/prelude/number/helpers.ts:87](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/helpers.ts#L87)

  Repeats a string with the specified number of repetitions and returns a new string

  #### Parameters

  + ##### str: string
  + ##### num: number

  #### Returns string