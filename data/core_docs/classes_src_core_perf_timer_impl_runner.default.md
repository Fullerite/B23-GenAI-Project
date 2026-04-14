# Class default
Represents abstraction that can measure the difference between time moments and create new performance timers

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_perf_timer_impl_runner.default.html#constructor)

### Properties

* [engine](src_core_perf_timer_impl_runner.default.html#engine)
* [filter](src_core_perf_timer_impl_runner.default.html#filter)
* [idToMeasurement](src_core_perf_timer_impl_runner.default.html#idToMeasurement)
* [nsToCounter](src_core_perf_timer_impl_runner.default.html#nsToCounter)
* [salt](src_core_perf_timer_impl_runner.default.html#salt)
* [timeOrigin](src_core_perf_timer_impl_runner.default.html#timeOrigin)

### Methods

* [createTimer](src_core_perf_timer_impl_runner.default.html#createTimer)
* [finish](src_core_perf_timer_impl_runner.default.html#finish)
* [getTimestamp](src_core_perf_timer_impl_runner.default.html#getTimestamp)
* [markTimestamp](src_core_perf_timer_impl_runner.default.html#markTimestamp)
* [start](src_core_perf_timer_impl_runner.default.html#start)
* [combineNamespaces](src_core_perf_timer_impl_runner.default.html#combineNamespaces)

## Constructors

### constructor

* new default(engine: [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html), opts?: [PerfTimersRunnerOptions](../interfaces/src_core_perf_timer_impl_interface.PerfTimersRunnerOptions.html)): [default](src_core_perf_timer_impl_runner.default.html)

* + Defined in [src/core/perf/timer/impl/runner.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L75)

  #### Parameters

  + ##### engine: [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html)

    engine instance that sends metrics to the target destination
  + ##### Optional opts: [PerfTimersRunnerOptions](../interfaces/src_core_perf_timer_impl_interface.PerfTimersRunnerOptions.html)

  #### Returns [default](src_core_perf_timer_impl_runner.default.html)

## Properties

### Protected engine

engine: [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html)

* Defined in [src/core/perf/timer/impl/runner.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L40)

An engine's instance that sends metrics to the target destination

### Protected Optional filter

filter?: [PerfPredicate](../modules/src_core_perf_config_interface.html#PerfPredicate)

* Defined in [src/core/perf/timer/impl/runner.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L52)

Predicate to filter metrics by their names.
If it returns `false`, the metrics will not send to the engine.

### Protected idToMeasurement

idToMeasurement: [Dictionary](../interfaces/index.Dictionary.html)<[PerfTimerMeasurement](../interfaces/src_core_perf_timer_impl_interface.PerfTimerMeasurement.html)> = ...

* Defined in [src/core/perf/timer/impl/runner.ts:62](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L62)

Internal storage for the current `start`/`finish` metrics

### Protected nsToCounter

nsToCounter: [Dictionary](../interfaces/index.Dictionary.html)<number> = ...

* Defined in [src/core/perf/timer/impl/runner.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L57)

Internal storage for the following identifier of each namespace

### Protected salt

salt: number = ...

* Defined in [src/core/perf/timer/impl/runner.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L69)

Salt for each runner instance.
It is used to generate a time, so the times from the different runners cannot be used interchangeably.
It prevents sending `start`/`finish` metrics by mistake.

### Protected timeOrigin

timeOrigin: number

* Defined in [src/core/perf/timer/impl/runner.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L46)

Time offset from the application start.
It may be considered as the time from which all metrics are measured for the current runner instance.

## Methods

### createTimer

* createTimer(group: "network" | "components" | "tools" | "manual"): [PerfTimer](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html)

* + Defined in [src/core/perf/timer/impl/runner.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L85)

  Returns a new instance of the performance timer

  #### Parameters

  + ##### group: "network" | "components" | "tools" | "manual"

    timer group

  #### Returns [PerfTimer](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html)

### Protected finish

* finish(perfTimerId: [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId), additional?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): void

* + Defined in [src/core/perf/timer/impl/runner.ts:145](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L145)

  see
  :   [PerfTimer.finish](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html#finish)

  #### Parameters

  + ##### perfTimerId: [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId)
  + ##### Optional additional: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

  #### Returns void

### Protected getTimestamp

* getTimestamp(): number

* + Defined in [src/core/perf/timer/impl/runner.ts:184](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L184)

  Returns a timestamp taking into account the runner's timer origin

  #### Returns number

### Protected markTimestamp

* markTimestamp(name: string, additional?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): void

* + Defined in [src/core/perf/timer/impl/runner.ts:170](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L170)

  see
  :   [PerfTimer.markTimestamp](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html#markTimestamp)

  #### Parameters

  + ##### name: string
  + ##### Optional additional: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

  #### Returns void

### Protected start

* start(name: string): [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId)

* + Defined in [src/core/perf/timer/impl/runner.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L123)

  see
  :   [PerfTimer.start](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html#start)

  #### Parameters

  + ##### name: string

  #### Returns [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId)

### Static combineNamespaces

* combineNamespaces(...namespaces: [CanUndef](../modules/index.html#CanUndef)<string>[]): string

* + Defined in [src/core/perf/timer/impl/runner.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/runner.ts#L33)

  Combines the passed namespaces together

  #### Parameters

  + ##### Rest ...namespaces: [CanUndef](../modules/index.html#CanUndef)<string>[]

    namespaces to combine

  #### Returns string