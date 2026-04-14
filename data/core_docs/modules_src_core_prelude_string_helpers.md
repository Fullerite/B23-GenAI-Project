# Module src/core/prelude/string/helpers
## Index

### Functions

* [convertToSeparatedStr](src_core_prelude_string_helpers.html#convertToSeparatedStr)
* [createStaticTransformFunction](src_core_prelude_string_helpers.html#createStaticTransformFunction)
* [isCharUpper](src_core_prelude_string_helpers.html#isCharUpper)
* [toCamelize](src_core_prelude_string_helpers.html#toCamelize)
* [toDasherize](src_core_prelude_string_helpers.html#toDasherize)
* [toUnderscore](src_core_prelude_string_helpers.html#toUnderscore)

## Functions

### convertToSeparatedStr

* convertToSeparatedStr(str: string, separator: string, stable?: boolean): string

* + Defined in [src/core/prelude/string/helpers.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/prelude/string/helpers.ts#L88)

  Converts the specified string to a string that logically split by a separator

  #### Parameters

  + ##### str: string
  + ##### separator: string
  + ##### Optional stable: boolean

  #### Returns string

### createStaticTransformFunction

* createStaticTransformFunction(method: string): [AnyFunction](../interfaces/index.AnyFunction.html)

* + Defined in [src/core/prelude/string/helpers.ts:140](https://github.com/V4Fire/Core/blob/master/src/core/prelude/string/helpers.ts#L140)

  Factory to create static string transform methods

  #### Parameters

  + ##### method: string

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)

### isCharUpper

* isCharUpper(char: string): boolean

* + Defined in [src/core/prelude/string/helpers.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/prelude/string/helpers.ts#L13)

  Returns true, if the specified character is declared in upper case

  #### Parameters

  + ##### char: string

  #### Returns boolean

### toCamelize

* toCamelize(str: string, start: [CanUndef](index.html#CanUndef)<string>, end: [CanUndef](index.html#CanUndef)<string>, middle: [CanUndef](index.html#CanUndef)<string>): string

* + Defined in [src/core/prelude/string/helpers.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/prelude/string/helpers.ts#L47)

  Transforms a string to a camelize style

  #### Parameters

  + ##### str: string
  + ##### start: [CanUndef](index.html#CanUndef)<string>
  + ##### end: [CanUndef](index.html#CanUndef)<string>
  + ##### middle: [CanUndef](index.html#CanUndef)<string>

  #### Returns string

### toDasherize

* toDasherize(str: string, start: [CanUndef](index.html#CanUndef)<string>, end: [CanUndef](index.html#CanUndef)<string>, middle: [CanUndef](index.html#CanUndef)<string>): string

* + Defined in [src/core/prelude/string/helpers.ts:68](https://github.com/V4Fire/Core/blob/master/src/core/prelude/string/helpers.ts#L68)

  Transforms a string to a dasherize style

  #### Parameters

  + ##### str: string
  + ##### start: [CanUndef](index.html#CanUndef)<string>
  + ##### end: [CanUndef](index.html#CanUndef)<string>
  + ##### middle: [CanUndef](index.html#CanUndef)<string>

  #### Returns string

### toUnderscore

* toUnderscore(str: string, start: [CanUndef](index.html#CanUndef)<string>, end: [CanUndef](index.html#CanUndef)<string>, middle: [CanUndef](index.html#CanUndef)<string>): string

* + Defined in [src/core/prelude/string/helpers.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/prelude/string/helpers.ts#L26)

  Transforms a string to an underscore style

  #### Parameters

  + ##### str: string
  + ##### start: [CanUndef](index.html#CanUndef)<string>
  + ##### end: [CanUndef](index.html#CanUndef)<string>
  + ##### middle: [CanUndef](index.html#CanUndef)<string>

  #### Returns string