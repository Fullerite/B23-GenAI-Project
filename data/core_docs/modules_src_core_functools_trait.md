# Module src/core/functools/trait
[# core/functools/trait](#corefunctoolstrait)

This module provides a bunch of functions to create and implement traits.
A trait is the special kind of abstract class that is used as an interface.
Why would we need that? Well, unlike Java or Kotlin, TypeScript interfaces can't have default implementations of methods.
So we need to implement each method in our classes even if the implementation doesn't change.
This is where traits come into play. How it works? Ok, let's enumerate the steps to create a trait:

1. Create an abstract class, where define all necessary abstract methods and properties (yes, the trait can also define properties,
   not only methods).

```
abstract class Duckable {  
  abstract name: string;  
  abstract fly(): void;  
}
```

2. Define all non-abstract methods as simple methods without implementations: as a method body, use the loopback code,
   like `return Object.throw()`.

```
abstract class Duckable {  
  abstract name: string;  
  abstract fly(): void;  
  
  getQuack(size: number): string {  
    return Object.throw();  
  }  
}
```

3. Define the non-abstract methods as static class methods with the same names and signatures but add as the first parameter
   a link to the class instance, as we do it in Python or Rust. Also, we can use the `AddSelf` helper to produce less code.

```
abstract class Duckable {  
  abstract name: string;  
  abstract fly(): void;  
  
  getQuack(size: number): string {  
    return Object.throw();  
  }  
  
  // The first parameter provides a method to wrap.  
  // The second parameter declares which type has `self`.  
  static getQuack: AddSelf<Duckable['getQuack'], Duckable> = (self, size) => {  
    if (size < 10) {  
      return 'quack!';  
    }  
  
    if (size < 20) {  
      return 'quack!!!';  
    }  
  
    return 'QUACK!!!';  
  };  
}
```

We have created a trait. Now we can implement it in a simple class.

1. Create a simple class and implement the trait by using the `implements` keyword.
   Don't implement methods, which you want to store their default implementations.

```
class DuckLike implements Duckable {  
  name: string = 'Bob';  
  
  fly(): void {  
    // Do some logic to fly  
  }  
}
```

2. Create an interface with the same name as our class and extend it from the trait using the `Trait` type.

```
interface DuckLike extends Trait<typeof Duckable> {}  
  
class DuckLike implements Duckable {  
  name: string = 'Bob';  
  
  fly(): void {  
    // Do some logic to fly  
  }  
}
```

3. Use the `derive` decorator from `core/functools/trait` with our class and provide all traits that we want to implement automatically.

```
import { derive } from 'core/functools/trait';  
  
interface DuckLike extends Trait<typeof Duckable> {}  
  
@derive(Duckable)  
class DuckLike implements Duckable {  
  name: string = 'Bob';  
  
  fly(): void {  
    // Do some logic to fly  
  }  
}
```

4. Profit! Now TS understands default methods of interfaces, and it works in runtime.

```
import { derive } from 'core/functools/trait';  
  
interface DuckLike extends Trait<typeof Duckable> {}  
  
@derive(Duckable)  
class DuckLike implements Duckable {  
  name: string = 'Bob';  
  
  fly(): void {  
    // Do some logic to fly  
  }  
}  
  
/// 'QUACK!!!'  
console.log(new DuckLike().getQuack(60));
```

5. Of course, we can implement more than one trait in a component.

```
import { derive } from 'core/functools/trait';  
  
interface DuckLike extends Trait<typeof Duckable>, Trait<typeof AnotherTrait> {}  
  
@derive(Duckable, AnotherTrait)  
class DuckLike implements Duckable, AnotherTrait, SimpleInterfaceWithoutDefaultMethods {  
  name: string = 'Bob';  
  
  fly(): void {  
    // Do some logic to fly  
  }  
}
```

Besides, regular methods, you can also define get/set accessors like this:

```
abstract class Duckable {  
  get canFly(): boolean {  
    return Object.throw();  
  }  
  
  set canFly(value: boolean) {};  
  
  static canFly(self: Duckable): string {  
    if (arguments.length > 1) {  
      const value = arguments[1];  
      // Setter code  
  
    } else {  
      return /* Getter code */;  
    }  
  }  
}
```

## Index

### Functions

* [derive](src_core_functools_trait.html#derive)

## Functions

### derive

* derive(...traits: Function[]): (target: Function) => void

* + Defined in [src/core/functools/trait/index.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/functools/trait/index.ts#L72)

  Derives the provided traits to a class.
  The function is used to organize multiple implementing interfaces with the support of default methods.

  decorator

  example
  :   ```
      abstract class Interface1 {  
        abstract bar(): string;  
        
        /**  
         * The method that have the default implementation.  
         * The implementation is placed as a static method.  
         *\/  
        bla(a: number): number {  
          return Object.throw();  
        };  
        
        /**  
         * The default implementation for `Interface1.bla`.  
         * As the first parameter, the method is taken a context.  
         *  
         * @see Interface1.bla  
         *\/  
        static bla: AddSelf<iFoo['bla'], Baz> = (self, a) => a + 1;  
      }  
        
      abstract class Interface2 {  
        abstract bar2(): string;  
        
        bla2(a: number): string {  
          return Object.throw();  
        };  
        
        /** @see Interface2.bla2 *\/  
        static bla2: AddSelf<iFoo2['bla2'], Baz> = (self, a) => a.toFixed();  
      }  
        
      interface Baz extends Trait<typeof iFoo>, Trait<typeof iFoo2> {  
        
      }  
        
      @derive(iFoo, iFoo2)  
      class Baz implements iFoo, iFoo2 {  
        bar() {  
          return '1';  
        }  
        
        bar2() {  
          return '1';  
        }  
      }  
        
      console.log(new Baz().bla2(2.9872));
      ```

  #### Parameters

  + ##### Rest ...traits: Function[]

  #### Returns (target: Function) => void

  + - (target: Function): void
    - #### Parameters

      * ##### target: Function

      #### Returns void