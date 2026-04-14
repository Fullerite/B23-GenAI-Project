# Module src/core/semver/const
## Index

### Variables

* [compareRgxp](src_core_semver_const.html#compareRgxp)
* [operandLengthErrorText](src_core_semver_const.html#operandLengthErrorText)
* [operations](src_core_semver_const.html#operations)

## Variables

### Const compareRgxp

compareRgxp: RegExp = ...

* Defined in [src/core/semver/const.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/semver/const.ts#L22)

### Const operandLengthErrorText

operandLengthErrorText: "Can't compare versions. The operand has an empty value." = 'Can\'t compare versions. The operand has an empty value.'

* Defined in [src/core/semver/const.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/semver/const.ts#L25)

### Const operations

operations: Record<[Operation](src_core_semver_interface.html#Operation), (a: number, b: number) => boolean> = ...

* Defined in [src/core/semver/const.ts:11](https://github.com/V4Fire/Core/blob/master/src/core/semver/const.ts#L11)