# Module src/core/queue/merge
[# core/queue/merge](#corequeuemerge)

This module provides a class to organize a [Queue](src_core_queue.html#Queue) data structure with support of task merging by a specified hash function.
It means that the same tasks aren't duplicated. See [`core/queue`](src_core_queue.html) for more information.

[## Usage](#usage)

```
import MergeQueue from 'core/queue/merge';  
  
const queue = new MergeQueue((task) => JSON.stringify(task));  
  
queue.push({a: 1});  
queue.push({a: 1});  
  
console.log(queue.length); // 1  
  
queue.push({a: 2});  
  
console.log(queue.head);   // {a: 1}  
console.log(queue.length); // 2  
  
queue.clear();  
console.log(queue.length); // 0
```

[### Providing a hash function](#providing-a-hash-function)

To provide a function to calculate task hashes, use the structure constructor.
By default, all hashes are calculated via `Object.fastHash`.

```
import MergeQueue from 'core/queue/merge';  
  
const queue = new MergeQueue((task) => JSON.stringify(task));  
  
queue.push({a: 1});  
queue.push({a: 1});
```

## Index

### References

* [CreateInnerQueue](src_core_queue_merge.html#CreateInnerQueue)
* [HashFn](src_core_queue_merge.html#HashFn)
* [InnerQueue](src_core_queue_merge.html#InnerQueue)
* [QueueOptions](src_core_queue_merge.html#QueueOptions)

### Classes

* [default](../classes/src_core_queue_merge.default.html)

## References

### CreateInnerQueue

Re-exports [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)

### HashFn

Re-exports [HashFn](../interfaces/src_core_queue_merge_interface.HashFn.html)

### InnerQueue

Re-exports [InnerQueue](../interfaces/src_core_queue_interface.InnerQueue.html)

### QueueOptions

Re-exports [QueueOptions](../interfaces/src_core_queue_interface.QueueOptions.html)