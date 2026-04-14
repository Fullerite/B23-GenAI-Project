# Class default
Class to create a set of HTTP headers

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_request_headers.default.html#constructor)

### Properties

* [[requestQuery]](src_core_request_headers.default.html#_requestQuery_)

### Methods

* [[iterator]](src_core_request_headers.default.html#_iterator_)
* [append](src_core_request_headers.default.html#append)
* [delete](src_core_request_headers.default.html#delete)
* [entries](src_core_request_headers.default.html#entries)
* [forEach](src_core_request_headers.default.html#forEach)
* [get](src_core_request_headers.default.html#get)
* [has](src_core_request_headers.default.html#has)
* [keys](src_core_request_headers.default.html#keys)
* [normalizeHeaderName](src_core_request_headers.default.html#normalizeHeaderName)
* [normalizeHeaderValue](src_core_request_headers.default.html#normalizeHeaderValue)
* [set](src_core_request_headers.default.html#set)
* [values](src_core_request_headers.default.html#values)

## Constructors

### constructor

* new default(headers?: [RawHeaders](../modules/src_core_request_headers_interface.html#RawHeaders), query?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): [default](src_core_request_headers.default.html)

* + Defined in [src/core/request/headers/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L34)

  #### Parameters

  + ##### Optional headers: [RawHeaders](../modules/src_core_request_headers_interface.html#RawHeaders)
  + ##### Optional query: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

  #### Returns [default](src_core_request_headers.default.html)

## Properties

### Optional [requestQuery]

[requestQuery]?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

* Defined in [src/core/request/headers/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L28)

Request query object (to interpolate values from headers)

## Methods

### [iterator]

* [iterator](): IterableIterator<[string, string]>

* + Defined in [src/core/request/headers/index.ts:94](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L94)

  Returns an iterator over headers.
  It produces tuples with headers' names and values.

  #### Returns IterableIterator<[string, string]>

### append

* append(name: string, value: [CanArray](../modules/index.html#CanArray)<string>): void

* + Defined in [src/core/request/headers/index.ts:150](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L150)

  Appends a new value into an existing header or adds the header if it does not already exist.
  To set multiple values for one header, provide its value as a list of values.

  #### Parameters

  + ##### name: string
  + ##### value: [CanArray](../modules/index.html#CanArray)<string>

  #### Returns void

### delete

* delete(name: string): void

* + Defined in [src/core/request/headers/index.ts:175](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L175)

  Deletes a header by the specified name

  #### Parameters

  + ##### name: string

  #### Returns void

### entries

* entries(): IterableIterator<[string, string]>

* + Defined in [src/core/request/headers/index.ts:210](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L210)

  Returns an iterator over headers.
  It produces tuples with headers' names and values.

  #### Returns IterableIterator<[string, string]>

### forEach

* forEach(cb: [HeadersForEachCb](../interfaces/src_core_request_headers_interface.HeadersForEachCb.html), thisArg?: any): void

* + Defined in [src/core/request/headers/index.ts:186](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L186)

  Iterates over the headers and invokes the given callback function at each header

  #### Parameters

  + ##### cb: [HeadersForEachCb](../interfaces/src_core_request_headers_interface.HeadersForEachCb.html)
  + ##### Optional thisArg: any

  #### Returns void

### get

* get(name: string): null | string

* + Defined in [src/core/request/headers/index.ts:102](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L102)

  Returns a header value by the specified name

  #### Parameters

  + ##### name: string

  #### Returns null | string

### has

* has(name: string): boolean

* + Defined in [src/core/request/headers/index.ts:110](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L110)

  Returns true if the structure contains a header by the specified name

  #### Parameters

  + ##### name: string

  #### Returns boolean

### keys

* keys(): IterableIterator<string>

* + Defined in [src/core/request/headers/index.ts:202](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L202)

  Returns an iterator over headers' names

  #### Returns IterableIterator<string>

### Protected normalizeHeaderName

* normalizeHeaderName(name: string): string

* + Defined in [src/core/request/headers/index.ts:218](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L218)

  Normalizes the specified header name

  #### Parameters

  + ##### name: string

  #### Returns string

### Protected normalizeHeaderValue

* normalizeHeaderValue(value: unknown): string

* + Defined in [src/core/request/headers/index.ts:226](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L226)

  Normalizes the specified header value

  #### Parameters

  + ##### value: unknown

  #### Returns string

### set

* set(name: string, value: [CanArray](../modules/index.html#CanArray)<string>): void

* + Defined in [src/core/request/headers/index.ts:121](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L121)

  Sets a new header value by the specified name.
  To set multiple values for one header, provide its value as a list of values.

  #### Parameters

  + ##### name: string
  + ##### value: [CanArray](../modules/index.html#CanArray)<string>

  #### Returns void

### values

* values(): IterableIterator<string>

* + Defined in [src/core/request/headers/index.ts:195](https://github.com/V4Fire/Core/blob/master/src/core/request/headers/index.ts#L195)

  Returns an iterator over headers' values

  #### Returns IterableIterator<string>