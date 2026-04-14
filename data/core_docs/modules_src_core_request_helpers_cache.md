# Module src/core/request/helpers/cache
## Index

### Functions

* [dropCache](src_core_request_helpers_cache.html#dropCache)
* [getRequestKey](src_core_request_helpers_cache.html#getRequestKey)

## Functions

### dropCache

* dropCache(): void

* + Defined in [src/core/request/helpers/cache.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/request/helpers/cache.ts#L17)

  Truncates all static cache storage-s

  #### Returns void

### getRequestKey

* getRequestKey<T>(url: string, params?: [NormalizedCreateRequestOptions](src_core_request_interface.html#NormalizedCreateRequestOptions)<T>): string

* + Defined in [src/core/request/helpers/cache.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/request/helpers/cache.ts#L31)

  Generates a string cache key for the specified parameters and returns it

  #### Type parameters

  + #### T

  #### Parameters

  + ##### url: string

    request url
  + ##### Optional params: [NormalizedCreateRequestOptions](src_core_request_interface.html#NormalizedCreateRequestOptions)<T>

  #### Returns string