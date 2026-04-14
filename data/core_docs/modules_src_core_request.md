# Module src/core/request
[# core/request](#corerequest)

This module provides API to request/submit data using different runtime engines, like XHR, Fetch, etc.
The submodules contain different classes to work with HTTP headers, server responses and errors.

```
import request from 'core/request';  
  
request('https://foo.com', {  
  method: 'POST',  
  body: {  
    bla: 'bar'  
  }  
}).then(async ({response}) => {  
  console.log(await response.decode(), response.status);  
});
```

[## Supported engines](#supported-engines)

* `xhr`
* `fetch`
* `browser` (the engine uses `fetch` when it's possible, otherwise `xhr`)
* `node` (the engine uses [Got](https://www.npmjs.com/package/got) as a request library)
* `provider` (the engine based on `core/data` providers)

[## API](#api)

The function has three overloads of usage.

[### Creating a request](#creating-a-request)

The first one creates a request based on the specified parameters.
As the first argument, the function takes a URL to request. The second argument is optional and declares additional request options.

```
import request from 'core/request';  
  
request('https://foo.com/users').then(async ({data, response}) => {  
  console.log(await data, response.status);  
});  
  
request('https://foo.com/create-user', {method: 'POST', body: {name: 'Bob'}}).then(async ({data, response}) => {  
  console.log(await data, response.status);  
});
```

[#### Request URL](#request-url)

There are two variants of request URL-s:

**absolute**

```
import request from 'core/request';  
  
request('https://foo.com/users').data.then(console.log);
```

**relative**

```
import request from 'core/request';  
  
request('/users').data.then(console.log);
```

In the case of a relative URL, the full request URL is based on the application `location`.

```
import request from 'core/request';  
  
// location.origin === 'https://foo.com';  
// URL: https://foo.com/users  
request('/users').data.then(console.log);  
  
// location.origin.href === 'https://foo.com/bla';  
// URL: https://foo.com/bla/users  
request('users').data.then(console.log);
```

But also, you can define the base API URL within your application config. This URL will be used for any relative requests.

**config**

```
import { extend } from '@v4fire/client/config';  
  
export default extend({  
  api: 'https://api.foo.com'  
});
```

**foo.ts**

```
import request from 'core/request';  
  
// URL: https://api.foo.com/users  
request('/users').data.then(console.log);
```

In addition, you can read or write the `api` property from `core/request#globalOpts` or
through `globalOpts.api` property within your encoders/decoders/middlewares.

```
import request, { globalOpts } from 'core/request';  
  
console.log(globalOpts.api);  
  
request('/users', {  
  middlewares: {  
    api: ({globalOpts}) => {  
      if (globalOpts.api == null) {  
        globalOpts.api = 'https://api.foo.com';  
      }  
    }  
  }  
}).data.then(console.log);
```

[### Creating a new request function with the default request options](#creating-a-new-request-function-with-the-default-request-options)

This overload is useful to create a wrapped request function.
It takes an object with request options and returns a new request function.
This function will use the passed options by default, but you can override them.
Finally, the result function can take another object with options and returns a new wrapped function recursively.
Parameters from the first and second invoke will be deeply merged.

```
import request from 'core/request';  
  
const post = request({method: 'POST'});  
  
const postWithoutCredentials = request({method: 'POST', credentials: false});  
  
postWithoutCredentials('https://foo.com/create-user', {body: {name: 'Bob'}}).then(async ({data, response}) => {  
  console.log(await data, response.status);  
});
```

[### Creating a new request factory with the specified URL and default request options](#creating-a-new-request-factory-with-the-specified-url-and-default-request-options)

The third overload helps to create a factory of requests.
It takes a URL to request, additional options (optional), and the special resolve function.
Then, it returns a new function to create requests with the passed options.

```
import request from 'core/request';  
  
const createUser = request(  
  'https://foo.com/user',  
  
  (url, {opts, globalOpts, ctx}, name, data) => {  
    opts.body = data;  
  
    // If the resolver function returns a string, it will be concatenated with the original request URL  
    return name;  
  },  
  
  {  
    method: 'POST'  
  }  
);  
  
// POST: https://foo.com/user/bob  
// BODY: {age: 37}  
createUser('bob', {age: 37}).then(async ({data, response}) => {  
  console.log(await data, response.status);  
});  
  
const wrappedRequest = request(  
  'https://foo.com/user',  
  
  (url, {opts, globalOpts, ctx}, ...args) => {  
    opts.body = args.at(-1);  
  
    // If the resolver function returns an array of string, it will replace the original request URL  
    return ['https://bla.com', ...args.slice(0, -1)];  
  }  
);  
  
// GET: https://bla.com/bla/baz  
wrappedRequest('bla', 'baz', {age: 37})
```

[### Returning request value](#returning-request-value)

After creating a request, the function returns an instance of `core/promise/abortable`.
The promise resolves with a special response object.

```
interface RequestResponseObject<D = unknown> {  
  // @see core/request/modules/context  
  ctx: Readonly<RequestContext<D>>;  
  
  // @see core/request/response  
  response: Response<D>;  
  
  // A promise with the response data  
  data: Promise<Nullable<D>>;  
  
  // An asynchronous iterable object to parse the response in a stream form  
  stream: AsyncIterableIterator<unknown>;  
  
  // An emitter to listen to raw request engine events  
  emitter: EventEmitter;  
  
  // An iterator to parse data in a stream form  
  [Symbol.asyncIterator](): AsyncIterable<RequestResponseChunk>;  
  
  // A type of the used cache if the data has been taken from it  
  cache?: CacheType;  
  
  // A method to drop cache of the request  
  dropCache(): void;  
}
```

```
import request from 'core/request';  
  
request('https://foo.com/users').then(async ({data, response}) => {  
  console.log(await data, response.status);  
});
```

Also, you can get `data`, `emitter` or `Symbol.asyncIterator` from a request promise.

```
import request from 'core/request';  
import xhr from 'core/request/engines/xhr';  
  
request('https://foo.com/users').data.then((data) => {  
  console.log(data);  
});  
  
request('https://foo.com/users', {engine: xhr}).emitter.on('readystatechange', (e) => {  
  console.log(e);  
});
```

[#### Parsing response data in a stream form](#parsing-response-data-in-a-stream-form)

If the used request engine supports streaming, you can use it via an async iterator.
Notice, you won't switch to another form when you read response as a whole data or in a stream form.

```
import request from 'core/request';  
  
(async () => {  
  for await (const {loaded, total, data} of request('https://foo.com/users')) {  
    console.log(loaded, total, data);  
  }  
})();  
  
request('https://foo.com/users').then(async (response) => {  
  for await (const {loaded, total, data} of response) {  
    console.log(loaded, total, data);  
  }  
});  
  
request('https://foo.com/users').then(async ({response}) => {  
  for await (const {loaded, total, data} of response) {  
    console.log(loaded, total, data);  
  }  
});
```

If you want to process only stream data without `total` and `loaded` fields, use the `stream` getter.

```
import request from 'core/request';  
  
(async () => {  
  for await (const data of request('https://foo.com/users').stream) {  
    console.log(data);  
  }  
})();  
  
request('https://foo.com/users').then(async (response) => {  
  for await (const data of response.stream) {  
    console.log(data);  
  }  
});  
  
request('https://foo.com/users').then(async ({response}) => {  
  for await (const data of response.decodeStream()) {  
    console.log(data);  
  }  
});
```

Mind, the XHR engine partially supports streaming based on its `progress` event.

[#### Listening to internal engine events](#listening-to-internal-engine-events)

If the used request engine emits some events, you can listen there via the `emitter` property.
Mind, not every engine dispatch events.

```
import request from 'core/request';  
import xhr from 'core/request/engines/xhr';  
  
const  
  req = request('https://foo.com/users', {engine: xhr});  
  
req.emitter.on('progress', (e) => {  
  console.log(e);  
});  
  
req.emitter.on('upload.progress', (e) => {  
  console.log(e);  
});
```

[### Request options](#request-options)

The request function can accept a bunch of optional parameters to make a request.

[#### method](#method)

HTTP method to create a request.
[See more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

```
import request from 'core/request';  
  
request('//create-user', {  
  method: 'POST',  
  body: {name: 'Bob'}  
}).data.then(console.log);
```

[#### headers](#headers)

Additional HTTP request headers. You can provide them as a simple dictionary or an instance of the Headers class.
Also, you can pass headers as an instance of the `core/request/headers` class.
[See more](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

```
import request from 'core/request';  
  
request('//users', {  
  headers: {  
    Authorization: myJWT  
  }  
}).data.then(console.log);
```

[#### credentials](#credentials)

Enables providing of credentials for cross-domain requests.
Also, you can manage to omit any credentials if the used request engine supports it.

```
import request from 'core/request';  
import fetchEngine from 'core/request/engines/fetch';  
  
request('//users', {  
  credentials: false  
}).data.then(console.log);  
  
request('//users', {  
  engine: fetchEngine,  
  credentials: 'omit'  
}).data.then(console.log);
```

[#### query](#query)

Request parameters that will be serialized to a string and passed via a request URL.
To customize how to encode data to a query string, see `querySerializer`.

```
import request from 'core/request';  
  
request('//user', {  
  query: {id: 125}  
}).data.then(console.log);
```

[#### querySerializer](#queryserializer)

Returns a serialized value of the specified query object.

```
import request from 'core/request';  
import { toQueryString } from 'core/url';  
  
request('//user', {  
  query: {ids: [125, 35, 454]},  
  querySerializer: (data) => toQueryString(data, {arraySyntax: true})  
}).data.then(console.log);
```

[#### body](#body)

A request body. Mind, not every HTTP method can send data in this way.
For instance, GET or HEAD requests can send data only with URLs (@see `query`).

```
import request from 'core/request';  
  
request('//create-user', {  
  method: 'POST',  
  body: {name: 'Bob'}  
}).data.then(console.log);  
  
const form = new FormData();  
  
form.set('name', 'Garry');  
form.set('age', '36');  
  
request('//send-form', {  
  method: 'POST',  
  body: form  
}).data.then(console.log);
```

[#### contentType](#contenttype)

A mime type of the request data (if not specified, it will be cast dynamically).

```
import request from 'core/request';  
  
request('//create-user', {  
  method: 'POST',  
  body: {name: 'Bob'},  
  contentType: 'application/x-msgpack',  
  encoder: toMessagePack  
}).data.then(console.log);
```

[#### responseType](#responsetype)

A type of the response data (if not specified, it will be cast dynamically from the response headers):

1. `'text'` - the result is interpreted as a simple string;
2. `'json'` - the result is interpreted as a JSON string;
3. `'document'` - the result is interpreted as an XML/HTML document;
4. `'formData'` - result is interpreted as a FormData object;
5. `'blob'` - the result is interpreted as a Blob object;
6. `'arrayBuffer'` - the result is interpreted as an array buffer;
7. `'object'` - the result is interpreted "as is" without any converting.

```
import request from 'core/request';  
  
request('//users', {  
  responseType: 'arrayBuffer',  
  decoder: fromMessagePack  
}).data.then(console.log);
```

[#### [okStatuses = `new Range(200, 299)`]](#okstatuses--new-range200-299)

A list of status codes (or a single code) that match successful operation.
Also, you can pass a range of codes.

```
import request from 'core/request';  
import Range from 'core/range';  
  
request('//users', {  
  okStatuses: [200, 201]  
}).data.then(console.log);  
  
request('//users', {  
  okStatuses: new Range(200, 210)  
}).data.then(console.log);
```

[#### timeout](#timeout)

A value in milliseconds for a request timeout.

```
import request from 'core/request';  
  
request('//users', {  
  timeout: (10).seconds()  
}).data.then(console.log);
```

[#### retry](#retry)

Options to retry bad requests or a number of maximum request retries.

```
import request from 'core/request';  
  
request('//users', {  
  timeout: (10).seconds(),  
  retry: 3  
}).data.then(console.log);  
  
request('//users', {  
  timeout: (10).seconds(),  
  retry: {  
    attempts: 3,  
    delay: (attempt) => attempt * (3).seconds()  
  }  
}).data.then(console.log);
```

```
/**  
 * @typeparam D - response data type  
 */  
export interface RetryOptions<D = unknown> {  
  /**  
   * Maximum number of attempts to request  
   */  
  attempts?: number;  
  
  /**  
   * Returns a number in milliseconds (or a promise) to wait before the next attempt.  
   * If the function returns false, it will prevent all further attempts.  
   *  
   * @param attempt - current attempt number  
   * @param error - error object  
   */  
  delay?(attempt: number, error: RequestError<D>): number | Promise<void> | false;  
}
```

[#### api](#api-1)

A map of API parameters.

These parameters apply if the original request URL is not absolute, and they can be used to customize the
base API URL depending on the runtime environment. If you define the base API URL via
`config#api` or `globalOpts.api`, these parameters will be mapped on it.

```
import request from 'core/request';  
  
// URL (IS_PROD === true): https://foo.com/users  
// URL (IS_PROD === false): https://foo.com/foo-stage  
  
request('/users', {  
  api: {  
    protocol: 'https',  
    domain2: () => IS_PROD ? 'foo' : 'foo-stage',  
    zone: 'com'  
  }  
}).data.then(console.log);  
  
  
// URL (globalOpts.api === 'https://api.foo.com' && IS_PROD === true): https://api.foo.com/users  
// URL (globalOpts.api === 'https://api.foo.com' && IS_PROD === false): https://api.foo-stage.com/users  
  
request('/users', {  
  api: {  
    domain2: () => IS_PROD ? 'foo' : 'foo-stage',  
  }  
}).data.then(console.log);
```

```
export interface RequestAPI {  
  /**  
   * The direct value of API URL.  
   * If this parameter is defined, all other parameters will be ignored.  
   *  
   * @example  
   * `'https://google.com'`  
   */  
  url?: RequestAPIValue;  
  
  /**  
   * API protocol  
   *  
   * @example  
   * `'http'`  
   * `'https'`  
   */  
  protocol?: RequestAPIValue;  
  
  /**  
   * Value for an API authorization part  
   *  
   * @example  
   * `'login:password'`  
   */  
  auth?: RequestAPIValue;  
  
  /**  
   * Value for an API domain level 6 part  
   */  
  domain6?: RequestAPIValue;  
  
  /**  
   * Value for an API domain level 5 part  
   */  
  domain5?: RequestAPIValue;  
  
  /**  
   * Value for an API domain level 4 part  
   */  
  domain4?: RequestAPIValue;  
  
  /**  
   * Value for an API domain level 3 part  
   */  
  domain3?: RequestAPIValue;  
  
  /**  
   * Value for an API domain level 2 part  
   */  
  domain2?: RequestAPIValue;  
  
  /**  
   * Value for an API domain zone part  
   */  
  zone?: RequestAPIValue;  
  
  /**  
   * Value for an API api port  
   */  
  port?: RequestAPIValue<string | number>;  
  
  /**  
   * Value for an API namespace part: it follows after '/' character  
   */  
  namespace?: RequestAPIValue;  
}
```

[#### cacheStrategy](#cachestrategy)

A strategy of caching for requests that support caching (by default, only GET requests can be cached):

1. `'forever'` - caches all requests and stores their values forever within the active session or
   until the cache expires (if `cacheTTL` is specified);
2. `'queue'` - caches all requests, but more frequent requests will push less frequent requests;
3. `'never'` - never caches any requests;
4. Or, you can pass a custom cache object.

```
import request from 'core/request';  
import RestrictedCache from 'core/cache/restricted';  
  
request('/users', {  
  cacheStrategy: 'forever'  
}).data.then(console.log);  
  
request('/users', {  
  cacheStrategy: new RestrictedCache(50)  
}).data.then(console.log);
```

If you set a strategy using string identifiers, all requests will be stored within the global cache objects.

```
import request, { cache } from 'core/request';  
  
request('/users', {  
  cacheStrategy: 'forever'  
}).data.then(console.log);  
  
cache.forever.clear();
```

[#### cacheTTL](#cachettl)

A value in milliseconds that indicates how long a request value should keep in the cache
(all requests are stored within the active session without expiring by default).

```
import request from 'core/request';  
import RestrictedCache from 'core/cache/restricted';  
  
request('/users', {  
  cacheStrategy: 'forever',  
  cacheTTL: (10).minutes()  
}).data.then(console.log);  
  
request('/users', {  
  cacheStrategy: new RestrictedCache(50),  
  cacheTTL: (10).minutes()  
}).data.then(console.log);
```

[#### offlineCache](#offlinecache)

This option enables support of offline caching.
By default, a request can only be taken from a cache if there is no network.
You can customize this logic by providing a custom cache object with the `core/cache/decorators/persistent` decorator.

```
import request from 'core/request';  
import { asyncLocal } from 'core/kv-storage';  
  
import addPersistent from 'core/cache/decorators/persistent';  
import SimpleCache from 'core/cache/simple';  
  
request('/users', {  
  cacheStrategy: 'forever',  
  offlineCache: true  
});  
  
const  
  opts = {loadFromStorage: 'onInit'},  
  persistentCache = await addPersistent(new SimpleCache(), asyncLocal, opts);  
  
request('/users', {  
  cacheStrategy: persistentCache  
});
```

[#### offlineCacheTTL](#offlinecachettl)

A value in milliseconds that indicates how long a request value should keep in the offline cache.

```
import request from 'core/request';  
import RestrictedCache from 'core/cache/restricted';  
  
request('/users', {  
  cacheStrategy: 'forever',  
  offlineCache: true,  
  offlineCacheTTL: (1).day()  
});  
  
request('/users', {  
  cacheStrategy: new RestrictedCache(50),  
  offlineCache: true,  
  offlineCacheTTL: (1).day()  
}).data.then(console.log);
```

[#### [cacheMethods = `['GET']`]](#cachemethods--39get39)

A list of request methods that support caching.

```
import request from 'core/request';  
  
request('/users', {  
  cacheStrategy: 'forever',  
  cacheMethods: ['GET', 'POST']  
}).data.then(console.log);
```

[#### cacheId](#cacheid)

A unique cache identifier: it can be useful to create request factories with isolated cache storages.

```
import request from 'core/request';  
  
const createUser = request(  
  'https://foo.com/user',  
  
  (url, {opts, globalOpts, ctx}, name, data) => {  
    opts.body = data;  
    return name;  
  },  
  
  {  
    method: 'POST',  
    cacheId: 'users'  
  }  
);  
  
createUser('bob', {age: 37}).then(async ({data, response}) => {  
  console.log(await data, response.status);  
});
```

[#### middlewares](#middlewares)

A dictionary or iterable value with middleware functions: functions take an environment of request parameters and can modify theirs.
Please notice that the order of middleware depends on the structure you use.
Also, if at least one of the middlewares returns a function, invoking this function will be returned as the request result.
It can be helpful to organize mocks of data and other similar cases when you don't want to execute a real request.

```
import request from 'core/request';  
  
request('/users', {  
  middlewares: {  
    addAPI({globalOpts}) {  
      if (globalOpts.api == null) {  
        globalOpts.api = 'https://api.foo.com';  
      }  
    },  
  
    addSession({opts}) {  
      opts.headers.set('Authorization', myJWT);  
    }  
  }  
}).data.then(console.log);  
  
// Mocking response data  
request('/users', {  
  middlewares: [  
    ({ctx}) => () => ctx.wrapAsResponse([  
      {name: 'Bob'},  
      {name: 'Robert'}  
    ])  
  ]  
});
```

[#### encoder](#encoder)

A function (or a sequence of functions) takes the current request data and returns new data to request.
If you provide a sequence of functions, the first function will pass a result in the next function from the sequence, etc.

```
import request from 'core/request';  
  
request('//create-user', {  
  method: 'POST',  
  body: {name: 'Bob'},  
  contentType: 'application/x-msgpack',  
  encoder: [normalize, toMessagePack]  
}).data.then(console.log);
```

[#### decoder](#decoder)

A function (or a sequence of functions) takes the current request response data and returns new data to respond.
If you provide a sequence of functions, the first function will pass a result to the next function from the sequence, etc.

```
import request from 'core/request';  
  
request('//users', {  
  responseType: 'arrayBuffer',  
  decoder: fromMessagePack  
}).data.then(console.log);
```

[#### streamDecoder](#streamdecoder)

A function (or a sequence of functions) takes the current request response data chunk and yields a new chunk to respond via an async iterator.
If you provide a sequence of functions, the first function will pass a result to the next function from the sequence, etc.
This parameter is used when you're parsing responses in a stream form.

```
import request from 'core/request';  
  
import { sequence } from 'core/iter/combinators';  
import { pick, andPick, assemble, streamArray } from 'core/json/stream';  
  
/*  
  {  
    "total": 3,  
    "data": [  
      {"name": "Bob", "age": 21},  
      {"name": "Rob", "age": 24},  
      {"name": "Jack", "age": 50}  
    ]  
  }  
 */  
const {stream} = request('//users', {  
  responseType: 'json',  
  streamDecoder: (data) => sequence(  
    assemble(pick(data, 'total')),  
    streamArray(andPick(data, 'data'))  
  )  
});  
  
(async () => {  
  for await (const chunk of stream) {  
    // 3  
    // {"name": "Bob", "age": 21}  
    // {"name": "Rob", "age": 24}  
    // {"name": "Jack", "age": 50}  
    console.log(chunk);  
  }  
})();
```

[#### [jsonReviver = `convertIfDate`]](#jsonreviver--convertifdate)

A reviver function for `JSON.parse` or `false` to disable defaults.
By default, it parses some strings as Date instances.

[#### meta](#meta)

A dictionary with some extra parameters for the request: is usually used with middlewares to provide domain-specific information.

```
import request from 'core/request';  
  
request('/users', {  
  meta: {addSession: true},  
  
  middlewares: {  
    addSession({opts}) {  
      if (opts.meta.addSession) {  
        opts.headers.set('Authorization', myJWT);  
      }  
    }  
  }  
}).data.then(console.log);
```

[#### important](#important)

A meta flag that indicates that the request is important: is usually used with middlewares to indicate that
the request needs to be executed as soon as possible.

```
import request from 'core/request';  
  
request('/users', {  
  important: true,  
  
  middlewares: {  
    doSomeWork({ctx}) {  
      if (ctx.important) {  
        // Do some work...  
      }  
    }  
  }  
}).data.then(console.log);
```

[#### engine](#engine)

This parameter defined a request engine to use.
The engine - is a simple function that takes request parameters and returns an abortable promise resolved with the `core/request/response` instance.
Mind, some engines provide extra features. For instance, you can listen to upload progress events with the XHR engine.
Or, you can parse responses in a stream form with the Fetch engine.

```
import AbortablePromise from 'core/promise/abortable';  
  
import request from 'core/request';  
import Response from 'core/request/response';  
  
import fetchEngine from 'core/request/engines/fetch';  
import xhrEngine from 'core/request/engines/xhr';  
  
request('//users', {  
  engine: fetchEngine,  
  credentials: 'omit'  
}).data.then(console.log);  
  
request('//users', {  
  engine: xhrEngine  
}).data.then(console.log);  
  
request('//users', {  
  engine: (params) => new AbortablePromise((resolve) => {  
    const res = new Response({  
      message: 'Hello world'  
    }, {responseType: 'object'});  
  
    resolve(res);  
  
  }, params.parent)  
  
}).data.then(console.log);
```

## Index

### References

* [CacheStrategy](src_core_request.html#CacheStrategy)
* [CacheType](src_core_request.html#CacheType)
* [CreateRequestOptions](src_core_request.html#CreateRequestOptions)
* [Decoder](src_core_request.html#Decoder)
* [Decoders](src_core_request.html#Decoders)
* [Encoder](src_core_request.html#Encoder)
* [Encoders](src_core_request.html#Encoders)
* [GlobalOptions](src_core_request.html#GlobalOptions)
* [JSONLikeValue](src_core_request.html#JSONLikeValue)
* [Middleware](src_core_request.html#Middleware)
* [MiddlewareParams](src_core_request.html#MiddlewareParams)
* [Middlewares](src_core_request.html#Middlewares)
* [NormalizedCreateRequestOptions](src_core_request.html#NormalizedCreateRequestOptions)
* [NormalizedRequestBody](src_core_request.html#NormalizedRequestBody)
* [NormalizedResponseOptions](src_core_request.html#NormalizedResponseOptions)
* [OkStatuses](src_core_request.html#OkStatuses)
* [RequestAPI](src_core_request.html#RequestAPI)
* [RequestAPIValue](src_core_request.html#RequestAPIValue)
* [RequestBody](src_core_request.html#RequestBody)
* [RequestEngine](src_core_request.html#RequestEngine)
* [RequestError](src_core_request.html#RequestError)
* [RequestFunctionResponse](src_core_request.html#RequestFunctionResponse)
* [RequestMethod](src_core_request.html#RequestMethod)
* [RequestOptions](src_core_request.html#RequestOptions)
* [RequestPromise](src_core_request.html#RequestPromise)
* [RequestQuery](src_core_request.html#RequestQuery)
* [RequestResolver](src_core_request.html#RequestResolver)
* [RequestResponse](src_core_request.html#RequestResponse)
* [RequestResponseChunk](src_core_request.html#RequestResponseChunk)
* [RequestResponseObject](src_core_request.html#RequestResponseObject)
* [ResolverResult](src_core_request.html#ResolverResult)
* [Response](src_core_request.html#Response)
* [ResponseChunk](src_core_request.html#ResponseChunk)
* [ResponseModeType](src_core_request.html#ResponseModeType)
* [ResponseOptions](src_core_request.html#ResponseOptions)
* [ResponseType](src_core_request.html#ResponseType)
* [ResponseTypeValue](src_core_request.html#ResponseTypeValue)
* [ResponseTypeValueP](src_core_request.html#ResponseTypeValueP)
* [RetryOptions](src_core_request.html#RetryOptions)
* [StreamDecoder](src_core_request.html#StreamDecoder)
* [StreamDecoders](src_core_request.html#StreamDecoders)
* [WrappedCreateRequestOptions](src_core_request.html#WrappedCreateRequestOptions)
* [WrappedDecoder](src_core_request.html#WrappedDecoder)
* [WrappedDecoders](src_core_request.html#WrappedDecoders)
* [WrappedEncoder](src_core_request.html#WrappedEncoder)
* [WrappedEncoders](src_core_request.html#WrappedEncoders)
* [WrappedStreamDecoder](src_core_request.html#WrappedStreamDecoder)
* [WrappedStreamDecoders](src_core_request.html#WrappedStreamDecoders)
* [applyQueryForStr](src_core_request.html#applyQueryForStr)
* [cache](src_core_request.html#cache)
* [default](src_core_request.html#default)
* [dropCache](src_core_request.html#dropCache)
* [getRequestKey](src_core_request.html#getRequestKey)
* [globalOpts](src_core_request.html#globalOpts)
* [merge](src_core_request.html#merge)
* [pendingCache](src_core_request.html#pendingCache)
* [tplRgxp](src_core_request.html#tplRgxp)

## References

### CacheStrategy

Re-exports [CacheStrategy](src_core_request_interface.html#CacheStrategy)

### CacheType

Re-exports [CacheType](src_core_request_interface.html#CacheType)

### CreateRequestOptions

Re-exports [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)

### Decoder

Re-exports [Decoder](../interfaces/src_core_request_interface.Decoder.html)

### Decoders

Re-exports [Decoders](src_core_request_interface.html#Decoders)

### Encoder

Re-exports [Encoder](../interfaces/src_core_request_interface.Encoder.html)

### Encoders

Re-exports [Encoders](src_core_request_interface.html#Encoders)

### GlobalOptions

Re-exports [GlobalOptions](../interfaces/src_core_request_interface.GlobalOptions.html)

### JSONLikeValue

Re-exports [JSONLikeValue](src_core_request_response_interface.html#JSONLikeValue)

### Middleware

Re-exports [Middleware](../interfaces/src_core_request_interface.Middleware.html)

### MiddlewareParams

Re-exports [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)

### Middlewares

Re-exports [Middlewares](src_core_request_interface.html#Middlewares)

### NormalizedCreateRequestOptions

Re-exports [NormalizedCreateRequestOptions](src_core_request_interface.html#NormalizedCreateRequestOptions)

### NormalizedRequestBody

Re-exports [NormalizedRequestBody](src_core_request_interface.html#NormalizedRequestBody)

### NormalizedResponseOptions

Re-exports [NormalizedResponseOptions](src_core_request_response_interface.html#NormalizedResponseOptions)

### OkStatuses

Re-exports [OkStatuses](src_core_request_interface.html#OkStatuses)

### RequestAPI

Re-exports [RequestAPI](../interfaces/src_core_request_interface.RequestAPI.html)

### RequestAPIValue

Re-exports [RequestAPIValue](src_core_request_interface.html#RequestAPIValue)

### RequestBody

Re-exports [RequestBody](src_core_request_interface.html#RequestBody)

### RequestEngine

Re-exports [RequestEngine](../interfaces/src_core_request_interface.RequestEngine.html)

### RequestError

Renames and re-exports [default](../classes/src_core_request_error.default.html)

### RequestFunctionResponse

Re-exports [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)

### RequestMethod

Re-exports [RequestMethod](src_core_request_interface.html#RequestMethod)

### RequestOptions

Re-exports [RequestOptions](../interfaces/src_core_request_interface.RequestOptions.html)

### RequestPromise

Re-exports [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)

### RequestQuery

Re-exports [RequestQuery](src_core_request_interface.html#RequestQuery)

### RequestResolver

Re-exports [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)

### RequestResponse

Re-exports [RequestResponse](src_core_request_interface.html#RequestResponse)

### RequestResponseChunk

Re-exports [RequestResponseChunk](../interfaces/src_core_request_interface.RequestResponseChunk.html)

### RequestResponseObject

Re-exports [RequestResponseObject](../interfaces/src_core_request_interface.RequestResponseObject.html)

### ResolverResult

Re-exports [ResolverResult](src_core_request_interface.html#ResolverResult)

### Response

Renames and re-exports [default](../classes/src_core_request_response.default.html)

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

### RetryOptions

Re-exports [RetryOptions](../interfaces/src_core_request_interface.RetryOptions.html)

### StreamDecoder

Re-exports [StreamDecoder](../interfaces/src_core_request_interface.StreamDecoder.html)

### StreamDecoders

Re-exports [StreamDecoders](src_core_request_interface.html#StreamDecoders)

### WrappedCreateRequestOptions

Re-exports [WrappedCreateRequestOptions](../interfaces/src_core_request_interface.WrappedCreateRequestOptions.html)

### WrappedDecoder

Re-exports [WrappedDecoder](../interfaces/src_core_request_interface.WrappedDecoder.html)

### WrappedDecoders

Re-exports [WrappedDecoders](src_core_request_interface.html#WrappedDecoders)

### WrappedEncoder

Re-exports [WrappedEncoder](../interfaces/src_core_request_interface.WrappedEncoder.html)

### WrappedEncoders

Re-exports [WrappedEncoders](src_core_request_interface.html#WrappedEncoders)

### WrappedStreamDecoder

Re-exports [WrappedStreamDecoder](../interfaces/src_core_request_interface.WrappedStreamDecoder.html)

### WrappedStreamDecoders

Re-exports [WrappedStreamDecoders](src_core_request_interface.html#WrappedStreamDecoders)

### applyQueryForStr

Re-exports [applyQueryForStr](src_core_request_helpers_interpolation.html#applyQueryForStr)

### cache

Re-exports [cache](src_core_request_const.html#cache)

### default

Renames and re-exports [\_\_type](../classes/src_core_data.default.html#__type)

### dropCache

Re-exports [dropCache](src_core_request_helpers_cache.html#dropCache)

### getRequestKey

Re-exports [getRequestKey](src_core_request_helpers_cache.html#getRequestKey)

### globalOpts

Re-exports [globalOpts](src_core_request_const.html#globalOpts)

### merge

Re-exports [merge](src_core_request_helpers_other.html#merge)

### pendingCache

Re-exports [pendingCache](src_core_request_const.html#pendingCache)

### tplRgxp

Re-exports [tplRgxp](src_core_request_helpers_const.html#tplRgxp)