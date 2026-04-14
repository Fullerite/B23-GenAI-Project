# Module src/core/functools/deprecation
[# core/functools/deprecation](#corefunctoolsdeprecation)

This module provides a bunch of functions and decorators to mark deprecated functions with the special flag.

```
import { deprecate, deprecated } from 'core/functools/deprecation';  
  
const foo = deprecate({  
  name: 'foo',  
  renamedTo: 'bar'  
}, bar);  
  
function bar() {  
  
}  
  
class Baz {  
  @deprecated({alternative: 'newMethod'})  
  oldMethod() {  
  
  }  
  
  newMethod() {}  
}
```

## Index

### References

* [InlineWarnOptions](src_core_functools_deprecation.html#InlineWarnOptions)
* [WarnAlternative](src_core_functools_deprecation.html#WarnAlternative)
* [WarnAlternativeOptions](src_core_functools_deprecation.html#WarnAlternativeOptions)
* [WarnContext](src_core_functools_deprecation.html#WarnContext)
* [WarnExprType](src_core_functools_deprecation.html#WarnExprType)
* [WarnOptions](src_core_functools_deprecation.html#WarnOptions)
* [WarnedFn](src_core_functools_deprecation.html#WarnedFn)

### Functions

* [deprecate](src_core_functools_deprecation.html#deprecate)
* [deprecated](src_core_functools_deprecation.html#deprecated)

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

### deprecate

* deprecate<T>(opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html), fn: T): T extends (...args: infer  A) => infer  R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T
* deprecate(opts: [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)): void
* deprecate<T>(fn: T): T extends (...args: infer  A) => infer  R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T

* + Defined in [src/core/functools/deprecation/index.ts:24](https://github.com/V4Fire/Core/blob/master/src/core/functools/deprecation/index.ts#L24)

  Marks the specified function as obsolescence

  #### Type parameters

  + #### T: Function

  #### Parameters

  + ##### opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

    additional options
  + ##### fn: T

    function to wrap

  #### Returns T extends (...args: infer A) => infer R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T
* + Defined in [src/core/functools/deprecation/index.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/functools/deprecation/index.ts#L33)

  Emits an obsolescence warning with the specified parameters

  #### Parameters

  + ##### opts: [InlineWarnOptions](../interfaces/src_core_functools_warning_interface.InlineWarnOptions.html)

    additional options

  #### Returns void
* + Defined in [src/core/functools/deprecation/index.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/functools/deprecation/index.ts#L39)

  Marks the specified function as obsolescence

  #### Type parameters

  + #### T: Function

  #### Parameters

  + ##### fn: T

    function to wrap

  #### Returns T extends (...args: infer A) => infer R ? [WarnedFn](../interfaces/src_core_functools_warning_interface.WarnedFn.html)<A, R> : T

### deprecated

* deprecated(target: object, key: string | symbol, descriptor: PropertyDescriptor): void
* deprecated(opts?: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)): Function

* + Defined in [src/core/functools/deprecation/index.ts:67](https://github.com/V4Fire/Core/blob/master/src/core/functools/deprecation/index.ts#L67)

  Decorator for `deprecate`

  decorator

  see
  :   [deprecate](src_core_functools_deprecation.html#deprecate)

  #### Parameters

  + ##### target: object
  + ##### key: string | symbol
  + ##### descriptor: PropertyDescriptor

  #### Returns void
* + Defined in [src/core/functools/deprecation/index.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/functools/deprecation/index.ts#L76)

  Decorator for `deprecate`.
  This overload adds a feature to provide additional options.

  see
  :   [deprecate](src_core_functools_deprecation.html#deprecate)

  #### Parameters

  + ##### Optional opts: [WarnOptions](../interfaces/src_core_functools_warning_interface.WarnOptions.html)

  #### Returns Function