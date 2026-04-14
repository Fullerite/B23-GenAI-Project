# Interface OptionalWrappedResource<T>
### Type parameters

* #### T

### Hierarchy

* [WrappedResource](src_core_pool_interface.WrappedResource.html)<[Nullable](../modules/index.html#Nullable)<T>>
  + OptionalWrappedResource

## Index

### Properties

* [value](src_core_pool_interface.OptionalWrappedResource.html#value)

### Methods

* [destroy](src_core_pool_interface.OptionalWrappedResource.html#destroy)
* [free](src_core_pool_interface.OptionalWrappedResource.html#free)

## Properties

### value

value: [Nullable](../modules/index.html#Nullable)<T>

Inherited from [WrappedResource](src_core_pool_interface.WrappedResource.html).[value](src_core_pool_interface.WrappedResource.html#value)

* Defined in [src/core/pool/interface.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L21)

Value from the pool

## Methods

### destroy

* destroy(): void

* Inherited from [WrappedResource](src_core_pool_interface.WrappedResource.html).[destroy](src_core_pool_interface.WrappedResource.html#destroy)

  + Defined in [src/core/pool/interface.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L32)

  Destroys the resource instead of returning it to the pool

  #### Returns void

### free

* free(...args: unknown[]): void

* Inherited from [WrappedResource](src_core_pool_interface.WrappedResource.html).[free](src_core_pool_interface.WrappedResource.html#free)

  + Defined in [src/core/pool/interface.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L27)

  Returns the resource to the pool

  #### Parameters

  + ##### Rest ...args: unknown[]

    extra arguments to pass to the `onFree` hook handler

  #### Returns void