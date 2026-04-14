# Module src/core/async/modules/wrappers
[# core/async/modules/wrappers](#coreasyncmoduleswrappers)

This module provides a bunch of helpers to wrap some objects, like event emitters or data providers.

[## wrapDataProvider](#wrapdataprovider)

The wrapper takes a link to the "raw" data provider and returns a new object that based on the original,
but all async methods and properties are wrapped by Async.

Notice, the wrapped methods can take additional Async parameters, like group or label.

```
import Async from 'core/async';  
import Provider, { provider } from 'core/data';  
  
@provider('api')  
export default class User extends Provider {  
  baseURL = 'user/:id';  
}  
  
const  
  $a = new Async(),  
  wrappedProvider = $a.wrapDataProvider(new User());  
  
wrappedProvider.get({uuid: 1}).then((res) => {  
  console.log(res);  
});  
  
// By default, all wrapped methods have a group name that is equal to the provider name.  
// So we can use it to clear or suspend requests, etc.  
$a.clearAll({group: 'api.User'})  
  
wrappedProvider.upd({uuid: 1}, {  
  // All wrapped methods can take additional Async parameters as the second argument: `group`, `label` and `join`  
  group: 'bla',  
  label: 'foo',  
  join: true,  
  
  // Also, the second argument of the wrapped method can take the original parameters from a provider  
  headers: {  
    'X-Foo': '1'  
  }  
  
}).then((res) => {  
  console.log(res);  
});  
  
// If we are providing a group to the method, it will be joined with the global group by using the `:` character  
$a.suspendAll({group: 'api.User:bla'});  
  
// Obviously, we can use a group as RegExp  
$a.muteAll({group: /api\.User/});  
  
// We can use any methods or properties from the original data provider  
wrappedProvider.dropCache();
```

[### Custom global group](#custom-global-group)

By default, when the wrapper wraps the provider, it takes the provider name and passes it as a group to all wrapped methods.
This behavior brings a future to clear or suspend all requests from the wrapped provider by its name.
But we can provide a different global name when wrapping a provider.

```
import Async from 'core/async';  
import Provider, { provider } from 'core/data';  
  
@provider('api')  
export default class User extends Provider {  
  baseURL = 'user/:id';  
}  
  
const  
  $a = new Async(),  
  dp1 = $a.wrapDataProvider(new User(), {group: 'foo'});  
  
dp1.get({uuid: 1}).then((res) => {  
  console.log(res);  
});  
  
$a.clearAll({group: 'foo'})
```

[## wrapEventEmitter](#wrapeventemitter)

The wrapper takes a link to the "raw" event emitter and returns a new object that based on the original,
but all async methods and properties are wrapped by Async.

Notice, the wrapped methods can take additional Async parameters, like group or label. In addition,
the wrapper adds new methods, like "on" or "off", to make the emitter API more standard.

```
import Async from 'core/async';  
  
const  
  $a = new Async(),  
  wrappedEventEmitter = $a.wrapEventEmitter(window);  
  
const handler = () => console.log('scroll event');  
  
// We can safely listen to emitter events, cause all emitter methods, like `addListener` or `on` are wrapped by Async.  
const id = wrappedEventEmitter.addEventListener('scroll', handler, {  
  // Notice, the third argument can take Async parameters in addition to the native emitter parameters  
  capture: true,  
  label: 'label'  
});  
  
// The wrapper preserves the original API of emitter methods, so we can call something like this  
wrappedEventEmitter.removeEventListener('scroll', handler);  
  
// Finally, the wrapper adds a bunch of standard methods to the emitter, like `on`, `once`, and other stuff.  
// We can use their instead of the original methods to make our code more universal.  
wrappedEventEmitter.once('resize', (e) => {  
  console.log(e);  
}, {group: 'resizers'});  
  
$a.muteAll({group: 'resizers'});  
  
// We can use any methods or properties from the original emitter  
console.log(wrappedEventEmitter.name); // window.name
```

[### Custom global group](#custom-global-group-1)

Unlike the wrapper of data providers, the emitter wrapper doesn't have any default global group for operations,
but you can pass it manually.
This behavior brings a future to clear or suspend all events from the wrapped provider by its name.

```
import Async from 'core/async';  
  
const  
  $a = new Async(),  
  wrappedEventEmitter = $a.wrapEventEmitter(window, {group: 'windowEvents'});  
  
wrappedEventEmitter.once('resize', (e) => {  
  console.log(e);  
});  
  
$a.muteAll({group: 'windowEvents'});  
  
wrappedEventEmitter.on('scroll', (e) => {  
  console.log(e);  
}, {  
  // If we are providing a group to the method, it will be joined with the global group by using the `:` character  
  group: 'scrolling'  
});  
  
$a.muteAll({group: 'windowEvents:scrolling'});
```

[### Native API of emitters](#native-api-of-emitters)

As you can see, the wrapper creates a new object based on the original emitter and replaces some methods with the safely Async analogs.
The overridden methods preserve the original emitter API, but some interfaces are not supported to use.

```
import Async from 'core/async';  
  
const  
  $a = new Async(),  
  wrappedEventEmitter = $a.wrapEventEmitter(window, {group: 'windowEvents'});  
  
// The wrapper does not support this kind of attaching listeners.  
// The replaced method can take the second argument only as a function.  
wrappedEventEmitter.addEventListener('scroll', {  
  handleEvent: (e) => {  
    console.log(e);  
  }  
})
```

[## wrapStorage](#wrapstorage)

The wrapper takes a link to the "raw" async storage and returns a new object that based on the original,
but all async methods and properties are wrapped by Async.

Notice, the wrapped methods can take additional Async parameters, like group or label.

```
import Async from 'core/async';  
import { asyncLocal } from 'core/kv-storage';  
  
const  
  $a = new Async(),  
  wrappedStorage = $a.wrapStorage(asyncLocal);  
  
wrappedStorage.set('someKey', 'someValue', {  
  // All wrapped methods can take additional Async parameters as the last argument: `group`, `label` and `join`  
  group: 'bla',  
  label: 'foo',  
  join: true,  
}).then(async () => {  
  console.log(await wrappedStorage.get('someKey') === 'someValue');  
});  
  
$a.suspendAll({label: 'foo'});
```

[### Custom global group](#custom-global-group-2)

The storage wrapper doesn't have any default global group for operations, but you can pass it manually.
This behavior brings a feature to clear or suspend all events from the wrapped provider by its name.

```
import Async from 'core/async';  
import { asyncLocal } from 'core/kv-storage';  
  
const  
  $a = new Async(),  
  wrappedStorage = $a.wrapStorage(asyncLocal, {group: 'globalGroup'});  
  
wrappedStorage.set('someKey', 'someValue').then(() => {  
  console.log('yeah!');  
});  
  
$a.muteAll({group: 'globalGroup'});  
  
wrappedStorage.get('someKey', {  
  // If we are providing a group to the method, it will be joined with the global group by using the `:` character  
  group: 'localGroup'  
}).then((val) => {  
  console.log(val) === 'someValue';  
});  
  
$a.clearAll({group: 'globalGroup:localGroup'});
```

[### Custom namespace](#custom-namespace)

By default, a custom namespace have the same global group as the global namespace

```
import Async from 'core/async';  
import { asyncLocal } from 'core/kv-storage';  
  
const  
  $a = new Async(),  
  wrappedStorage = $a.wrapStorage(asyncLocal, {group: 'bar'});  
  
// We can provide own global group to namespace, it will be joined with the parent's global group  
const blaStore = wrappedStorage.namespace('[[BLA]]', {group: 'bla'});  
  
blaStore.clear({group: 'foo'});  
  
$a.muteAll({group: 'bar:bla:foo'});
```

## Index

### References

* [AsyncCb](src_core_async_modules_wrappers.html#AsyncCb)
* [AsyncCbOptions](src_core_async_modules_wrappers.html#AsyncCbOptions)
* [AsyncCbOptionsSingle](src_core_async_modules_wrappers.html#AsyncCbOptionsSingle)
* [AsyncIdleOptions](src_core_async_modules_wrappers.html#AsyncIdleOptions)
* [AsyncOnOptions](src_core_async_modules_wrappers.html#AsyncOnOptions)
* [AsyncOnceOptions](src_core_async_modules_wrappers.html#AsyncOnceOptions)
* [AsyncOptions](src_core_async_modules_wrappers.html#AsyncOptions)
* [AsyncOptionsForWrappers](src_core_async_modules_wrappers.html#AsyncOptionsForWrappers)
* [AsyncPromiseOptions](src_core_async_modules_wrappers.html#AsyncPromiseOptions)
* [AsyncPromisifyOnceOptions](src_core_async_modules_wrappers.html#AsyncPromisifyOnceOptions)
* [AsyncProxyOptions](src_core_async_modules_wrappers.html#AsyncProxyOptions)
* [AsyncRequestIdleCallbackOptions](src_core_async_modules_wrappers.html#AsyncRequestIdleCallbackOptions)
* [AsyncRequestOptions](src_core_async_modules_wrappers.html#AsyncRequestOptions)
* [AsyncWaitOptions](src_core_async_modules_wrappers.html#AsyncWaitOptions)
* [AsyncWorkerOptions](src_core_async_modules_wrappers.html#AsyncWorkerOptions)
* [BoundFn](src_core_async_modules_wrappers.html#BoundFn)
* [CancelablePromise](src_core_async_modules_wrappers.html#CancelablePromise)
* [ClearFn](src_core_async_modules_wrappers.html#ClearFn)
* [ClearOptions](src_core_async_modules_wrappers.html#ClearOptions)
* [ClearOptionsId](src_core_async_modules_wrappers.html#ClearOptionsId)
* [ClearProxyOptions](src_core_async_modules_wrappers.html#ClearProxyOptions)
* [ClearReason](src_core_async_modules_wrappers.html#ClearReason)
* [DataProviderBodyMethodsToReplace](src_core_async_modules_wrappers.html#DataProviderBodyMethodsToReplace)
* [DataProviderMethodsToReplace](src_core_async_modules_wrappers.html#DataProviderMethodsToReplace)
* [DataProviderQueryMethodsToReplace](src_core_async_modules_wrappers.html#DataProviderQueryMethodsToReplace)
* [EmitLikeEvents](src_core_async_modules_wrappers.html#EmitLikeEvents)
* [Event](src_core_async_modules_wrappers.html#Event)
* [EventEmitterLike](src_core_async_modules_wrappers.html#EventEmitterLike)
* [EventEmitterLikeP](src_core_async_modules_wrappers.html#EventEmitterLikeP)
* [EventEmitterOverwritten](src_core_async_modules_wrappers.html#EventEmitterOverwritten)
* [EventEmitterWrapper](src_core_async_modules_wrappers.html#EventEmitterWrapper)
* [EventId](src_core_async_modules_wrappers.html#EventId)
* [FullAsyncOptions](src_core_async_modules_wrappers.html#FullAsyncOptions)
* [FullClearOptions](src_core_async_modules_wrappers.html#FullClearOptions)
* [GlobalCache](src_core_async_modules_wrappers.html#GlobalCache)
* [Group](src_core_async_modules_wrappers.html#Group)
* [IdObject](src_core_async_modules_wrappers.html#IdObject)
* [IdleCb](src_core_async_modules_wrappers.html#IdleCb)
* [Join](src_core_async_modules_wrappers.html#Join)
* [Label](src_core_async_modules_wrappers.html#Label)
* [LinkNames](src_core_async_modules_wrappers.html#LinkNames)
* [LocalCache](src_core_async_modules_wrappers.html#LocalCache)
* [MarkReason](src_core_async_modules_wrappers.html#MarkReason)
* [Namespace](src_core_async_modules_wrappers.html#Namespace)
* [Namespaces](src_core_async_modules_wrappers.html#Namespaces)
* [PromiseLikeP](src_core_async_modules_wrappers.html#PromiseLikeP)
* [ProxyCb](src_core_async_modules_wrappers.html#ProxyCb)
* [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers.html#ReadonlyEventEmitterWrapper)
* [StrictClearOptions](src_core_async_modules_wrappers.html#StrictClearOptions)
* [StrictClearOptionsId](src_core_async_modules_wrappers.html#StrictClearOptionsId)
* [Task](src_core_async_modules_wrappers.html#Task)
* [TaskCtx](src_core_async_modules_wrappers.html#TaskCtx)
* [TimerId](src_core_async_modules_wrappers.html#TimerId)
* [WorkerLike](src_core_async_modules_wrappers.html#WorkerLike)
* [WorkerLikeP](src_core_async_modules_wrappers.html#WorkerLikeP)
* [WrappedAsyncStorage](src_core_async_modules_wrappers.html#WrappedAsyncStorage)
* [WrappedAsyncStorageNamespace](src_core_async_modules_wrappers.html#WrappedAsyncStorageNamespace)
* [WrappedDataProvider](src_core_async_modules_wrappers.html#WrappedDataProvider)
* [asyncCounter](src_core_async_modules_wrappers.html#asyncCounter)
* [asyncOptionsKeys](src_core_async_modules_wrappers.html#asyncOptionsKeys)
* [dataProviderMethodsToReplace](src_core_async_modules_wrappers.html#dataProviderMethodsToReplace)
* [emitLikeEvents](src_core_async_modules_wrappers.html#emitLikeEvents)
* [isAsyncOptions](src_core_async_modules_wrappers.html#isAsyncOptions)
* [isEvent](src_core_async_modules_wrappers.html#isEvent)
* [isParams](src_core_async_modules_wrappers.html#isParams)
* [isPromisifyLinkName](src_core_async_modules_wrappers.html#isPromisifyLinkName)
* [isPromisifyNamespace](src_core_async_modules_wrappers.html#isPromisifyNamespace)
* [isZombieGroup](src_core_async_modules_wrappers.html#isZombieGroup)

### Classes

* [default](../classes/src_core_async_modules_wrappers.default.html)

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