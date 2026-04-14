# Module src/core/async/modules/events/interface
## Index

### Interfaces

* [AsyncOnOptions](../interfaces/src_core_async_modules_events_interface.AsyncOnOptions.html)
* [AsyncOnceOptions](../interfaces/src_core_async_modules_events_interface.AsyncOnceOptions.html)
* [AsyncPromisifyOnceOptions](../interfaces/src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html)
* [Event](../interfaces/src_core_async_modules_events_interface.Event.html)
* [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html)

### Type aliases

* [EmitLikeEvents](src_core_async_modules_events_interface.html#EmitLikeEvents)
* [EventEmitterLikeP](src_core_async_modules_events_interface.html#EventEmitterLikeP)
* [EventId](src_core_async_modules_events_interface.html#EventId)

## Type aliases

### EmitLikeEvents

EmitLikeEvents: "emit" | "fire" | "dispatch" | "dispatchEvent"

* Defined in [src/core/async/modules/events/interface.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L24)

### EventEmitterLikeP

EventEmitterLikeP: ((event: string, handler: Function) => [CanUndef](index.html#CanUndef)<Function>) | [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html)

* Defined in [src/core/async/modules/events/interface.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L52)

Extended type of event emitter

### EventId

EventId: [CanArray](index.html#CanArray)<[IdObject](../interfaces/src_core_async_modules_base_interface.IdObject.html)>

* Defined in [src/core/async/modules/events/interface.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L22)