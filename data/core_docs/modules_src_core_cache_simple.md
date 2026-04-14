# Module src/core/cache/simple
[# core/cache/simple](#corecachesimple)

This module provides a class for a simple in-memory [Cache](src_core_cache.html#Cache) data structure.

```
import SimpleCache from 'core/cache/simple';  
  
const  
  cache = new SimpleCache();  
  
cache.set('foo', 'bar1');  
cache.set('foo2', 'bar2');  
cache.set('baz', 'bar3');  
  
console.log(cache.keys().length); // 3  
  
cache.clear((val, key) => /foo/.test(key));  
  
console.log(cache.keys().length); // 1
```

[## API](#api)

See [Cache](src_core_cache.html#Cache).

## Index

### References

* [ClearFilter](src_core_cache_simple.html#ClearFilter)

### Classes

* [default](../classes/src_core_cache_simple.default.html)

## References

### ClearFilter

Re-exports [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)