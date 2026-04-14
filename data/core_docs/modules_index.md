# Module index
[# core/prelude](#coreprelude)

This module provides extensions for a bunch of builtin objects, such as String, Number, etc.
The module is uploaded to the runtime automatically, you don't need to require it.

## Index

### Namespaces

* [TB](index.TB.html)

### Interfaces

* [AnyFunction](../interfaces/index.AnyFunction.html)
* [AnyOneArgFunction](../interfaces/index.AnyOneArgFunction.html)
* [DateCreateOptions](../interfaces/index.DateCreateOptions.html)
* [DateHTMLDateStringOptions](../interfaces/index.DateHTMLDateStringOptions.html)
* [DateHTMLTimeStringOptions](../interfaces/index.DateHTMLTimeStringOptions.html)
* [DateRelative](../interfaces/index.DateRelative.html)
* [DateSetParams](../interfaces/index.DateSetParams.html)
* [Dictionary](../interfaces/index.Dictionary.html)
* [Either](../interfaces/index.Either.html)
* [FastCloneOptions](../interfaces/index.FastCloneOptions.html)
* [JSONCb](../interfaces/index.JSONCb.html)
* [Maybe](../interfaces/index.Maybe.html)
* [NumberPadOptions](../interfaces/index.NumberPadOptions.html)
* [ObjectForEachOptions](../interfaces/index.ObjectForEachOptions.html)
* [ObjectForEachPropertyDescriptor](../interfaces/index.ObjectForEachPropertyDescriptor.html)
* [ObjectFromArrayOptions](../interfaces/index.ObjectFromArrayOptions.html)
* [ObjectGetOptions](../interfaces/index.ObjectGetOptions.html)
* [ObjectMixinOptions](../interfaces/index.ObjectMixinOptions.html)
* [ObjectPropertyFilter](../interfaces/index.ObjectPropertyFilter.html)
* [ObjectSetOptions](../interfaces/index.ObjectSetOptions.html)
* [StrictDictionary](../interfaces/index.StrictDictionary.html)
* [StringCamelizeOptions](../interfaces/index.StringCamelizeOptions.html)
* [StringCapitalizeOptions](../interfaces/index.StringCapitalizeOptions.html)
* [StringDasherizeOptions](../interfaces/index.StringDasherizeOptions.html)
* [StringUnderscoreOptions](../interfaces/index.StringUnderscoreOptions.html)
* [ThrottleOptions](../interfaces/index.ThrottleOptions.html)

### Type aliases

* [AddSelf](index.html#AddSelf)
* [AnyIterable](index.html#AnyIterable)
* [AnyToBoolean](index.html#AnyToBoolean)
* [AnyToIgnore](index.html#AnyToIgnore)
* [CanArray](index.html#CanArray)
* [CanPromise](index.html#CanPromise)
* [CanPromiseLike](index.html#CanPromiseLike)
* [CanUndef](index.html#CanUndef)
* [CanVoid](index.html#CanVoid)
* [ClassConstructor](index.html#ClassConstructor)
* [DateCreateValue](index.html#DateCreateValue)
* [DateHTMLStringOptions](index.html#DateHTMLStringOptions)
* [DateRelativeType](index.html#DateRelativeType)
* [DictionaryType](index.html#DictionaryType)
* [I18nParams](index.html#I18nParams)
* [IterableType](index.html#IterableType)
* [JSONLikeValue](index.html#JSONLikeValue)
* [Language](index.html#Language)
* [NewPromise](index.html#NewPromise)
* [Nullable](index.html#Nullable)
* [NumberOption](index.html#NumberOption)
* [ObjectPropertyPath](index.html#ObjectPropertyPath)
* [Overwrite](index.html#Overwrite)
* [Primitive](index.html#Primitive)
* [PromiseType](index.html#PromiseType)
* [RegExpFlag](index.html#RegExpFlag)
* [ReturnPromise](index.html#ReturnPromise)
* [StringPluralizationForms](index.html#StringPluralizationForms)
* [Trait](index.html#Trait)
* [Writable](index.html#Writable)

### Variables

* [API\_URL](index.html#API_URL)
* [APP\_NAME](index.html#APP_NAME)
* [DEBUG](index.html#DEBUG)
* [IS\_PROD](index.html#IS_PROD)
* [LOCALE](index.html#LOCALE)

### Functions

* [Any](index.html#Any)
* [i18n](index.html#i18n)
* [stderr](index.html#stderr)
* [structuredClone](index.html#structuredClone)

## Type aliases

### AddSelf

AddSelf<M, S>: M extends (...args: infer  A) => infer  R ? (self: S, ...args: A) => R : never

* Defined in [index.d.ts:303](https://github.com/V4Fire/Core/blob/master/index.d.ts#L303)

Returns a new function based on the specified with adding as the first parameter the passed object

example
:   ```
    // (self: bFoo, a: number) => string  
    AddSelf<(a: number) => string, bFoo>
    ```

#### Type parameters

* #### M: Function
* #### S: object

### AnyIterable

AnyIterable<T>: Iterable<T> | AsyncIterable<T>

* Defined in [index.d.ts:234](https://github.com/V4Fire/Core/blob/master/index.d.ts#L234)

#### Type parameters

* #### T = unknown

### AnyToBoolean

AnyToBoolean: any

* Defined in [index.d.ts:182](https://github.com/V4Fire/Core/blob/master/index.d.ts#L182)

### AnyToIgnore

AnyToIgnore: any

* Defined in [index.d.ts:181](https://github.com/V4Fire/Core/blob/master/index.d.ts#L181)

### CanArray

CanArray<T>: T | T[]

* Defined in [index.d.ts:173](https://github.com/V4Fire/Core/blob/master/index.d.ts#L173)

#### Type parameters

* #### T

### CanPromise

CanPromise<T>: T | Promise<T>

* Defined in [index.d.ts:171](https://github.com/V4Fire/Core/blob/master/index.d.ts#L171)

#### Type parameters

* #### T

### CanPromiseLike

CanPromiseLike<T>: T | PromiseLike<T>

* Defined in [index.d.ts:172](https://github.com/V4Fire/Core/blob/master/index.d.ts#L172)

#### Type parameters

* #### T

### CanUndef

CanUndef<T>: T | undefined

* Defined in [index.d.ts:175](https://github.com/V4Fire/Core/blob/master/index.d.ts#L175)

#### Type parameters

* #### T

### CanVoid

CanVoid<T>: T | void

* Defined in [index.d.ts:179](https://github.com/V4Fire/Core/blob/master/index.d.ts#L179)

#### Type parameters

* #### T

### ClassConstructor

ClassConstructor<ARGS, R>: new (...args: ARGS) => R

* Defined in [index.d.ts:191](https://github.com/V4Fire/Core/blob/master/index.d.ts#L191)

#### Type parameters

* #### ARGS: any[] = any[]
* #### R = any

#### Type declaration

* + new (...args: ARGS): R
  + #### Parameters

    - ##### Rest ...args: ARGS

    #### Returns R

### DateCreateValue

DateCreateValue: number | string | Date

* Defined in [index.d.ts:2913](https://github.com/V4Fire/Core/blob/master/index.d.ts#L2913)

### DateHTMLStringOptions

DateHTMLStringOptions: [DateHTMLTimeStringOptions](../interfaces/index.DateHTMLTimeStringOptions.html) & [DateHTMLDateStringOptions](../interfaces/index.DateHTMLDateStringOptions.html)

* Defined in [index.d.ts:3420](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3420)

### DateRelativeType

DateRelativeType: "milliseconds" | "seconds" | "minutes" | "hours" | "days" | "weeks" | "months" | "years"

* Defined in [index.d.ts:3424](https://github.com/V4Fire/Core/blob/master/index.d.ts#L3424)

### DictionaryType

DictionaryType<T>: T extends [Dictionary](../interfaces/index.Dictionary.html)<infer  V> ? NonNullable<V> : T

* Defined in [index.d.ts:232](https://github.com/V4Fire/Core/blob/master/index.d.ts#L232)

#### Type parameters

* #### T: [Dictionary](../interfaces/index.Dictionary.html)

### I18nParams

I18nParams: { count?: number | [StringPluralizationForms](index.html#StringPluralizationForms) } & {}

* Defined in [index.d.ts:133](https://github.com/V4Fire/Core/blob/master/index.d.ts#L133)

Parameters for the internationalization function

### IterableType

IterableType<T>: T extends Iterable<infer  V> ? V : T extends AsyncIterable<infer  V> ? V : T

* Defined in [index.d.ts:236](https://github.com/V4Fire/Core/blob/master/index.d.ts#L236)

#### Type parameters

* #### T: Iterable<any> | AsyncIterable<any>

### JSONLikeValue

JSONLikeValue: string | number | boolean | null | [JSONLikeValue](index.html#JSONLikeValue)[] | [Dictionary](../interfaces/index.Dictionary.html)<[JSONLikeValue](index.html#JSONLikeValue)>

* Defined in [index.d.ts:163](https://github.com/V4Fire/Core/blob/master/index.d.ts#L163)

### Language

Language: "be" | "en" | "kk" | "ru" | "tr" | "tt" | "uk" | "id" | "uz" | "es" | "de" | "hy" | "ka" | "ky" | "sr" | "fr" | "lv" | "lt" | "ro" | "fi" | "az" | "zh" | "he" | "et" | "no" | "sv" | "pt" | "ar" | "sw"

* Defined in [index.d.ts:89](https://github.com/V4Fire/Core/blob/master/index.d.ts#L89)

### NewPromise

NewPromise<K, V>: K extends [Maybe](../interfaces/index.Maybe.html) ? [Maybe](../interfaces/index.Maybe.html)<V> : K extends [Either](../interfaces/index.Either.html) ? [Either](../interfaces/index.Either.html)<V> : Promise<V>

* Defined in [index.d.ts:209](https://github.com/V4Fire/Core/blob/master/index.d.ts#L209)

#### Type parameters

* #### K
* #### V

### Nullable

Nullable<T>: T | null | undefined

* Defined in [index.d.ts:176](https://github.com/V4Fire/Core/blob/master/index.d.ts#L176)

#### Type parameters

* #### T

### NumberOption

NumberOption: "decimal" | "thousands"

* Defined in [index.d.ts:2328](https://github.com/V4Fire/Core/blob/master/index.d.ts#L2328)

### ObjectPropertyPath

ObjectPropertyPath: string | any[]

* Defined in [index.d.ts:713](https://github.com/V4Fire/Core/blob/master/index.d.ts#L713)

### Overwrite

Overwrite<T, U>: Pick<T, Exclude<keyof T, keyof U>> & U

* Defined in [index.d.ts:266](https://github.com/V4Fire/Core/blob/master/index.d.ts#L266)

Overrides properties of the specified type or interface.
Don't use this helper if you simply extend one type from another, i.e. without overriding properties.

example
:   ```
    type A = {  
      x: number;  
      y: number;  
    };  
      
    // {x:number; y: string}  
    type B = Overwrite<A, {y: string}>;
    ```

#### Type parameters

* #### T

  original type
* #### U

  type with the overridden properties

### Primitive

Primitive: string | symbol | number | bigint | boolean | undefined | null

* Defined in [index.d.ts:154](https://github.com/V4Fire/Core/blob/master/index.d.ts#L154)

### PromiseType

PromiseType<T>: T extends [Maybe](../interfaces/index.Maybe.html)<infer  V> ? NonNullable<V> : T extends Promise<infer  V> ? V : T

* Defined in [index.d.ts:213](https://github.com/V4Fire/Core/blob/master/index.d.ts#L213)

#### Type parameters

* #### T

### RegExpFlag

RegExpFlag: "" | "g" | "i" | "m" | "u" | "y" | "s"

* Defined in [index.d.ts:2802](https://github.com/V4Fire/Core/blob/master/index.d.ts#L2802)

### ReturnPromise

ReturnPromise<T>: (...args: Parameters<T>) => Promise<ReturnType<T>>

* Defined in [index.d.ts:230](https://github.com/V4Fire/Core/blob/master/index.d.ts#L230)

#### Type parameters

* #### T: [AnyFunction](../interfaces/index.AnyFunction.html)<any[], unknown>

  any function

#### Type declaration

* + (...args: Parameters<T>): Promise<ReturnType<T>>
  + Wraps the specified function to return a value as Promise

    example
    :   ```
        type A = typeof () => null;  
          
        // () => Promise<null>  
        type B = ReturnPromise<A>;
        ```

    #### Parameters

    - ##### Rest ...args: Parameters<T>

    #### Returns Promise<ReturnType<T>>

### StringPluralizationForms

StringPluralizationForms: "one" | "some" | "many" | "none"

* Defined in [index.d.ts:140](https://github.com/V4Fire/Core/blob/master/index.d.ts#L140)

String pluralization constants that can be used instead of numbers

### Trait

Trait<C, I>: { [ K in Extract<keyof C, keyof I>]: I[K] }

* Defined in [index.d.ts:290](https://github.com/V4Fire/Core/blob/master/index.d.ts#L290)

Returns a new non-abstract class from the specified abstract class where methods can have the default implementation.
The default implementations are taken from the static methods that match by names with the class's methods.

example
:   ```
    abstract class iFoo {  
      static bar(self: object): string {  
        return self.bla.toString();  
      }  
      
      bar(): string {  
        return Object.throw();  
      }  
      
      abstract bar(): number;  
    }  
      
    // class { bar(): string; }  
    Trait<typeof bFoo>
    ```

#### Type parameters

* #### C: Function
* #### I: C["prototype"] = C["prototype"]

### Writable

Writable<T>: { -readonly [ K in keyof T]: T[K] }

* Defined in [index.d.ts:244](https://github.com/V4Fire/Core/blob/master/index.d.ts#L244)

Creates an interface based on the specified type or interface but every property can be edited

#### Type parameters

* #### T

## Variables

### Const API\_URL

API\_URL: [CanUndef](index.html#CanUndef)<string>

* Defined in [index.d.ts:86](https://github.com/V4Fire/Core/blob/master/index.d.ts#L86)

### Const APP\_NAME

APP\_NAME: string

* Defined in [index.d.ts:85](https://github.com/V4Fire/Core/blob/master/index.d.ts#L85)

### Const DEBUG

DEBUG: boolean

* Defined in [index.d.ts:82](https://github.com/V4Fire/Core/blob/master/index.d.ts#L82)

### Const IS\_PROD

IS\_PROD: boolean

* Defined in [index.d.ts:83](https://github.com/V4Fire/Core/blob/master/index.d.ts#L83)

### Const LOCALE

LOCALE: [Language](index.html#Language)

* Defined in [index.d.ts:87](https://github.com/V4Fire/Core/blob/master/index.d.ts#L87)

## Functions

### Any

* Any(obj: any): any
* Any(obj: any): any

* + Defined in [index.d.ts:105](https://github.com/V4Fire/Core/blob/master/index.d.ts#L105)

  Converts the specified unknown value to any

  #### Parameters

  + ##### obj: any

  #### Returns any
* + Defined in dist/index.d.ts:93

  Converts the specified unknown value to any

  #### Parameters

  + ##### obj: any

  #### Returns any

### i18n

* i18n(keysetNameOrNames: [CanArray](index.html#CanArray)<string>, customLocale?: [Language](index.html#Language)): (key: string | TemplateStringsArray, params?: [I18nParams](index.html#I18nParams)) => string
* i18n(strings: any, ...expr: any[]): string

* + Defined in [index.d.ts:126](https://github.com/V4Fire/Core/blob/master/index.d.ts#L126)

  Creates a function to internationalize strings in an application based on the given locale and keyset.
  Keyset allows you to share the same keys in different contexts.
  For example, the key "Next" may have a different value in different components of the application, therefore,
  we can use the name of the component as a keyset value.

  #### Parameters

  + ##### keysetNameOrNames: [CanArray](index.html#CanArray)<string>

    the name of keyset or array with names of keysets to use.
    If passed as an array, the priority of the cases will be arranged in the order of the elements,
    the first one will have the highest priority.
  + ##### Optional customLocale: [Language](index.html#Language)

  #### Returns (key: string | TemplateStringsArray, params?: [I18nParams](index.html#I18nParams)) => string

  + - (key: string | TemplateStringsArray, params?: [I18nParams](index.html#I18nParams)): string
    - Creates a function to internationalize strings in an application based on the given locale and keyset.
      Keyset allows you to share the same keys in different contexts.
      For example, the key "Next" may have a different value in different components of the application, therefore,
      we can use the name of the component as a keyset value.

      #### Parameters

      * ##### key: string | TemplateStringsArray
      * ##### Optional params: [I18nParams](index.html#I18nParams)

      #### Returns string
* + Defined in dist/index.d.ts:104

  Global i18n function (can be used as a string tag or simple function)

  #### Parameters

  + ##### strings: any
  + ##### Rest ...expr: any[]

  #### Returns string

### stderr

* stderr(err: any): void
* stderr(err: any): void

* + Defined in [index.d.ts:111](https://github.com/V4Fire/Core/blob/master/index.d.ts#L111)

  STDERR wrapper

  #### Parameters

  + ##### err: any

  #### Returns void
* + Defined in dist/index.d.ts:99

  STDERR wrapper

  #### Parameters

  + ##### err: any

  #### Returns void

### structuredClone

* structuredClone<T>(obj: T): T

* + Defined in [index.d.ts:145](https://github.com/V4Fire/Core/blob/master/index.d.ts#L145)

  #### Type parameters

  + #### T

  #### Parameters

  + ##### obj: T

  #### Returns T