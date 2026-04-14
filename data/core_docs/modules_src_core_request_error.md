# Module src/core/request/error
[# core/request/error](#corerequesterror)

This module provides a class for any request error and its details' extractor.

[## RequestError](#requesterror)

A constructor of the class accepts two parameters: required `type` and optional `details`.

```
throw new RequestError(RequestError.InvalidStatus, details);
```

Now we support the following types of `RequestError`:

* `RequestError.InvalidStatus` - a server has responded with a non-ok status;
* `RequestError.Abort` - a request was aborted;
* `RequestError.Timeout` - a request was aborted because of a timeout;
* `RequestError.Offline` - a request was failed because there is no connection to a network;
* `RequestError.Engine` - a request was failed because of an internal request engine' error.

The second parameter could contain `request` and `response` objects and an `error` object that is caused the problem.

[## RequestErrorDetailsExtractor](#requesterrordetailsextractor)

The extractor gets details from `RequestError`. A constructor of the class accepts one optional parameter with extra options.
These options allow filtering headers from request and response objects of the error's details object. It helps to hide
sensitive information.

The options itself look like this:

```
const opts = {  
  headers: {  
    include: [/*...*/],  
    exclude: [/*...*/]  
  }  
};  
  
const extractor = new RequestErrorDetailsExtractor(opts);
```

If `include` is defined, the extractor gets only headers from this array.
If `exclude` is defined, the extractor gets all available headers except the specified ones.
If both options are defined, then only `inlcude` option will be used.

## Index

### References

* [Details](src_core_request_error.html#Details)
* [RequestErrorDetailsExtractor](src_core_request_error.html#RequestErrorDetailsExtractor)
* [RequestErrorDetailsExtractorOptions](src_core_request_error.html#RequestErrorDetailsExtractorOptions)

### Classes

* [default](../classes/src_core_request_error.default.html)

## References

### Details

Re-exports [Details](../interfaces/src_core_request_error_interface.Details.html)

### RequestErrorDetailsExtractor

Re-exports [RequestErrorDetailsExtractor](../classes/src_core_request_error_extractor.RequestErrorDetailsExtractor.html)

### RequestErrorDetailsExtractorOptions

Re-exports [RequestErrorDetailsExtractorOptions](../interfaces/src_core_request_error_interface.RequestErrorDetailsExtractorOptions.html)