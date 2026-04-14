# Module src/core/pool/interface
## Index

### Interfaces

* [ArgsFn](../interfaces/src_core_pool_interface.ArgsFn.html)
* [HashFn](../interfaces/src_core_pool_interface.HashFn.html)
* [OptionalWrappedResource](../interfaces/src_core_pool_interface.OptionalWrappedResource.html)
* [PoolHook](../interfaces/src_core_pool_interface.PoolHook.html)
* [PoolOptions](../interfaces/src_core_pool_interface.PoolOptions.html)
* [ResourceDestructor](../interfaces/src_core_pool_interface.ResourceDestructor.html)
* [ResourceFactory](../interfaces/src_core_pool_interface.ResourceFactory.html)
* [ResourceHook](../interfaces/src_core_pool_interface.ResourceHook.html)
* [WrappedResource](../interfaces/src_core_pool_interface.WrappedResource.html)

### Type aliases

* [Args](src_core_pool_interface.html#Args)
* [Resource](src_core_pool_interface.html#Resource)

## Type aliases

### Args

Args: unknown[] | [ArgsFn](../interfaces/src_core_pool_interface.ArgsFn.html)

* Defined in [src/core/pool/interface.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L85)

### Resource

Resource<T>: T & { [borrowCounter]: number; [hashVal]: string }

* Defined in [src/core/pool/interface.ts:12](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L12)

#### Type parameters

* #### T