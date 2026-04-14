# Module src/core/promise/abortable
[# core/promise/abortable](#corepromiseabortable)

This module provides a class wraps promise-like objects and adds to them some extra functionality, such as possibility of cancellation, etc.

```
import AbortablePromise from 'core/promise/abortable';  
  
const promise = new AbortablePromise((resolve, reject, onAbort) => {  
  setTimeout(resolve, 100);  
  
  onAbort((reason) => {  
    console.error(`The promise was aborted by a reason of ${reason}`);  
  });  
  
}).catch((err) => console.error(err)); // timeout  
  
// Invoking of `abort` rejects the promise.  
// Additionally, you can specify a reason to abort.  
promise.abort('timeout');
```

[## Tied promises](#tied-promises)

You can tie one promise with another. Tying is mean that when your abort one promise, another one will be aborted too.
To tie a promise, provide a parent promise as the second argument of the constructor or static methods, like `all` or `race`.

```
import AbortablePromise from 'core/promise/abortable';  
  
// catch: timeout  
const parent = new AbortablePromise((resolve) => setTimeout(resolve, 100)).catch((err) => console.error(err));  
  
// catch: timeout  
const childPromise = new AbortablePromise((resolve) => setTimeout(resolve, 200)).catch((err) => console.error(err), parent);  
  
parent.abort('timeout');
```

[## API](#api)

The module re-use native Promise API with adding some extra getters, etc., you free to use such methods like `then`, `catch`, or `finally`.

[### isPending](#ispending)

True if the current promise is pending.

```
import AbortablePromise from 'core/promise/abortable';  
  
const promise = new AbortablePromise((resolve) => {  
  setTimeout(() => {  
    resolve();  
  
    // false  
    console.log(promise.isPending);  
  }, 100);  
});  
  
// true  
console.log(promise.isPending);
```

[## Helpers](#helpers)

The module provides a bunch of static helper methods and getters.

[### wrapReasonToIgnore](#wrapreasontoignore)

The method wraps the specified abort reason to ignore with tied promises,
i.e., this reason won't reject all child promises.

[### resolveAndCall](#resolveandcall)

The method creates a new resolved promise for the specified value.
If the resolved value is a function, it will be invoked.
The result of the invoking will be provided as a value of the promise.

```
import AbortablePromise from 'core/promise/abortable';  
  
AbortablePromise.resolveAndCall(Promise.resolve(() => 1)).then((res) => {  
  // 1  
  console.log(res);  
});
```

## Index

### References

* [ConstrAbortHandler](src_core_promise_abortable.html#ConstrAbortHandler)
* [ConstrRejectHandler](src_core_promise_abortable.html#ConstrRejectHandler)
* [ConstrResolveHandler](src_core_promise_abortable.html#ConstrResolveHandler)
* [ExecutableValue](src_core_promise_abortable.html#ExecutableValue)
* [Executor](src_core_promise_abortable.html#Executor)
* [IGNORE](src_core_promise_abortable.html#IGNORE)
* [RejectHandler](src_core_promise_abortable.html#RejectHandler)
* [ResolveHandler](src_core_promise_abortable.html#ResolveHandler)
* [State](src_core_promise_abortable.html#State)
* [Value](src_core_promise_abortable.html#Value)

### Classes

* [default](../classes/src_core_promise_abortable.default.html)

## References

### ConstrAbortHandler

Re-exports [ConstrAbortHandler](../interfaces/src_core_promise_abortable_interface.ConstrAbortHandler.html)

### ConstrRejectHandler

Re-exports [ConstrRejectHandler](../interfaces/src_core_promise_abortable_interface.ConstrRejectHandler.html)

### ConstrResolveHandler

Re-exports [ConstrResolveHandler](../interfaces/src_core_promise_abortable_interface.ConstrResolveHandler.html)

### ExecutableValue

Re-exports [ExecutableValue](src_core_promise_abortable_interface.html#ExecutableValue)

### Executor

Re-exports [Executor](../interfaces/src_core_promise_abortable_interface.Executor.html)

### IGNORE

Re-exports [IGNORE](src_core_promise_abortable_const.html#IGNORE)

### RejectHandler

Re-exports [RejectHandler](src_core_promise_abortable_interface.html#RejectHandler)

### ResolveHandler

Re-exports [ResolveHandler](src_core_promise_abortable_interface.html#ResolveHandler)

### State

Re-exports [State](../enums/src_core_promise_abortable_interface.State.html)

### Value

Re-exports [Value](src_core_promise_abortable_interface.html#Value)