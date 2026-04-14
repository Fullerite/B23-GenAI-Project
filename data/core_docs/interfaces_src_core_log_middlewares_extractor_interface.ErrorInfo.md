# Interface ErrorInfo
Recurrent structure that represents detailed error information

### Hierarchy

* ErrorInfo

## Index

### Properties

* [cause](src_core_log_middlewares_extractor_interface.ErrorInfo.html#cause)
* [details](src_core_log_middlewares_extractor_interface.ErrorInfo.html#details)
* [error](src_core_log_middlewares_extractor_interface.ErrorInfo.html#error)

## Properties

### Optional cause

cause?: [ErrorInfo](src_core_log_middlewares_extractor_interface.ErrorInfo.html)

* Defined in [src/core/log/middlewares/extractor/interface.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/interface.ts#L30)

Information of a caused error

### Optional details

details?: unknown

* Defined in [src/core/log/middlewares/extractor/interface.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/interface.ts#L25)

Error's details that could be extracted from it via error details extractors

### Optional error

error?: { message: string; name: string }

* Defined in [src/core/log/middlewares/extractor/interface.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/extractor/interface.ts#L17)

General info about an error.
Using only for cause errors and not for the root one.

#### Type declaration

* ##### message: string
* ##### name: string