# Interface ObjectMixinOptions<V, K, D>
### Type parameters

* #### V = unknown
* #### K = unknown
* #### D = unknown

### Hierarchy

* ObjectMixinOptions

## Index

### Properties

* [concatArray](index.ObjectMixinOptions.html#concatArray)
* [concatArrays](index.ObjectMixinOptions.html#concatArrays)
* [deep](index.ObjectMixinOptions.html#deep)
* [onlyNew](index.ObjectMixinOptions.html#onlyNew)
* [propsToCopy](index.ObjectMixinOptions.html#propsToCopy)
* [skipUndefs](index.ObjectMixinOptions.html#skipUndefs)
* [traits](index.ObjectMixinOptions.html#traits)
* [withAccessors](index.ObjectMixinOptions.html#withAccessors)
* [withDescriptor](index.ObjectMixinOptions.html#withDescriptor)
* [withDescriptors](index.ObjectMixinOptions.html#withDescriptors)
* [withNonEnumerables](index.ObjectMixinOptions.html#withNonEnumerables)
* [withProto](index.ObjectMixinOptions.html#withProto)
* [withUndef](index.ObjectMixinOptions.html#withUndef)

### Methods

* [concatFn](index.ObjectMixinOptions.html#concatFn)
* [extendFilter](index.ObjectMixinOptions.html#extendFilter)
* [filter](index.ObjectMixinOptions.html#filter)

## Properties

### Optional concatArray

concatArray?: boolean

* Defined in [index.d.ts:525](https://github.com/V4Fire/Core/blob/master/index.d.ts#L525)

deprecated

see
:   [ObjectMixinOptions.concatArrays](index.ObjectMixinOptions.html#concatArrays)

### Optional concatArrays

concatArrays?: boolean | ((a: unknown[], b: unknown[], key: K) => unknown[])

* Defined in [index.d.ts:519](https://github.com/V4Fire/Core/blob/master/index.d.ts#L519)

If true, then to merge two arrays will be used a concatenation strategy (works only with the `deep` mode).
Also, the parameter can be passed as a function to concatenate arrays.

default
:   `false`

example
:   ```
    // {a: [2]}  
    Object.mixin({deep: true, concatArrays: false}, {a: [1]}, {a: [2]});  
      
    // {a: [1, 2]}  
    Object.mixin({deep: true, concatArrays: true}, {a: [1]}, {a: [2]});  
      
    // {a: [1, 1, 2]}  
    Object.mixin({deep: true, concatArrays: true}, {a: [1]}, {a: [1, 2]});  
      
    // {a: [1, 2]}  
    Object.mixin({deep: true, concatArrays: (a, b) => a.union(b)}, {a: [1]}, {a: [1, 2]});
    ```

### Optional deep

deep?: boolean

* Defined in [index.d.ts:349](https://github.com/V4Fire/Core/blob/master/index.d.ts#L349)

If true, then object properties are copied recursively.
Also, this mode enables copying properties from a prototype.

default
:   `false`

example
:   ```
    // {a: {c: 2}}  
    Object.mixin({deep: false}, {a: {b: 1}}, {a: {c: 2}});  
      
    // {a: {b: 1, c: 2}}  
    Object.mixin({deep: true}, {a: {b: 1}}, {a: {c: 2}});  
      
    // {a: {c: 2}}  
    Object.mixin({deep: true}, {}, {__proto__: {a: {c: 2}}});
    ```

### Optional onlyNew

onlyNew?: boolean | -1

* Defined in [index.d.ts:537](https://github.com/V4Fire/Core/blob/master/index.d.ts#L537)

deprecated

see
:   [ObjectMixinOptions.propsToCopy](index.ObjectMixinOptions.html#propsToCopy)

### Optional propsToCopy

propsToCopy?: "all" | "new" | "exist"

* Defined in [index.d.ts:370](https://github.com/V4Fire/Core/blob/master/index.d.ts#L370)

Strategy to resolve collisions of properties when merging:

1. `'all'` - all properties are merged in spite of possible collisions (by default)
2. `'new'` - properties with collisions aren't merged
3. `'exist'` - properties without collisions aren't merged

default
:   `'all'`

example
:   ```
    // {a: 2, b: 3}  
    Object.mixin({propsToCopy: 'all'}, {a: 1}, {a: 2, b: 3});  
      
    // {a: 1, b: 3}  
    Object.mixin({propsToCopy: 'new'}, {a: 1}, {a: 2, b: 3});  
      
    // {a: 2}  
    Object.mixin({propsToCopy: 'exist'}, {a: 1}, {a: 2, b: 3});
    ```

### Optional skipUndefs

skipUndefs?: boolean

* Defined in [index.d.ts:422](https://github.com/V4Fire/Core/blob/master/index.d.ts#L422)

If true, all properties with undefined value aren't copied

default
:   `true`

example
:   ```
    // {a: 1}  
    Object.mixin({skipUndefs: true}, {a: 1}, {a: undefined});  
      
    // {a: undefined}  
    Object.mixin({skipUndefs: false}, {a: 1}, {a: undefined});
    ```

### Optional traits

traits?: boolean | -1

* Defined in [index.d.ts:543](https://github.com/V4Fire/Core/blob/master/index.d.ts#L543)

deprecated

see
:   [ObjectMixinOptions.propsToCopy](index.ObjectMixinOptions.html#propsToCopy)

### Optional withAccessors

withAccessors?: boolean

* Defined in [index.d.ts:561](https://github.com/V4Fire/Core/blob/master/index.d.ts#L561)

deprecated

see
:   [ObjectMixinOptions.withDescriptors](index.ObjectMixinOptions.html#withDescriptors)

### Optional withDescriptor

withDescriptor?: boolean

* Defined in [index.d.ts:555](https://github.com/V4Fire/Core/blob/master/index.d.ts#L555)

deprecated

see
:   [ObjectMixinOptions.withDescriptors](index.ObjectMixinOptions.html#withDescriptors)

### Optional withDescriptors

withDescriptors?: boolean | "onlyAccessors"

* Defined in [index.d.ts:447](https://github.com/V4Fire/Core/blob/master/index.d.ts#L447)

Should or shouldn't copy property descriptors too.
If passed `onlyAccessors`, the descriptor properties like `enumerable` or `configurable` are ignored.

default
:   `false`

### Optional withNonEnumerables

withNonEnumerables?: boolean

* Defined in [index.d.ts:439](https://github.com/V4Fire/Core/blob/master/index.d.ts#L439)

If true, the function will merge all object properties, but not only enumerable.
Non-enumerable properties from a prototype are ignored.

default
:   `false`

example
:   ```
    const obj = {a: 1};  
      
    Object.defineProperty(obj, 'b', {value: 2});  
      
    // {a: 1, b: 2}  
    Object.mixin({withNonEnumerables: true}, {}, obj);
    ```

### Optional withProto

withProto?: boolean

* Defined in [index.d.ts:497](https://github.com/V4Fire/Core/blob/master/index.d.ts#L497)

If true, then merging preserve prototypes of properties
(works only with the `deep` mode)

default
:   `false`

example
:   ```
    const proto = {  
      a: {  
        b: 2  
      },  
      
      c: 3  
    };  
      
    const obj = Object.create(proto);  
    Object.mixin({deep: true, withProto: false}, obj, {c: 2, a: {d: 4}});  
      
    // 2  
    // 4  
    // 2  
    // true  
    // true  
    console.log(  
      obj.c,  
      obj.a.d,  
      obj.a.b,  
      obj.a.hasOwnProperty('d'),  
      obj.a.hasOwnProperty('b')  
    );  
      
    const obj2 = Object.create(proto);  
    Object.mixin({deep: true, withProto: true}, obj2, {c: 2, a: {d: 4}});  
      
    // 2  
    // 4  
    // 2  
    // true  
    // false  
    console.log(  
      obj2.c,  
      obj2.a.d,  
      obj2.a.b,  
      obj2.a.hasOwnProperty('d'),  
      obj2.a.hasOwnProperty('b')  
    );
    ```

### Optional withUndef

withUndef?: boolean

* Defined in [index.d.ts:549](https://github.com/V4Fire/Core/blob/master/index.d.ts#L549)

deprecated

see
:   [ObjectMixinOptions.skipUndefs](index.ObjectMixinOptions.html#skipUndefs)

## Methods

### Optional concatFn

* concatFn(a: unknown[], b: unknown[], key: K): unknown[]
* concatFn(a: unknown[], b: unknown[], key: K): unknown[]

* + Defined in [index.d.ts:531](https://github.com/V4Fire/Core/blob/master/index.d.ts#L531)

  deprecated

  see
  :   [ObjectMixinOptions.concatArrays](index.ObjectMixinOptions.html#concatArrays)

  #### Parameters

  + ##### a: unknown[]
  + ##### b: unknown[]
  + ##### key: K

  #### Returns unknown[]
* + Defined in dist/index.d.ts:473

  deprecated

  see
  :   [ObjectMixinOptions.concatArrays](index.ObjectMixinOptions.html#concatArrays)

  #### Parameters

  + ##### a: unknown[]
  + ##### b: unknown[]
  + ##### key: K

  #### Returns unknown[]

### Optional extendFilter

* extendFilter(el: unknown, key: K, data: V): any
* extendFilter(el: unknown, key: K, data: V): any

* + Defined in [index.d.ts:407](https://github.com/V4Fire/Core/blob/master/index.d.ts#L407)

  Function to filter values that support deep extending
  (works only with the `deep` mode)

  example
  :   ```
      // {a: {a: 1, b: 2}}  
      Object.mixin({deep: true}, {a: {a: 1}}, {a: {b: 2}});  
        
      // {a: {b: 2}}  
      Object.mixin({deep: true, extendFilter: (el) => !el.b}, {a: {a: 1}}, {a: {b: 2}});
      ```

  #### Parameters

  + ##### el: unknown

    element value
  + ##### key: K

    element key
  + ##### data: V

    element container

  #### Returns any
* + Defined in dist/index.d.ts:349

  Function to filter values that support deep extending
  (works only with the `deep` mode)

  example
  :   ```
      // {a: {a: 1, b: 2}}  
      Object.mixin({deep: true}, {a: {a: 1}}, {a: {b: 2}});  
        
      // {a: {b: 2}}  
      Object.mixin({deep: true, extendFilter: (el) => !el.b}, {a: {a: 1}}, {a: {b: 2}});
      ```

  #### Parameters

  + ##### el: unknown

    element value
  + ##### key: K

    element key
  + ##### data: V

    element container

  #### Returns any

### Optional filter

* filter(el: V, key: K, data: D): any
* filter(el: V, key: K, data: D): any

* + Defined in [index.d.ts:388](https://github.com/V4Fire/Core/blob/master/index.d.ts#L388)

  Function to filter values that shouldn't be copied

  example
  :   ```
      // {a: 1, b: 2}  
      Object.mixin({deep: true}, {a: 1}, {b: 2});  
        
      // {a: 1}  
      Object.mixin({deep: true, filter: (el, key) => key !== 'b'}, {a: 1}, {b: 2});
      ```

  #### Parameters

  + ##### el: V

    element value
  + ##### key: K

    element key
  + ##### data: D

    element container

  #### Returns any
* + Defined in dist/index.d.ts:330

  Function to filter values that shouldn't be copied

  example
  :   ```
      // {a: 1, b: 2}  
      Object.mixin({deep: true}, {a: 1}, {b: 2});  
        
      // {a: 1}  
      Object.mixin({deep: true, filter: (el, key) => key !== 'b'}, {a: 1}, {b: 2});
      ```

  #### Parameters

  + ##### el: V

    element value
  + ##### key: K

    element key
  + ##### data: D

    element container

  #### Returns any