# Module src/core/queue/worker
[# core/queue/worker](#corequeueworker)

This module provides an abstract class for a [[WorkerQueue]] data structure.
The submodules contain different implementations of that class. See [`core/queue`](src_core_queue.html) for more information.

[## Implementations](#implementations)

* [SimpleWorkerQueue](src_core_queue_worker_simple.html)
* [MergeWorkerQueue](src_core_queue_worker_merge.html)

[## API](#api)
[### Constructor](#constructor)
[#### Providing a task executor](#providing-a-task-executor)

The structure constructor expects a function that will be invoked on each processed task.
The function can return a promise (it will be awaited).

```
import WorkerQueue from 'core/queue/worker/simple';  
  
const queue = new WorkerQueue((task) => {  
  console.log(task);  
});  
  
queue.push({a: 1});  
queue.push({a: 2});
```

[#### Queue options](#queue-options)
[##### [concurrency = `1`]](#concurrency--1)

The maximum number of concurrent workers.

```
import WorkerQueue from 'core/queue/worker/simple';  
  
const queue = new WorkerQueue((task) => {  
  console.log(task);  
}, {concurrency: 2});  
  
queue.push({a: 1});  
  
console.log(queue.length); // 0  
  
queue.push({a: 2});  
  
console.log(queue.length); // 0  
  
queue.push({a: 3});  
  
console.log(queue.length); // 1  
  
queue.push({a: 4});  
  
console.log(queue.length); // 2
```

[##### [refreshInterval]](#refreshinterval)

How often to update task statuses, i.e. the next batch of tasks will be executed at the specified interval
(by default on the next tick of the process).

[### Class properties](#class-properties)
[#### concurrency](#concurrency)

The maximum number of concurrent workers.

[#### refreshInterval](#refreshinterval-1)

How often to update task statuses, i.e. the next batch of tasks will be executed at the specified interval
(by default on the next tick of the process).

[#### activeWorkers](#activeworkers)

Number of active workers.

## Index

### References

* [CreateInnerQueue](src_core_queue_worker.html#CreateInnerQueue)
* [CreateTasks](src_core_queue_worker.html#CreateTasks)
* [InnerQueue](src_core_queue_worker.html#InnerQueue)
* [QueueOptions](src_core_queue_worker.html#QueueOptions)
* [QueueWorker](src_core_queue_worker.html#QueueWorker)
* [Task](src_core_queue_worker.html#Task)
* [Tasks](src_core_queue_worker.html#Tasks)
* [WorkerQueueOptions](src_core_queue_worker.html#WorkerQueueOptions)
* [default](src_core_queue_worker.html#default)

## References

### CreateInnerQueue

Re-exports [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)

### CreateTasks

Re-exports [CreateTasks](src_core_queue_worker_interface.html#CreateTasks)

### InnerQueue

Re-exports [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)

### QueueOptions

Re-exports [QueueOptions](../interfaces/src_core_queue_interface.QueueOptions.html)

### QueueWorker

Re-exports [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)

### Task

Re-exports [Task](../interfaces/src_core_queue_worker_interface.Task.html)

### Tasks

Re-exports [Tasks](src_core_queue_worker_interface.html#Tasks)

### WorkerQueueOptions

Re-exports [WorkerQueueOptions](../interfaces/src_core_queue_worker_interface.WorkerQueueOptions.html)

### default

Re-exports [default](../classes/src_core_queue_worker_interface.default.html)