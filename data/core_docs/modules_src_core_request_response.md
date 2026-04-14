# Module src/core/request/response
[# core/request/response](#corerequestresponse)

This module provides a class to work with server response data.
The class' API is pretty similar to native the [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) class
but has some extra functionality. The class doesn't implement native Response static methods.

[## Why not just use the native Response class?](#why-not-just-use-the-native-response-class)

Because, the `core/request` module can use different engines, but not only `fetch` or `XMLHttpRequest`.
These engines can have different peculiarities, so we need to create a new abstraction.

[## Difference between native and V4 Response classes](#difference-between-native-and-v4-response-classes)

There are a few differences between these classes:

1. The `body` property is not a stream object. Instead, it contains raw response data used to initialize an instance.
2. Each `Response` instance is an async iterable object. So you can use this feature to process the response as a stream.
   Notice, not every request engine can stream response.

```
import request from 'core/request';  
import fetchEngine from 'core/request/engines/fetch';  
  
for await (const chunk of request('//movie', {engine: fetchEngine})) {  
  console.log(chunk.data, chunk.total, chunk.loaded);  
}
```

[## Extra API](#extra-api)
[### Events](#events)

| EventName | Description | Payload description | Payload |
| --- | --- | --- | --- |
| `bodyUsed` | The response body has been read via `decode` | - | - |
| `streamUsed` | The response body has been read via an async iterator | - | - |

[### Constructor options](#constructor-options)

With creation of a Response instance you can pass a bunch of options.

```
export interface ResponseOptions {  
  url?: string;  
  redirected?: boolean;  
  type?: ResponseModeType;  
  
  /**  
   * Parent operation promise  
   */  
  parent?: AbortablePromise;  
  
  /**  
   * A meta flag that indicates that the request is important: is usually used with decoders to indicate that  
   * the request needs to be executed as soon as possible  
   */  
  important?: boolean;  
  
  status?: StatusCodes;  
  statusText?: string;  
  
  /**  
   * A list of status codes (or a single code) that match successful operation.  
   * Also, you can pass a range of codes.  
   */  
  okStatuses?: OkStatuses;  
  
  /**  
   * Type of the response data  
   */  
  responseType?: ResponseType;  
  
  /**  
   * Set of response headers  
   */  
  headers?: RawHeaders;  
  
  /**  
   * A function or sequence of functions to decode a response body  
   */  
  decoder?: WrappedDecoder | WrappedDecoders;  
  
  /**  
   * A function or sequence of functions to decode a response chunk when you are parsing the response in a stream form  
   */  
  streamDecoder?: WrappedStreamDecoder | WrappedStreamDecoders;  
  
  /**  
   * Reviver function for `JSON.parse`  
   * @default `convertIfDate`  
   */  
  jsonReviver?: JSONCb | false;  
}
```

[### Properties](#properties)
[#### streamUsed](#streamused)

True, if the response body is already read as a stream.

[#### okStatuses](#okstatuses)

A list of status codes (or a single code) that match successful operation.
Also, you can pass a range of codes.

[#### decoders](#decoders)

A list of response decoders.

[#### streamDecoders](#streamdecoders)

A list of response decoders to apply for chunks when you are parsing response in a stream form.

[#### jsonReviver](#jsonreviver)

A reviver function for `JSON.parse`.

[#### emitter](#emitter)

Event emitter to broadcast response events.

```
import request from 'core/request';  
  
request('//foo.jpg')  
  .then(({response}) => {  
    response.emitter.once('bodyUsed', () => {  
      console.log('Body has been read');  
    });  
  
    return response.decode();  
  });
```

[### Methods](#methods)
[#### decode](#decode)

Parses the response body and returns a promise with the result.
The operation result is memoized, and you can't parse the response as a stream after invoking this method.

A way to parse data is based on the response `Content-Type` header or a passed `responseType` constructor option.
Also, a sequence of decoders is applied to the parsed result if they are passed with a `decoders`constructor option.

```
import request from 'core/request';  
  
request('//foo.jpg')  
  .then(({response}) => response.decode())  
  .then((img) => console.log(img instanceof Blob));  
  
request('//users', {decoders: [parseProtobuf, normalizeUsers], responseType: 'arrayBuffer'})  
  .then(({response}) => response.decode())  
  .then((users) => console.log(users));
```

[#### decodeStream](#decodestream)

Parses the response body as a stream and yields chunks via an async iterator.
You can't parse the response as a whole data after invoking this method.

A way to parse data chunks is based on the response `Content-Type` header or a passed `responseType`constructor option.
Also, a sequence of stream decoders is applied to the parsed chunk if they are passed with a `streamDecoders` constructor option.

```
import request from 'core/request';  
import { streamArray } from 'core/json/stream';  
  
request('//foo.jpg')  
  .then(async ({response}) => {  
    for await (const chunk of response.decodeStream()) {  
      console.log(chunk instanceof ArrayBuffer);  
    }  
  });  
  
request('//users', {streamDecoders: [streamArray], responseType: 'json'})  
  .then(async ({response}) => {  
    for await (const user of response.decodeStream()) {  
      console.log(user);  
    }  
  });
```

[#### jsonStream](#jsonstream)

Parses the response data stream as a JSON tokens and yields them via an async iterator.

```
import request from 'core/request';  
import { streamArray } from 'core/json/stream';  
  
request('//users', {streamDecoders: [streamArray]})  
  .then(async ({response}) => {  
    for await (const user of response.jsonStream()) {  
      console.log(user);  
    }  
  });
```

[#### textStream](#textstream)

Parses the response data stream as a text chunks and yields them via an async iterator.

```
import request from 'core/request';  
  
request('//users')  
  .then(async ({response}) => {  
    for await (const textFragment of response.textStream()) {  
      console.log(textFragment);  
    }  
  });
```

[#### stream](#stream)

Parses the response data stream as an ArrayBuffer chunks and yields them via an async iterator.

```
import request from 'core/request';  
  
request('//users')  
  .then(async ({response}) => {  
    for await (const chunkBuffer of response.stream()) {  
      console.log(chunkBuffer);  
    }  
  });
```

[#### [Symbol.asyncIterator]](#symbolasynciterator)

Returns an iterator by the response body.
Mind, when you parse response via iterator, you won't be able to use other parse methods, like `json` or `text`.

```
import request from 'core/request';  
  
request('//users')  
  .then(async ({response}) => {  
    for await (const {loaded, total, data} of response) {  
      console.log(loaded, total, data);  
    }  
  });
```

## Index

### References

* [HeadersForEachCb](src_core_request_response.html#HeadersForEachCb)
* [JSONLikeValue](src_core_request_response.html#JSONLikeValue)
* [NormalizedResponseOptions](src_core_request_response.html#NormalizedResponseOptions)
* [RawHeaders](src_core_request_response.html#RawHeaders)
* [ResponseChunk](src_core_request_response.html#ResponseChunk)
* [ResponseModeType](src_core_request_response.html#ResponseModeType)
* [ResponseOptions](src_core_request_response.html#ResponseOptions)
* [ResponseType](src_core_request_response.html#ResponseType)
* [ResponseTypeValue](src_core_request_response.html#ResponseTypeValue)
* [ResponseTypeValueP](src_core_request_response.html#ResponseTypeValueP)
* [defaultResponseOpts](src_core_request_response.html#defaultResponseOpts)
* [noContentStatusCodes](src_core_request_response.html#noContentStatusCodes)

### Classes

* [default](../classes/src_core_request_response.default.html)

### Variables

* [$$](src_core_request_response.html#__)

## References

### HeadersForEachCb

Re-exports [HeadersForEachCb](../interfaces/src_core_request_headers_interface.HeadersForEachCb.html)

### JSONLikeValue

Re-exports [JSONLikeValue](src_core_request_response_interface.html#JSONLikeValue)

### NormalizedResponseOptions

Re-exports [NormalizedResponseOptions](src_core_request_response_interface.html#NormalizedResponseOptions)

### RawHeaders

Re-exports [RawHeaders](src_core_request_headers_interface.html#RawHeaders)

### ResponseChunk

Re-exports [ResponseChunk](../interfaces/src_core_request_response_interface.ResponseChunk.html)

### ResponseModeType

Re-exports [ResponseModeType](src_core_request_response_interface.html#ResponseModeType)

### ResponseOptions

Re-exports [ResponseOptions](../interfaces/src_core_request_response_interface.ResponseOptions.html)

### ResponseType

Re-exports [ResponseType](src_core_request_response_interface.html#ResponseType)

### ResponseTypeValue

Re-exports [ResponseTypeValue](src_core_request_response_interface.html#ResponseTypeValue)

### ResponseTypeValueP

Re-exports [ResponseTypeValueP](src_core_request_response_interface.html#ResponseTypeValueP)

### defaultResponseOpts

Re-exports [defaultResponseOpts](src_core_request_response_const.html#defaultResponseOpts)

### noContentStatusCodes

Re-exports [noContentStatusCodes](src_core_request_response_const.html#noContentStatusCodes)

## Variables

### Const $$

$$: [StrictDictionary](../interfaces/index.StrictDictionary.html)<symbol> = ...

* Defined in [src/core/request/response/index.ts:62](https://github.com/V4Fire/Core/blob/master/src/core/request/response/index.ts#L62)