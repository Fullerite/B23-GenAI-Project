# Namespace TB
## Index

### Type aliases

* [Append](index.TB.html#Append)
* [Cast](index.TB.html#Cast)
* [CleanedGaps](index.TB.html#CleanedGaps)
* [Concat](index.TB.html#Concat)
* [Curry](index.TB.html#Curry)
* [Drop](index.TB.html#Drop)
* [GapOf](index.TB.html#GapOf)
* [Gaps](index.TB.html#Gaps)
* [GapsOf](index.TB.html#GapsOf)
* [HasTail](index.TB.html#HasTail)
* [Head](index.TB.html#Head)
* [Last](index.TB.html#Last)
* [Length](index.TB.html#Length)
* [Next](index.TB.html#Next)
* [PartialGaps](index.TB.html#PartialGaps)
* [Pos](index.TB.html#Pos)
* [Prepend](index.TB.html#Prepend)
* [Prev](index.TB.html#Prev)
* [Reverse](index.TB.html#Reverse)
* [Tail](index.TB.html#Tail)
* [Type](index.TB.html#Type)
* [\_\_](index.TB.html#__)

## Type aliases

### Append

Append<E, T>: [Concat](index.TB.html#Concat)<T, [E]>

* Defined in [index.d.ts:52](https://github.com/V4Fire/Core/blob/master/index.d.ts#L52)

#### Type parameters

* #### E
* #### T: any[]

### Cast

Cast<X, Y>: X extends Y ? X : Y

* Defined in [index.d.ts:17](https://github.com/V4Fire/Core/blob/master/index.d.ts#L17)

#### Type parameters

* #### X
* #### Y

### CleanedGaps

CleanedGaps<T>: { [ K in keyof T]: NonNullable<T[K]> }

* Defined in [index.d.ts:68](https://github.com/V4Fire/Core/blob/master/index.d.ts#L68)

#### Type parameters

* #### T: any[]

### Concat

Concat<T1, T2>: [Reverse](index.TB.html#Reverse)<[Cast](index.TB.html#Cast)<[Reverse](index.TB.html#Reverse)<T1>, any[]>, T2>

* Defined in [index.d.ts:50](https://github.com/V4Fire/Core/blob/master/index.d.ts#L50)

#### Type parameters

* #### T1: any[]
* #### T2: any[]

### Curry

Curry<F>: <T>(...args: [Cast](index.TB.html#Cast)<T, [Gaps](index.TB.html#Gaps)<Parameters<F>>>) => [GapsOf](index.TB.html#GapsOf)<T, Parameters<F>> extends [any, ...any[]] ? [Curry](index.TB.html#Curry)<(...args: [Cast](index.TB.html#Cast)<[GapsOf](index.TB.html#GapsOf)<T, Parameters<F>>, any[]>) => ReturnType<F>> : ReturnType<F>

* Defined in [index.d.ts:75](https://github.com/V4Fire/Core/blob/master/index.d.ts#L75)

#### Type parameters

* #### F: (...args: any) => any

#### Type declaration

* + <T>(...args: [Cast](index.TB.html#Cast)<T, [Gaps](index.TB.html#Gaps)<Parameters<F>>>): [GapsOf](index.TB.html#GapsOf)<T, Parameters<F>> extends [any, ...any[]] ? [Curry](index.TB.html#Curry)<(...args: [Cast](index.TB.html#Cast)<[GapsOf](index.TB.html#GapsOf)<T, Parameters<F>>, any[]>) => ReturnType<F>> : ReturnType<F>
  + #### Type parameters

    - #### T: any[]

    #### Parameters

    - ##### Rest ...args: [Cast](index.TB.html#Cast)<T, [Gaps](index.TB.html#Gaps)<Parameters<F>>>

    #### Returns [GapsOf](index.TB.html#GapsOf)<T, Parameters<F>> extends [any, ...any[]] ? [Curry](index.TB.html#Curry)<(...args: [Cast](index.TB.html#Cast)<[GapsOf](index.TB.html#GapsOf)<T, Parameters<F>>, any[]>) => ReturnType<F>> : ReturnType<F>

### Drop

Drop<N, T, I>: [Length](index.TB.html#Length)<I> extends N ? T : [Drop](index.TB.html#Drop)<N, [Tail](index.TB.html#Tail)<T>, [Prepend](index.TB.html#Prepend)<any, I>>

* Defined in [index.d.ts:39](https://github.com/V4Fire/Core/blob/master/index.d.ts#L39)

#### Type parameters

* #### N: number
* #### T: any[]
* #### I: any[] = []

### GapOf

GapOf<T1, T2, TN, I>: T1[[Pos](index.TB.html#Pos)<I>] extends [TB](index.TB.html).[\_\_](index.TB.html#__) ? [Append](index.TB.html#Append)<T2[[Pos](index.TB.html#Pos)<I>], TN> : TN

* Defined in [index.d.ts:56](https://github.com/V4Fire/Core/blob/master/index.d.ts#L56)

#### Type parameters

* #### T1: any[]
* #### T2: any[]
* #### TN: any[]
* #### I: any[]

### Gaps

Gaps<T>: [CleanedGaps](index.TB.html#CleanedGaps)<[PartialGaps](index.TB.html#PartialGaps)<T>> extends [...infer  A] ? A : never

* Defined in [index.d.ts:72](https://github.com/V4Fire/Core/blob/master/index.d.ts#L72)

#### Type parameters

* #### T: any[]

### GapsOf

GapsOf<T1, T2, TN, I>: [Pos](index.TB.html#Pos)<I> extends [Length](index.TB.html#Length)<T1> ? [Concat](index.TB.html#Concat)<TN, [Cast](index.TB.html#Cast)<[Drop](index.TB.html#Drop)<[Pos](index.TB.html#Pos)<I>, T2>, any[]>> : [GapsOf](index.TB.html#GapsOf)<T1, T2, [Cast](index.TB.html#Cast)<[GapOf](index.TB.html#GapOf)<T1, T2, TN, I>, any[]>, [Next](index.TB.html#Next)<I>>

* Defined in [index.d.ts:59](https://github.com/V4Fire/Core/blob/master/index.d.ts#L59)

#### Type parameters

* #### T1: any[]
* #### T2: any[]
* #### TN: any[] = []
* #### I: any[] = []

### HasTail

HasTail<T>: [Length](index.TB.html#Length)<T> extends 0 | 1 ? false : true

* Defined in [index.d.ts:31](https://github.com/V4Fire/Core/blob/master/index.d.ts#L31)

#### Type parameters

* #### T: any[]

### Head

Head<T>: T extends [infer  H, ...any[]] ? H : never

* Defined in [index.d.ts:25](https://github.com/V4Fire/Core/blob/master/index.d.ts#L25)

#### Type parameters

* #### T: any[]

### Last

Last<T>: [HasTail](index.TB.html#HasTail)<T> extends true ? [Last](index.TB.html#Last)<[Tail](index.TB.html#Tail)<T>> : [Head](index.TB.html#Head)<T>

* Defined in [index.d.ts:34](https://github.com/V4Fire/Core/blob/master/index.d.ts#L34)

#### Type parameters

* #### T: any[]

### Length

Length<T>: T["length"]

* Defined in [index.d.ts:23](https://github.com/V4Fire/Core/blob/master/index.d.ts#L23)

#### Type parameters

* #### T: any[]

### Next

Next<I>: [Prepend](index.TB.html#Prepend)<any, I>

* Defined in [index.d.ts:44](https://github.com/V4Fire/Core/blob/master/index.d.ts#L44)

#### Type parameters

* #### I: any[]

### PartialGaps

PartialGaps<T>: { [ K in keyof T]?: T[K] | [TB](index.TB.html).[\_\_](index.TB.html#__) }

* Defined in [index.d.ts:64](https://github.com/V4Fire/Core/blob/master/index.d.ts#L64)

#### Type parameters

* #### T: any[]

### Pos

Pos<I>: [Length](index.TB.html#Length)<I>

* Defined in [index.d.ts:42](https://github.com/V4Fire/Core/blob/master/index.d.ts#L42)

#### Type parameters

* #### I: any[]

### Prepend

Prepend<E, T>: [E, ...T]

* Defined in [index.d.ts:37](https://github.com/V4Fire/Core/blob/master/index.d.ts#L37)

#### Type parameters

* #### E
* #### T: any[]

### Prev

Prev<I>: [Tail](index.TB.html#Tail)<I>

* Defined in [index.d.ts:45](https://github.com/V4Fire/Core/blob/master/index.d.ts#L45)

#### Type parameters

* #### I: any[]

### Reverse

Reverse<T, R, I>: [Pos](index.TB.html#Pos)<I> extends [Length](index.TB.html#Length)<T> ? R : [Reverse](index.TB.html#Reverse)<T, [Prepend](index.TB.html#Prepend)<T[[Pos](index.TB.html#Pos)<I>], R>, [Next](index.TB.html#Next)<I>>

* Defined in [index.d.ts:47](https://github.com/V4Fire/Core/blob/master/index.d.ts#L47)

#### Type parameters

* #### T: any[]
* #### R: any[] = []
* #### I: any[] = []

### Tail

Tail<T>: T extends [any, ...infer  TT] ? TT : []

* Defined in [index.d.ts:28](https://github.com/V4Fire/Core/blob/master/index.d.ts#L28)

#### Type parameters

* #### T: any[]

### Type

Type<A, ID>: A & { [ K in "symbol"]: ID }

* Defined in [index.d.ts:19](https://github.com/V4Fire/Core/blob/master/index.d.ts#L19)

#### Type parameters

* #### A: any
* #### ID: string

### \_\_

\_\_: [Type](index.TB.html#Type)<{}, "x">

* Defined in [index.d.ts:54](https://github.com/V4Fire/Core/blob/master/index.d.ts#L54)