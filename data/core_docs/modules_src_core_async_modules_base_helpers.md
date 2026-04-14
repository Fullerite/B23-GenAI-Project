# Module src/core/async/modules/base/helpers
## Index

### Variables

* [isParams](src_core_async_modules_base_helpers.html#isParams)

### Functions

* [isAsyncOptions](src_core_async_modules_base_helpers.html#isAsyncOptions)

## Variables

### Const isParams

isParams: [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<[value: unknown], boolean> = ...

* Defined in [src/core/async/modules/base/helpers.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/helpers.ts#L24)

deprecated

see
:   isAsyncOptions

## Functions

### isAsyncOptions

* isAsyncOptions<T>(value: unknown): value is T

* + Defined in [src/core/async/modules/base/helpers.ts:16](https://github.com/V4Fire/Core/blob/master/src/core/async/modules/base/helpers.ts#L16)

  Returns true if the specified value is looks like an instance of AsyncOptions

  #### Type parameters

  + #### T: object = [AsyncOptions](../interfaces/src_core_async_modules_base_interface.AsyncOptions.html)

  #### Parameters

  + ##### value: unknown

  #### Returns value is T