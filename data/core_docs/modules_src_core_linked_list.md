# Module src/core/linked-list
[# core/linked-list](#corelinked-list)

This module provides a class to organize a double-ended two-way linked list.
For convenience, the list API is similar to the regular JS Array API.

```
import LinkedList from 'core/linked-list';  
  
const  
  list = new LinkedList();  
  
list.push(10, 11);  
  
// 2  
console.log(list.length);  
  
// 11  
console.log(list.pop());
```

[## API](#api)
[### Constructor](#constructor)

The LinkedList constructor can take any Iterable object whose elements will be used to populate the list.

```
import LinkedList from 'core/linked-list';  
  
const  
  list = new LinkedList([1, 2, 3]);  
  
// 3  
console.log(list.length);
```

[### Own API](#own-api)
[#### first](#first)

Data of the first node in the list.

```
import LinkedList from 'core/linked-list';  
  
const  
  list = new LinkedList([1, 2, 3]);  
  
// 1  
console.log(list.first);
```

[#### last](#last)

Data of the last node in the list.

```
import LinkedList from 'core/linked-list';  
  
const  
  list = new LinkedList([1, 2, 3]);  
  
// 3  
console.log(list.last);
```

[#### clear](#clear)

Clears all nodes from the list.

```
import LinkedList from 'core/linked-list';  
  
const  
  list = new LinkedList([1, 2, 3]);  
  
list.clear();  
  
console.log(list.first);  // undefined  
console.log(list.last);   // undefined  
console.log(list.length); // 0
```

[#### reverse](#reverse)

Returns an iterator over the data in the list.
The traversal will proceed from the last node to the first.

```
import LinkedList from 'core/linked-list';  
  
const  
  list = new LinkedList([1, 2, 3]);  
  
// 3, 2, 1  
console.log(...list.reverse());
```

[### Array-Like API](#array-like-api)

For convenience, the LinkedList API is similar to the regular JS Array API:

1. Adding and removing is done through the `push/pop/shift/unshift` methods.

   ```
   import LinkedList from 'core/linked-list';  
     
   const  
     list = new LinkedList();  
     
   list.push(10, 11);  
   list.unshift(9);  
     
   // 11  
   console.log(list.pop());  
     
   // 9  
   console.log(list.shift());
   ```
2. Checking if a node is in the list with a given value is done using `includes`.

   ```
   import LinkedList from 'core/linked-list';  
     
   const  
     list = new LinkedList([-0, 1, NaN, 2]);  
     
   console.log(list.includes(0));   // true  
   console.log(list.includes(1));   // true  
   console.log(list.includes(NaN)); // true  
   console.log(list.includes(12));  // false
   ```
3. Use the `length` getter to get the number of nodes in the list. The `push/unshift` methods also return the length of the list.

   ```
   import LinkedList from 'core/linked-list';  
     
   const  
     list = new LinkedList();  
     
   list.push(10, 11); // 2  
   list.unshift(9);   // 3  
     
   // 3  
   console.log(list.length);
   ```
4. To create a new list based on another, use `slice`.

   ```
   import LinkedList from 'core/linked-list';  
     
   const  
     list = new LinkedList([1, 2, 3]);  
     
   // [3]  
   console.log([...list.slice(-1)]);  
     
   // [1, 2]  
   console.log([...list.slice(0, -1)]);
   ```
5. There are 2 iterators to traverse the list: `values` (used by default) and `reverse`.
   Note that unlike arrays, here `reverse` returns an iterator, not a new linked list.
   However, you can pass this iterator to the constructor when creating a new list.

   ```
   import LinkedList from 'core/linked-list';  
     
   const  
     list = new LinkedList([1, 2, 3]);  
     
   // [1, 2, 3]  
   console.log([...list]);  
     
   // [3, 2, 1]  
   console.log([...list.reverse()]);  
     
   const  
     reversedList = new LinkedList([...list.reverse()]);  
     
   // [3, 2, 1]  
   console.log([...reversedList]);
   ```

## Index

### References

* [default](src_core_linked_list.html#default)

## References

### default

Re-exports [default](../classes/src_core_linked_list_list.default.html)