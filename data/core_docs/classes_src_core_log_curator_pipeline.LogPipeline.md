# Class LogPipeline
### Hierarchy

* LogPipeline

## Index

### Constructors

* [constructor](src_core_log_curator_pipeline.LogPipeline.html#constructor)

### Properties

* [engine](src_core_log_curator_pipeline.LogPipeline.html#engine)
* [middlewareIndex](src_core_log_curator_pipeline.LogPipeline.html#middlewareIndex)
* [middlewares](src_core_log_curator_pipeline.LogPipeline.html#middlewares)
* [minLevel](src_core_log_curator_pipeline.LogPipeline.html#minLevel)
* [nextCallback](src_core_log_curator_pipeline.LogPipeline.html#nextCallback)

### Methods

* [next](src_core_log_curator_pipeline.LogPipeline.html#next)
* [run](src_core_log_curator_pipeline.LogPipeline.html#run)

## Constructors

### constructor

* new LogPipeline(engine: [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html), middlewares: [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)[], minLevel: [LogLevel](../modules/src_core_log_interface.html#LogLevel)): [LogPipeline](src_core_log_curator_pipeline.LogPipeline.html)

* + Defined in [src/core/log/curator/pipeline.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L22)

  #### Parameters

  + ##### engine: [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html)
  + ##### middlewares: [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)[]
  + ##### minLevel: [LogLevel](../modules/src_core_log_interface.html#LogLevel)

  #### Returns [LogPipeline](src_core_log_curator_pipeline.LogPipeline.html)

## Properties

### Protected engine

engine: [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html)

* Defined in [src/core/log/curator/pipeline.ts:16](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L16)

### Protected middlewareIndex

middlewareIndex: number = 0

* Defined in [src/core/log/curator/pipeline.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L19)

### Protected middlewares

middlewares: [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)[]

* Defined in [src/core/log/curator/pipeline.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L17)

### Protected minLevel

minLevel: [LogLevel](../modules/src_core_log_interface.html#LogLevel)

* Defined in [src/core/log/curator/pipeline.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L20)

### Protected nextCallback

nextCallback: (events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>) => void

* Defined in [src/core/log/curator/pipeline.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L18)

#### Type declaration

* + (events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>): void
  + #### Parameters

    - ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>

    #### Returns void

## Methods

### Protected next

* next(events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>): void

* + Defined in [src/core/log/curator/pipeline.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L66)

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>

  #### Returns void

### run

* run(events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>): void

* + Defined in [src/core/log/curator/pipeline.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/log/curator/pipeline.ts#L33)

  Carries events through a chain of middlewares and passes them to the engine in the end

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<[LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)>

  #### Returns void