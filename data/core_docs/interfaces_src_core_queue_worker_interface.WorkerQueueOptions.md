# Interface WorkerQueueOptions<T>
### Type parameters

* #### T: [Tasks](../modules/src_core_queue_worker_interface.html#Tasks)<any> = [Tasks](../modules/src_core_queue_worker_interface.html#Tasks)

### Hierarchy

* WorkerQueueOptions
  + [WorkerQueueOptions](src_core_queue_worker_merge_interface.WorkerQueueOptions.html)

## Index

### Properties

* [concurrency](src_core_queue_worker_interface.WorkerQueueOptions.html#concurrency)
* [refreshInterval](src_core_queue_worker_interface.WorkerQueueOptions.html#refreshInterval)
* [tasksFactory](src_core_queue_worker_interface.WorkerQueueOptions.html#tasksFactory)

## Properties

### Optional concurrency

concurrency?: number

* Defined in [src/core/queue/worker/interface.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L37)

The maximum number of concurrent workers

### Optional refreshInterval

refreshInterval?: number

* Defined in [src/core/queue/worker/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L42)

How often to update task statuses (in milliseconds)

### Optional tasksFactory

tasksFactory?: [CreateInnerQueue](src_core_queue_interface.CreateInnerQueue.html)<T>

* Defined in [src/core/queue/worker/interface.ts:32](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L32)

A factory to create the internal queue to store elements