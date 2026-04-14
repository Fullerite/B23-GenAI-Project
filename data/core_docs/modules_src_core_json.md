# Module src/core/json
[# core/json](#corejson)

This module provides a bunch of helper functions to serialize/parse JSON data.

[## Stream API](#stream-api)

The `core/json/stream` submodule provides API to work with JSON in a stream form.

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

[## Revivers](#revivers)
[### convertIfDate](#convertifdate)

A reviver for the `JSON.parse` method: converts all strings that are looks like a date to Date.

```
import { convertIfDate } from 'core/json';  
  
// true  
console.log(JSON.parse('"2015-10-12"', convertIfDate).is(new Date(2015, 9, 12)));
```

## Index

### Functions

* [convertIfDate](src_core_json.html#convertIfDate)

## Functions

### convertIfDate

* convertIfDate(key: string, value: unknown): unknown

* + Defined in [src/core/json/index.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/json/index.ts#L30)

  Reviver for the `JSON.parse` method: converts all strings that are looks like a date to Date

  example
  :   ```
      JSON.parse('"2015-10-12"', convertIfDate) instanceof Date // true
      ```

  #### Parameters

  + ##### key: string
  + ##### value: unknown

  #### Returns unknown