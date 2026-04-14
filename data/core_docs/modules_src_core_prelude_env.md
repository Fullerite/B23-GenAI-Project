# Module src/core/prelude/env
## Index

### References

* [GLOBAL](src_core_prelude_env.html#GLOBAL)
* [HAS\_WINDOW](src_core_prelude_env.html#HAS_WINDOW)
* [IS\_NODE](src_core_prelude_env.html#IS_NODE)
* [emitter](src_core_prelude_env.html#emitter)
* [event](src_core_prelude_env.html#event)

### Functions

* [get](src_core_prelude_env.html#get)
* [remove](src_core_prelude_env.html#remove)
* [set](src_core_prelude_env.html#set)

## References

### GLOBAL

Re-exports [GLOBAL](src_core_prelude_env_const.html#GLOBAL)

### HAS\_WINDOW

Re-exports [HAS\_WINDOW](src_core_prelude_env_const.html#HAS_WINDOW)

### IS\_NODE

Re-exports [IS\_NODE](src_core_prelude_env_const.html#IS_NODE)

### emitter

Re-exports [emitter](src_core_prelude_env_const.html#emitter)

### event

Re-exports [event](src_core_prelude_env_const.html#event)

## Functions

### get

* get(key: string): Promise<[CanUndef](index.html#CanUndef)<[Dictionary](../interfaces/index.Dictionary.html)>>

* + Defined in [src/core/prelude/env/index.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/index.ts#L31)

  Returns settings from the application environment by the specified key

  #### Parameters

  + ##### key: string

  #### Returns Promise<[CanUndef](index.html#CanUndef)<[Dictionary](../interfaces/index.Dictionary.html)>>

### remove

* remove(key: string): void

* + Defined in [src/core/prelude/env/index.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/index.ts#L60)

  Removes settings from the application environment by the specified key

  #### Parameters

  + ##### key: string

  #### Returns void

### set

* set(key: string, value: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): void

* + Defined in [src/core/prelude/env/index.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/prelude/env/index.ts#L45)

  Added settings to the application environment by the specified key

  #### Parameters

  + ##### key: string
  + ##### value: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

  #### Returns void