# Module src/core/json/stream/parser/states/string
## Index

### Functions

* [string](src_core_json_stream_parser_states_string.html#string)

## Functions

### string

* string(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/string.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/string.ts#L30)

  Parses the buffer for the end of a key or string and generates a sequence of tokens
  `endKey`, `keyValue` for a key or `endString`, `stringValue` and `stringChunk` for a string

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>