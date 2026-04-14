# Class ErrorsDeduplicatorMiddleware
Middleware to omit duplicated errors

### Hierarchy

* ErrorsDeduplicatorMiddleware

### Implements

* [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)

## Index

### Constructors

* [constructor](src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html#constructor)

### Properties

* [errorsDoubles](src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html#errorsDoubles)

### Methods

* [exec](src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html#exec)
* [omitEvent](src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html#omitEvent)

## Constructors

### constructor

* new ErrorsDeduplicatorMiddleware(): [ErrorsDeduplicatorMiddleware](src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html)

* #### Returns [ErrorsDeduplicatorMiddleware](src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html)

## Properties

### Protected errorsDoubles

errorsDoubles: WeakSet<Error> = ...

* Defined in [src/core/log/middlewares/errors-deduplicator/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/errors-deduplicator/index.ts#L23)

Errors that have already been occurred

## Methods

### exec

* exec(events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>, next: [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)): void

* Implementation of [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html).[exec](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html#exec)

  + Defined in [src/core/log/middlewares/errors-deduplicator/index.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/errors-deduplicator/index.ts#L26)

  Processes the events
  (if it has data to pass to the next middleware, calls the next callback)

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>
  + ##### next: [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)

  #### Returns void

### Protected omitEvent

* omitEvent(event: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)): boolean

* + Defined in [src/core/log/middlewares/errors-deduplicator/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/errors-deduplicator/index.ts#L43)

  Returns true if the passed event has an error that's already occurred

  #### Parameters

  + ##### event: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)

    log event from a pipeline

  #### Returns boolean