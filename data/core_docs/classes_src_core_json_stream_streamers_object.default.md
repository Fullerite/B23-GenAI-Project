# Class default<T>
### Type parameters

* #### T = unknown

### Hierarchy

* [default](src_core_json_stream_streamers_interface.default.html)<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>>
  + default

## Index

### Constructors

* [constructor](src_core_json_stream_streamers_object.default.html#constructor)

### Properties

* [assembler](src_core_json_stream_streamers_object.default.html#assembler)
* [isChecked](src_core_json_stream_streamers_object.default.html#isChecked)
* [key](src_core_json_stream_streamers_object.default.html#key)
* [level](src_core_json_stream_streamers_object.default.html#level)

### Methods

* [checkToken](src_core_json_stream_streamers_object.default.html#checkToken)
* [processToken](src_core_json_stream_streamers_object.default.html#processToken)
* [push](src_core_json_stream_streamers_object.default.html#push)

## Constructors

### constructor

* new default<T>(opts?: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)): [default](src_core_json_stream_streamers_object.default.html)<T>

* Overrides [default](src_core_json_stream_streamers_interface.default.html).[constructor](src_core_json_stream_streamers_interface.default.html#constructor)

  + Defined in [src/core/json/stream/streamers/object.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/object.ts#L20)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### Optional opts: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)

  #### Returns [default](src_core_json_stream_streamers_object.default.html)<T>

## Properties

### Protected assembler

assembler: [default](src_core_json_stream_assembler.default.html)<unknown>

Inherited from [default](src_core_json_stream_streamers_interface.default.html).[assembler](src_core_json_stream_streamers_interface.default.html#assembler)

* Defined in [src/core/json/stream/streamers/interface.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L31)

Instance of a token assembler

### Protected isChecked

isChecked: boolean = false

Inherited from [default](src_core_json_stream_streamers_interface.default.html).[isChecked](src_core_json_stream_streamers_interface.default.html#isChecked)

* Defined in [src/core/json/stream/streamers/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L36)

True if the streamed structure is already checked

### Protected key

key: null | string = null

* Defined in [src/core/json/stream/streamers/object.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/object.ts#L18)

Last key of the current streamed object property

### Protected level

level: number = 1

Inherited from [default](src_core_json_stream_streamers_interface.default.html).[level](src_core_json_stream_streamers_interface.default.html#level)

* Defined in [src/core/json/stream/streamers/interface.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L26)

Actual depth of the streamed structure

## Methods

### Protected checkToken

* checkToken(chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)): boolean

* Overrides [default](src_core_json_stream_streamers_interface.default.html).[checkToken](src_core_json_stream_streamers_interface.default.html#checkToken)

  + Defined in [src/core/json/stream/streamers/object.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/object.ts#L25)

  Checks that specified token is matched for the streamer type

  #### Parameters

  + ##### chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

  #### Returns boolean

### processToken

* processToken(chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)): Generator<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>, any, unknown>

* Inherited from [default](src_core_json_stream_streamers_interface.default.html).[processToken](src_core_json_stream_streamers_interface.default.html#processToken)

  + Defined in [src/core/json/stream/streamers/interface.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/interface.ts#L59)

  Processes the passed JSON token and yields the assembled value

  #### Parameters

  + ##### chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

  #### Returns Generator<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>, any, unknown>

### Protected push

* push(): Generator<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>, any, unknown>

* Overrides [default](src_core_json_stream_streamers_interface.default.html).[push](src_core_json_stream_streamers_interface.default.html#push)

  + Defined in [src/core/json/stream/streamers/object.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/streamers/object.ts#L34)

  Method to yield assembled tokens

  #### Returns Generator<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>, any, unknown>