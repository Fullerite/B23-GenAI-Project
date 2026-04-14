# Module src/core/json/stream/parser/interface
## Index

### Interfaces

* [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)
* [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)
* [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)

### Type aliases

* [ParentParserState](src_core_json_stream_parser_interface.html#ParentParserState)
* [ParserState](src_core_json_stream_parser_interface.html#ParserState)
* [TokenName](src_core_json_stream_parser_interface.html#TokenName)
* [TokenValue](src_core_json_stream_parser_interface.html#TokenValue)

## Type aliases

### ParentParserState

ParentParserState: typeof [OBJECT](src_core_json_stream_parser_const.html#parserStateTypes.__type-3.OBJECT) | typeof [ARRAY](src_core_json_stream_parser_const.html#parserStateTypes.__type-3.ARRAY) | typeof [EMPTY](src_core_json_stream_parser_const.html#parserStateTypes.__type-3.EMPTY)

* Defined in [src/core/json/stream/parser/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/interface.ts#L15)

### ParserState

ParserState: typeof [parserStateTypes](src_core_json_stream_parser_const.html#parserStateTypes)[keyof typeof [parserStateTypes](src_core_json_stream_parser_const.html#parserStateTypes)]

* Defined in [src/core/json/stream/parser/interface.ts:11](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/interface.ts#L11)

### TokenName

TokenName: "" | "startObject" | "endObject" | "startArray" | "endArray" | "startKey" | "stringChunk" | "endKey" | "keyValue" | "startString" | "endString" | "stringValue" | "startNumber" | "numberChunk" | "numberValue" | "endNumber" | "nullValue" | "trueValue" | "falseValue"

* Defined in [src/core/json/stream/parser/interface.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/interface.ts#L20)

### TokenValue

TokenValue: string | boolean | number | null

* Defined in [src/core/json/stream/parser/interface.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/interface.ts#L41)