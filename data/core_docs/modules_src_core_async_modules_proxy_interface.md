# Module src/core/async/modules/proxy/interface
## Index

### Interfaces

* [AsyncPromiseOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncPromiseOptions.html)
* [AsyncRequestOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncRequestOptions.html)
* [AsyncWorkerOptions](../interfaces/src_core_async_modules_proxy_interface.AsyncWorkerOptions.html)
* [CancelablePromise](../interfaces/src_core_async_modules_proxy_interface.CancelablePromise.html)
* [WorkerLike](../interfaces/src_core_async_modules_proxy_interface.WorkerLike.html)

### Type aliases

* [PromiseLikeP](src_core_async_modules_proxy_interface.html#PromiseLikeP)
* [WorkerLikeP](src_core_async_modules_proxy_interface.html#WorkerLikeP)

## Type aliases

### PromiseLikeP

PromiseLikeP<T>: (() => PromiseLike<T>) | PromiseLike<T>

* Defined in [src/core/async/modules/proxy/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/interface.ts#L42)

Extended type of promise

#### Type parameters

* #### T = unknown

### WorkerLikeP

WorkerLikeP: Function | [WorkerLike](../interfaces/src_core_async_modules_proxy_interface.WorkerLike.html)

* Defined in [src/core/async/modules/proxy/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/proxy/interface.ts#L29)

Extended type of worker