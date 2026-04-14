# Interface ToQueryStringOptions
### Hierarchy

* ToQueryStringOptions

## Index

### Properties

* [arraySyntax](src_core_url_interface.ToQueryStringOptions.html#arraySyntax)
* [encode](src_core_url_interface.ToQueryStringOptions.html#encode)
* [separator](src_core_url_interface.ToQueryStringOptions.html#separator)

### Methods

* [paramsFilter](src_core_url_interface.ToQueryStringOptions.html#paramsFilter)

## Properties

### Optional arraySyntax

arraySyntax?: boolean

* Defined in [src/core/url/interface.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L40)

If true, then nested properties will be encoded by using `[]` syntax

default
:   `false`

example
:   ```
    // foo[]=1&bar[bla]=2  
    toQueryString({foo: [1], bar: {bla: 2}}, {arraySyntax: true});
    ```

### Optional encode

encode?: boolean

* Defined in [src/core/url/interface.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L14)

If false, then the result string won't be encoded by using `encodeURIComponent`

default
:   `true`

### Optional separator

separator?: string

* Defined in [src/core/url/interface.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L27)

Separator for nested properties

default
:   `'_'`

example
:   ```
    // foo.bar=1  
    toQueryString({foo: {bar: 1}}, {separator: '.'});
    ```

## Methods

### Optional paramsFilter

* paramsFilter(value: unknown, key: string, path?: string): unknown

* + Defined in [src/core/url/interface.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L56)

  Filters values that shouldn't be serialized.
  By default, the function skip all values with null-s and empty strings.

  example
  :   ```
      // foo=1  
      toQueryString({foo: 1, bar: {bla: 2}}, {paramsFilter: (el, key) => key !== 'bla'});
      ```

  #### Parameters

  + ##### value: unknown
  + ##### key: string

    property key
  + ##### Optional path: string

    accumulated property path `({a: {b: 1}} => 'a_b')`

  #### Returns unknown