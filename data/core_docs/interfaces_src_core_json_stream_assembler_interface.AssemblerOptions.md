# Interface AssemblerOptions
### Hierarchy

* AssemblerOptions

## Index

### Properties

* [numberAsString](src_core_json_stream_assembler_interface.AssemblerOptions.html#numberAsString)
* [reviver](src_core_json_stream_assembler_interface.AssemblerOptions.html#reviver)

## Properties

### Optional numberAsString

numberAsString?: boolean

* Defined in [src/core/json/stream/assembler/interface.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/interface.ts#L14)

Should or not parse numeric values as string literals

default
:   `false`

### Optional reviver

reviver?: [JSONCb](index.JSONCb.html)

* Defined in [src/core/json/stream/assembler/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/assembler/interface.ts#L19)

Reviver function similar to `JSON.parse`