# Module src/core/request/helpers/interpolation
## Index

### Functions

* [applyQueryForStr](src_core_request_helpers_interpolation.html#applyQueryForStr)

## Functions

### applyQueryForStr

* applyQueryForStr(str: string, query?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>, rgxp?: RegExp): string

* + Defined in [src/core/request/helpers/interpolation.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/request/helpers/interpolation.ts#L19)

  Applies a query object for the specified string
  (used keys are removed from the query)

  #### Parameters

  + ##### str: string
  + ##### Optional query: [Dictionary](../interfaces/index.Dictionary.html)<unknown>
  + ##### rgxp: RegExp = tplRgxp

  #### Returns string