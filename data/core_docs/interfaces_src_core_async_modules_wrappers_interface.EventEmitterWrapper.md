# Interface EventEmitterWrapper<CTX>
### Type parameters

* #### CTX: object = [default](../classes/src_core_async.default.html)

### Hierarchy

* [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html)<CTX>
  + EventEmitterWrapper

## Index

### Methods

* [emit](src_core_async_modules_wrappers_interface.EventEmitterWrapper.html#emit)
* [off](src_core_async_modules_wrappers_interface.EventEmitterWrapper.html#off)
* [on](src_core_async_modules_wrappers_interface.EventEmitterWrapper.html#on)
* [once](src_core_async_modules_wrappers_interface.EventEmitterWrapper.html#once)
* [promisifyOnce](src_core_async_modules_wrappers_interface.EventEmitterWrapper.html#promisifyOnce)

## Methods

### emit

* emit(event: string, ...args: unknown[]): boolean

* + Defined in [src/core/async/modules/wrappers/interface.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L101)

  #### Parameters

  + ##### event: string
  + ##### Rest ...args: unknown[]

  #### Returns boolean

### off

* off(id?: object): void
* off(params: [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html)<object>): void

* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[off](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#off)

  + Defined in [src/core/async/modules/wrappers/interface.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L96)

  #### Parameters

  + ##### Optional id: object

  #### Returns void
* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[off](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#off)

  + Defined in [src/core/async/modules/wrappers/interface.ts:97](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L97)

  #### Parameters

  + ##### params: [ClearOptionsId](src_core_async_modules_base_interface.ClearOptionsId.html)<object>

  #### Returns void

### on

* on<E, R>(events: [CanArray](../modules/index.html#CanArray)<string>, handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>, ...args: unknown[]): object
* on<E, R>(events: [CanArray](../modules/index.html#CanArray)<string>, handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>, params: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html), ...args: unknown[]): object

* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[on](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#on)

  + Defined in [src/core/async/modules/wrappers/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L63)

  #### Type parameters

  + #### E = unknown
  + #### R = unknown

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<string>
  + ##### handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>
  + ##### Rest ...args: unknown[]

  #### Returns object
* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[on](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#on)

  + Defined in [src/core/async/modules/wrappers/interface.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L69)

  #### Type parameters

  + #### E = unknown
  + #### R = unknown

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<string>
  + ##### handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>
  + ##### params: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + ##### Rest ...args: unknown[]

  #### Returns object

### once

* once<E, R>(events: [CanArray](../modules/index.html#CanArray)<string>, handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>, ...args: unknown[]): object
* once<E, R>(events: [CanArray](../modules/index.html#CanArray)<string>, handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>, params: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html), ...args: unknown[]): object

* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[once](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#once)

  + Defined in [src/core/async/modules/wrappers/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L76)

  #### Type parameters

  + #### E = unknown
  + #### R = unknown

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<string>
  + ##### handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>
  + ##### Rest ...args: unknown[]

  #### Returns object
* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[once](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#once)

  + Defined in [src/core/async/modules/wrappers/interface.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L82)

  #### Type parameters

  + #### E = unknown
  + #### R = unknown

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<string>
  + ##### handler: [ProxyCb](../modules/src_core_async_modules_base_interface.html#ProxyCb)<E, R, CTX>
  + ##### params: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + ##### Rest ...args: unknown[]

  #### Returns object

### promisifyOnce

* promisifyOnce<T>(events: [CanArray](../modules/index.html#CanArray)<string>, ...args: unknown[]): Promise<[CanUndef](../modules/index.html#CanUndef)<T>>
* promisifyOnce<T>(events: [CanArray](../modules/index.html#CanArray)<string>, params: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html), ...args: unknown[]): Promise<[CanUndef](../modules/index.html#CanUndef)<T>>

* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[promisifyOnce](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#promisifyOnce)

  + Defined in [src/core/async/modules/wrappers/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L89)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<string>
  + ##### Rest ...args: unknown[]

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<T>>
* Inherited from [ReadonlyEventEmitterWrapper](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html).[promisifyOnce](src_core_async_modules_wrappers_interface.ReadonlyEventEmitterWrapper.html#promisifyOnce)

  + Defined in [src/core/async/modules/wrappers/interface.ts:90](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/wrappers/interface.ts#L90)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### events: [CanArray](../modules/index.html#CanArray)<string>
  + ##### params: [AsyncOptions](src_core_async_modules_base_interface.AsyncOptions.html)
  + ##### Rest ...args: unknown[]

  #### Returns Promise<[CanUndef](../modules/index.html#CanUndef)<T>>