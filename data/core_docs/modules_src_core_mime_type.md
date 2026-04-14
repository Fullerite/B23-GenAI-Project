# Module src/core/mime-type
[# core/mime-type](#coremime-type)

This module provides API to extract data types from mime-type/DATA:URI strings.

[## getDataType](#getdatatype)

Returns a type of data from the specified mime type string.

```
import { getDataType } from 'core/mine-type';  
  
console.log(getDataType('application/json')); // json
```

[## getDataTypeFromURI](#getdatatypefromuri)

Returns a type of data from the specified DATA:URI string.

```
import { getDataTypeFromURI } from 'core/mine-type';  
  
console.log(getDataTypeFromURI('data:application/javascript;...')); // text
```

## Index

### References

* [DataType](src_core_mime_type.html#DataType)
* [dataURIRgxp](src_core_mime_type.html#dataURIRgxp)
* [isTextType](src_core_mime_type.html#isTextType)
* [isXMLType](src_core_mime_type.html#isXMLType)
* [mimeTypes](src_core_mime_type.html#mimeTypes)
* [normalizeMimeStrRgxp](src_core_mime_type.html#normalizeMimeStrRgxp)

### Functions

* [getDataType](src_core_mime_type.html#getDataType)
* [getDataTypeFromURI](src_core_mime_type.html#getDataTypeFromURI)
* [getDataTypeFromURL](src_core_mime_type.html#getDataTypeFromURL)

## References

### DataType

Re-exports [DataType](src_core_mime_type_interface.html#DataType)

### dataURIRgxp

Re-exports [dataURIRgxp](src_core_mime_type_const.html#dataURIRgxp)

### isTextType

Re-exports [isTextType](src_core_mime_type_const.html#isTextType)

### isXMLType

Re-exports [isXMLType](src_core_mime_type_const.html#isXMLType)

### mimeTypes

Re-exports [mimeTypes](src_core_mime_type_const.html#mimeTypes)

### normalizeMimeStrRgxp

Re-exports [normalizeMimeStrRgxp](src_core_mime_type_const.html#normalizeMimeStrRgxp)

## Functions

### getDataType

* getDataType(str: string): [DataType](src_core_mime_type_interface.html#DataType)

* + Defined in [src/core/mime-type/index.ts:44](https://github.com/V4Fire/Core/blob/master/src/core/mime-type/index.ts#L44)

  Returns a type of data from the specified mime type string

  #### Parameters

  + ##### str: string

  #### Returns [DataType](src_core_mime_type_interface.html#DataType)

### getDataTypeFromURI

* getDataTypeFromURI(uri: string): [CanUndef](index.html#CanUndef)<[DataType](src_core_mime_type_interface.html#DataType)>

* + Defined in [src/core/mime-type/index.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/mime-type/index.ts#L26)

  Returns a type of data from the specified DATA:URI string

  #### Parameters

  + ##### uri: string

  #### Returns [CanUndef](index.html#CanUndef)<[DataType](src_core_mime_type_interface.html#DataType)>

### getDataTypeFromURL

* getDataTypeFromURL(url: string): [CanUndef](index.html#CanUndef)<[DataType](src_core_mime_type_interface.html#DataType)>

* + Defined in [src/core/mime-type/index.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/mime-type/index.ts#L35)

  deprecated

  see
  :   [getDataTypeFromURI](src_core_mime_type.html#getDataTypeFromURI)

  #### Parameters

  + ##### url: string

  #### Returns [CanUndef](index.html#CanUndef)<[DataType](src_core_mime_type_interface.html#DataType)>