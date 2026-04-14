# Module src/core/url/convert
## Index

### References

* [FromQueryStringOptions](src_core_url_convert.html#FromQueryStringOptions)
* [ToQueryStringOptions](src_core_url_convert.html#ToQueryStringOptions)

### Functions

* [fromQueryString](src_core_url_convert.html#fromQueryString)
* [toQueryString](src_core_url_convert.html#toQueryString)

## References

### FromQueryStringOptions

Re-exports [FromQueryStringOptions](../interfaces/src_core_url_interface.FromQueryStringOptions.html)

### ToQueryStringOptions

Re-exports [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)

## Functions

### fromQueryString

* fromQueryString(query: string, decode?: boolean): [Dictionary](../interfaces/index.Dictionary.html)
* fromQueryString(query: string, opts: [FromQueryStringOptions](../interfaces/src_core_url_interface.FromQueryStringOptions.html)): [Dictionary](../interfaces/index.Dictionary.html)
* fromQueryString(query: string, opts: { convert: false } & [FromQueryStringOptions](../interfaces/src_core_url_interface.FromQueryStringOptions.html)): [Dictionary](../interfaces/index.Dictionary.html)<string | null>

* + Defined in [src/core/url/convert.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/url/convert.ts#L169)

  Creates a dictionary from the specified querystring and returns it

  example
  :   ```
      // {a: 1}  
      fromQueryString('?a=1');
      ```

  #### Parameters

  + ##### query: string
  + ##### Optional decode: boolean

  #### Returns [Dictionary](../interfaces/index.Dictionary.html)
* + Defined in [src/core/url/convert.ts:183](https://github.com/V4Fire/Core/blob/master/src/core/url/convert.ts#L183)

  Creates a dictionary from the specified querystring and returns it

  example
  :   ```
      // {a: [1, 2]}  
      fromQueryString('?a[]=1&a[]=2', {arraySyntax: true});
      ```

  #### Parameters

  + ##### query: string
  + ##### opts: [FromQueryStringOptions](../interfaces/src_core_url_interface.FromQueryStringOptions.html)

    additional options

  #### Returns [Dictionary](../interfaces/index.Dictionary.html)
* + Defined in [src/core/url/convert.ts:198](https://github.com/V4Fire/Core/blob/master/src/core/url/convert.ts#L198)

  Creates a dictionary from the specified querystring and returns it.
  This overload doesn't convert key values from a string.

  example
  :   ```
      // {a: '1'}  
      fromQueryString('?a=1', {convert: false});
      ```

  #### Parameters

  + ##### query: string
  + ##### opts: { convert: false } & [FromQueryStringOptions](../interfaces/src_core_url_interface.FromQueryStringOptions.html)

    additional options

  #### Returns [Dictionary](../interfaces/index.Dictionary.html)<string | null>

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