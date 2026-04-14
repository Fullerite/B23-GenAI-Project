# Interface AndPickOptions
### Hierarchy

* [FilterOptions](src_core_json_stream_filters_interface.FilterOptions.html)
  + AndPickOptions

## Index

### Properties

* [from](src_core_json_stream_interface.AndPickOptions.html#from)
* [multiple](src_core_json_stream_interface.AndPickOptions.html#multiple)

## Properties

### Optional from

from?: "object" | "array"

* Defined in [src/core/json/stream/interface.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/interface.ts#L40)

A type of parsed structure in which the picking takes place

default
:   `'object'`

example
:   ```
    const tokens = intoIter(from(JSON.stringify([  
      {user: 'Bob', age: 21},  
      {user: 'Ben', age: 24},  
      {user: 'Rob', age: 28}  
    ])));  
      
    const seq = sequence(  
      assemble(pick(tokens, '0')),  
      
      // 1 refers to `{user: ‘Rob’, age: 28}` because `{user: ‘Bob’, age: 21}` is already picked previously,  
      // i.e. selector tight to the previous  
      assemble(andPick(tokens, '1', {from: 'array'}))  
    );  
      
    for await (const val of seq) {  
      // {user: 'Bob', age: 21}  
      // {user: 'Rob', age: 28}  
      console.log(val);  
    }
    ```

### Optional multiple

multiple?: boolean

Inherited from [FilterOptions](src_core_json_stream_filters_interface.FilterOptions.html).[multiple](src_core_json_stream_filters_interface.FilterOptions.html#multiple)

* Defined in [src/core/json/stream/filters/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/interface.ts#L19)

If true the filtration will return all matched filter results, otherwise only the first match will be returned