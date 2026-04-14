# Interface PerfTimersRunnerOptions
Options of a performance timers runner

### Hierarchy

* PerfTimersRunnerOptions

## Index

### Properties

* [filter](src_core_perf_timer_impl_interface.PerfTimersRunnerOptions.html#filter)
* [withCurrentTimeOrigin](src_core_perf_timer_impl_interface.PerfTimersRunnerOptions.html#withCurrentTimeOrigin)

## Properties

### Optional filter

filter?: [PerfPredicate](../modules/src_core_perf_config_interface.html#PerfPredicate)

* Defined in [src/core/perf/timer/impl/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/interface.ts#L77)

Predicate to filter metrics

### Optional withCurrentTimeOrigin

withCurrentTimeOrigin?: boolean

* Defined in [src/core/perf/timer/impl/interface.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/impl/interface.ts#L82)

If `true`, then a moment of instantiating of the runner is considering as its time origin