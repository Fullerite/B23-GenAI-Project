# Interface WrappedCreateRequestOptions<D>
### Type parameters

* #### D = unknown

### Hierarchy

* [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html)<D>
  + WrappedCreateRequestOptions

## Index

### Properties

* [api](src_core_request_interface.WrappedCreateRequestOptions.html#api)
* [body](src_core_request_interface.WrappedCreateRequestOptions.html#body)
* [cacheId](src_core_request_interface.WrappedCreateRequestOptions.html#cacheId)
* [cacheMethods](src_core_request_interface.WrappedCreateRequestOptions.html#cacheMethods)
* [cacheStrategy](src_core_request_interface.WrappedCreateRequestOptions.html#cacheStrategy)
* [cacheTTL](src_core_request_interface.WrappedCreateRequestOptions.html#cacheTTL)
* [contentType](src_core_request_interface.WrappedCreateRequestOptions.html#contentType)
* [credentials](src_core_request_interface.WrappedCreateRequestOptions.html#credentials)
* [decoder](src_core_request_interface.WrappedCreateRequestOptions.html#decoder)
* [encoder](src_core_request_interface.WrappedCreateRequestOptions.html#encoder)
* [engine](src_core_request_interface.WrappedCreateRequestOptions.html#engine)
* [headers](src_core_request_interface.WrappedCreateRequestOptions.html#headers)
* [important](src_core_request_interface.WrappedCreateRequestOptions.html#important)
* [jsonReviver](src_core_request_interface.WrappedCreateRequestOptions.html#jsonReviver)
* [meta](src_core_request_interface.WrappedCreateRequestOptions.html#meta)
* [method](src_core_request_interface.WrappedCreateRequestOptions.html#method)
* [middlewares](src_core_request_interface.WrappedCreateRequestOptions.html#middlewares)
* [offlineCache](src_core_request_interface.WrappedCreateRequestOptions.html#offlineCache)
* [offlineCacheTTL](src_core_request_interface.WrappedCreateRequestOptions.html#offlineCacheTTL)
* [okStatuses](src_core_request_interface.WrappedCreateRequestOptions.html#okStatuses)
* [path](src_core_request_interface.WrappedCreateRequestOptions.html#path)
* [query](src_core_request_interface.WrappedCreateRequestOptions.html#query)
* [responseType](src_core_request_interface.WrappedCreateRequestOptions.html#responseType)
* [retry](src_core_request_interface.WrappedCreateRequestOptions.html#retry)
* [streamDecoder](src_core_request_interface.WrappedCreateRequestOptions.html#streamDecoder)
* [timeout](src_core_request_interface.WrappedCreateRequestOptions.html#timeout)
* [url](src_core_request_interface.WrappedCreateRequestOptions.html#url)

### Methods

* [querySerializer](src_core_request_interface.WrappedCreateRequestOptions.html#querySerializer)

## Properties

### Optional api

api?: [RequestAPI](src_core_request_interface.RequestAPI.html)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[api](src_core_request_interface.CreateRequestOptions.html#api)

* Defined in [src/core/request/interface.ts:322](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L322)

A map of API parameters.

These parameters apply if the original request URL is not absolute, and they can be used to customize the
base API URL depending on the runtime environment. If you define the base API URL via
`config#api` or `globalOpts.api`, these parameters will be mapped on it.

example
:   ```
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

### Optional body

body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[body](src_core_request_interface.CreateRequestOptions.html#body)

* Defined in [src/core/request/interface.ts:218](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L218)

Request body.
Mind, not every HTTP method can send data in this way. For instance,
GET or HEAD requests can send data only with URLs (@see `query`).

### Optional cacheId

cacheId?: string | symbol

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[cacheId](src_core_request_interface.CreateRequestOptions.html#cacheId)

* Defined in [src/core/request/interface.ts:404](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L404)

Unique cache identifier: it can be useful to create request factories with isolated cache storages

### Optional cacheMethods

cacheMethods?: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)[]

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[cacheMethods](src_core_request_interface.CreateRequestOptions.html#cacheMethods)

* Defined in [src/core/request/interface.ts:399](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L399)

List of request methods that support caching

default
:   `['GET']`

### Optional cacheStrategy

cacheStrategy?: [CacheStrategy](../modules/src_core_request_interface.html#CacheStrategy)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[cacheStrategy](src_core_request_interface.CreateRequestOptions.html#cacheStrategy)

* Defined in [src/core/request/interface.ts:350](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L350)

Strategy of caching for requests that support caching (by default, only GET requests can be cached):

1. `'forever'` - caches all requests and stores their values forever within the active session or
   until the cache expires (if `cacheTTL` is specified);
2. `'queue'` - caches all requests, but more frequent requests will push less frequent requests;
3. `'never'` - never caches any requests;
4. Or, you can pass a custom cache object.

example
:   ```
    import request, { cache } from 'core/request';  
    import RestrictedCache from 'core/cache/restricted';  
      
    request('/users', {  
      cacheStrategy: 'forever'  
    }).data.then(console.log);  
      
    request('/users', {  
      cacheStrategy: new RestrictedCache(50)  
    }).data.then(console.log);  
      
    // If you set a strategy using string identifiers, all requests will be stored within the global cache objects.  
    cache.forever.clear();
    ```

### Optional cacheTTL

cacheTTL?: number

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[cacheTTL](src_core_request_interface.CreateRequestOptions.html#cacheTTL)

* Defined in [src/core/request/interface.ts:356](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L356)

Value in milliseconds that indicates how long a request value should keep in the cache
(all requests are stored within the active session without expiring by default)

### Optional contentType

contentType?: string

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[contentType](src_core_request_interface.CreateRequestOptions.html#contentType)

* Defined in [src/core/request/interface.ts:233](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L233)

Mime type of the request data (if not specified, it will be cast dynamically)

example
:   ```
    request('//create-user', {  
      method: 'POST',  
      body: {name: 'Bob'},  
      contentType: 'application/x-msgpack',  
      encoder: toMessagePack  
    }).data.then(console.log);
    ```

### Optional credentials

credentials?: boolean | RequestCredentials

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[credentials](src_core_request_interface.CreateRequestOptions.html#credentials)

* Defined in [src/core/request/interface.ts:188](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L188)

Enables providing of credentials for cross-domain requests.
Also, you can manage to omit any credentials if the used request engine supports it.

### Optional decoder

decoder?: [WrappedDecoder](src_core_request_interface.WrappedDecoder.html)<unknown, unknown> | [WrappedDecoders](../modules/src_core_request_interface.html#WrappedDecoders)

Overrides [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[decoder](src_core_request_interface.CreateRequestOptions.html#decoder)

* Defined in [src/core/request/interface.ts:653](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L653)

A function (or a sequence of functions) takes the current request response data
and returns new data to respond. If you provide a sequence of functions,
the first function will pass a result to the next function from the sequence, etc.

### Optional encoder

encoder?: [WrappedEncoder](src_core_request_interface.WrappedEncoder.html)<unknown, unknown> | [WrappedEncoders](../modules/src_core_request_interface.html#WrappedEncoders)

Overrides [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[encoder](src_core_request_interface.CreateRequestOptions.html#encoder)

* Defined in [src/core/request/interface.ts:652](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L652)

A function (or a sequence of functions) takes the current request data
and returns new data to request. If you provide a sequence of functions,
the first function will pass a result in the next function from the sequence, etc.

### Optional engine

engine?: [RequestEngine](src_core_request_interface.RequestEngine.html)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[engine](src_core_request_interface.CreateRequestOptions.html#engine)

* Defined in [src/core/request/interface.ts:539](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L539)

A request engine to use.
The engine - is a simple function that takes request parameters and returns an abortable promise resolved with the
`core/request/response` instance. Mind, some engines provide extra features. For instance, you can listen to upload
progress events with the XHR engine. Or, you can parse responses in a stream form with the Fetch engine.

example
:   ```
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

### headers

headers: [default](../classes/src_core_request_headers.default.html)

Overrides [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[headers](src_core_request_interface.CreateRequestOptions.html#headers)

* Defined in [src/core/request/interface.ts:651](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L651)

Additional HTTP request headers.
You can provide them as a simple dictionary or an instance of the Headers class.
Also, you can pass headers as an instance of the `core/request/headers` class.

### Optional important

important?: boolean

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[important](src_core_request_interface.CreateRequestOptions.html#important)

* Defined in [src/core/request/interface.ts:499](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L499)

A meta flag that indicates that the request is important: is usually used with middlewares to indicate that
the request needs to be executed as soon as possible

example
:   ```
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

### Optional jsonReviver

jsonReviver?: false | [JSONCb](index.JSONCb.html)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[jsonReviver](src_core_request_interface.CreateRequestOptions.html#jsonReviver)

* Defined in [src/core/request/interface.ts:472](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L472)

Reviver function for `JSON.parse` or false to disable defaults.
By default, it parses some strings as Date instances.

default
:   `convertIfDate`

### Optional meta

meta?: [Dictionary](index.Dictionary.html)<unknown>

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[meta](src_core_request_interface.CreateRequestOptions.html#meta)

* Defined in [src/core/request/interface.ts:478](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L478)

A dictionary with some extra parameters for the request: is usually used with middlewares to provide
domain-specific information

### Optional method

method?: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[method](src_core_request_interface.CreateRequestOptions.html#method)

* Defined in [src/core/request/interface.ts:173](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L173)

HTTP method to create a request

see
:   <https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods>

### Optional middlewares

middlewares?: [Middlewares](../modules/src_core_request_interface.html#Middlewares)<D>

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[middlewares](src_core_request_interface.CreateRequestOptions.html#middlewares)

* Defined in [src/core/request/interface.ts:442](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L442)

A dictionary or iterable value with middleware functions:
functions take an environment of request parameters and can modify theirs.

Please notice that the order of middleware depends on the structure you use.
Also, if at least one of the middlewares returns a function, invoking this function
will be returned as the request result. It can be helpful to organize mocks of data and
other similar cases when you don't want to execute a real request.

example
:   ```
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

### Optional offlineCache

offlineCache?: boolean

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[offlineCache](src_core_request_interface.CreateRequestOptions.html#offlineCache)

* Defined in [src/core/request/interface.ts:387](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L387)

Enables support of offline caching.
By default, a request can only be taken from a cache if there is no network.
You can customize this logic by providing a custom cache object with the `core/cache/decorators/persistent`
decorator.

default
:   `false`

example
:   ```
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

### Optional offlineCacheTTL

offlineCacheTTL?: number

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[offlineCacheTTL](src_core_request_interface.CreateRequestOptions.html#offlineCacheTTL)

* Defined in [src/core/request/interface.ts:393](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L393)

Value in milliseconds that indicates how long a request value should keep in the offline cache

default
:   `(1).day()`

### Optional okStatuses

okStatuses?: [OkStatuses](../modules/src_core_request_interface.html#OkStatuses)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[okStatuses](src_core_request_interface.CreateRequestOptions.html#okStatuses)

* Defined in [src/core/request/interface.ts:263](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L263)

A list of status codes (or a single code) that match successful operation.
Also, you can pass a range of codes.

default
:   `new Range(200, 299)`

### path

path: [CanUndef](../modules/index.html#CanUndef)<string>

* Defined in [src/core/request/interface.ts:649](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L649)

Original path that was passed into the request function

### Optional query

query?: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[query](src_core_request_interface.CreateRequestOptions.html#query)

* Defined in [src/core/request/interface.ts:194](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L194)

Request parameters that will be serialized to a string and passed via a request URL.
To customize how to encode data to a query string, see `querySerializer`.

### Optional responseType

responseType?: [ResponseType](../modules/src_core_request_response_interface.html#ResponseType)

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[responseType](src_core_request_interface.CreateRequestOptions.html#responseType)

* Defined in [src/core/request/interface.ts:255](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L255)

Type of the response data
(if not specified, it will be cast dynamically from the response headers):

1. `'text'` - result is interpreted as a simple string;
2. `'json'` - result is interpreted as a JSON object;
3. `'document'` - result is interpreted as an XML/HTML document;
4. `'formData'` - result is interpreted as a FormData object;
5. `'blob'` - result is interpreted as a Blob object;
6. `'arrayBuffer'` - result is interpreted as a raw array buffer;
7. `'object'` - result is interpreted "as is" without any converting.

example
:   ```
    request('//users', {  
      responseType: 'arrayBuffer',  
      decoder: fromMessagePack  
    }).data.then(console.log);
    ```

### Optional retry

retry?: number | [RetryOptions](src_core_request_interface.RetryOptions.html)<unknown>

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[retry](src_core_request_interface.CreateRequestOptions.html#retry)

* Defined in [src/core/request/interface.ts:289](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L289)

Options to retry bad requests or a number of maximum request retries

example
:   ```
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

### Optional streamDecoder

streamDecoder?: [WrappedStreamDecoder](src_core_request_interface.WrappedStreamDecoder.html)<unknown, unknown> | [WrappedStreamDecoders](../modules/src_core_request_interface.html#WrappedStreamDecoders)

Overrides [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[streamDecoder](src_core_request_interface.CreateRequestOptions.html#streamDecoder)

* Defined in [src/core/request/interface.ts:654](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L654)

A function (or a sequence of functions) takes the current request response data chunk
and yields a new chunk to respond via an async iterator. If you provide a sequence of functions,
the first function will pass a result to the next function from the sequence, etc.
This parameter is used when you're parsing responses in a stream form.

### Optional timeout

timeout?: number

Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[timeout](src_core_request_interface.CreateRequestOptions.html#timeout)

* Defined in [src/core/request/interface.ts:268](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L268)

Value in milliseconds for a request timeout

### url

url: [CanUndef](../modules/index.html#CanUndef)<string>

* Defined in [src/core/request/interface.ts:644](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L644)

URL to make request

## Methods

### Optional querySerializer

* querySerializer(query: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)): string

* Inherited from [CreateRequestOptions](src_core_request_interface.CreateRequestOptions.html).[querySerializer](src_core_request_interface.CreateRequestOptions.html#querySerializer)

  + Defined in [src/core/request/interface.ts:211](https://github.com/V4Fire/Core/blob/master/src/core/request/interface.ts#L211)

  Returns a serialized value of the specified query object

  example
  :   ```
      import request from 'core/request';  
      import { toQueryString } from 'core/url';  
        
      request('//user', {  
        query: {ids: [125, 35, 454]},  
        querySerializer: (data) => toQueryString(data, {arraySyntax: true})  
      }).data.then(console.log);
      ```

  #### Parameters

  + ##### query: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)

  #### Returns string