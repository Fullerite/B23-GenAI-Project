# Class default<T>
Implementation of a queue data structure with support of task merging by a specified hash function

### Type parameters

* #### T

  the queue element

### Hierarchy

* [default](src_core_queue_interface.default.html)<T>
  + default

## Index

### Constructors

* [constructor](src_core_queue_merge.default.html#constructor)

### Properties

* [InnerQueue](src_core_queue_merge.default.html#InnerQueue)
* [createInnerQueue](src_core_queue_merge.default.html#createInnerQueue)
* [hashFn](src_core_queue_merge.default.html#hashFn)
* [innerQueue](src_core_queue_merge.default.html#innerQueue)
* [tasksMap](src_core_queue_merge.default.html#tasksMap)

### Accessors

* [head](src_core_queue_merge.default.html#head)
* [length](src_core_queue_merge.default.html#length)

### Methods

* [[iterator]](src_core_queue_merge.default.html#_iterator_)
* [clear](src_core_queue_merge.default.html#clear)
* [clone](src_core_queue_merge.default.html#clone)
* [pop](src_core_queue_merge.default.html#pop)
* [push](src_core_queue_merge.default.html#push)
* [shift](src_core_queue_merge.default.html#shift)
* [unshift](src_core_queue_merge.default.html#unshift)
* [values](src_core_queue_merge.default.html#values)

## Constructors

### constructor

* new default<T>(hashFn?: [HashFn](../interfaces/src_core_queue_merge_interface.HashFn.html)<T>): [default](src_core_queue_merge.default.html)<T>

* Overrides [default](src_core_queue_interface.default.html).[constructor](src_core_queue_interface.default.html#constructor)

  + Defined in [src/core/queue/merge/index.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L64)

  override

  #### Type parameters

  + #### T

  #### Parameters

  + ##### Optional hashFn: [HashFn](../interfaces/src_core_queue_merge_interface.HashFn.html)<T>

  #### Returns [default](src_core_queue_merge.default.html)<T>

## Properties

### Readonly InnerQueue

InnerQueue: [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)<string>

* Defined in [src/core/queue/merge/index.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L29)

Type: the internal queue to store elements

### Protected createInnerQueue

createInnerQueue: [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)<[InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)<string>> = ...

* Defined in [src/core/queue/merge/index.ts:126](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L126)

Returns a new blank internal queue to store elements

### Protected Readonly hashFn

hashFn: [HashFn](../interfaces/src_core_queue_merge_interface.HashFn.html)<T>

* Defined in [src/core/queue/merge/index.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L58)

A function to calculate task hashes

### Protected innerQueue

innerQueue: [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)<string>

* Defined in [src/core/queue/merge/index.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L48)

The internal queue to store elements

### Protected tasksMap

tasksMap: Map<string, T> = ...

* Defined in [src/core/queue/merge/index.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L53)

A map of registered tasks

## Accessors

### head

* get head(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides AbstractQueue.head

  + Defined in [src/core/queue/merge/index.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L32)

  The first element in the queue

  inheritdoc

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### length

* get length(): number

* Overrides AbstractQueue.length

  + Defined in [src/core/queue/merge/index.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L41)

  Number of elements in the queue

  inheritdoc

  #### Returns number

## Methods

### [iterator]

* [iterator](): IterableIterator<T>

* Inherited from [default](src_core_queue_interface.default.html).[[iterator]](src_core_queue_interface.default.html#_iterator_)

  + Defined in [src/core/queue/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L89)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>

### clear

* clear(): void

* Overrides [default](src_core_queue_interface.default.html).[clear](src_core_queue_interface.default.html#clear)

  + Defined in [src/core/queue/merge/index.ts:99](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L99)

  Clears the queue

  #### Returns void

### clone

* clone(): [default](src_core_queue_merge.default.html)<T>

* Overrides [default](src_core_queue_interface.default.html).[clone](src_core_queue_interface.default.html#clone)

  + Defined in [src/core/queue/merge/index.ts:107](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L107)

  Creates a new queue based on the current one and returns it

  #### Returns [default](src_core_queue_merge.default.html)<T>

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides [default](src_core_queue_interface.default.html).[pop](src_core_queue_interface.default.html#pop)

  + Defined in [src/core/queue/merge/index.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L84)

  Removes the head element from the queue and returns it

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### push

* push(task: T): number

* Overrides [default](src_core_queue_interface.default.html).[push](src_core_queue_interface.default.html#push)

  + Defined in [src/core/queue/merge/index.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/queue/merge/index.ts#L71)

  Adds a new element to the queue

  #### Parameters

  + ##### task: T

  #### Returns number

### shift

* shift(): [CanUndef](../modules/index.html#CanUndef)<T>

* Inherited from [default](src_core_queue_interface.default.html).[shift](src_core_queue_interface.default.html#shift)

  + Defined in [src/core/queue/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L72)

  Alias to `pop`

  see
  :   [[Queue.pop]]

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### unshift

* unshift(el: T): number

* Inherited from [default](src_core_queue_interface.default.html).[unshift](src_core_queue_interface.default.html#unshift)

  + Defined in [src/core/queue/interface.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L64)

  Alias to `push`

  see
  :   [[Queue.push]]

  #### Parameters

  + ##### el: T

  #### Returns number

### values

* values(): IterableIterator<T>

* Inherited from [default](src_core_queue_interface.default.html).[values](src_core_queue_interface.default.html#values)

  + Defined in [src/core/queue/interface.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L96)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>