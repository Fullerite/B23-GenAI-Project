# Interface PerfIncludeFilter
Include/exclude patterns for perf filters

### Hierarchy

* PerfIncludeFilter

## Index

### Properties

* [exclude](src_core_perf_config_interface.PerfIncludeFilter.html#exclude)
* [include](src_core_perf_config_interface.PerfIncludeFilter.html#include)

## Properties

### Optional exclude

exclude?: string[]

* Defined in [src/core/perf/config/interface.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/interface.ts#L57)

Exclude only specific events.
If `include` and `exclude` are both presented, will be used only include.

### Optional include

include?: string[]

* Defined in [src/core/perf/config/interface.ts:51](https://github.com/V4Fire/Core/blob/master/src/core/perf/config/interface.ts#L51)

Include only specific events