# Class default
### Hierarchy

* default
  + [default](src_core_data_modules_base.default.html)

## Index

### Constructors

* [constructor](src_core_data_modules_params.default.html#constructor)

### Properties

* [addMethod](src_core_data_modules_params.default.html#addMethod)
* [advURL](src_core_data_modules_params.default.html#advURL)
* [baseAddURL](src_core_data_modules_params.default.html#baseAddURL)
* [baseDelURL](src_core_data_modules_params.default.html#baseDelURL)
* [baseGetURL](src_core_data_modules_params.default.html#baseGetURL)
* [basePeekURL](src_core_data_modules_params.default.html#basePeekURL)
* [baseURL](src_core_data_modules_params.default.html#baseURL)
* [baseUpdURL](src_core_data_modules_params.default.html#baseUpdURL)
* [customMethod](src_core_data_modules_params.default.html#customMethod)
* [delMethod](src_core_data_modules_params.default.html#delMethod)
* [eventName](src_core_data_modules_params.default.html#eventName)
* [extraProviders](src_core_data_modules_params.default.html#extraProviders)
* [getMethod](src_core_data_modules_params.default.html#getMethod)
* [globalEmitter](src_core_data_modules_params.default.html#globalEmitter)
* [mocks](src_core_data_modules_params.default.html#mocks)
* [peekMethod](src_core_data_modules_params.default.html#peekMethod)
* [socketURL](src_core_data_modules_params.default.html#socketURL)
* [updMethod](src_core_data_modules_params.default.html#updMethod)
* [decoders](src_core_data_modules_params.default.html#decoders)
* [encoders](src_core_data_modules_params.default.html#encoders)
* [middlewares](src_core_data_modules_params.default.html#middlewares)
* [mocks](src_core_data_modules_params.default.html#mocks-1)
* [request](src_core_data_modules_params.default.html#request)

### Accessors

* [globalEvent](src_core_data_modules_params.default.html#globalEvent)
* [request](src_core_data_modules_params.default.html#request-1)

### Methods

* [select](src_core_data_modules_params.default.html#select)

## Constructors

### constructor

* new default(): [default](src_core_data_modules_params.default.html)

* #### Returns [default](src_core_data_modules_params.default.html)

## Properties

### addMethod

addMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'POST'

* Defined in [src/core/data/modules/params.ts:325](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L325)

Default HTTP request method for the "add" method

### advURL

advURL: string = ''

* Defined in [src/core/data/modules/params.ts:212](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L212)

Advanced part of URL for a request of all request methods
(it is concatenated with the base part)

### Optional baseAddURL

baseAddURL?: string

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

### customMethod

customMethod: [CanUndef](../modules/index.html#CanUndef)<[RequestMethod](../modules/src_core_request_interface.html#RequestMethod)>

* Defined in [src/core/data/modules/params.ts:341](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L341)

HTTP request method for all request methods.
This parameter will override other method parameters, such as "getMethod" or "delMethod".

### delMethod

delMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'DELETE'

* Defined in [src/core/data/modules/params.ts:335](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L335)

Default HTTP request method for the "del" method

### eventName

eventName: [CanUndef](../modules/index.html#CanUndef)<[ModelMethod](../modules/src_core_data_interface_types.html#ModelMethod)>

* Defined in [src/core/data/modules/params.ts:347](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L347)

Event name for requests.
Please notice that all request methods except "get", "peek" and "request" emit events by default.

### Optional extraProviders

extraProviders?: [FunctionalExtraProviders](../modules/src_core_data_interface_types.html#FunctionalExtraProviders)<unknown>

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

* Defined in [src/core/data/modules/params.ts:315](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L315)

Default HTTP request method for the "get" method

### Readonly globalEmitter

globalEmitter: EventEmitter2 = emitter

* Defined in [src/core/data/modules/params.ts:194](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L194)

Global event emitter to broadcast provider events

### Optional mocks

mocks?: [Mocks](../modules/src_core_data_interface_types.html#Mocks)

* Defined in [src/core/data/modules/params.ts:353](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L353)

deprecated

see
:   [[Provider.mocks]]

### peekMethod

peekMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'HEAD'

* Defined in [src/core/data/modules/params.ts:320](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L320)

Default HTTP request method for the "peek" method

### Optional socketURL

socketURL?: string

* Defined in [src/core/data/modules/params.ts:217](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L217)

URL for a socket connection

### updMethod

updMethod: [RequestMethod](../modules/src_core_request_interface.html#RequestMethod) = 'PUT'

* Defined in [src/core/data/modules/params.ts:330](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L330)

Default HTTP request method for the "upd" method

### Static Readonly decoders

decoders: [DecodersMap](../modules/src_core_data_interface_types.html#DecodersMap) = {}

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

* Defined in [src/core/data/modules/params.ts:48](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L48)

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

### globalEvent

* get globalEvent(): EventEmitter2

* + Defined in [src/core/data/modules/params.ts:359](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L359)

  deprecated

  see
  :   [[Provider.globalEmitter]]

  #### Returns EventEmitter2

### request

* get request(): { <D>(path: string, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestPromise](../interfaces/src_core_request_interface.RequestPromise.html)<D>; <D>(opts: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): typeof [\_\_type](src_core_data.default.html#__type); <D, A>(path: string, resolver: [RequestResolver](../interfaces/src_core_request_interface.RequestResolver.html)<D, A>, opts?: [CreateRequestOptions](../interfaces/src_core_request_interface.CreateRequestOptions.html)<D>): [RequestFunctionResponse](../interfaces/src_core_request_interface.RequestFunctionResponse.html)<D, A extends infer  V[] ? V[] : unknown[]> }

* + Defined in [src/core/data/modules/params.ts:367](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L367)

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

### Static select

* select<T>(obj: unknown, params: [SelectParams](../interfaces/src_core_object_select_interface.SelectParams.html)): [CanUndef](../modules/index.html#CanUndef)<T>

* + Defined in [src/core/data/modules/params.ts:187](https://github.com/V4Fire/Core/blob/master/src/core/data/modules/params.ts#L187)

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