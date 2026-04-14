# Class ConfigurableMiddleware
### Hierarchy

* ConfigurableMiddleware

### Implements

* [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)

## Index

### Constructors

* [constructor](src_core_log_middlewares_configurable.ConfigurableMiddleware.html#constructor)

### Properties

* [queue](src_core_log_middlewares_configurable.ConfigurableMiddleware.html#queue)

### Methods

* [exec](src_core_log_middlewares_configurable.ConfigurableMiddleware.html#exec)
* [filterContext](src_core_log_middlewares_configurable.ConfigurableMiddleware.html#filterContext)

## Constructors

### constructor

* new ConfigurableMiddleware(): [ConfigurableMiddleware](src_core_log_middlewares_configurable.ConfigurableMiddleware.html)

* #### Returns [ConfigurableMiddleware](src_core_log_middlewares_configurable.ConfigurableMiddleware.html)

## Properties

### Protected queue

queue: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)[] = []

* Defined in [src/core/log/middlewares/configurable.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/configurable.ts#L39)

## Methods

### exec

* exec(events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>, next: [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)): void

* Implementation of [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html).[exec](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html#exec)

  + Defined in [src/core/log/middlewares/configurable.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/configurable.ts#L41)

  Processes the events
  (if it has data to pass to the next middleware, calls the next callback)

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>
  + ##### next: [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)

  #### Returns void

### Protected filterContext

* filterContext(context: string): boolean

* + Defined in [src/core/log/middlewares/configurable.ts:103](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/configurable.ts#L103)

  Returns true if config patterns allow to log a record with the specified context

  #### Parameters

  + ##### context: string

  #### Returns boolean