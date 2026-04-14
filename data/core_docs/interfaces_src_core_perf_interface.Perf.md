# Interface Perf
### Hierarchy

* Perf

## Index

### Methods

* [getScopedTimer](src_core_perf_interface.Perf.html#getScopedTimer)
* [getTimer](src_core_perf_interface.Perf.html#getTimer)

## Methods

### getScopedTimer

* getScopedTimer(group: "network" | "components" | "tools" | "manual", scope: string): [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

* + Defined in [src/core/perf/interface.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/perf/interface.ts#L33)

  Returns an instance of the scoped performance timer for a specific group

  see
  :   [PerfTimerFactory.getScopedTimer](src_core_perf_timer_interface.PerfTimerFactory.html#getScopedTimer)

  #### Parameters

  + ##### group: "network" | "components" | "tools" | "manual"

    group name, that timer should belong to. It appears at the beginning of all time marks namespaces.
  + ##### scope: string

    scope name, that defines the scope. It doesn't appear in any time mark namespaces.

  #### Returns [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

### getTimer

* getTimer(group: "network" | "components" | "tools" | "manual"): [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

* + Defined in [src/core/perf/interface.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/perf/interface.ts#L24)

  Returns an instance of the performance timer for a specific group

  see
  :   [PerfTimerFactory.getTimer](src_core_perf_timer_interface.PerfTimerFactory.html#getTimer)

  #### Parameters

  + ##### group: "network" | "components" | "tools" | "manual"

    group name, that timer should belong to. It appears at the beginning of all time marks namespaces.

  #### Returns [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)