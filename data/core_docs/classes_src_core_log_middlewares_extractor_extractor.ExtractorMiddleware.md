# Class ExtractorMiddleware
Middleware to extract information from an error log event and store
it within the `additionals` dictionary of the event

### Hierarchy

* ExtractorMiddleware

### Implements

* [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)

## Index

### Constructors

* [constructor](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html#constructor)

### Properties

* [extractorsMap](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html#extractorsMap)

### Methods

* [exec](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html#exec)
* [generateErrorInfo](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html#generateErrorInfo)
* [processEvent](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html#processEvent)

## Constructors

### constructor

* new ExtractorMiddleware(...extractors: [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>[]): [ExtractorMiddleware](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html)

* + Defined in [src/core/log/middlewares/extractor/extractor.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/extractor.ts#L23)

  #### Parameters

  + ##### Rest ...extractors: [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>[]

  #### Returns [ExtractorMiddleware](src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html)

## Properties

### extractorsMap

extractorsMap: Map<[ErrorCtor](../modules/src_core_error_interface.html#ErrorCtor)<Error>, [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>>

* Defined in [src/core/log/middlewares/extractor/extractor.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/extractor.ts#L21)

## Methods

### exec

* exec(events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>, next: [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)): void

* Implementation of [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html).[exec](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html#exec)

  + Defined in [src/core/log/middlewares/extractor/extractor.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/extractor.ts#L28)

  Processes the events
  (if it has data to pass to the next middleware, calls the next callback)

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>
  + ##### next: [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)

  #### Returns void

### Protected generateErrorInfo

* generateErrorInfo(error: Error, isRoot?: boolean, depthLimit?: number): [ErrorInfo](../interfaces/src_core_log_middlewares_extractor_interface.ErrorInfo.html)

* + Defined in [src/core/log/middlewares/extractor/extractor.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/extractor.ts#L61)

  Returns an error's info structure

  #### Parameters

  + ##### error: Error

    error, which details should be returned
  + ##### isRoot: boolean = true

    if false then adds `name` and `message` of the passed error to its info
  + ##### depthLimit: number = DEPTH\_LIMIT

    maximum depth of nested errors

  #### Returns [ErrorInfo](../interfaces/src_core_log_middlewares_extractor_interface.ErrorInfo.html)

### Protected processEvent

* processEvent(event: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)): [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)

* + Defined in [src/core/log/middlewares/extractor/extractor.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/extractor.ts#L41)

  Extracts error's details from the passed log event and stores it within the `additionals.error` property

  #### Parameters

  + ##### event: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)

    log event from a pipeline

  #### Returns [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)