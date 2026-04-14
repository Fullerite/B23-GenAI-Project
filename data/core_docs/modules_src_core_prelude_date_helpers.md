# Module src/core/prelude/date/helpers
## Index

### Functions

* [createDateModifier](src_core_prelude_date_helpers.html#createDateModifier)
* [createStaticDateComparator](src_core_prelude_date_helpers.html#createStaticDateComparator)
* [createStaticDateFormatter](src_core_prelude_date_helpers.html#createStaticDateFormatter)
* [createStaticDateModifier](src_core_prelude_date_helpers.html#createStaticDateModifier)

## Functions

### createDateModifier

* createDateModifier(mod?: (val: number, base: number) => number): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/date/helpers.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/helpers.ts#L13)

  Factory to create functions to modify date values

  #### Parameters

  + ##### mod: (val: number, base: number) => number = ...

    - * (val: number, base: number): number
      * #### Parameters

        + ##### val: number
        + ##### base: number

        #### Returns number

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createStaticDateComparator

* createStaticDateComparator(method: string): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/date/helpers.ts:129](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/helpers.ts#L129)

  Factory to create static functions to compare date values

  #### Parameters

  + ##### method: string

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createStaticDateFormatter

* createStaticDateFormatter(method: string): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/date/helpers.ts:152](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/helpers.ts#L152)

  Factory to create static functions to format date values

  #### Parameters

  + ##### method: string

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### createStaticDateModifier

* createStaticDateModifier(method: string): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/date/helpers.ts:113](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/helpers.ts#L113)

  Factory to create static functions to modify date values

  #### Parameters

  + ##### method: string

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)