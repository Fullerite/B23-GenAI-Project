# Module src/core/data/middlewares/wait
[# core/data/middlewares/wait](#coredatamiddlewareswait)

This module provides a middleware to suspend a request until will be resolved the specified value to wait.
The middleware can be used as encoder: the value to wait will be taken from input data (`.wait`),
otherwise, it will be taken from `.meta.wait`.

```
import Provider, { provider } from 'core/data';  
import { wait } from 'core/data/middlewares';  
  
@provider  
export default class User extends Provider {  
  static encoders = {  
    get: [wait]  
  };  
  
  baseURL = 'user/:id';  
}  
  
(async () => {  
  const  
    user = new User(),  
  
    // Sleep 500 ms before do the request  
    bob = await user.get('bob', {meta: {wait: () => sleep(500)}}).data;  
  
  console.log(bob);  
  
  function sleep(ms) {  
    return new Promise((r) => setTimeout(r, ms));  
  }  
})();
```

## Index

### References

* [DataWithStatus](src_core_data_middlewares_wait.html#DataWithStatus)

### Functions

* [wait](src_core_data_middlewares_wait.html#wait)

## References

### DataWithStatus

Re-exports [DataWithStatus](../interfaces/src_core_data_middlewares_attach_status_interface.DataWithStatus.html)

## Functions

### wait

* wait(...args: unknown[]): Promise<unknown>

* + Defined in [src/core/data/middlewares/wait/index.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/data/middlewares/wait/index.ts#L25)

  Middleware: if the request has some parameter to wait,
  then the middleware won't be resolved until this parameter isn't resolved.

  This middleware can be used as encoder: the value to wait will be taken from input data (`.wait`),
  otherwise, it will be taken from `.meta.wait`.

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns Promise<unknown>