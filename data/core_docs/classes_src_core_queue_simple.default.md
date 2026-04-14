# Class default<T>
Implementation of a queue data structure based on a linked-list

### Type parameters

* #### T

  the queue element

### Hierarchy

* [default](src_core_queue_interface.default.html)<T>
  + default

## Index

### Constructors

* [constructor](src_core_queue_simple.default.html#constructor)

### Properties

* [InnerQueue](src_core_queue_simple.default.html#InnerQueue)
* [createInnerQueue](src_core_queue_simple.default.html#createInnerQueue)
* [innerQueue](src_core_queue_simple.default.html#innerQueue)

### Accessors

* [head](src_core_queue_simple.default.html#head)
* [length](src_core_queue_simple.default.html#length)

### Methods

* [[iterator]](src_core_queue_simple.default.html#_iterator_)
* [clear](src_core_queue_simple.default.html#clear)
* [clone](src_core_queue_simple.default.html#clone)
* [pop](src_core_queue_simple.default.html#pop)
* [push](src_core_queue_simple.default.html#push)
* [shift](src_core_queue_simple.default.html#shift)
* [unshift](src_core_queue_simple.default.html#unshift)
* [values](src_core_queue_simple.default.html#values)

## Constructors

### constructor

* new default<T>(): [default](src_core_queue_simple.default.html)<T>

* Overrides [default](src_core_queue_interface.default.html).[constructor](src_core_queue_interface.default.html#constructor)

  + Defined in [src/core/queue/simple/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L47)

  override

  #### Type parameters

  + #### T

  #### Returns [default](src_core_queue_simple.default.html)<T>

## Properties

### Readonly InnerQueue

InnerQueue: [default](src_core_linked_list_list.default.html)<T>

* Defined in [src/core/queue/simple/index.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L29)

Type: the internal queue to store elements

### Protected createInnerQueue

createInnerQueue: [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)<[default](src_core_linked_list_list.default.html)<T>> = ...

* Defined in [src/core/queue/simple/index.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L84)

Returns a new blank internal queue to store elements

### Protected innerQueue

innerQueue: [default](src_core_linked_list_list.default.html)<T>

* Defined in [src/core/queue/simple/index.ts:44](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L44)

The internal queue to store elements

## Accessors

### head

* get head(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides Queue.head

  + Defined in [src/core/queue/simple/index.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L32)

  The first element in the queue

  inheritdoc

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### length

* get length(): number

* Overrides Queue.length

  + Defined in [src/core/queue/simple/index.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L37)

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

  + Defined in [src/core/queue/simple/index.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L64)

  Clears the queue

  #### Returns void

### clone

* clone(): [default](src_core_queue_simple.default.html)<T>

* Overrides [default](src_core_queue_interface.default.html).[clone](src_core_queue_interface.default.html#clone)

  + Defined in [src/core/queue/simple/index.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L71)

  Creates a new queue based on the current one and returns it

  #### Returns [default](src_core_queue_simple.default.html)<T>

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides [default](src_core_queue_interface.default.html).[pop](src_core_queue_interface.default.html#pop)

  + Defined in [src/core/queue/simple/index.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L59)

  Removes the head element from the queue and returns it

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### push

* push(task: T): number

* Overrides [default](src_core_queue_interface.default.html).[push](src_core_queue_interface.default.html#push)

  + Defined in [src/core/queue/simple/index.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L53)

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

* Overrides [default](src_core_queue_interface.default.html).[values](src_core_queue_interface.default.html#values)

  + Defined in [src/core/queue/simple/index.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/queue/simple/index.ts#L77)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>