# Module src/core/async
[# core/async](#coreasync)

This module provides a class to control asynchronous operations.

```
import Async from 'core/async';  
  
const  
  watcher = new Async();  
  
watcher.setTimeout(() => {  
  console.log(1);  
}, 100, {group: 'foo'});  
  
watcher.setTimeout(() => {  
  console.log(2);  
}, 200, {group: 'foo'});  
  
watcher.clearTimeout({group: 'foo'});
```

## Index

### References

* [AsyncCb](src_core_async.html#AsyncCb)
* [AsyncCbOptions](src_core_async.html#AsyncCbOptions)
* [AsyncCbOptionsSingle](src_core_async.html#AsyncCbOptionsSingle)
* [AsyncIdleOptions](src_core_async.html#AsyncIdleOptions)
* [AsyncOnOptions](src_core_async.html#AsyncOnOptions)
* [AsyncOnceOptions](src_core_async.html#AsyncOnceOptions)
* [AsyncOptions](src_core_async.html#AsyncOptions)
* [AsyncOptionsForWrappers](src_core_async.html#AsyncOptionsForWrappers)
* [AsyncPromiseOptions](src_core_async.html#AsyncPromiseOptions)
* [AsyncPromisifyOnceOptions](src_core_async.html#AsyncPromisifyOnceOptions)
* [AsyncProxyOptions](src_core_async.html#AsyncProxyOptions)
* [AsyncRequestIdleCallbackOptions](src_core_async.html#AsyncRequestIdleCallbackOptions)
* [AsyncRequestOptions](src_core_async.html#AsyncRequestOptions)
* [AsyncWaitOptions](src_core_async.html#AsyncWaitOptions)
* [AsyncWorkerOptions](src_core_async.html#AsyncWorkerOptions)
* [BoundFn](src_core_async.html#BoundFn)
* [CancelablePromise](src_core_async.html#CancelablePromise)
* [ClearFn](src_core_async.html#ClearFn)
* [ClearOptions](src_core_async.html#ClearOptions)
* [ClearOptionsId](src_core_async.html#ClearOptionsId)
* [ClearProxyOptions](src_core_async.html#ClearProxyOptions)
* [ClearReason](src_core_async.html#ClearReason)
* [DataProviderBodyMethodsToReplace](src_core_async.html#DataProviderBodyMethodsToReplace)
* [DataProviderMethodsToReplace](src_core_async.html#DataProviderMethodsToReplace)
* [DataProviderQueryMethodsToReplace](src_core_async.html#DataProviderQueryMethodsToReplace)
* [EmitLikeEvents](src_core_async.html#EmitLikeEvents)
* [Event](src_core_async.html#Event)
* [EventEmitterLike](src_core_async.html#EventEmitterLike)
* [EventEmitterLikeP](src_core_async.html#EventEmitterLikeP)
* [EventEmitterOverwritten](src_core_async.html#EventEmitterOverwritten)
* [EventEmitterWrapper](src_core_async.html#EventEmitterWrapper)
* [EventId](src_core_async.html#EventId)
* [FullAsyncOptions](src_core_async.html#FullAsyncOptions)
* [FullClearOptions](src_core_async.html#FullClearOptions)
* [GlobalCache](src_core_async.html#GlobalCache)
* [Group](src_core_async.html#Group)
* [IdObject](src_core_async.html#IdObject)
* [IdleCb](src_core_async.html#IdleCb)
* [Join](src_core_async.html#Join)
* [Label](src_core_async.html#Label)
* [LinkNames](src_core_async.html#LinkNames)
* [LocalCache](src_core_async.html#LocalCache)
* [MarkReason](src_core_async.html#MarkReason)
* [Namespace](src_core_async.html#Namespace)
* [Namespaces](src_core_async.html#Namespaces)
* [NamespacesDictionary](src_core_async.html#NamespacesDictionary)
* [PromiseLikeP](src_core_async.html#PromiseLikeP)
* [ProxyCb](src_core_async.html#ProxyCb)
* [ReadonlyEventEmitterWrapper](src_core_async.html#ReadonlyEventEmitterWrapper)
* [StrictClearOptions](src_core_async.html#StrictClearOptions)
* [StrictClearOptionsId](src_core_async.html#StrictClearOptionsId)
* [Task](src_core_async.html#Task)
* [TaskCtx](src_core_async.html#TaskCtx)
* [TimerId](src_core_async.html#TimerId)
* [WorkerLike](src_core_async.html#WorkerLike)
* [WorkerLikeP](src_core_async.html#WorkerLikeP)
* [WrappedAsyncStorage](src_core_async.html#WrappedAsyncStorage)
* [WrappedAsyncStorageNamespace](src_core_async.html#WrappedAsyncStorageNamespace)
* [WrappedDataProvider](src_core_async.html#WrappedDataProvider)
* [asyncCounter](src_core_async.html#asyncCounter)
* [asyncOptionsKeys](src_core_async.html#asyncOptionsKeys)
* [dataProviderMethodsToReplace](src_core_async.html#dataProviderMethodsToReplace)
* [emitLikeEvents](src_core_async.html#emitLikeEvents)
* [isAsyncOptions](src_core_async.html#isAsyncOptions)
* [isEvent](src_core_async.html#isEvent)
* [isParams](src_core_async.html#isParams)
* [isPromisifyLinkName](src_core_async.html#isPromisifyLinkName)
* [isPromisifyNamespace](src_core_async.html#isPromisifyNamespace)
* [isZombieGroup](src_core_async.html#isZombieGroup)
* [linkNamesDictionary](src_core_async.html#linkNamesDictionary)
* [namespaces](src_core_async.html#namespaces)

### Classes

* [default](../classes/src_core_async.default.html)

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

### NamespacesDictionary

Re-exports [NamespacesDictionary](src_core_async_const.html#NamespacesDictionary)

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

### asyncOptionsKeys

Re-exports [asyncOptionsKeys](src_core_async_modules_wrappers_consts.html#asyncOptionsKeys)

### dataProviderMethodsToReplace

Re-exports [dataProviderMethodsToReplace](src_core_async_modules_wrappers_consts.html#dataProviderMethodsToReplace)

### emitLikeEvents

Re-exports [emitLikeEvents](src_core_async_modules_wrappers_consts.html#emitLikeEvents)

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

### linkNamesDictionary

Re-exports [linkNamesDictionary](src_core_async_const.html#linkNamesDictionary)

### namespaces

Re-exports [namespaces](src_core_async_const.html#namespaces)