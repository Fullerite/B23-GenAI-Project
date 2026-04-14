# Interface Event<E>
Event object

### Type parameters

* #### E: [EventEmitterLikeP](../modules/src_core_async_modules_events_interface.html#EventEmitterLikeP) = [EventEmitterLikeP](../modules/src_core_async_modules_events_interface.html#EventEmitterLikeP)

### Hierarchy

* Event

## Index

### Properties

* [args](src_core_async_modules_events_interface.Event.html#args)
* [emitter](src_core_async_modules_events_interface.Event.html#emitter)
* [event](src_core_async_modules_events_interface.Event.html#event)
* [handler](src_core_async_modules_events_interface.Event.html#handler)

## Properties

### args

args: unknown[]

* Defined in [src/core/async/modules/events/interface.ts:106](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L106)

Additional arguments for the emitter

### emitter

emitter: E

* Defined in [src/core/async/modules/events/interface.ts:91](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L91)

Event emitter

### event

event: string

* Defined in [src/core/async/modules/events/interface.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L96)

Event name

### handler

handler: Function | ((this: [default](../classes/src_core_async.default.html)<[default](../classes/src_core_async.default.html)<any>>, e: unknown) => unknown)

* Defined in [src/core/async/modules/events/interface.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/events/interface.ts#L101)

Event handler