# Interface FastCloneOptions
### Hierarchy

* FastCloneOptions

## Index

### Properties

* [freezable](index.FastCloneOptions.html#freezable)
* [replacer](index.FastCloneOptions.html#replacer)
* [reviver](index.FastCloneOptions.html#reviver)

## Properties

### Optional freezable

freezable?: boolean

* Defined in [index.d.ts:328](https://github.com/V4Fire/Core/blob/master/index.d.ts#L328)

If false the object freeze/seal state won't be copy

default
:   `true`

### Optional replacer

replacer?: [JSONCb](index.JSONCb.html)

* Defined in [index.d.ts:316](https://github.com/V4Fire/Core/blob/master/index.d.ts#L316)

Replacer function for `JSON.stringify`

see
:   [[JSON.stringify]]

### Optional reviver

reviver?: [JSONCb](index.JSONCb.html)

* Defined in [index.d.ts:322](https://github.com/V4Fire/Core/blob/master/index.d.ts#L322)

Reviver function for `JSON.parse`

see
:   [[JSON.parse]]