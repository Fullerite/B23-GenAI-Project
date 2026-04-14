# Module src/core/log/engines
## Index

### References

* [Extended](src_core_log_engines.html#Extended)
* [LogEngine](src_core_log_engines.html#LogEngine)
* [LogEngineConstructor](src_core_log_engines.html#LogEngineConstructor)
* [LogEngines](src_core_log_engines.html#LogEngines)
* [extend](src_core_log_engines.html#extend)

### Variables

* [default](src_core_log_engines.html#default)

### Functions

* [creatorFor](src_core_log_engines.html#creatorFor)

## References

### Extended

Re-exports [Extended](src_core_log_base_interface.html#Extended)

### LogEngine

Re-exports [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html)

### LogEngineConstructor

Re-exports [LogEngineConstructor](../interfaces/src_core_log_engines_interface.LogEngineConstructor.html)

### LogEngines

Re-exports [LogEngines](src_core_log_engines_interface.html#LogEngines)

### extend

Renames and re-exports [default](src_core_log_base_extend.html#default)

## Variables

### Const default

default: { console: (opts?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>) => [ConsoleEngine](../classes/src_core_log_engines_console.ConsoleEngine.html) } = ...

* Defined in [src/core/log/engines/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/index.ts#L23)

#### Type declaration

* ##### console: (opts?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>) => [ConsoleEngine](../classes/src_core_log_engines_console.ConsoleEngine.html)

  + - (opts?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): [ConsoleEngine](../classes/src_core_log_engines_console.ConsoleEngine.html)
    - Returns a function that creates an engine of the specified class

      #### Parameters

      * ##### Optional opts: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

      #### Returns [ConsoleEngine](../classes/src_core_log_engines_console.ConsoleEngine.html)

## Functions

### creatorFor

* creatorFor<T>(Ctor: [LogEngineConstructor](../interfaces/src_core_log_engines_interface.LogEngineConstructor.html)<T>): (opts?: [Dictionary](../interfaces/index.Dictionary.html)) => T

* + Defined in [src/core/log/engines/index.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/log/engines/index.ts#L19)

  Returns a function that creates an engine of the specified class

  #### Type parameters

  + #### T: [LogEngine](../interfaces/src_core_log_engines_interface.LogEngine.html)

  #### Parameters

  + ##### Ctor: [LogEngineConstructor](../interfaces/src_core_log_engines_interface.LogEngineConstructor.html)<T>

    constructor or just a class

  #### Returns (opts?: [Dictionary](../interfaces/index.Dictionary.html)) => T

  + - (opts?: [Dictionary](../interfaces/index.Dictionary.html)): T
    - Returns a function that creates an engine of the specified class

      #### Parameters

      * ##### Optional opts: [Dictionary](../interfaces/index.Dictionary.html)

      #### Returns T