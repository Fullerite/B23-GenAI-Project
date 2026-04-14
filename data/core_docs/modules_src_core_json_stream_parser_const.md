# Module src/core/json/stream/parser/const
## Index

### Variables

* [MAX\_PATTERN\_SIZE](src_core_json_stream_parser_const.html#MAX_PATTERN_SIZE)
* [PARSING\_COMPLETE](src_core_json_stream_parser_const.html#PARSING_COMPLETE)
* [parserCharCodes](src_core_json_stream_parser_const.html#parserCharCodes)
* [parserExpected](src_core_json_stream_parser_const.html#parserExpected)
* [parserPatterns](src_core_json_stream_parser_const.html#parserPatterns)
* [parserStateTypes](src_core_json_stream_parser_const.html#parserStateTypes)
* [parserStates](src_core_json_stream_parser_const.html#parserStates)

## Variables

### Const MAX\_PATTERN\_SIZE

MAX\_PATTERN\_SIZE: 16 = 16

* Defined in [src/core/json/stream/parser/const.ts:10](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L10)

### Const PARSING\_COMPLETE

PARSING\_COMPLETE: typeof [PARSING\_COMPLETE](src_core_json_stream_parser_const.html#PARSING_COMPLETE) = ...

* Defined in [src/core/json/stream/parser/const.ts:11](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L11)

### Const parserCharCodes

parserCharCodes: { ": string; /: string; \: string; b: string; f: string; n: string; r: string; t: string } = ...

* Defined in [src/core/json/stream/parser/const.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L69)

#### Type declaration

* ##### ": string
* ##### /: string
* ##### \: string
* ##### b: string
* ##### f: string
* ##### n: string
* ##### r: string
* ##### t: string

### Const parserExpected

parserExpected: { : "done"; array: "arrayStop"; object: "objectStop" } = ...

* Defined in [src/core/json/stream/parser/const.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L63)

#### Type declaration

* ##### : "done"
* ##### array: "arrayStop"
* ##### object: "objectStop"

### Const parserPatterns

parserPatterns: { colon: RegExp; comma: RegExp; key1: RegExp; numberDigit: RegExp; numberExpDigit: RegExp; numberExpSign: RegExp; numberExpStart: RegExp; numberExponent: RegExp; numberFracDigit: RegExp; numberFracStart: RegExp; numberFraction: RegExp; numberStart: RegExp; string: RegExp; value1: RegExp; ws: RegExp } = ...

* Defined in [src/core/json/stream/parser/const.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L20)

#### Type declaration

* ##### colon: RegExp
* ##### comma: RegExp
* ##### key1: RegExp
* ##### numberDigit: RegExp
* ##### numberExpDigit: RegExp
* ##### numberExpSign: RegExp
* ##### numberExpStart: RegExp
* ##### numberExponent: RegExp
* ##### numberFracDigit: RegExp
* ##### numberFracStart: RegExp
* ##### numberFraction: RegExp
* ##### numberStart: RegExp
* ##### string: RegExp
* ##### value1: RegExp
* ##### ws: RegExp

### Const parserStateTypes

parserStateTypes: { ARRAY: "array"; ARRAY\_STOP: "arrayStop"; COLON: "colon"; DONE: "done"; EMPTY: ""; KEY: "key"; KEY1: "key1"; KEY\_VAL: "keyVal"; NUMBER\_DIGIT: "numberDigit"; NUMBER\_EXPONENT: "numberExponent"; NUMBER\_EXP\_DIGIT: "numberExpDigit"; NUMBER\_EXP\_SIGN: "numberExpSign"; NUMBER\_EXP\_START: "numberExpStart"; NUMBER\_FRACTION: "numberFraction"; NUMBER\_FRACTION\_DIGIT: "numberFracDigit"; NUMBER\_FRACTION\_START: "numberFracStart"; NUMBER\_START: "numberStart"; OBJECT: "object"; OBJECT\_STOP: "objectStop"; STRING: "string"; VALUE: "value"; VALUE1: "value1" } = ...

* Defined in [src/core/json/stream/parser/const.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L38)

#### Type declaration

* ##### ARRAY: "array"
* ##### ARRAY\_STOP: "arrayStop"
* ##### COLON: "colon"
* ##### DONE: "done"
* ##### EMPTY: ""
* ##### KEY: "key"
* ##### KEY1: "key1"
* ##### KEY\_VAL: "keyVal"
* ##### NUMBER\_DIGIT: "numberDigit"
* ##### NUMBER\_EXPONENT: "numberExponent"
* ##### NUMBER\_EXP\_DIGIT: "numberExpDigit"
* ##### NUMBER\_EXP\_SIGN: "numberExpSign"
* ##### NUMBER\_EXP\_START: "numberExpStart"
* ##### NUMBER\_FRACTION: "numberFraction"
* ##### NUMBER\_FRACTION\_DIGIT: "numberFracDigit"
* ##### NUMBER\_FRACTION\_START: "numberFracStart"
* ##### NUMBER\_START: "numberStart"
* ##### OBJECT: "object"
* ##### OBJECT\_STOP: "objectStop"
* ##### STRING: "string"
* ##### VALUE: "value"
* ##### VALUE1: "value1"

### Const parserStates

parserStates: {} = {}

* Defined in [src/core/json/stream/parser/const.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/parser/const.ts#L14)

#### Type declaration