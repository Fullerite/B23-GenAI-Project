# Interface LogMiddleware
### Hierarchy

* LogMiddleware

### Implemented by

* [ConfigurableMiddleware](../classes/src_core_log_middlewares_configurable.ConfigurableMiddleware.html)
* [ErrorsDeduplicatorMiddleware](../classes/src_core_log_middlewares_errors_deduplicator.ErrorsDeduplicatorMiddleware.html)
* [ExtractorMiddleware](../classes/src_core_log_middlewares_extractor_extractor.ExtractorMiddleware.html)

## Index

### Methods

* [exec](src_core_log_middlewares_interface.LogMiddleware.html#exec)

## Methods

### exec

* exec(events: [CanArray](../modules/index.html#CanArray)<[LogEvent](src_core_log_middlewares_interface.LogEvent.html)>, next: [NextCallback](src_core_log_middlewares_interface.NextCallback.html)): void

* + Defined in [src/core/log/middlewares/interface.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/interface.ts#L37)

  Processes the events
  (if it has data to pass to the next middleware, calls the next callback)

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](src_core_log_middlewares_interface.LogEvent.html)>
  + ##### next: [NextCallback](src_core_log_middlewares_interface.NextCallback.html)

  #### Returns void