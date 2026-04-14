# Interface ErrorDetailsExtractor<E>
Extractor that gets details from an error of type `E`

### Type parameters

* #### E: Error

### Hierarchy

* ErrorDetailsExtractor

### Implemented by

* [RequestErrorDetailsExtractor](../classes/src_core_request_error_extractor.RequestErrorDetailsExtractor.html)
* [TestExtractor](../classes/src_core_log_middlewares_extractor_testing.TestExtractor.html)

## Index

### Properties

* [target](src_core_error_interface.ErrorDetailsExtractor.html#target)

### Methods

* [extract](src_core_error_interface.ErrorDetailsExtractor.html#extract)

## Properties

### target

target: [ErrorCtor](../modules/src_core_error_interface.html#ErrorCtor)<E>

* Defined in [src/core/error/interface.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/error/interface.ts#L18)

Constructor function of an error

## Methods

### extract

* extract(error: E): unknown

* + Defined in [src/core/error/interface.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/error/interface.ts#L24)

  Extracts details from the passed error

  #### Parameters

  + ##### error: E

    an error, which details should be extracted

  #### Returns unknown