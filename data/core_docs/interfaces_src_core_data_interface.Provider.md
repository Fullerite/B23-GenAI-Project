# Interface Provider
Base interface of a data provider

### Hierarchy

* Provider

### Implemented by

* [default](../classes/src_core_data_modules_base.default.html)

## Index

### Properties

* [alias](src_core_data_interface.Provider.html#alias)
* [emitter](src_core_data_interface.Provider.html#emitter)
* [event](src_core_data_interface.Provider.html#event)
* [providerName](src_core_data_interface.Provider.html#providerName)

### Methods

* [add](src_core_data_interface.Provider.html#add)
* [base](src_core_data_interface.Provider.html#base)
* [del](src_core_data_interface.Provider.html#del)
* [dropCache](src_core_data_interface.Provider.html#dropCache)
* [get](src_core_data_interface.Provider.html#get)
* [method](src_core_data_interface.Provider.html#method)
* [name](src_core_data_interface.Provider.html#name)
* [peek](src_core_data_interface.Provider.html#peek)
* [post](src_core_data_interface.Provider.html#post)
* [upd](src_core_data_interface.Provider.html#upd)
* [url](src_core_data_interface.Provider.html#url)

## Properties

### Optional Readonly alias

alias?: string

* Defined in [src/core/data/interface/index.ts:44](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L44)

Provider alias

### Readonly emitter

emitter: [EventEmitterLike](src_core_async_modules_events_interface.EventEmitterLike.html)

* Defined in [src/core/data/interface/index.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L49)

Event emitter to broadcast provider events

### Readonly event

event: [EventEmitterLike](src_core_async_modules_events_interface.EventEmitterLike.html)

* Defined in [src/core/data/interface/index.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L55)

deprecated

see
:   [Provider.emitter](src_core_data_interface.Provider.html#emitter)

### Readonly providerName

providerName: string

* Defined in [src/core/data/interface/index.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L39)

Full name of the provider including a namespace

## Methods

### add

* add<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/interface/index.ts:151](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L151)

  Add new data to the provider.
  This method is similar for a POST request.

  emits
  :   `add<T>(data: () => AbortablePromise<T>)`

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

### base

* base(): string
* base(value: string): [Provider](src_core_data_interface.Provider.html)

* + Defined in [src/core/data/interface/index.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L88)

  Returns the base part of URL of any request

  #### Returns string
* + Defined in [src/core/data/interface/index.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L96)

  Sets the base part of URL for any request.
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: string

  #### Returns [Provider](src_core_data_interface.Provider.html)

### del

* del<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/interface/index.ts:171](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L171)

  Deletes data of the provider by a query.
  This method is similar for a DELETE request.

  emits
  :   `del<T>(data: () => AbortablePromise<T>)`

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

### dropCache

* dropCache(): void

* + Defined in [src/core/data/interface/index.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L114)

  Drops the request cache of the current provider

  #### Returns void

### get

* get<D>(query?: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery), opts?: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/interface/index.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L123)

  Requests the provider for data by a query.
  This method is similar for a GET request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional query: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)
  + ##### Optional opts: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

### method

* method(): [CanUndef](../modules/index.html#CanUndef)<[RequestMethod](../modules/src_core_request_interface.html#RequestMethod)>
* method(value: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)): [Provider](src_core_data_interface.Provider.html)

* + Defined in [src/core/data/interface/index.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L75)

  Returns the custom HTTP request method of any request

  #### Returns [CanUndef](../modules/index.html#CanUndef)<[RequestMethod](../modules/src_core_request_interface.html#RequestMethod)>
* + Defined in [src/core/data/interface/index.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L83)

  Sets the custom HTTP request method for any request.
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)

  #### Returns [Provider](src_core_data_interface.Provider.html)

### name

* name(): [CanUndef](../modules/index.html#CanUndef)<[ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)>
* name(value: [ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)): [Provider](src_core_data_interface.Provider.html)

* + Defined in [src/core/data/interface/index.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L61)

  Returns the custom logical name of any request.
  If a request has the name, then it will fire an event with the same name after successful receiving.

  #### Returns [CanUndef](../modules/index.html#CanUndef)<[ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)>
* + Defined in [src/core/data/interface/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L70)

  Sets the custom logical name for any request.
  If a request has the name, then it will fire an event with the same name after successful receiving.
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: [ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)

  #### Returns [Provider](src_core_data_interface.Provider.html)

### peek

* peek<D>(query?: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery), opts?: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/interface/index.ts:132](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L132)

  Checks accessibility of the provider by a query.
  This method is similar for a HEAD request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional query: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)
  + ##### Optional opts: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

### post

* post<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/interface/index.ts:141](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L141)

  Sends custom data to the provider without any logically effect.
  This method is similar for a POST request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

### upd

* upd<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/interface/index.ts:161](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L161)

  Updates data of the provider by a query.
  This method is similar for a PUT request.

  emits
  :   `upd<T>(data: () => AbortablePromise<T>)`

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](src_core_request_interface.RequestPromise.html)<D>

### url

* url(): string
* url(value: string): [Provider](src_core_data_interface.Provider.html)

* + Defined in [src/core/data/interface/index.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L101)

  Returns the full URL of any request

  #### Returns string
* + Defined in [src/core/data/interface/index.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/index.ts#L109)

  Sets an extra URL part for any request (it is concatenated with the base part of URL).
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: string

  #### Returns [Provider](src_core_data_interface.Provider.html)