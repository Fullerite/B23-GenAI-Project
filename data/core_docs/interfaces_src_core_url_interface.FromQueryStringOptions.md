# Interface FromQueryStringOptions
### Hierarchy

* FromQueryStringOptions

## Index

### Properties

* [arraySyntax](src_core_url_interface.FromQueryStringOptions.html#arraySyntax)
* [convert](src_core_url_interface.FromQueryStringOptions.html#convert)
* [decode](src_core_url_interface.FromQueryStringOptions.html#decode)
* [separator](src_core_url_interface.FromQueryStringOptions.html#separator)

## Properties

### Optional arraySyntax

arraySyntax?: boolean

* Defined in [src/core/url/interface.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L101)

If true, then nested properties will be decoded by using `[]` syntax

default
:   `false`

example
:   ```
    // {foo: [1], bar: {bla: 2}}  
    fromQueryString('foo[]=1&bar[bla]=2', {arraySyntax: true});
    ```

### Optional convert

convert?: boolean

* Defined in [src/core/url/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L77)

If false, then all parsed values won't be converted from a string

default
:   `true`

example
:   ```
    // {foo: '1'}  
    fromQueryString('foo=1', {convert: false});
    ```

### Optional decode

decode?: boolean

* Defined in [src/core/url/interface.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L64)

If false, then the passed string won't be decoded by using `decodeURIComponent`

default
:   `true`

### Optional separator

separator?: string

* Defined in [src/core/url/interface.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/url/interface.ts#L88)

Separator for nested properties

example
:   ```
    // {foo: {bar: 1}}  
    fromQueryString('foo_bar=1', {separator: '_'});
    ```