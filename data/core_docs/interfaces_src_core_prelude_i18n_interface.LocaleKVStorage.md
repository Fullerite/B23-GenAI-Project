# Interface LocaleKVStorage
### Hierarchy

* LocaleKVStorage

## Index

### Properties

* [get](src_core_prelude_i18n_interface.LocaleKVStorage.html#get)
* [set](src_core_prelude_i18n_interface.LocaleKVStorage.html#set)

## Properties

### get

get: <T>(key: string, ...args: unknown[]) => [CanUndef](../modules/index.html#CanUndef)<T>

* Defined in [src/core/prelude/i18n/interface.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/interface.ts#L24)

#### Type declaration

* + <T>(key: string, ...args: unknown[]): [CanUndef](../modules/index.html#CanUndef)<T>
  + Returns a value from the storage by the specified key.

    The returning value automatically parses by using `Object.parse` from a string to equivalent JS value, i.e.,
    `'1'` will be parsed to `1`, `'true'` to `true`, `'2021-07-09T08:15:57.753Z'` to `Date`, etc.

    Notice, the method can take a list of additional parameters provided to the used storage' engine.

    #### Type parameters

    - #### T = unknown

    #### Parameters

    - ##### key: string
    - ##### Rest ...args: unknown[]

    #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### Optional set

set?: (key: string, value: unknown, ...args: unknown[]) => void

* Defined in [src/core/prelude/i18n/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/interface.ts#L29)

#### Type declaration

* + (key: string, value: unknown, ...args: unknown[]): void
  + Saves a value to the storage by the specified key.

    The value to parse automatically serializes to a string by using `Object.trySerialize`, i.e.,
    arrays and dictionaries will be serialized to JSON, etc.

    Notice, the method can take a list of additional parameters provided to the used storage' engine.

    #### Parameters

    - ##### key: string
    - ##### value: unknown
    - ##### Rest ...args: unknown[]

    #### Returns void