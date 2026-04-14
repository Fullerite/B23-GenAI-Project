# Module src/core/log
[# core/log](#corelog)

This module provides API to log different system/application events.

```
import log from 'core/log';  
  
log.info('Info message');  
log.warn('Some warning');  
log.error('Some error', new Error('Boom!'));  
  
log.namespace('net').error('Some error with the context');
```

## Index

### References

* [ExtendedLogger](src_core_log.html#ExtendedLogger)
* [LogConfig](src_core_log.html#LogConfig)
* [LogLevel](src_core_log.html#LogLevel)
* [LogMessageOptions](src_core_log.html#LogMessageOptions)
* [LogPipelineConfig](src_core_log.html#LogPipelineConfig)
* [LogStylesConfig](src_core_log.html#LogStylesConfig)
* [Logger](src_core_log.html#Logger)
* [StylesCache](src_core_log.html#StylesCache)
* [createPipeline](src_core_log.html#createPipeline)
* [createStyleCache](src_core_log.html#createStyleCache)

### Variables

* [default](src_core_log.html#default)

## References

### ExtendedLogger

Re-exports [ExtendedLogger](../interfaces/src_core_log_interface.ExtendedLogger.html)

### LogConfig

Re-exports [LogConfig](../interfaces/src_core_log_config_interface.LogConfig.html)

### LogLevel

Re-exports [LogLevel](src_core_log_interface.html#LogLevel)

### LogMessageOptions

Re-exports [LogMessageOptions](../interfaces/src_core_log_interface.LogMessageOptions.html)

### LogPipelineConfig

Re-exports [LogPipelineConfig](../interfaces/src_core_log_config_interface.LogPipelineConfig.html)

### LogStylesConfig

Re-exports [LogStylesConfig](src_core_log_config_interface.html#LogStylesConfig)

### Logger

Re-exports [Logger](../interfaces/src_core_log_interface.Logger.html)

### StylesCache

Re-exports [StylesCache](../interfaces/src_core_log_config_interface.StylesCache.html)

### createPipeline

Re-exports [createPipeline](src_core_log_config_pipeline.html#createPipeline)

### createStyleCache

Re-exports [createStyleCache](src_core_log_config_styles.html#createStyleCache)

## Variables

### Const default

default: [ExtendedLogger](../interfaces/src_core_log_interface.ExtendedLogger.html) = ...

* Defined in [src/core/log/index.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/log/index.ts#L24)

API for logging

defaultexport