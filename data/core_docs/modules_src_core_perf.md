# Module src/core/perf
[# core/perf](#coreperf)

This module provides API to send performance metrics.

[## Usage](#usage)

```
import perf from 'core/perf';  
  
const timer = perf.getTimer('network').namespace('auth');  
  
// Duration of the `loginUser` request  
  
const  
  timerId = timer.start('login'),  
  user = await loginUser(credential);  
  
timer.finish(timerId, {email: user.email});  
  
// A reference point in time for the following measurements  
const scopedTimer = perf.getScopedTimer('component').namespace('index-page');  
  
// A component was created  
scopedTimer.markTimestamp('created');  
  
// A component was mounted  
scopedTimer.markTimestamp('mounted');
```

[## Configuration](#configuration)

There are two ways to use this module: with a custom configuration or default one.

[### Default configuration](#default-configuration)

The default module export refers to a performance metrics factory configured using the runtime config from `src/config`.
To configure it, define a `perf` property within your config file.

**config**

```
import { extend } from '@v4fire/core/config';  
  
extend({  
  perf: {  
    timer: {  
      engine: 'console',  
      filters: {  
        network: ['login'],  
  
        localDB: {  
          include: ['load', 'unload']  
        },  
  
        components: {  
          exclude: ['mount']  
        }  
      }  
    }  
  }  
})
```

**some-file.ts**

```
import perf from 'core/perf';  
  
const  
  timer = perf.getTimer('network').namespace('auth'),  
  timerId = timer.start('login');  
  
// ..  
  
timer.finish(timerId);
```

[#### Configuration interface](#configuration-interface)

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

[### Custom configuration](#custom-configuration)

There is a possibility to create a performance metrics factory with a custom configuration. It allows having several
differently configured performance metrics factories at the same time.

This is achieved using the `perf` method, which acquires a new config as the first argument.

```
import { perf as factory } from 'core/perf';  
  
const perf = factory({  
  timer: {  
    engine: 'console',  
    filters: {  
      network: {  
        include: ['login']  
      }  
    }  
  }  
});  
  
const  
  timer = perf.getTimer('network').namespace('auth'),  
  timerId = timer.start('login');  
  
// ..  
  
timer.finish(timerId);
```

[## Time metrics](#time-metrics)

Currently, the module supports only the time metrics [core/perf/timer](src_core_perf_timer.html).

## Index

### References

* [Perf](src_core_perf.html#Perf)
* [PerfGroup](src_core_perf.html#PerfGroup)
* [PerfTimer](src_core_perf.html#PerfTimer)
* [PerfTimerId](src_core_perf.html#PerfTimerId)
* [PerfTimerMeasurement](src_core_perf.html#PerfTimerMeasurement)
* [PerfTimersRunnerOptions](src_core_perf.html#PerfTimersRunnerOptions)

### Variables

* [default](src_core_perf.html#default)

### Functions

* [perf](src_core_perf.html#perf)

## References

### Perf

Re-exports [Perf](../interfaces/src_core_perf_interface.Perf.html)

### PerfGroup

Re-exports [PerfGroup](src_core_perf_interface.html#PerfGroup)

### PerfTimer

Re-exports [PerfTimer](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html)

### PerfTimerId

Re-exports [PerfTimerId](src_core_perf_timer_impl_interface.html#PerfTimerId)

### PerfTimerMeasurement

Re-exports [PerfTimerMeasurement](../interfaces/src_core_perf_timer_impl_interface.PerfTimerMeasurement.html)

### PerfTimersRunnerOptions

Re-exports [PerfTimersRunnerOptions](../interfaces/src_core_perf_timer_impl_interface.PerfTimersRunnerOptions.html)

## Variables

### Const default

default: [Perf](../interfaces/src_core_perf_interface.Perf.html) = ...

* Defined in [src/core/perf/index.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/perf/index.ts#L39)

## Functions

### perf

* perf(perfConfig?: Partial<[PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)>): [Perf](../interfaces/src_core_perf_interface.Perf.html)

* + Defined in [src/core/perf/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/perf/index.ts#L28)

  Returns a configured instance of the `Perf` class

  #### Parameters

  + ##### Optional perfConfig: Partial<[PerfConfig](../interfaces/src_core_perf_config_interface.PerfConfig.html)>

  #### Returns [Perf](../interfaces/src_core_perf_interface.Perf.html)