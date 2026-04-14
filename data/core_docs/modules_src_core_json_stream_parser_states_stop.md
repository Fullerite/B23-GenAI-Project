# Module src/core/json/stream/parser/states/stop
## Index

### Functions

* [stop](src_core_json_stream_parser_states_stop.html#stop)

## Functions

### stop

* stop(this: [default](../classes/src_core_json_stream_parser.default.html)): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/parser/states/stop.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/states/stop.ts#L18)

  Parses the buffer for the end of the current structure (an object or array) and
  generates tokens `endObject` or `endArray`

  #### Parameters

  + ##### this: [default](../classes/src_core_json_stream_parser.default.html)

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>