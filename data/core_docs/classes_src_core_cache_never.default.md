# Class default<V, K>
Loopback class for a cache data structure

### Type parameters

* #### V = any
* #### K = any

### Hierarchy

* default

### Implements

* [default](../interfaces/src_core_cache_interface.default.html)<V, K>

## Index

### Constructors

* [constructor](src_core_cache_never.default.html#constructor)

### Properties

* [storage](src_core_cache_never.default.html#storage)

### Accessors

* [size](src_core_cache_never.default.html#size)

### Methods

* [[iterator]](src_core_cache_never.default.html#_iterator_)
* [clear](src_core_cache_never.default.html#clear)
* [entries](src_core_cache_never.default.html#entries)
* [get](src_core_cache_never.default.html#get)
* [has](src_core_cache_never.default.html#has)
* [keys](src_core_cache_never.default.html#keys)
* [remove](src_core_cache_never.default.html#remove)
* [set](src_core_cache_never.default.html#set)
* [values](src_core_cache_never.default.html#values)

## Constructors

### constructor

* new default<V, K>(): [default](src_core_cache_never.default.html)<V, K>

* #### Type parameters

  + #### V = any
  + #### K = any

  #### Returns [default](src_core_cache_never.default.html)<V, K>

## Properties

### Protected Readonly storage

storage: Map<K, V> = ...

* Defined in [src/core/cache/never/index.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L33)

Cache object

## Accessors

### size

* get size(): number

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[size](../interfaces/src_core_cache_interface.default.html#size)

  + Defined in [src/core/cache/never/index.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L26)

  see
  :   [[Cache.size]]

  #### Returns number

## Methods

### [iterator]

* [iterator](): IterableIterator<K>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[[iterator]](../interfaces/src_core_cache_interface.default.html#_iterator_)

  + Defined in [src/core/cache/never/index.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L35)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### clear

* clear(filter?: [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)<V, K>): Map<K, V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[clear](../interfaces/src_core_cache_interface.default.html#clear)

  + Defined in [src/core/cache/never/index.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L75)

  see
  :   [[Cache.clear]]

  #### Parameters

  + ##### Optional filter: [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)<V, K>

  #### Returns Map<K, V>

### entries

* entries(): IterableIterator<[K, V]>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[entries](../interfaces/src_core_cache_interface.default.html#entries)

  + Defined in [src/core/cache/never/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L70)

  see
  :   [[Cache.entries]]

  #### Returns IterableIterator<[K, V]>

### get

* get(key: K): undefined

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[get](../interfaces/src_core_cache_interface.default.html#get)

  + Defined in [src/core/cache/never/index.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L45)

  see
  :   [[Cache.get]]

  #### Parameters

  + ##### key: K

  #### Returns undefined

### has

* has(key: K): boolean

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[has](../interfaces/src_core_cache_interface.default.html#has)

  + Defined in [src/core/cache/never/index.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L40)

  see
  :   [[Cache.has]]

  #### Parameters

  + ##### key: K

  #### Returns boolean

### keys

* keys(): IterableIterator<K>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[keys](../interfaces/src_core_cache_interface.default.html#keys)

  + Defined in [src/core/cache/never/index.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L60)

  see
  :   [[Cache.keys]]

  #### Returns IterableIterator<K>

### remove

* remove(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[remove](../interfaces/src_core_cache_interface.default.html#remove)

  + Defined in [src/core/cache/never/index.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L55)

  see
  :   [[Cache.remove]]

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### set

* set(key: K, value: V): V

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[set](../interfaces/src_core_cache_interface.default.html#set)

  + Defined in [src/core/cache/never/index.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L50)

  see
  :   [[Cache.set]]

  #### Parameters

  + ##### key: K
  + ##### value: V

  #### Returns V

### values

* values(): IterableIterator<V>

* Implementation of [default](../interfaces/src_core_cache_interface.default.html).[values](../interfaces/src_core_cache_interface.default.html#values)

  + Defined in [src/core/cache/never/index.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/cache/never/index.ts#L65)

  see
  :   [[Cache.values]]

  #### Returns IterableIterator<V>