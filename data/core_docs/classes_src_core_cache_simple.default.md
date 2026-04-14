# Class default<V, K>
Implementation for a simple in-memory cache data structure

### Type parameters

* #### V = unknown

  value type
* #### K = string

  key type (`string` by default)

### Hierarchy

* default
  + [default](src_core_cache_restricted.default.html)

### Implements

* [default](../interfaces/src_core_cache_interface.default.html)<V, K>

## Index

### Constructors

* [constructor](src_core_cache_simple.default.html#constructor)

### Properties

* [storage](src_core_cache_simple.default.html#storage)

### Accessors

* [size](src_core_cache_simple.default.html#size)

### Methods

* [[iterator]](src_core_cache_simple.default.html#_iterator_)
* [clear](src_core_cache_simple.default.html#clear)
* [entries](src_core_cache_simple.default.html#entries)
* [get](src_core_cache_simple.default.html#get)
* [has](src_core_cache_simple.default.html#has)
* [keys](src_core_cache_simple.default.html#keys)
* [remove](src_core_cache_simple.default.html#remove)
* [set](src_core_cache_simple.default.html#set)
* [values](src_core_cache_simple.default.html#values)

## Constructors

### constructor

* new default<V, K>(): [default](src_core_cache_simple.default.html)<V, K>

* #### Type parameters

  + #### V = unknown
  + #### K = string

  #### Returns [default](src_core_cache_simple.default.html)<V, K>

## Properties

### Protected Readonly storage

storage: Map<K, V> = ...

* Defined in [src/core/cache/simple/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L34)

Cache object

## Accessors

### size

* get size(): number

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[size](../interfaces/src_core_cache_interface.default.html#size)

  + Defined in [src/core/cache/simple/index.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L27)

  see
  :   [[Cache.size]]

  #### Returns number

## Methods

### [iterator]

* [iterator](): IterableIterator<K>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[[iterator]](../interfaces/src_core_cache_interface.default.html#_iterator_)

  + Defined in [src/core/cache/simple/index.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L36)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### clear

* clear(filter?: [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)<V, K>): Map<K, V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[clear](../interfaces/src_core_cache_interface.default.html#clear)

  + Defined in [src/core/cache/simple/index.ts:81](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L81)

  see
  :   [[Cache.clear]]

  #### Parameters

  + ##### Optional filter: [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)<V, K>

  #### Returns Map<K, V>

### entries

* entries(): IterableIterator<[K, V]>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[entries](../interfaces/src_core_cache_interface.default.html#entries)

  + Defined in [src/core/cache/simple/index.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L76)

  see
  :   [[Cache.entries]]

  #### Returns IterableIterator<[K, V]>

### get

* get(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[get](../interfaces/src_core_cache_interface.default.html#get)

  + Defined in [src/core/cache/simple/index.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L46)

  see
  :   [[Cache.get]]

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### has

* has(key: K): boolean

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[has](../interfaces/src_core_cache_interface.default.html#has)

  + Defined in [src/core/cache/simple/index.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L41)

  see
  :   [[Cache.has]]

  #### Parameters

  + ##### key: K

  #### Returns boolean

### keys

* keys(): IterableIterator<K>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[keys](../interfaces/src_core_cache_interface.default.html#keys)

  + Defined in [src/core/cache/simple/index.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L66)

  see
  :   [[Cache.keys]]

  #### Returns IterableIterator<K>

### remove

* remove(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[remove](../interfaces/src_core_cache_interface.default.html#remove)

  + Defined in [src/core/cache/simple/index.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L57)

  see
  :   [[Cache.remove]]

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### set

* set(key: K, value: V): V

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[set](../interfaces/src_core_cache_interface.default.html#set)

  + Defined in [src/core/cache/simple/index.ts:51](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L51)

  see
  :   [[Cache.set]]

  #### Parameters

  + ##### key: K
  + ##### value: V

  #### Returns V

### values

* values(): IterableIterator<V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[values](../interfaces/src_core_cache_interface.default.html#values)

  + Defined in [src/core/cache/simple/index.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L71)

  see
  :   [[Cache.values]]

  #### Returns IterableIterator<V>