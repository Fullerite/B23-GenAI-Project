# Module src/core/data/middlewares/attach-mock
[# core/data/middlewares/attach-mock](#coredatamiddlewaresattach-mock)

This module provides a middleware to attach mock data to a request.

[## Usage](#usage)

```
import Provider, { provider } from 'core/data';  
import { attachMock } from 'core/data/middlewares';  
  
@provider  
export default class User extends Provider {  
  static middlewares = {  
    attachMock  
  };  
  
  static mocks = {  
    PUT: [  
      {  
        body: {  
          age: 31  
        },  
  
        response: {  
          id: 1,  
          name: "Andrey",  
          age: 31  
        }  
      }  
    ],  
  
    GET: [{  
      response: {  
        id: 1,  
        name: "Andrey",  
        age: 30  
      }  
    }]  
  };  
  
  baseURL = 'user/:id';  
}
```

Mind that the root keys of mocks represent HTTP methods, but not provider methods.
The values contain arrays of request objects to match: the algorithm finds the most suitable option and returns its response.
Also, the middleware supports dynamically casting responses:

```
import Provider, { provider } from 'core/data';  
import { attachMock } from 'core/data/middlewares';  
  
@provider  
export default class User extends Provider {  
  static middlewares = {  
    attachMock  
  };  
  
  static mocks = {  
    GET: [{  
      response(params, response) {  
        if (!params.opts.query?.id) {  
          response.status = 400;  
          return;  
        }  
  
        response.status = 200;  
  
        return {  
          id: 1,  
          name: "Andrey",  
          age: 30  
        };  
       }  
    }]  
  };  
  
  baseURL = 'user/:id';  
}
```

Finally, you can use dynamic importing with mocks:

```
import Provider, { provider } from 'core/data';  
import { attachMock } from 'core/data/middlewares';  
  
@provider  
export default class User extends Provider {  
  static middlewares = {  
    attachMock  
  };  
  
  static mocks = import('mocks/user.json');  
  
  baseURL = 'user/:id';  
}
```

[## Enabling data mocks](#enabling-data-mocks)

By default, all data mocks are disabled, but you can enable them just type to a console of a browser:

```
// Enables mocks for the User provider  
setEnv('mock', {patterns: ['User']});  
  
// Enables mocks for all providers  
setEnv('mock', {patterns: ['.*']});
```

The values of patterns are converted to RegExp objects and applied to provider names (including namespaces).
Config settings are stored within a local browser storage.

## Index

### References

* [MockOptions](src_core_data_middlewares_attach_mock.html#MockOptions)

### Functions

* [attachMock](src_core_data_middlewares_attach_mock.html#attachMock)

## References

### MockOptions

Re-exports [MockOptions](../interfaces/src_core_data_middlewares_attach_mock_interface.MockOptions.html)

## Functions

### attachMock

* attachMock(this: [default](../classes/src_core_data.default.html), params: [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)<unknown>): Promise<[CanUndef](index.html#CanUndef)<Function>>

* + Defined in [src/core/data/middlewares/attach-mock/index.ts:50](https://github.com/V4Fire/Core/blob/master/src/core/data/middlewares/attach-mock/index.ts#L50)

  Middleware: attaches mock data from the `mocks` property

  #### Parameters

  + ##### this: [default](../classes/src_core_data.default.html)
  + ##### params: [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)<unknown>

  #### Returns Promise<[CanUndef](index.html#CanUndef)<Function>>