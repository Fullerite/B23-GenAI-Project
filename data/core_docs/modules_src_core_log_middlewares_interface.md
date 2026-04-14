# Module src/core/log/middlewares/interface
## Index

### Interfaces

* [LogEvent](../interfaces/src_core_log_middlewares_interface.LogEvent.html)
* [LogMiddleware](../interfaces/src_core_log_middlewares_interface.LogMiddleware.html)
* [NextCallback](../interfaces/src_core_log_middlewares_interface.NextCallback.html)

### Type aliases

* [CtorArgs](src_core_log_middlewares_interface.html#CtorArgs)
* [LogMiddlewares](src_core_log_middlewares_interface.html#LogMiddlewares)
* [LogMiddlewaresName](src_core_log_middlewares_interface.html#LogMiddlewaresName)
* [LogMiddlewaresTuple](src_core_log_middlewares_interface.html#LogMiddlewaresTuple)

## Type aliases

### CtorArgs

CtorArgs<T>: T extends (...args: infer  A) => ReturnType<T> ? A : never

* Defined in [src/core/log/middlewares/interface.ts:46](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/interface.ts#L46)

#### Type parameters

* #### T: (...args: any[]) => any

### LogMiddlewares

LogMiddlewares: [LogMiddlewaresName](src_core_log_middlewares_interface.html#LogMiddlewaresName) | [LogMiddlewaresTuple](src_core_log_middlewares_interface.html#LogMiddlewaresTuple)<[LogMiddlewaresName](src_core_log_middlewares_interface.html#LogMiddlewaresName)>

* Defined in [src/core/log/middlewares/interface.ts:42](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/interface.ts#L42)

### LogMiddlewaresName

LogMiddlewaresName: keyof typeof [default](src_core_log_middlewares.html#default)

* Defined in [src/core/log/middlewares/interface.ts:40](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/interface.ts#L40)

### LogMiddlewaresTuple

LogMiddlewaresTuple<K>: [K, [CtorArgs](src_core_log_middlewares_interface.html#CtorArgs)<typeof [default](src_core_log_middlewares.html#default)[K]>]

* Defined in [src/core/log/middlewares/interface.ts:44](https://github.com/V4Fire/Core/blob/master/src/core/log/middlewares/interface.ts#L44)

#### Type parameters

* #### K: [LogMiddlewaresName](src_core_log_middlewares_interface.html#LogMiddlewaresName)