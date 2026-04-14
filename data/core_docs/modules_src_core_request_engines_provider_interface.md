# Module src/core/request/engines/provider/interface
## Index

### Interfaces

* [AvailableOptions](../interfaces/src_core_request_engines_provider_interface.AvailableOptions.html)
* [Meta](../interfaces/src_core_request_engines_provider_interface.Meta.html)

### Type aliases

* [MethodsMapping](src_core_request_engines_provider_interface.html#MethodsMapping)

## Type aliases

### MethodsMapping

MethodsMapping: { [ key in [ModelMethod](src_core_data_interface_types.html#ModelMethod)]?: [ModelMethod](src_core_data_interface_types.html#ModelMethod) } & { [ key in [RequestMethod](src_core_request_interface.html#RequestMethod)]?: [ModelMethod](src_core_data_interface_types.html#ModelMethod) }

* Defined in [src/core/request/engines/provider/interface.ts:54](https://github.com/V4Fire/Core/blob/master/src/core/request/engines/provider/interface.ts#L54)

Mapping of methods to request for the engine