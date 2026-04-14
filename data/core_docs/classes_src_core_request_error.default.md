# Class default<D>
Class to wrap any request error

### Type parameters

* #### D = undefined

### Hierarchy

* [default](src_core_error.default.html)
  + default

## Index

### Constructors

* [constructor](src_core_request_error.default.html#constructor)

### Properties

* [cause](src_core_request_error.default.html#cause)
* [details](src_core_request_error.default.html#details)
* [internalMessage](src_core_request_error.default.html#internalMessage)
* [type](src_core_request_error.default.html#type)
* [Abort](src_core_request_error.default.html#Abort)
* [Engine](src_core_request_error.default.html#Engine)
* [InvalidStatus](src_core_request_error.default.html#InvalidStatus)
* [Offline](src_core_request_error.default.html#Offline)
* [Timeout](src_core_request_error.default.html#Timeout)

### Methods

* [format](src_core_request_error.default.html#format)

## Constructors

### constructor

* new default<D>(type: string, details?: [Details](../interfaces/src_core_request_error_interface.Details.html)<D>): [default](src_core_request_error.default.html)<D>

* Overrides [default](src_core_error.default.html).[constructor](src_core_error.default.html#constructor)

  + Defined in [src/core/request/error/index.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L63)

  #### Type parameters

  + #### D = undefined

  #### Parameters

  + ##### type: string

    error type
  + ##### Optional details: [Details](../interfaces/src_core_request_error_interface.Details.html)<D>

    error details

  #### Returns [default](src_core_request_error.default.html)<D>

## Properties

### Optional Readonly cause

cause?: Error

Inherited from [default](src_core_error.default.html).[cause](src_core_error.default.html#cause)

* Defined in [src/core/error/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L23)

An error that causes the current error

### Readonly details

details: [Details](../interfaces/src_core_request_error_interface.Details.html)<D>

* Defined in [src/core/request/error/index.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L57)

Error details

### Protected Optional internalMessage

internalMessage?: string

Inherited from [default](src_core_error.default.html).[internalMessage](src_core_error.default.html#internalMessage)

* Defined in [src/core/error/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L28)

Internal storage for an error message

### Readonly type

type: string

* Defined in [src/core/request/error/index.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L52)

Error type

### Static Readonly Abort

Abort: string = 'abort'

* Defined in [src/core/request/error/index.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L32)

Default error type: a request was aborted

### Static Readonly Engine

Engine: string = 'engine'

* Defined in [src/core/request/error/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L47)

Default error type: a request was failed because of an internal request engine' error

### Static Readonly InvalidStatus

InvalidStatus: string = 'invalidStatus'

* Defined in [src/core/request/error/index.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L27)

Default error type: a server has responded with a non-ok status

### Static Readonly Offline

Offline: string = 'offline'

* Defined in [src/core/request/error/index.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L42)

Default error type: a request was failed because there is no connection to a network

### Static Readonly Timeout

Timeout: string = 'timeout'

* Defined in [src/core/request/error/index.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L37)

Default error type: a request was aborted because of a timeout

## Methods

### Protected format

* format(): string

* Overrides [default](src_core_error.default.html).[format](src_core_error.default.html#format)

  + Defined in [src/core/request/error/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/request/error/index.ts#L70)

  Formats internal error's data to produce a message.
  The method calls when accessing the `message` property.

  #### Returns string