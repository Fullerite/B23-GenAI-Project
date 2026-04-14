# Module src/core/request/engines/helpers
## Index

### Functions

* [convertDataToSend](src_core_request_engines_helpers.html#convertDataToSend)

## Functions

### convertDataToSend

* convertDataToSend(data: unknown, contentType?: string): [[NormalizedRequestBody](src_core_request_interface.html#NormalizedRequestBody)?, string?]

* + Defined in [src/core/request/engines/helpers.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/request/engines/helpers.ts#L22)

  Converts the specified data to send via request engines.
  The function returns a tuple, where on the first position is converted data and its new content type on
  the second position.

  #### Parameters

  + ##### data: unknown
  + ##### Optional contentType: string

  #### Returns [[NormalizedRequestBody](src_core_request_interface.html#NormalizedRequestBody)?, string?]