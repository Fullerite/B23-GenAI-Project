# Class default<T>
Implementation of an object pool structure

### Type parameters

* #### T = unknown

  pool resource

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_pool.default.html#constructor)

### Properties

* [availableResources](src_core_pool.default.html#availableResources)
* [borrowEventsInQueue](src_core_pool.default.html#borrowEventsInQueue)
* [borrowedResourceStore](src_core_pool.default.html#borrowedResourceStore)
* [emitter](src_core_pool.default.html#emitter)
* [events](src_core_pool.default.html#events)
* [hashFn](src_core_pool.default.html#hashFn)
* [maxSize](src_core_pool.default.html#maxSize)
* [onBorrow](src_core_pool.default.html#onBorrow)
* [onClear](src_core_pool.default.html#onClear)
* [onFree](src_core_pool.default.html#onFree)
* [onTake](src_core_pool.default.html#onTake)
* [resourceDestructor](src_core_pool.default.html#resourceDestructor)
* [resourceFactory](src_core_pool.default.html#resourceFactory)
* [resourceStore](src_core_pool.default.html#resourceStore)
* [unavailableResources](src_core_pool.default.html#unavailableResources)

### Accessors

* [available](src_core_pool.default.html#available)
* [size](src_core_pool.default.html#size)

### Methods

* [borrow](src_core_pool.default.html#borrow)
* [borrowOrCreate](src_core_pool.default.html#borrowOrCreate)
* [borrowOrWait](src_core_pool.default.html#borrowOrWait)
* [canBorrow](src_core_pool.default.html#canBorrow)
* [canTake](src_core_pool.default.html#canTake)
* [clear](src_core_pool.default.html#clear)
* [createResource](src_core_pool.default.html#createResource)
* [free](src_core_pool.default.html#free)
* [take](src_core_pool.default.html#take)
* [takeOrCreate](src_core_pool.default.html#takeOrCreate)
* [takeOrWait](src_core_pool.default.html#takeOrWait)
* [wrapResource](src_core_pool.default.html#wrapResource)

## Constructors

### constructor

* new default<T>(resourceFactory: [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)<T>, args: [Args](../modules/src_core_pool_interface.html#Args), opts?: [PoolOptions](../interfaces/src_core_pool_interface.PoolOptions.html)<T>): [default](src_core_pool.default.html)<T>
* new default<T>(resourceFactory: [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)<T>, opts?: [PoolOptions](../interfaces/src_core_pool_interface.PoolOptions.html)<T>): [default](src_core_pool.default.html)<T>

* + Defined in [src/core/pool/index.ts:146](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L146)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### resourceFactory: [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)<T>
  + ##### args: [Args](../modules/src_core_pool_interface.html#Args)

    extra arguments to pass to the resource factory during initialization
  + ##### Optional opts: [PoolOptions](../interfaces/src_core_pool_interface.PoolOptions.html)<T>

  #### Returns [default](src_core_pool.default.html)<T>
* + Defined in [src/core/pool/index.ts:156](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L156)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### resourceFactory: [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)<T>
  + ##### Optional opts: [PoolOptions](../interfaces/src_core_pool_interface.PoolOptions.html)<T>

  #### Returns [default](src_core_pool.default.html)<T>

## Properties

### Protected availableResources

availableResources: Set<[Resource](../modules/src_core_pool_interface.html#Resource)<[Resource](../modules/src_core_pool_interface.html#Resource)<T>>> = ...

* Defined in [src/core/pool/index.ts:104](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L104)

Set of all available resources

### Protected borrowEventsInQueue

borrowEventsInQueue: Map<string, string> = ...

* Defined in [src/core/pool/index.ts:119](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L119)

Map of active borrow events

### Protected borrowedResourceStore

borrowedResourceStore: Map<string, [Resource](../modules/src_core_pool_interface.html#Resource)<T>> = ...

* Defined in [src/core/pool/index.ts:99](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L99)

Store of borrowed pool resources

### Protected emitter

emitter: EventEmitter2 = ...

* Defined in [src/core/pool/index.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L89)

Event emitter to broadcast pool events

see
:   [[EventEmitter]]

### Protected events

events: Map<string, [default](src_core_queue_simple.default.html)<string>> = ...

* Defined in [src/core/pool/index.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L114)

Queue of active events

### Protected hashFn

hashFn: [HashFn](../interfaces/src_core_pool_interface.HashFn.html)

* Defined in [src/core/pool/index.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L83)

A function to calculate a hash string for the specified arguments

### Readonly maxSize

maxSize: number = Infinity

* Defined in [src/core/pool/index.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L53)

The maximum number of resources that the pool can contain

### Protected Optional onBorrow

onBorrow?: [ResourceHook](../interfaces/src_core_pool_interface.ResourceHook.html)<T>

* Defined in [src/core/pool/index.ts:129](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L129)

Handler: taking some resource via `borrow` methods

### Protected Optional onClear

onClear?: [PoolHook](../interfaces/src_core_pool_interface.PoolHook.html)<T>

* Defined in [src/core/pool/index.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L139)

Handler: clearing of all pool resources

### Protected Optional onFree

onFree?: [ResourceHook](../interfaces/src_core_pool_interface.ResourceHook.html)<T>

* Defined in [src/core/pool/index.ts:134](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L134)

Handler: releasing of some resource

### Protected Optional onTake

onTake?: [ResourceHook](../interfaces/src_core_pool_interface.ResourceHook.html)<T>

* Defined in [src/core/pool/index.ts:124](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L124)

Handler: taking some resource via `take` methods

### Protected Optional resourceDestructor

resourceDestructor?: [ResourceDestructor](../interfaces/src_core_pool_interface.ResourceDestructor.html)<T>

* Defined in [src/core/pool/index.ts:78](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L78)

A function to destroy one resource from the pool

### Protected resourceFactory

resourceFactory: [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)<T>

* Defined in [src/core/pool/index.ts:73](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L73)

A factory to create a new resource for the pool.
The function take arguments that are passed to `takeOrCreate`, `borrowAndCreate`, etc.

### Protected resourceStore

resourceStore: Map<string, [Resource](../modules/src_core_pool_interface.html#Resource)<T>[]> = ...

* Defined in [src/core/pool/index.ts:94](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L94)

Store of pool resources

### Protected unavailableResources

unavailableResources: Set<[Resource](../modules/src_core_pool_interface.html#Resource)<[Resource](../modules/src_core_pool_interface.html#Resource)<T>>> = ...

* Defined in [src/core/pool/index.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L109)

Set of all unavailable resources

## Accessors

### available

* get available(): number

* + Defined in [src/core/pool/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L65)

  Number of available resources that are stored in the pool

  #### Returns number

### size

* get size(): number

* + Defined in [src/core/pool/index.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L58)

  Number of resources that are stored in the pool

  #### Returns number

## Methods

### borrow

* borrow(...args: unknown[]): [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)<T>

* + Defined in [src/core/pool/index.ts:279](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L279)

  Borrows an available resource from the pool.
  The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

  When a resource is borrowed, it won’t be dropped from the pool. I.e. you can share it with other consumers.
  Mind, you can’t take this resource from the pool when it’s borrowed.

  The returned result is wrapped with a structure that contains methods to release or drop this resource.
  If the pool is empty, the structure value field will be nullish.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)<T>

### borrowOrCreate

* borrowOrCreate(...args: unknown[]): [WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>

* + Defined in [src/core/pool/index.ts:312](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L312)

  Borrows an available resource from the pool.
  The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

  When a resource is borrowed, it won’t be dropped from the pool. I.e. you can share it with other consumers.
  Mind, you can’t take this resource from the pool when it’s borrowed.

  The returned result is wrapped with a structure that contains methods to release or drop this resource.
  If the pool is empty, it creates a new resource and returns it.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>

### borrowOrWait

* borrowOrWait(...args: unknown[]): [default](src_core_prelude_structures_sync_promise.default.html)<[WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>>

* + Defined in [src/core/pool/index.ts:332](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L332)

  Returns a promise with a borrowed resource from the pull.
  The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

  When a resource is borrowed, it won’t be dropped from the pool. I.e. you can share it with other consumers.
  Mind, you can’t take this resource from the pool when it’s borrowed.

  The returned result is wrapped with a structure that contains methods to release or drop this resource.
  If the pool is empty, the promise will wait till it release.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<[WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>>

### Protected canBorrow

* canBorrow(...args: unknown[]): boolean

* + Defined in [src/core/pool/index.ts:415](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L415)

  Checks if you can borrow a resource.
  The passed arguments will be used to calculate a resource hash.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns boolean

### Protected canTake

* canTake(...args: unknown[]): number

* + Defined in [src/core/pool/index.ts:404](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L404)

  Returns how many elements of the specified kind you can take.
  The method takes arguments that will be used to calculate a resource hash.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns number

### clear

* clear(...args: unknown[]): void

* + Defined in [src/core/pool/index.ts:373](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L373)

  Clears the pool, i.e. drops all created resource.
  The method takes arguments that will be provided to hook handlers.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns void

### Protected createResource

* createResource(...args: unknown[]): [Resource](../modules/src_core_pool_interface.html#Resource)<T>

* + Defined in [src/core/pool/index.ts:426](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L426)

  Creates a resource and stores it in the pool.
  The method takes arguments that will be provided to a resource factory.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [Resource](../modules/src_core_pool_interface.html#Resource)<T>

### Protected free

* free(resource: [Resource](../modules/src_core_pool_interface.html#Resource)<T>, ...args: unknown[]): void

* + Defined in [src/core/pool/index.ts:520](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L520)

  Releases the specified resource.
  The method takes arguments that will be provided to hook handlers.

  #### Parameters

  + ##### resource: [Resource](../modules/src_core_pool_interface.html#Resource)<T>
  + ##### Rest ...args: unknown[]

  #### Returns void

### take

* take(...args: unknown[]): [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)<T>

* + Defined in [src/core/pool/index.ts:198](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L198)

  Returns an available resource from the pool.
  The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

  The returned result is wrapped with a structure that contains methods to release or drop this resource.
  If the pool is empty, the structure value field will be nullish.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)<T>

### takeOrCreate

* takeOrCreate(...args: unknown[]): [WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>

* + Defined in [src/core/pool/index.ts:226](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L226)

  Returns an available resource from the pool.
  The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

  The returned result is wrapped with a structure that contains methods to release or drop this resource.
  If the pool is empty, it creates a new resource and returns it.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>

### takeOrWait

* takeOrWait(...args: unknown[]): [default](src_core_prelude_structures_sync_promise.default.html)<[WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>>

* + Defined in [src/core/pool/index.ts:243](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L243)

  Returns a promise with an available resource from the pull.
  The passed arguments will be used to calculate a resource hash. Also, they will be provided to hook handlers.

  The returned result is wrapped with a structure that contains methods to release or drop this resource.
  If the pool is empty, the promise will wait till it release.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns [default](src_core_prelude_structures_sync_promise.default.html)<[WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)<T>>

### Protected wrapResource

* wrapResource(resource: null | [Resource](../modules/src_core_pool_interface.html#Resource)<T>): [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)<T>

* + Defined in [src/core/pool/index.ts:467](https://github.com/V4Fire/Core/blob/master/src/core/pool/index.ts#L467)

  Wraps the specified resource and returns the wrapper

  #### Parameters

  + ##### resource: null | [Resource](../modules/src_core_pool_interface.html#Resource)<T>

  #### Returns [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)<T>