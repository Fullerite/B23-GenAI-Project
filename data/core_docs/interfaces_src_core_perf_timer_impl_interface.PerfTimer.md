# Interface PerfTimer
Performance timer

### Hierarchy

* PerfTimer

## Index

### Methods

* [finish](src_core_perf_timer_impl_interface.PerfTimer.html#finish)
* [markTimestamp](src_core_perf_timer_impl_interface.PerfTimer.html#markTimestamp)
* [namespace](src_core_perf_timer_impl_interface.PerfTimer.html#namespace)
* [start](src_core_perf_timer_impl_interface.PerfTimer.html#start)

## Methods

### finish

* finish(timerId: [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId), additional?: [Dictionary](index.Dictionary.html)<unknown>): void

* + Defined in [src/core/perf/timer/impl/interface.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/interface.ts#L43)

  Finishes started measurement by its identifier.
  Works together with the `start` method.

  #### Parameters

  + ##### timerId: [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId)

    id of the metrics to stop
  + ##### Optional additional: [Dictionary](index.Dictionary.html)<unknown>

  #### Returns void

### markTimestamp

* markTimestamp(name: string, additional?: [Dictionary](index.Dictionary.html)<unknown>): void

* + Defined in [src/core/perf/timer/impl/interface.ts:51](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/interface.ts#L51)

  Measures difference between the current moment and the time origin of a corresponding timers runner

  #### Parameters

  + ##### name: string

    full name of the metrics
  + ##### Optional additional: [Dictionary](index.Dictionary.html)<unknown>

  #### Returns void

### namespace

* namespace(ns: string): [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

* + Defined in [src/core/perf/timer/impl/interface.ts:67](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/interface.ts#L67)

  Returns a new instance of the performance timer but with the passed suffix

  example
  :   ```
      // `timer` has a namespace "components"  
      const timer = getTimer('components');  
        
      // `newTimer` has a namespace "components.button"  
      const newTimer = timer.namespace('button');
      ```

  #### Parameters

  + ##### ns: string

    namespace suffix

  #### Returns [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

### start

* start(name: string): [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId)

* + Defined in [src/core/perf/timer/impl/interface.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/interface.ts#L34)

  Starts measuring for the specified name and returns an identifier of the metrics

  #### Parameters

  + ##### name: string

    full name of the metrics

  #### Returns [PerfTimerId](../modules/src_core_perf_timer_impl_interface.html#PerfTimerId)