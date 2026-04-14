# Module src/core/uuid
[# core/uuid](#coreuuid)

This module provides API to generate, parse and serialize UUID strings and binary sequences.

[## Usage](#usage)

```
import { generate, serialize, parse } from 'core/uuid';  
  
// Generates UUID v4  
console.log(generate());  
  
const  
  uuid = new Uint8Array([174, 42, 253, 26, 185, 60, 17, 234, 179, 222, 2, 66, 172, 19, 0, 4]);  
  
console.log(parse('ae2afd1a-b93c-11ea-b3de-0242ac130004')) // = uuid  
console.log(serialize(uuid)) // 'ae2afd1a-b93c-11ea-b3de-0242ac130004'
```

[## generate](#generate)

Generates a UUIDv4 buffer and returns it.

[## serialize](#serialize)

Converts the specified binary UUID to a string and returns it.

[## parse](#parse)

Converts the specified UUID string to a binary sequence and returns it.

## Index

### Functions

* [generate](src_core_uuid.html#generate)
* [parse](src_core_uuid.html#parse)
* [serialize](src_core_uuid.html#serialize)

## Functions

### generate

* generate(): Uint8Array

* + Defined in [src/core/uuid/index.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/uuid/index.ts#L20)

  Generates a UUIDv4 buffer and returns it

  #### Returns Uint8Array

### parse

* parse(uuid: string): Uint8Array

* + Defined in [src/core/uuid/index.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/uuid/index.ts#L89)

  Converts the specified UUID string to a binary sequence and returns it

  #### Parameters

  + ##### uuid: string

  #### Returns Uint8Array

### serialize

* serialize(uuid: Uint8Array): string

* + Defined in [src/core/uuid/index.ts:67](https://github.com/V4Fire/Core/blob/master/src/core/uuid/index.ts#L67)

  Converts the specified binary UUID to a string and returns it

  #### Parameters

  + ##### uuid: Uint8Array

  #### Returns string