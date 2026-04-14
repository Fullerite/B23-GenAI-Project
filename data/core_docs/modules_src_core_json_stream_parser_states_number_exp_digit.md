# Module src/core/json/stream/parser/states/number-exp-digit
## Index

### Functions

* [numberExpDigit](src_core_json_stream_parser_states_number_exp_digit.html#numberExpDigit)

## Functions

### numberExpDigit

* numberExpDigit(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-exp-digit.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-exp-digit.ts#L17)

  Parses the buffer for a digit expression `[0-9]*` and generates a token `numberChunk` with a number value

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>