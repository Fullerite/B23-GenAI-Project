# Class default<T>
An abstract class for any queue data structure

### Type parameters

* #### T

  queue element

### Hierarchy

* default
  + [default](src_core_queue_merge.default.html)
  + [default](src_core_queue_order.default.html)
  + [default](src_core_queue_simple.default.html)
  + [default](src_core_queue_worker_interface.default.html)

## Index

### Constructors

* [constructor](src_core_queue_interface.default.html#constructor)

### Properties

* [head](src_core_queue_interface.default.html#head)
* [length](src_core_queue_interface.default.html#length)

### Methods

* [[iterator]](src_core_queue_interface.default.html#_iterator_)
* [clear](src_core_queue_interface.default.html#clear)
* [clone](src_core_queue_interface.default.html#clone)
* [pop](src_core_queue_interface.default.html#pop)
* [push](src_core_queue_interface.default.html#push)
* [shift](src_core_queue_interface.default.html#shift)
* [unshift](src_core_queue_interface.default.html#unshift)
* [values](src_core_queue_interface.default.html#values)

## Constructors

### constructor

* new default<T>(): [default](src_core_queue_interface.default.html)<T>

* #### Type parameters

  + #### T

  #### Returns [default](src_core_queue_interface.default.html)<T>

## Properties

### Readonly Abstract head

head: [CanUndef](../modules/index.html#CanUndef)<T>

* Defined in [src/core/queue/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L42)

The first element in the queue

### Readonly Abstract length

length: number

* Defined in [src/core/queue/interface.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L47)

Number of elements in the queue

## Methods

### [iterator]

* [iterator](): IterableIterator<T>

* + Defined in [src/core/queue/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L89)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>

### Abstract clear

* clear(): void

* + Defined in [src/core/queue/interface.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L79)

  Clears the queue

  #### Returns void

### Abstract clone

* clone(): [default](src_core_queue_interface.default.html)<T>

* + Defined in [src/core/queue/interface.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L84)

  Creates a new queue based on the current one and returns it

  #### Returns [default](src_core_queue_interface.default.html)<T>

### Abstract pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/queue/interface.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L58)

  Removes the head element from the queue and returns it

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### Abstract push

* push(el: T): unknown

* + Defined in [src/core/queue/interface.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L53)

  Adds a new element to the queue

  #### Parameters

  + ##### el: T

  #### Returns unknown

### shift

* shift(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/queue/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L72)

  Alias to `pop`

  see
  :   [[Queue.pop]]

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### unshift

* unshift(el: T): unknown

* + Defined in [src/core/queue/interface.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L64)

  Alias to `push`

  see
  :   [[Queue.push]]

  #### Parameters

  + ##### el: T

  #### Returns unknown

### values

* values(): IterableIterator<T>

* + Defined in [src/core/queue/interface.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L96)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>