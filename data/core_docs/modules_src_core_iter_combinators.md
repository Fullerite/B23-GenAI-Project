# Module src/core/iter/combinators
[# core/iter/combinators](#coreitercombinators)

This module provides a bunch of helpers to combine different iterable structures.

[## sequence](#sequence)

Takes iterable objects and returns a new iterator that produces values from them sequentially.

```
import { sequence } from 'core/iterr/combinators';  
  
// [1, 2, 3, 4, 5, 6]  
console.log([  
  ...sequence([1, 2], new Set([3, 4], [5, 6].values()))  
]);
```

If the first passed object has an asynchronous iterator, the result iterator will also be asynchronous.

```
import { intoIter } from 'core/iter';  
import { sequence } from 'core/iterr/combinators';  
import { from, pick, andPick, assemble, streamArray } from 'core/json/stream';  
  
const tokens = intoIter(from(JSON.stringify({  
  total: 3,  
  data: [  
    {  
      user: 'Bob',  
      age: 21  
    },  
    {  
      user: 'Ben',  
      age: 24  
    },  
    {  
      user: 'Rob',  
      age: 28  
    }  
  ]  
})));  
  
const seq = sequence(  
  assemble(pick(tokens, 'total')),  
  streamArray(andPick(tokens, 'data'))  
);  
  
for await (const val of seq) {  
  // 3  
  // {index: 0, value: {user: 'Bob', age: 21}}  
  // {index: 1, value: {user: 'Ben', age: 24}}  
  // {index: 2, value: {user: 'Rob', age: 28}}  
  console.log(val);  
}
```

## Index

### Functions

* [sequence](src_core_iter_combinators.html#sequence)

## Functions

### sequence

* sequence<T>(...iterables: T[]): IterableIterator<[IterableType](index.html#IterableType)<T>>
* sequence<T, A>(iterable: T, ...iterables: A[]): AsyncIterableIterator<[IterableType](index.html#IterableType)<T> | [IterableType](index.html#IterableType)<A>>

* + Defined in [src/core/iter/combinators/index.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/iter/combinators/index.ts#L18)

  Takes iterable objects and returns a new iterator that produces values from them sequentially

  #### Type parameters

  + #### T: Iterable<any, T>

  #### Parameters

  + ##### Rest ...iterables: T[]

  #### Returns IterableIterator<[IterableType](index.html#IterableType)<T>>
* + Defined in [src/core/iter/combinators/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/iter/combinators/index.ts#L28)

  Takes async iterable objects and returns a new async iterator that produces values from them sequentially

  #### Type parameters

  + #### T: AsyncIterable<any, T>
  + #### A: [AnyIterable](index.html#AnyIterable)<any>

  #### Parameters

  + ##### iterable: T
  + ##### Rest ...iterables: A[]

  #### Returns AsyncIterableIterator<[IterableType](index.html#IterableType)<T> | [IterableType](index.html#IterableType)<A>>