# Module src/core/request/const
## Index

### Variables

* [cache](src_core_request_const.html#cache)
* [caches](src_core_request_const.html#caches)
* [defaultRequestOpts](src_core_request_const.html#defaultRequestOpts)
* [globalOpts](src_core_request_const.html#globalOpts)
* [isAbsoluteURL](src_core_request_const.html#isAbsoluteURL)
* [methodsWithoutBody](src_core_request_const.html#methodsWithoutBody)
* [pendingCache](src_core_request_const.html#pendingCache)
* [storage](src_core_request_const.html#storage)

## Variables

### Const cache

cache: Record<Exclude<[CacheStrategy](src_core_request_interface.html#CacheStrategy), [default](../interfaces/src_core_cache_interface.default.html) | Promise<[default](../interfaces/src_core_cache_interface.default.html)>>, [default](../interfaces/src_core_cache_interface.default.html)> = ...

* Defined in [src/core/request/const.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L47)

### Const caches

caches: Set<[default](../interfaces/src_core_cache_interface.default.html)<unknown, string>> = ...

* Defined in [src/core/request/const.ts:44](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L44)

### Const defaultRequestOpts

defaultRequestOpts: { cacheMethods: [RequestMethod](src_core_request_interface.html#RequestMethod)[]; cacheStrategy: [CacheStrategy](src_core_request_interface.html#CacheStrategy); engine: [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html); headers: [RawHeaders](src_core_request_headers_interface.html#RawHeaders); meta: [Dictionary](../interfaces/index.Dictionary.html)<unknown>; method: [RequestMethod](src_core_request_interface.html#RequestMethod); offlineCacheTTL: number; query: [RequestQuery](src_core_request_interface.html#RequestQuery); querySerializer: { (data: unknown, encode?: boolean): string; (data: unknown, opts: [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)): string } } = ...

* Defined in [src/core/request/const.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L70)

#### Type declaration

* ##### cacheMethods: [RequestMethod](src_core_request_interface.html#RequestMethod)[]
* ##### cacheStrategy: [CacheStrategy](src_core_request_interface.html#CacheStrategy)
* ##### engine: [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html)
* ##### headers: [RawHeaders](src_core_request_headers_interface.html#RawHeaders)
* ##### meta: [Dictionary](../interfaces/index.Dictionary.html)<unknown>
* ##### method: [RequestMethod](src_core_request_interface.html#RequestMethod)
* ##### offlineCacheTTL: number
* ##### query: [RequestQuery](src_core_request_interface.html#RequestQuery)
* ##### querySerializer: { (data: unknown, encode?: boolean): string; (data: unknown, opts: [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)): string }

  + - (data: unknown, encode?: boolean): string
    - (data: unknown, opts: [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)): string
    - Creates a querystring from the specified data and returns it

      example
      :   ```
          // '?a=1'  
          toQueryString({a: 1});
          ```

      #### Parameters

      * ##### data: unknown
      * ##### Optional encode: boolean

      #### Returns string
    - Creates a querystring from the specified data and returns it

      example
      :   ```
          // '?a[]=1&a[]=2'  
          toQueryString({a: [1, 2]}, {arraySyntax: true});
          ```

      #### Parameters

      * ##### data: unknown
      * ##### opts: [ToQueryStringOptions](../interfaces/src_core_url_interface.ToQueryStringOptions.html)

        additional options

      #### Returns string

### Const globalOpts

globalOpts: [GlobalOptions](../interfaces/src_core_request_interface.GlobalOptions.html) = ...

* Defined in [src/core/request/const.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L53)

### Const isAbsoluteURL

isAbsoluteURL: RegExp = ...

* Defined in [src/core/request/const.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L41)

### Const methodsWithoutBody

methodsWithoutBody: Pick<{ GET: boolean; HEAD: boolean }, "GET" | "HEAD"> = ...

* Defined in [src/core/request/const.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L65)

### Const pendingCache

pendingCache: [default](../classes/src_core_cache_simple.default.html)<[RequestResponse](src_core_request_interface.html#RequestResponse)<unknown>, string> = ...

* Defined in [src/core/request/const.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L45)

### storage

storage: [CanUndef](index.html#CanUndef)<Promise<[AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html)>>

* Defined in [src/core/request/const.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/request/const.ts#L33)