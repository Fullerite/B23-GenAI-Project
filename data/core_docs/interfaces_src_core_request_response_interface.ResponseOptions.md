# Interface ResponseOptions
### Hierarchy

* ResponseOptions

## Index

### Properties

* [decoder](src_core_request_response_interface.ResponseOptions.html#decoder)
* [headers](src_core_request_response_interface.ResponseOptions.html#headers)
* [important](src_core_request_response_interface.ResponseOptions.html#important)
* [jsonReviver](src_core_request_response_interface.ResponseOptions.html#jsonReviver)
* [okStatuses](src_core_request_response_interface.ResponseOptions.html#okStatuses)
* [parent](src_core_request_response_interface.ResponseOptions.html#parent)
* [redirected](src_core_request_response_interface.ResponseOptions.html#redirected)
* [responseType](src_core_request_response_interface.ResponseOptions.html#responseType)
* [status](src_core_request_response_interface.ResponseOptions.html#status)
* [statusText](src_core_request_response_interface.ResponseOptions.html#statusText)
* [streamDecoder](src_core_request_response_interface.ResponseOptions.html#streamDecoder)
* [type](src_core_request_response_interface.ResponseOptions.html#type)
* [url](src_core_request_response_interface.ResponseOptions.html#url)

## Properties

### Optional decoder

decoder?: [WrappedDecoder](src_core_request_interface.WrappedDecoder.html)<unknown, unknown> | [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)

* Defined in [src/core/request/response/interface.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L84)

### Optional headers

headers?: [RawHeaders](../modules/src_core_request_headers_interface.html#RawHeaders)

* Defined in [src/core/request/response/interface.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L82)

### Optional important

important?: boolean

* Defined in [src/core/request/response/interface.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L75)

### Optional jsonReviver

jsonReviver?: false | [JSONCb](index.JSONCb.html)

* Defined in [src/core/request/response/interface.ts:86](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L86)

### Optional okStatuses

okStatuses?: [OkStatuses](../modules/src_core_request_interface.html#OkStatuses)

* Defined in [src/core/request/response/interface.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L79)

### Optional parent

parent?: [default](../classes/src_core_promise_abortable.default.html)<unknown>

* Defined in [src/core/request/response/interface.ts:74](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L74)

### Optional redirected

redirected?: boolean

* Defined in [src/core/request/response/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L71)

### Optional responseType

responseType?: [ResponseType](../modules/src_core_request_response_interface.html#ResponseType)

* Defined in [src/core/request/response/interface.ts:81](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L81)

### Optional status

status?: [StatusCodes](../enums/src_core_status_codes_interface.StatusCodes.html)

* Defined in [src/core/request/response/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L77)

### Optional statusText

statusText?: string

* Defined in [src/core/request/response/interface.ts:78](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L78)

### Optional streamDecoder

streamDecoder?: [WrappedStreamDecoder](src_core_request_interface.WrappedStreamDecoder.html)<unknown, unknown> | [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)

* Defined in [src/core/request/response/interface.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L85)

### Optional type

type?: [ResponseModeType](../modules/src_core_request_response_interface.html#ResponseModeType)

* Defined in [src/core/request/response/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L72)

### Optional url

url?: string

* Defined in [src/core/request/response/interface.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/request/response/interface.ts#L70)