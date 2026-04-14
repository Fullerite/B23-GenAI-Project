# Module src/core/promise
## Index

### References

* [ControllablePromise](src_core_promise.html#ControllablePromise)
* [ControllablePromiseConstructor](src_core_promise.html#ControllablePromiseConstructor)
* [ControllablePromiseExecutor](src_core_promise.html#ControllablePromiseExecutor)
* [ControllablePromiseRejectHandler](src_core_promise.html#ControllablePromiseRejectHandler)
* [ControllablePromiseResolveHandler](src_core_promise.html#ControllablePromiseResolveHandler)
* [CreateControllablePromiseOptions](src_core_promise.html#CreateControllablePromiseOptions)

### Functions

* [createControllablePromise](src_core_promise.html#createControllablePromise)
* [isControllablePromise](src_core_promise.html#isControllablePromise)

## References

### ControllablePromise

Re-exports [ControllablePromise](src_core_promise_interface.html#ControllablePromise)

### ControllablePromiseConstructor

Re-exports [ControllablePromiseConstructor](../interfaces/src_core_promise_interface.ControllablePromiseConstructor.html)

### ControllablePromiseExecutor

Re-exports [ControllablePromiseExecutor](../interfaces/src_core_promise_interface.ControllablePromiseExecutor.html)

### ControllablePromiseRejectHandler

Re-exports [ControllablePromiseRejectHandler](../interfaces/src_core_promise_interface.ControllablePromiseRejectHandler.html)

### ControllablePromiseResolveHandler

Re-exports [ControllablePromiseResolveHandler](../interfaces/src_core_promise_interface.ControllablePromiseResolveHandler.html)

### CreateControllablePromiseOptions

Re-exports [CreateControllablePromiseOptions](../interfaces/src_core_promise_interface.CreateControllablePromiseOptions.html)

## Functions

### createControllablePromise

* createControllablePromise<T>(opts: [CreateControllablePromiseOptions](../interfaces/src_core_promise_interface.CreateControllablePromiseOptions.html)<T>): [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<T extends new (...args: any[]) => infer  R ? R : Promise<unknown>>
* createControllablePromise<T>(opts?: [CreateControllablePromiseOptions](../interfaces/src_core_promise_interface.CreateControllablePromiseOptions.html)<PromiseConstructor>): [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<Promise<T>>

* + Defined in [src/core/promise/index.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/promise/index.ts#L46)

  Creates a promise that can be resolved from the "outside"

  example
  :   ```
      const promise = createControllablePromise();  
      promise.resolve(10);
      ```

  #### Type parameters

  + #### T: [ControllablePromiseConstructor](../interfaces/src_core_promise_interface.ControllablePromiseConstructor.html)<unknown, T>

    promise constructor

  #### Parameters

  + ##### opts: [CreateControllablePromiseOptions](../interfaces/src_core_promise_interface.CreateControllablePromiseOptions.html)<T>

    additional options

  #### Returns [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<T extends new (...args: any[]) => infer R ? R : Promise<unknown>>
* + Defined in [src/core/promise/index.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/promise/index.ts#L56)

  Creates a promise that can be resolved from the "outside"

  #### Type parameters

  + #### T = unknown

    type of the resolved promise value

  #### Parameters

  + ##### Optional opts: [CreateControllablePromiseOptions](../interfaces/src_core_promise_interface.CreateControllablePromiseOptions.html)<PromiseConstructor>

  #### Returns [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<Promise<T>>

### isControllablePromise

* isControllablePromise<T>(promise: T): promise is [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<T>
* isControllablePromise(obj: unknown): obj is [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<PromiseLike<unknown>>

* + Defined in [src/core/promise/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/promise/index.ts#L23)

  Returns true if the specified promise implements the interface of `ControllablePromise`

  #### Type parameters

  + #### T: PromiseLike<any, T>

  #### Parameters

  + ##### promise: T

  #### Returns promise is [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<T>
* + Defined in [src/core/promise/index.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/promise/index.ts#L29)

  Returns true if the specified object implements the interface of `ControllablePromise`

  #### Parameters

  + ##### obj: unknown

  #### Returns obj is [ControllablePromise](src_core_promise_interface.html#ControllablePromise)<PromiseLike<unknown>>