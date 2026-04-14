# Class RequestErrorDetailsExtractor
Extractor to get details from `RequestError`

### Hierarchy

* RequestErrorDetailsExtractor

### Implements

* [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<[default](src_core_request_error.default.html)>

## Index

### Constructors

* [constructor](src_core_request_error_extractor.RequestErrorDetailsExtractor.html#constructor)

### Properties

* [headersFilterParams](src_core_request_error_extractor.RequestErrorDetailsExtractor.html#headersFilterParams)
* [target](src_core_request_error_extractor.RequestErrorDetailsExtractor.html#target)

### Methods

* [extract](src_core_request_error_extractor.RequestErrorDetailsExtractor.html#extract)
* [prepareHeaders](src_core_request_error_extractor.RequestErrorDetailsExtractor.html#prepareHeaders)

## Constructors

### constructor

* new RequestErrorDetailsExtractor(opts?: [RequestErrorDetailsExtractorOptions](../interfaces/src_core_request_error_interface.RequestErrorDetailsExtractorOptions.html)): [RequestErrorDetailsExtractor](src_core_request_error_extractor.RequestErrorDetailsExtractor.html)

* + Defined in [src/core/request/error/extractor.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/request/error/extractor.ts#L33)

  #### Parameters

  + ##### Optional opts: [RequestErrorDetailsExtractorOptions](../interfaces/src_core_request_error_interface.RequestErrorDetailsExtractorOptions.html)

  #### Returns [RequestErrorDetailsExtractor](src_core_request_error_extractor.RequestErrorDetailsExtractor.html)

## Properties

### Protected headersFilterParams

headersFilterParams: FilterParams

* Defined in [src/core/request/error/extractor.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/request/error/extractor.ts#L31)

Parameters to define which header makes its way to the result

### target

target: [ErrorCtor](../modules/src_core_error_interface.html#ErrorCtor)<[default](src_core_request_error.default.html)<undefined>> = RequestError

Implementation of [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html).[target](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html#target)

* Defined in [src/core/request/error/extractor.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/request/error/extractor.ts#L26)

Constructor function of an error

## Methods

### extract

* extract(error: [default](src_core_request_error.default.html)<undefined>): unknown

* Implementation of [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html).[extract](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html#extract)

  + Defined in [src/core/request/error/extractor.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/request/error/extractor.ts#L41)

  Extracts details from the passed error

  #### Parameters

  + ##### error: [default](src_core_request_error.default.html)<undefined>

    an error, which details should be extracted

  #### Returns unknown

### Protected prepareHeaders

* prepareHeaders(headers: [CanUndef](../modules/index.html#CanUndef)<[RawHeaders](../modules/src_core_request_headers_interface.html#RawHeaders)>): [CanUndef](../modules/index.html#CanUndef)<[default](src_core_request_headers.default.html)>

* + Defined in [src/core/request/error/extractor.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/request/error/extractor.ts#L70)

  Filters the specified headers according to settings

  see
  :   headersFilterParams

  #### Parameters

  + ##### headers: [CanUndef](../modules/index.html#CanUndef)<[RawHeaders](../modules/src_core_request_headers_interface.html#RawHeaders)>

    headers that need to be filtered

  #### Returns [CanUndef](../modules/index.html#CanUndef)<[default](src_core_request_headers.default.html)>