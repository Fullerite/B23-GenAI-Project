# Interface WarnOptions
### Hierarchy

* WarnOptions
  + [InlineWarnOptions](src_core_functools_warning_interface.InlineWarnOptions.html)

## Index

### Properties

* [alternative](src_core_functools_warning_interface.WarnOptions.html#alternative)
* [context](src_core_functools_warning_interface.WarnOptions.html#context)
* [movedTo](src_core_functools_warning_interface.WarnOptions.html#movedTo)
* [name](src_core_functools_warning_interface.WarnOptions.html#name)
* [notice](src_core_functools_warning_interface.WarnOptions.html#notice)
* [renamedTo](src_core_functools_warning_interface.WarnOptions.html#renamedTo)
* [type](src_core_functools_warning_interface.WarnOptions.html#type)

## Properties

### Optional alternative

alternative?: [WarnAlternative](../modules/src_core_functools_warning_interface.html#WarnAlternative)

* Defined in [src/core/functools/warning/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L63)

Name of a function/method/etc. that need to use instead of the current
or an object with additional options of the alternative

### Optional context

context?: [WarnContext](../modules/src_core_functools_warning_interface.html#WarnContext)

* Defined in [src/core/functools/warning/interface.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L47)

Type of warn context

### Optional movedTo

movedTo?: string

* Defined in [src/core/functools/warning/interface.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L75)

Indicates that a function/method/etc. was moved to a different file, but its interface still actual,
the value contains a source path after moving

### Optional name

name?: string

* Defined in [src/core/functools/warning/interface.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L52)

Name of an expression to wrap

### Optional notice

notice?: string

* Defined in [src/core/functools/warning/interface.ts:80](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L80)

Additional information

### Optional renamedTo

renamedTo?: string

* Defined in [src/core/functools/warning/interface.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L69)

Indicates that a function/method/etc. was renamed, but its interface still actual,
the value contains a name after renaming

### Optional type

type?: [WarnExprType](../modules/src_core_functools_warning_interface.html#WarnExprType)

* Defined in [src/core/functools/warning/interface.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L57)

Type of expression to wrap