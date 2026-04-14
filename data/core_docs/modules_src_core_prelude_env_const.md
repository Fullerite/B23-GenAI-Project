# Module src/core/prelude/env/const
## Index

### Variables

* [GLOBAL](src_core_prelude_env_const.html#GLOBAL)
* [HAS\_WINDOW](src_core_prelude_env_const.html#HAS_WINDOW)
* [IS\_NODE](src_core_prelude_env_const.html#IS_NODE)
* [emitter](src_core_prelude_env_const.html#emitter)
* [event](src_core_prelude_env_const.html#event)

## Variables

### Const GLOBAL

GLOBAL: any = ...

* Defined in [src/core/prelude/env/const.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/const.ts#L30)

Link to the global object

### Const HAS\_WINDOW

HAS\_WINDOW: boolean = ...

* Defined in [src/core/prelude/env/const.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/const.ts#L40)

True if the current runtime has window object

### Const IS\_NODE

IS\_NODE: boolean = ...

* Defined in [src/core/prelude/env/const.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/const.ts#L45)

True if the current runtime is looks like Node.js

### Const emitter

emitter: EventEmitter2 = ...

* Defined in [src/core/prelude/env/const.ts:16](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/const.ts#L16)

Event emitter to broadcast environment events

### Const event

event: EventEmitter2 = emitter

* Defined in [src/core/prelude/env/const.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/const.ts#L23)

deprecated

see
:   [emitter](src_core_prelude_env_const.html#emitter)