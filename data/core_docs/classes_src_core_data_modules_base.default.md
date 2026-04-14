# Class default
### Hierarchy

* [default](src_core_data_modules_params.default.html)
  + default
    - [default](src_core_data.default.html)

### Implements

* [Provider](../interfaces/src_core_data_interface.Provider.html)

## Index

### Constructors

* [constructor](src_core_data_modules_base.default.html#constructor)

### Properties

* [addMethod](src_core_data_modules_base.default.html#addMethod)
* [advURL](src_core_data_modules_base.default.html#advURL)
* [alias](src_core_data_modules_base.default.html#alias)
* [async](src_core_data_modules_base.default.html#async)
* [baseAddURL](src_core_data_modules_base.default.html#baseAddURL)
* [baseDelURL](src_core_data_modules_base.default.html#baseDelURL)
* [baseGetURL](src_core_data_modules_base.default.html#baseGetURL)
* [basePeekURL](src_core_data_modules_base.default.html#basePeekURL)
* [baseURL](src_core_data_modules_base.default.html#baseURL)
* [baseUpdURL](src_core_data_modules_base.default.html#baseUpdURL)
* [cacheId](src_core_data_modules_base.default.html#cacheId)
* [connection](src_core_data_modules_base.default.html#connection)
* [customMethod](src_core_data_modules_base.default.html#customMethod)
* [delMethod](src_core_data_modules_base.default.html#delMethod)
* [emitter](src_core_data_modules_base.default.html#emitter)
* [eventName](src_core_data_modules_base.default.html#eventName)
* [extraProviders](src_core_data_modules_base.default.html#extraProviders)
* [getMethod](src_core_data_modules_base.default.html#getMethod)
* [globalEmitter](src_core_data_modules_base.default.html#globalEmitter)
* [mocks](src_core_data_modules_base.default.html#mocks)
* [peekMethod](src_core_data_modules_base.default.html#peekMethod)
* [socketURL](src_core_data_modules_base.default.html#socketURL)
* [updMethod](src_core_data_modules_base.default.html#updMethod)
* [decoders](src_core_data_modules_base.default.html#decoders)
* [encoders](src_core_data_modules_base.default.html#encoders)
* [middlewares](src_core_data_modules_base.default.html#middlewares)
* [mocks](src_core_data_modules_base.default.html#mocks-1)
* [request](src_core_data_modules_base.default.html#request)

### Accessors

* [event](src_core_data_modules_base.default.html#event)
* [globalEvent](src_core_data_modules_base.default.html#globalEvent)
* [providerName](src_core_data_modules_base.default.html#providerName)
* [request](src_core_data_modules_base.default.html#request-1)

### Methods

* [add](src_core_data_modules_base.default.html#add)
* [base](src_core_data_modules_base.default.html#base)
* [connect](src_core_data_modules_base.default.html#connect)
* [del](src_core_data_modules_base.default.html#del)
* [delete](src_core_data_modules_base.default.html#delete)
* [dropCache](src_core_data_modules_base.default.html#dropCache)
* [get](src_core_data_modules_base.default.html#get)
* [getAuthParams](src_core_data_modules_base.default.html#getAuthParams)
* [getCacheKey](src_core_data_modules_base.default.html#getCacheKey)
* [getEventKey](src_core_data_modules_base.default.html#getEventKey)
* [getRequestOptions](src_core_data_modules_base.default.html#getRequestOptions)
* [initSocketBehaviour](src_core_data_modules_base.default.html#initSocketBehaviour)
* [method](src_core_data_modules_base.default.html#method)
* [name](src_core_data_modules_base.default.html#name)
* [peek](src_core_data_modules_base.default.html#peek)
* [post](src_core_data_modules_base.default.html#post)
* [resolveURL](src_core_data_modules_base.default.html#resolveURL)
* [resolver](src_core_data_modules_base.default.html#resolver)
* [setReadonlyParam](src_core_data_modules_base.default.html#setReadonlyParam)
* [upd](src_core_data_modules_base.default.html#upd)
* [update](src_core_data_modules_base.default.html#update)
* [updateRequest](src_core_data_modules_base.default.html#updateRequest)
* [url](src_core_data_modules_base.default.html#url)
* [select](src_core_data_modules_base.default.html#select)

## Constructors

### Protected constructor

* new default(opts?: [ProviderOptions](../interfaces/src_core_data_interface_types.ProviderOptions.html)): [default](src_core_data_modules_base.default.html)

* Overrides [default](src_core_data_modules_params.default.html).[constructor](src_core_data_modules_params.default.html#constructor)

  + Defined in [src/core/data/modules/base.ts:105](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L105)

  #### Parameters

  + ##### opts: [ProviderOptions](../interfaces/src_core_data_interface_types.ProviderOptions.html) = {}

  #### Returns [default](src_core_data_modules_base.default.html)

## Properties

### addMethod

addMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'POST'

Inherited from [default](src_core_data_modules_params.default.html).[addMethod](src_core_data_modules_params.default.html#addMethod)

* Defined in [src/core/data/modules/params.ts:325](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L325)

Default HTTP request method for the "add" method

### advURL

advURL: string = ''

Inherited from [default](src_core_data_modules_params.default.html).[advURL](src_core_data_modules_params.default.html#advURL)

* Defined in [src/core/data/modules/params.ts:212](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L212)

Advanced part of URL for a request of all request methods
(it is concatenated with the base part)

### Optional Readonly alias

alias?: string

Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[alias](../interfaces/src_core_data_interface.Provider.html#alias)

* Defined in [src/core/data/modules/base.ts:76](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L76)

Provider alias

### Protected Readonly async

async: [default](src_core_async.default.html)<[default](src_core_data_modules_base.default.html)>

* Defined in [src/core/data/modules/base.ts:95](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L95)

API for async operations

### Optional baseAddURL

baseAddURL?: string

Inherited from [default](src_core_data_modules_params.default.html).[baseAddURL](src_core_data_modules_params.default.html#baseAddURL)

* Defined in [src/core/data/modules/params.ts:259](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L259)

Base part of URL for a request for the "add" method

example
:   ```
    class Profile extends Provider {  
      // baseURL request methods despite the "add" is used this URL  
      basePeekURL: 'profile/info'  
      baseAddURL: 'profile/info/add'  
    }
    ```

### Optional baseDelURL

baseDelURL?: string

Inherited from [default](src_core_data_modules_params.default.html).[baseDelURL](src_core_data_modules_params.default.html#baseDelURL)

* Defined in [src/core/data/modules/params.ts:287](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L287)

Base part of URL for a request for the "del" method

example
:   ```
    class Profile extends Provider {  
      // baseURL request methods despite the "del" is used this URL  
      basePeekURL: 'profile/info'  
      baseDelURL: 'profile/info/del'  
    }
    ```

### Optional baseGetURL

baseGetURL?: string

Inherited from [default](src_core_data_modules_params.default.html).[baseGetURL](src_core_data_modules_params.default.html#baseGetURL)

* Defined in [src/core/data/modules/params.ts:231](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L231)

Base part of URL for a request for the "get" method

example
:   ```
    class Profile extends Provider {  
      // For all request methods despite the "get" is used this URL  
      baseURL: 'profile/info'  
      baseGetURL: 'profile/info/get'  
    }
    ```

### Optional basePeekURL

basePeekURL?: string

Inherited from [default](src_core_data_modules_params.default.html).[basePeekURL](src_core_data_modules_params.default.html#basePeekURL)

* Defined in [src/core/data/modules/params.ts:245](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L245)

Base part of URL for a request for the "peek" method

example
:   ```
    class Profile extends Provider {  
      // For all request methods despite the "peek" is used this URL  
      baseURL: 'profile/info'  
      basePeekURL: 'profile/info/peek'  
    }
    ```

### baseURL

baseURL: string = ''

Inherited from [default](src_core_data_modules_params.default.html).[baseURL](src_core_data_modules_params.default.html#baseURL)

* Defined in [src/core/data/modules/params.ts:206](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L206)

Base part of URL for a request of all request methods

example
:   ```
    class Profile extends Provider {  
      baseURL: 'profile/info'  
    }
    ```

### Optional baseUpdURL

baseUpdURL?: string

Inherited from [default](src_core_data_modules_params.default.html).[baseUpdURL](src_core_data_modules_params.default.html#baseUpdURL)

* Defined in [src/core/data/modules/params.ts:273](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L273)

Base part of URL for a request for the "upd" method

example
:   ```
    class Profile extends Provider {  
      // baseURL request methods despite the "upd" is used this URL  
      basePeekURL: 'profile/info'  
      baseUpdURL: 'profile/info/upd'  
    }
    ```

### Readonly cacheId

cacheId: string

* Defined in [src/core/data/modules/base.ts:73](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L73)

Cache identifier

### Protected Optional connection

connection?: Promise<[Socket](../modules/src_core_socket_interface.html#Socket)>

* Defined in [src/core/data/modules/base.ts:100](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L100)

Socket connection

### customMethod

customMethod: [CanUndef](../modules/index.html#CanUndef)<[RequestMethod](../modules/src_core_request_interface.html#RequestMethod)>

Inherited from [default](src_core_data_modules_params.default.html).[customMethod](src_core_data_modules_params.default.html#customMethod)

* Defined in [src/core/data/modules/params.ts:341](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L341)

HTTP request method for all request methods.
This parameter will override other method parameters, such as "getMethod" or "delMethod".

### delMethod

delMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'DELETE'

Inherited from [default](src_core_data_modules_params.default.html).[delMethod](src_core_data_modules_params.default.html#delMethod)

* Defined in [src/core/data/modules/params.ts:335](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L335)

Default HTTP request method for the "del" method

### Readonly emitter

emitter: EventEmitter2

Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[emitter](../interfaces/src_core_data_interface.Provider.html#emitter)

* Defined in [src/core/data/modules/base.ts:79](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L79)

Event emitter to broadcast provider events

### eventName

eventName: [CanUndef](../modules/index.html#CanUndef)<[ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)>

Inherited from [default](src_core_data_modules_params.default.html).[eventName](src_core_data_modules_params.default.html#eventName)

* Defined in [src/core/data/modules/params.ts:347](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L347)

Event name for requests.
Please notice that all request methods except "get", "peek" and "request" emit events by default.

### Optional extraProviders

extraProviders?: [FunctionalExtraProviders](../modules/src_core_data_interface_types.html#FunctionalExtraProviders)<unknown>

Inherited from [default](src_core_data_modules_params.default.html).[extraProviders](src_core_data_modules_params.default.html#extraProviders)

* Defined in [src/core/data/modules/params.ts:310](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L310)

List of additional data providers for the "get" method.
It can be useful if you have some providers that you want combine to one.

example
:   ```
    class User extends Provider {  
      baseURL: 'user/info',  
      
      extraProviders: {  
        balance: {  
          provider: 'UserBalance'  
        },  
      
        hobby: {  
          provider: 'UserHobby'  
        },  
      }  
    }
    ```

### getMethod

getMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'GET'

Inherited from [default](src_core_data_modules_params.default.html).[getMethod](src_core_data_modules_params.default.html#getMethod)

* Defined in [src/core/data/modules/params.ts:315](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L315)

Default HTTP request method for the "get" method

### Readonly globalEmitter

globalEmitter: EventEmitter2 = emitter

Inherited from [default](src_core_data_modules_params.default.html).[globalEmitter](src_core_data_modules_params.default.html#globalEmitter)

* Defined in [src/core/data/modules/params.ts:194](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L194)

Global event emitter to broadcast provider events

### Optional mocks

mocks?: [Mocks](../modules/src_core_data_interface_types.html#Mocks)

Inherited from [default](src_core_data_modules_params.default.html).[mocks](src_core_data_modules_params.default.html#mocks)

* Defined in [src/core/data/modules/params.ts:353](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L353)

deprecated

see
:   [[Provider.mocks]]

### peekMethod

peekMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'HEAD'

Inherited from [default](src_core_data_modules_params.default.html).[peekMethod](src_core_data_modules_params.default.html#peekMethod)

* Defined in [src/core/data/modules/params.ts:320](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L320)

Default HTTP request method for the "peek" method

### Optional socketURL

socketURL?: string

Inherited from [default](src_core_data_modules_params.default.html).[socketURL](src_core_data_modules_params.default.html#socketURL)

* Defined in [src/core/data/modules/params.ts:217](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L217)

URL for a socket connection

### updMethod

updMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'PUT'

Inherited from [default](src_core_data_modules_params.default.html).[updMethod](src_core_data_modules_params.default.html#updMethod)

* Defined in [src/core/data/modules/params.ts:330](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L330)

Default HTTP request method for the "upd" method

### Static Readonly decoders

decoders: [DecodersMap](../modules/src_core_data_interface_types.html#DecodersMap) = {}

Inherited from [default](src_core_data_modules_params.default.html).[decoders](src_core_data_modules_params.default.html#decoders)

* Defined in [src/core/data/modules/params.ts:111](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L111)

Map of data decoder sequences.
The key of a map element represent a name of the provider method: 'get', 'post', etc.
The value of a map element represent a sequence of decoders for the specified provider method.

see
:   [Decoders](../modules/src_core_request_interface.html#Decoders)

example
:   ```
    class MyProvider extends Provider {  
      static decoders = {  
        get: [fromJSON],  
        upd: [fromBuffer]  
      };  
    }
    ```

### Static Readonly encoders

encoders: [EncodersMap](../modules/src_core_data_interface_types.html#EncodersMap) = {}

Inherited from [default](src_core_data_modules_params.default.html).[encoders](src_core_data_modules_params.default.html#encoders)

* Defined in [src/core/data/modules/params.ts:93](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L93)

Map of data encoder sequences.
The key of a map element represent a name of the provider method: 'get', 'post', etc.
The value of a map element represent a sequence of encoders for the specified provider method.

see
:   [Encoders](../modules/src_core_request_interface.html#Encoders)

example
:   ```
    class MyProvider extends Provider {  
      static encoders = {  
        get: [convertToJSON],  
        upd: [convertToBuffer]  
      };  
    }
    ```

### Static Readonly middlewares

middlewares: [Middlewares](../modules/src_core_request_interface.html#Middlewares)<unknown> = {}

Inherited from [default](src_core_data_modules_params.default.html).[middlewares](src_core_data_modules_params.default.html#middlewares)

* Defined in [src/core/data/modules/params.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L75)

Sequence of middlewares that is provided to the request function.
An object form is easily to extend, bur you can choose any different form.

see
:   [Middlewares](../modules/src_core_request_interface.html#Middlewares)

example
:   ```
    import request from 'core/request';  
      
    class Parent extends Provider {  
      static middlewares = {  
        attachGeoCoords() { ... }  
      };  
    }  
      
    class Children extends Parent {  
      static middlewares = {  
        ...Parent.middlewares,  
        addSession() {  
          ...  
        }  
      };  
    }
    ```

### Static Optional mocks

mocks?: [Mocks](../modules/src_core_data_interface_types.html#Mocks)

Inherited from [default](src_core_data_modules_params.default.html).[mocks](src_core_data_modules_params.default.html#mocks-1)

* Defined in [src/core/data/modules/params.ts:173](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L173)

Map of data mocks.
This object can be used with a middleware that implements API for data mocking,
for example [attachMock](../modules/src_core_data_middlewares_attach_mock.html#attachMock) from `'core/data/middlewares'`.

The key of a map element represent a method request type: 'GET', 'POST', etc.
The value of a map element represent a list of parameters to match.

see
:   [Middlewares](../modules/src_core_request_interface.html#Middlewares)

example
:   ```
    import { attachMock } from 'core/data/middlewares';  
      
    class MyProvider extends Provider {  
      static mocks = {  
        GET: [  
          // The mock for a GET request with a query parameter that contains  
          // `search=foo` parameter  
          {  
            status: 200,  
      
            // For the mock response won't be applied decoders  
            // (by default, `true`)  
            decoders: false,  
      
            query: {  
              search: 'foo'  
            },  
      
            // The response  
            response: {  
              data: [  
                'bla',  
                'baz  
              ]  
            }  
          }  
        ],  
      
        POST: [  
          // The mock is catches all POST requests and dynamically generated responses  
          {  
            response(params, response) {  
              if (!params.opts.query?.data) {  
                response.status = 400;  
                return;  
              }  
      
              response.status = 200;  
              response.responseType = 'string';  
              return 'ok';  
            }  
          }  
        ]  
      };  
      
      static middlewares = {attachMock};  
    }
    ```

### Static Readonly request

request: { <D>(path: string, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>; <D>(opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): typeof [\_\_type](src_core_data.default.html#__type); <D, A>(path: string, resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer  V[] ? V[] : unknown[]> } = request

Inherited from [default](src_core_data_modules_params.default.html).[request](src_core_data_modules_params.default.html#request)

* Defined in [src/core/data/modules/params.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L48)

Transport function for a request.
Basically, you can use an overload of the request API for flexibly extending.

#### Type declaration

* + <D>(path: string, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>
  + <D>(opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): typeof [\_\_type](src_core_data.default.html#__type)
  + <D, A>(path: string, resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer  V[] ? V[] : unknown[]>
  + Creates a new remote request with the specified options

    example
    :   ```
        request('bla/get').then(({data, response}) => {  
          console.log(data, response.status);  
        });
        ```

    #### Type parameters

    - #### D = unknown

    #### Parameters

    - ##### path: string

      request path URL
    - ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

      request options

    #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>
  + Returns a wrapped request constructor with the specified options.
    This overload helps to organize the "builder" pattern.

    example
    :   ```
        request({okStatuses: 200})({method: 'POST'})('bla/get').then(({data, response}) => {  
          console.log(data, response.status);  
        });
        ```

    #### Type parameters

    - #### D = unknown

    #### Parameters

    - ##### opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

      request options

    #### Returns typeof [\_\_type](src_core_data.default.html#__type)
  + Returns a function to create a new remote request with the specified options.
    This overload helps to create a factory of requests.

    example
    :   ```
        // Modifying the current URL  
        request('https://foo.com', (url, env, ...args) => args.join('/'))('bla', 'baz') // https://foo.com/bla/baz  
          
        // Replacing the current URL  
        request('https://foo.com', () => ['https://bla.com', 'bla', 'baz'])() // https://bla.com/bla/baz
        ```

    #### Type parameters

    - #### D = unknown
    - #### A: any[] = unknown[]

    #### Parameters

    - ##### path: string

      request path URL
    - ##### resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>

      function to resolve a request: it takes a request URL, request environment, and arguments
      from invoking the outer function and can modify some request parameters.
      Also, if the function returns a new string, the string will be appended to the request URL, or
      if the function returns a string wrapped with an array, the string fully overrides the original URL.
    - ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

      request options

    #### Returns [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer V[] ? V[] : unknown[]>

## Accessors

### event

* get event(): EventEmitter2

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[event](../interfaces/src_core_data_interface.Provider.html#event)

  + Defined in [src/core/data/modules/base.ts:87](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L87)

  #### Returns EventEmitter2

### globalEvent

* get globalEvent(): EventEmitter2

* Inherited from ParamsProvider.globalEvent

  + Defined in [src/core/data/modules/params.ts:359](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L359)

  deprecated

  see
  :   [[Provider.globalEmitter]]

  #### Returns EventEmitter2

### providerName

* get providerName(): string

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[providerName](../interfaces/src_core_data_interface.Provider.html#providerName)

  + Defined in [src/core/data/modules/base.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L82)

  Full name of the provider including a namespace

  #### Returns string

### request

* get request(): { <D>(path: string, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>; <D>(opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): typeof [\_\_type](src_core_data.default.html#__type); <D, A>(path: string, resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer  V[] ? V[] : unknown[]> }

* Inherited from ParamsProvider.request

  + Defined in [src/core/data/modules/params.ts:367](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L367)

  Alias for the request function

  #### Returns { <D>(path: string, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>; <D>(opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): typeof [\_\_type](src_core_data.default.html#__type); <D, A>(path: string, resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer V[] ? V[] : unknown[]> }

  + - <D>(path: string, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>
    - <D>(opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): typeof [\_\_type](src_core_data.default.html#__type)
    - <D, A>(path: string, resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer  V[] ? V[] : unknown[]>
    - Creates a new remote request with the specified options

      example
      :   ```
          request('bla/get').then(({data, response}) => {  
            console.log(data, response.status);  
          });
          ```

      #### Type parameters

      * #### D = unknown

      #### Parameters

      * ##### path: string

        request path URL
      * ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

        request options

      #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>
    - Returns a wrapped request constructor with the specified options.
      This overload helps to organize the "builder" pattern.

      example
      :   ```
          request({okStatuses: 200})({method: 'POST'})('bla/get').then(({data, response}) => {  
            console.log(data, response.status);  
          });
          ```

      #### Type parameters

      * #### D = unknown

      #### Parameters

      * ##### opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

        request options

      #### Returns typeof [\_\_type](src_core_data.default.html#__type)
    - Returns a function to create a new remote request with the specified options.
      This overload helps to create a factory of requests.

      example
      :   ```
          // Modifying the current URL  
          request('https://foo.com', (url, env, ...args) => args.join('/'))('bla', 'baz') // https://foo.com/bla/baz  
            
          // Replacing the current URL  
          request('https://foo.com', () => ['https://bla.com', 'bla', 'baz'])() // https://bla.com/bla/baz
          ```

      #### Type parameters

      * #### D = unknown
      * #### A: any[] = unknown[]

      #### Parameters

      * ##### path: string

        request path URL
      * ##### resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>

        function to resolve a request: it takes a request URL, request environment, and arguments
        from invoking the outer function and can modify some request parameters.
        Also, if the function returns a new string, the string will be appended to the request URL, or
        if the function returns a string wrapped with an array, the string fully overrides the original URL.
      * ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

        request options

      #### Returns [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer V[] ? V[] : unknown[]>

## Methods

### add

* add<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[add](../interfaces/src_core_data_interface.Provider.html#add)

  + Defined in [src/core/data/modules/base.ts:469](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L469)

  Add new data to the provider.
  This method is similar for a POST request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### base

* base(): string
* base(value: string): [default](src_core_data_modules_base.default.html)

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[base](../interfaces/src_core_data_interface.Provider.html#base)

  + Defined in [src/core/data/modules/base.ts:232](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L232)

  Returns the base part of URL of any request

  #### Returns string
* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[base](../interfaces/src_core_data_interface.Provider.html#base)

  + Defined in [src/core/data/modules/base.ts:235](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L235)

  Sets the base part of URL for any request.
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: string

  #### Returns [default](src_core_data_modules_base.default.html)

### connect

* connect(opts?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): Promise<[Socket](../modules/src_core_socket_interface.html#Socket)>

* + Defined in [src/core/data/modules/base.ts:165](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L165)

  Connects to a socket server and returns the connection

  #### Parameters

  + ##### Optional opts: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

  #### Returns Promise<[Socket](../modules/src_core_socket_interface.html#Socket)>

### del

* del<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[del](../interfaces/src_core_data_interface.Provider.html#del)

  + Defined in [src/core/data/modules/base.ts:517](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L517)

  Deletes data of the provider by a query.
  This method is similar for a DELETE request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### delete

* delete<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/modules/base.ts:512](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L512)

  alias

  see
  :   [Provider.del](../interfaces/src_core_data_interface.Provider.html#del)

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### dropCache

* dropCache(): void

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[dropCache](../interfaces/src_core_data_interface.Provider.html#dropCache)

  + Defined in [src/core/data/modules/base.ts:270](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L270)

  Drops the request cache of the current provider

  #### Returns void

### get

* get<D>(query?: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[get](../interfaces/src_core_data_interface.Provider.html#get)

  + Defined in [src/core/data/modules/base.ts:289](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L289)

  Requests the provider for data by a query.
  This method is similar for a GET request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional query: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### getAuthParams

* getAuthParams(params?: [Dictionary](../interfaces/index.Dictionary.html)<unknown>): Promise<[Dictionary](../interfaces/index.Dictionary.html)<unknown>>

* + Defined in [src/core/data/modules/base.ts:141](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L141)

  Returns an object with authentication parameters

  #### Parameters

  + ##### Optional params: [Dictionary](../interfaces/index.Dictionary.html)<unknown>

    additional parameters

  #### Returns Promise<[Dictionary](../interfaces/index.Dictionary.html)<unknown>>

### getCacheKey

* getCacheKey(paramsForCache?: [ProviderOptions](../interfaces/src_core_data_interface_types.ProviderOptions.html)): string

* + Defined in [src/core/data/modules/base.ts:132](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L132)

  Returns a key to the class instance cache

  #### Parameters

  + ##### paramsForCache: [ProviderOptions](../interfaces/src_core_data_interface_types.ProviderOptions.html) = {}

  #### Returns string

### Protected getEventKey

* getEventKey(event: string, data: unknown): unknown

* + Defined in [src/core/data/modules/base.ts:561](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L561)

  Returns an event cache key by the specified parameters

  #### Parameters

  + ##### event: string

    event name
  + ##### data: unknown

    event data

  #### Returns unknown

### Protected getRequestOptions

* getRequestOptions<D>(method: [ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod), params?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

* + Defined in [src/core/data/modules/base.ts:575](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L575)

  Returns an object with request options by the specified model name and object with additional parameters

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### method: [ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)

    model method
  + ##### Optional params: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

### Protected initSocketBehaviour

* initSocketBehaviour(): Promise<void>

* + Defined in [src/core/data/modules/base.ts:692](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L692)

  Initializes the socket behaviour after successful connecting

  #### Returns Promise<void>

### method

* method(): [CanUndef](../modules/index.html#CanUndef)<[RequestMethod](../modules/src_core_request_interface.html#RequestMethod)>
* method(value: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)): [default](src_core_data_modules_base.default.html)

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[method](../interfaces/src_core_data_interface.Provider.html#method)

  + Defined in [src/core/data/modules/base.ts:217](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L217)

  Returns the custom HTTP request method of any request

  #### Returns [CanUndef](../modules/index.html#CanUndef)<[RequestMethod](../modules/src_core_request_interface.html#RequestMethod)>
* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[method](../interfaces/src_core_data_interface.Provider.html#method)

  + Defined in [src/core/data/modules/base.ts:220](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L220)

  Sets the custom HTTP request method for any request.
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod)

  #### Returns [default](src_core_data_modules_base.default.html)

### name

* name(): [CanUndef](../modules/index.html#CanUndef)<[ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)>
* name(value: [ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)): [default](src_core_data_modules_base.default.html)

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[name](../interfaces/src_core_data_interface.Provider.html#name)

  + Defined in [src/core/data/modules/base.ts:202](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L202)

  Returns the custom logical name of any request.
  If a request has the name, then it will fire an event with the same name after successful receiving.

  #### Returns [CanUndef](../modules/index.html#CanUndef)<[ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)>
* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[name](../interfaces/src_core_data_interface.Provider.html#name)

  + Defined in [src/core/data/modules/base.ts:205](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L205)

  Sets the custom logical name for any request.
  If a request has the name, then it will fire an event with the same name after successful receiving.
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: [ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)

  #### Returns [default](src_core_data_modules_base.default.html)

### peek

* peek<D>(query?: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[peek](../interfaces/src_core_data_interface.Provider.html#peek)

  + Defined in [src/core/data/modules/base.ts:429](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L429)

  Checks accessibility of the provider by a query.
  This method is similar for a HEAD request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional query: [RequestQuery](../modules/src_core_request_interface.html#RequestQuery)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### post

* post<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[post](../interfaces/src_core_data_interface.Provider.html#post)

  + Defined in [src/core/data/modules/base.ts:449](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L449)

  Sends custom data to the provider without any logically effect.
  This method is similar for a POST request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### Protected resolveURL

* resolveURL(baseURL?: [Nullable](../modules/index.html#Nullable)<string>, advURL?: [Nullable](../modules/index.html#Nullable)<string>): string

* + Defined in [src/core/data/modules/base.ts:538](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L538)

  Returns full request URL by the specified URL chunks

  #### Parameters

  + ##### Optional baseURL: [Nullable](../modules/index.html#Nullable)<string>
  + ##### Optional advURL: [Nullable](../modules/index.html#Nullable)<string>

  #### Returns string

### resolver

* resolver<T>(url: string, params: [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)<T>): [ResolverResult](../modules/src_core_request_interface.html#ResolverResult)

* + Defined in [src/core/data/modules/base.ts:157](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L157)

  Function to resolve a request: it takes a request URL and request environment
  and can modify some request parameters.

  Also, if the function returns a new string, the string will be appended to the request URL, or
  if the function returns a string that wrapped with an array, the string fully override the original URL.

  see
  :   [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### url: string

    request URL
  + ##### params: [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)<T>

    request parameters

  #### Returns [ResolverResult](../modules/src_core_request_interface.html#ResolverResult)

### Protected setReadonlyParam

* setReadonlyParam(key: string, val: unknown): void

* + Defined in [src/core/data/modules/base.ts:545](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L545)

  Sets a readonly value by the specified key to the current provider

  #### Parameters

  + ##### key: string
  + ##### val: unknown

  #### Returns void

### upd

* upd<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[upd](../interfaces/src_core_data_interface.Provider.html#upd)

  + Defined in [src/core/data/modules/base.ts:493](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L493)

  Updates data of the provider by a query.
  This method is similar for a PUT request.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### update

* update<D>(body?: [RequestBody](../modules/src_core_request_interface.html#RequestBody), opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/modules/base.ts:488](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L488)

  alias

  see
  :   [Provider.upd](../interfaces/src_core_data_interface.Provider.html#upd)

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### Optional body: [RequestBody](../modules/src_core_request_interface.html#RequestBody)
  + ##### Optional opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### Protected updateRequest

* updateRequest<D>(url: string, factory: [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, unknown[]>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>
* updateRequest<D>(url: string, event: string, factory: [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, unknown[]>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

* + Defined in [src/core/data/modules/base.ts:619](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L619)

  Updates the specified request with adding caching, etc.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### url: string

    request url
  + ##### factory: [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, unknown[]>

    request factory

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>
* + Defined in [src/core/data/modules/base.ts:628](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L628)

  Updates the specified request with adding caching, etc.

  #### Type parameters

  + #### D = unknown

  #### Parameters

  + ##### url: string

    request url
  + ##### event: string

    event name that is fired after resolving of the request
  + ##### factory: [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, unknown[]>

    request factory

  #### Returns [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>

### url

* url(): string
* url(value: string): [default](src_core_data_modules_base.default.html)

* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[url](../interfaces/src_core_data_interface.Provider.html#url)

  + Defined in [src/core/data/modules/base.ts:255](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L255)

  Returns the full URL of any request

  #### Returns string
* Implementation of [Provider](../interfaces/src_core_data_interface.Provider.html).[url](../interfaces/src_core_data_interface.Provider.html#url)

  + Defined in [src/core/data/modules/base.ts:258](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/base.ts#L258)

  Sets an extra URL part for any request (it is concatenated with the base part of URL).
  This method returns a new provider object with context.

  #### Parameters

  + ##### value: string

  #### Returns [default](src_core_data_modules_base.default.html)

### Static select

* select<T>(obj: unknown, params: [SelectParams](../interfaces/src_core_object_select_interface.SelectParams.html)): [CanUndef](../modules/index.html#CanUndef)<T>

* Inherited from [default](src_core_data_modules_params.default.html).[select](src_core_data_modules_params.default.html#select)

  + Defined in [src/core/data/modules/params.ts:187](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L187)

  Finds an element from an object by the specified parameters

  example
  :   ```
      class MyProvider extends Provider {}  
      MyProvider.select([{test: 1}], {where: {test: 1}}) // {test: 1}
      ```

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### obj: unknown

    object to search
  + ##### params: [SelectParams](../interfaces/src_core_object_select_interface.SelectParams.html)

    search parameters

  #### Returns [CanUndef](../modules/index.html#CanUndef)<T>