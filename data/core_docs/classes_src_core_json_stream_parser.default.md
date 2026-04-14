# Class default
### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_json_stream_parser.default.html#constructor)

### Properties

* [accumulator](src_core_json_stream_parser.default.html#accumulator)
* [buffer](src_core_json_stream_parser.default.html#buffer)
* [expected](src_core_json_stream_parser.default.html#expected)
* [index](src_core_json_stream_parser.default.html#index)
* [isOpenNumber](src_core_json_stream_parser.default.html#isOpenNumber)
* [matched](src_core_json_stream_parser.default.html#matched)
* [parent](src_core_json_stream_parser.default.html#parent)
* [patterns](src_core_json_stream_parser.default.html#patterns)
* [stack](src_core_json_stream_parser.default.html#stack)
* [value](src_core_json_stream_parser.default.html#value)

### Methods

* [finishChunkProcessing](src_core_json_stream_parser.default.html#finishChunkProcessing)
* [processChunk](src_core_json_stream_parser.default.html#processChunk)
* [from](src_core_json_stream_parser.default.html#from)

## Constructors

### constructor

* new default(): [default](src_core_json_stream_parser.default.html)

* #### Returns [default](src_core_json_stream_parser.default.html)

## Properties

### Protected accumulator

accumulator: string = ''

* Defined in [src/core/json/stream/parser/index.ts:103](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L103)

Accumulator for the current parsed structure

### Protected buffer

buffer: string = ''

* Defined in [src/core/json/stream/parser/index.ts:98](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L98)

The current piece of JSON

### Protected expected

expected: [ParserState](../modules/src_core_json_stream_parser_interface.html#ParserState) = parserStateTypes.VALUE

* Defined in [src/core/json/stream/parser/index.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L123)

The next expected parser state from a stream

### Protected index

index: number = 0

* Defined in [src/core/json/stream/parser/index.ts:113](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L113)

The current index in a buffer parsing process

### Protected isOpenNumber

isOpenNumber: boolean = false

* Defined in [src/core/json/stream/parser/index.ts:133](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L133)

Is the parser parsing a number now

### Protected Optional matched

matched?: null | RegExpExecArray

* Defined in [src/core/json/stream/parser/index.ts:118](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L118)

The current match value after RegExp execution

### Protected parent

parent: [ParentParserState](../modules/src_core_json_stream_parser_interface.html#ParentParserState) = parserStateTypes.EMPTY

* Defined in [src/core/json/stream/parser/index.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L88)

The current parent of a parsed structure

### Protected patterns

patterns: Record<string, RegExp> = parserPatterns

* Defined in [src/core/json/stream/parser/index.ts:128](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L128)

Dictionary with RegExp-s to different types of data

### Protected Readonly stack

stack: [ParentParserState](../modules/src_core_json_stream_parser_interface.html#ParentParserState)[] = []

* Defined in [src/core/json/stream/parser/index.ts:93](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L93)

An array of parent objects for the current parsed structure

### Protected Optional value

value?: string = ''

* Defined in [src/core/json/stream/parser/index.ts:108](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L108)

The current parsed value

## Methods

### finishChunkProcessing

* finishChunkProcessing(): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>

* + Defined in [src/core/json/stream/parser/index.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L139)

  Closes all unclosed tokens and returns a Generator of tokens.
  The method must be called after the end of parsing.

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>

### processChunk

* processChunk(chunk: string): Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>

* + Defined in [src/core/json/stream/parser/index.ts:150](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L150)

  Processes the passed JSON chunk and yields tokens via an asynchronous Generator

  #### Parameters

  + ##### chunk: string

  #### Returns Generator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>

### Static from

* from(source: Iterable<string> | AsyncIterable<string>): AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>
* from<T>(source: Iterable<string> | AsyncIterable<string>, ...processors: T): T extends [[TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<R>] ? AsyncGenerator<R, any, unknown> : T extends [...A[], [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<R>] ? AsyncGenerator<R, any, unknown> : unknown

* + Defined in [src/core/json/stream/parser/index.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L35)

  Parses the specified iterable object as a JSON stream and yields tokens via a Generator

  #### Parameters

  + ##### source: Iterable<string> | AsyncIterable<string>

  #### Returns AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>
* + Defined in [src/core/json/stream/parser/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/index.ts#L43)

  Parses the specified iterable object as a JSON stream and yields tokens or values via a Generator

  #### Type parameters

  + #### T: [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<any>[]

  #### Parameters

  + ##### source: Iterable<string> | AsyncIterable<string>
  + ##### Rest ...processors: T

  #### Returns T extends [[TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<R>] ? AsyncGenerator<R, any, unknown> : T extends [...A[], [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<R>] ? AsyncGenerator<R, any, unknown> : unknown