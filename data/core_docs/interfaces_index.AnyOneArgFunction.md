# Interface AnyOneArgFunction<ARG, R>
### Type parameters

* #### ARG = any
* #### R = any

### Hierarchy

* Function
  + AnyOneArgFunction

### Callable

* AnyOneArgFunction(arg: ARG): R
* AnyOneArgFunction(arg: ARG): R

* + Defined in [index.d.ts:188](https://github.com/V4Fire/Core/blob/master/index.d.ts#L188)

  #### Parameters

  + ##### arg: ARG

  #### Returns R
* + Defined in dist/index.d.ts:139

  #### Parameters

  + ##### arg: ARG

  #### Returns R

## Index

### Methods

* [compose](index.AnyOneArgFunction.html#compose)
* [curry](index.AnyOneArgFunction.html#curry)
* [debounce](index.AnyOneArgFunction.html#debounce)
* [once](index.AnyOneArgFunction.html#once)
* [option](index.AnyOneArgFunction.html#option)
* [result](index.AnyOneArgFunction.html#result)
* [throttle](index.AnyOneArgFunction.html#throttle)

## Methods

### compose

* compose<T>(this: T): T
* compose<A, T1, T2>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>): [AnyFunction](index.AnyFunction.html)<A, T1 extends Promise<any> ? Promise<T2> : T2>
* compose<A, T1, T2, T3>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>): [AnyFunction](index.AnyFunction.html)<A, T2 extends Promise<any> ? Promise<T3> : T1 extends Promise<any> ? Promise<T3> : T3>
* compose<A, T1, T2, T3, T4>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>, fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>): [AnyFunction](index.AnyFunction.html)<A, T3 extends Promise<any> ? Promise<T4> : T2 extends Promise<any> ? Promise<T4> : T1 extends Promise<any> ? Promise<T4> : T4>
* compose<A, T1, T2, T3, T4, T5>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>, fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>, fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>): [AnyFunction](index.AnyFunction.html)<A, T4 extends Promise<any> ? Promise<T5> : T3 extends Promise<any> ? Promise<T5> : T2 extends Promise<any> ? Promise<T5> : T1 extends Promise<any> ? Promise<T5> : T5>
* compose<A, T1, T2, T3, T4, T5, T6>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>, fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>, fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>, fn5: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T5, T6>): [AnyFunction](index.AnyFunction.html)<A, T5 extends Promise<any> ? Promise<T6> : T4 extends Promise<any> ? Promise<T6> : T3 extends Promise<any> ? Promise<T6> : T2 extends Promise<any> ? Promise<T6> : T1 extends Promise<any> ? Promise<T6> : T6>
* compose<T>(this: T): T
* compose<A, T1, T2>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>): [AnyFunction](index.AnyFunction.html)<A, T1 extends Promise<any> ? Promise<T2> : T2>
* compose<A, T1, T2, T3>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>): [AnyFunction](index.AnyFunction.html)<A, T2 extends Promise<any> ? Promise<T3> : T1 extends Promise<any> ? Promise<T3> : T3>
* compose<A, T1, T2, T3, T4>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>, fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>): [AnyFunction](index.AnyFunction.html)<A, T3 extends Promise<any> ? Promise<T4> : T2 extends Promise<any> ? Promise<T4> : T1 extends Promise<any> ? Promise<T4> : T4>
* compose<A, T1, T2, T3, T4, T5>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>, fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>, fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>): [AnyFunction](index.AnyFunction.html)<A, T4 extends Promise<any> ? Promise<T5> : T3 extends Promise<any> ? Promise<T5> : T2 extends Promise<any> ? Promise<T5> : T1 extends Promise<any> ? Promise<T5> : T5>
* compose<A, T1, T2, T3, T4, T5, T6>(this: [AnyFunction](index.AnyFunction.html)<A, T1>, fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>, fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>, fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>, fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>, fn5: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T5, T6>): [AnyFunction](index.AnyFunction.html)<A, T5 extends Promise<any> ? Promise<T6> : T4 extends Promise<any> ? Promise<T6> : T3 extends Promise<any> ? Promise<T6> : T2 extends Promise<any> ? Promise<T6> : T1 extends Promise<any> ? Promise<T6> : T6>

* Inherited from Function.compose

  + Defined in [index.d.ts:4037](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4037)

  Performs left-to-right function composition.
  The first argument may have any arity; the remaining arguments must be unary.

  If any function from parameters returns a Promise, the next function from the parameters
  will take the resolved value of that promise,
  the final result of calling the composition function is also a promise.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### this: T

  #### Returns T
* Inherited from Function.compose

  + Defined in [index.d.ts:4039](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4039)

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T1 extends Promise<any> ? Promise<T2> : T2>
* Inherited from Function.compose

  + Defined in [index.d.ts:4044](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4044)

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T2 extends Promise<any> ? Promise<T3> : T1 extends Promise<any> ? Promise<T3> : T3>
* Inherited from Function.compose

  + Defined in [index.d.ts:4050](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4050)

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3
  + #### T4

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>
  + ##### fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T3 extends Promise<any> ? Promise<T4> : T2 extends Promise<any> ? Promise<T4> : T1 extends Promise<any> ? Promise<T4> : T4>
* Inherited from Function.compose

  + Defined in [index.d.ts:4063](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4063)

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3
  + #### T4
  + #### T5

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>
  + ##### fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>
  + ##### fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T4 extends Promise<any> ? Promise<T5> : T3 extends Promise<any> ? Promise<T5> : T2 extends Promise<any> ? Promise<T5> : T1 extends Promise<any> ? Promise<T5> : T5>
* Inherited from Function.compose

  + Defined in [index.d.ts:4078](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4078)

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3
  + #### T4
  + #### T5
  + #### T6

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>
  + ##### fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>
  + ##### fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>
  + ##### fn5: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T5, T6>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T5 extends Promise<any> ? Promise<T6> : T4 extends Promise<any> ? Promise<T6> : T3 extends Promise<any> ? Promise<T6> : T2 extends Promise<any> ? Promise<T6> : T1 extends Promise<any> ? Promise<T6> : T6>
* Inherited from Function.compose

  + Defined in dist/index.d.ts:3913

  Performs left-to-right function composition.
  The first argument may have any arity; the remaining arguments must be unary.

  If any function from parameters returns a Promise, the next function from the parameters
  will take the resolved value of that promise,
  the final result of calling the composition function is also a promise.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### this: T

  #### Returns T
* Inherited from Function.compose

  + Defined in dist/index.d.ts:3915

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T1 extends Promise<any> ? Promise<T2> : T2>
* Inherited from Function.compose

  + Defined in dist/index.d.ts:3920

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T2 extends Promise<any> ? Promise<T3> : T1 extends Promise<any> ? Promise<T3> : T3>
* Inherited from Function.compose

  + Defined in dist/index.d.ts:3926

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3
  + #### T4

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>
  + ##### fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T3 extends Promise<any> ? Promise<T4> : T2 extends Promise<any> ? Promise<T4> : T1 extends Promise<any> ? Promise<T4> : T4>
* Inherited from Function.compose

  + Defined in dist/index.d.ts:3939

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3
  + #### T4
  + #### T5

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>
  + ##### fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>
  + ##### fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T4 extends Promise<any> ? Promise<T5> : T3 extends Promise<any> ? Promise<T5> : T2 extends Promise<any> ? Promise<T5> : T1 extends Promise<any> ? Promise<T5> : T5>
* Inherited from Function.compose

  + Defined in dist/index.d.ts:3954

  #### Type parameters

  + #### A: any[]
  + #### T1
  + #### T2
  + #### T3
  + #### T4
  + #### T5
  + #### T6

  #### Parameters

  + ##### this: [AnyFunction](index.AnyFunction.html)<A, T1>
  + ##### fn1: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T1, T2>
  + ##### fn2: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T2, T3>
  + ##### fn3: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T3, T4>
  + ##### fn4: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T4, T5>
  + ##### fn5: [AnyOneArgFunction](index.AnyOneArgFunction.html)<T5, T6>

  #### Returns [AnyFunction](index.AnyFunction.html)<A, T5 extends Promise<any> ? Promise<T6> : T4 extends Promise<any> ? Promise<T6> : T3 extends Promise<any> ? Promise<T6> : T2 extends Promise<any> ? Promise<T6> : T1 extends Promise<any> ? Promise<T6> : T6>

### curry

* curry<T>(this: T): [Curry](../modules/index.TB.html#Curry)<T>
* curry<T>(this: T): [Curry](../modules/index.TB.html#Curry)<T>

* Inherited from Function.curry

  + Defined in [index.d.ts:4027](https://github.com/V4Fire/Core/blob/master/index.d.ts#L4027)

  Returns a curried equivalent of the function.

  The curried function has two unusual capabilities.
  First, its arguments needn't be provided one at a time.
  If f is a ternary function and g is f.curry(), the following are equivalent:

  ```
  g(1)(2)(3)  
  g(1)(2, 3)  
  g(1, 2)(3)  
  g(1, 2, 3)
  ```

  Secondly, the special placeholder value Function.\_\_ may be used to specify "gaps", allowing partial application
  of any combination of arguments, regardless of their positions. If g is as above and \_ is Function.\_\_,
  the following are equivalent:

  ```
  g(1, 2, 3)  
  g(_, 2, 3)(1)  
  g(_, _, 3)(1)(2)  
  g(_, _, 3)(1, 2)  
  g(_, 2)(1)(3)  
  g(_, 2)(1, 3)  
  g(_, 2)(_, 3)(1)
  ```

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T

  #### Returns [Curry](../modules/index.TB.html#Curry)<T>
* Inherited from Function.curry

  + Defined in dist/index.d.ts:3903

  Returns a curried equivalent of the function.

  The curried function has two unusual capabilities.
  First, its arguments needn't be provided one at a time.
  If f is a ternary function and g is f.curry(), the following are equivalent:

  ```
  g(1)(2)(3)  
  g(1)(2, 3)  
  g(1, 2)(3)  
  g(1, 2, 3)
  ```

  Secondly, the special placeholder value Function.\_\_ may be used to specify "gaps", allowing partial application
  of any combination of arguments, regardless of their positions. If g is as above and \_ is Function.\_\_,
  the following are equivalent:

  ```
  g(1, 2, 3)  
  g(_, 2, 3)(1)  
  g(_, _, 3)(1)(2)  
  g(_, _, 3)(1, 2)  
  g(_, 2)(1)(3)  
  g(_, 2)(1, 3)  
  g(_, 2)(_, 3)(1)
  ```

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T

  #### Returns [Curry](../modules/index.TB.html#Curry)<T>

### debounce

* debounce<T>(this: T, delay?: number): [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* debounce<T>(this: T, delay?: number): [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>

* Inherited from Function.debounce

  + Defined in [index.d.ts:3907](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3907)

  Returns a new function that allows to invoke the target function only with the specified delay.
  The next invocation of the function will cancel the previous.

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T
  + ##### Optional delay: number

  #### Returns [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* Inherited from Function.debounce

  + Defined in dist/index.d.ts:3783

  Returns a new function that allows to invoke the target function only with the specified delay.
  The next invocation of the function will cancel the previous.

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T
  + ##### Optional delay: number

  #### Returns [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>

### once

* once<T>(this: T): T
* once<T>(this: T): T

* Inherited from Function.once

  + Defined in [index.d.ts:3899](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3899)

  Returns a new function that allows to invoke the target function only once

  #### Type parameters

  + #### T

  #### Parameters

  + ##### this: T

  #### Returns T
* Inherited from Function.once

  + Defined in dist/index.d.ts:3775

  Returns a new function that allows to invoke the target function only once

  #### Type parameters

  + #### T

  #### Parameters

  + ##### this: T

  #### Returns T

### option

* option<R>(this: () => R): [AnyFunction](index.AnyFunction.html)<any[], [Maybe](index.Maybe.html)<R>>
* option<A1, A, R>(this: (a1: A1, ...rest: A) => R): (a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>, ...rest: A) => [Maybe](index.Maybe.html)<R>
* option<R>(this: () => R): [AnyFunction](index.AnyFunction.html)<any[], [Maybe](index.Maybe.html)<R>>
* option<A1, A, R>(this: (a1: A1, ...rest: A) => R): (a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>, ...rest: A) => [Maybe](index.Maybe.html)<R>

* Inherited from Function.option

  + Defined in [index.d.ts:3944](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3944)

  Returns a new function based on the target that wraps the returning value into the Either structure.
  If the first argument of the created function is taken null or undefined, the function returns the rejected value.

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.option()(null).catch((err) => err === null);  
      toLowerCase.option()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
        
      toLowerCase.option()('FOO').then((value) => value === 'foo');  
      toLowerCase.option()(toLowerCase.option()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### R

  #### Parameters

  + ##### this: () => R

    - * (): R
      * #### Returns R

  #### Returns [AnyFunction](index.AnyFunction.html)<any[], [Maybe](index.Maybe.html)<R>>
* Inherited from Function.option

  + Defined in [index.d.ts:3963](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3963)

  Returns a new function based on the target that wraps the returning value into the Either structure.
  If the first argument of the created function is taken null or undefined, the function returns the rejected value.

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.option()(null).catch((err) => err === null);  
      toLowerCase.option()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
        
      toLowerCase.option()('FOO').then((value) => value === 'foo');  
      toLowerCase.option()(toLowerCase.option()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### A1
  + #### A: any[]
  + #### R

  #### Parameters

  + ##### this: (a1: A1, ...rest: A) => R

    - * (a1: A1, ...rest: A): R
      * #### Parameters

        + ##### a1: A1
        + ##### Rest ...rest: A

        #### Returns R

  #### Returns (a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>, ...rest: A) => [Maybe](index.Maybe.html)<R>

  + - (a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>, ...rest: A): [Maybe](index.Maybe.html)<R>
    - Returns a new function based on the target that wraps the returning value into the Either structure.
      If the first argument of the created function is taken null or undefined, the function returns the rejected value.

      example
      :   ```
          function toLowerCase(str: string): string {  
            return str.toLowerCase();  
          }  
            
          toLowerCase.option()(null).catch((err) => err === null);  
          toLowerCase.option()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
            
          toLowerCase.option()('FOO').then((value) => value === 'foo');  
          toLowerCase.option()(toLowerCase.option()('FOO')).then((value) => value === 'foo');
          ```

      #### Parameters

      * ##### a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>
      * ##### Rest ...rest: A

      #### Returns [Maybe](index.Maybe.html)<R>
* Inherited from Function.option

  + Defined in dist/index.d.ts:3820

  Returns a new function based on the target that wraps the returning value into the Either structure.
  If the first argument of the created function is taken null or undefined, the function returns the rejected value.

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.option()(null).catch((err) => err === null);  
      toLowerCase.option()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
        
      toLowerCase.option()('FOO').then((value) => value === 'foo');  
      toLowerCase.option()(toLowerCase.option()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### R

  #### Parameters

  + ##### this: () => R

    - * (): R
      * #### Returns R

  #### Returns [AnyFunction](index.AnyFunction.html)<any[], [Maybe](index.Maybe.html)<R>>
* Inherited from Function.option

  + Defined in dist/index.d.ts:3839

  Returns a new function based on the target that wraps the returning value into the Either structure.
  If the first argument of the created function is taken null or undefined, the function returns the rejected value.

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.option()(null).catch((err) => err === null);  
      toLowerCase.option()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
        
      toLowerCase.option()('FOO').then((value) => value === 'foo');  
      toLowerCase.option()(toLowerCase.option()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### A1
  + #### A: any[]
  + #### R

  #### Parameters

  + ##### this: (a1: A1, ...rest: A) => R

    - * (a1: A1, ...rest: A): R
      * #### Parameters

        + ##### a1: A1
        + ##### Rest ...rest: A

        #### Returns R

  #### Returns (a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>, ...rest: A) => [Maybe](index.Maybe.html)<R>

  + - (a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>, ...rest: A): [Maybe](index.Maybe.html)<R>
    - Returns a new function based on the target that wraps the returning value into the Either structure.
      If the first argument of the created function is taken null or undefined, the function returns the rejected value.

      example
      :   ```
          function toLowerCase(str: string): string {  
            return str.toLowerCase();  
          }  
            
          toLowerCase.option()(null).catch((err) => err === null);  
          toLowerCase.option()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
            
          toLowerCase.option()('FOO').then((value) => value === 'foo');  
          toLowerCase.option()(toLowerCase.option()('FOO')).then((value) => value === 'foo');
          ```

      #### Parameters

      * ##### a1: [Nullable](../modules/index.html#Nullable)<A1> | [Maybe](index.Maybe.html)<[Nullable](../modules/index.html#Nullable)<A1>> | [Either](index.Either.html)<A1>
      * ##### Rest ...rest: A

      #### Returns [Maybe](index.Maybe.html)<R>

### result

* result<R>(this: () => R): [AnyFunction](index.AnyFunction.html)<any[], [Either](index.Either.html)<R>>
* result<A1, A, R>(this: (a1: A1, ...rest: A) => R): (a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>, ...rest: A) => [Either](index.Either.html)<R>
* result<R>(this: () => R): [AnyFunction](index.AnyFunction.html)<any[], [Either](index.Either.html)<R>>
* result<A1, A, R>(this: (a1: A1, ...rest: A) => R): (a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>, ...rest: A) => [Either](index.Either.html)<R>

* Inherited from Function.result

  + Defined in [index.d.ts:3980](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3980)

  Returns a new function based on the target that wraps the returning value into the Either structure

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.result()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
      toLowerCase.result()('FOO').then((value) => value === 'foo');  
      toLowerCase.result()(toLowerCase.result()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### R

  #### Parameters

  + ##### this: () => R

    - * (): R
      * #### Returns R

  #### Returns [AnyFunction](index.AnyFunction.html)<any[], [Either](index.Either.html)<R>>
* Inherited from Function.result

  + Defined in [index.d.ts:3996](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3996)

  Returns a new function based on the target that wraps the returning value into the Either structure

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.result()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
      toLowerCase.result()('FOO').then((value) => value === 'foo');  
      toLowerCase.result()(toLowerCase.result()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### A1
  + #### A: any[]
  + #### R

  #### Parameters

  + ##### this: (a1: A1, ...rest: A) => R

    - * (a1: A1, ...rest: A): R
      * #### Parameters

        + ##### a1: A1
        + ##### Rest ...rest: A

        #### Returns R

  #### Returns (a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>, ...rest: A) => [Either](index.Either.html)<R>

  + - (a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>, ...rest: A): [Either](index.Either.html)<R>
    - Returns a new function based on the target that wraps the returning value into the Either structure

      example
      :   ```
          function toLowerCase(str: string): string {  
            return str.toLowerCase();  
          }  
            
          toLowerCase.result()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
          toLowerCase.result()('FOO').then((value) => value === 'foo');  
          toLowerCase.result()(toLowerCase.result()('FOO')).then((value) => value === 'foo');
          ```

      #### Parameters

      * ##### a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>
      * ##### Rest ...rest: A

      #### Returns [Either](index.Either.html)<R>
* Inherited from Function.result

  + Defined in dist/index.d.ts:3856

  Returns a new function based on the target that wraps the returning value into the Either structure

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.result()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
      toLowerCase.result()('FOO').then((value) => value === 'foo');  
      toLowerCase.result()(toLowerCase.result()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### R

  #### Parameters

  + ##### this: () => R

    - * (): R
      * #### Returns R

  #### Returns [AnyFunction](index.AnyFunction.html)<any[], [Either](index.Either.html)<R>>
* Inherited from Function.result

  + Defined in dist/index.d.ts:3872

  Returns a new function based on the target that wraps the returning value into the Either structure

  example
  :   ```
      function toLowerCase(str: string): string {  
        return str.toLowerCase();  
      }  
        
      toLowerCase.result()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
      toLowerCase.result()('FOO').then((value) => value === 'foo');  
      toLowerCase.result()(toLowerCase.result()('FOO')).then((value) => value === 'foo');
      ```

  #### Type parameters

  + #### A1
  + #### A: any[]
  + #### R

  #### Parameters

  + ##### this: (a1: A1, ...rest: A) => R

    - * (a1: A1, ...rest: A): R
      * #### Parameters

        + ##### a1: A1
        + ##### Rest ...rest: A

        #### Returns R

  #### Returns (a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>, ...rest: A) => [Either](index.Either.html)<R>

  + - (a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>, ...rest: A): [Either](index.Either.html)<R>
    - Returns a new function based on the target that wraps the returning value into the Either structure

      example
      :   ```
          function toLowerCase(str: string): string {  
            return str.toLowerCase();  
          }  
            
          toLowerCase.result()(1).catch((err) => err.message === 'str.toLowerCase is not a function');  
          toLowerCase.result()('FOO').then((value) => value === 'foo');  
          toLowerCase.result()(toLowerCase.result()('FOO')).then((value) => value === 'foo');
          ```

      #### Parameters

      * ##### a1: [Maybe](index.Maybe.html)<A1> | [Either](index.Either.html)<A1>
      * ##### Rest ...rest: A

      #### Returns [Either](index.Either.html)<R>

### throttle

* throttle<T>(this: T, delay?: number): [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* throttle<T>(this: T, opts: [ThrottleOptions](index.ThrottleOptions.html)): [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* throttle<T>(this: T, delay?: number): [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* throttle<T>(this: T, opts: [ThrottleOptions](index.ThrottleOptions.html)): [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>

* Inherited from Function.throttle

  + Defined in [index.d.ts:3916](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3916)

  Returns a new function that allows to invoke the target function not more often than the specified delay.
  The first invoking of a function will run immediately, but all rest invokes will be merged to one and
  executes after the specified delay.

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T
  + ##### Optional delay: number

  #### Returns [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* Inherited from Function.throttle

  + Defined in [index.d.ts:3925](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3925)

  Returns a new function that allows to invoke the target function not more often than the specified delay.
  The first invoking of a function will run immediately, but all rest invokes will be merged to one and
  executes after the specified delay.

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T
  + ##### opts: [ThrottleOptions](index.ThrottleOptions.html)

    options for the operation

  #### Returns [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* Inherited from Function.throttle

  + Defined in dist/index.d.ts:3792

  Returns a new function that allows to invoke the target function not more often than the specified delay.
  The first invoking of a function will run immediately, but all rest invokes will be merged to one and
  executes after the specified delay.

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T
  + ##### Optional delay: number

  #### Returns [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>
* Inherited from Function.throttle

  + Defined in dist/index.d.ts:3801

  Returns a new function that allows to invoke the target function not more often than the specified delay.
  The first invoking of a function will run immediately, but all rest invokes will be merged to one and
  executes after the specified delay.

  #### Type parameters

  + #### T: [AnyFunction](index.AnyFunction.html)<any[], any, T>

  #### Parameters

  + ##### this: T
  + ##### opts: [ThrottleOptions](index.ThrottleOptions.html)

    options for the operation

  #### Returns [AnyFunction](index.AnyFunction.html)<Parameters<T>, void>