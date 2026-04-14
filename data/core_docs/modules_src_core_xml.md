# Module src/core/xml
[# core/xml](#corexml)

This module provides a bunch of helper functions to work with XML documents.

[## toDataURI](#todatauri)

Converts the specified XML node to a `DATA:URI` string.

```
import { toDataURI } from 'core/xml';  
import { getDataTypeFromURI } from 'core/mime-type';  
  
const node = document.createElement('foo');  
node.innerHTML = 'hello';  
  
// "data:image/svg+xml;%3Cfoo xmlns='http://www.w3.org/1999/xhtml'%3Ehello%3C/foo%3E"  
console.log(toDataURI(node));  
  
// document  
console.log(getDataTypeFromURI(toDataURI(node)));
```

## Index

### Functions

* [toDataURI](src_core_xml.html#toDataURI)

## Functions

### toDataURI

* toDataURI(node: Node): string

* + Defined in [src/core/xml/index.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/xml/index.ts#L21)

  Converts the specified XML node to a DATA:URI string

  #### Parameters

  + ##### node: Node

  #### Returns string