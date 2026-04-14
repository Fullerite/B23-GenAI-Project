# Class default<T>
A class to create a range with the specified type.
The class supports ranges of numbers, strings, and dates.

### Type parameters

* #### T: [RangeValue](../modules/src_core_range_interface.html#RangeValue)

  range type value

### Hierarchy

* default

## Index

### Constructors

* [constructor](src_core_range.default.html#constructor)

### Properties

* [end](src_core_range.default.html#end)
* [isReversed](src_core_range.default.html#isReversed)
* [start](src_core_range.default.html#start)
* [type](src_core_range.default.html#type)

### Methods

* [[iterator]](src_core_range.default.html#_iterator_)
* [clamp](src_core_range.default.html#clamp)
* [clone](src_core_range.default.html#clone)
* [contains](src_core_range.default.html#contains)
* [entries](src_core_range.default.html#entries)
* [indices](src_core_range.default.html#indices)
* [intersect](src_core_range.default.html#intersect)
* [isValid](src_core_range.default.html#isValid)
* [reverse](src_core_range.default.html#reverse)
* [span](src_core_range.default.html#span)
* [toArray](src_core_range.default.html#toArray)
* [toString](src_core_range.default.html#toString)
* [toType](src_core_range.default.html#toType)
* [union](src_core_range.default.html#union)
* [values](src_core_range.default.html#values)

## Constructors

### constructor

* new default<T>(start?: number | T[] | [Nullable](../modules/index.html#Nullable)<T>, end?: number | T[] | [Nullable](../modules/index.html#Nullable)<T>): [default](src_core_range.default.html)<T>

* + Defined in [src/core/range/index.ts:75](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L75)

  example
  :   ```
      // [0, 1, 2, 3]  
      console.log(new Range(0, 3).toArray());  
        
      // [0, 1, 2]  
      console.log(new Range(0, [3]).toArray());  
        
      // ['b', 'c']  
      console.log(new Range(['a'], ['d']).toArray());  
        
      // []  
      console.log(new Range('a', ['a']).toArray());  
        
      // 'Wed Oct 18 1989 00:00:00..'  
      console.log(new Range(new Date(1989, 9, 18)).string());  
        
      // '..Wed Oct 18 1989 00:00:00'  
      console.log(new Range(null, new Date(1989, 9, 18)).string());
      ```

  #### Type parameters

  + #### T: [RangeValue](../modules/src_core_range_interface.html#RangeValue)

  #### Parameters

  + ##### start: number | T[] | [Nullable](../modules/index.html#Nullable)<T> = -Infinity
  + ##### end: number | T[] | [Nullable](../modules/index.html#Nullable)<T> = Infinity

  #### Returns [default](src_core_range.default.html)<T>

## Properties

### end

end: number

* Defined in [src/core/range/index.ts:33](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L33)

Top bound

### isReversed

isReversed: boolean = false

* Defined in [src/core/range/index.ts:43](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L43)

True if the range is reversed

### start

start: number

* Defined in [src/core/range/index.ts:28](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L28)

Bottom bound

### type

type: [RangeType](../modules/src_core_range_interface.html#RangeType)

* Defined in [src/core/range/index.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L38)

Range type

## Methods

### [iterator]

* [iterator](): IterableIterator<T>

* + Defined in [src/core/range/index.ts:169](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L169)

  Returns an iterator from the range

  #### Returns IterableIterator<T>

### clamp

* clamp(el: unknown): null | T

* + Defined in [src/core/range/index.ts:363](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L363)

  Clamps an element to be within the range if it falls outside.
  If the range is invalid or empty, the method always returns `null`.

  example
  :   ```
      // 3  
      console.log(new Range(0, 10).clamp(3));  
        
      // 'd'  
      console.log(new Range('a', 'd').clamp('z'));  
        
      // null  
      console.log(new Range(0, [0]).clamp(10));
      ```

  #### Parameters

  + ##### el: unknown

  #### Returns null | T

### clone

* clone(): [default](src_core_range.default.html)<T>

* + Defined in [src/core/range/index.ts:321](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L321)

  Clones the range and returns a new

  #### Returns [default](src_core_range.default.html)<T>

### contains

* contains(el: unknown): boolean

* + Defined in [src/core/range/index.ts:219](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L219)

  Returns true if the specified element is contained inside the range
  (the element can be a simple value or another range)

  example
  :   ```
      // true  
      console.log(new Range(0, 10).contains(4));  
        
      // false  
      console.log(new Range(0, [10]).contains(10));  
        
      // false  
      console.log(new Range(0, 10).contains(12));  
        
      // false  
      console.log(new Range(0, 10).contains('a'));  
        
      // true  
      console.log(new Range(0, 10).contains(Range(3, 6)));  
        
      // false  
      console.log(new Range(0, 10).contains(Range(3, 16)));  
        
      // false  
      console.log(new Range(0, 10).contains(Range('a', 'b')));
      ```

  #### Parameters

  + ##### el: unknown

  #### Returns boolean

### entries

* entries(step?: number): IterableIterator<[number, T]>

* + Defined in [src/core/range/index.ts:567](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L567)

  Returns an iterator from the range that produces pairs of iteration indices and values

  example
  :   ```
      for (const el of new Range(3, 1).entries()) {  
        // [0, 3] [1, 2] [2 3]  
        console.log(el);  
      }  
        
      for (const el of new Range(0, 3).entries(2)) {  
        // [0, 0] [1, 2]  
        console.log(el);  
      }
      ```

  #### Parameters

  + ##### Optional step: number

  #### Returns IterableIterator<[number, T]>

### indices

* indices(step?: number): IterableIterator<number>

* + Defined in [src/core/range/index.ts:527](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L527)

  Returns an iterator from the range that produces iteration indices

  example
  :   ```
      for (const el of new Range(3, 1).indices()) {  
        // 0 1 2  
        console.log(el);  
      }  
        
      for (const el of new Range(0, 3).indices(2)) {  
        // 0 1  
        console.log(el);  
      }
      ```

  #### Parameters

  + ##### Optional step: number

  #### Returns IterableIterator<number>

### intersect

* intersect(range: [default](src_core_range.default.html)<T extends string ? string : T>): [default](src_core_range.default.html)<T>

* + Defined in [src/core/range/index.ts:257](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L257)

  Returns a new range with the latest starting point as its start, and the earliest ending point as its end.
  If the two ranges do not intersect, this will effectively produce an empty range.

  The method preserves element ordering of the first range.
  The intersection of ranges with different types will always produce an empty range.

  example
  :   ```
      // 8..10  
      console.log(new Range(0, 10).intersect(new Range([7], 14)).toString());  
        
      // 10..7  
      console.log(new Range(10, 0).intersect(new Range(7, 14)).toString());  
        
      // 7..10  
      console.log(new Range(0, 10).intersect(new Range(7)).toString());  
        
      // 7..  
      console.log(new Range(0).intersect(new Range(7)).toString());  
        
      // ''  
      console.log(new Range(0, 10).intersect(new Range(11, 14)).toString());  
        
      // ''  
      console.log(new Range(0, 10).intersect(new Range('a', 'z')).toString());
      ```

  #### Parameters

  + ##### range: [default](src_core_range.default.html)<T extends string ? string : T>

  #### Returns [default](src_core_range.default.html)<T>

### isValid

* isValid(): boolean

* + Defined in [src/core/range/index.ts:186](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L186)

  Returns true if the range is valid

  example
  :   ```
      console.log(new Range('a', {}).isValid() === false);  
        
      console.log(new Range(new Date('boom!')).isValid() === false);  
        
      // The empty range is not valid  
      console.log(new Range([0], [0]).isValid() === false);
      ```

  #### Returns boolean

### reverse

* reverse(): [default](src_core_range.default.html)<T>

* + Defined in [src/core/range/index.ts:340](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L340)

  Clones the range with reversing of element ordering and returns a new

  example
  :   ```
      // [3, 2, 1, 0]  
      console.log(new Range(0, 3).reverse().toArray());
      ```

  #### Returns [default](src_core_range.default.html)<T>

### span

* span(): number

* + Defined in [src/core/range/index.ts:398](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L398)

  Returns a span of the range.
  The span includes both the start and the end.

  If the range is a date range, the value is in milliseconds.
  If the range is invalid or empty, the method always returns `0`.

  example
  :   ```
      // 4  
      console.log(new Range(7, 10).span());  
        
      // 0  
      console.log(new Range(0, [0]).span());
      ```

  #### Returns number

### toArray

* toArray(step?: number): T[]

* + Defined in [src/core/range/index.ts:607](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L607)

  Creates an array from the range and returns it.
  Mind, you can't transform infinite ranges to arrays, but you free to use iterators.

  example
  :   ```
      // [0, 3, 6, 9]  
      console.log(new Range(0, 10).toArray(3));  
        
      // ['a', 'b']  
      console.log(new Range('a', ['c']).toArray());  
        
      // []  
      console.log(new Range(0, [0]).toArray());
      ```

  #### Parameters

  + ##### Optional step: number

  #### Returns T[]

### toString

* toString(): string

* + Defined in [src/core/range/index.ts:637](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L637)

  Creates a string from the range and returns it.
  If the range invalid or empty, the method always returns an empty string.

  example
  :   ```
      // 0..10  
      console.log(new Range(0, 10).toString());  
        
      // 0..9  
      console.log(new Range(0, [10]).toString());  
        
      // 0..  
      console.log(new Range(0).toString());  
        
      // ..z  
      console.log(new Range(null, 'z').toString());  
        
      // ''  
      console.log(new Range(0, [0]).toString());
      ```

  #### Returns string

### toType

* toType(value: number): T

* + Defined in [src/core/range/index.ts:676](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L676)

  Converts a value to the real range type

  example
  :   ```
      // j  
      console.log(new Range('a', 'z).toType(106));
      ```

  #### Parameters

  + ##### value: number

  #### Returns T

### union

* union(range: [default](src_core_range.default.html)<T extends string ? string : T>): [default](src_core_range.default.html)<T>

* + Defined in [src/core/range/index.ts:302](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L302)

  Returns a new range with the earliest starting point as its start, and the latest ending point as its end.
  If the two ranges do not intersect, this will effectively remove the "gap" between them.

  The method preserves element ordering of the first range.
  The union of ranges with different types will always produce an empty range.

  example
  :   ```
      // 0..13  
      console.log(new Range(0, 10).union(new Range(7, [14])).toString());  
        
      // 14..0  
      console.log(new Range(10, 0).union(new Range(7, 14)).toString());  
        
      // 0..  
      console.log(new Range(0, 10).union(new Range(7)).toString());  
        
      // ..  
      console.log(new Range().union(new Range(7)).toString());  
        
      // ''  
      console.log(new Range(0, 10).union(new Range('a', 'z')).toString());
      ```

  #### Parameters

  + ##### range: [default](src_core_range.default.html)<T extends string ? string : T>

  #### Returns [default](src_core_range.default.html)<T>

### values

* values(step?: number): IterableIterator<T>

* + Defined in [src/core/range/index.ts:427](https://github.com/V4Fire/Core/blob/master/src/core/range/index.ts#L427)

  Returns an iterator from the range

  example
  :   ```
      for (const el of new Range(0, 3).values()) {  
        // 0 1 2 3  
        console.log(el);  
      }  
        
      for (const el of new Range(0, 3).values(2)) {  
        // 0 2  
        console.log(el);  
      }
      ```

  #### Parameters

  + ##### Optional step: number

  #### Returns IterableIterator<T>