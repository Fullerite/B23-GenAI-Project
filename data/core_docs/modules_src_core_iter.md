# Module src/core/iter
[# core/iter](#coreiter)

This module provides a bunch of helpers to create and work with iterators.

[## intoIter](#intoiter)

Creates an iterator based on the specified object and returns it.
The function has various overloads:

1. If the passed value is a boolean, the function creates an infinite iterator.

```
import { intoIter } from 'core/iter';  
  
// From 0 to Infinity  
intoIter(true);  
  
// From 0 to Infinity  
intoIter(false);
```

2. If the passed value is `null` or `undefined`, the function creates an empty iterator.

```
import { intoIter } from 'core/iter';  
  
// []  
console.log([...intoIter(null)]);
```

3. If the passed value is a number, the function creates an iterator from zero to the specified number (non including).

```
import { intoIter } from 'core/iter';  
  
// [0, 1, 2]  
console.log([...intoIter(3)]);  
  
// [0, -1, -2]  
console.log([...intoIter(-3)]);
```

4. If the passed value is a string, the function creates an iterator over the string graphical letters.

```
import { intoIter } from 'core/iter';  
  
// ['f', 'o', 'o']  
console.log([...intoIter('foo')]);  
  
// ['1', '😃', 'à', '🇷🇺', '👩🏽‍❤️‍💋‍👨']  
console.log([...intoIter('1😃à🇷🇺👩🏽‍❤️‍💋‍👨')]);
```

5. If the passed value is a dictionary, the function creates an iterator over the dictionary values.

```
import { intoIter } from 'core/iter';  
  
// [1, 2]  
console.log([...intoIter({a: 1, b: 2})]);
```

6. If the passed value is a generator, the function creates a new iterator over it.

```
import { intoIter } from 'core/iter';  
  
// [1, 2]  
console.log(function* () { yield* [1, 2]; });
```

7. If the passed value is an async generator, the function creates a new async iterator over it.

```
import { intoIter } from 'core/iter';  
  
for await (const el of async function* () { yield* [1, 2]; }) {  
  // 1  
  // 2  
  console.log(el);  
}
```

8. If the passed value is an iterable structure, the function creates a new iterator over it.

```
import { intoIter } from 'core/iter';  
  
// [1, 2]  
console.log([...intoIter([1, 2].values())]);
```

9. If the passed value is an async iterable structure, the function creates a new async iterator over it.

```
import { intoIter } from 'core/iter';  
  
for await (const el of (async function* () { yield* [1, 2]; })()) {  
  // 1  
  // 2  
  console.log(el);  
}
```

## Index

### Functions

* [intoIter](src_core_iter.html#intoIter)

## Functions

### intoIter

* intoIter(obj: boolean): IterableIterator<number>
* intoIter(obj: undefined | null): IterableIterator<undefined>
* intoIter(obj: number): IterableIterator<number>
* intoIter(obj: string): IterableIterator<string>
* intoIter<T>(obj: T): IterableIterator<[DictionaryType](index.html#DictionaryType)<T>>
* intoIter<T>(obj: ArrayLike<T>): IterableIterator<T>
* intoIter<T>(obj: GeneratorFunction): IterableIterator<T>
* intoIter<T>(obj: AsyncGeneratorFunction): AsyncIterableIterator<T>
* intoIter<T>(obj: T): IterableIterator<[IterableType](index.html#IterableType)<T>>
* intoIter<T>(obj: T): AsyncIterableIterator<[IterableType](index.html#IterableType)<T>>

* + Defined in [src/core/iter/index.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L23)

  Creates an infinite iterator and returns it.
  If the passed value is true, the created iterator will produce values from zero to the positive infinity.
  Otherwise, from zero to the negative infinity.

  #### Parameters

  + ##### obj: boolean

  #### Returns IterableIterator<number>
* + Defined in [src/core/iter/index.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L29)

  Creates an empty iterator and returns it

  #### Parameters

  + ##### obj: undefined | null

  #### Returns IterableIterator<undefined>
* + Defined in [src/core/iter/index.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L36)

  Creates an iterator from zero to the passed number (non including) and returns it

  #### Parameters

  + ##### obj: number

  #### Returns IterableIterator<number>
* + Defined in [src/core/iter/index.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L42)

  Creates an iterator over the passed string by graphical letters

  #### Parameters

  + ##### obj: string

  #### Returns IterableIterator<string>
* + Defined in [src/core/iter/index.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L48)

  Creates an iterator over values from the specified dictionary and returns it

  #### Type parameters

  + #### T: [Dictionary](../interfaces/index.Dictionary.html)<unknown, T>

  #### Parameters

  + ##### obj: T

  #### Returns IterableIterator<[DictionaryType](index.html#DictionaryType)<T>>
* + Defined in [src/core/iter/index.ts:54](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L54)

  Creates an iterator over values from the specified array-like object and returns it

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: ArrayLike<T>

  #### Returns IterableIterator<T>
* + Defined in [src/core/iter/index.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L60)

  Creates an iterator from the passed generator function and returns it

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: GeneratorFunction

  #### Returns IterableIterator<T>
* + Defined in [src/core/iter/index.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L66)

  Creates an iterator from the passed async generator function and returns it

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: AsyncGeneratorFunction

  #### Returns AsyncIterableIterator<T>
* + Defined in [src/core/iter/index.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L72)

  Creates a new iterator based on the specified iterable structure and returns it

  #### Type parameters

  + #### T: Iterable<any, T>

  #### Parameters

  + ##### obj: T

  #### Returns IterableIterator<[IterableType](index.html#IterableType)<T>>
* + Defined in [src/core/iter/index.ts:78](https://github.com/V4Fire/Core/blob/master/src/core/iter/index.ts#L78)

  Creates a new async iterator based on the specified async iterable structure and returns it

  #### Type parameters

  + #### T: AsyncIterable<any, T>

  #### Parameters

  + ##### obj: T

  #### Returns AsyncIterableIterator<[IterableType](index.html#IterableType)<T>>