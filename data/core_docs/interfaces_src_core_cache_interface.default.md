# Interface default<V, K>
Base interface for a cache data structure

### Type parameters

* #### V = unknown

  value type
* #### K = string

  key type (`string` by default)

### Hierarchy

* default
  + [CacheWithEmitter](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)

### Implemented by

* [default](../classes/src_core_cache_never.default.html)
* [default](../classes/src_core_cache_simple.default.html)

## Index

### Properties

* [size](src_core_cache_interface.default.html#size)

### Methods

* [[iterator]](src_core_cache_interface.default.html#_iterator_)
* [clear](src_core_cache_interface.default.html#clear)
* [entries](src_core_cache_interface.default.html#entries)
* [get](src_core_cache_interface.default.html#get)
* [has](src_core_cache_interface.default.html#has)
* [keys](src_core_cache_interface.default.html#keys)
* [remove](src_core_cache_interface.default.html#remove)
* [set](src_core_cache_interface.default.html#set)
* [values](src_core_cache_interface.default.html#values)

## Properties

### Readonly size

size: number

* Defined in [src/core/cache/interface.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L23)

Number of elements within the cache

## Methods

### [iterator]

* [iterator](): IterableIterator<K>

* + Defined in [src/core/cache/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L61)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### clear

* clear(filter?: [ClearFilter](src_core_cache_interface.ClearFilter.html)<V, K>): Map<K, V>

* + Defined in [src/core/cache/interface.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L56)

  Clears the cache by the specified filter and returns a map of removed keys

  #### Parameters

  + ##### Optional filter: [ClearFilter](src_core_cache_interface.ClearFilter.html)<V, K>

  #### Returns Map<K, V>

### entries

* entries(): IterableIterator<[K, V]>

* + Defined in [src/core/cache/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L76)

  Returns an iterator from the cache that produces pairs of keys and values

  #### Returns IterableIterator<[K, V]>

### get

* get(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* + Defined in [src/core/cache/interface.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L35)

  Returns a value from the cache by the specified key

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### has

* has(key: K): boolean

* + Defined in [src/core/cache/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L29)

  Returns true if a value by the specified key exists in the cache

  #### Parameters

  + ##### key: K

  #### Returns boolean

### keys

* keys(): IterableIterator<K>

* + Defined in [src/core/cache/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L66)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### remove

* remove(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* + Defined in [src/core/cache/interface.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L50)

  Removes a value from the cache by the specified key

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### set

* set(key: K, value: V, opts?: {}): V

* + Defined in [src/core/cache/interface.ts:44](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L44)

  Saves a value to the cache by the specified key

  #### Parameters

  + ##### key: K
  + ##### value: V
  + ##### Optional opts: {}

  #### Returns V

### values

* values(): IterableIterator<V>

* + Defined in [src/core/cache/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L71)

  Returns an iterator by the cache values

  #### Returns IterableIterator<V>