# Module src/core/queue/worker/simple
[# core/queue/worker/simple](#corequeueworkersimple)

This module provides a class to organize a [[WorkerQueue]] data structure.
See [`core/queue/worker`](src_core_queue_worker.html) and [`core/queue`](src_core_queue.html) for more information.

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
  
queue.clear();  
console.log(queue.length); // 0
```

## Index

### References

* [CreateInnerQueue](src_core_queue_worker_simple.html#CreateInnerQueue)
* [CreateTasks](src_core_queue_worker_simple.html#CreateTasks)
* [HashFn](src_core_queue_worker_simple.html#HashFn)
* [InnerQueue](src_core_queue_worker_simple.html#InnerQueue)
* [QueueOptions](src_core_queue_worker_simple.html#QueueOptions)
* [QueueWorker](src_core_queue_worker_simple.html#QueueWorker)
* [Task](src_core_queue_worker_simple.html#Task)
* [Tasks](src_core_queue_worker_simple.html#Tasks)
* [WorkerQueueOptions](src_core_queue_worker_simple.html#WorkerQueueOptions)

### Classes

* [default](../classes/src_core_queue_worker_simple.default.html)

## References

### CreateInnerQueue

Re-exports [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)

### CreateTasks

Re-exports [CreateTasks](src_core_queue_worker_interface.html#CreateTasks)

### HashFn

Re-exports [HashFn](../interfaces/src_core_queue_merge_interface.HashFn.html)

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

Re-exports [WorkerQueueOptions](../interfaces/src_core_queue_worker_merge_interface.WorkerQueueOptions.html)