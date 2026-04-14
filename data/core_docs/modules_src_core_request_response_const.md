# Module src/core/request/response/const
## Index

### Variables

* [defaultResponseOpts](src_core_request_response_const.html#defaultResponseOpts)
* [noContentStatusCodes](src_core_request_response_const.html#noContentStatusCodes)

## Variables

### Const defaultResponseOpts

defaultResponseOpts: { headers: {}; okStatuses: [default](../classes/src_core_range.default.html)<200 | 299>; redirected: boolean; responseType: [ResponseType](src_core_request_response_interface.html#ResponseType); status: number; statusText: string; url: string } = ...

* Defined in [src/core/request/response/const.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/request/response/const.ts#L13)

#### Type declaration

* ##### headers: {}
* ##### okStatuses: [default](../classes/src_core_range.default.html)<200 | 299>
* ##### redirected: boolean
* ##### responseType: [ResponseType](src_core_request_response_interface.html#ResponseType)
* ##### status: number
* ##### statusText: string
* ##### url: string

### Const noContentStatusCodes

noContentStatusCodes: number[] = ...

* Defined in [src/core/request/response/const.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/request/response/const.ts#L30)

Status codes that cannot contain any content according to the HTTP standard

1xx - <https://tools.ietf.org/html/rfc7231#section-6.2>
204 - <https://tools.ietf.org/html/rfc7231#section-6.3.5>
304 - <https://tools.ietf.org/html/rfc7232#section-4.1>