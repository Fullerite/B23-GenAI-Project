# Class default<T>
### Type parameters

* #### T = unknown

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_request_modules_stream_buffer.default.html#constructor)

### Properties

* [buffer](src_core_request_modules_stream_buffer.default.html#buffer)
* [isAsyncIteratorInvoked](src_core_request_modules_stream_buffer.default.html#isAsyncIteratorInvoked)
* [pendingPromise](src_core_request_modules_stream_buffer.default.html#pendingPromise)

### Accessors

* [isOpened](src_core_request_modules_stream_buffer.default.html#isOpened)

### Methods

* [[asyncIterator]](src_core_request_modules_stream_buffer.default.html#_asyncIterator_)
* [[iterator]](src_core_request_modules_stream_buffer.default.html#_iterator_)
* [add](src_core_request_modules_stream_buffer.default.html#add)
* [close](src_core_request_modules_stream_buffer.default.html#close)
* [destroy](src_core_request_modules_stream_buffer.default.html#destroy)

## Constructors

### constructor

* new default<T>(values?: Iterable<T>): [default](src_core_request_modules_stream_buffer.default.html)<T>

* + Defined in [src/core/request/modules/stream-buffer/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L43)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### values: Iterable<T> = []

  #### Returns [default](src_core_request_modules_stream_buffer.default.html)<T>

## Properties

### Protected buffer

buffer: T[]

* Defined in [src/core/request/modules/stream-buffer/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L28)

Buffer of added values

### Protected isAsyncIteratorInvoked

isAsyncIteratorInvoked: boolean

* Defined in [src/core/request/modules/stream-buffer/index.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L38)

True, if an asynchronous iterator from `Symbol.asyncIterator` was called

### Protected pendingPromise

pendingPromise: [Nullable](../modules/index.html#Nullable)<[ControllablePromise](../interfaces/src_core_request_modules_stream_buffer_interface.ControllablePromise.html)<T>>

* Defined in [src/core/request/modules/stream-buffer/index.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L33)

Current pending promise that resolves when a new value is added

## Accessors

### isOpened

* get isOpened(): boolean

* + Defined in [src/core/request/modules/stream-buffer/index.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L21)

  Returns a boolean stating whether the stream is open or not

  #### Returns boolean

## Methods

### [asyncIterator]

* [asyncIterator](): AsyncIterableIterator<T>

* + Defined in [src/core/request/modules/stream-buffer/index.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L59)

  Returns an async iterator allowing to go through the stream

  #### Returns AsyncIterableIterator<T>

### [iterator]

* [iterator](): IterableIterator<T>

* + Defined in [src/core/request/modules/stream-buffer/index.ts:52](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L52)

  Returns an iterator allowing to go through all items that were already added

  #### Returns IterableIterator<T>

### add

* add(value: T): void

* + Defined in [src/core/request/modules/stream-buffer/index.ts:97](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L97)

  Adds a new value to the stream if it is opened, otherwise does nothing

  #### Parameters

  + ##### value: T

    item to add

  #### Returns void

### close

* close(): void

* + Defined in [src/core/request/modules/stream-buffer/index.ts:110](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L110)

  Closes the stream

  #### Returns void

### destroy

* destroy<R>(reason?: R): void

* + Defined in [src/core/request/modules/stream-buffer/index.ts:123](https://github.com/V4Fire/Core/blob/master/src/core/request/modules/stream-buffer/index.ts#L123)

  Destroys the stream

  #### Type parameters

  + #### R = unknown

  #### Parameters

  + ##### Optional reason: R

  #### Returns void