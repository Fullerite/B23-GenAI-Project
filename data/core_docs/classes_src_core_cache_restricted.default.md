# Class default<V, K>
Implementation for an in-memory data structure with support for limiting of values in the cache

### Type parameters

* #### V = unknown

  value type
* #### K = string

  key type (`string` by default)

### Hierarchy

* [default](src_core_cache_simple.default.html)<V, K>
  + default

## Index

### Constructors

* [constructor](src_core_cache_restricted.default.html#constructor)

### Properties

* [capacity](src_core_cache_restricted.default.html#capacity)
* [queue](src_core_cache_restricted.default.html#queue)
* [storage](src_core_cache_restricted.default.html#storage)

### Accessors

* [size](src_core_cache_restricted.default.html#size)

### Methods

* [[iterator]](src_core_cache_restricted.default.html#_iterator_)
* [clear](src_core_cache_restricted.default.html#clear)
* [entries](src_core_cache_restricted.default.html#entries)
* [get](src_core_cache_restricted.default.html#get)
* [has](src_core_cache_restricted.default.html#has)
* [keys](src_core_cache_restricted.default.html#keys)
* [remove](src_core_cache_restricted.default.html#remove)
* [set](src_core_cache_restricted.default.html#set)
* [setCapacity](src_core_cache_restricted.default.html#setCapacity)
* [values](src_core_cache_restricted.default.html#values)

## Constructors

### constructor

* new default<V, K>(max?: number): [default](src_core_cache_restricted.default.html)<V, K>

* Overrides [default](src_core_cache_simple.default.html).[constructor](src_core_cache_simple.default.html#constructor)

  + Defined in [src/core/cache/restricted/index.ts:39](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L39)

  override

  #### Type parameters

  + #### V = unknown
  + #### K = string

  #### Parameters

  + ##### Optional max: number

  #### Returns [default](src_core_cache_restricted.default.html)<V, K>

## Properties

### Protected capacity

capacity: number = 20

* Defined in [src/core/cache/restricted/index.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L33)

Number of maximum records in the cache

### Protected Readonly queue

queue: Set<K> = ...

* Defined in [src/core/cache/restricted/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L28)

Queue object

### Protected Readonly storage

storage: Map<K, V> = ...

Inherited from [default](src_core_cache_simple.default.html).[storage](src_core_cache_simple.default.html#storage)

* Defined in [src/core/cache/simple/index.ts:34](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L34)

Cache object

## Accessors

### size

* get size(): number

* Inherited from SimpleCache.size

  + Defined in [src/core/cache/simple/index.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L27)

  see
  :   [[Cache.size]]

  #### Returns number

## Methods

### [iterator]

* [iterator](): IterableIterator<K>

* Inherited from [default](src_core_cache_simple.default.html).[[iterator]](src_core_cache_simple.default.html#_iterator_)

  + Defined in [src/core/cache/simple/index.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L36)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### clear

* clear(filter?: [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)<V, K>): Map<K, V>

* Overrides [default](src_core_cache_simple.default.html).[clear](src_core_cache_simple.default.html#clear)

  + Defined in [src/core/cache/restricted/index.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L79)

  #### Parameters

  + ##### Optional filter: [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)<V, K>

  #### Returns Map<K, V>

### entries

* entries(): IterableIterator<[K, V]>

* Inherited from [default](src_core_cache_simple.default.html).[entries](src_core_cache_simple.default.html#entries)

  + Defined in [src/core/cache/simple/index.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L76)

  see
  :   [[Cache.entries]]

  #### Returns IterableIterator<[K, V]>

### get

* get(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Overrides [default](src_core_cache_simple.default.html).[get](src_core_cache_simple.default.html#get)

  + Defined in [src/core/cache/restricted/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L47)

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### has

* has(key: K): boolean

* Inherited from [default](src_core_cache_simple.default.html).[has](src_core_cache_simple.default.html#has)

  + Defined in [src/core/cache/simple/index.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L41)

  see
  :   [[Cache.has]]

  #### Parameters

  + ##### key: K

  #### Returns boolean

### keys

* keys(): IterableIterator<K>

* Inherited from [default](src_core_cache_simple.default.html).[keys](src_core_cache_simple.default.html#keys)

  + Defined in [src/core/cache/simple/index.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L66)

  see
  :   [[Cache.keys]]

  #### Returns IterableIterator<K>

### remove

* remove(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Overrides [default](src_core_cache_simple.default.html).[remove](src_core_cache_simple.default.html#remove)

  + Defined in [src/core/cache/restricted/index.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L72)

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### set

* set(key: K, value: V): V

* Overrides [default](src_core_cache_simple.default.html).[set](src_core_cache_simple.default.html#set)

  + Defined in [src/core/cache/restricted/index.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L56)

  #### Parameters

  + ##### key: K
  + ##### value: V

  #### Returns V

### setCapacity

* setCapacity(value: number): Map<K, V>

* + Defined in [src/core/cache/restricted/index.ts:101](https://github.com/V4Fire/Core/blob/master/src/core/cache/restricted/index.ts#L101)

  Sets a new capacity of the cache.
  The method returns a map of truncated elements that the cache can't fit anymore.

  #### Parameters

  + ##### value: number

  #### Returns Map<K, V>

### values

* values(): IterableIterator<V>

* Inherited from [default](src_core_cache_simple.default.html).[values](src_core_cache_simple.default.html#values)

  + Defined in [src/core/cache/simple/index.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/cache/simple/index.ts#L71)

  see
  :   [[Cache.values]]

  #### Returns IterableIterator<V>