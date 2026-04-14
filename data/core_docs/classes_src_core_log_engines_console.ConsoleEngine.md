# Class ConsoleEngine
### Hierarchy

* ConsoleEngine

### Implements

* [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html)

## Index

### Constructors

* [constructor](src_core_log_engines_console.ConsoleEngine.html#constructor)

### Properties

* [stringifiedStylesCache](src_core_log_engines_console.ConsoleEngine.html#stringifiedStylesCache)
* [stylesCache](src_core_log_engines_console.ConsoleEngine.html#stylesCache)

### Methods

* [getStringifiedStyle](src_core_log_engines_console.ConsoleEngine.html#getStringifiedStyle)
* [log](src_core_log_engines_console.ConsoleEngine.html#log)

## Constructors

### constructor

* new ConsoleEngine(styles?: [LogStylesConfig](../modules/src_core_log_config_interface.html#LogStylesConfig)): [ConsoleEngine](src_core_log_engines_console.ConsoleEngine.html)

* + Defined in [src/core/log/engines/console.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/console.ts#L21)

  #### Parameters

  + ##### Optional styles: [LogStylesConfig](../modules/src_core_log_config_interface.html#LogStylesConfig)

  #### Returns [ConsoleEngine](src_core_log_engines_console.ConsoleEngine.html)

## Properties

### Protected stringifiedStylesCache

stringifiedStylesCache: [Dictionary](../interfaces/index.Dictionary.html)<string> = ...

* Defined in [src/core/log/engines/console.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/console.ts#L19)

### Protected Optional stylesCache

stylesCache?: [StylesCache](../interfaces/src_core_log_config_interface.StylesCache.html)

* Defined in [src/core/log/engines/console.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/console.ts#L18)

## Methods

### Protected getStringifiedStyle

* getStringifiedStyle(logLevel: [LogLevel](../modules/src_core_log_interface.html#LogLevel)): string

* + Defined in [src/core/log/engines/console.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/console.ts#L59)

  Returns a string representing of a style for the specified log level

  #### Parameters

  + ##### logLevel: [LogLevel](../modules/src_core_log_interface.html#LogLevel)

    level of logging that needs a style

  #### Returns string

### log

* log(event: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)): void

* Implementation of [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html).[log](../interfaces/src_core_log_engines_interface.LogEngine.html#log)

  + Defined in [src/core/log/engines/console.ts:31](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/console.ts#L31)

  Prints the specified event to a console

  #### Parameters

  + ##### event: [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)

    log event to print

  #### Returns void