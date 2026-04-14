# Interface Logger
### Hierarchy

* Logger
  + [ExtendedLogger](src_core_log_interface.ExtendedLogger.html)

### Callable

* Logger(context: string | [LogMessageOptions](src_core_log_interface.LogMessageOptions.html), ...details: unknown[]): void
* Logger(context: string | [LogMessageOptions](src_core_log_interface.LogMessageOptions.html), error: Error, ...details: unknown[]): void

* + Defined in [src/core/log/interface.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L17)

  #### Parameters

  + ##### context: string | [LogMessageOptions](src_core_log_interface.LogMessageOptions.html)
  + ##### Rest ...details: unknown[]

  #### Returns void
* + Defined in [src/core/log/interface.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L18)

  #### Parameters

  + ##### context: string | [LogMessageOptions](src_core_log_interface.LogMessageOptions.html)
  + ##### error: Error
  + ##### Rest ...details: unknown[]

  #### Returns void