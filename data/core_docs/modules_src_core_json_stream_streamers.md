# Module src/core/json/stream/streamers
[# core/json/stream/streamers](#corejsonstreamstreamers)

This module provides a bunch of classes to stream object or array elements.
Also, the module provides an abstract class to create your own streamers

[## Usage](#usage)

```
import { convertIfDate } from 'core/json';  
  
import Parser from 'core/json/stream/parser';  
import { ArrayStreamer } from 'core/json/stream/assembler';  
  
const  
  parser = Parser.from('[1, {"a": true}, true, -0.234]', new ArrayStreamer({reviver: convertIfDate}));  
  
for await (const val of parser) {  
  // {index: 0, value: 1}  
  // {index: 1, value: {a: true}}  
  // {index: 2, value: true}  
  // {index: 3, value: -0.234}  
  console.log(val);  
}
```

[## Streamers](#streamers)
[### ObjectStreamer](#objectstreamer)

An instance of the ObjectStreamer class takes an iterable object of parsed tokens of some object and
yields assembled elements of this object.

```
import Parser from 'core/json/stream/parser';  
import { ObjectStreamer } from 'core/json/stream/assembler';  
  
const  
  parser = Parser.from('{"a": 1, "b": true}', new ObjectStreamer());  
  
for await (const val of parser) {  
  // {key: 'a', value: 1}  
  // {key: 'b', value: true}  
  console.log(val);  
}
```

[#### ArrayStreamer](#arraystreamer)

An instance of ArrayStreamer ObjectStreamer class takes an iterable object of parsed tokens of some array and
yields assembled elements of this array.

```
import Parser from 'core/json/stream/parser';  
import { ArrayStreamer } from 'core/json/stream/assembler';  
  
const  
  parser = Parser.from('[1, {"a": true}, true, -0.234]', new ArrayStreamer());  
  
for await (const val of parser) {  
  // {index: 0, value: 1}  
  // {index: 1, value: {a: true}}  
  // {index: 2, value: true}  
  // {index: 3, value: -0.234}  
  console.log(val);  
}
```

[#### AbstractStreamer](#abstractstreamer)

When creating a new streamer class, extend it from the `AbstractStreamer` and implement the `checkToken` and `push` methods.

```
import type { Token } from 'core/json/stream/parser';  
import type { AssemblerOptions } from 'core/json/stream/assembler';  
  
import Streamer, { StreamedArray } from 'core/json/stream/streamers/interface';  
  
export default class ArrayStreamer<T = unknown> extends Streamer<StreamedArray<T>> {  
  /**  
   * Index of the current streamed array element  
   */  
  protected index: number = 0;  
  
  public constructor(opts?: AssemblerOptions) {  
    super(opts);  
  }  
  
  /** @inheritDoc */  
  protected checkToken(chunk: Token): boolean {  
    if (chunk.name !== 'startArray') {  
      throw new TypeError('The top-level object should be an array');  
    }  
  
    return true;  
  }  
  
  /** @inheritDoc */  
  protected*push(): Generator<StreamedArray<T>> {  
    const  
      {value} = this.assembler;  
  
    if (Object.isArray(value) && value.length > 0) {  
      yield {  
        index: this.index++,  
        value: Object.cast(value.pop())  
      };  
    }  
  }  
}
```

[#### API](#api)
[##### constructor](#constructor)

The instance constructor takes one optional parameter.
It is an object with parameters for a token [[Assembler]].

[##### processToken](#processtoken)

Processes the passed JSON token and yields values.

```
import Parser from 'core/json/stream/parser';  
import { ArrayStreamer } from 'core/json/stream/streamers';  
  
const  
  streamer = new Streamer(),  
  values = [];  
  
for (const token of new Parser().processChunk('["foo"]')) {  
  values.push(...streamer.processToken(token));  
}  
  
// ['foo']  
console.log(values);
```

## Index

### References

* [AbstractStreamer](src_core_json_stream_streamers.html#AbstractStreamer)
* [ArrayStreamer](src_core_json_stream_streamers.html#ArrayStreamer)
* [ObjectStreamer](src_core_json_stream_streamers.html#ObjectStreamer)
* [StreamedArray](src_core_json_stream_streamers.html#StreamedArray)
* [StreamedObject](src_core_json_stream_streamers.html#StreamedObject)

## References

### AbstractStreamer

Renames and re-exports [default](../classes/src_core_json_stream_streamers_interface.default.html)

### ArrayStreamer

Renames and re-exports [default](../classes/src_core_json_stream_streamers_array.default.html)

### ObjectStreamer

Renames and re-exports [default](../classes/src_core_json_stream_streamers_object.default.html)

### StreamedArray

Re-exports [StreamedArray](../interfaces/src_core_json_stream_streamers_interface.StreamedArray.html)

### StreamedObject

Re-exports [StreamedObject](../interfaces/src_core_json_stream_streamers_interface.StreamedObject.html)