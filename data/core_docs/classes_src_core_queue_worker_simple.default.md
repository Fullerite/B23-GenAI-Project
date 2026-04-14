# Class default<T, V>
Implementation of a worker queue data structure

### Type parameters

* #### T

  the task element
* #### V = unknown

  the worker value

### Hierarchy

* [default](src_core_queue_worker_interface.default.html)<T, V>
  + default

## Index

### Constructors

* [constructor](src_core_queue_worker_simple.default.html#constructor)

### Properties

* [Tasks](src_core_queue_worker_simple.default.html#Tasks)
* [activeWorkers](src_core_queue_worker_simple.default.html#activeWorkers)
* [concurrency](src_core_queue_worker_simple.default.html#concurrency)
* [createTasks](src_core_queue_worker_simple.default.html#createTasks)
* [refreshInterval](src_core_queue_worker_simple.default.html#refreshInterval)
* [tasks](src_core_queue_worker_simple.default.html#tasks)
* [worker](src_core_queue_worker_simple.default.html#worker)

### Accessors

* [head](src_core_queue_worker_simple.default.html#head)
* [length](src_core_queue_worker_simple.default.html#length)

### Methods

* [[asyncIterator]](src_core_queue_worker_simple.default.html#_asyncIterator_)
* [[iterator]](src_core_queue_worker_simple.default.html#_iterator_)
* [clear](src_core_queue_worker_simple.default.html#clear)
* [clone](src_core_queue_worker_simple.default.html#clone)
* [deferPerform](src_core_queue_worker_simple.default.html#deferPerform)
* [perform](src_core_queue_worker_simple.default.html#perform)
* [pop](src_core_queue_worker_simple.default.html#pop)
* [push](src_core_queue_worker_simple.default.html#push)
* [resolveTask](src_core_queue_worker_simple.default.html#resolveTask)
* [shift](src_core_queue_worker_simple.default.html#shift)
* [start](src_core_queue_worker_simple.default.html#start)
* [unshift](src_core_queue_worker_simple.default.html#unshift)
* [values](src_core_queue_worker_simple.default.html#values)

## Constructors

### Protected constructor

* new default<T, V>(worker: [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)<T, V>, opts?: [WorkerQueueOptions](../interfaces/src_core_queue_worker_interface.WorkerQueueOptions.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>>): [default](src_core_queue_worker_simple.default.html)<T, V>

* Inherited from [default](src_core_queue_worker_interface.default.html).[constructor](src_core_queue_worker_interface.default.html#constructor)

  + Defined in [src/core/queue/worker/interface.ts:93](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L93)

  #### Type parameters

  + #### T
  + #### V = unknown

  #### Parameters

  + ##### worker: [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)<T, V>
  + ##### opts: [WorkerQueueOptions](../interfaces/src_core_queue_worker_interface.WorkerQueueOptions.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>> = {}

  #### Returns [default](src_core_queue_worker_simple.default.html)<T, V>

## Properties

### Readonly Tasks

Tasks: [Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<[Task](../interfaces/src_core_queue_worker_interface.Task.html)<T, unknown>>

Overrides [default](src_core_queue_worker_interface.default.html).[Tasks](src_core_queue_worker_interface.default.html#Tasks)

* Defined in [src/core/queue/worker/simple/index.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/simple/index.ts#L26)

Type: a queue of tasks

### activeWorkers

activeWorkers: number = 0

Inherited from [default](src_core_queue_worker_interface.default.html).[activeWorkers](src_core_queue_worker_interface.default.html#activeWorkers)

* Defined in [src/core/queue/worker/interface.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L77)

Number of active workers

### concurrency

concurrency: number

Inherited from [default](src_core_queue_worker_interface.default.html).[concurrency](src_core_queue_worker_interface.default.html#concurrency)

* Defined in [src/core/queue/worker/interface.ts:67](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L67)

The maximum number of concurrent workers

### Protected createTasks

createTasks: [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<[Task](../interfaces/src_core_queue_worker_interface.Task.html)<T, unknown>>> = ...

Inherited from [default](src_core_queue_worker_interface.default.html).[createTasks](src_core_queue_worker_interface.default.html#createTasks)

* Defined in [src/core/queue/worker/interface.ts:156](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L156)

Returns a new blank internal queue of tasks

### refreshInterval

refreshInterval: number

Inherited from [default](src_core_queue_worker_interface.default.html).[refreshInterval](src_core_queue_worker_interface.default.html#refreshInterval)

* Defined in [src/core/queue/worker/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L72)

How often to update task statuses (in milliseconds)

### Protected tasks

tasks: [Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<[Task](../interfaces/src_core_queue_worker_interface.Task.html)<T, unknown>>

Inherited from [default](src_core_queue_worker_interface.default.html).[tasks](src_core_queue_worker_interface.default.html#tasks)

* Defined in [src/core/queue/worker/interface.ts:87](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L87)

A queue of tasks

### Protected worker

worker: [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)<T, V>

Inherited from [default](src_core_queue_worker_interface.default.html).[worker](src_core_queue_worker_interface.default.html#worker)

* Defined in [src/core/queue/worker/interface.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L82)

The worker constructor

## Accessors

### head

* get head(): [CanUndef](../modules/index.html#CanUndef)<T>

* Overrides WorkerQueue.head

  + Defined in [src/core/queue/worker/simple/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/simple/index.ts#L28)

  The first element in the queue

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### length

* get length(): number

* Inherited from WorkerQueue.length

  + Defined in [src/core/queue/worker/interface.ts:60](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L60)

  inheritdoc

  #### Returns number

## Methods

### [asyncIterator]

* [asyncIterator](): AsyncIterableIterator<T>

* Inherited from [default](src_core_queue_worker_interface.default.html).[[asyncIterator]](src_core_queue_worker_interface.default.html#_asyncIterator_)

  + Defined in [src/core/queue/worker/interface.ts:113](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L113)

  Returns an asynchronous iterator over the queue elements

  #### Returns AsyncIterableIterator<T>

### [iterator]

* [iterator](): IterableIterator<T>

* Inherited from [default](src_core_queue_worker_interface.default.html).[[iterator]](src_core_queue_worker_interface.default.html#_iterator_)

  + Defined in [src/core/queue/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L89)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>

### clear

* clear(): void

* Inherited from [default](src_core_queue_worker_interface.default.html).[clear](src_core_queue_worker_interface.default.html#clear)

  + Defined in [src/core/queue/worker/interface.ts:146](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L146)

  Clears the queue

  #### Returns void

### clone

* clone(): [default](src_core_queue_worker_simple.default.html)<T, V>

* Overrides [default](src_core_queue_worker_interface.default.html).[clone](src_core_queue_worker_interface.default.html#clone)

  + Defined in [src/core/queue/worker/simple/index.ts:53](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/simple/index.ts#L53)

  Creates a new queue based on the current one and returns it

  #### Returns [default](src_core_queue_worker_simple.default.html)<T, V>

### Protected deferPerform

* deferPerform(): Promise<unknown>

* Inherited from [default](src_core_queue_worker_interface.default.html).[deferPerform](src_core_queue_worker_interface.default.html#deferPerform)

  + Defined in [src/core/queue/worker/interface.ts:166](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L166)

  Executes a task chunk from the queue (deferred version)

  #### Returns Promise<unknown>

### Protected perform

* perform(): void

* Overrides [default](src_core_queue_worker_interface.default.html).[perform](src_core_queue_worker_interface.default.html#perform)

  + Defined in [src/core/queue/worker/simple/index.ts:74](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/simple/index.ts#L74)

  Executes a task chunk from the queue

  #### Returns void

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* Inherited from [default](src_core_queue_worker_interface.default.html).[pop](src_core_queue_worker_interface.default.html#pop)

  + Defined in [src/core/queue/worker/interface.ts:139](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L139)

  Removes the head element from the queue and returns it

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### push

* push(task: T): Promise<V>

* Overrides [default](src_core_queue_worker_interface.default.html).[push](src_core_queue_worker_interface.default.html#push)

  + Defined in [src/core/queue/worker/simple/index.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/simple/index.ts#L32)

  Adds a new element to the queue

  #### Parameters

  + ##### task: T

  #### Returns Promise<V>

### Protected resolveTask

* resolveTask(task: T, resolve: Function): void

* Inherited from [default](src_core_queue_worker_interface.default.html).[resolveTask](src_core_queue_worker_interface.default.html#resolveTask)

  + Defined in [src/core/queue/worker/interface.ts:204](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L204)

  Provides a task result to the specified promise resolve function

  #### Parameters

  + ##### task: T
  + ##### resolve: Function

  #### Returns void

### shift

* shift(): [CanUndef](../modules/index.html#CanUndef)<T>

* Inherited from [default](src_core_queue_worker_interface.default.html).[shift](src_core_queue_worker_interface.default.html#shift)

  + Defined in [src/core/queue/interface.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L72)

  Alias to `pop`

  see
  :   [[Queue.pop]]

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### Protected start

* start(): void

* Inherited from [default](src_core_queue_worker_interface.default.html).[start](src_core_queue_worker_interface.default.html#start)

  + Defined in [src/core/queue/worker/interface.ts:186](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L186)

  Starts an execution of tasks from the queue

  #### Returns void

### unshift

* unshift(el: T): Promise<V>

* Inherited from [default](src_core_queue_worker_interface.default.html).[unshift](src_core_queue_worker_interface.default.html#unshift)

  + Defined in [src/core/queue/interface.ts:64](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L64)

  Alias to `push`

  see
  :   [[Queue.push]]

  #### Parameters

  + ##### el: T

  #### Returns Promise<V>

### values

* values(): IterableIterator<T>

* Inherited from [default](src_core_queue_worker_interface.default.html).[values](src_core_queue_worker_interface.default.html#values)

  + Defined in [src/core/queue/interface.ts:96](https://github.com/V4Fire/Core/blob/master/src/core/queue/interface.ts#L96)

  Returns an iterator over the queue elements

  #### Returns IterableIterator<T>