# Module src/core/json/stream/parser
[# core/json/stream/parser](#corejsonstreamparser)

This module provides a class to parse JSON from separated string chunks, i.e., stream form.
The class instance takes a JSON chunk and returns a Generator that produces parsed JSON tokens; otherwise, it throws a syntax error.

[## Usage](#usage)

```
import Parser from 'core/json/stream/parser';  
  
const  
  parser = Parser.from(['{"key', '": 2', '}']);  
  tokens = [];  
  
for await (const token of parser) {  
  tokens.push(token);  
}  
  
/* [  
  {name: 'startObject'},  
  {name: 'startKey'},  
  {name: 'stringChunk', value: 'key'},  
  {name: 'endKey'},  
  {name: 'keyValue', value: 'key'},  
  {name: 'startNumber'},  
  {name: 'numberChunk', value: '2'},  
  {name: 'endNumber'},  
  {name: 'numberValue', value: '2'},  
  {name: 'endObject'}  
] */  
console.log(tokens);
```

[## API](#api)
[### Static](#static)
[#### from](#from)

The method parses the specified iterable object as a JSON stream and yields tokens via an asynchronous Generator.

```
import Parser from 'core/json/stream/parser';  
  
const  
  parser = Parser.from('[1]');  
  
for await (const token of parser) {  
  // {name: 'startArray'},  
  // {name: 'startNumber'},  
  // {name: 'numberChunk', value: '1'},  
  // {name: 'endNumber'},  
  // {name: 'numberValue', value: '1'},  
  // {name: 'endArray'}  
  console.log(token);  
}
```

The method can also take a list of token processors to apply.

```
import Parser from 'core/json/stream/parser';  
  
import Assembler from 'core/json/stream/assembler';  
import { Filter } from 'core/json/stream/filters';  
  
const  
  parser = Parser.from('[{"a": 1}, {"b": 2}]', new Filter(/\d+\.a/), new Assembler());  
  
for await (const result of parser) {  
  // [{a: 1}]  
  console.log(result);  
}
```

[### Instance](#instance)
[#### processChunk](#processchunk)

The method processes the passed JSON chunk and yields tokens via a Generator.

```
import Parser from 'core/json/stream/parser';  
  
const  
  parser = new Parser();  
  
/* [  
  {name: 'startArray'},  
  {name: 'startNumber'},  
  {name: 'numberChunk', value: '1'},  
  {name: 'endNumber'},  
  {name: 'numberValue', value: '1'},  
  {name: 'endArray'}  
] */  
console.log([...parser.processChunk('[1]')]);
```

[## Tokens](#tokens)

This is the list of data objects produced by Parser in the correct order:

```
// A sequence can have 0 or more items.  
// A value is one of: object, array, string, number, null, true, false.  
  
// A parser produces a sequence of values:  
  
// Object  
({name: 'startObject'});  
  
// Sequence of object properties: key, then value  
({name: 'endObject'});  
  
// ----  
  
// Array  
({name: 'startArray'});  
  
// Sequence of values  
({name: 'endArray'});  
  
// ----  
  
// Key  
({name: 'startKey'});  
  
// Sequence of string chunks:  
({name: 'stringChunk', value: 'string value chunk'});  
({name: 'endKey'});  
({name: 'keyValue', value: 'key value'});  
  
// ----  
  
// String  
({name: 'startString'});  
  
// Sequence of string chunks:  
({name: 'stringChunk', value: 'string value chunk'});  
({name: 'endString'});  
({name: 'stringValue', value: 'string value'});  
  
// ----  
  
// Number  
({name: 'startNumber'});  
  
// Sequence of number chunks (as strings):  
({name: 'numberChunk', value: 'string value chunk'});  
({name: 'endNumber'});  
({name: 'numberValue', value: 'string value'});  
  
// ----  
  
// null, true, false  
({name: 'nullValue', value: null});  
({name: 'trueValue', value: true});  
({name: 'falseValue', value: false});
```

All value chunks (stringChunk and numberChunk) should be concatenated in order to produce a final value.
Empty string values may have no chunks. String chunks may have empty values.

**Important:** values of `numberChunk` and `numberValue` are strings, not numbers.
It is up to a downstream code to convert it to a number using `parseInt(x)`, `parseFloat(x)` or simply `x => +x`.

All items follow in the correct order. If something is going wrong, a parser will produce an error event. For example:

* All `startXXX` are balanced with `endXXX`.
* Between `startKey` and `endKey` can be zero or more `stringChunk` items. No other items can be seen.
* After `startObject` optional key-value pairs emitted in a strict pattern: a key-related item, then a value, and
  this cycle can be continued until all key-value pairs are streamed.

  + It is not possible for a key to be missing a value.
* All `endObject` are balanced with the corresponding `startObject`.
* `endObject` cannot close `startArray`.
* Between `startString` and `endString` can go 0 or more `stringChunk`, but no other items.
* `endKey` can be optionally followed by `keyValue`, then a new value will be started, but no `endObject`.

In short, the item sequence is always correctly formed. No need to do unnecessary checks.

## Index

### References

* [MAX\_PATTERN\_SIZE](src_core_json_stream_parser.html#MAX_PATTERN_SIZE)
* [PARSING\_COMPLETE](src_core_json_stream_parser.html#PARSING_COMPLETE)
* [ParentParserState](src_core_json_stream_parser.html#ParentParserState)
* [ParserState](src_core_json_stream_parser.html#ParserState)
* [Token](src_core_json_stream_parser.html#Token)
* [TokenName](src_core_json_stream_parser.html#TokenName)
* [TokenProcessor](src_core_json_stream_parser.html#TokenProcessor)
* [TokenProcessorFn](src_core_json_stream_parser.html#TokenProcessorFn)
* [TokenValue](src_core_json_stream_parser.html#TokenValue)
* [parserCharCodes](src_core_json_stream_parser.html#parserCharCodes)
* [parserExpected](src_core_json_stream_parser.html#parserExpected)
* [parserPatterns](src_core_json_stream_parser.html#parserPatterns)
* [parserStateTypes](src_core_json_stream_parser.html#parserStateTypes)
* [parserStates](src_core_json_stream_parser.html#parserStates)

### Classes

* [default](../classes/src_core_json_stream_parser.default.html)

## References

### MAX\_PATTERN\_SIZE

Re-exports [MAX\_PATTERN\_SIZE](src_core_json_stream_parser_const.html#MAX_PATTERN_SIZE)

### PARSING\_COMPLETE

Re-exports [PARSING\_COMPLETE](src_core_json_stream_parser_const.html#PARSING_COMPLETE)

### ParentParserState

Re-exports [ParentParserState](src_core_json_stream_parser_interface.html#ParentParserState)

### ParserState

Re-exports [ParserState](src_core_json_stream_parser_interface.html#ParserState)

### Token

Re-exports [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

### TokenName

Re-exports [TokenName](src_core_json_stream_parser_interface.html#TokenName)

### TokenProcessor

Re-exports [TokenProcessor](../interfaces/src_core_json_stream_parser_interface.TokenProcessor.html)

### TokenProcessorFn

Re-exports [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)

### TokenValue

Re-exports [TokenValue](src_core_json_stream_parser_interface.html#TokenValue)

### parserCharCodes

Re-exports [parserCharCodes](src_core_json_stream_parser_const.html#parserCharCodes)

### parserExpected

Re-exports [parserExpected](src_core_json_stream_parser_const.html#parserExpected)

### parserPatterns

Re-exports [parserPatterns](src_core_json_stream_parser_const.html#parserPatterns)

### parserStateTypes

Re-exports [parserStateTypes](src_core_json_stream_parser_const.html#parserStateTypes)

### parserStates

Re-exports [parserStates](src_core_json_stream_parser_const.html#parserStates)