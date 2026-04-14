# Module src/core/promise/sync/helpers
## Index

### Functions

* [memoize](src_core_promise_sync_helpers.html#memoize)

## Functions

### memoize

* memoize<T>(keyOrPromise: unknown, promise?: [PromiseLikeP](src_core_async_modules_proxy_interface.html#PromiseLikeP)<T>): Promise<T>

* + Defined in [src/core/promise/sync/helpers.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/promise/sync/helpers.ts#L28)

  Memorizes the specified promise and converts it to a synchronous promise.
  It means that after the first resolution,
  the promised result will be cached, and the method returns the synchronous version of a promise.

  example
  :   ```
      memoize(nextTick());  
      memoize('core/url/concat', () => import('core/url/concat'));
      ```

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### keyOrPromise: unknown

    promise or a promise factory to cache, or a key to cache the promise
  + ##### Optional promise: [PromiseLikeP](src_core_async_modules_proxy_interface.html#PromiseLikeP)<T>

    promise or a promise factory to cache (if the first argument is a key)

  #### Returns Promise<T>