# Module src/core/perf/timer
[# core/perf/timer](#coreperftimer)

This module provides an implementation of the performance timer API.
It allows calculating and sending time metrics.

[## Overview](#overview)

The module consists of several abstractions:

* engines - actually send metrics data to the specific destination
* a performance timer - has methods to capture a specific time moment and calculate the difference between them
* a timers' runner - combines previous abstractions together and makes them work
* a timers' factory - using the runner creates timers

[## Factory](#factory)

The timers' factory is created using `getTimerFactory` function. The function acquires timers' config as the first
argument. It means that there could be several timers' factories with different configurations simultaneously.

```
import { getTimerFactory } from 'core/perf/timer';  
  
const someFactory = getTimerFactory(generalConfig);  
const anotherFactory = getTimerFactory(specificConfig);
```

[### Methods](#methods)

Each factory has the following methods: `getTimer`, `getScopedTimer`. These methods are entry points to work with timers.
Each of them uses runners inside to create a timer and return it. Also, the methods create a runner for passed arguments
only once and then use the same runner for the next call with the same arguments.

These methods are called from the main `perf` object, so there is no need to create the timers' factory directly.
The following examples imply that a factory has already created and use it only for educational purpose.

[### Regular timer](#regular-timer)

```
const timer = factory.getTimer('manual');
```

This method returns a regular timer that starts time measurement from
[the time origin](https://developer.mozilla.org/en-US/docs/Web/API/DOMHighResTimeStamp#the_time_origin).

**Duration measurement**

```
const timer = perf.getTimer('network').namespace('auth');  
  
// Duration of the `loginUser` request  
const loginTimerId = timer.start('login');  
const user = await loginUser(credential);  
timer.finish(loginTimerId);  
  
// Duration of the `logoutUser` request  
const logoutTimerId = timer.start('logout');  
await logoutUser(user);  
  
// It's possible to send additional data when finishing measurement  
timer.finish(logoutTimerId, {email: user.email});
```

**Time marks from the time origin**

```
const timer = perf.getTimer('components').namespace('index-page');  
  
// A page was created  
scopedTimer.markTimestamp('created');  
  
// A page was mounted  
// It's possible to send additional data with timestamp  
scopedTimer.markTimestamp('mounted', {id: data.id});
```

Using the same factory in different files and calling `getTimer` method with the same arguments guarantees that inside
it will be used the same instance of the timers' runner. But the method returns different instances of the performance
timer itself.

**file1.ts**

```
const timer = factory.getTimer('components');
```

**file2.ts**

```
// A different timer from the same runner  
const timer = factory.getTimer('components');
```

[### Scoped timer](#scoped-timer)

```
const timer = factory.getScopedTimer('network', 'old-api');
```

This method returns a scoped timer that starts time measurement from the moment its runner was created.
Timers from `getTimer` and `getScopedTimer` have the same interfaces.

Since the next call of the method with the same arguments uses the already created runner, then the time origin
for the new timer will be the same as for the previously created one.

**file1.ts**

```
// A time origin for the internal runner is exact this moment — m0  
const timer = factory.getScopedTimer('tools', 'page-helpers');
```

**file2.ts**

```
// A different timer but its time origin is m0 as well  
const timer = factory.getScopedTimer('tools', 'page-helpers');
```

## Index

### References

* [PerfTimerFactory](src_core_perf_timer.html#PerfTimerFactory)

### Functions

* [getTimerFactory](src_core_perf_timer.html#getTimerFactory)

## References

### PerfTimerFactory

Re-exports [PerfTimerFactory](../interfaces/src_core_perf_timer_interface.PerfTimerFactory.html)

## Functions

### getTimerFactory

* getTimerFactory(config: [PerfTimerConfig](../interfaces/src_core_perf_config_interface.PerfTimerConfig.html)): [PerfTimerFactory](../interfaces/src_core_perf_timer_interface.PerfTimerFactory.html)

* + Defined in [src/core/perf/timer/index.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/index.ts#L27)

  Returns a timers' factory for the passed config

  #### Parameters

  + ##### config: [PerfTimerConfig](../interfaces/src_core_perf_config_interface.PerfTimerConfig.html)

    config, that the new factory will use

  #### Returns [PerfTimerFactory](../interfaces/src_core_perf_timer_interface.PerfTimerFactory.html)