# Module src/core/object/select
[# core/object/select](#coreobjectselect)

This module provides a function to find an element from an object by the specified parameters.
The function is useful for declarative searching from data without functions, i.e., we can take parameters to search from JSON
or other stuff.

[## Searching upon a plain object](#searching-upon-a-plain-object)

When the search function takes a plain object and some `where` condition, it returns the object itself if it matches the condition.
Otherwise, it returns `undefined`.

```
import select from 'core/object/select';  
  
// {foo: 1, bar: 2}  
select({foo: 1, bar: 2}, {where: {foo: 1}});  
  
// undefined  
select({foo: 1, bar: 2}, {where: {foo: 1, bar: 3}});
```

The matching process is recursive, i.e., it checks the nested structure of the condition and object.

```
import select from 'core/object/select';  
  
// {foo: {b: [1, 2, 3]}}  
select({foo: {b: [1, 2, 3]}}, {where: {foo: {b: [1, 2, 3]}}});  
  
// undefined  
select({foo: {b: [1, 2, 3]}}, {where: {foo: {b: [1]}}});
```

If the object to search doesn't have some property from `where`, the property will be ignored if other conditions are matched.

```
import select from 'core/object/select';  
  
// {foo: 1, bar: 2}  
select({foo: 1, bar: 2}, {where: {baz: 78, foo: 1}});  
  
// undefined  
select({foo: 1, bar: 2}, {where: {baz: 78}});
```

[## Searching upon an iterable object](#searching-upon-an-iterable-object)

When the search function takes an iterable object and some `where` condition, it returns the first element from the object
that matches the condition. If there are no elements that match the condition, the function returns undefined.

```
import select from 'core/object/select';  
  
// {foo: 1, bar: 2}  
select([{bla: 12}, {foo: 1, bar: 2}], {where: {foo: 1}});  
  
// undefined  
select(new Set([{bla: 12}, {foo: 1, bar: 2}]), {where: {foo: 1, bar: 3}});
```

[## Providing multiple conditions to search](#providing-multiple-conditions-to-search)

When `where` contains an array, it will be represented as the `OR` condition.

```
import select from 'core/object/select';  
  
// {test: 2}  
select({test: 2}, {where: [{test: 1}, {test: 2}]});
```

[## Providing a context to search](#providing-a-context-to-search)

By using the `from` option, you can define a start point to search.

```
import select from 'core/object/select';  
  
// {foo: 1, bar: 2}  
select({my: {data: {foo: 1, bar: 2}}}, {where: {foo: 1}, from: 'my.data'});  
  
// undefined  
select(new Map([[0, {data: {foo: 1, bar: 2}}]]), {where: {foo: 21}, from: [0, 'data']});
```

If there is no provided `where` condition but specified `from`, the function returns a value by the path.

```
import select from 'core/object/select';  
  
// {foo: 1, bar: 2}  
select({my: {data: {foo: 1, bar: 2}}}, {from: 'my.data'});  
  
// {foo: 1, bar: 2}  
select(new Map([[0, {data: {foo: 1, bar: 2}}]]), {from: [0, 'data']});
```

## Index

### References

* [SelectParams](src_core_object_select.html#SelectParams)

### Functions

* [default](src_core_object_select.html#default)

## References

### SelectParams

Re-exports [SelectParams](../interfaces/src_core_object_select_interface.SelectParams.html)

## Functions

### default

* default<T>(obj: unknown, params?: [SelectParams](../interfaces/src_core_object_select_interface.SelectParams.html)): [CanUndef](index.html#CanUndef)<T>

* + Defined in [src/core/object/select/index.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/object/select/index.ts#L24)

  Finds an element from an object by the specified parameters

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: unknown

    object to search
  + ##### params: [SelectParams](../interfaces/src_core_object_select_interface.SelectParams.html) = {}

  #### Returns [CanUndef](index.html#CanUndef)<T>