# Module src/core/data/middlewares/attach-status
[# core/data/middlewares/attach-status](#coredatamiddlewaresattach-status)

This module provides a decoder middleware to attach a response status to the response data.

```
import Provider, { provider } from 'core/data';  
import { attachStatus } from 'core/data/middlewares';  
  
@provider  
export default class User extends Provider {  
  static decoders = {  
    get: [attachStatus]  
  };  
  
  baseURL = 'user/:id';  
}  
  
(async () => {  
  const  
    user = new User(),  
    bob = await user.get('bob').data;  
  
  // Response status code (number)  
  console.log(bob.status);  
  
  // User response data  
  console.log(bob.data);  
})();
```

## Index

### References

* [DataWithStatus](src_core_data_middlewares_attach_status.html#DataWithStatus)

### Functions

* [attachStatus](src_core_data_middlewares_attach_status.html#attachStatus)

## References

### DataWithStatus

Re-exports [DataWithStatus](../interfaces/src_core_data_middlewares_attach_status_interface.DataWithStatus.html)

## Functions

### attachStatus

* attachStatus<D>(data: D, params: [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)<D>, response: [default](../classes/src_core_request_response.default.html)<D>): [DataWithStatus](../interfaces/src_core_data_middlewares_attach_status_interface.DataWithStatus.html)<D>

* + Defined in [src/core/data/middlewares/attach-status/index.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/data/middlewares/attach-status/index.ts#L26)

  Decoder: attaches a response status to response data

  #### Type parameters

  + #### D

  #### Parameters

  + ##### data: D
  + ##### params: [MiddlewareParams](../interfaces/src_core_request_interface.MiddlewareParams.html)<D>
  + ##### response: [default](../classes/src_core_request_response.default.html)<D>

  #### Returns [DataWithStatus](../interfaces/src_core_data_middlewares_attach_status_interface.DataWithStatus.html)<D>