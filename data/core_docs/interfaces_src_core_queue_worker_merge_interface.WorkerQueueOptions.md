# Interface WorkerQueueOptions<T>
### Type parameters

* #### T

### Hierarchy

* [WorkerQueueOptions](src_core_queue_worker_interface.WorkerQueueOptions.html)
  + WorkerQueueOptions

## Index

### Properties

* [concurrency](src_core_queue_worker_merge_interface.WorkerQueueOptions.html#concurrency)
* [hashFn](src_core_queue_worker_merge_interface.WorkerQueueOptions.html#hashFn)
* [refreshInterval](src_core_queue_worker_merge_interface.WorkerQueueOptions.html#refreshInterval)
* [tasksFactory](src_core_queue_worker_merge_interface.WorkerQueueOptions.html#tasksFactory)

## Properties

### Optional concurrency

concurrency?: number

Inherited from [WorkerQueueOptions](src_core_queue_worker_interface.WorkerQueueOptions.html).[concurrency](src_core_queue_worker_interface.WorkerQueueOptions.html#concurrency)

* Defined in [src/core/queue/worker/interface.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L37)

The maximum number of concurrent workers

### Optional hashFn

hashFn?: [HashFn](src_core_queue_merge_interface.HashFn.html)<T>

* Defined in [src/core/queue/worker/merge/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/merge/interface.ts#L19)

Hash function for a task

### Optional refreshInterval

refreshInterval?: number

Inherited from [WorkerQueueOptions](src_core_queue_worker_interface.WorkerQueueOptions.html).[refreshInterval](src_core_queue_worker_interface.WorkerQueueOptions.html#refreshInterval)

* Defined in [src/core/queue/worker/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L42)

How often to update task statuses (in milliseconds)

### Optional tasksFactory

tasksFactory?: [CreateInnerQueue](src_core_queue_interface.CreateInnerQueue.html)<[Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<unknown>>

Inherited from [WorkerQueueOptions](src_core_queue_worker_interface.WorkerQueueOptions.html).[tasksFactory](src_core_queue_worker_interface.WorkerQueueOptions.html#tasksFactory)

* Defined in [src/core/queue/worker/interface.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L32)

A factory to create the internal queue to store elements