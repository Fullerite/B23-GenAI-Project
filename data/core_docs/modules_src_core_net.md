# Module src/core/net
[# core/net](#corenet)

This module provides API to work with a network, such as testing of the network connection, etc.

```
import * as net from 'core/net';  
  
(async () => {  
  console.log(await net.isOnline());  
})();
```

[## Configuration](#configuration)

To enable online checking you need to add a configuration within your runtime config module (`src/config`).

**config**

```
import { extend } from '@v4fire/core/config';  
  
extend({  
  online: {  
    // URL to check the online connection  
    // (with the "browser.request" engine can be used only image URL-s)  
    checkURL: 'https://google.com/favicon.ico',  
  
    // Default options:  
  
    // How often need to check the online connection (ms)  
    checkInterval: (30).seconds(),  
  
    // Timeout of a connection checking request  
    checkTimeout: (2).seconds(),  
  
    // The maximum number of retries to check the online connection  
    retryCount: 3,  
  
    // How often to update the last online connection time  
    lastDateSyncInterval: (1).minute(),  
  
    // True, if we need to save a time of the last online connection in the local cache  
    persistence: true,  
  
    // How long to store a checking result in the local cache  
    cacheTTL: (1).second()  
  }  
});
```

[## Events](#events)

| EventName | Description | Payload description | Payload |
| --- | --- | --- | --- |
| `online` | The network connection has appeared | - | - |
| `offline` | The network connection has lost | When was the last connection | `Date` |
| `status` | The network connection status has been changed | Connection status | `NetStatus` |

```
import * as net from 'core/net';  
  
net.emitter.emitter.on('online', () => {  
  console.log("I'm online!");  
});  
  
net.emitter.emitter.on('offline', (lastOnlineDate) => {  
  console.log(`I have been online at ${lastOnlineDate}`);  
});  
  
net.emitter.emitter.on('status', (e) => {  
  console.log(`Connection is ${e.status ? 'online' : 'offline'}`);  
  
  if (!e.status) {  
    console.log(`I have been online at ${e.lastOnline}`);  
  }  
});
```

[## Engines](#engines)

The module supports different implementations to check the online connection.
The implementations are placed within `core/net/engines`. By default, it uses a strategy by requesting
some recourses from the internet, like a Google favicon. But you can manually provide an engine to use.

```
import * as net from 'core/net';  
  
(async () => {  
  // Loopback. Always online.  
  console.log(await net.isOnline(async () => true));  
})();
```

## Index

### References

* [NetEngine](src_core_net.html#NetEngine)
* [NetState](src_core_net.html#NetState)
* [NetStatus](src_core_net.html#NetStatus)
* [OnlineCheckConfig](src_core_net.html#OnlineCheckConfig)
* [emitter](src_core_net.html#emitter)
* [event](src_core_net.html#event)
* [state](src_core_net.html#state)

### Functions

* [isOnline](src_core_net.html#isOnline)
* [syncStatusWithStorage](src_core_net.html#syncStatusWithStorage)
* [updateStatus](src_core_net.html#updateStatus)

## References

### NetEngine

Re-exports [NetEngine](../interfaces/src_core_net_interface.NetEngine.html)

### NetState

Re-exports [NetState](src_core_net_interface.html#NetState)

### NetStatus

Re-exports [NetStatus](../interfaces/src_core_net_interface.NetStatus.html)

### OnlineCheckConfig

Re-exports [OnlineCheckConfig](../interfaces/src_core_net_interface.OnlineCheckConfig.html)

### emitter

Re-exports [emitter](src_core_net_const.html#emitter)

### event

Re-exports [event](src_core_net_const.html#event)

### state

Re-exports [state](src_core_net_const.html#state)

## Functions

### isOnline

* isOnline(engine?: [NetEngine](../interfaces/src_core_net_interface.NetEngine.html)): Promise<[NetStatus](../interfaces/src_core_net_interface.NetStatus.html)>

* + Defined in [src/core/net/index.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/net/index.ts#L46)

  Returns information about the internet connection status

  emits
  :   `online()`

  emits
  :   `offline(lastOnline: Date)`

  emits
  :   `status(value:` [NetStatus](src_core_net.html#NetStatus) `)`

  #### Parameters

  + ##### engine: [NetEngine](../interfaces/src_core_net_interface.NetEngine.html) = netEngine

  #### Returns Promise<[NetStatus](../interfaces/src_core_net_interface.NetStatus.html)>

### syncStatusWithStorage

* syncStatusWithStorage(): Promise<void>

* + Defined in [src/core/net/index.ts:124](https://github.com/V4Fire/Core/blob/master/src/core/net/index.ts#L124)

  Synchronizes the online status with a local storage

  #### Returns Promise<void>

### updateStatus

* updateStatus(): Promise<void>

* + Defined in [src/core/net/index.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/net/index.ts#L169)

  Updates the online status

  #### Returns Promise<void>