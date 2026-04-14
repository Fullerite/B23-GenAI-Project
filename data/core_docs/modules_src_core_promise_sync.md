# Module src/core/promise/sync
[# core/promise/sync](#corepromisesync)

This module provides a class is similar to the native promise class but works synchronously.

```
import SyncPromise from 'core/promise/sync';  
  
// 1  
// 2  
SyncPromise.resolve().then(() => console.log(1));  
console.log(2);
```

[## Non-standard API](#non-standard-api)
[### isPending](#ispending)

True if the current promise is pending.

```
import SyncPromise from 'core/prelude/structures/sync-promise';  
  
const sleep = new SyncPromise((r) => setTimeout(r, 100));  
console.log(sleep.isPending === true);  
  
setTimeout(() => {  
  console.log(sleep.isPending === false);  
}, 200);
```

[### unwrap](#unwrap)

Returns the promise' value if it is fulfilled, otherwise throws an exception.

```
import SyncPromise from 'core/prelude/structures/sync-promise';  
  
const sleep = new SyncPromise((r) => setTimeout(() => r(10), 100));  
  
try {  
  sleep.unwrap();  
  
} catch (err) {  
  console.error(err);  
}  
  
setTimeout(() => {  
  console.log(sleep.unwrap() === 10);  
}, 200);
```

[## Helpers](#helpers)

The module provides a bunch of helpers to memoize promises.

[### Memoize](#memoize)

Memorizes the specified promise and converts it to a synchronous promise.
It means that after the first resolution, the promised result will be cached,
and the method returns the synchronous version of a promise.

```
import { memoize } from 'core/promise/memoize';  
  
// Will fire:  
// 2  
// 1  
// 3  
// 4  
memoize('core/url/concat', () => import('core/url/concat')).then(() => {  
  console.log(1);  
  
  memoize('core/url/concat', () => import('core/url/concat')).then(() => {  
    console.log(3);  
  });  
  
  console.log(4);  
});  
  
console.log(2);
```

## Index

### References

* [ConstrRejectHandler](src_core_promise_sync.html#ConstrRejectHandler)
* [ConstrResolveHandler](src_core_promise_sync.html#ConstrResolveHandler)
* [Executor](src_core_promise_sync.html#Executor)
* [RejectHandler](src_core_promise_sync.html#RejectHandler)
* [ResolveHandler](src_core_promise_sync.html#ResolveHandler)
* [State](src_core_promise_sync.html#State)
* [Value](src_core_promise_sync.html#Value)
* [default](src_core_promise_sync.html#default)
* [memoize](src_core_promise_sync.html#memoize)

## References

### ConstrRejectHandler

Re-exports [ConstrRejectHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrRejectHandler.html)

### ConstrResolveHandler

Re-exports [ConstrResolveHandler](../interfaces/src_core_prelude_structures_sync_promise_interface.ConstrResolveHandler.html)

### Executor

Re-exports [Executor](../interfaces/src_core_prelude_structures_sync_promise_interface.Executor.html)

### RejectHandler

Re-exports [RejectHandler](src_core_prelude_structures_sync_promise_interface.html#RejectHandler)

### ResolveHandler

Re-exports [ResolveHandler](src_core_prelude_structures_sync_promise_interface.html#ResolveHandler)

### State

Re-exports [State](../enums/src_core_prelude_structures_sync_promise_interface.State.html)

### Value

Re-exports [Value](src_core_prelude_structures_sync_promise_interface.html#Value)

### default

Re-exports [default](../classes/src_core_prelude_structures_sync_promise.default.html)

### memoize

Re-exports [memoize](src_core_promise_sync_helpers.html#memoize)