# Class default<T>
Implementation of an ordered queue data structure based on a binary heap

### Type parameters

* #### T

  the queue element

### Hierarchy

* [default](src_core_queue_interface.default.html)<T>
  + default

## Index

### Constructors

* [constructor](src_core_queue_order.default.html#constructor)

### Properties

* [InnerQueue](src_core_queue_order.default.html#InnerQueue)
* [comparator](src_core_queue_order.default.html#comparator)
* [createInnerQueue](src_core_queue_order.default.html#createInnerQueue)
* [innerQueue](src_core_queue_order.default.html#innerQueue)
* [lastIndex](src_core_queue_order.default.html#lastIndex)

### Accessors

* [head](src_core_queue_order.default.html#head)
* [length](src_core_queue_order.default.html#length)

### Methods

* [[iterator]](src_core_queue_order.default.html#_iterator_)
* [clear](src_core_queue_order.default.html#clear)
* [clone](src_core_queue_order.default.html#clone)
* [fromBottom](src_core_queue_order.default.html#fromBottom)
* [pop](src_core_queue_order.default.html#pop)
* [push](src_core_queue_order.default.html#push)
* [shift](src_core_queue_order.default.html#shift)
* [toBottom](src_core_queue_order.default.html#toBottom)
* [unshift](src_core_queue_order.default.html#unshift)
* [values](src_core_queue_order.default.html#values)

## Constructors

### constructor

* new default<T>(comparator: [ElsComparator](../interfaces/src_core_queue_order_interface.ElsComparator.html)<T>): [default](src_core_queue_order.default.html)<T>

* Overrides [default](src_core_queue_interface.default.html).[constructor](src_core_queue_interface.default.html#constructor)

  + Defined in [src/core/queue/order/index.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L57)

  #### Type parameters

  + #### T

  #### Parameters

  + ##### comparator: [ElsComparator](../interfaces/src_core_queue_order_interface.ElsComparator.html)<T>

    a function to compare tasks

  #### Returns [default](src_core_queue_order.default.html)<T>

## Properties

### Readonly InnerQueue

InnerQueue: [InnerQueue](../interfaces/src_core_queue_order_interface.InnerQueue.html)<T>

* Defined in [src/core/queue/order/index.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L27)

Type: the internal queue to store elements

### Protected comparator

comparator: [ElsComparator](../interfaces/src_core_queue_order_interface.ElsComparator.html)<T>

* Defined in [src/core/queue/order/index.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L52)

A function to compare tasks

### Protected createInnerQueue

createInnerQueue: [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)<[InnerQueue](../interfaces/src_core_queue_order_interface.InnerQueue.html)<T>> = ...

* Defined in [src/core/queue/order/index.ts:110](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L110)

Returns a new blank internal queue to store elements

### Protected innerQueue

innerQueue: [InnerQueue](../interfaces/src_core_queue_order_interface.InnerQueue.html)<T>

* Defined in [src/core/queue/order/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L47)

The internal queue to store elements

### Protected lastIndex

lastIndex: number = -1

* Defined in [src/core/queue/order/index.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L42)

An index of the last element from the queue

## Accessors

### head

* get head(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides Queue.head

  + Defined in [src/core/queue/order/index.ts:30](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L30)

  The first element in the queue

  inheritdoc

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### length

* get length(): number

* Overrides Queue.length

  + Defined in [src/core/queue/order/index.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L35)

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

  + Defined in [src/core/queue/order/index.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L88)

  Clears the queue

  #### Returns void

### clone

* clone(): [default](src_core_queue_order.default.html)<T>

* Overrides [default](src_core_queue_interface.default.html).[clone](src_core_queue_interface.default.html#clone)

  + Defined in [src/core/queue/order/index.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L96)

  Creates a new queue based on the current one and returns it

  #### Returns [default](src_core_queue_order.default.html)<T>

### Protected fromBottom

* fromBottom(): void

* + Defined in [src/core/queue/order/index.ts:115](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L115)

  Pushes the last queue element to the top

  #### Returns void

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides [default](src_core_queue_interface.default.html).[pop](src_core_queue_interface.default.html#pop)

  + Defined in [src/core/queue/order/index.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L71)

  Removes the head element from the queue and returns it

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### push

* push(task: T): number

* Overrides [default](src_core_queue_interface.default.html).[push](src_core_queue_interface.default.html#push)

  + Defined in [src/core/queue/order/index.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L64)

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

### Protected toBottom

* toBottom(): void

* + Defined in [src/core/queue/order/index.ts:142](https://github.com/V4Fire/Core/blob/master/src/core/queue/order/index.ts#L142)

  Pushes the first queue element down

  #### Returns void

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