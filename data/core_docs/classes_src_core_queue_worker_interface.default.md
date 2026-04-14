# Class default<T, V>
An abstract class for a worker queue data structure

### Type parameters

* #### T

  the task element
* #### V = unknown

  the worker value

### Hierarchy

* [default](src_core_queue_interface.default.html)<T>
  + default
    - [default](src_core_queue_worker_merge.default.html)
    - [default](src_core_queue_worker_simple.default.html)

## Index

### Constructors

* [constructor](src_core_queue_worker_interface.default.html#constructor)

### Properties

* [Tasks](src_core_queue_worker_interface.default.html#Tasks)
* [activeWorkers](src_core_queue_worker_interface.default.html#activeWorkers)
* [concurrency](src_core_queue_worker_interface.default.html#concurrency)
* [createTasks](src_core_queue_worker_interface.default.html#createTasks)
* [head](src_core_queue_worker_interface.default.html#head)
* [refreshInterval](src_core_queue_worker_interface.default.html#refreshInterval)
* [tasks](src_core_queue_worker_interface.default.html#tasks)
* [worker](src_core_queue_worker_interface.default.html#worker)

### Accessors

* [length](src_core_queue_worker_interface.default.html#length)

### Methods

* [[asyncIterator]](src_core_queue_worker_interface.default.html#_asyncIterator_)
* [[iterator]](src_core_queue_worker_interface.default.html#_iterator_)
* [clear](src_core_queue_worker_interface.default.html#clear)
* [clone](src_core_queue_worker_interface.default.html#clone)
* [deferPerform](src_core_queue_worker_interface.default.html#deferPerform)
* [perform](src_core_queue_worker_interface.default.html#perform)
* [pop](src_core_queue_worker_interface.default.html#pop)
* [push](src_core_queue_worker_interface.default.html#push)
* [resolveTask](src_core_queue_worker_interface.default.html#resolveTask)
* [shift](src_core_queue_worker_interface.default.html#shift)
* [start](src_core_queue_worker_interface.default.html#start)
* [unshift](src_core_queue_worker_interface.default.html#unshift)
* [values](src_core_queue_worker_interface.default.html#values)

## Constructors

### Protected constructor

* new default<T, V>(worker: [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)<T, V>, opts?: [WorkerQueueOptions](../interfaces/src_core_queue_worker_interface.WorkerQueueOptions.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>>): [default](src_core_queue_worker_interface.default.html)<T, V>

* Overrides [default](src_core_queue_interface.default.html).[constructor](src_core_queue_interface.default.html#constructor)

  + Defined in [src/core/queue/worker/interface.ts:93](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L93)

  #### Type parameters

  + #### T
  + #### V = unknown

  #### Parameters

  + ##### worker: [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)<T, V>
  + ##### opts: [WorkerQueueOptions](../interfaces/src_core_queue_worker_interface.WorkerQueueOptions.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>> = {}

  #### Returns [default](src_core_queue_worker_interface.default.html)<T, V>

## Properties

### Readonly Tasks

Tasks: [Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>

* Defined in [src/core/queue/worker/interface.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L55)

Type: a queue of tasks

### activeWorkers

activeWorkers: number = 0

* Defined in [src/core/queue/worker/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L77)

Number of active workers

### concurrency

concurrency: number

* Defined in [src/core/queue/worker/interface.ts:67](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L67)

The maximum number of concurrent workers

### Protected createTasks

createTasks: [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>> = ...

* Defined in [src/core/queue/worker/interface.ts:156](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L156)

Returns a new blank internal queue of tasks

### Readonly Abstract head

head: [CanUndef](../modules/index.html#CanUndef)<T>

Overrides [default](src_core_queue_interface.default.html).[head](src_core_queue_interface.default.html#head)

* Defined in [src/core/queue/worker/interface.ts:57](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L57)

The first element in the queue

### refreshInterval

refreshInterval: number

* Defined in [src/core/queue/worker/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L72)

How often to update task statuses (in milliseconds)

### Protected tasks

tasks: [Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>

* Defined in [src/core/queue/worker/interface.ts:87](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L87)

A queue of tasks

### Protected worker

worker: [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)<T, V>

* Defined in [src/core/queue/worker/interface.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L82)

The worker constructor

## Accessors

### length

* get length(): number

* Overrides AbstractQueue.length

  + Defined in [src/core/queue/worker/interface.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L60)

  Number of elements in the queue

  inheritdoc

  #### Returns number

## Methods

### [asyncIterator]

* [asyncIterator](): AsyncIterableIterator<T>

* + Defined in [src/core/queue/worker/interface.ts:113](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L113)

  Returns an asynchronous iterator over the queue elements

  #### Returns AsyncIterableIterator<T>

### [iterator]

* [iterator](): IterableIterator<T>

* Inherited from [default](src_core_queue_interface.default.html).[[iterator]](src_core_queue_interface.default.html#_iterator_)

  + Defined in [src/core/queue/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L89)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>

### clear

* clear(): void

* Overrides [default](src_core_queue_interface.default.html).[clear](src_core_queue_interface.default.html#clear)

  + Defined in [src/core/queue/worker/interface.ts:146](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L146)

  Clears the queue

  #### Returns void

### Abstract clone

* clone(): [default](src_core_queue_interface.default.html)<T>

* Inherited from [default](src_core_queue_interface.default.html).[clone](src_core_queue_interface.default.html#clone)

  + Defined in [src/core/queue/interface.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L84)

  Creates a new queue based on the current one and returns it

  #### Returns [default](src_core_queue_interface.default.html)<T>

### Protected deferPerform

* deferPerform(): Promise<unknown>

* + Defined in [src/core/queue/worker/interface.ts:166](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L166)

  Executes a task chunk from the queue (deferred version)

  #### Returns Promise<unknown>

### Protected Abstract perform

* perform(): unknown

* + Defined in [src/core/queue/worker/interface.ts:161](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L161)

  Executes a task chunk from the queue

  #### Returns unknown

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides [default](src_core_queue_interface.default.html).[pop](src_core_queue_interface.default.html#pop)

  + Defined in [src/core/queue/worker/interface.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L139)

  Removes the head element from the queue and returns it

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### Abstract push

* push(task: T): unknown

* Overrides [default](src_core_queue_interface.default.html).[push](src_core_queue_interface.default.html#push)

  + Defined in [src/core/queue/worker/interface.ts:108](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L108)

  Adds a new element to the queue

  #### Parameters

  + ##### task: T

  #### Returns unknown

### Protected resolveTask

* resolveTask(task: T, resolve: Function): void

* + Defined in [src/core/queue/worker/interface.ts:204](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L204)

  Provides a task result to the specified promise resolve function

  #### Parameters

  + ##### task: T
  + ##### resolve: Function

  #### Returns void

### shift

* shift(): [CanUndef](../modules/index.html#CanUndef)<T>

* Inherited from [default](src_core_queue_interface.default.html).[shift](src_core_queue_interface.default.html#shift)

  + Defined in [src/core/queue/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L72)

  Alias to `pop`

  see
  :   [[Queue.pop]]

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### Protected start

* start(): void

* + Defined in [src/core/queue/worker/interface.ts:186](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L186)

  Starts an execution of tasks from the queue

  #### Returns void

### unshift

* unshift(el: T): unknown

* Inherited from [default](src_core_queue_interface.default.html).[unshift](src_core_queue_interface.default.html#unshift)

  + Defined in [src/core/queue/interface.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L64)

  Alias to `push`

  see
  :   [[Queue.push]]

  #### Parameters

  + ##### el: T

  #### Returns unknown

### values

* values(): IterableIterator<T>

* Inherited from [default](src_core_queue_interface.default.html).[values](src_core_queue_interface.default.html#values)

  + Defined in [src/core/queue/interface.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L96)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>