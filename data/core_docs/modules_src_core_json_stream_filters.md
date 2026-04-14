# Module src/core/json/stream/filters
[# core/json/stream/filters](#corejsonstreamfilters)

This module provides a bunch of classes to filter tokens produced by `json/stream/parser` Parser.
Also, the module provides an abstract class to create your own filters.

[## Usage](#usage)

```
import Parser from 'core/json/stream/parser';  
import { Filter } from 'core/json/stream/filters';  
  
const  
  parser = Parser.from(['{"total": 2, "data": [1, 2]}'], new Filter('data'));  
  tokens = [];  
  
for await (const token of parser) {  
  tokens.push(token);  
}  
  
/* [  
  {name: 'startObject'},  
  {name: 'startKey'},  
  {name: 'stringChunk', value: 'data'},  
  {name: 'endKey'},  
  {name: 'keyValue', value: 'data'},  
  {name: 'startArray'},  
  {name: 'startNumber'},  
  {name: 'numberChunk', value: '1'},  
  {name: 'endNumber'},  
  {name: 'numberValue', value: '1'},  
  {name: 'startNumber'},  
  {name: 'numberChunk', value: '2'},  
  {name: 'endNumber'},  
  {name: 'numberValue', value: '2'},  
  {name: 'endArray'},  
  {name: 'endObject'}  
] */  
console.log(tokens);
```

[## Filters](#filters)
[### Filter](#filter)

An instance of the Filter class takes an iterable object of parsed tokens, filters values matched with the specified condition,
and yields only the filtered tokens.

[#### Preserving tokens by the specified path](#preserving-tokens-by-the-specified-path)

If a filter condition is provided as a string, the Filter instance will interpret it as a property path that should preserve.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Filter } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, 2], "b": [2, 3]}}'],  
  parser = Parser.from(src, new Filter('data.a'), new Assembler());  
  
for await (const val of parser) {  
  // {data: {a: [1, 2]}  
  console.log(val);  
}
```

[#### Preserving tokens with paths matched to the specified regular expression](#preserving-tokens-with-paths-matched-to-the-specified-regular-expression)

If a filter condition is provided as a RegExp, the Filter instance will interpret it as a pattern of property paths that should preserve.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Filter } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, 2], "b": [2, 3]}}'],  
  parser = Parser.from(src, new Filter(/\b[ab]\b/), new Assembler());  
  
for await (const val of parser) {  
  // {data: {a: [1, 2], b: [2, 3]}}  
  console.log(val);  
}
```

[#### Preserving tokens filtered via the specified function](#preserving-tokens-filtered-via-the-specified-function)

If a filter condition is provided as a function, the Filter instance will invoke it at each token and preserve it if the function returns true.
The filter function takes a property path and token.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Filter } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, true, "foo", 2], "b": [2, 3]}}'],  
  filter = (path, token) => path.includes('a') && token.name === 'numberValue',  
  parser = Parser.from(src, new Filter(filter), new Assembler());  
  
for await (const val of parser) {  
  // {data: {a: [1, 2]}}  
  console.log(val);  
}
```

[### Pick](#pick)

An instance of the Pick class takes an iterable object of parsed tokens and yields only tokens by the specified selector.

[#### Picking tokens by the specified path](#picking-tokens-by-the-specified-path)

If a pick selector is provided as a string, the Pick instance will interpret it as a property path that should pick.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Pick } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, 2], "b": [2, 3]}}'],  
  parser = Parser.from(src, new Pick('data.a'), new Assembler());  
  
for await (const val of parser) {  
  // [1, 2]  
  console.log(val);  
}
```

[#### Picking tokens with paths matched to the specified regular expression](#picking-tokens-with-paths-matched-to-the-specified-regular-expression)

If a pick selector is provided as a RegExp, the Pick instance will interpret it as a pattern of property path that should pick.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Pick } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, 2], "b": [2, 3]}}'],  
  parser = Parser.from(src, new Pick(/\b[ab]\b/), new Assembler());  
  
for await (const val of parser) {  
  // [1, 2]  
  console.log(val);  
}
```

[##### Multiple mode](#multiple-mode)

When you need to pick more than one set of tokens by a selector, use the additional `multiple` option.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Pick } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, 2], "b": [2, 3]}}'],  
  parser = Parser.from(src, new Pick(/\b[ab]\b/, {multiple: true}), new Assembler());  
  
const  
  values = [];  
  
for await (const val of parser) {  
  values.push(val);  
}  
  
// [[1, 2], [2, 3]]  
console.log(values);
```

[#### Picking tokens filtered via the specified function](#picking-tokens-filtered-via-the-specified-function)

If a pick selector is provided as a function, the Pick instance will invoke it at each token and pick it if the function returns true.
The pick function takes a property path and token.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Pick } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, true, "foo", 2], "b": [2, 3]}}'],  
  selector = (path, token) => path.includes('a') && token.name === 'numberValue',  
  parser = Parser.from(src, new Pick(selector), new Assembler());  
  
for await (const val of parser) {  
  // 1  
  console.log(val);  
}
```

[##### Multiple mode](#multiple-mode-1)

When you need to pick more than one set of tokens by a selector, use the additional `multiple` option.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
import { Pick } from 'core/json/stream/filters';  
  
const  
  src = ['{"total": 2, "data": {"a": [1, true, "foo", 2], "b": [2, 3]}}'],  
  selector = (path, token) => path.includes('a') && token.name === 'numberValue',  
  parser = Parser.from(src, new Pick(selector), new Assembler());  
  
const  
  values = [];  
  
for await (const val of parser) {  
  values.push(val);  
}  
  
// [1, 2]  
console.log(values);
```

[### AbstractFilter](#abstractfilter)

When creating a new filter class, extend it from the `AbstractFilter` and implement the `checkToken` method.
In addition, you can override `finishTokenProcessing` if needed.

```
import type { Token } from 'core/json/stream/parser';  
  
import Super from 'core/json/stream/filters/abstract-filter';  
import type { TokenFilter, FilterOptions } from 'core/json/stream/filters/interface';  
  
export default class PickObject extends Super {  
  public constructor(filter: TokenFilter, opts?: FilterOptions) {  
    super(filter, opts);  
  }  
  
  /** @inheritDoc */  
  protected*checkToken(chunk: Token): Generator<boolean | Token> {  
    switch (chunk.name) {  
      case 'startObject':  
      case 'startArray':  
        if (this.filter(this.stack, chunk)) {  
          yield chunk;  
  
          // eslint-disable-next-line @typescript-eslint/unbound-method  
          this.processToken = this.passObject;  
          this.depth = 1;  
  
          return true;  
        }  
  
        break;  
  
      default:  
        // Do nothing  
    }  
  
    return false;  
  }  
}
```

[#### API](#api)
[##### constructor](#constructor)

The instance constructor takes two parameters.
The first one is a filter. The second one is an object with optional filter parameters.
A filter can be defined via a string, regular expression, or function.
By providing the optional `multiple` parameter, you can customize should or not to stop filter after the first successful token.

[##### processToken](#processtoken)

Processes the passed JSON token and yields tokens.

```
import Parser from 'core/json/stream/parser';  
import { Pick } from 'core/json/stream/filters';  
  
const  
  pick = new Pick('0'),  
  tokens = [];  
  
for (const token of new Parser().processChunk('["foo"]')) {  
  tokens.push(...pick.processToken(token));  
}  
  
tokens.push(...pick.finishTokenProcessing());
```

[##### finishTokenProcessing](#finishtokenprocessing)

Closes all unclosed tokens and returns a Generator of filtered tokens.
The method must be called after the end of filtration.

## Index

### References

* [AbstractFilter](src_core_json_stream_filters.html#AbstractFilter)
* [Filter](src_core_json_stream_filters.html#Filter)
* [FilterOptions](src_core_json_stream_filters.html#FilterOptions)
* [FilterStack](src_core_json_stream_filters.html#FilterStack)
* [FilterToken](src_core_json_stream_filters.html#FilterToken)
* [Pick](src_core_json_stream_filters.html#Pick)
* [TokenFilter](src_core_json_stream_filters.html#TokenFilter)
* [TokenFilterFn](src_core_json_stream_filters.html#TokenFilterFn)

## References

### AbstractFilter

Renames and re-exports [default](../classes/src_core_json_stream_filters_abstract_filter.default.html)

### Filter

Renames and re-exports [default](../classes/src_core_json_stream_filters_filter.default.html)

### FilterOptions

Re-exports [FilterOptions](../interfaces/src_core_json_stream_filters_interface.FilterOptions.html)

### FilterStack

Re-exports [FilterStack](src_core_json_stream_filters_interface.html#FilterStack)

### FilterToken

Re-exports [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)

### Pick

Renames and re-exports [default](../classes/src_core_json_stream_filters_pick.default.html)

### TokenFilter

Re-exports [TokenFilter](src_core_json_stream_filters_interface.html#TokenFilter)

### TokenFilterFn

Re-exports [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)