# Module src/core/queue/worker/interface
## Index

### References

* [CreateInnerQueue](src_core_queue_worker_interface.html#CreateInnerQueue)
* [InnerQueue](src_core_queue_worker_interface.html#InnerQueue)
* [QueueOptions](src_core_queue_worker_interface.html#QueueOptions)

### Classes

* [default](../classes/src_core_queue_worker_interface.default.html)

### Interfaces

* [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)
* [Task](../interfaces/src_core_queue_worker_interface.Task.html)
* [WorkerQueueOptions](../interfaces/src_core_queue_worker_interface.WorkerQueueOptions.html)

### Type aliases

* [CreateTasks](src_core_queue_worker_interface.html#CreateTasks)
* [Tasks](src_core_queue_worker_interface.html#Tasks)

## References

### CreateInnerQueue

Re-exports [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)

### InnerQueue

Re-exports [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)

### QueueOptions

Re-exports [QueueOptions](../interfaces/src_core_queue_interface.QueueOptions.html)

## Type aliases

### CreateTasks

CreateTasks<T>: [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)<T>

* Defined in [src/core/queue/worker/interface.ts:22](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L22)

#### Type parameters

* #### T: [Tasks](src_core_queue_worker_interface.html#Tasks)<any>

### Tasks

Tasks<T>: [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)<T>

* Defined in [src/core/queue/worker/interface.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/queue/worker/interface.ts#L20)

#### Type parameters

* #### T = unknown