# Module src/core/json/stream/parser/states/number-fraction-start
## Index

### Functions

* [numberFractionStart](src_core_json_stream_parser_states_number_fraction_start.html#numberFractionStart)

## Functions

### numberFractionStart

* numberFractionStart(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-fraction-start.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-fraction-start.ts#L18)

  Parse the buffer for the first digit in a number fraction `[0-9]`
  and generates a token `numberChunk` with a fraction value

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>