# Module src/core/request/engines/node
[# core/request/engines/node](#corerequestenginesnode)

This module provides a function that creates a request engine for node.js scripts.

[## Synopsis](#synopsis)

* The engine is used by default in a node.js.
* The engine uses [Got](https://www.npmjs.com/package/got) as a request library.
* The engine supports response streaming.

[## Example](#example)

```
import nodeEngine from 'core/request/engines/node';  
  
req('/search', {engine: nodeEngine}).then(({response}) => {  
  console.log(response.decode());  
});
```

## Index

### Variables

* [default](src_core_request_engines_node.html#default)

## Variables

### Const default

default: [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html) = ...

* Defined in [src/core/request/engines/node/index.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/request/engines/node/index.ts#L31)

Creates request by using node.js with the specified parameters and returns a promise

param params