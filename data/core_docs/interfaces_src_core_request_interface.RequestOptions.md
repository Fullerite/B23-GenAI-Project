# Interface RequestOptions
### Hierarchy

* RequestOptions

## Index

### Properties

* [body](src_core_request_interface.RequestOptions.html#body)
* [contentType](src_core_request_interface.RequestOptions.html#contentType)
* [credentials](src_core_request_interface.RequestOptions.html#credentials)
* [decoders](src_core_request_interface.RequestOptions.html#decoders)
* [emitter](src_core_request_interface.RequestOptions.html#emitter)
* [headers](src_core_request_interface.RequestOptions.html#headers)
* [important](src_core_request_interface.RequestOptions.html#important)
* [jsonReviver](src_core_request_interface.RequestOptions.html#jsonReviver)
* [method](src_core_request_interface.RequestOptions.html#method)
* [okStatuses](src_core_request_interface.RequestOptions.html#okStatuses)
* [parent](src_core_request_interface.RequestOptions.html#parent)
* [responseType](src_core_request_interface.RequestOptions.html#responseType)
* [streamDecoders](src_core_request_interface.RequestOptions.html#streamDecoders)
* [timeout](src_core_request_interface.RequestOptions.html#timeout)
* [url](src_core_request_interface.RequestOptions.html#url)

## Properties

### Optional Readonly body

body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody)

* Defined in [src/core/request/interface.ts:677](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L677)

### Optional Readonly contentType

contentType?: string

* Defined in [src/core/request/interface.ts:669](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L669)

### Optional Readonly credentials

credentials?: boolean | RequestCredentials

* Defined in [src/core/request/interface.ts:680](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L680)

### Optional Readonly decoders

decoders?: [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)

* Defined in [src/core/request/interface.ts:672](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L672)

### Readonly emitter

emitter: EventEmitter2

* Defined in [src/core/request/interface.ts:663](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L663)

### Optional Readonly headers

headers?: [default](../classes/src_core_request_headers.default.html)

* Defined in [src/core/request/interface.ts:676](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L676)

### Optional Readonly important

important?: boolean

* Defined in [src/core/request/interface.ts:679](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L679)

### Optional Readonly jsonReviver

jsonReviver?: false | [JSONCb](index.JSONCb.html)

* Defined in [src/core/request/interface.ts:674](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L674)

### Readonly method

method: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)

* Defined in [src/core/request/interface.ts:661](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L661)

### Optional Readonly okStatuses

okStatuses?: [OkStatuses](../modules/src_core_request_interface.html#OkStatuses)

* Defined in [src/core/request/interface.ts:667](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L667)

### Readonly parent

parent: [default](../classes/src_core_promise_abortable.default.html)<unknown>

* Defined in [src/core/request/interface.ts:664](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L664)

### Optional Readonly responseType

responseType?: [ResponseType](../modules/src_core_request_response_interface.html#ResponseType)

* Defined in [src/core/request/interface.ts:670](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L670)

### Optional Readonly streamDecoders

streamDecoders?: [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)

* Defined in [src/core/request/interface.ts:673](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L673)

### Optional Readonly timeout

timeout?: number

* Defined in [src/core/request/interface.ts:666](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L666)

### Readonly url

url: string

* Defined in [src/core/request/interface.ts:660](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L660)