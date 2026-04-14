# Module src/core/data/decorators
## Index

### Functions

* [provider](src_core_data_decorators.html#provider)

## Functions

### provider

* provider(namespace: string): (target: Function) => void
* provider(provider: Function): void

* + Defined in [src/core/data/decorators.ts:26](https://github.com/V4Fire/Core/blob/master/src/core/data/decorators.ts#L26)

  Registers a data provider class to the global store with the specified namespace:
  the namespace value is concatenated with a name of the provider class

  decorator

  example
  :   ```
      // The provider is registered as 'user.List'  
      @provider('user')  
      class List extends Provider {}
      ```

  #### Parameters

  + ##### namespace: string

    namespace string

  #### Returns (target: Function) => void

  + - (target: Function): void
    - Registers a data provider class to the global store with the specified namespace:
      the namespace value is concatenated with a name of the provider class

      decorator

      example
      :   ```
          // The provider is registered as 'user.List'  
          @provider('user')  
          class List extends Provider {}
          ```

      #### Parameters

      * ##### target: Function

      #### Returns void
* + Defined in [src/core/data/decorators.ts:41](https://github.com/V4Fire/Core/blob/master/src/core/data/decorators.ts#L41)

  Registers a data provider class to the global store by a name of the provider class

  decorator

  example
  :   ```
      // The provider is registered as 'List'  
      @provider  
      class List extends Provider {}
      ```

  #### Parameters

  + ##### provider: Function

    provider class

  #### Returns void