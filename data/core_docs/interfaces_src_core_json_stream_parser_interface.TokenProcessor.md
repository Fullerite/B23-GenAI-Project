# Interface TokenProcessor<T>
### Type parameters

* #### T

### Hierarchy

* TokenProcessor

### Implemented by

* [default](../classes/src_core_json_stream_assembler.default.html)
* [default](../classes/src_core_json_stream_filters_abstract_filter.default.html)
* [default](../classes/src_core_json_stream_streamers_interface.default.html)

## Index

### Properties

* [processToken](src_core_json_stream_parser_interface.TokenProcessor.html#processToken)

### Methods

* [finishTokenProcessing](src_core_json_stream_parser_interface.TokenProcessor.html#finishTokenProcessing)

## Properties

### processToken

processToken: [TokenProcessorFn](src_core_json_stream_parser_interface.TokenProcessorFn.html)<T>

* Defined in [src/core/json/stream/parser/interface.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/interface.ts#L57)

## Methods

### Optional finishTokenProcessing

* finishTokenProcessing(): Generator<T, any, unknown>

* + Defined in [src/core/json/stream/parser/interface.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/interface.ts#L58)

  #### Returns Generator<T, any, unknown>