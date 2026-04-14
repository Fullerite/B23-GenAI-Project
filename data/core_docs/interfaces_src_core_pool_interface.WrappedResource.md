# Interface WrappedResource<T>
### Type parameters

* #### T = unknown

### Hierarchy

* WrappedResource
  + [OptionalWrappedResource](src_core_pool_interface.OptionalWrappedResource.html)

## Index

### Properties

* [value](src_core_pool_interface.WrappedResource.html#value)

### Methods

* [destroy](src_core_pool_interface.WrappedResource.html#destroy)
* [free](src_core_pool_interface.WrappedResource.html#free)

## Properties

### value

value: T

* Defined in [src/core/pool/interface.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L21)

Value from the pool

## Methods

### destroy

* destroy(): void

* + Defined in [src/core/pool/interface.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L32)

  Destroys the resource instead of returning it to the pool

  #### Returns void

### free

* free(...args: unknown[]): void

* + Defined in [src/core/pool/interface.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/pool/interface.ts#L27)

  Returns the resource to the pool

  #### Parameters

  + ##### Rest ...args: unknown[]

    extra arguments to pass to the `onFree` hook handler

  #### Returns void