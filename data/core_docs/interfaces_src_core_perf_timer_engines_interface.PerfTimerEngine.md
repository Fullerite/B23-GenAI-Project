# Interface PerfTimerEngine
An engine to send time metrics to the target

### Hierarchy

* PerfTimerEngine

## Index

### Methods

* [getTimestampFromTimeOrigin](src_core_perf_timer_engines_interface.PerfTimerEngine.html#getTimestampFromTimeOrigin)
* [sendDelta](src_core_perf_timer_engines_interface.PerfTimerEngine.html#sendDelta)

## Methods

### getTimestampFromTimeOrigin

* getTimestampFromTimeOrigin(): number

* + Defined in [src/core/perf/timer/engines/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/engines/interface.ts#L29)

  Returns a timestamp from the application start

  #### Returns number

### sendDelta

* sendDelta(name: string, duration: number, additional?: [Dictionary](index.Dictionary.html)<unknown>): void

* + Defined in [src/core/perf/timer/engines/interface.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/engines/interface.ts#L24)

  Sends metrics by the specified parameters

  #### Parameters

  + ##### name: string

    metrics name
  + ##### duration: number

    difference between two moments of time
  + ##### Optional additional: [Dictionary](index.Dictionary.html)<unknown>

  #### Returns void