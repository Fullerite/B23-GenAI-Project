# Module src/core/queue
[# core/queue](#corequeue)

This module provides an abstract class for any [Queue](src_core_queue.html#Queue) data structure.
For convenience, the underlying queue API is fairly close to the regular JS array API.

The submodules contain different classes and interfaces that extends or implements that class.
The main module re-exports these implementations:

* `AbstractQueue` — an alias for [`core/queue/interface/Queue`](src_core_queue_interface.html);
* `AbstractWorkerQueue` — an alias for [`core/queue/worker/interface/WorkerQueue`](src_core_queue_worker_interface.html);
* `Queue` — an alias for [`core/queue/simple`](src_core_queue_simple.html);
* `OrderedQueue` — an alias for [`core/queue/order`](src_core_queue_order.html);
* `MergeQueue` — an alias for [`core/queue/merge`](src_core_queue_merge.html).
* `AbstractWorkerQueue` — an alias for [`core/queue/worker`](src_core_queue_worker.html).
* `WorkerQueue` — an alias for [`core/queue/worker/simple`](src_core_queue_worker_simple.html).
* `MergeWorkerQueue` — an alias for [`core/queue/worker/merge`](src_core_queue_worker_merge.html).

[## API](#api)
[### Own API](#own-api)
[#### head](#head)

The first element in the queue.

```
import Queue from 'core/queue/simple';  
  
const  
 queue = new Queue();  
  
queue.push(1);  
queue.push(5);  
  
console.log(queue.head); // 1
```

[#### clone](#clone)

Creates a new queue based on the current one and returns it.

```
import Queue from 'core/queue/simple';  
  
const  
 queue1 = new Queue();  
  
queue1.push(1);  
queue1.push(5);  
  
const  
  queue2 = queue1.clone();  
  
console.log(queue2.head);       // 1  
console.log(queue1 !== queue2); // true
```

[#### clear](#clear)

Clears the queue.

```
import Queue from 'core/queue/simple';  
  
const  
  queue = new Queue();  
  
queue.push(1);  
queue.push(5);  
  
console.log(queue.head); // 1  
  
queue.clear();  
  
console.log(queue.head);   // undefined  
console.log(queue.length); // 0
```

[### Array-Like API](#array-like-api)

For convenience, the underlying queue API is fairly close to the regular JS array API.

1. That is, you have methods for adding and removing elements: `push/unshift` and `pop/shift`.
   Notice, the `shift` and `unshift` methods just aliases for `pop` and `push`.

   ```
   import Queue from 'core/queue/simple';  
     
   const  
     queue = new Queue();  
     
   queue.push(1);  
   queue.unshift(5);  
     
   console.log(queue.pop());   // 1  
   console.log(queue.shift()); // 5
   ```
2. You can also find out the number of elements in the queue using the `length` getter.

   ```
   import Queue from 'core/queue/simple';  
     
   const  
     queue = new Queue();  
     
   queue.push(1);  
   queue.push(5);  
     
   console.log(queue.length);  // 2
   ```
3. Like arrays, any queue can be traversed using an iterator.

   ```
   import Queue from 'core/queue/simple';  
     
   const  
     queue = new Queue();  
     
   queue.push(1);  
   queue.push(5);  
     
   // [1, 5]  
   console.log([...queue]);  
     
   // [1, 5]  
   console.log([...queue.values()]);
   ```

In addition, the API declares `head` to get the first element from the queue and `clear` to clear the queue.

```
import Queue from 'core/queue/simple';  
  
const  
 queue = new Queue();  
  
queue.push(1);  
queue.push(5);  
  
console.log(queue.head); // 1  
  
queue.clear();  
  
console.log(queue.head);   // undefined  
console.log(queue.length); // 0
```

[### Simple implementation](#simple-implementation)

```
import { AbstractQueue } from 'core/queue';  
  
export default class Queue extends AbstractQueue {  
  internalQueue = [];  
  
  get head() {  
    return this.internalQueue[0];  
  }  
  
  get length() {  
    return this.internalQueue.length;  
  }  
  
  push(el) {  
    return this.internalQueue.push(el);  
  }  
  
  pop() {  
    return this.internalQueue.shift();  
  }  
  
  clone() {  
    const queue = new Queue();  
    queue.internalQueue = this.internalQueue.slice();  
    return queue;  
  }  
  
  clear() {  
    this.internalQueue = [];  
  }  
}
```

## Index

### References

* [AbstractQueue](src_core_queue.html#AbstractQueue)
* [AbstractWorkerQueue](src_core_queue.html#AbstractWorkerQueue)
* [CreateInnerQueue](src_core_queue.html#CreateInnerQueue)
* [CreateTasks](src_core_queue.html#CreateTasks)
* [InnerQueue](src_core_queue.html#InnerQueue)
* [MergeWorkerQueue](src_core_queue.html#MergeWorkerQueue)
* [OrderedQueue](src_core_queue.html#OrderedQueue)
* [Queue](src_core_queue.html#Queue)
* [QueueOptions](src_core_queue.html#QueueOptions)
* [QueueWorker](src_core_queue.html#QueueWorker)
* [Task](src_core_queue.html#Task)
* [Tasks](src_core_queue.html#Tasks)
* [WorkerQueueOptions](src_core_queue.html#WorkerQueueOptions)

## References

### AbstractQueue

Renames and re-exports [default](../classes/src_core_queue_interface.default.html)

### AbstractWorkerQueue

Renames and re-exports [default](../classes/src_core_queue_worker_interface.default.html)

### CreateInnerQueue

Re-exports [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)

### CreateTasks

Re-exports [CreateTasks](src_core_queue_worker_interface.html#CreateTasks)

### InnerQueue

Re-exports [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)

### MergeWorkerQueue

Renames and re-exports [default](../classes/src_core_queue_worker_merge.default.html)

### OrderedQueue

Renames and re-exports [default](../classes/src_core_queue_order.default.html)

### Queue

Renames and re-exports [default](../classes/src_core_queue_simple.default.html)

### QueueOptions

Re-exports [QueueOptions](../interfaces/src_core_queue_interface.QueueOptions.html)

### QueueWorker

Re-exports [QueueWorker](../interfaces/src_core_queue_worker_interface.QueueWorker.html)

### Task

Re-exports [Task](../interfaces/src_core_queue_worker_interface.Task.html)

### Tasks

Re-exports [Tasks](src_core_queue_worker_interface.html#Tasks)

### WorkerQueueOptions

Renames and re-exports [QueueOptions](../interfaces/src_core_queue_interface.QueueOptions.html)