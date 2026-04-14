# Interface SelectParams
### Hierarchy

* SelectParams

## Index

### Properties

* [from](src_core_object_select_interface.SelectParams.html#from)
* [where](src_core_object_select_interface.SelectParams.html#where)

## Properties

### Optional from

from?: number | [ObjectPropertyPath](../modules/index.html#ObjectPropertyPath)

* Defined in [src/core/object/select/interface.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/object/select/interface.ts#L18)

Path to an object property

example
:   ```
    select({foo: {bar: {bla: {}}}}, {from: 'foo.bla'})
    ```

### Optional where

where?: [CanArray](../modules/index.html#CanArray)<[Dictionary](index.Dictionary.html)<unknown>>

* Defined in [src/core/object/select/interface.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/object/select/interface.ts#L30)

Object to match or array of objects.
The array is interpreted as "or".

example
:   ```
    select({test: 2}, {where: {test: 2}}) // {test: 2}  
    select({test: 2}, {where: [{test: 1}, {test: 2}]}) // {test: 2}
    ```