# Module src/core/perf/timer/impl
[# core/perf/timer/impl](#coreperftimerimpl)

This module contains a runner implementation for performance timers.

[## Overview](#overview)

The runner is the actual thing that measures the difference between time moments.
It can create performance timers that are just proxies that execute measurement methods of the runner they created.
The main responsibility of timers is to store the whole namespace of current metrics to make them easy to use.

[## Runner](#runner)
[### Constructor](#constructor)

The `PerfTimersRunner` class has several parameters in its constructor:

* `engine` - the most important argument is `PerfTimerEngine` instance. It is **required**.
* `filter` - predicate to filter metrics. If it returns `false`, the metrics won't be sent anywhere.
* `keepTImeOffset` - the runner becomes a scoped one. All new timestamps measure from the moment the runner was created.

A simple runner:

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const runner = new PerfTimersRunner(engines.console);
```

A scoped runner:

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const scopedRunner = new PerfTimersRunner(engines.console, {withCurrentTimeOrigin: true});
```

A runner with filtering:

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const filterPredicate = (ns: string) => ns.startsWith('network');  
  
// Only metrics which namespace starts with 'network' will be printed in the console  
const runner = new PerfTimersRunner(engines.console, {filter: filterPredicate});
```

[### Methods](#methods)

The class has only one public method `createTimer` that returns an instance of performance timer.

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const runner = new PerfTimersRunner(engines.console);  
const timer = runner.createTimer('network');
```

Some protected methods are used by performance timer instances.

[## Timer](#timer)

A performance timer is used to make time measurements.

After its creation, the timer has only a group name. The timer stores the whole namespace inside.
When new metrics are created, the timer's namespace prepends to metrics name, forming the full name of the metrics.

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const runner = new PerfTimersRunner(engines.console);  
  
// Timer's namespace at this point is "network"  
const timer = runner.createTimer('network');  
  
// Here time metrics are created, and its full name is "network.auth"  
const timerId = timer.start('auth');
```

[### Methods](#methods-1)

The performance timer has several methods to measure and one method to define a namespace.

[#### Namespace](#namespace)

Returns a new performance timer instance with the updated namespace.

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const  
  runner = new PerfTimersRunner(engines.console),  
  timer = runner.createTimer('network');  
  
// The timer namespace is "network.auth"  
const timerNs = timer.namespace('auth');  
  
// The full metrics name is "network.auth.login"  
const timerId = timerNs.start('login');
```

[#### Local measurement](#local-measurement)

Two methods `start` and `finish` are designed for local measurements.
Method `start` marks the beginning of measurement and returns a timer identifier to finish the measurement.

The advantage of this approach is that there could be a number of concurrent measurements with the same name,
and none of them will affect each other since every timer identifier is unique.

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const  
  runner = new PerfTimersRunner(engines.console),  
  timer = runner.createTimer('network').namespace('auth');  
  
const timerId = timer.start('login');  
  
await login(credentials);  
  
timer.finish(timerId);
```

The `finish` method also acquires some additional information for the metrics as a second parameter.
This kind of measurement is not affected by the runner's time origin because it measures the time difference between two moments.

[#### Time marks](#time-marks)

Also, there is a possibility to measure time from the runner's time origin with `markTimestamp` method.

```
import { PerfTimersRunner } from 'core/perf/timer/impl'  
import engines from 'core/perf/timer/engines';  
  
const  
  runner = new PerfTimersRunner(engines.console),  
  timer = runner.createTimer('components').namespace('button');  
  
// Some code  
timer.markTimestamp('created');  
  
// Another code  
timer.markTimestamp('mounted');
```

This method measures time from the runner's time origin to the moment the method was called.
It is possible to pass additional data as the second argument to the method.

## Index

### References

* [PerfTimer](src_core_perf_timer_impl.html#PerfTimer)
* [PerfTimerId](src_core_perf_timer_impl.html#PerfTimerId)
* [PerfTimerMeasurement](src_core_perf_timer_impl.html#PerfTimerMeasurement)
* [PerfTimersRunner](src_core_perf_timer_impl.html#PerfTimersRunner)
* [PerfTimersRunnerOptions](src_core_perf_timer_impl.html#PerfTimersRunnerOptions)

## References

### PerfTimer

Re-exports [PerfTimer](../interfaces/src_core_perf_timer_impl_interface.PerfTimer.html)

### PerfTimerId

Re-exports [PerfTimerId](src_core_perf_timer_impl_interface.html#PerfTimerId)

### PerfTimerMeasurement

Re-exports [PerfTimerMeasurement](../interfaces/src_core_perf_timer_impl_interface.PerfTimerMeasurement.html)

### PerfTimersRunner

Renames and re-exports [default](../classes/src_core_perf_timer_impl_runner.default.html)

### PerfTimersRunnerOptions

Re-exports [PerfTimersRunnerOptions](../interfaces/src_core_perf_timer_impl_interface.PerfTimersRunnerOptions.html)