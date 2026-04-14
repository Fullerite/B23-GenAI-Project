# Class TestError
### Hierarchy

* [default](src_core_error.default.html)
  + TestError

## Index

### Constructors

* [constructor](src_core_error_testing.TestError.html#constructor)

### Properties

* [cause](src_core_error_testing.TestError.html#cause)
* [internalMessage](src_core_error_testing.TestError.html#internalMessage)

### Methods

* [format](src_core_error_testing.TestError.html#format)

## Constructors

### constructor

* new TestError(message?: string, cause?: Error): [TestError](src_core_error_testing.TestError.html)

* Inherited from [default](src_core_error.default.html).[constructor](src_core_error.default.html#constructor)

  + Defined in [src/core/error/index.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L30)

  #### Parameters

  + ##### Optional message: string
  + ##### Optional cause: Error

  #### Returns [TestError](src_core_error_testing.TestError.html)

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

## Methods

### Protected format

* format(): string

* Inherited from [default](src_core_error.default.html).[format](src_core_error.default.html#format)

  + Defined in [src/core/error/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/error/index.ts#L65)

  Formats internal error's data to produce a message.
  The method calls when accessing the `message` property.

  #### Returns string