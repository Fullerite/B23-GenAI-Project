# Module src/core/event
[# core/event](#coreevent)

This module provides a bunch of helper functions to handle events in more flexibly way.

[## resolveAfterEvents](#resolveafterevents)

The function returns a promise that will be resolved after emitting of all events from the specified emitter.

```
import { EventEmitter2 as EventEmitter } from 'eventemitter2';  
import { resolveAfterEvents } from 'core/event';  
  
const  
  emitter = new EventEmitter();  
  
resolveAfterEvents(emitter, 'foo', 'bar')  
  .then(() => console.log('Bang!'));  
  
emitter.emit('foo');  
emitter.emit('bar');
```

[## createsAsyncSemaphore](#createsasyncsemaphore)

The function wraps a callback into a new function that never calls the target until all specified flags are resolved.
`createsAsyncSemaphore` returns a new function that takes a string flag and resolves it.
After all, flags are resolved, the last function invokes the target function.
If you try to invoke the function after the first time resolving, ii won't be executed.

```
import { EventEmitter2 as EventEmitter } from 'eventemitter2';  
import { createsAsyncSemaphore } from 'core/event';  
  
const semaphore = createsAsyncSemaphore(() => {  
  console.log('Boom!');  
}, 'foo', 'bar');  
  
semaphore('foo');  
semaphore('bar') // Boom!
```

## Index

### Variables

* [afterEvents](src_core_event.html#afterEvents)
* [createSyncPromise](src_core_event.html#createSyncPromise)
* [onEverythingReady](src_core_event.html#onEverythingReady)

### Functions

* [createsAsyncSemaphore](src_core_event.html#createsAsyncSemaphore)
* [resolveAfterEvents](src_core_event.html#resolveAfterEvents)

## Variables

### Const afterEvents

afterEvents: [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<[emitter: [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html), cb: string | Function, ...events: string[]], Promise<void>> = ...

* Defined in [src/core/event/index.ts:129](https://github.com/V4Fire/Core/blob/master/src/core/event/index.ts#L129)

deprecated

see
:   [resolveAfterEvents](src_core_event.html#resolveAfterEvents)

### Const createSyncPromise

createSyncPromise: [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<[resolveValue?: unknown, rejectValue?: unknown], Promise<unknown>> = ...

* Defined in [src/core/event/index.ts:154](https://github.com/V4Fire/Core/blob/master/src/core/event/index.ts#L154)

Creates a synchronous promise wrapper for the specified value

deprecated

see
:   [SyncPromise](src_core_prelude_structures.html#SyncPromise)

param resolveValue

param rejectValue

### Const onEverythingReady

onEverythingReady: [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<[cb: () => unknown, ...flags: string[]], (flag: string) => void> = ...

* Defined in [src/core/event/index.ts:115](https://github.com/V4Fire/Core/blob/master/src/core/event/index.ts#L115)

deprecated

see
:   [createsAsyncSemaphore](src_core_event.html#createsAsyncSemaphore)

## Functions

### createsAsyncSemaphore

* createsAsyncSemaphore<T>(cb: () => T, ...flags: string[]): (flag: string) => [CanUndef](index.html#CanUndef)<T>

* + Defined in [src/core/event/index.ts:78](https://github.com/V4Fire/Core/blob/master/src/core/event/index.ts#L78)

  Wraps a callback into a new function that never calls the target until all specified flags are resolved.
  The function returns a new function that takes a string flag and resolves it.
  After all, flags are resolved, the last function invokes the target function.
  If you try to invoke the function after the first time resolving, ii won't be executed.

  example
  :   ```
      const semaphore = createsAsyncSemaphore(() => {  
        console.log('Boom!');  
      }, 'foo', 'bar');  
        
      semaphore('foo');  
      semaphore('bar'); // 'Boom!'  
        
      // Function already resolved, the target function isn't executed  
      semaphore();
      ```

  #### Type parameters

  + #### T

  #### Parameters

  + ##### cb: () => T

    callback function that is invoked after resolving all flags

    - * (): T
      * #### Returns T
  + ##### Rest ...flags: string[]

    flags to resolve

  #### Returns (flag: string) => [CanUndef](index.html#CanUndef)<T>

  + - (flag: string): [CanUndef](index.html#CanUndef)<T>
    - Wraps a callback into a new function that never calls the target until all specified flags are resolved.
      The function returns a new function that takes a string flag and resolves it.
      After all, flags are resolved, the last function invokes the target function.
      If you try to invoke the function after the first time resolving, ii won't be executed.

      example
      :   ```
          const semaphore = createsAsyncSemaphore(() => {  
            console.log('Boom!');  
          }, 'foo', 'bar');  
            
          semaphore('foo');  
          semaphore('bar'); // 'Boom!'  
            
          // Function already resolved, the target function isn't executed  
          semaphore();
          ```

      #### Parameters

      * ##### flag: string

      #### Returns [CanUndef](index.html#CanUndef)<T>

### resolveAfterEvents

* resolveAfterEvents(emitter: [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html), ...events: string[]): Promise<void>

* + Defined in [src/core/event/index.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/event/index.ts#L32)

  Returns a promise that will be resolved after emitting of all events from the specified emitter

  example
  :   ```
      // The promise will be resolved after two window events  
      resolveAfterEvents(window, 'resize', 'scroll').then(() => {  
        console.log('Boom!');  
      });
      ```

  #### Parameters

  + ##### emitter: [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html)
  + ##### Rest ...events: string[]

    events to listen

  #### Returns Promise<void>