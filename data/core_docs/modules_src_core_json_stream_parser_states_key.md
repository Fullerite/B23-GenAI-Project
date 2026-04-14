# Module src/core/json/stream/parser/states/key
## Index

### Functions

* [key](src_core_json_stream_parser_states_key.html#key)

## Functions

### key

* key(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/key.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/key.ts#L18)

  Parses the buffer for an object key and generates a token `startKey`.
  Or if the object ended generates `endObject` token.

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>