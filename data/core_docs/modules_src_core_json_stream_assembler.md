# Module src/core/json/stream/assembler
[# core/json/stream/assembler](#corejsonstreamassembler)

This module provides a class to assemble JS values from an iterable of tokens produced by `json/stream/parser` Parser.

[## Usage](#usage)

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
  
const  
  src = ['{"total": 2, "data', '": {"a": [1', ', true, "foo", 2', '], "b": [2, 3]}}'],  
  parser = Parser.from(src, new Assembler());  
  
for await (const val of parser) {  
  // {total: 2, data: {a: [1, true, "foo", 2], b: [2, 3]}}  
  console.log(val);  
}
```

[## API](#api)
[### constructor](#constructor)

The instance constructor can take an object with optional parameter.

[#### [numberAsString = `false`]](#numberasstring--false)

Should or not parse numeric values as string literals.

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
  
const  
  parser1 = Parser.from('-13.4e-3', new Assembler({numberAsString: true}));  
  
for await (const val of parser1) {  
  // '-13.4e-3'  
  console.log(val);  
}  
  
const  
  parser2 = Parser.from('-13.4e-3', new Assembler());  
  
for await (const val of parser2) {  
  // -0.0134  
  console.log(val);  
}
```

[#### reviver](#reviver)

The option defines a reviver function similar to `JSON.parse`.

```
import { convertIfDate } from 'core/json';  
  
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
  
const  
  parser = Parser.from(JSON.stringify([new Date()]), new Assembler({reviver: convertIfDate}))  
  
for await (const val of parser) {  
  // true  
  console.log(val[0] instanceof Date);  
}
```

[### Properties](#properties)
[#### key](#key)

A property key of the active assembling value.

[#### value](#value)

A value of the active assembled item.
If it is a container (object or array), all new assembled values will be added to it.

[### Getters](#getters)
[#### isValueAssembled](#isvalueassembled)

Indicates that the active value is fully assembled.

[#### depth](#depth)

A depth of the assembling structure.

[### Methods](#methods)
[#### processToken](#processtoken)

Processes the passed JSON token and yields the assembled values

```
import Parser from 'core/json/stream/parser';  
import Assembler from 'core/json/stream/assembler';  
  
const  
  assembler = new Assembler();  
  
for (const token of new Parser().processChunk('["foo"]')) {  
  // ["foo"]  
  console.log(...assembler.processToken(token));  
}
```

## Index

### References

* [AssemblerOptions](src_core_json_stream_assembler.html#AssemblerOptions)

### Classes

* [default](../classes/src_core_json_stream_assembler.default.html)

### Variables

* [$$](src_core_json_stream_assembler.html#__)

## References

### AssemblerOptions

Re-exports [AssemblerOptions](../interfaces/src_core_json_stream_assembler_interface.AssemblerOptions.html)

## Variables

### Const $$

$$: [StrictDictionary](../interfaces/index.StrictDictionary.html)<symbol> = ...

* Defined in [src/core/json/stream/assembler/index.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/index.ts#L24)