# Module src/core/cache/decorators/ttl
[# core/cache/decorators/ttl](#corecachedecoratorsttl)

This module provides a wrapper for [Cache](src_core_cache.html#Cache) data structures to add a feature of the cache expiring.
To describe how long should keep an item in the cache, use the `ttl` parameter.
The value for `ttl` should be provided in milliseconds.

[## Example](#example)

```
import addTTL from 'core/cache/decorators/ttl';  
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = addTTL(new SimpleCache());  
  
cache.add('foo', 'bar1', {ttl: 500});  
cache.add('foo2', 'bar2', {ttl: 1000});  
cache.add('baz', 'bar3');  
  
console.log(cache.keys().length); // 3  
  
setTimeout(() => {  
  console.log(cache.keys().length); // 1  
}, 2000);
```

[## Default ttl](#default-ttl)

When you wrap a cache object with the `ttl` decorator, you can provide the default ttl value.
This value is used when you don't provide the `ttl` parameter when saving an item.

```
import addTTL from 'core/cache/decorators/ttl';  
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = addTTL(new SimpleCache(), 10000);  
  
cache.add('foo', 'bar1', {ttl: 500}); // TTL 500 has the higher priority and will overwrite 10000s  
cache.add('foo2', 'bar2'); // TTL will be 10000
```

[## Property collisions](#property-collisions)

In case of a property collision, all old properties, including their TTL values, will be overwritten.

```
import addTTL from 'core/cache/decorators/ttl';  
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = addTTL(new SimpleCache());  
  
cache.add('foo', 'bar1', {ttl: 500});  
cache.add('foo', 'bar1'); // TTL will be overwritten
```

## Index

### References

* [TTLCache](src_core_cache_decorators_ttl.html#TTLCache)
* [TTLDecoratorOptions](src_core_cache_decorators_ttl.html#TTLDecoratorOptions)

### Functions

* [default](src_core_cache_decorators_ttl.html#default)

## References

### TTLCache

Re-exports [TTLCache](../interfaces/src_core_cache_decorators_ttl_interface.TTLCache.html)

### TTLDecoratorOptions

Re-exports [TTLDecoratorOptions](../interfaces/src_core_cache_decorators_ttl_interface.TTLDecoratorOptions.html)

## Functions

### default

* default<T, V, K>(cache: T, ttl?: number): [TTLCache](../interfaces/src_core_cache_decorators_ttl_interface.TTLCache.html)<V, K, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, K, T>>

* + Defined in [src/core/cache/decorators/ttl/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/cache/decorators/ttl/index.ts#L43)

  Wraps the specified cache object to add a feature of the cache expiring

  example
  :   ```
      import addTTL from 'core/cache/decorators/ttl';  
      import SimpleCache from 'core/cache/simple';  
        
      const  
        cache = addTTL(new SimpleCache(), (10).seconds());  
        
      cache.add('foo', 'bar1', {ttl: 0.5.seconds()});  
      cache.add('foo2', 'bar2');
      ```

  #### Type parameters

  + #### T: [default](../interfaces/src_core_cache_interface.default.html)<V, K, T>
  + #### V = unknown

    value type of the cache object
  + #### K: string = string

    key type of the cache object

  #### Parameters

  + ##### cache: T

    cache object to wrap
  + ##### Optional ttl: number

    default ttl value in milliseconds

  #### Returns [TTLCache](../interfaces/src_core_cache_decorators_ttl_interface.TTLCache.html)<V, K, [CacheWithEmitter](../interfaces/src_core_cache_decorators_helpers_add_emitter_interface.CacheWithEmitter.html)<V, K, T>>