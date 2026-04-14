# Module src/core/json/stream/parser/states/number-exp-sign
## Index

### Functions

* [numberExpSign](src_core_json_stream_parser_states_number_exp_sign.html#numberExpSign)

## Functions

### numberExpSign

* numberExpSign(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-exp-sign.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-exp-sign.ts#L17)

  Parses the buffer for signs `[-+]?*` and generates a token `numberChunk` with a sign

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>