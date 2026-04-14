# Interface CacheWithEmitter<V, K, T>
### Type parameters

* #### V = unknown
* #### K = string
* #### T: [default](src_core_cache_interface.default.html)<V, K> = [default](src_core_cache_interface.default.html)<V, K>

### Hierarchy

* [default](src_core_cache_interface.default.html)<V, K>
  + CacheWithEmitter
    - [TTLCache](src_core_cache_decorators_ttl_interface.TTLCache.html)

## Index

### Properties

* [[eventEmitter]](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#_eventEmitter_)
* [size](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#size)

### Methods

* [[iterator]](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#_iterator_)
* [clear](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#clear)
* [entries](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#entries)
* [get](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#get)
* [has](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#has)
* [keys](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#keys)
* [remove](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#remove)
* [set](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#set)
* [values](src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html#values)

## Properties

### [eventEmitter]

[eventEmitter]: EventEmitter2

* Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L35)

Event emitter to produce mutation events

### Readonly size

size: number

Inherited from [default](src_core_cache_interface.default.html).[size](src_core_cache_interface.default.html#size)

* Defined in [src/core/cache/interface.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L23)

Number of elements within the cache

## Methods

### [iterator]

* [iterator](): IterableIterator<K>

* Inherited from [default](src_core_cache_interface.default.html).[[iterator]](src_core_cache_interface.default.html#_iterator_)

  + Defined in [src/core/cache/interface.ts:61](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L61)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### clear

* clear(filter?: [ClearFilter](src_core_cache_interface.ClearFilter.html)<V, K>): Map<K, V>

* Inherited from [default](src_core_cache_interface.default.html).[clear](src_core_cache_interface.default.html#clear)

  + Defined in [src/core/cache/interface.ts:56](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L56)

  Clears the cache by the specified filter and returns a map of removed keys

  #### Parameters

  + ##### Optional filter: [ClearFilter](src_core_cache_interface.ClearFilter.html)<V, K>

  #### Returns Map<K, V>

### entries

* entries(): IterableIterator<[K, V]>

* Inherited from [default](src_core_cache_interface.default.html).[entries](src_core_cache_interface.default.html#entries)

  + Defined in [src/core/cache/interface.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L76)

  Returns an iterator from the cache that produces pairs of keys and values

  #### Returns IterableIterator<[K, V]>

### get

* get(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Inherited from [default](src_core_cache_interface.default.html).[get](src_core_cache_interface.default.html#get)

  + Defined in [src/core/cache/interface.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L35)

  Returns a value from the cache by the specified key

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### has

* has(key: K): boolean

* Inherited from [default](src_core_cache_interface.default.html).[has](src_core_cache_interface.default.html#has)

  + Defined in [src/core/cache/interface.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L29)

  Returns true if a value by the specified key exists in the cache

  #### Parameters

  + ##### key: K

  #### Returns boolean

### keys

* keys(): IterableIterator<K>

* Inherited from [default](src_core_cache_interface.default.html).[keys](src_core_cache_interface.default.html#keys)

  + Defined in [src/core/cache/interface.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L66)

  Returns an iterator by the cache keys

  #### Returns IterableIterator<K>

### remove

* remove(key: K): [CanUndef](../modules/index.html#CanUndef)<V>

* Inherited from [default](src_core_cache_interface.default.html).[remove](src_core_cache_interface.default.html#remove)

  + Defined in [src/core/cache/interface.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L50)

  Removes a value from the cache by the specified key

  #### Parameters

  + ##### key: K

  #### Returns [CanUndef](../modules/index.html#CanUndef)<V>

### set

* set(key: K, value: V, opts?: Parameters<T["set"]>[2]): V

* Overrides [default](src_core_cache_interface.default.html).[set](src_core_cache_interface.default.html#set)

  + Defined in [src/core/cache/decorators/helpers/add-emitter/interface.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/helpers/add-emitter/interface.ts#L30)

  override

  #### Parameters

  + ##### key: K
  + ##### value: V
  + ##### Optional opts: Parameters<T["set"]>[2]

  #### Returns V

### values

* values(): IterableIterator<V>

* Inherited from [default](src_core_cache_interface.default.html).[values](src_core_cache_interface.default.html#values)

  + Defined in [src/core/cache/interface.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/cache/interface.ts#L71)

  Returns an iterator by the cache values

  #### Returns IterableIterator<V>