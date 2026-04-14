# Module src/core/async/modules/events
[# core/async/modules/events](#coreasyncmodulesevents)

This module provides Async wrappers for event emitters.

```
import Async from 'core/async';  
import { EventEmitter2 as EventEmitter } from 'eventemitter2';  
  
const  
  emitter = new EventEmitter(),  
  watcher = new Async();  
  
watcher.on(emitter, 'foo', (e) => {  
  console.log(e);  
});  
  
emitter.emit('foo', 'bar');
```

## Index

### References

* [AsyncCb](src_core_async_modules_events.html#AsyncCb)
* [AsyncCbOptions](src_core_async_modules_events.html#AsyncCbOptions)
* [AsyncCbOptionsSingle](src_core_async_modules_events.html#AsyncCbOptionsSingle)
* [AsyncIdleOptions](src_core_async_modules_events.html#AsyncIdleOptions)
* [AsyncOnOptions](src_core_async_modules_events.html#AsyncOnOptions)
* [AsyncOnceOptions](src_core_async_modules_events.html#AsyncOnceOptions)
* [AsyncOptions](src_core_async_modules_events.html#AsyncOptions)
* [AsyncOptionsForWrappers](src_core_async_modules_events.html#AsyncOptionsForWrappers)
* [AsyncPromiseOptions](src_core_async_modules_events.html#AsyncPromiseOptions)
* [AsyncPromisifyOnceOptions](src_core_async_modules_events.html#AsyncPromisifyOnceOptions)
* [AsyncProxyOptions](src_core_async_modules_events.html#AsyncProxyOptions)
* [AsyncRequestIdleCallbackOptions](src_core_async_modules_events.html#AsyncRequestIdleCallbackOptions)
* [AsyncRequestOptions](src_core_async_modules_events.html#AsyncRequestOptions)
* [AsyncWaitOptions](src_core_async_modules_events.html#AsyncWaitOptions)
* [AsyncWorkerOptions](src_core_async_modules_events.html#AsyncWorkerOptions)
* [BoundFn](src_core_async_modules_events.html#BoundFn)
* [CancelablePromise](src_core_async_modules_events.html#CancelablePromise)
* [ClearFn](src_core_async_modules_events.html#ClearFn)
* [ClearOptions](src_core_async_modules_events.html#ClearOptions)
* [ClearOptionsId](src_core_async_modules_events.html#ClearOptionsId)
* [ClearProxyOptions](src_core_async_modules_events.html#ClearProxyOptions)
* [ClearReason](src_core_async_modules_events.html#ClearReason)
* [DataProviderBodyMethodsToReplace](src_core_async_modules_events.html#DataProviderBodyMethodsToReplace)
* [DataProviderMethodsToReplace](src_core_async_modules_events.html#DataProviderMethodsToReplace)
* [DataProviderQueryMethodsToReplace](src_core_async_modules_events.html#DataProviderQueryMethodsToReplace)
* [EmitLikeEvents](src_core_async_modules_events.html#EmitLikeEvents)
* [Event](src_core_async_modules_events.html#Event)
* [EventEmitterLike](src_core_async_modules_events.html#EventEmitterLike)
* [EventEmitterLikeP](src_core_async_modules_events.html#EventEmitterLikeP)
* [EventEmitterOverwritten](src_core_async_modules_events.html#EventEmitterOverwritten)
* [EventEmitterWrapper](src_core_async_modules_events.html#EventEmitterWrapper)
* [EventId](src_core_async_modules_events.html#EventId)
* [FullAsyncOptions](src_core_async_modules_events.html#FullAsyncOptions)
* [FullClearOptions](src_core_async_modules_events.html#FullClearOptions)
* [GlobalCache](src_core_async_modules_events.html#GlobalCache)
* [Group](src_core_async_modules_events.html#Group)
* [IdObject](src_core_async_modules_events.html#IdObject)
* [IdleCb](src_core_async_modules_events.html#IdleCb)
* [Join](src_core_async_modules_events.html#Join)
* [Label](src_core_async_modules_events.html#Label)
* [LinkNames](src_core_async_modules_events.html#LinkNames)
* [LocalCache](src_core_async_modules_events.html#LocalCache)
* [MarkReason](src_core_async_modules_events.html#MarkReason)
* [Namespace](src_core_async_modules_events.html#Namespace)
* [Namespaces](src_core_async_modules_events.html#Namespaces)
* [PromiseLikeP](src_core_async_modules_events.html#PromiseLikeP)
* [ProxyCb](src_core_async_modules_events.html#ProxyCb)
* [ReadonlyEventEmitterWrapper](src_core_async_modules_events.html#ReadonlyEventEmitterWrapper)
* [StrictClearOptions](src_core_async_modules_events.html#StrictClearOptions)
* [StrictClearOptionsId](src_core_async_modules_events.html#StrictClearOptionsId)
* [Task](src_core_async_modules_events.html#Task)
* [TaskCtx](src_core_async_modules_events.html#TaskCtx)
* [TimerId](src_core_async_modules_events.html#TimerId)
* [WorkerLike](src_core_async_modules_events.html#WorkerLike)
* [WorkerLikeP](src_core_async_modules_events.html#WorkerLikeP)
* [WrappedAsyncStorage](src_core_async_modules_events.html#WrappedAsyncStorage)
* [WrappedAsyncStorageNamespace](src_core_async_modules_events.html#WrappedAsyncStorageNamespace)
* [WrappedDataProvider](src_core_async_modules_events.html#WrappedDataProvider)
* [asyncCounter](src_core_async_modules_events.html#asyncCounter)
* [isAsyncOptions](src_core_async_modules_events.html#isAsyncOptions)
* [isEvent](src_core_async_modules_events.html#isEvent)
* [isParams](src_core_async_modules_events.html#isParams)
* [isPromisifyLinkName](src_core_async_modules_events.html#isPromisifyLinkName)
* [isPromisifyNamespace](src_core_async_modules_events.html#isPromisifyNamespace)
* [isZombieGroup](src_core_async_modules_events.html#isZombieGroup)

### Classes

* [default](../classes/src_core_async_modules_events.default.html)

## References

### AsyncCb

Re-exports [AsyncCb](src_core_async_modules_base_interface.html#AsyncCb)

### AsyncCbOptions

Re-exports [AsyncCbOptions](../interfaces/src_core_async_modules_base_interface.AsyncCbOptions.html)

### AsyncCbOptionsSingle

Re-exports [AsyncCbOptionsSingle](../interfaces/src_core_async_modules_base_interface.AsyncCbOptionsSingle.html)

### AsyncIdleOptions

Re-exports [AsyncIdleOptions](../interfaces/src_core_async_modules_timers_interface.AsyncIdleOptions.html)

### AsyncOnOptions

Re-exports [AsyncOnOptions](../interfaces/src_core_async_modules_events_interface.AsyncOnOptions.html)

### AsyncOnceOptions

Re-exports [AsyncOnceOptions](../interfaces/src_core_async_modules_events_interface.AsyncOnceOptions.html)

### AsyncOptions

Re-exports [AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html)

### AsyncOptionsForWrappers

Re-exports [AsyncOptionsForWrappers](src_core_async_modules_wrappers_interface.html#AsyncOptionsForWrappers)

### AsyncPromiseOptions

Re-exports [AsyncPromiseOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncPromiseOptions.html)

### AsyncPromisifyOnceOptions

Re-exports [AsyncPromisifyOnceOptions](../interfaces/src_core_async_modules_events_interface.AsyncPromisifyOnceOptions.html)

### AsyncProxyOptions

Re-exports [AsyncProxyOptions](../interfaces/src_core_async_modules_base_interface.AsyncProxyOptions.html)

### AsyncRequestIdleCallbackOptions

Re-exports [AsyncRequestIdleCallbackOptions](../interfaces/src_core_async_modules_timers_interface.AsyncRequestIdleCallbackOptions.html)

### AsyncRequestOptions

Re-exports [AsyncRequestOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncRequestOptions.html)

### AsyncWaitOptions

Re-exports [AsyncWaitOptions](../interfaces/src_core_async_modules_timers_interface.AsyncWaitOptions.html)

### AsyncWorkerOptions

Re-exports [AsyncWorkerOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncWorkerOptions.html)

### BoundFn

Re-exports [BoundFn](../interfaces/src_core_async_modules_base_interface.BoundFn.html)

### CancelablePromise

Re-exports [CancelablePromise](../interfaces/src_core_async_modules_proxy_interface.CancelablePromise.html)

### ClearFn

Re-exports [ClearFn](../interfaces/src_core_async_modules_base_interface.ClearFn.html)

### ClearOptions

Re-exports [ClearOptions](../interfaces/src_core_async_modules_base_interface.ClearOptions.html)

### ClearOptionsId

Re-exports [ClearOptionsId](../interfaces/src_core_async_modules_base_interface.ClearOptionsId.html)

### ClearProxyOptions

Re-exports [ClearProxyOptions](../interfaces/src_core_async_modules_base_interface.ClearProxyOptions.html)

### ClearReason

Re-exports [ClearReason](src_core_async_modules_base_interface.html#ClearReason)

### DataProviderBodyMethodsToReplace

Re-exports [DataProviderBodyMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderBodyMethodsToReplace)

### DataProviderMethodsToReplace

Re-exports [DataProviderMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderMethodsToReplace)

### DataProviderQueryMethodsToReplace

Re-exports [DataProviderQueryMethodsToReplace](src_core_async_modules_wrappers_interface.html#DataProviderQueryMethodsToReplace)

### EmitLikeEvents

Re-exports [EmitLikeEvents](src_core_async_modules_events_interface.html#EmitLikeEvents)

### Event

Re-exports [Event](../interfaces/src_core_async_modules_events_interface.Event.html)

### EventEmitterLike

Re-exports [EventEmitterLike](../interfaces/src_core_async_modules_events_interface.EventEmitterLike.html)

### EventEmitterLikeP

Re-exports [EventEmitterLikeP](src_core_async_modules_events_interface.html#EventEmitterLikeP)

### EventEmitterOverwritten

Re-exports [EventEmitterOverwritten](src_core_async_modules_wrappers_interface.html#EventEmitterOverwritten)

### EventEmitterWrapper

Re-exports [EventEmitterWrapper](../interfaces/src_core_async_modules_wrappers_interface.EventEmitterWrapper.html)

### EventId

Re-exports [EventId](src_core_async_modules_events_interface.html#EventId)

### FullAsyncOptions

Re-exports [FullAsyncOptions](src_core_async_interface.html#FullAsyncOptions)

### FullClearOptions

Re-exports [FullClearOptions](../interfaces/src_core_async_interface.FullClearOptions.html)

### GlobalCache

Re-exports [GlobalCache](../interfaces/src_core_async_modules_base_interface.GlobalCache.html)

### Group

Re-exports [Group](src_core_async_modules_base_interface.html#Group)

### IdObject

Re-exports [IdObject](../interfaces/src_core_async_modules_base_interface.IdObject.html)

### IdleCb

Re-exports [IdleCb](src_core_async_modules_timers_interface.html#IdleCb)

### Join

Re-exports [Join](src_core_async_modules_base_interface.html#Join)

### Label

Re-exports [Label](src_core_async_modules_base_interface.html#Label)

### LinkNames

Renames and re-exports [Namespaces](../enums/src_core_async_interface.Namespaces.html)

### LocalCache

Re-exports [LocalCache](../interfaces/src_core_async_modules_base_interface.LocalCache.html)

### MarkReason

Re-exports [MarkReason](src_core_async_modules_base_interface.html#MarkReason)

### Namespace

Re-exports [Namespace](src_core_async_interface.html#Namespace)

### Namespaces

Re-exports [Namespaces](../enums/src_core_async_interface.Namespaces.html)

### PromiseLikeP

Re-exports [PromiseLikeP](src_core_async_modules_proxy_interface.html#PromiseLikeP)

### ProxyCb

Re-exports [ProxyCb](src_core_async_modules_base_interface.html#ProxyCb)

### ReadonlyEventEmitterWrapper

Re-exports [ReadonlyEventEmitterWrapper](../interfaces/src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html)

### StrictClearOptions

Re-exports [StrictClearOptions](src_core_async_modules_base_interface.html#StrictClearOptions)

### StrictClearOptionsId

Re-exports [StrictClearOptionsId](src_core_async_modules_base_interface.html#StrictClearOptionsId)

### Task

Re-exports [Task](../interfaces/src_core_async_modules_base_interface.Task.html)

### TaskCtx

Re-exports [TaskCtx](src_core_async_modules_base_interface.html#TaskCtx)

### TimerId

Re-exports [TimerId](src_core_async_modules_timers_interface.html#TimerId)

### WorkerLike

Re-exports [WorkerLike](../interfaces/src_core_async_modules_proxy_interface.WorkerLike.html)

### WorkerLikeP

Re-exports [WorkerLikeP](src_core_async_modules_proxy_interface.html#WorkerLikeP)

### WrappedAsyncStorage

Re-exports [WrappedAsyncStorage](../interfaces/src_core_async_modules_wrappers_interface.WrappedAsyncStorage.html)

### WrappedAsyncStorageNamespace

Re-exports [WrappedAsyncStorageNamespace](../interfaces/src_core_async_modules_wrappers_interface.WrappedAsyncStorageNamespace.html)

### WrappedDataProvider

Re-exports [WrappedDataProvider](src_core_async_modules_wrappers_interface.html#WrappedDataProvider)

### asyncCounter

Re-exports [asyncCounter](src_core_async_modules_base_const.html#asyncCounter)

### isAsyncOptions

Re-exports [isAsyncOptions](src_core_async_modules_base_helpers.html#isAsyncOptions)

### isEvent

Re-exports [isEvent](src_core_async_modules_events_helpers.html#isEvent)

### isParams

Re-exports [isParams](src_core_async_modules_base_helpers.html#isParams)

### isPromisifyLinkName

Re-exports [isPromisifyLinkName](src_core_async_modules_base_const.html#isPromisifyLinkName)

### isPromisifyNamespace

Re-exports [isPromisifyNamespace](src_core_async_modules_base_const.html#isPromisifyNamespace)

### isZombieGroup

Re-exports [isZombieGroup](src_core_async_modules_base_const.html#isZombieGroup)