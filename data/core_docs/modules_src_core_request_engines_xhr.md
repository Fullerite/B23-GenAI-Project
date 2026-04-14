# Module src/core/request/engines/xhr
[# core/request/engines/xhr](#corerequestenginesxhr)

This module provides a function that creates a request engine based on the [XMLHttpRequest API](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest).
Mind, this API is developed to work in a browser — node.js support only for tests.

[## Synopsis](#synopsis)

* The engine is used by default in a browser if it doesn't support `AbortController`.
* The engine partly supports response streaming (only `total`/`loaded` fields without `data`).
* The engine provides a bunch of internal events.

[## Example](#example)

```
import xhrEngine from 'core/request/engines/xhr';  
  
const req = req('/search', {engine: xhrEngine}).then(({response}) => {  
  console.log(response.decode());  
});  
  
req.emitter.on('progress', () => {  
  // ..  
});  
  
req.emitter.on('upload.progress', () => {  
  // ..  
});
```

## Index

### Variables

* [default](src_core_request_engines_xhr.html#default)

## Variables

### Const default

default: [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html) = ...

* Defined in [src/core/request/engines/xhr/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/request/engines/xhr/index.ts#L34)

Creates request by using XMLHttpRequest with the specified parameters and returns a promise

param params