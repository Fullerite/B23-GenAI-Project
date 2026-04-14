# Module src/core/functools/implementation
[# core/functools/implementation](#corefunctoolsimplementation)

This module provides a bunch of functions and decorators to mark unimplemented functions with the special flag.

```
import { unimplement, unimplemented } from 'core/functools/implementation';  
  
const foo = unimplement({name: 'foo', alternative: 'bar'}, () => {  
  
});  
  
function bar() {  
  
}  
  
class Baz {  
  @unimplemented({alternative: 'newMethod'})  
  oldMethod() {  
  
  }  
  
  newMethod() {}  
}
```

## Index

### References

* [InlineWarnOptions](src_core_functools_implementation.html#InlineWarnOptions)
* [WarnAlternative](src_core_functools_implementation.html#WarnAlternative)
* [WarnAlternativeOptions](src_core_functools_implementation.html#WarnAlternativeOptions)
* [WarnContext](src_core_functools_implementation.html#WarnContext)
* [WarnExprType](src_core_functools_implementation.html#WarnExprType)
* [WarnOptions](src_core_functools_implementation.html#WarnOptions)
* [WarnedFn](src_core_functools_implementation.html#WarnedFn)

### Functions

* [unimplement](src_core_functools_implementation.html#unimplement)
* [unimplemented](src_core_functools_implementation.html#unimplemented)

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

### unimplement

* unimplement<T>(opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html), fn: T): T extends (...args: infer  A) => any ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, void> : T
* unimplement(opts: [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)): void
* unimplement<T>(fn: T): T extends (...args: infer  A) => any ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, void> : T

* + Defined in [src/core/functools/implementation/index.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/functools/implementation/index.ts#L24)

  Marks the specified function as unimplemented

  #### Type parameters

  + #### T: Function

  #### Parameters

  + ##### opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

    additional options
  + ##### fn: T

    function to wrap

  #### Returns T extends (...args: infer A) => any ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, void> : T
* + Defined in [src/core/functools/implementation/index.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/functools/implementation/index.ts#L33)

  Emits an "unimplemented" warning with the specified parameters

  #### Parameters

  + ##### opts: [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)

    additional options

  #### Returns void
* + Defined in [src/core/functools/implementation/index.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/functools/implementation/index.ts#L39)

  Marks the specified function as unimplemented

  #### Type parameters

  + #### T: Function

  #### Parameters

  + ##### fn: T

    function to wrap

  #### Returns T extends (...args: infer A) => any ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, void> : T

### unimplemented

* unimplemented(target: object, key: string | symbol, descriptor: PropertyDescriptor): void
* unimplemented(opts?: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)): Function

* + Defined in [src/core/functools/implementation/index.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/functools/implementation/index.ts#L77)

  Decorator for `unimplement`

  decorator

  see
  :   [unimplement](src_core_functools_implementation.html#unimplement)

  example
  :   ```
      class Foo {  
        @unimplemented()  
        bar() {  
        
        }  
      }
      ```

  #### Parameters

  + ##### target: object
  + ##### key: string | symbol
  + ##### descriptor: PropertyDescriptor

  #### Returns void
* + Defined in [src/core/functools/implementation/index.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/functools/implementation/index.ts#L96)

  Decorator for `unimplement`.
  This overload adds a feature to provide additional options.

  see
  :   [unimplement](src_core_functools_implementation.html#unimplement)

  example
  :   ```
      class Foo {  
        @unimplemented({alternative: 'baz'}})  
        bar() {  
        
        }  
      }
      ```

  #### Parameters

  + ##### Optional opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

  #### Returns Function