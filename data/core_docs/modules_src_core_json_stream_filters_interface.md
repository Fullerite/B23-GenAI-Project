# Module src/core/json/stream/filters/interface
## Index

### Interfaces

* [FilterOptions](../interfaces/src_core_json_stream_filters_interface.FilterOptions.html)
* [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)
* [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)

### Type aliases

* [FilterStack](src_core_json_stream_filters_interface.html#FilterStack)
* [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter)

## Type aliases

### FilterStack

FilterStack: [Nullable](index.html#Nullable)<[TokenValue](src_core_json_stream_parser_interface.html#TokenValue)>[]

* Defined in [src/core/json/stream/filters/interface.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/interface.ts#L22)

### TokenFilter

TokenFilter: string | RegExp | [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)

* Defined in [src/core/json/stream/filters/interface.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/interface.ts#L30)