# Module src/core/prelude/i18n/const
## Index

### Variables

* [emitter](src_core_prelude_i18n_const.html#emitter)
* [event](src_core_prelude_i18n_const.html#event)
* [locale](src_core_prelude_i18n_const.html#locale)
* [pluralizeMap](src_core_prelude_i18n_const.html#pluralizeMap)

## Variables

### Const emitter

emitter: EventEmitter2 = ...

* Defined in [src/core/prelude/i18n/const.ts:16](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/const.ts#L16)

The event emitter to broadcast localization events

### Const event

event: EventEmitter2 = emitter

* Defined in [src/core/prelude/i18n/const.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/const.ts#L23)

deprecated

see
:   [emitter](src_core_prelude_i18n_const.html#emitter)

### Const locale

locale: [Locale](../interfaces/src_core_prelude_i18n_interface.Locale.html) = ...

* Defined in [src/core/prelude/i18n/const.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/const.ts#L28)

The default application language

### Const pluralizeMap

pluralizeMap: Pick<{ many: number; none: number; one: number; some: number }, "none" | "one" | "some" | "many"> = ...

* Defined in [src/core/prelude/i18n/const.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/const.ts#L36)

A dictionary to map literal pluralization forms to numbers