# Module src/core/data/interface/types
## Index

### Interfaces

* [ExtraProvider](../interfaces/src_core_data_interface_types.ExtraProvider.html)
* [ExtraProviderParams](../interfaces/src_core_data_interface_types.ExtraProviderParams.html)
* [Mock](../interfaces/src_core_data_interface_types.Mock.html)
* [MockCustomResponse](../interfaces/src_core_data_interface_types.MockCustomResponse.html)
* [MockResponseFunction](../interfaces/src_core_data_interface_types.MockResponseFunction.html)
* [ProviderConstructor](../interfaces/src_core_data_interface_types.ProviderConstructor.html)
* [ProviderOptions](../interfaces/src_core_data_interface_types.ProviderOptions.html)

### Type aliases

* [DecodersMap](src_core_data_interface_types.html#DecodersMap)
* [EncodersMap](src_core_data_interface_types.html#EncodersMap)
* [ExtraProviderConstructor](src_core_data_interface_types.html#ExtraProviderConstructor)
* [ExtraProviders](src_core_data_interface_types.html#ExtraProviders)
* [FunctionalExtraProviders](src_core_data_interface_types.html#FunctionalExtraProviders)
* [MockResponse](src_core_data_interface_types.html#MockResponse)
* [MockResponseValue](src_core_data_interface_types.html#MockResponseValue)
* [Mocks](src_core_data_interface_types.html#Mocks)
* [ModelMethod](src_core_data_interface_types.html#ModelMethod)

## Type aliases

### DecodersMap

DecodersMap: Record<[ModelMethod](src_core_data_interface_types.html#ModelMethod) | "def", [Decoders](src_core_request_interface.html#Decoders)> | {}

* Defined in [src/core/data/interface/types.ts:106](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L106)

### EncodersMap

EncodersMap: Record<[ModelMethod](src_core_data_interface_types.html#ModelMethod) | "def", [Encoders](src_core_request_interface.html#Encoders)> | {}

* Defined in [src/core/data/interface/types.ts:105](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L105)

### ExtraProviderConstructor

ExtraProviderConstructor: string | [Provider](../interfaces/src_core_data_interface.Provider.html) | [ProviderConstructor](../interfaces/src_core_data_interface_types.ProviderConstructor.html)

* Defined in [src/core/data/interface/types.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L84)

### ExtraProviders

ExtraProviders<D>: [Dictionary](../interfaces/index.Dictionary.html)<[Nullable](index.html#Nullable)<[ExtraProvider](../interfaces/src_core_data_interface_types.ExtraProvider.html)<D>>>

* Defined in [src/core/data/interface/types.ts:97](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L97)

#### Type parameters

* #### D = unknown

### FunctionalExtraProviders

FunctionalExtraProviders<D>: [ExtraProviders](src_core_data_interface_types.html#ExtraProviders)<D> | ((params: [ExtraProviderParams](../interfaces/src_core_data_interface_types.ExtraProviderParams.html)<D>) => [CanUndef](index.html#CanUndef)<[ExtraProviders](src_core_data_interface_types.html#ExtraProviders)<D>>)

* Defined in [src/core/data/interface/types.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L101)

#### Type parameters

* #### D = unknown

### MockResponse

MockResponse<D>: [CanPromise](index.html#CanPromise)<[MockResponseValue](src_core_data_interface_types.html#MockResponseValue)> | [MockResponseFunction](../interfaces/src_core_data_interface_types.MockResponseFunction.html)<D>

* Defined in [src/core/data/interface/types.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L41)

#### Type parameters

* #### D = unknown

### MockResponseValue

MockResponseValue: [ResponseTypeValue](src_core_request_response_interface.html#ResponseTypeValue) | object

* Defined in [src/core/data/interface/types.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L27)

### Mocks

Mocks: [CanPromise](index.html#CanPromise)<{ [ key in [RequestMethod](src_core_request_interface.html#RequestMethod)]?: [Mock](../interfaces/src_core_data_interface_types.Mock.html)[] } | { default: { [ key in [RequestMethod](src_core_request_interface.html#RequestMethod)]?: [Mock](../interfaces/src_core_data_interface_types.Mock.html)[] } }>

* Defined in [src/core/data/interface/types.ts:54](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L54)

### ModelMethod

ModelMethod: "peek" | "get" | "post" | "add" | "upd" | "del"

* Defined in [src/core/data/interface/types.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/data/interface/types.ts#L59)