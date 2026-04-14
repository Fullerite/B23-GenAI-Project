# Module src/core/log/middlewares
## Index

### References

* [CtorArgs](src_core_log_middlewares.html#CtorArgs)
* [Extended](src_core_log_middlewares.html#Extended)
* [LogEvent](src_core_log_middlewares.html#LogEvent)
* [LogMiddleware](src_core_log_middlewares.html#LogMiddleware)
* [LogMiddlewares](src_core_log_middlewares.html#LogMiddlewares)
* [LogMiddlewaresName](src_core_log_middlewares.html#LogMiddlewaresName)
* [LogMiddlewaresTuple](src_core_log_middlewares.html#LogMiddlewaresTuple)
* [NextCallback](src_core_log_middlewares.html#NextCallback)
* [extend](src_core_log_middlewares.html#extend)

### Variables

* [default](src_core_log_middlewares.html#default)

### Functions

* [creatorFor](src_core_log_middlewares.html#creatorFor)

## References

### CtorArgs

Re-exports [CtorArgs](src_core_log_middlewares_interface.html#CtorArgs)

### Extended

Re-exports [Extended](src_core_log_base_interface.html#Extended)

### LogEvent

Re-exports [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)

### LogMiddleware

Re-exports [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)

### LogMiddlewares

Re-exports [LogMiddlewares](src_core_log_middlewares_interface.html#LogMiddlewares)

### LogMiddlewaresName

Re-exports [LogMiddlewaresName](src_core_log_middlewares_interface.html#LogMiddlewaresName)

### LogMiddlewaresTuple

Re-exports [LogMiddlewaresTuple](src_core_log_middlewares_interface.html#LogMiddlewaresTuple)

### NextCallback

Re-exports [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)

### extend

Renames and re-exports [default](src_core_log_base_extend.html#default)

## Variables

### Const default

default: { configurable: (...args: []) => [ConfigurableMiddleware](../classes/src_core_log_middlewares_configurable.ConfigurableMiddleware.html); errorsDeduplicator: (...args: []) => [ErrorsDeduplicatorMiddleware](../classes/src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html); extractor: (...args: [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>[]) => [ExtractorMiddleware](../classes/src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html) } = ...

* Defined in [src/core/log/middlewares/index.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/index.ts#L25)

#### Type declaration

* ##### configurable: (...args: []) => [ConfigurableMiddleware](../classes/src_core_log_middlewares_configurable.ConfigurableMiddleware.html)

  + - (...args: []): [ConfigurableMiddleware](../classes/src_core_log_middlewares_configurable.ConfigurableMiddleware.html)
    - Returns a function that creates a middleware of the specified class

      #### Parameters

      * ##### Rest ...args: []

      #### Returns [ConfigurableMiddleware](../classes/src_core_log_middlewares_configurable.ConfigurableMiddleware.html)
* ##### errorsDeduplicator: (...args: []) => [ErrorsDeduplicatorMiddleware](../classes/src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html)

  + - (...args: []): [ErrorsDeduplicatorMiddleware](../classes/src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html)
    - Returns a function that creates a middleware of the specified class

      #### Parameters

      * ##### Rest ...args: []

      #### Returns [ErrorsDeduplicatorMiddleware](../classes/src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html)
* ##### extractor: (...args: [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>[]) => [ExtractorMiddleware](../classes/src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html)

  + - (...args: [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>[]): [ExtractorMiddleware](../classes/src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html)
    - Returns a function that creates a middleware of the specified class

      #### Parameters

      * ##### Rest ...args: [ErrorDetailsExtractor](../interfaces/src_core_error_interface.ErrorDetailsExtractor.html)<Error>[]

      #### Returns [ExtractorMiddleware](../classes/src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html)

## Functions

### creatorFor

* creatorFor<T, A>(Ctor: new (...args: A) => T): (...args: A) => T

* + Defined in [src/core/log/middlewares/index.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/index.ts#L21)

  Returns a function that creates a middleware of the specified class

  #### Type parameters

  + #### T: [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)
  + #### A: any[]

  #### Parameters

  + ##### Ctor: new (...args: A) => T

    constructor or just a class

    - * new (...args: A): T
      * #### Parameters

        + ##### Rest ...args: A

        #### Returns T

  #### Returns (...args: A) => T

  + - (...args: A): T
    - Returns a function that creates a middleware of the specified class

      #### Parameters

      * ##### Rest ...args: A

      #### Returns T