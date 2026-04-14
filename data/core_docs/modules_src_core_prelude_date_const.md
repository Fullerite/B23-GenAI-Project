# Module src/core/prelude/date/const
## Index

### Variables

* [boolAliases](src_core_prelude_date_const.html#boolAliases)
* [createAliases](src_core_prelude_date_const.html#createAliases)
* [dateChunkRgxp](src_core_prelude_date_const.html#dateChunkRgxp)
* [defaultFormats](src_core_prelude_date_const.html#defaultFormats)
* [formatAliases](src_core_prelude_date_const.html#formatAliases)
* [formatCache](src_core_prelude_date_const.html#formatCache)
* [isDateStr](src_core_prelude_date_const.html#isDateStr)
* [isFloatStr](src_core_prelude_date_const.html#isFloatStr)
* [normalizeDateChunkRgxp](src_core_prelude_date_const.html#normalizeDateChunkRgxp)
* [normalizeZoneRgxp](src_core_prelude_date_const.html#normalizeZoneRgxp)
* [timeChunkRgxp](src_core_prelude_date_const.html#timeChunkRgxp)
* [zoneChunkRgxp](src_core_prelude_date_const.html#zoneChunkRgxp)

## Variables

### Const boolAliases

boolAliases: Pick<{ +: boolean; -: boolean }, "+" | "-"> = ...

* Defined in [src/core/prelude/date/const.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L72)

### Const createAliases

createAliases: Pick<{ now: () => Date; today: () => Date; tomorrow: () => Date; yesterday: () => Date }, "now" | "today" | "yesterday" | "tomorrow"> = ...

* Defined in [src/core/prelude/date/const.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L25)

### Const dateChunkRgxp

dateChunkRgxp: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:13](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L13)

### Const defaultFormats

defaultFormats: Pick<DateTimeFormatOptions, keyof DateTimeFormatOptions> = ...

* Defined in [src/core/prelude/date/const.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L77)

### Const formatAliases

formatAliases: Pick<{ M: string; Y: string; d: string; e: string; h: string; m: string; s: string; w: string; z: string }, "e" | "Y" | "M" | "d" | "w" | "h" | "m" | "s" | "z"> = ...

* Defined in [src/core/prelude/date/const.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L42)

### Const formatCache

formatCache: [Dictionary](../interfaces/index.Dictionary.html)<DateTimeFormat> = ...

* Defined in [src/core/prelude/date/const.ts:10](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L10)

### Const isDateStr

isDateStr: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L22)

### Const isFloatStr

isFloatStr: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L23)

### Const normalizeDateChunkRgxp

normalizeDateChunkRgxp: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L18)

### Const normalizeZoneRgxp

normalizeZoneRgxp: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L19)

### Const timeChunkRgxp

timeChunkRgxp: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L14)

### Const zoneChunkRgxp

zoneChunkRgxp: RegExp = ...

* Defined in [src/core/prelude/date/const.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/prelude/date/const.ts#L15)