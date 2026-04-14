# Interface OnlineCheckConfig
### Hierarchy

* OnlineCheckConfig

## Index

### Properties

* [cacheTTL](src_core_net_interface.OnlineCheckConfig.html#cacheTTL)
* [checkInterval](src_core_net_interface.OnlineCheckConfig.html#checkInterval)
* [checkTimeout](src_core_net_interface.OnlineCheckConfig.html#checkTimeout)
* [checkURL](src_core_net_interface.OnlineCheckConfig.html#checkURL)
* [lastDateSyncInterval](src_core_net_interface.OnlineCheckConfig.html#lastDateSyncInterval)
* [persistence](src_core_net_interface.OnlineCheckConfig.html#persistence)
* [retryCount](src_core_net_interface.OnlineCheckConfig.html#retryCount)

## Properties

### Optional cacheTTL

cacheTTL?: number

* Defined in [src/core/net/interface.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L60)

How long to store a checking result in the local cache

### Optional checkInterval

checkInterval?: number

* Defined in [src/core/net/interface.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L35)

How often need to check the online connection (ms)

### Optional checkTimeout

checkTimeout?: number

* Defined in [src/core/net/interface.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L40)

Timeout of a connection checking request

### Optional checkURL

checkURL?: [CanUndef](../modules/index.html#CanUndef)<string>

* Defined in [src/core/net/interface.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L30)

URL to check the online connection
(with the "browser.request" engine can be used only image URL-s)

### Optional lastDateSyncInterval

lastDateSyncInterval?: number

* Defined in [src/core/net/interface.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L50)

How often to update the last online connection time

### Optional persistence

persistence?: boolean

* Defined in [src/core/net/interface.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L55)

True, if we need to save a time of the last online connection in the local cache

### Optional retryCount

retryCount?: number

* Defined in [src/core/net/interface.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/net/interface.ts#L45)

The maximum number of retries to check the online connection