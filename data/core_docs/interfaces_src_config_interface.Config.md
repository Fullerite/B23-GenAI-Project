# Interface Config
### Hierarchy

* Config

## Index

### Properties

* [api](src_config_interface.Config.html#api)
* [appName](src_config_interface.Config.html#appName)
* [locale](src_config_interface.Config.html#locale)
* [log](src_config_interface.Config.html#log)
* [online](src_config_interface.Config.html#online)
* [perf](src_config_interface.Config.html#perf)

## Properties

### api

api: [CanUndef](../modules/index.html#CanUndef)<string>

* Defined in [src/config/interface.ts:28](https://github.com/V4Fire/Core/blob/master/src/config/interface.ts#L28)

Base API URL: primary service domain

### appName

appName: [CanUndef](../modules/index.html#CanUndef)<string>

* Defined in [src/config/interface.ts:17](https://github.com/V4Fire/Core/blob/master/src/config/interface.ts#L17)

Base application name

### locale

locale: [CanUndef](../modules/index.html#CanUndef)<[Language](../modules/index.html#Language)>

* Defined in [src/config/interface.ts:23](https://github.com/V4Fire/Core/blob/master/src/config/interface.ts#L23)

Default system locale
(used for internalizing)

### log

log: [LogConfig](src_core_log_config_interface.LogConfig.html)

* Defined in [src/config/interface.ts:33](https://github.com/V4Fire/Core/blob/master/src/config/interface.ts#L33)

Options for the "core/log" module

### online

online: [OnlineCheckConfig](src_core_net_interface.OnlineCheckConfig.html)

* Defined in [src/config/interface.ts:43](https://github.com/V4Fire/Core/blob/master/src/config/interface.ts#L43)

Options for the "core/net" module

### perf

perf: [PerfConfig](src_core_perf_config_interface.PerfConfig.html)

* Defined in [src/config/interface.ts:38](https://github.com/V4Fire/Core/blob/master/src/config/interface.ts#L38)

Options for "core/perf" module