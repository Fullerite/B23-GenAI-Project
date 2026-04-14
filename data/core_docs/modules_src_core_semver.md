# Module src/core/semver
[# core/semver](#coresemver)

This module provides a function to compare string versions by using semver strategy.

```
import check from 'core/semver';  
  
console.log(check('1.4.1', '1.5.2', '>'));  // false  
console.log(check('1', '1.5.2', '=='));     // true  
console.log(check('2.4.1', '2.4', '<='));   // true  
console.log(check('2.4', '2.4.2', '^='));   // true
```

[## Supported Comparisons](#supported-comparisons)
> Note:
> The module currently supports only a numeric comparison with x-ranges. Without `beta`, `alpha` or `rc` postfixes.

* `==` equal
* `^=` caret range
* `~=` tilda range
* `>` greater than
* `<` less than
* `>=` greater than or equal to
* `<=` less than or equal to

## Index

### References

* [ComparisonOptions](src_core_semver.html#ComparisonOptions)
* [Operation](src_core_semver.html#Operation)
* [Strategy](src_core_semver.html#Strategy)
* [compareRgxp](src_core_semver.html#compareRgxp)
* [operandLengthErrorText](src_core_semver.html#operandLengthErrorText)
* [operations](src_core_semver.html#operations)

### Functions

* [default](src_core_semver.html#default)

## References

### ComparisonOptions

Re-exports [ComparisonOptions](../interfaces/src_core_semver_interface.ComparisonOptions.html)

### Operation

Re-exports [Operation](src_core_semver_interface.html#Operation)

### Strategy

Re-exports [Strategy](src_core_semver_interface.html#Strategy)

### compareRgxp

Re-exports [compareRgxp](src_core_semver_const.html#compareRgxp)

### operandLengthErrorText

Re-exports [operandLengthErrorText](src_core_semver_const.html#operandLengthErrorText)

### operations

Re-exports [operations](src_core_semver_const.html#operations)

## Functions

### default

* default(a: string, b: string, op: [Operation](src_core_semver_interface.html#Operation), opts?: [ComparisonOptions](../interfaces/src_core_semver_interface.ComparisonOptions.html)): boolean

* + Defined in [src/core/semver/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/semver/index.ts#L28)

  Compares two strings with number versions (a  b) by using the semver strategy

  #### Parameters

  + ##### a: string
  + ##### b: string
  + ##### op: [Operation](src_core_semver_interface.html#Operation)

    operation type
  + ##### opts: [ComparisonOptions](../interfaces/src_core_semver_interface.ComparisonOptions.html) = ...

  #### Returns boolean