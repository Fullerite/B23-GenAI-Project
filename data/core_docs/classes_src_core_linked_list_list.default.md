# Class default<T>
Double-ended two-way linked list

### Type parameters

* #### T

  linked list node data

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_linked_list_list.default.html#constructor)

### Properties

* [firstNode](src_core_linked_list_list.default.html#firstNode)
* [lastNode](src_core_linked_list_list.default.html#lastNode)
* [lengthStore](src_core_linked_list_list.default.html#lengthStore)

### Accessors

* [first](src_core_linked_list_list.default.html#first)
* [last](src_core_linked_list_list.default.html#last)
* [length](src_core_linked_list_list.default.html#length)

### Methods

* [[iterator]](src_core_linked_list_list.default.html#_iterator_)
* [clear](src_core_linked_list_list.default.html#clear)
* [includes](src_core_linked_list_list.default.html#includes)
* [pop](src_core_linked_list_list.default.html#pop)
* [push](src_core_linked_list_list.default.html#push)
* [reverse](src_core_linked_list_list.default.html#reverse)
* [shift](src_core_linked_list_list.default.html#shift)
* [slice](src_core_linked_list_list.default.html#slice)
* [unshift](src_core_linked_list_list.default.html#unshift)
* [values](src_core_linked_list_list.default.html#values)

## Constructors

### constructor

* new default<T>(iterable?: Iterable<T>): [default](src_core_linked_list_list.default.html)<T>

* + Defined in [src/core/linked-list/list.ts:55](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L55)

  #### Type parameters

  + #### T

  #### Parameters

  + ##### Optional iterable: Iterable<T>

  #### Returns [default](src_core_linked_list_list.default.html)<T>

## Properties

### Protected firstNode

firstNode: [Nullable](../modules/index.html#Nullable)<[default](src_core_linked_list_node.default.html)<T>> = null

* Defined in [src/core/linked-list/list.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L40)

A link to the first node of the list

### Protected lastNode

lastNode: [Nullable](../modules/index.html#Nullable)<[default](src_core_linked_list_node.default.html)<T>> = null

* Defined in [src/core/linked-list/list.ts:45](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L45)

A link to the last node of the list

### Protected lengthStore

lengthStore: number = 0

* Defined in [src/core/linked-list/list.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L50)

Internal length value of the list

## Accessors

### first

* get first(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/linked-list/list.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L26)

  Data of the first node in the list

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### last

* get last(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/linked-list/list.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L33)

  Data of the last node in the list

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### length

* get length(): number

* + Defined in [src/core/linked-list/list.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L19)

  Number of nodes in the list

  #### Returns number

## Methods

### [iterator]

* [iterator](): IterableIterator<T>

* + Defined in [src/core/linked-list/list.ts:66](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L66)

  Returns an iterator over the data from the list

  #### Returns IterableIterator<T>

### clear

* clear(): void

* + Defined in [src/core/linked-list/list.ts:204](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L204)

  Clears all nodes from the list

  #### Returns void

### includes

* includes(data: T): boolean

* + Defined in [src/core/linked-list/list.ts:182](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L182)

  Returns true if the list contains a node with the given data

  #### Parameters

  + ##### data: T

  #### Returns boolean

### pop

* pop(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/linked-list/list.ts:151](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L151)

  Removes the last node from the list and returns its data as the result.
  This method changes the length of the list.

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### push

* push(...data: T[]): number

* + Defined in [src/core/linked-list/list.ts:127](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L127)

  Adds the passed data to the end of the list and returns its new length

  #### Parameters

  + ##### Rest ...data: T[]

  #### Returns number

### reverse

* reverse(): IterableIterator<T>

* + Defined in [src/core/linked-list/list.ts:330](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L330)

  Returns an iterator over the data in the list.
  The traversal will proceed from the last node to the first.

  #### Returns IterableIterator<T>

### shift

* shift(): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/linked-list/list.ts:98](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L98)

  Removes the first node from the list and returns its data as the result.
  This method changes the length of the list.

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>

### slice

* slice(start?: number, end?: number): [default](src_core_linked_list_list.default.html)<T>

* + Defined in [src/core/linked-list/list.ts:217](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L217)

  Returns a shallow copy of a portion of a list into a new LinkedList selected from start to end (end not included)
  where start and end represent the index of nodes in that list. The original list will not be modified.

  #### Parameters

  + ##### Optional start: number
  + ##### Optional end: number

  #### Returns [default](src_core_linked_list_list.default.html)<T>

### unshift

* unshift(...data: T[]): number

* + Defined in [src/core/linked-list/list.ts:74](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L74)

  Adds the passed data to the beginning of the list and returns its new length

  #### Parameters

  + ##### Rest ...data: T[]

  #### Returns number

### values

* values(): IterableIterator<T>

* + Defined in [src/core/linked-list/list.ts:291](https://github.com/V4Fire/Core/blob/master/src/core/linked-list/list.ts#L291)

  Returns an iterator over the data from the list

  #### Returns IterableIterator<T>