# Interface InnerQueue<T>
### Type parameters

* #### T = unknown

### Hierarchy

* InnerQueue
  + [InnerQueue](src_core_queue_order_interface.InnerQueue.html)
  + [InnerQueue](src_core_queue_simple_interface.InnerQueue.html)

## Index

### Properties

* [head](src_core_queue_interface.InnerQueue.html#head)
* [length](src_core_queue_interface.InnerQueue.html#length)

### Methods

* [[iterator]](src_core_queue_interface.InnerQueue.html#_iterator_)
* [clone](src_core_queue_interface.InnerQueue.html#clone)
* [pop](src_core_queue_interface.InnerQueue.html#pop)
* [push](src_core_queue_interface.InnerQueue.html#push)
* [shift](src_core_queue_interface.InnerQueue.html#shift)
* [unshift](src_core_queue_interface.InnerQueue.html#unshift)

## Properties

### Optional Readonly head

head?: [CanUndef](../modules/index.html#CanUndef)<T>

* Defined in [src/core/queue/interface.ts:11](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L11)

### Readonly length

length: number

* Defined in [src/core/queue/interface.ts:10](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L10)

## Methods

### [iterator]

* [iterator](): IterableIterator<T>

* + Defined in [src/core/queue/interface.ts:12](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L12)

  #### Returns IterableIterator<T>

### Optional clone

* clone(): [InnerQueue](src_core_queue_interface.InnerQueue.html)<T>

* + Defined in [src/core/queue/interface.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L20)

  #### Returns [InnerQueue](src_core_queue_interface.InnerQueue.html)<T>

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/queue/interface.ts:17](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L17)

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### push

* push(task: T): number

* + Defined in [src/core/queue/interface.ts:14](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L14)

  #### Parameters

  + ##### task: T

  #### Returns number

### shift

* shift(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/queue/interface.ts:18](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L18)

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### unshift

* unshift(task: T): number

* + Defined in [src/core/queue/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L15)

  #### Parameters

  + ##### task: T

  #### Returns number