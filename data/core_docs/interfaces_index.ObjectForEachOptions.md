# Interface ObjectForEachOptions
### Hierarchy

* ObjectForEachOptions

## Index

### Properties

* [notOwn](index.ObjectForEachOptions.html#notOwn)
* [passDescriptor](index.ObjectForEachOptions.html#passDescriptor)
* [propsToIterate](index.ObjectForEachOptions.html#propsToIterate)
* [withDescriptor](index.ObjectForEachOptions.html#withDescriptor)
* [withNonEnumerables](index.ObjectForEachOptions.html#withNonEnumerables)

## Properties

### Optional notOwn

notOwn?: boolean | -1

* Defined in [index.d.ts:671](https://github.com/V4Fire/Core/blob/master/index.d.ts#L671)

deprecated

see
:   [ObjectForEachOptions.propsToIterate](index.ObjectForEachOptions.html#propsToIterate)

### Optional passDescriptor

passDescriptor?: boolean

* Defined in [index.d.ts:612](https://github.com/V4Fire/Core/blob/master/index.d.ts#L612)

If true, then the callback function takes an element descriptor instead of a value

default
:   `false`

example
:   ```
    Object.forEach({a: 1}, {showDescriptor: true}, (el) => {  
      // {configurable: true, enumerable: true, writable: true, value: 1}  
      console.log(el);  
    });
    ```

### Optional propsToIterate

propsToIterate?: "all" | "own" | "inherited"

* Defined in [index.d.ts:639](https://github.com/V4Fire/Core/blob/master/index.d.ts#L639)

Strategy to iterate object properties:

1. `'own'` - the object iterates only own properties (by default)
2. `'inherited'` - the object iterates only inherited properties
   (for-in with the negative `hasOwnProperty` check)

3. `'all'` - the object iterates inherited properties too (for-in without the `hasOwnProperty` check)

example
:   ```
    const obj = {a: 1, __proto__: {b: 2}};  
      
    Object.forEach(obj, (el) => {  
      console.log(el); // 1  
    });  
      
    Object.forEach(obj, {propsToIterate: 'all'}, (el) => {  
      console.log(el); // 1 2  
    });  
      
    Object.forEach(obj, {propsToIterate: 'inherited'}, (el) => {  
      console.log(el); // 2  
    });
    ```

### Optional withDescriptor

withDescriptor?: boolean

* Defined in [index.d.ts:665](https://github.com/V4Fire/Core/blob/master/index.d.ts#L665)

deprecated

see
:   [ObjectForEachOptions.passDescriptor](index.ObjectForEachOptions.html#passDescriptor)

### Optional withNonEnumerables

withNonEnumerables?: boolean

* Defined in [index.d.ts:659](https://github.com/V4Fire/Core/blob/master/index.d.ts#L659)

If true, the function will iterate all object properties, but not only enumerable.
Non-enumerable properties from a prototype are ignored.

default
:   `false`

example
:   ```
    const obj = {a: 1};  
      
    Object.defineProperty(obj, 'b', {value: 2});  
      
    // 1  
    // 2  
    Object.forEach(obj, {withNonEnumerables: true}, (el) => {  
      console.log(el);  
    });
    ```