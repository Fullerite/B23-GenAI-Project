# Class TestExtractor
### Hierarchy

* TestExtractor

### Implements

* [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<[TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)>

## Index

### Constructors

* [constructor](src_core_log_middlewares_extractor_testing.TestExtractor.html#constructor)

### Properties

* [target](src_core_log_middlewares_extractor_testing.TestExtractor.html#target)

### Methods

* [extract](src_core_log_middlewares_extractor_testing.TestExtractor.html#extract)

## Constructors

### constructor

* new TestExtractor(): [TestExtractor](src_core_log_middlewares_extractor_testing.TestExtractor.html)

* #### Returns [TestExtractor](src_core_log_middlewares_extractor_testing.TestExtractor.html)

## Properties

### target

target: [ErrorCtor](../modules/src_core_error_interface.html#ErrorCtor)<[TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)> = TestDetailedBaseError

Implementation of [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html).[target](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html#target)

* Defined in [src/core/log/middlewares/extractor/testing.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/testing.ts#L32)

Constructor function of an error

## Methods

### extract

* extract(error: [TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)): unknown

* Implementation of [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html).[extract](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html#extract)

  + Defined in [src/core/log/middlewares/extractor/testing.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/testing.ts#L34)

  Extracts details from the passed error

  #### Parameters

  + ##### error: [TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)

  #### Returns unknown