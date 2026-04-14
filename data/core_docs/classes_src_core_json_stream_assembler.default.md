# Class default<T>
### Type parameters

* #### T = unknown

### Hierarchy

* default

### Implements

* [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)<T>

## Index

### Constructors

* [constructor](src_core_json_stream_assembler.default.html#constructor)

### Properties

* [key](src_core_json_stream_assembler.default.html#key)
* [reviver](src_core_json_stream_assembler.default.html#reviver)
* [stack](src_core_json_stream_assembler.default.html#stack)
* [startArray](src_core_json_stream_assembler.default.html#startArray)
* [startObject](src_core_json_stream_assembler.default.html#startObject)
* [value](src_core_json_stream_assembler.default.html#value)

### Accessors

* [depth](src_core_json_stream_assembler.default.html#depth)
* [isValueAssembled](src_core_json_stream_assembler.default.html#isValueAssembled)

### Methods

* [createStartObjectHandler](src_core_json_stream_assembler.default.html#createStartObjectHandler)
* [endArray](src_core_json_stream_assembler.default.html#endArray)
* [endObject](src_core_json_stream_assembler.default.html#endObject)
* [endPrimitive](src_core_json_stream_assembler.default.html#endPrimitive)
* [falseValue](src_core_json_stream_assembler.default.html#falseValue)
* [keyValue](src_core_json_stream_assembler.default.html#keyValue)
* [nullValue](src_core_json_stream_assembler.default.html#nullValue)
* [numberValue](src_core_json_stream_assembler.default.html#numberValue)
* [processToken](src_core_json_stream_assembler.default.html#processToken)
* [saveValue](src_core_json_stream_assembler.default.html#saveValue)
* [stringValue](src_core_json_stream_assembler.default.html#stringValue)
* [trueValue](src_core_json_stream_assembler.default.html#trueValue)

## Constructors

### constructor

* new default<T>(opts?: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)): [default](src_core_json_stream_assembler.default.html)<T>

* + Defined in [src/core/json/stream/assembler/index.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L88)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### opts: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html) = {}

  #### Returns [default](src_core_json_stream_assembler.default.html)<T>

## Properties

### key

key: null | string = null

* Defined in [src/core/json/stream/assembler/index.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L30)

Property key of the active assembling value

### Protected Optional Readonly reviver

reviver?: [JSONCb](../interfaces/index.JSONCb.html)

* Defined in [src/core/json/stream/assembler/index.ts:83](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L83)

Function to transform a value after assembling.
Its API is identical to the reviver from `JSON.parse`.

param key

param value

### Protected stack

stack: unknown[] = []

* Defined in [src/core/json/stream/assembler/index.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L64)

Stack of nested assembled items and keys contained within the active assembling value

### Protected startArray

startArray: [AnyFunction](../interfaces/index.AnyFunction.html)<any[], any> = ...

* Defined in [src/core/json/stream/assembler/index.ts:74](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L74)

Handler to process an array start

### Protected startObject

startObject: [AnyFunction](../interfaces/index.AnyFunction.html)<any[], any> = ...

* Defined in [src/core/json/stream/assembler/index.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L69)

Handler to process an object start

### value

value: unknown = NULL

* Defined in [src/core/json/stream/assembler/index.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L36)

A value of the active assembled item.
If it is a container (object or array), all new assembled values will be added to it.

## Accessors

### depth

* get depth(): number

* + Defined in [src/core/json/stream/assembler/index.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L56)

  Depth of the assembling structure

  #### Returns number

### isValueAssembled

* get isValueAssembled(): boolean
* set isValueAssembled(value: boolean): void

* + Defined in [src/core/json/stream/assembler/index.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L41)

  Indicates that the active value is fully assembled

  #### Returns boolean
* + Defined in [src/core/json/stream/assembler/index.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L49)

  Sets the value assembling status

  #### Parameters

  + ##### value: boolean

  #### Returns void

## Methods

### Protected createStartObjectHandler

* createStartObjectHandler(Constr: ObjectConstructor | ArrayConstructor): [AnyFunction](../interfaces/index.AnyFunction.html)<any[], any>

* + Defined in [src/core/json/stream/assembler/index.ts:117](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L117)

  Creates a handler to process starting of an object or array

  #### Parameters

  + ##### Constr: ObjectConstructor | ArrayConstructor

    constructor to create a structure

  #### Returns [AnyFunction](../interfaces/index.AnyFunction.html)<any[], any>

### Protected endArray

* endArray(): void

* + Defined in [src/core/json/stream/assembler/index.ts:202](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L202)

  Handler to process an array end

  #### Returns void

### Protected endObject

* endObject(): void

* + Defined in [src/core/json/stream/assembler/index.ts:185](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L185)

  Handler to process an object end

  #### Returns void

### Protected endPrimitive

* endPrimitive(): void

* + Defined in [src/core/json/stream/assembler/index.ts:209](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L209)

  Handler to process ending of primitive values

  #### Returns void

### Protected falseValue

* falseValue(): void

* + Defined in [src/core/json/stream/assembler/index.ts:177](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L177)

  Handler to process a falsy boolean value

  #### Returns void

### Protected keyValue

* keyValue(value: string): void

* + Defined in [src/core/json/stream/assembler/index.ts:136](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L136)

  Handler to process an object key value

  #### Parameters

  + ##### value: string

  #### Returns void

### Protected nullValue

* nullValue(): void

* + Defined in [src/core/json/stream/assembler/index.ts:161](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L161)

  Handler to process nullish values

  #### Returns void

### Protected numberValue

* numberValue(value: string): void

* + Defined in [src/core/json/stream/assembler/index.ts:153](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L153)

  Handler to process a number value

  #### Parameters

  + ##### value: string

  #### Returns void

### processToken

* processToken(chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)): Generator<T, any, unknown>

* Implementation of TokenProcessor.processToken

  + Defined in [src/core/json/stream/assembler/index.ts:102](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L102)

  Processes the passed JSON token and yields the assembled values

  #### Parameters

  + ##### chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

  #### Returns Generator<T, any, unknown>

### Protected saveValue

* saveValue(value: unknown): void

* + Defined in [src/core/json/stream/assembler/index.ts:219](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L219)

  Saves an assembled value into the internal structure

  #### Parameters

  + ##### value: unknown

  #### Returns void

### Protected stringValue

* stringValue(value: string): void

* + Defined in [src/core/json/stream/assembler/index.ts:144](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L144)

  Handler to process a string value

  #### Parameters

  + ##### value: string

  #### Returns void

### Protected trueValue

* trueValue(): void

* + Defined in [src/core/json/stream/assembler/index.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L169)

  Handler to process a truly boolean value

  #### Returns void