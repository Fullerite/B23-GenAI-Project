# Class default<T>
### Type parameters

* #### T = unknown

### Hierarchy

* default
  + [default](src_core_json_stream_streamers_array.default.html)
  + [default](src_core_json_stream_streamers_object.default.html)

### Implements

* [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<T>

## Index

### Constructors

* [constructor](src_core_json_stream_streamers_interface.default.html#constructor)

### Properties

* [assembler](src_core_json_stream_streamers_interface.default.html#assembler)
* [isChecked](src_core_json_stream_streamers_interface.default.html#isChecked)
* [level](src_core_json_stream_streamers_interface.default.html#level)

### Methods

* [checkToken](src_core_json_stream_streamers_interface.default.html#checkToken)
* [processToken](src_core_json_stream_streamers_interface.default.html#processToken)
* [push](src_core_json_stream_streamers_interface.default.html#push)

## Constructors

### Protected constructor

* new default<T>(opts?: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)): [default](src_core_json_stream_streamers_interface.default.html)<T>

* + Defined in [src/core/json/stream/streamers/interface.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L52)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### Optional opts: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)

  #### Returns [default](src_core_json_stream_streamers_interface.default.html)<T>

## Properties

### Protected assembler

assembler: [default](src_core_json_stream_assembler.default.html)<unknown>

* Defined in [src/core/json/stream/streamers/interface.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L31)

Instance of a token assembler

### Protected isChecked

isChecked: boolean = false

* Defined in [src/core/json/stream/streamers/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L36)

True if the streamed structure is already checked

### Protected level

level: number = 1

* Defined in [src/core/json/stream/streamers/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L26)

Actual depth of the streamed structure

## Methods

### Protected Abstract checkToken

* checkToken(token: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)): boolean

* + Defined in [src/core/json/stream/streamers/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L42)

  Checks that specified token is matched for the streamer type

  #### Parameters

  + ##### token: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

  #### Returns boolean

### processToken

* processToken(chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)): Generator<T, any, unknown>

* Implementation of TokenProcessor.processToken

  + Defined in [src/core/json/stream/streamers/interface.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L59)

  Processes the passed JSON token and yields the assembled value

  #### Parameters

  + ##### chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

  #### Returns Generator<T, any, unknown>

### Protected Abstract push

* push(): Generator<T, any, unknown>

* + Defined in [src/core/json/stream/streamers/interface.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L47)

  Method to yield assembled tokens

  #### Returns Generator<T, any, unknown>