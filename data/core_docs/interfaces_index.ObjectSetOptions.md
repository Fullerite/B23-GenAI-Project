# Interface ObjectSetOptions
### Hierarchy

* [ObjectGetOptions](index.ObjectGetOptions.html)
  + ObjectSetOptions

## Index

### Properties

* [concat](index.ObjectSetOptions.html#concat)
* [separator](index.ObjectSetOptions.html#separator)

### Methods

* [setter](index.ObjectSetOptions.html#setter)

## Properties

### Optional concat

concat?: boolean

* Defined in [index.d.ts:587](https://github.com/V4Fire/Core/blob/master/index.d.ts#L587)

If true, then a new value will be concatenated with the old

example
:   ```
    const obj = {a: {b: 1}};  
    Object.set(obj, 'a.b', 2, {concat: true})  
    console.log(obj); // [1, 2]
    ```

### Optional separator

separator?: string

Inherited from [ObjectGetOptions](index.ObjectGetOptions.html).[separator](index.ObjectGetOptions.html#separator)

* Defined in [index.d.ts:573](https://github.com/V4Fire/Core/blob/master/index.d.ts#L573)

Character to declare the path

example
:   ```
    Object.get({a: {b: 1}}, 'a:b', {separator: ':'})
    ```

## Methods

### Optional setter

* setter(obj: unknown, key: unknown, value: unknown): any
* setter(obj: unknown, key: unknown, value: unknown): any

* + Defined in [index.d.ts:596](https://github.com/V4Fire/Core/blob/master/index.d.ts#L596)

  Function to set a value

  #### Parameters

  + ##### obj: unknown
  + ##### key: unknown
  + ##### value: unknown

  #### Returns any
* + Defined in dist/index.d.ts:538

  Function to set a value

  #### Parameters

  + ##### obj: unknown
  + ##### key: unknown
  + ##### value: unknown

  #### Returns any