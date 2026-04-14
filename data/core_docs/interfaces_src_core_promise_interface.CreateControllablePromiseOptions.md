# Interface CreateControllablePromiseOptions<T>
### Type parameters

* #### T: [ControllablePromiseConstructor](src_core_promise_interface.ControllablePromiseConstructor.html)

### Hierarchy

* CreateControllablePromiseOptions

## Index

### Properties

* [args](src_core_promise_interface.CreateControllablePromiseOptions.html#args)
* [type](src_core_promise_interface.CreateControllablePromiseOptions.html#type)

### Methods

* [executor](src_core_promise_interface.CreateControllablePromiseOptions.html#executor)

## Properties

### Optional args

args?: Iterable<any>

* Defined in [src/core/promise/interface.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/promise/interface.ts#L75)

Extra arguments to pass to the promise constructor

### Optional type

type?: T

* Defined in [src/core/promise/interface.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/promise/interface.ts#L57)

Promise constructor

default
:   `Promise`

## Methods

### Optional executor

* executor(resolve: [ControllablePromiseResolveHandler](src_core_promise_interface.ControllablePromiseResolveHandler.html)<unknown>, reject: [ControllablePromiseRejectHandler](src_core_promise_interface.ControllablePromiseRejectHandler.html), ...args: any[]): void

* + Defined in [src/core/promise/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/promise/interface.ts#L66)

  Promise constructor executor

  #### Parameters

  + ##### resolve: [ControllablePromiseResolveHandler](src_core_promise_interface.ControllablePromiseResolveHandler.html)<unknown>
  + ##### reject: [ControllablePromiseRejectHandler](src_core_promise_interface.ControllablePromiseRejectHandler.html)
  + ##### Rest ...args: any[]

  #### Returns void