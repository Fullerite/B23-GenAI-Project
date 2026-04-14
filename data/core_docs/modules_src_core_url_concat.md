# Module src/core/url/concat
## Index

### Functions

* [concatURLs](src_core_url_concat.html#concatURLs)
* [concatUrls](src_core_url_concat.html#concatUrls)

## Functions

### concatURLs

* concatURLs(...urls: [Nullable](index.html#Nullable)<string>[]): string

* + Defined in [src/core/url/concat.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/url/concat.ts#L26)

  Concatenates the specified parts of URL-s with correctly arranging of slashes and returns a new string

  example
  :   ```
      // 'foo/baz/bar/bla'  
      concatURLs('foo/baz', '/bar', 'bla');  
        
      // 'http://foo.bar/bla'  
      concatURLs('http://foo.bar', 'bla');
      ```

  #### Parameters

  + ##### Rest ...urls: [Nullable](index.html#Nullable)<string>[]

  #### Returns string

### concatUrls

* concatUrls(...urls: [Nullable](index.html#Nullable)<string>[]): string

* + Defined in [src/core/url/concat.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/url/concat.ts#L69)

  deprecated

  see
  :   [concatURLs](src_core_url_concat.html#concatURLs)

  #### Parameters

  + ##### Rest ...urls: [Nullable](index.html#Nullable)<string>[]

  #### Returns string