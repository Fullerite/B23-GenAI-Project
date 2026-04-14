# Class default<D>
Class to work with server response data

### Type parameters

* #### D: [Nullable](../modules/index.html#Nullable)<string | [JSONLikeValue](../modules/src_core_request_response_interface.html#JSONLikeValue) | ArrayBuffer | Blob | Document | unknown> = unknown

  response data type

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_request_response.default.html#constructor)

### Properties

* [body](src_core_request_response.default.html#body)
* [clone](src_core_request_response.default.html#clone)
* [decoders](src_core_request_response.default.html#decoders)
* [emitter](src_core_request_response.default.html#emitter)
* [headers](src_core_request_response.default.html#headers)
* [important](src_core_request_response.default.html#important)
* [jsonReviver](src_core_request_response.default.html#jsonReviver)
* [ok](src_core_request_response.default.html#ok)
* [okStatuses](src_core_request_response.default.html#okStatuses)
* [parent](src_core_request_response.default.html#parent)
* [redirected](src_core_request_response.default.html#redirected)
* [sourceResponseType](src_core_request_response.default.html#sourceResponseType)
* [status](src_core_request_response.default.html#status)
* [statusText](src_core_request_response.default.html#statusText)
* [streamDecoders](src_core_request_response.default.html#streamDecoders)
* [type](src_core_request_response.default.html#type)
* [url](src_core_request_response.default.html#url)

### Accessors

* [bodyUsed](src_core_request_response.default.html#bodyUsed)
* [responseType](src_core_request_response.default.html#responseType)
* [streamUsed](src_core_request_response.default.html#streamUsed)

### Methods

* [[asyncIterator]](src_core_request_response.default.html#_asyncIterator_)
* [applyDecoders](src_core_request_response.default.html#applyDecoders)
* [applyStreamDecoders](src_core_request_response.default.html#applyStreamDecoders)
* [arrayBuffer](src_core_request_response.default.html#arrayBuffer)
* [blob](src_core_request_response.default.html#blob)
* [decode](src_core_request_response.default.html#decode)
* [decodeStream](src_core_request_response.default.html#decodeStream)
* [decodeToBlob](src_core_request_response.default.html#decodeToBlob)
* [decodeToString](src_core_request_response.default.html#decodeToString)
* [document](src_core_request_response.default.html#document)
* [formData](src_core_request_response.default.html#formData)
* [getHeader](src_core_request_response.default.html#getHeader)
* [json](src_core_request_response.default.html#json)
* [jsonStream](src_core_request_response.default.html#jsonStream)
* [readBody](src_core_request_response.default.html#readBody)
* [stream](src_core_request_response.default.html#stream)
* [text](src_core_request_response.default.html#text)
* [textStream](src_core_request_response.default.html#textStream)

## Constructors

### constructor

* new default<D>(body?: [ResponseTypeValueP](../modules/src_core_request_response_interface.html#ResponseTypeValueP), opts?: [ResponseOptions](../interfaces/src_core_request_response_interface.ResponseOptions.html)): [default](src_core_request_response.default.html)<D>

* + Defined in [src/core/request/response/index.ts:207](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L207)

  #### Type parameters

  + #### D: unknown = unknown

  #### Parameters

  + ##### Optional body: [ResponseTypeValueP](../modules/src_core_request_response_interface.html#ResponseTypeValueP)
  + ##### Optional opts: [ResponseOptions](../interfaces/src_core_request_response_interface.ResponseOptions.html)

  #### Returns [default](src_core_request_response.default.html)<D>

## Properties

### Readonly body

body: [ResponseTypeValueP](../modules/src_core_request_response_interface.html#ResponseTypeValueP)

* Defined in [src/core/request/response/index.ts:163](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L163)

Response body value

### Readonly clone

clone: () => [default](src_core_request_response.default.html)<D>

* Defined in [src/core/request/response/index.ts:201](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L201)

#### Type declaration

* + (): [default](src_core_request_response.default.html)<D>
  + Creates a clone of a response object, identical in every way, but stored in a different variable

    #### Returns [default](src_core_request_response.default.html)<D>

### Readonly decoders

decoders: [WrappedDecoder](../interfaces/src_core_request_interface.WrappedDecoder.html)<unknown, unknown>[]

* Defined in [src/core/request/response/index.ts:147](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L147)

List of response decoders

### Readonly emitter

emitter: EventEmitter2 = ...

* Defined in [src/core/request/response/index.ts:196](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L196)

Event emitter to broadcast response events

### Readonly headers

headers: Readonly<[default](src_core_request_headers.default.html)>

* Defined in [src/core/request/response/index.ts:142](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L142)

Set of response headers

### Optional Readonly important

important?: boolean

* Defined in [src/core/request/response/index.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L96)

A meta flag that indicates that the request is important: is usually used with decoders to indicate that
the request needs to be executed as soon as possible

### Optional Readonly jsonReviver

jsonReviver?: [JSONCb](../interfaces/index.JSONCb.html)

* Defined in [src/core/request/response/index.ts:158](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L158)

Reviver function for `JSON.parse`

default
:   `convertIfDate`

### Readonly ok

ok: boolean

* Defined in [src/core/request/response/index.ts:131](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L131)

True if the response status matches with a successful status codes
(by default it should match range from 200 to 299)

### Readonly okStatuses

okStatuses: [OkStatuses](../modules/src_core_request_interface.html#OkStatuses)

* Defined in [src/core/request/response/index.ts:137](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L137)

A list of status codes (or a single code) that match successful operation.
Also, you can pass a range of codes.

### Optional Readonly parent

parent?: [default](src_core_promise_abortable.default.html)<unknown>

* Defined in [src/core/request/response/index.ts:90](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L90)

Parent operation promise

### Readonly redirected

redirected: boolean

* Defined in [src/core/request/response/index.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L79)

True if the response was obtained through a redirect

### Optional Readonly sourceResponseType

sourceResponseType?: [ResponseType](../modules/src_core_request_response_interface.html#ResponseType)

* Defined in [src/core/request/response/index.ts:115](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L115)

Original type of the response data

### Readonly status

status: number

* Defined in [src/core/request/response/index.ts:120](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L120)

Response status code

### Readonly statusText

statusText: string

* Defined in [src/core/request/response/index.ts:125](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L125)

Response status text

### Readonly streamDecoders

streamDecoders: [WrappedStreamDecoder](../interfaces/src_core_request_interface.WrappedStreamDecoder.html)<unknown, unknown>[]

* Defined in [src/core/request/response/index.ts:152](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L152)

List of response decoders to apply for chunks when you are parsing response in a stream form

### Readonly type

type: [ResponseModeType](../modules/src_core_request_response_interface.html#ResponseModeType)

* Defined in [src/core/request/response/index.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L85)

Mode type of the response

see
:   <https://developer.mozilla.org/en-US/docs/Web/API/Response/type>

### Readonly url

url: string

* Defined in [src/core/request/response/index.ts:74](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L74)

The resolved request URL (after resolving redirects, etc.)

## Accessors

### bodyUsed

* get bodyUsed(): boolean
* set bodyUsed(value: boolean): void

* + Defined in [src/core/request/response/index.ts:168](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L168)

  True, if the response body is already read

  #### Returns boolean
* + Defined in [src/core/request/response/index.ts:175](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L175)

  Sets a new status of `bodyUsed`

  #### Parameters

  + ##### value: boolean

  #### Returns void

### responseType

* get responseType(): [CanUndef](../modules/index.html#CanUndef)<[ResponseType](../modules/src_core_request_response_interface.html#ResponseType)>
* set responseType(value: [CanUndef](../modules/index.html#CanUndef)<[ResponseType](../modules/src_core_request_response_interface.html#ResponseType)>): void

* + Defined in [src/core/request/response/index.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L101)

  Type of the response data

  #### Returns [CanUndef](../modules/index.html#CanUndef)<[ResponseType](../modules/src_core_request_response_interface.html#ResponseType)>
* + Defined in [src/core/request/response/index.ts:108](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L108)

  Sets a new type of the response data

  #### Parameters

  + ##### value: [CanUndef](../modules/index.html#CanUndef)<[ResponseType](../modules/src_core_request_response_interface.html#ResponseType)>

  #### Returns void

### streamUsed

* get streamUsed(): boolean
* set streamUsed(value: boolean): void

* + Defined in [src/core/request/response/index.ts:182](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L182)

  True, if the response body is already read as a stream

  #### Returns boolean
* + Defined in [src/core/request/response/index.ts:189](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L189)

  Sets a new status of `streamUsed`

  #### Parameters

  + ##### value: boolean

  #### Returns void

## Methods

### [asyncIterator]

* [asyncIterator](): AsyncIterableIterator<[RequestResponseChunk](../interfaces/src_core_request_interface.RequestResponseChunk.html)>

* + Defined in [src/core/request/response/index.ts:289](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L289)

  Returns an iterator by the response body.
  Mind, when you parse response via iterator, you won't be able to use other parse methods, like `json` or `text`.

  emits
  :   `streamUsed()`

  #### Returns AsyncIterableIterator<[RequestResponseChunk](../interfaces/src_core_request_interface.RequestResponseChunk.html)>

### Protected applyDecoders

* applyDecoders<T>(data: [CanPromise](../modules/index.html#CanPromise)<[ResponseTypeValue](../modules/src_core_request_response_interface.html#ResponseTypeValue)>, decoders?: [WrappedDecoder](../interfaces/src_core_request_interface.WrappedDecoder.html)<unknown, unknown>[]): T

* + Defined in [src/core/request/response/index.ts:683](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L683)

  Applies the given decoders to the specified data and returns a promise with the result

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### data: [CanPromise](../modules/index.html#CanPromise)<[ResponseTypeValue](../modules/src_core_request_response_interface.html#ResponseTypeValue)>
  + ##### decoders: [WrappedDecoder](../interfaces/src_core_request_interface.WrappedDecoder.html)<unknown, unknown>[] = ...

  #### Returns T

### Protected applyStreamDecoders

* applyStreamDecoders<T>(stream: [AnyIterable](../modules/index.html#AnyIterable)<unknown>, decoders?: [WrappedStreamDecoder](../interfaces/src_core_request_interface.WrappedStreamDecoder.html)<unknown, unknown>[]): AsyncIterableIterator<T>

* + Defined in [src/core/request/response/index.ts:729](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L729)

  Applies the given decoders to the specified data stream and yields values via an asynchronous iterator

  #### Type parameters

  + #### T

  #### Parameters

  + ##### stream: [AnyIterable](../modules/index.html#AnyIterable)<unknown>
  + ##### decoders: [WrappedStreamDecoder](../interfaces/src_core_request_interface.WrappedStreamDecoder.html)<unknown, unknown>[] = ...

  #### Returns AsyncIterableIterator<T>

### arrayBuffer

* arrayBuffer(): [default](src_core_promise_abortable.default.html)<ArrayBuffer>

* + Defined in [src/core/request/response/index.ts:642](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L642)

  Parses the response body as an ArrayBuffer and returns it

  #### Returns [default](src_core_promise_abortable.default.html)<ArrayBuffer>

### blob

* blob(): [default](src_core_promise_abortable.default.html)<Blob>

* + Defined in [src/core/request/response/index.ts:634](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L634)

  Parses the response body as a Blob structure and returns it

  #### Returns [default](src_core_promise_abortable.default.html)<Blob>

### decode

* decode(): [default](src_core_promise_abortable.default.html)<null | D>

* + Defined in [src/core/request/response/index.ts:326](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L326)

  Parses the response body and returns a promise with the result.
  The operation result is memoized, and you can't parse the response as a stream after invoking this method.

  A way to parse data is based on the response `Content-Type` header or a passed `responseType` constructor option.
  Also, a sequence of decoders is applied to the parsed result if they are passed with a `decoders`
  constructor option.

  #### Returns [default](src_core_promise_abortable.default.html)<null | D>

### decodeStream

* decodeStream<T>(): AsyncIterableIterator<T>

* + Defined in [src/core/request/response/index.ts:394](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L394)

  Parses the response body as a stream and yields chunks via an async iterator.
  You can't parse the response as a whole data after invoking this method.

  A way to parse data chunks is based on the response `Content-Type` header or a passed `responseType`
  constructor option. Also, a sequence of stream decoders is applied to the parsed chunk if they are
  passed with a `streamDecoders` constructor option.

  #### Type parameters

  + #### T = unknown

  #### Returns AsyncIterableIterator<T>

### Protected decodeToBlob

* decodeToBlob(data: unknown, type?: string): Blob

* + Defined in [src/core/request/response/index.ts:771](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L771)

  Converts the specified data to a Blob structure and returns it

  #### Parameters

  + ##### data: unknown
  + ##### type: string = ...

  #### Returns Blob

### Protected decodeToString

* decodeToString(data: unknown, encoding?: string): [default](src_core_promise_abortable.default.html)<string>

* + Defined in [src/core/request/response/index.ts:796](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L796)

  Converts the specified data to a string and returns it

  #### Parameters

  + ##### data: unknown
  + ##### Optional encoding: string

  #### Returns [default](src_core_promise_abortable.default.html)<string>

### document

* document(): [default](src_core_promise_abortable.default.html)<Document>

* + Defined in [src/core/request/response/index.ts:546](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L546)

  Parses the response body as a Document instance and returns it

  #### Returns [default](src_core_promise_abortable.default.html)<Document>

### formData

* formData(): [default](src_core_promise_abortable.default.html)<FormData>

* + Defined in [src/core/request/response/index.ts:492](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L492)

  Parses the response body as a FormData object and returns it

  #### Returns [default](src_core_promise_abortable.default.html)<FormData>

### getHeader

* getHeader(name: string): [CanUndef](../modules/index.html#CanUndef)<string>

* + Defined in [src/core/request/response/index.ts:314](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L314)

  Returns an HTTP header value by the specified name

  #### Parameters

  + ##### name: string

  #### Returns [CanUndef](../modules/index.html#CanUndef)<string>

### json

* json(): [default](src_core_promise_abortable.default.html)<[JSONLikeValue](../modules/src_core_request_response_interface.html#JSONLikeValue)>

* + Defined in [src/core/request/response/index.ts:423](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L423)

  Parses the response body as a JSON object and returns it

  #### Returns [default](src_core_promise_abortable.default.html)<[JSONLikeValue](../modules/src_core_request_response_interface.html#JSONLikeValue)>

### jsonStream

* jsonStream(): AsyncIterableIterator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/request/response/index.ts:475](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L475)

  Parses the response data stream as a JSON tokens and yields them via an async iterator

  #### Returns AsyncIterableIterator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

### Protected readBody

* readBody(): [default](src_core_promise_abortable.default.html)<[ResponseTypeValue](../modules/src_core_request_response_interface.html#ResponseTypeValue)>

* + Defined in [src/core/request/response/index.ts:664](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L664)

  Reads the response body or throws an exception if reading is impossible

  emits
  :   `bodyUsed()`

  #### Returns [default](src_core_promise_abortable.default.html)<[ResponseTypeValue](../modules/src_core_request_response_interface.html#ResponseTypeValue)>

### stream

* stream(): AsyncIterableIterator<undefined | ArrayBuffer>

* + Defined in [src/core/request/response/index.ts:609](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L609)

  Parses the response data stream as an ArrayBuffer chunks and yields them via an async iterator

  #### Returns AsyncIterableIterator<undefined | ArrayBuffer>

### text

* text(): [default](src_core_promise_abortable.default.html)<string>

* + Defined in [src/core/request/response/index.ts:576](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L576)

  Parses the response body as a string and returns it

  #### Returns [default](src_core_promise_abortable.default.html)<string>

### textStream

* textStream(): AsyncIterableIterator<string>

* + Defined in [src/core/request/response/index.ts:584](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L584)

  Parses the response data stream as a text chunks and yields them via an async iterator

  #### Returns AsyncIterableIterator<string>