# Module src/core/perf/timer/engines
[# core/perf/timer/engines](#coreperftimerengines)

This module contains the engines that send time metrics to a target destination.

[## Overview](#overview)

Each engine has to implement the `PerfTimerEngine` interface. It means that an engine should have the following methods:

* `sendDelta` - to send metrics data
* `getTimestampFromTimeOrigin` - returns a timestamp from the application start. In the simple example, it could be
  `performance.now()`, but the engine can define the precision and the moment the application starts.

## Index

### References

* [PerfTimerEngine](src_core_perf_timer_engines.html#PerfTimerEngine)
* [PerfTimerEngineName](src_core_perf_timer_engines.html#PerfTimerEngineName)

### Variables

* [default](src_core_perf_timer_engines.html#default)

## References

### PerfTimerEngine

Re-exports [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html)

### PerfTimerEngineName

Re-exports [PerfTimerEngineName](src_core_perf_timer_engines_interface.html#PerfTimerEngineName)

## Variables

### Const default

default: { console: [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html) } = ...

* Defined in [src/core/perf/timer/engines/index.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/engines/index.ts#L18)

#### Type declaration

* ##### console: [PerfTimerEngine](../interfaces/src_core_perf_timer_engines_interface.PerfTimerEngine.html)