# Interface ObjectGetOptions
### Hierarchy

* ObjectGetOptions
  + [ObjectSetOptions](index.ObjectSetOptions.html)

## Index

### Properties

* [separator](index.ObjectGetOptions.html#separator)

## Properties

### Optional separator

separator?: string

* Defined in [index.d.ts:573](https://github.com/V4Fire/Core/blob/master/index.d.ts#L573)

Character to declare the path

example
:   ```
    Object.get({a: {b: 1}}, 'a:b', {separator: ':'})
    ```