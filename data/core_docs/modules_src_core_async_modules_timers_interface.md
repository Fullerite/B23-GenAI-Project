# Module src/core/async/modules/timers/interface
## Index

### Interfaces

* [AsyncIdleOptions](../interfaces/src_core_async_modules_timers_interface.AsyncIdleOptions.html)
* [AsyncRequestIdleCallbackOptions](../interfaces/src_core_async_modules_timers_interface.AsyncRequestIdleCallbackOptions.html)
* [AsyncWaitOptions](../interfaces/src_core_async_modules_timers_interface.AsyncWaitOptions.html)

### Type aliases

* [IdleCb](src_core_async_modules_timers_interface.html#IdleCb)
* [TimerId](src_core_async_modules_timers_interface.html#TimerId)

## Type aliases

### IdleCb

IdleCb<R, CTX>: [ProxyCb](src_core_async_modules_base_interface.html#ProxyCb)<IdleDeadline, R, CTX>

* Defined in [src/core/async/modules/timers/interface.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/timers/interface.ts#L35)

#### Type parameters

* #### R = unknown
* #### CTX: object = [default](../classes/src_core_async.default.html)

### TimerId

TimerId: number | [IdObject](../interfaces/src_core_async_modules_base_interface.IdObject.html)

* Defined in [src/core/async/modules/timers/interface.ts:12](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/timers/interface.ts#L12)