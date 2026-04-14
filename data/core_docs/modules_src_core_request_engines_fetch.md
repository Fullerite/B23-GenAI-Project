# Module src/core/request/engines/fetch
[# core/request/engines/fetch](#corerequestenginesfetch)

This module provides a function that creates a request engine based on the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).
Mind, this API is developed to work in a browser — node.js support only for tests.

[## Synopsis](#synopsis)

* The engine is used by default in a browser if it supports `AbortController`.
* The engine supports response streaming.

[## Example](#example)

```
import fetchEngine from 'core/request/engines/fetch';  
  
req('/search', {engine: fetchEngine}).then(({response}) => {  
  console.log(response.decode());  
});
```

## Index

### Variables

* [default](src_core_request_engines_fetch.html#default)

## Variables

### Const default

default: [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html) = ...

* Defined in [src/core/request/engines/fetch/index.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/request/engines/fetch/index.ts#L32)

Creates request by using the fetch API with the specified parameters and returns a promise

param params