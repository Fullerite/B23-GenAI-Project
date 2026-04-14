# Class TestDetailedBaseError
### Hierarchy

* [default](src_core_error.default.html)
  + TestDetailedBaseError

## Index

### Constructors

* [constructor](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html#constructor)

### Properties

* [cause](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html#cause)
* [internalMessage](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html#internalMessage)
* [reason](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html#reason)

### Methods

* [format](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html#format)

## Constructors

### constructor

* new TestDetailedBaseError(message: string, reason: unknown, cause: Error): [TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)

* Overrides [default](src_core_error.default.html).[constructor](src_core_error.default.html#constructor)

  + Defined in [src/core/log/middlewares/extractor/testing.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/testing.ts#L25)

  #### Parameters

  + ##### message: string
  + ##### reason: unknown
  + ##### cause: Error

  #### Returns [TestDetailedBaseError](src_core_log_middlewares_extractor_testing.TestDetailedBaseError.html)

## Properties

### Optional Readonly cause

cause?: Error

Inherited from [default](src_core_error.default.html).[cause](src_core_error.default.html#cause)

* Defined in [src/core/error/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L23)

An error that causes the current error

### Protected Optional internalMessage

internalMessage?: string

Inherited from [default](src_core_error.default.html).[internalMessage](src_core_error.default.html#internalMessage)

* Defined in [src/core/error/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L28)

Internal storage for an error message

### Readonly reason

reason: unknown

* Defined in [src/core/log/middlewares/extractor/testing.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/testing.ts#L23)

## Methods

### Protected format

* format(): string

* Inherited from [default](src_core_error.default.html).[format](src_core_error.default.html#format)

  + Defined in [src/core/error/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L65)

  Formats internal error's data to produce a message.
  The method calls when accessing the `message` property.

  #### Returns string