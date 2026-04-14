# Interface RetryOptions<D>
Options to retry bad requests

### Type parameters

* #### D = unknown

  response data type

### Hierarchy

* RetryOptions

## Index

### Properties

* [attempts](src_core_request_interface.RetryOptions.html#attempts)

### Methods

* [delay](src_core_request_interface.RetryOptions.html#delay)

## Properties

### Optional attempts

attempts?: number

* Defined in [src/core/request/interface.ts:550](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L550)

Maximum number of attempts to request

## Methods

### Optional delay

* delay(attempt: number, error: [default](../classes/src_core_request_error.default.html)<D>): number | false | Promise<void>

* + Defined in [src/core/request/interface.ts:559](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L559)

  Returns a number in milliseconds (or a promise) to wait before the next attempt.
  If the function returns false, it will prevent all further attempts.

  #### Parameters

  + ##### attempt: number

    current attempt number
  + ##### error: [default](../classes/src_core_request_error.default.html)<D>

    error object

  #### Returns number | false | Promise<void>