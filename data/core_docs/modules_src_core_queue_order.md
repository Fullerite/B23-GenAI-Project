# Module src/core/queue/order
[# core/queue/order](#corequeueorder)

This module provides a class to organize an ordered [Queue](src_core_queue.html#Queue) data structure.
See [`core/queue`](src_core_queue.html) for more information.

[## Usage](#usage)

```
import OrderedQueue from 'core/queue/order';  
  
const  
  queue = new OrderedQueue<number>((a, b) => a - b);  
  
queue.push(1);  
queue.push(5);  
queue.push(2);  
queue.push(-1);  
queue.push(5);  
queue.push(2);  
queue.push(-1);  
queue.push(5);  
  
console.log(queue.length); // 8  
  
console.log(queue.head);   // 5  
console.log(queue.pop());  // 5  
  
console.log(queue.head);   // 5  
console.log(queue.pop());  // 5  
  
console.log(queue.pop());  // 5  
console.log(queue.pop());  // 2  
console.log(queue.pop());  // 2  
  
queue.clear();  
console.log(queue.length); // 0
```

[### Providing a comparator](#providing-a-comparator)

To compare different elements from the queue, a special comparator function is used, which has the same API as
the native comparator `Array.prototype.sort`. To provide a comparator, use the structure constructor.

```
import OrderedQueue from 'core/queue/order';  
  
const  
  queue = new OrderedQueue<number>((a, b) => a - b);  
  
queue.push(1);  
queue.push(5);
```

## Index

### References

* [CreateInnerQueue](src_core_queue_order.html#CreateInnerQueue)
* [ElsComparator](src_core_queue_order.html#ElsComparator)
* [InnerQueue](src_core_queue_order.html#InnerQueue)
* [QueueOptions](src_core_queue_order.html#QueueOptions)

### Classes

* [default](../classes/src_core_queue_order.default.html)

## References

### CreateInnerQueue

Re-exports [CreateInnerQueue](../interfaces/src_core_queue_interface.CreateInnerQueue.html)

### ElsComparator

Re-exports [ElsComparator](../interfaces/src_core_queue_order_interface.ElsComparator.html)

### InnerQueue

Re-exports [InnerQueue](../interfaces/src_core_queue_order_interface.InnerQueue.html)

### QueueOptions

Re-exports [QueueOptions](../interfaces/src_core_queue_interface.QueueOptions.html)