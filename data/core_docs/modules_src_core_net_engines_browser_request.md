# Module src/core/net/engines/browser-request
## Index

### Functions

* [isOnline](src_core_net_engines_browser_request.html#isOnline)

## Functions

### isOnline

* isOnline(): Promise<boolean | null>

* + Defined in [src/core/net/engines/browser-request.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/net/engines/browser-request.ts#L24)

  Returns true if the current host has a connection to the internet or null
  if the connection status can't be checked.

  This engine checks the connection by using a request for some data from the internet.

  #### Returns Promise<boolean | null>