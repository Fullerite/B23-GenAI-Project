# Interface InlineWarnOptions
### Hierarchy

* [WarnOptions](src_core_functools_warning_interface.WarnOptions.html)
  + InlineWarnOptions

## Index

### Properties

* [alternative](src_core_functools_warning_interface.InlineWarnOptions.html#alternative)
* [context](src_core_functools_warning_interface.InlineWarnOptions.html#context)
* [movedTo](src_core_functools_warning_interface.InlineWarnOptions.html#movedTo)
* [name](src_core_functools_warning_interface.InlineWarnOptions.html#name)
* [notice](src_core_functools_warning_interface.InlineWarnOptions.html#notice)
* [renamedTo](src_core_functools_warning_interface.InlineWarnOptions.html#renamedTo)
* [type](src_core_functools_warning_interface.InlineWarnOptions.html#type)

## Properties

### Optional alternative

alternative?: [WarnAlternative](../modules/src_core_functools_warning_interface.html#WarnAlternative)

Inherited from [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[alternative](src_core_functools_warning_interface.WarnOptions.html#alternative)

* Defined in [src/core/functools/warning/interface.ts:63](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L63)

Name of a function/method/etc. that need to use instead of the current
or an object with additional options of the alternative

### Optional context

context?: [WarnContext](../modules/src_core_functools_warning_interface.html#WarnContext)

Inherited from [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[context](src_core_functools_warning_interface.WarnOptions.html#context)

* Defined in [src/core/functools/warning/interface.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L47)

Type of warn context

### Optional movedTo

movedTo?: string

Inherited from [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[movedTo](src_core_functools_warning_interface.WarnOptions.html#movedTo)

* Defined in [src/core/functools/warning/interface.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L75)

Indicates that a function/method/etc. was moved to a different file, but its interface still actual,
the value contains a source path after moving

### name

name: string

Overrides [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[name](src_core_functools_warning_interface.WarnOptions.html#name)

* Defined in [src/core/functools/warning/interface.ts:85](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L85)

see
:   [WarnOptions.name](src_core_functools_warning_interface.WarnOptions.html#name)

### Optional notice

notice?: string

Inherited from [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[notice](src_core_functools_warning_interface.WarnOptions.html#notice)

* Defined in [src/core/functools/warning/interface.ts:80](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L80)

Additional information

### Optional renamedTo

renamedTo?: string

Inherited from [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[renamedTo](src_core_functools_warning_interface.WarnOptions.html#renamedTo)

* Defined in [src/core/functools/warning/interface.ts:69](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L69)

Indicates that a function/method/etc. was renamed, but its interface still actual,
the value contains a name after renaming

### type

type: [WarnExprType](../modules/src_core_functools_warning_interface.html#WarnExprType)

Overrides [WarnOptions](src_core_functools_warning_interface.WarnOptions.html).[type](src_core_functools_warning_interface.WarnOptions.html#type)

* Defined in [src/core/functools/warning/interface.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/functools/warning/interface.ts#L88)

see
:   [WarnOptions.type](src_core_functools_warning_interface.WarnOptions.html#type)