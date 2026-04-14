# Module src/core/perf/config/interface
## Index

### Interfaces

* [PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)
* [PerfIncludeFilter](../interfaces/src_core_perf_config_interface.PerfIncludeFilter.html)
* [PerfTimerConfig](../interfaces/src_core_perf_config_interface.PerfTimerConfig.html)

### Type aliases

* [PerfGroupFilters](src_core_perf_config_interface.html#PerfGroupFilters)
* [PerfPredicate](src_core_perf_config_interface.html#PerfPredicate)
* [PerfPredicates](src_core_perf_config_interface.html#PerfPredicates)

## Type aliases

### PerfGroupFilters

PerfGroupFilters: { [ K in [PerfGroup](src_core_perf_interface.html#PerfGroup)]?: [PerfIncludeFilter](../interfaces/src_core_perf_config_interface.PerfIncludeFilter.html) | string[] | boolean }

* Defined in [src/core/perf/config/interface.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/interface.ts#L40)

Settings to filter perf events by groups

### PerfPredicate

PerfPredicate: (ns: string) => boolean

* Defined in [src/core/perf/config/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/interface.ts#L63)

#### Type declaration

* + (ns: string): boolean
  + Filtering predicate

    #### Parameters

    - ##### ns: string

    #### Returns boolean

### PerfPredicates

PerfPredicates: { [ K in [PerfGroup](src_core_perf_interface.html#PerfGroup)]: [PerfPredicate](src_core_perf_config_interface.html#PerfPredicate) }

* Defined in [src/core/perf/config/interface.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/interface.ts#L69)

Simple filtering predicates for each group

see
:   PerfGroupFilters