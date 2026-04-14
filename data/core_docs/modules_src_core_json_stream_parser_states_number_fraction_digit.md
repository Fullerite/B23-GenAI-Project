# Module src/core/json/stream/parser/states/number-fraction-digit
## Index

### Functions

* [numberFractionDigit](src_core_json_stream_parser_states_number_fraction_digit.html#numberFractionDigit)

## Functions

### numberFractionDigit

* numberFractionDigit(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-fraction-digit.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-fraction-digit.ts#L17)

  Parses the buffer for number fraction digits `[0-9]` and generates a token `numberChunk` with a fraction value

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>