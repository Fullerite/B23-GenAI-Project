# Module src/core/json/stream/parser/states/number-exp-start
## Index

### Functions

* [numberExpStart](src_core_json_stream_parser_states_number_exp_start.html#numberExpStart)

## Functions

### numberExpStart

* numberExpStart(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-exp-start.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-exp-start.ts#L18)

  Parses the buffer for the first digit `[0-9]` in a numeric expression and
  generates a token `numberChunk` with a digit value

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>