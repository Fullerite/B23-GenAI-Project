# Module src/core/pool
[# core/pool](#corepool)

This module provides a class to create an object pool structure. The pool supports a classical API when you take and
release some resources from the pool, and the API with support of sharing resources between different consumers.
In addition, the pool supports segmentation of resources via a provided hash function.

[## "Classical" API](#quotclassicalquot-api)

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool(createDBConnection, {size: 5});  
  
// Number of resources in the pool (5)  
console.log(pool.size);  
  
// Number of available resources in the pool (5)  
console.log(pool.available);  
  
// If the pool is empty, `value` will be nullish  
const {value, free, destroy} = pool.take();  
  
// 5  
console.log(pool.size);  
  
// 4  
console.log(pool.available);  
  
// Releasing a resource and returning it to the pool  
free();  
  
// 5  
console.log(pool.available);  
  
// Creating a new resource if the pool is empty  
const anotherResource = pool.takeOrCreate();  
  
// Destroying a resource instead of returning it to the pool  
// (if you provide a resource destructor when creating a pull instance, it will be used there)  
anotherResource.destroy();  
  
// Returning a promise that resolves with a resource from the pool  
pool.takeOrWait().then(({value, free, destroy}) => {});
```

[## Borrowing of resources](#borrowing-of-resources)

Using API of borrowing you can share resources between different consumers without taking their from the pool.
If you borrow a resource, you can't `take` it till all borrow consumers release it.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool(createDOMObserver, {size: 1});  
  
// Number of resources in the pool (5)  
console.log(pool.size);  
  
// Number of available resources in the pool (5)  
console.log(pool.available);  
  
// If the pool is empty, `value` will be nullish  
const resource1 = pool.borrow();  
  
console.log(resource1.value);  
  
// 5  
console.log(pool.size);  
  
// 5  
console.log(pool.available);  
  
// You can't take a resource if it already borrowed  
console.log(pool.take().value === null);  
  
// But, you can borrow it  
const resource2 = pool.borrow();  
  
console.log(resource2.value);  
  
// Releasing resources and returning their to the pool  
resource1.free();  
resource2.free();  
  
// Now you can take it  
console.log(pool.take().value);  
  
// Creating a new resource if the pool is empty  
const anotherResource = pool.borrowOrCreate();  
  
// Destroying a resource instead of releasing it  
// (if you provide a resource destructor when creating a pull instance, it will be used there)  
anotherResource.destroy();  
  
// Returning a promise that resolves with a borrowed resource from the pool  
pool.borrowOrWait().then(({value, free, destroy}) => {});
```

[## Providing arguments to a resource constructor](#providing-arguments-to-a-resource-constructor)

There is a possibility to provide arguments into a resource constructor.
Just pass them as the second argument into the pool constructor.

```
import Pool from 'core/pool';  
  
// The pull contains two arrays: [1, 2, 3], [1, 2, 3]  
const pool = new Pool((...values) => [...values], [1, 2, 3], {  
  size: 2  
});
```

Also, you can pass arguments as a function.
This function will be invoked with a resource index and should return arguments to pass.

```
import Pool from 'core/pool';  
  
// The pull contains two arrays: [0], [1]  
const pool = new Pool((...values) => [...values], (i) => [i], {  
  size: 2  
});
```

In addition, you can provide arguments to create a resource to `takeOrCreate` and `borrowOrCreate` methods.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool((...values) => [...values]);  
  
// [1]  
console.log(pool.takeOrCreate(1).value);  
  
// [1, 2, 3]  
console.log(pool.borrowOrCreate(1, 2, 3).value);
```

[## Segmentation of resources](#segmentation-of-resources)

You can add a function to calculate a hash of the created resource.
Using this hash, you will be able to take or borrow a resource that matches to the specified hash.

```
import Pool from 'core/pool';  
  
// The pull contains five arrays: [0], [1], [2], [3], [4]  
const pool = new Pool((...values) => [...values], (i) => [i], {  
  size: 5,  
  hashFn: (...args) => Object.fastHash(args)  
});  
  
// All arguments that are passed to the pool methods are using to calculate a hash  
// [1]  
console.log(pool.take(1).value)  
  
// The pool doesn’t have any resources matched with the passed hash  
console.log(pool.take(2, 3).value === null)  
  
// [2]  
console.log(pool.borrow(2).value);
```

[## Limiting the pool size](#limiting-the-pool-size)

By passing a `maxSize` property you can define how many elements can be contained in the pool.
Mind, if you also pass a `size` property larger than `maxSize`, there will be generated an exception.

```
import Pool from 'core/pool';  
  
const pool = new Pool((...values) => [...values], {  
  maxSize: 2  
});  
  
// 2  
console.log(pool.maxSize);  
  
// [1]  
console.log(pool.takeOrCreate(1).value);  
  
// [2]  
console.log(pool.takeOrCreate(2).value);  
  
try {  
  // [3]  
  console.log(pool.takeOrCreate(2).value);  
  
} catch (err) {  
  // The pool contains too many resources  
  console.log(err.message);  
}
```

[## Clearing a pool](#clearing-a-pool)

You can clear a pool and destroys all created resources via invoking the `clear` method.
If you provide a resource destructor when creating a pull instance, it will be with this method.

```
import Pool from 'core/pool';  
  
const pool = new Pool(createDbConnection, {  
  size: 10,  
  resourceDestructor: (resource) => resource.disconnect()  
});  
  
// 10  
console.log(pool.size);  
  
// This resource will be destroyed too  
pool.take();  
  
pool.clear();  
  
// 0  
console.log(pool.size);
```

[## Attaching hook handlers](#attaching-hook-handlers)

You can pass callback functions to handle `take`, `borrow`, `free`, `clear` pool hooks.
Besides regular arguments, these handlers take arguments that are passed to the associated methods.

```
import Pool from 'core/pool';  
  
const pool = new Pool((...values) => [...values], {  
  size: 5,  
  
  onTake(resource, pool, ...args) {  
    console.log(resource, pool, ...args);  
  },  
  
  onBorrow(resource, pool, ...args) {  
    console.log(resource, pool, ...args);  
  },  
  
  onFree(resource, pool, ...args) {  
    console.log(resource, pool, ...args);  
  },  
  
  onClear(pool, ...args) {  
    console.log(pool, ...args);  
  }  
});  
  
pool.take(1, 2, 3);  
pool.takeOrCreate(7, 2).free(10);  
pool.takeOrWait({foo: 'bla'});  
  
pool.borrow(6, 3);  
pool.borrowOrCreate(7, 2).free(10);  
pool.borrowOrWait({foo: 'bla'});  
  
pool.clear();
```

[## API](#api)
[### Constructor options](#constructor-options)

The structure constructor can take an object with optional parameters.

```
export interface PoolOptions<T = unknown> {  
  /**  
   * Number of resources to create at pull initialization  
   * @default `0`  
   */  
  size?: number;  
  
  /**  
   * The maximum number of resources that the pool can contain  
   * @default `Infinity`  
   */  
  maxSize?: number;  
  
  /**  
   * A function to destroy one resource from the pool  
   */  
  resourceDestructor?: ResourceDestructor<T>;  
  
  /**  
   * A function to calculate a hash string for the specified arguments  
   */  
  hashFn?: HashFn;  
  
  /**  
   * Handler: taking some resource via `take` methods  
   */  
  onTake?: ResourceHook<T>;  
  
  /**  
   * Handler: taking some resource via `borrow` methods  
   */  
  onBorrow?: ResourceHook<T>;  
  
  /**  
   * Handler: releasing of some resource  
   */  
  onFree?: ResourceHook<T>;  
  
  /**  
   * Handler: clearing of all pool resources  
   */  
  onClear?: PoolHook<T>;  
}
```

[### Getters](#getters)
[#### maxSize](#maxsize)

The maximum number of resources that the pool can contain.

```
import Pool from 'core/pool';  
  
const pool = new Pool((...values) => [...values], {  
  maxSize: 2  
});  
  
// 2  
console.log(pool.maxSize);
```

[#### size](#size)

Number of resources that are stored in the pool.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool(createDBConnection, {size: 5});  
  
// 5  
console.log(pool.size);  
  
pool.take();  
  
// 5  
console.log(pool.size);
```

[#### available](#available)

Number of available resources that are stored in the pool.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool(createDBConnection, {size: 5});  
  
// 5  
console.log(pool.available);  
  
pool.take();  
  
// 4  
console.log(pool.available);  
  
pool.borrow();  
  
// 4  
console.log(pool.available);
```

[### Methods](#methods)
[#### take](#take)

Returns an available resource from the pool.
The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

The returned result is wrapped with a structure that contains methods to release or drop this resource.
If the pool is empty, the structure value field will be nullish.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool(() => [], {size: 5});  
  
// []  
console.log(pool.take().value);
```

[#### takeOrCreate](#takeorcreate)

Returns an available resource from the pool.
The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

The returned result is wrapped with a structure that contains methods to release or drop this resource.
If the pool is empty, it creates a new resource and returns it.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool((...values) => [...values]);  
  
// [1, 2, 3]  
console.log(pool.takeOrCreate(1, 2, 3).value);
```

[#### takeOrWait](#takeorwait)

Returns a promise with an available resource from the pull.
The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

The returned result is wrapped with a structure that contains methods to release or drop this resource.
If the pool is empty, the promise will wait till it release.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool((...values) => [...values]);  
  
pool.takeOrWait().then(({value}) => {  
  // [1, 2, 3]  
  console.log(value);  
});  
  
pool.takeOrCreate(1, 2, 3).free();
```

[#### borrow](#borrow)

Borrows an available resource from the pool.
The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

When a resource is borrowed, it won’t be dropped from the pool. I.e. you can share it with other consumers.
Mind, you can’t take this resource from the pool when it’s borrowed.

The returned result is wrapped with a structure that contains methods to release or drop this resource.
If the pool is empty, the structure value field will be nullish.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool(() => [], {size: 1});  
  
// []  
console.log(pool.borrow().value);  
  
// []  
console.log(pool.borrow().value);  
  
// []  
console.log(pool.borrow().value);
```

[#### borrowOrCreate](#borroworcreate)

Borrows an available resource from the pool.
The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

When a resource is borrowed, it won’t be dropped from the pool. I.e. you can share it with other consumers.
Mind, you can’t take this resource from the pool when it’s borrowed.

The returned result is wrapped with a structure that contains methods to release or drop this resource.
If the pool is empty, it creates a new resource and returns it.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool((...values) => [...values]);  
  
// [1, 2, 3]  
console.log(pool.borrowOrCreate(1, 2, 3).value);  
  
// [1, 2, 3]  
console.log(pool.borrow().value);
```

[#### borrowOrWait](#borroworwait)

Returns a promise with a borrowed resource from the pull.
The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

When a resource is borrowed, it won’t be dropped from the pool. I.e. you can share it with other consumers.
Mind, you can’t take this resource from the pool when it’s borrowed.

The returned result is wrapped with a structure that contains methods to release or drop this resource.
If the pool is empty, the promise will wait till it release.

```
import Pool from 'core/pool';  
  
const  
  pool = new Pool((...values) => [...values]);  
  
pool.takeOrWait().then(({value}) => {  
  // [1, 2, 3]  
  console.log(value);  
});  
  
pool.takeOrCreate(1, 2, 3).free();
```

[#### clear](#clear)

Clears the pool, i.e. drops all created resource.
The method takes arguments that will be provided to hook handlers.

```
import Pool from 'core/pool';  
  
const pool = new Pool(createDbConnection, {  
  size: 10,  
  resourceDestructor: (resource) => resource.disconnect()  
});  
  
// 10  
console.log(pool.size);  
  
pool.clear();  
  
// 0  
console.log(pool.size);
```

## Index

### References

* [Args](src_core_pool.html#Args)
* [ArgsFn](src_core_pool.html#ArgsFn)
* [HashFn](src_core_pool.html#HashFn)
* [OptionalWrappedResource](src_core_pool.html#OptionalWrappedResource)
* [PoolHook](src_core_pool.html#PoolHook)
* [PoolOptions](src_core_pool.html#PoolOptions)
* [Resource](src_core_pool.html#Resource)
* [ResourceDestructor](src_core_pool.html#ResourceDestructor)
* [ResourceFactory](src_core_pool.html#ResourceFactory)
* [ResourceHook](src_core_pool.html#ResourceHook)
* [WrappedResource](src_core_pool.html#WrappedResource)
* [borrowCounter](src_core_pool.html#borrowCounter)
* [hashVal](src_core_pool.html#hashVal)

### Classes

* [default](../classes/src_core_pool.default.html)

## References

### Args

Re-exports [Args](src_core_pool_interface.html#Args)

### ArgsFn

Re-exports [ArgsFn](../interfaces/src_core_pool_interface.ArgsFn.html)

### HashFn

Re-exports [HashFn](../interfaces/src_core_pool_interface.HashFn.html)

### OptionalWrappedResource

Re-exports [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)

### PoolHook

Re-exports [PoolHook](../interfaces/src_core_pool_interface.PoolHook.html)

### PoolOptions

Re-exports [PoolOptions](../interfaces/src_core_pool_interface.PoolOptions.html)

### Resource

Re-exports [Resource](src_core_pool_interface.html#Resource)

### ResourceDestructor

Re-exports [ResourceDestructor](../interfaces/src_core_pool_interface.ResourceDestructor.html)

### ResourceFactory

Re-exports [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)

### ResourceHook

Re-exports [ResourceHook](../interfaces/src_core_pool_interface.ResourceHook.html)

### WrappedResource

Re-exports [WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)

### borrowCounter

Re-exports [borrowCounter](src_core_pool_const.html#borrowCounter)

### hashVal

Re-exports [hashVal](src_core_pool_const.html#hashVal)