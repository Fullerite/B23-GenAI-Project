# Interface PoolOptions<T>
### Type parameters

* #### T = unknown

### Hierarchy

* PoolOptions

## Index

### Properties

* [hashFn](src_core_pool_interface.PoolOptions.html#hashFn)
* [maxSize](src_core_pool_interface.PoolOptions.html#maxSize)
* [onBorrow](src_core_pool_interface.PoolOptions.html#onBorrow)
* [onClear](src_core_pool_interface.PoolOptions.html#onClear)
* [onFree](src_core_pool_interface.PoolOptions.html#onFree)
* [onTake](src_core_pool_interface.PoolOptions.html#onTake)
* [resourceDestructor](src_core_pool_interface.PoolOptions.html#resourceDestructor)
* [size](src_core_pool_interface.PoolOptions.html#size)

## Properties

### Optional hashFn

hashFn?: [HashFn](src_core_pool_interface.HashFn.html)

* Defined in [src/core/pool/interface.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L58)

A function to calculate a hash string for the specified arguments

### Optional maxSize

maxSize?: number

* Defined in [src/core/pool/interface.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L48)

The maximum number of resources that the pool can contain

default
:   `Infinity`

### Optional onBorrow

onBorrow?: [ResourceHook](src_core_pool_interface.ResourceHook.html)<T>

* Defined in [src/core/pool/interface.ts:68](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L68)

Handler: taking some resource via `borrow` methods

### Optional onClear

onClear?: [PoolHook](src_core_pool_interface.PoolHook.html)<T>

* Defined in [src/core/pool/interface.ts:78](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L78)

Handler: clearing of all pool resources

### Optional onFree

onFree?: [ResourceHook](src_core_pool_interface.ResourceHook.html)<T>

* Defined in [src/core/pool/interface.ts:73](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L73)

Handler: releasing of some resource

### Optional onTake

onTake?: [ResourceHook](src_core_pool_interface.ResourceHook.html)<T>

* Defined in [src/core/pool/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L63)

Handler: taking some resource via `take` methods

### Optional resourceDestructor

resourceDestructor?: [ResourceDestructor](src_core_pool_interface.ResourceDestructor.html)<T>

* Defined in [src/core/pool/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L53)

A function to destroy one resource from the pool

### Optional size

size?: number

* Defined in [src/core/pool/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L42)

Number of resources to create at pull initialization

default
:   `0`