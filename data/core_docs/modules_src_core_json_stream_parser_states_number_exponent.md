# Module src/core/json/stream/parser/states/number-exponent
## Index

### Functions

* [numberExponent](src_core_json_stream_parser_states_number_exponent.html#numberExponent)

## Functions

### numberExponent

* numberExponent(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/number-exponent.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/number-exponent.ts#L17)

  Parses the buffer for an exponent symbol `[eE]?` and generates a token `numberChunk` with a symbol value

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>