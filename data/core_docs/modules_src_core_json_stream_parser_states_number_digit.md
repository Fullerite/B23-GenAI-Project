# Module src/core/json/stream/parser/states/number-digit
## Index

### Functions

* [numberDigit](src_core_json_stream_parser_states_number_digit.html#numberDigit)

## Functions

### numberDigit

* numberDigit(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-digit.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-digit.ts#L17)

  Parses the buffer and generates from digits `[0-9]*` a token `numberChunk` with a number value

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>