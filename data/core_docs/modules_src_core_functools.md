# Module src/core/functools
[# core/functools](#corefunctools)

This module provides a bunch of functions and decorators to wrap another functions with adding some extra functionality.
Also, see submodules of this module:

* [`core/functools/deprecation`](src_core_functools_deprecation.html);
* [`core/functools/implementation`](src_core_functools_implementation.html);
* [`core/functools/warning`](src_core_functools_warning.html);
* [`core/functools/trait`](src_core_functools_trait.html).

[## once](#once)

Decorator for `Function.prototype.once`.
Returns a new function that allows to invoke the specified function only once.

```
import { once, debounce } from 'core/functools';  
  
class Foo {  
  @once  
  bar() {  
    return Math.random();  
  }  
}  
  
const foo = new Foo();  
console.log(foo.bar() === foo.bar());
```

[## debounce](#debounce)

Decorator for `Function.prototype.debounce`
Returns a new function that allows to invoke a function, which it takes, only with the specified delay.
The next invocation of the function will cancel the previous.

```
import { debounce } from 'core/functools';  
  
class Foo {  
  @debounce(500)  
  bla() {  
    console.log('Bang!');  
  }  
}
```

[## throttle](#throttle)

Decorator for `Function.prototype.throttle`.
Returns a new function that allows to invoke a function, which it takes, not more often than the specified delay.
The first invoking of a function will run immediately, but all rest invokes will be merged to one and
executes after the specified delay.

```
import { throttle } from 'core/functools';  
  
class Foo {  
  @throttle(500)  
  bla() {  
    console.log('Bang!');  
  }  
}
```

## Index

### References

* [InlineWarnOptions](src_core_functools.html#InlineWarnOptions)
* [WarnAlternative](src_core_functools.html#WarnAlternative)
* [WarnAlternativeOptions](src_core_functools.html#WarnAlternativeOptions)
* [WarnContext](src_core_functools.html#WarnContext)
* [WarnExprType](src_core_functools.html#WarnExprType)
* [WarnOptions](src_core_functools.html#WarnOptions)
* [WarnedFn](src_core_functools.html#WarnedFn)
* [constant](src_core_functools.html#constant)
* [debounce](src_core_functools.html#debounce)
* [deprecate](src_core_functools.html#deprecate)
* [deprecated](src_core_functools.html#deprecated)
* [identity](src_core_functools.html#identity)
* [once](src_core_functools.html#once)
* [throttle](src_core_functools.html#throttle)
* [unimplement](src_core_functools.html#unimplement)
* [unimplemented](src_core_functools.html#unimplemented)
* [warn](src_core_functools.html#warn)
* [warned](src_core_functools.html#warned)

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

### constant

Re-exports [constant](src_core_functools_helpers.html#constant)

### debounce

Re-exports [debounce](src_core_functools_lazy.html#debounce)

### deprecate

Re-exports [deprecate](src_core_functools_deprecation.html#deprecate)

### deprecated

Re-exports [deprecated](src_core_functools_deprecation.html#deprecated)

### identity

Re-exports [identity](src_core_functools_helpers.html#identity)

### once

Re-exports [once](src_core_functools_memoize.html#once)

### throttle

Re-exports [throttle](src_core_functools_lazy.html#throttle)

### unimplement

Re-exports [unimplement](src_core_functools_implementation.html#unimplement)

### unimplemented

Re-exports [unimplemented](src_core_functools_implementation.html#unimplemented)

### warn

Re-exports [warn](src_core_functools_warning.html#warn)

### warned

Re-exports [warned](src_core_functools_warning.html#warned)