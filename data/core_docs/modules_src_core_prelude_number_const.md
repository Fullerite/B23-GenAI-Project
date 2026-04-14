# Module src/core/prelude/number/const
## Index

### Variables

* [boolAliases](src_core_prelude_number_const.html#boolAliases)
* [decPartRgxp](src_core_prelude_number_const.html#decPartRgxp)
* [defaultFormats](src_core_prelude_number_const.html#defaultFormats)
* [formatAliases](src_core_prelude_number_const.html#formatAliases)
* [formatCache](src_core_prelude_number_const.html#formatCache)
* [globalFormatOpts](src_core_prelude_number_const.html#globalFormatOpts)

## Variables

### Const boolAliases

boolAliases: Pick<{ +: boolean; -: boolean }, "+" | "-"> = ...

* Defined in [src/core/prelude/number/const.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/const.ts#L28)

### Const decPartRgxp

decPartRgxp: RegExp = ...

* Defined in [src/core/prelude/number/const.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/const.ts#L13)

### Const defaultFormats

defaultFormats: Pick<NumberFormatOptions, keyof NumberFormatOptions> = ...

* Defined in [src/core/prelude/number/const.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/const.ts#L33)

### Const formatAliases

formatAliases: Pick<{ $: string; $d: string; %: string; .: string }, "." | "$" | "$d" | "%"> = ...

* Defined in [src/core/prelude/number/const.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/const.ts#L21)

### Const formatCache

formatCache: [Dictionary](../interfaces/index.Dictionary.html)<NumberFormat> = ...

* Defined in [src/core/prelude/number/const.ts:10](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/const.ts#L10)

### Const globalFormatOpts

globalFormatOpts: Pick<{ decimal: string; init: boolean; thousands: string }, "init" | "decimal" | "thousands"> = ...

* Defined in [src/core/prelude/number/const.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/prelude/number/const.ts#L15)