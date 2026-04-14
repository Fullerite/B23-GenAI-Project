# Module src/core/functools/warning
[# core/functools/warning](#corefunctoolswarning)

This module provides a bunch of functions and decorators to mark functions with different warnings.

```
import { warn, warned } from 'core/functools/warning';  
  
const foo = warn({context: 'unimplemented', name: 'foo', alternative: 'bar'}, () => {  
  
});  
  
function bar() {  
  
}  
  
class Baz {  
  @warned({context: 'deprecated', alternative: 'newMethod'})  
  oldMethod() {  
  
  }  
  
  newMethod() {}  
}
```

## Index

### References

* [InlineWarnOptions](src_core_functools_warning.html#InlineWarnOptions)
* [WarnAlternative](src_core_functools_warning.html#WarnAlternative)
* [WarnAlternativeOptions](src_core_functools_warning.html#WarnAlternativeOptions)
* [WarnContext](src_core_functools_warning.html#WarnContext)
* [WarnExprType](src_core_functools_warning.html#WarnExprType)
* [WarnOptions](src_core_functools_warning.html#WarnOptions)
* [WarnedFn](src_core_functools_warning.html#WarnedFn)

### Functions

* [warn](src_core_functools_warning.html#warn)
* [warned](src_core_functools_warning.html#warned)

## References

### InlineWarnOptions

Re-exports [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)

### WarnAlternative

Re-exports [WarnAlternative](src_core_functools_warning_interface.html#WarnAlternative)

### WarnAlternativeOptions

Re-exports [WarnAlternativeOptions](../interfaces/src_core_functools_warning_interface.WarnAlternativeOptions.html)

### WarnContext

Re-exports [WarnContext](src_core_functools_warning_interface.html#WarnContext)

### WarnExprType

Re-exports [WarnExprType](src_core_functools_warning_interface.html#WarnExprType)

### WarnOptions

Re-exports [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

### WarnedFn

Re-exports [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)

## Functions

### warn

* warn<T>(opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html), fn: T): T extends (...args: infer  A) => infer  R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T
* warn(opts: [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)): void
* warn<T>(fn: T): T extends (...args: infer  A) => infer  R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T

* + Defined in [src/core/functools/warning/index.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/index.ts#L25)

  Marks a function with the specified warning

  #### Type parameters

  + #### T: Function

  #### Parameters

  + ##### opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

    additional options
  + ##### fn: T

    function to wrap

  #### Returns T extends (...args: infer A) => infer R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T
* + Defined in [src/core/functools/warning/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/index.ts#L34)

  Emits a warning with the specified parameters

  #### Parameters

  + ##### opts: [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)

    additional options

  #### Returns void
* + Defined in [src/core/functools/warning/index.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/index.ts#L40)

  Marks a function as non-recommended to use

  #### Type parameters

  + #### T: Function

  #### Parameters

  + ##### fn: T

    function to wrap

  #### Returns T extends (...args: infer A) => infer R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T

### warned

* warned(target: object, key: string | symbol, descriptor: PropertyDescriptor): void
* warned(opts?: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)): Function

* + Defined in [src/core/functools/warning/index.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/index.ts#L169)

  Decorator for `warn`

  decorator

  see
  :   [warn](src_core_functools_warning.html#warn)

  example
  :   ```
      class Foo {  
        @warned()  
        bar() {  
        
        }  
      }
      ```

  #### Parameters

  + ##### target: object
  + ##### key: string | symbol
  + ##### descriptor: PropertyDescriptor

  #### Returns void
* + Defined in [src/core/functools/warning/index.ts:188](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/index.ts#L188)

  Decorator for `warn`.
  This overload adds a feature to provide additional options.

  see
  :   [warn](src_core_functools_warning.html#warn)

  example
  :   ```
      class Foo {  
        @warned({alternative: 'baz'}})  
        bar() {  
        
        }  
      }
      ```

  #### Parameters

  + ##### Optional opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

  #### Returns Function