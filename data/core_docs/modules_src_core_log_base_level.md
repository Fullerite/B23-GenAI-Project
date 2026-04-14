# Module src/core/log/base/level
## Index

### Variables

* [DEFAULT\_LEVEL](src_core_log_base_level.html#DEFAULT_LEVEL)

### Functions

* [cmpLevels](src_core_log_base_level.html#cmpLevels)

## Variables

### Const DEFAULT\_LEVEL

DEFAULT\_LEVEL: [LogLevel](src_core_log_interface.html#LogLevel) = 'info'

* Defined in [src/core/log/base/level.ts:12](https://github.com/V4Fire/Core/blob/master/src/core/log/base/level.ts#L12)

## Functions

### cmpLevels

* cmpLevels(left: [LogLevel](src_core_log_interface.html#LogLevel), right: [LogLevel](src_core_log_interface.html#LogLevel)): number

* + Defined in [src/core/log/base/level.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/log/base/level.ts#L35)

  Compares log levels:

  < 0 if left < right

  > 0 if left > right
  > = 0 if left === right

  #### Parameters

  + ##### left: [LogLevel](src_core_log_interface.html#LogLevel)
  + ##### right: [LogLevel](src_core_log_interface.html#LogLevel)

  #### Returns number