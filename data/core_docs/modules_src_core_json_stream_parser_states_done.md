# Module src/core/json/stream/parser/states/done
## Index

### Functions

* [done](src_core_json_stream_parser_states_done.html#done)

## Functions

### done

* done(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/done.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/done.ts#L17)

  Parses the buffer, adds tokens to close a numeric chunk if needed, and finishes the parsing

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>