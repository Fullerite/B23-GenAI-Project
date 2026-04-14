# Module src/core/json/stream
[# core/json/stream](#corejsonstream)

This module provides a bunch of functions to work with JSON in a stream form.
The submodules contain different classes to parse, filter and assemble JSON in a stream form.

[## Usage](#usage)

```
import { convertIfDate } from 'core/json';  
import { from, pick, streamArrray } from 'core/json/stream';  
  
const  
  parser = streamArrray(pick(from('{"data": [1, 2, 3]}'), 'data'), {reviver: convertIfDate});  
  
for await (const val of parser) {  
  // {index: 0, value: 1}  
  // {index: 1, value: 2}  
  // {index: 2, value: 3}  
  console.log(val);  
}
```

[## Functions](#functions)
[### from](#from)

Parses the specified iterable object as a JSON stream and yields tokens via a Generator.
See `core/json/stream/parser` for more information.

```
import { from } from 'core/json/stream';  
  
const  
  parser = from('{"data": [1, 2, 3]}');  
  
for await (const token of parser) {  
  console.log(token);  
}
```

[### filter](#filter)

Takes the specified iterable object of tokens and filters it via the specified filter.
See `core/json/stream/filters` for more information.

```
import { from, filter } from 'core/json/stream';  
  
const  
  parser = filter(from('{"total": 3, "data": [1, 2, 3]}'), 'data');  
  
for await (const token of parser) {  
  console.log(token);  
}
```

[### pick](#pick)

Takes the specified iterable object of tokens and pick from it value that matches the specified selector.
See `core/json/stream/filters` for more information.

```
import { from, pick } from 'core/json/stream';  
  
const  
  parser = pick(from('{"total": 3, "data": [1, 2, 3]}'), 'data');  
  
for await (const token of parser) {  
  console.log(token);  
}
```

[### andPick](#andpick)

Takes the specified iterable object of tokens that has already been `pick` or `pickAnd` applied to,
and picks from it a value that matches the specified selector.
Use this function when you need to combine two or more Pick-s from a one token stream.

```
import { intoIter } from 'core/iter';  
import { sequence } from 'core/iter/combinators';  
import { from, pick, andPick, assemble, streamArray } from 'core/json/stream';  
  
const tokens = intoIter(from(JSON.stringify({  
  total: 3,  
  data: [  
    {user: 'Bob', age: 21},  
    {user: 'Ben', age: 24},  
    {user: 'Rob', age: 28}  
  ]  
})));  
  
const seq = sequence(  
  assemble(pick(tokens, 'total')),  
  streamArray(andPick(tokens, 'data'))  
);  
  
for await (const val of seq) {  
  console.log(val);  
}
```

[### assemble](#assemble)

Takes the specified iterable object of tokens and yields an assembled item from it.
See `core/json/stream/assembler` for more information.

```
import { from, assemble } from 'core/json/stream';  
  
const  
  parser = assemble(from('{"total": 3, "data": [1, 2, 3]}'));  
  
for await (const val of parser) {  
  // {total: 3, data: [1, 2, 3]}  
  console.log(val);  
}
```

[### streamObject](#streamobject)

Takes the specified iterable object of tokens representing an object and yields assembled object items.
See `core/json/stream/streamers` for more information.

```
import { from, streamObject } from 'core/json/stream';  
  
const  
  parser = streamObject(from('{"total": 3, "data": [1, 2, 3]}'));  
  
for await (const val of parser) {  
  // {key: 'total', value: 3}  
  // {key: 'data', value: [1, 2, 3]}  
  console.log(val);  
}
```

[### streamArray](#streamarray)

Takes the specified iterable object of tokens representing an array and yields assembled array items.
See `core/json/stream/streamers` for more information.

```
import { from, streamArray } from 'core/json/stream';  
  
const  
  parser = streamArray(from('[1, 2, 3]'));  
  
for await (const val of parser) {  
  // {index: 0, value: 1}  
  // {index: 1, value: 2]}  
  // {index: 2, value: 3}  
  console.log(val);  
}
```

## Index

### References

* [AndPickOptions](src_core_json_stream.html#AndPickOptions)

### Functions

* [andPick](src_core_json_stream.html#andPick)
* [assemble](src_core_json_stream.html#assemble)
* [filter](src_core_json_stream.html#filter)
* [from](src_core_json_stream.html#from)
* [pick](src_core_json_stream.html#pick)
* [streamArray](src_core_json_stream.html#streamArray)
* [streamObject](src_core_json_stream.html#streamObject)

## References

### AndPickOptions

Re-exports [AndPickOptions](../interfaces/src_core_json_stream_interface.AndPickOptions.html)

## Functions

### andPick

* andPick(source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>, selector: [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter), opts?: [AndPickOptions](../interfaces/src_core_json_stream_interface.AndPickOptions.html)): AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/index.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L139)

  Takes the specified iterable object of tokens that has already been `pick` or `pickAnd` applied to,
  and picks from it a value that matches the specified selector.
  Use this function when you need to combine two or more Pick-s from a one token stream.

  example
  :   ```
      const tokens = intoIter(from(JSON.stringify({  
        total: 3,  
        data: [  
          {user: 'Bob', age: 21},  
          {user: 'Ben', age: 24},  
          {user: 'Rob', age: 28}  
        ]  
      })));  
        
      const seq = sequence(  
        assemble(pick(tokens, 'total')),  
        streamArray(andPick(tokens, 'data'))  
      );  
        
      for await (const val of seq) {  
        console.log(val);  
      }
      ```

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>
  + ##### selector: [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter)
  + ##### Optional opts: [AndPickOptions](../interfaces/src_core_json_stream_interface.AndPickOptions.html)

  #### Returns AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

### assemble

* assemble<T>(source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>, opts?: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)): AsyncGenerator<T>

* + Defined in [src/core/json/stream/index.ts:176](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L176)

  Takes the specified iterable object of tokens and yields an assembled item from it

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>
  + ##### Optional opts: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)

  #### Returns AsyncGenerator<T>

### filter

* filter(source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>, filter: [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter)): AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/index.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L59)

  Takes the specified iterable object of tokens and filters it via the specified filter

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>
  + ##### filter: [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter)

  #### Returns AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

### from

* from(source: [AnyIterable](index.html#AnyIterable)<string>): AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/index.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L49)

  Parses the specified iterable object as a JSON stream and yields tokens via a Generator

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<string>

  #### Returns AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

### pick

* pick(source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>, selector: [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter), opts?: [FilterOptions](../interfaces/src_core_json_stream_filters_interface.FilterOptions.html)): AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

* + Defined in [src/core/json/stream/index.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L77)

  Takes the specified iterable object of tokens and picks from it a value that matches the specified selector

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>
  + ##### selector: [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter)
  + ##### Optional opts: [FilterOptions](../interfaces/src_core_json_stream_filters_interface.FilterOptions.html)

  #### Returns AsyncGenerator<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>

### streamArray

* streamArray<T>(source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>, opts?: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)): AsyncGenerator<[StreamedArray](../interfaces/src_core_json_stream_streamers_interface.StreamedArray.html)<T>>

* + Defined in [src/core/json/stream/index.ts:194](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L194)

  Takes the specified iterable object of tokens representing an array and yields assembled array items

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>
  + ##### Optional opts: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)

  #### Returns AsyncGenerator<[StreamedArray](../interfaces/src_core_json_stream_streamers_interface.StreamedArray.html)<T>>

### streamObject

* streamObject<T>(source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>, opts?: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)): AsyncGenerator<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>>

* + Defined in [src/core/json/stream/index.ts:212](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/index.ts#L212)

  Takes the specified iterable object of tokens representing an object and yields assembled object items

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### source: [AnyIterable](index.html#AnyIterable)<[Token](../interfaces/src_core_json_stream_parser_interface.Token.html)>
  + ##### Optional opts: [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)

  #### Returns AsyncGenerator<[StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)<T>>