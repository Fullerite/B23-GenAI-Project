# Class default
Superclass of any error to inherit

### Hierarchy

* Error
  + default
    - [TestError](src_core_error_testing.TestError.html)
    - [TestBaseError](src_core_log_middlewares_extractor_testing.TestBaseError.html)
    - [TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)
    - [default](src_core_request_error.default.html)

## Index

### Constructors

* [constructor](src_core_error.default.html#constructor)

### Properties

* [cause](src_core_error.default.html#cause)
* [internalMessage](src_core_error.default.html#internalMessage)

### Methods

* [format](src_core_error.default.html#format)

## Constructors

### constructor

* new default(message?: string, cause?: Error): [default](src_core_error.default.html)

* Overrides Error.constructor

  + Defined in [src/core/error/index.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L30)

  #### Parameters

  + ##### Optional message: string
  + ##### Optional cause: Error

  #### Returns [default](src_core_error.default.html)

## Properties

### Optional Readonly cause

cause?: Error

Overrides Error.cause

* Defined in [src/core/error/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L23)

An error that causes the current error

### Protected Optional internalMessage

internalMessage?: string

* Defined in [src/core/error/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L28)

Internal storage for an error message

## Methods

### Protected format

* format(): string

* + Defined in [src/core/error/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L65)

  Formats internal error's data to produce a message.
  The method calls when accessing the `message` property.

  #### Returns string