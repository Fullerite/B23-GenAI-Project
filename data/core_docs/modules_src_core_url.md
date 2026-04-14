# Module src/core/url
[# core/url](#coreurl)

This module provides a bunch of functions to work with URL strings, such as parsing/serializing, concatenating groups of URLs to one, etc.

[## concatURLs](#concaturls)

Concatenates the specified parts of URL-s with correctly arranging of slashes and returns a new string.

```
import { concatURLs } from 'core/url';  
concatURLs('foo/baz', '/bar', 'bla') === 'foo/baz/bar/bla';
```

[## Parsing/Serialization](#parsingserialization)

```
import { fromQueryString, toQueryString } from 'core/url';  
  
const data = {  
  foo: 1,  
  bar: true,  
  baz: [1, 2, 3],  
  ban: {a: 2}  
};  
  
toQueryString(data) === 'ban_a=2&bar=true&baz=1&baz=2&baz=3&foo=1';  
  
// {foo: 1, bar: true, baz: [1, 2, 3], ban: {a: 2}}  
fromQueryString(toQueryString(data), {separator: '_'});
```

[### fromQueryString](#fromquerystring)

Creates a querystring from the specified data and returns it. The method can take additional options:

```
interface FromQueryStringOptions {  
  /**  
   * If false, then the passed string won't be decoded by using `decodeURIComponent`  
   * @default `true`  
   */  
  decode?: boolean;  
  
  /**  
   * If false, then all parsed values won't be converted from a string  
   *  
   * @default `true`  
   *  
   * @example  
   * ```js  
   * // {foo: '1'}  
   * fromQueryString('foo=1', {convert: false});  
   * ```  
   */  
  convert?: boolean;  
  
  /**  
   * Separator for nested properties  
   *  
   * @example  
   * ```js  
   * // {foo: {bar: 1}}  
   * fromQueryString('foo_bar=1', {separator: '_'});  
   * ```  
   */  
  separator?: string;  
  
  /**  
   * If true, then nested properties will be decoded by using `[]` syntax  
   *  
   * @default `false`  
   *  
   * @example  
   * ```js  
   * // {foo: [1], bar: {bla: 2}}  
   * fromQueryString('foo[]=1&bar[bla]=2', {arraySyntax: true});  
   * ```  
   */  
  arraySyntax?: boolean;  
}
```

[### toQueryString](#toquerystring)

Creates a querystring from the specified data and returns it. The method can take additional options:

```
interface ToQueryStringOptions {  
  /**  
   * If false, then the result string won't be encoded by using `encodeURIComponent`  
   * @default `true`  
   */  
  encode?: boolean;  
  
  /**  
   * Separator for nested properties  
   *  
   * @default `'_'`  
   *  
   * @example  
   * ```js  
   * // foo.bar=1  
   * toQueryString({foo: {bar: 1}}, {separator: '.'});  
   * ```  
   */  
  separator?: string;  
  
  /**  
   * If true, then nested properties will be encoded by using `[]` syntax  
   *  
   * @default `false`  
   *  
   * @example  
   * ```js  
   * // foo[]=1&bar[bla]=2  
   * toQueryString({foo: [1], bar: {bla: 2}}, {arraySyntax: true});  
   * ```  
   */  
  arraySyntax?: boolean;  
  
  /**  
   * Filters values that shouldn't be serialized.  
   * By default, the function skip all values with null-s and empty strings.  
   *  
   * @param value  
   * @param key - property key  
   * @param path - accumulated property path `({a: {b: 1}} => 'a_b')`  
   *  
   * @example  
   * ```js  
   * // foo=1  
   * toQueryString({foo: 1, bar: {bla: 2}}, {paramsFilter: (el, key) => key !== 'bla'});  
   * ```  
   */  
  paramsFilter?(value: unknown, key: string, path?: string): unknown;  
}
```

## Index

### References

* [FromQueryStringOptions](src_core_url.html#FromQueryStringOptions)
* [ToQueryStringOptions](src_core_url.html#ToQueryStringOptions)
* [concatURLs](src_core_url.html#concatURLs)
* [concatUrls](src_core_url.html#concatUrls)
* [defaultToQueryStringParamsFilter](src_core_url.html#defaultToQueryStringParamsFilter)
* [endSlashesRgxp](src_core_url.html#endSlashesRgxp)
* [fromQueryString](src_core_url.html#fromQueryString)
* [isAbsURL](src_core_url.html#isAbsURL)
* [isStrictAbsURL](src_core_url.html#isStrictAbsURL)
* [startSlashesRgxp](src_core_url.html#startSlashesRgxp)

### Functions

* [toQueryString](src_core_url.html#toQueryString)

## References

### FromQueryStringOptions

Re-exports [FromQueryStringOptions](../interfaces/src_core_url_interface.FromQueryStringOptions.html)

### ToQueryStringOptions

Re-exports [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)

### concatURLs

Re-exports [concatURLs](src_core_url_concat.html#concatURLs)

### concatUrls

Re-exports [concatUrls](src_core_url_concat.html#concatUrls)

### defaultToQueryStringParamsFilter

Re-exports [defaultToQueryStringParamsFilter](src_core_url_const.html#defaultToQueryStringParamsFilter)

### endSlashesRgxp

Re-exports [endSlashesRgxp](src_core_url_const.html#endSlashesRgxp)

### fromQueryString

Re-exports [fromQueryString](src_core_url_convert.html#fromQueryString)

### isAbsURL

Re-exports [isAbsURL](src_core_url_const.html#isAbsURL)

### isStrictAbsURL

Re-exports [isStrictAbsURL](src_core_url_const.html#isStrictAbsURL)

### startSlashesRgxp

Re-exports [startSlashesRgxp](src_core_url_const.html#startSlashesRgxp)

## Functions

### toQueryString

* toQueryString(data: unknown, encode?: boolean): string
* toQueryString(data: unknown, opts: [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)): string

* + Defined in [src/core/url/convert.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/url/convert.ts#L28)

  Creates a querystring from the specified data and returns it

  example
  :   ```
      // '?a=1'  
      toQueryString({a: 1});
      ```

  #### Parameters

  + ##### data: unknown
  + ##### Optional encode: boolean

  #### Returns string
* + Defined in [src/core/url/convert.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/url/convert.ts#L42)

  Creates a querystring from the specified data and returns it

  example
  :   ```
      // '?a[]=1&a[]=2'  
      toQueryString({a: [1, 2]}, {arraySyntax: true});
      ```

  #### Parameters

  + ##### data: unknown
  + ##### opts: [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)

    additional options

  #### Returns string