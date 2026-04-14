# Module src/core/promise/interface
## Index

### Interfaces

* [ControllablePromiseConstructor](../interfaces/src_core_promise_interface.ControllablePromiseConstructor.html)
* [ControllablePromiseExecutor](../interfaces/src_core_promise_interface.ControllablePromiseExecutor.html)
* [ControllablePromiseRejectHandler](../interfaces/src_core_promise_interface.ControllablePromiseRejectHandler.html)
* [ControllablePromiseResolveHandler](../interfaces/src_core_promise_interface.ControllablePromiseResolveHandler.html)
* [CreateControllablePromiseOptions](../interfaces/src_core_promise_interface.CreateControllablePromiseOptions.html)

### Type aliases

* [ControllablePromise](src_core_promise_interface.html#ControllablePromise)

## Type aliases

### ControllablePromise

ControllablePromise<P>: P & { isPending: boolean; reject: any; resolve: any }

* Defined in [src/core/promise/interface.ts:9](https://github.com/V4Fire/Core/blob/master/src/core/promise/interface.ts#L9)

#### Type parameters

* #### P: PromiseLike<any> = Promise<unknown>