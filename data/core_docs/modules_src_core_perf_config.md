# Module src/core/perf/config
[# core/perf/config](#coreperfconfig)

This module provides a bunch of helpers to configure the `core/perf` module.

[## Configuration interface](#configuration-interface)

```
/**  
 * General config for performance metrics  
 */  
export interface PerfConfig {  
  /**  
   * Performance timers config  
   */  
  timer: PerfTimerConfig;  
}  
  
/**  
 * Performance timers config  
 */  
export interface PerfTimerConfig {  
  /**  
   * Name of the used engine  
   */  
  engine: PerfTimerEngineName;  
  
  /**  
   * Settings to filter perf events by groups  
   */  
  filters?: PerfGroupFilters;  
}  
  
/**  
 * Settings to filter perf events by groups  
 */  
export type PerfGroupFilters = {  
  [K in PerfGroup]?: PerfIncludeFilter | string[] | boolean;  
};  
  
/**  
 * Include/exclude patterns for perf filters  
 */  
export interface PerfIncludeFilter {  
  /**  
   * Include only specific events  
   */  
  include?: string[];  
  
  /**  
   * Exclude only specific events.  
   * If `include` and `exclude` are both presented, will be used only include.  
   */  
  exclude?: string[];  
}
```

## Index

### References

* [PerfConfig](src_core_perf_config.html#PerfConfig)
* [PerfGroupFilters](src_core_perf_config.html#PerfGroupFilters)
* [PerfIncludeFilter](src_core_perf_config.html#PerfIncludeFilter)
* [PerfPredicate](src_core_perf_config.html#PerfPredicate)
* [PerfPredicates](src_core_perf_config.html#PerfPredicates)
* [PerfTimerConfig](src_core_perf_config.html#PerfTimerConfig)

### Functions

* [createPredicates](src_core_perf_config.html#createPredicates)
* [getTimerEngine](src_core_perf_config.html#getTimerEngine)
* [mergeConfigs](src_core_perf_config.html#mergeConfigs)

## References

### PerfConfig

Re-exports [PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)

### PerfGroupFilters

Re-exports [PerfGroupFilters](src_core_perf_config_interface.html#PerfGroupFilters)

### PerfIncludeFilter

Re-exports [PerfIncludeFilter](../interfaces/src_core_perf_config_interface.PerfIncludeFilter.html)

### PerfPredicate

Re-exports [PerfPredicate](src_core_perf_config_interface.html#PerfPredicate)

### PerfPredicates

Re-exports [PerfPredicates](src_core_perf_config_interface.html#PerfPredicates)

### PerfTimerConfig

Re-exports [PerfTimerConfig](../interfaces/src_core_perf_config_interface.PerfTimerConfig.html)

## Functions

### createPredicates

* createPredicates(filters: [PerfGroupFilters](src_core_perf_config_interface.html#PerfGroupFilters)): [PerfPredicates](src_core_perf_config_interface.html#PerfPredicates)

* + Defined in [src/core/perf/config/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/index.ts#L43)

  Creates filter predicates for every group

  #### Parameters

  + ##### filters: [PerfGroupFilters](src_core_perf_config_interface.html#PerfGroupFilters)

    filters from the performance config

  #### Returns [PerfPredicates](src_core_perf_config_interface.html#PerfPredicates)

### getTimerEngine

* getTimerEngine(config: [PerfTimerConfig](../interfaces/src_core_perf_config_interface.PerfTimerConfig.html)): [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html)

* + Defined in [src/core/perf/config/index.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/index.ts#L35)

  Returns an instance of the timer engine that defined in the performance config

  #### Parameters

  + ##### config: [PerfTimerConfig](../interfaces/src_core_perf_config_interface.PerfTimerConfig.html)

    performance config

  #### Returns [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html)

### mergeConfigs

* mergeConfigs(baseConfig: [PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html), ...configs: Partial<[PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)>[]): [PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)

* + Defined in [src/core/perf/config/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/index.ts#L70)

  Combines the passed configs together

  #### Parameters

  + ##### baseConfig: [PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)

    base config, that has all required fields
  + ##### Rest ...configs: Partial<[PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)>[]

    additional configs, that override fields of the base one

  #### Returns [PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)