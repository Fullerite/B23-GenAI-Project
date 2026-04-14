# Interface ExtendedLogger
### Hierarchy

* [Logger](src_core_log_interface.Logger.html)
  + ExtendedLogger

### Callable

* ExtendedLogger(context: string | [LogMessageOptions](src_core_log_interface.LogMessageOptions.html), ...details: unknown[]): void
* ExtendedLogger(context: string | [LogMessageOptions](src_core_log_interface.LogMessageOptions.html), error: Error, ...details: unknown[]): void

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

## Index

### Methods

* [error](src_core_log_interface.ExtendedLogger.html#error)
* [info](src_core_log_interface.ExtendedLogger.html#info)
* [namespace](src_core_log_interface.ExtendedLogger.html#namespace)
* [warn](src_core_log_interface.ExtendedLogger.html#warn)

## Methods

### error

* error(context: string, ...details: unknown[]): void
* error(context: string, error: Error, ...details: unknown[]): void

* + Defined in [src/core/log/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L53)

  Logs a message with the error level and specified context

  #### Parameters

  + ##### context: string

    log record context
  + ##### Rest ...details: unknown[]

  #### Returns void
* + Defined in [src/core/log/interface.ts:62](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L62)

  Logs a message with the error level and specified context

  #### Parameters

  + ##### context: string

    log record context
  + ##### error: Error

    thrown error
  + ##### Rest ...details: unknown[]

  #### Returns void

### info

* info(context: string, ...details: unknown[]): void

* + Defined in [src/core/log/interface.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L28)

  Logs a message with the info level and specified context

  #### Parameters

  + ##### context: string

    log record context
  + ##### Rest ...details: unknown[]

  #### Returns void

### namespace

* namespace(value: string): [ExtendedLogger](src_core_log_interface.ExtendedLogger.html)

* + Defined in [src/core/log/interface.ts:80](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L80)

  Returns a new logging function with the specified namespace

  example
  :   ```
      const log2 = log.namespace('global');  
      log2.info('res', 'hello');  
      // Prints context 'global:res'  
        
      const log3 = log.namespace('super').namespace('global');  
      log3.info('res', 'hello');  
      // Prints context 'super:global:res'
      ```

  #### Parameters

  + ##### value: string

  #### Returns [ExtendedLogger](src_core_log_interface.ExtendedLogger.html)

### warn

* warn(context: string, ...details: unknown[]): void
* warn(context: string, error: Error, ...details: unknown[]): void

* + Defined in [src/core/log/interface.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L36)

  Logs a message with the warning level and specified context

  #### Parameters

  + ##### context: string

    log record context
  + ##### Rest ...details: unknown[]

  #### Returns void
* + Defined in [src/core/log/interface.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/log/interface.ts#L45)

  Logs a message with the warning level and specified context

  #### Parameters

  + ##### context: string

    log record context
  + ##### error: Error

    thrown error
  + ##### Rest ...details: unknown[]

  #### Returns void