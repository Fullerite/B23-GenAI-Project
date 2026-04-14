# Module src/config
[# config](#config)

This module provides options to configure the application.

## Index

### References

* [Config](src_config.html#Config)

### Variables

* [$$](src_config.html#__)
* [default](src_config.html#default)

### Functions

* [extend](src_config.html#extend)

## References

### Config

Re-exports [Config](../interfaces/src_config_interface.Config.html)

## Variables

### Const $$

$$: [StrictDictionary](../interfaces/index.StrictDictionary.html)<symbol> = ...

* Defined in [src/config/index.ts:22](https://github.com/V4Fire/Core/blob/master/src/config/index.ts#L22)

### Const default

default: [Config](../interfaces/src_config_interface.Config.html) = ...

* Defined in [src/config/index.ts:24](https://github.com/V4Fire/Core/blob/master/src/config/index.ts#L24)

## Functions

### extend

* extend<T>(...objects: [CanUndef](index.html#CanUndef)<[Dictionary](../interfaces/index.Dictionary.html)<unknown>>[]): T

* + Defined in [src/config/index.ts:113](https://github.com/V4Fire/Core/blob/master/src/config/index.ts#L113)

  Extends the config object with additional objects

  #### Type parameters

  + #### T: [Config](../interfaces/src_config_interface.Config.html)

  #### Parameters

  + ##### Rest ...objects: [CanUndef](index.html#CanUndef)<[Dictionary](../interfaces/index.Dictionary.html)<unknown>>[]

  #### Returns T