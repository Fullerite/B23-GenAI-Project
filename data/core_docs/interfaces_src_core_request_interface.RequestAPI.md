# Interface RequestAPI
A map of API parameters.

These parameters apply if the original request URL is not absolute, and they can be used to customize the
base API URL depending on the runtime environment. If you define the base API URL via
`config#api` or `globalOpts.api`, these parameters will be mapped on it.

### Hierarchy

* RequestAPI

## Index

### Properties

* [auth](src_core_request_interface.RequestAPI.html#auth)
* [domain2](src_core_request_interface.RequestAPI.html#domain2)
* [domain3](src_core_request_interface.RequestAPI.html#domain3)
* [domain4](src_core_request_interface.RequestAPI.html#domain4)
* [domain5](src_core_request_interface.RequestAPI.html#domain5)
* [domain6](src_core_request_interface.RequestAPI.html#domain6)
* [namespace](src_core_request_interface.RequestAPI.html#namespace)
* [port](src_core_request_interface.RequestAPI.html#port)
* [protocol](src_core_request_interface.RequestAPI.html#protocol)
* [url](src_core_request_interface.RequestAPI.html#url)
* [zone](src_core_request_interface.RequestAPI.html#zone)

## Properties

### Optional auth

auth?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:596](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L596)

Value for an API authorization part

example
:   `'login:password'`

### Optional domain2

domain2?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:621](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L621)

Value for an API domain level 2 part

### Optional domain3

domain3?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:616](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L616)

Value for an API domain level 3 part

### Optional domain4

domain4?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:611](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L611)

Value for an API domain level 4 part

### Optional domain5

domain5?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:606](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L606)

Value for an API domain level 5 part

### Optional domain6

domain6?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:601](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L601)

Value for an API domain level 6 part

### Optional namespace

namespace?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:636](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L636)

Value for an API namespace part: it follows after '/' character

### Optional port

port?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string | number>

* Defined in [src/core/request/interface.ts:631](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L631)

Value for an API api port

### Optional protocol

protocol?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:588](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L588)

API protocol

example
:   `'http'`
    `'https'`

### Optional url

url?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:579](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L579)

The direct value of API URL.
If this parameter is defined, all other parameters will be ignored.

example
:   `'https://google.com'`

### Optional zone

zone?: [RequestAPIValue](../modules/src_core_request_interface.html#RequestAPIValue)<string>

* Defined in [src/core/request/interface.ts:626](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L626)

Value for an API domain zone part