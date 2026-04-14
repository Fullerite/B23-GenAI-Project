# Interface PerfTimerFactory
A factory to create performance timers

### Hierarchy

* PerfTimerFactory

## Index

### Methods

* [getScopedTimer](src_core_perf_timer_interface.PerfTimerFactory.html#getScopedTimer)
* [getTimer](src_core_perf_timer_interface.PerfTimerFactory.html#getTimer)

## Methods

### getScopedTimer

* getScopedTimer(group: "network" | "components" | "tools" | "manual", scope: string): [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

* + Defined in [src/core/perf/timer/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/interface.ts#L41)

  Returns an instance of the scoped performance timer for a specific group.
  The scoped timer is a timer that measures timestamps from the moment of the first scope using.
  This moment is called the time origin.

  example
  :   ```
      // The 'handlers' scope is created at this moment  
      const timer = factory.getScopedTimer('manual', 'handlers');  
        
      // <some code>  
        
      // Uses the previous timer origin  
      const anotherTimer = factory.getScopedTimer('manual', 'handlers');
      ```

  #### Parameters

  + ##### group: "network" | "components" | "tools" | "manual"

    group name, that timer should belong to. It appears at the beginning of all time marks namespaces.
  + ##### scope: string

    scope name, that defines the scope. It doesn't appear in any time mark namespaces.

  #### Returns [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

### getTimer

* getTimer(group: "network" | "components" | "tools" | "manual"): [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)

* + Defined in [src/core/perf/timer/interface.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/perf/timer/interface.ts#L20)

  Returns an instance of the performance timer for a specific group

  #### Parameters

  + ##### group: "network" | "components" | "tools" | "manual"

    group name, that timer should belong to. It appears at the beginning of all time marks namespaces.

  #### Returns [PerfTimer](src_core_perf_timer_impl_interface.PerfTimer.html)