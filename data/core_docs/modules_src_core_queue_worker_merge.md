# Module src/core/queue/worker/merge
[# core/queue/worker/merge](#corequeueworkermerge)

This module provides a class to organize a [[WorkerQueue]] data structure with support of task merging by a specified hash function.
It means that the same tasks aren't duplicated. See [`core/queue/worker`](src_core_queue_worker.html) and
[`core/queue`](src_core_queue.html) for more information.

[## Usage](#usage)

```
import MergeQueue from 'core/queue/worker/merge';  
  
const queue = new MergeQueue((task) => {  
  console.log(task);  
}, {  
  concurrency: 2,  
  refreshInterval: 50,  
  hashFn: (task) => JSON.stringify(task)  
});  
  
queue.push({a: 1});  
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

[### Providing a hash function](#providing-a-hash-function)

To provide a function to calculate task hashes, use the structure constructor `hashFn` option.
By default, all hashes are calculated via `Object.fastHash`.

```
import MergeQueue from 'core/queue/worker/merge';  
  
const queue = new MergeQueue((task) => {  
  console.log(task);  
}, {  
  hashFn: (task) => JSON.stringify(task)  
});  
  
queue.push({a: 1});  
queue.push({a: 1});
```

## Index

### References

* [CreateInnerQueue](src_core_queue_worker_merge.html#CreateInnerQueue)
* [CreateTasks](src_core_queue_worker_merge.html#CreateTasks)
* [HashFn](src_core_queue_worker_merge.html#HashFn)
* [InnerQueue](src_core_queue_worker_merge.html#InnerQueue)
* [QueueOptions](src_core_queue_worker_merge.html#QueueOptions)
* [QueueWorker](src_core_queue_worker_merge.html#QueueWorker)
* [Task](src_core_queue_worker_merge.html#Task)
* [Tasks](src_core_queue_worker_merge.html#Tasks)
* [WorkerQueueOptions](src_core_queue_worker_merge.html#WorkerQueueOptions)

### Classes

* [default](../classes/src_core_queue_worker_merge.default.html)

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