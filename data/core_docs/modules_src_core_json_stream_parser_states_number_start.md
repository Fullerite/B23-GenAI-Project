# Module src/core/json/stream/parser/states/number-start
## Index

### Functions

* [numberStart](src_core_json_stream_parser_states_number_start.html#numberStart)

## Functions

### numberStart

* numberStart(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-start.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-start.ts#L17)

  Parses the buffer for number digits `[0-9]` and generates a token `numberChunk` with a number

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>