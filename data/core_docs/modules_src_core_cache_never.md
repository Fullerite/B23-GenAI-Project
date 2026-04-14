# Module src/core/cache/never
[# core/cache/never](#corecachenever)

This module provides a loopback class for a [Cache](src_core_cache.html#Cache) data structure.
It can be helpful if you use the "strategy" pattern and need to prevent caching.

```
import * as cache from 'core/cache';  
  
class Foo {  
  constructor(cacheStrategy) {  
    this.cache = cache[cacheStrategy];  
  }  
}  
  
const withCache = new Foo('Cache');  
const withoutCache = new Foo('NeverCache');
```

[## API](#api)

See [Cache](src_core_cache.html#Cache).

## Index

### References

* [ClearFilter](src_core_cache_never.html#ClearFilter)

### Classes

* [default](../classes/src_core_cache_never.default.html)

## References

### ClearFilter

Re-exports [ClearFilter](../interfaces/src_core_cache_interface.ClearFilter.html)