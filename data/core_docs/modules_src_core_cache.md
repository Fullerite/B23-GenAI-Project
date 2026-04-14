# Module src/core/cache
[# core/cache](#corecache)

This module provides the base interface for a [Cache](src_core_cache.html#Cache) data structure: a simple in-memory key-value storage,
which can be useful to organize cache data structures.
The submodules contain different implementations for that interface. The main module re-exports these implementations:

* `AbstractCache` — an alias for [`core/cache/interface/Cache`](src_core_cache_interface.html);
* `Cache` — an alias for [`core/cache/simple`](src_core_cache_simple.html);
* `RestrictedCache` — an alias for [`core/cache/restricted`](src_core_cache_restricted.html);
* `NeverCache` — an alias for [`core/cache/never`](src_core_cache_never.html).

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.set('foo', 'bar1');  
cache.set('foo2', 'bar2');  
cache.set('baz', 'bar3');  
  
console.log(cache.size); // 3  
  
cache.clear((val, key) => /foo/.test(key));  
  
console.log(cache.size); // 1
```

[## Iterators](#iterators)

All caches support three kinds of iterators:

1. By keys (used by default).

```
import SimpleCache from 'core/cache/simple';  
  
cache.set('foo', 'bar1');  
cache.set('foo2', 'bar2');  
cache.set('baz', 'bar3');  
  
for (const key of SimpleCache) {  
  // 'foo' 'foo2' 'baz'  
  console.log(el);  
}  
  
for (const key of SimpleCache.keys()) {  
  // 'foo' 'foo2' 'baz'  
  console.log(el);  
}
```

2. By values.

```
import SimpleCache from 'core/cache/simple';  
  
cache.set('foo', 'bar1');  
cache.set('foo2', 'bar2');  
cache.set('baz', 'bar3');  
  
for (const key of SimpleCache.values()) {  
  // 'bar1' 'bar2' 'bar3'  
  console.log(el);  
}
```

3. By pairs of keys and values.

```
import SimpleCache from 'core/cache/simple';  
  
cache.set('foo', 'bar1');  
cache.set('foo2', 'bar2');  
cache.set('baz', 'bar3');  
  
for (const key of SimpleCache.entries()) {  
  // ['foo', 'bar1'] ['foo2', 'bar2'] ['baz', 'bar3']  
  console.log(el);  
}
```

[## Decorators](#decorators)

Also, the module provides a bunch of functions to decorate cache storages, like adding the `ttl` feature or persisting data storing.

[### core/cache/decorators/ttl](#corecachedecoratorsttl)

Provides a decorator for any cache to add a feature of cache expiring.

```
import addTTL from 'core/cache/decorators/ttl';  
import SimpleCache from 'core/cache/simple';  
  
// The function `addTTL` accepts a cache object and a value for the default TTL as the second argument  
const  
  cache = addTTL(new SimpleCache(), 1000);  
  
// The method "add" accepts as the third optional parameter time until expiring the item to store in milliseconds  
cache.add('foo', 'bar1', {ttl: 500});  
  
// Additional method to remove the `ttl` descriptor from a cache item by the specified key  
cache.removeTTLFrom('foo');
```

[### core/cache/decorators/persistent](#corecachedecoratorspersistent)

Provides a decorator for any cache to add a feature of persistent data storing.

```
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
const  
  persistentCache = await addPersistent(new SimpleCache(), asyncLocal);  
  
await persistentCache.set('foo', 'bar', {persistentTTL: (2).seconds()});  
await persistentCache.set('foo2', 'bar2');  
  
// Cause we use the same instance for the local data storing,  
// this cache will have all values from the previous (it will be loaded from the storage during initialization)  
  
const  
  copyOfCache = await addPersistent(new SimpleCache(), asyncLocal, opts);
```

[## API](#api)

Ranges support a bunch of methods to work with them.

[### size (getter)](#size-getter)

Number of elements within the cache.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.add('foo', 'bar1');  
console.log(cache.size); // 1
```

[### has](#has)

Returns true if a value by the specified key exists in the cache.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.add('foo', 'bar1');  
console.log(cache.has('foo')); // true
```

[### get](#get)

Returns a value from the cache by the specified key.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.add('foo', 'bar1');  
console.log(cache.get('foo')); // 'bar1'
```

[### set](#set)

Saves a value to the cache by the specified key.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.set('foo', 'bar1');  
console.log(cache.has('foo')); // true
```

[### remove](#remove)

Removes a value from the cache by the specified key.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.set('foo', 'bar1');  
console.log(cache.has('foo')); // true  
  
cache.remove('foo');  
console.log(cache.has('foo')); // false
```

[### clear](#clear)

Clears the cache by the specified filter and returns a map of removed keys.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.set('foo1', 'bar1');  
cache.set('foo2', 'bar2');  
cache.set('foo3', 'bar2');  
  
cache.clear((val) => val === 'bar2');  
  
console.log(cache.has('foo1')); // true  
console.log(cache.has('foo1')); // true  
console.log(cache.has('foo2')); // false  
  
cache.clear();  
  
console.log(cache.has('foo1')); // true
```

## Index

### References

* [AbstractCache](src_core_cache.html#AbstractCache)
* [Cache](src_core_cache.html#Cache)
* [ClearFilter](src_core_cache.html#ClearFilter)
* [NeverCache](src_core_cache.html#NeverCache)
* [RestrictedCache](src_core_cache.html#RestrictedCache)

## References

### AbstractCache

Renames and re-exports [default](../interfaces/src_core_cache_interface.default.html)

### Cache

Renames and re-exports [default](../classes/src_core_cache_simple.default.html)

### ClearFilter

Re-exports [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)

### NeverCache

Renames and re-exports [default](../classes/src_core_cache_never.default.html)

### RestrictedCache

Renames and re-exports [default](../classes/src_core_cache_restricted.default.html)