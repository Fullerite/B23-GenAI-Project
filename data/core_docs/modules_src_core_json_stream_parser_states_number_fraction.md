# Module src/core/json/stream/parser/states/number-fraction
## Index

### Functions

* [numberFraction](src_core_json_stream_parser_states_number_fraction.html#numberFraction)

## Functions

### numberFraction

* numberFraction(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-fraction.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-fraction.ts#L17)

  Parses the buffer for a numeric fraction symbol `[\.eE]?` and generates a token `numberChunk` with a fraction symbol

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>