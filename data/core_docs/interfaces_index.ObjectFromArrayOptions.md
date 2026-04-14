# Interface ObjectFromArrayOptions<T>
### Type parameters

* #### T = boolean

### Hierarchy

* ObjectFromArrayOptions

## Index

### Methods

* [key](index.ObjectFromArrayOptions.html#key)
* [keyConverter](index.ObjectFromArrayOptions.html#keyConverter)
* [value](index.ObjectFromArrayOptions.html#value)
* [valueConverter](index.ObjectFromArrayOptions.html#valueConverter)

## Methods

### Optional key

* key(el: unknown, i: number): PropertyKey
* key(el: unknown, i: number): DictionaryKey

* + Defined in [index.d.ts:690](https://github.com/V4Fire/Core/blob/master/index.d.ts#L690)

  Function that returns a key value

  #### Parameters

  + ##### el: unknown

    element value
  + ##### i: number

    element index

  #### Returns PropertyKey
* + Defined in dist/index.d.ts:632

  Function that returns a key value

  #### Parameters

  + ##### el: unknown

    element value
  + ##### i: number

    element index

  #### Returns DictionaryKey

### Optional keyConverter

* keyConverter(i: number, el: unknown): PropertyKey
* keyConverter(i: number, el: unknown): DictionaryKey

* + Defined in [index.d.ts:696](https://github.com/V4Fire/Core/blob/master/index.d.ts#L696)

  deprecated

  see
  :   [ObjectFromArrayOptions.key](index.ObjectFromArrayOptions.html#key)

  #### Parameters

  + ##### i: number
  + ##### el: unknown

  #### Returns PropertyKey
* + Defined in dist/index.d.ts:638

  deprecated

  see
  :   [ObjectFromArrayOptions.key](index.ObjectFromArrayOptions.html#key)

  #### Parameters

  + ##### i: number
  + ##### el: unknown

  #### Returns DictionaryKey

### Optional value

* value(el: unknown, i: number): T
* value(el: unknown, i: number): T

* + Defined in [index.d.ts:704](https://github.com/V4Fire/Core/blob/master/index.d.ts#L704)

  Function that returns an element value

  #### Parameters

  + ##### el: unknown

    element value
  + ##### i: number

    element index

  #### Returns T
* + Defined in dist/index.d.ts:646

  Function that returns an element value

  #### Parameters

  + ##### el: unknown

    element value
  + ##### i: number

    element index

  #### Returns T

### Optional valueConverter

* valueConverter(el: unknown, i: number): T
* valueConverter(el: unknown, i: number): T

* + Defined in [index.d.ts:710](https://github.com/V4Fire/Core/blob/master/index.d.ts#L710)

  deprecated

  see
  :   [ObjectFromArrayOptions.value](index.ObjectFromArrayOptions.html#value)

  #### Parameters

  + ##### el: unknown
  + ##### i: number

  #### Returns T
* + Defined in dist/index.d.ts:652

  deprecated

  see
  :   [ObjectFromArrayOptions.value](index.ObjectFromArrayOptions.html#value)

  #### Parameters

  + ##### el: unknown
  + ##### i: number

  #### Returns T