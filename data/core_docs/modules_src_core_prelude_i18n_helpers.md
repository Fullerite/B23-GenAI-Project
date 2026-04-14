# Module src/core/prelude/i18n/helpers
## Index

### Functions

* [i18nFactory](src_core_prelude_i18n_helpers.html#i18nFactory)
* [pluralizeText](src_core_prelude_i18n_helpers.html#pluralizeText)
* [resolveTemplate](src_core_prelude_i18n_helpers.html#resolveTemplate)

## Functions

### i18nFactory

* i18nFactory(keysetNameOrNames: string | string[], customLocale?: [Language](index.html#Language)): (key: string, params?: [I18nParams](index.html#I18nParams)) => string

* + Defined in [src/core/prelude/i18n/helpers.ts:36](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/helpers.ts#L36)

  Creates a function to internationalize strings in an application based on the given locale and keyset.
  Keyset allows you to share the same keys in different contexts.
  For example, the key "Next" may have a different value in different components of the application, therefore,
  we can use the name of the component as a keyset value.

  #### Parameters

  + ##### keysetNameOrNames: string | string[]

    the name of keyset or array with names of keysets to use.
    If passed as an array, the priority of the cases will be arranged in the order of the elements,
    the first one will have the highest priority.
  + ##### Optional customLocale: [Language](index.html#Language)

  #### Returns (key: string, params?: [I18nParams](index.html#I18nParams)) => string

  + - (key: string, params?: [I18nParams](index.html#I18nParams)): string
    - Creates a function to internationalize strings in an application based on the given locale and keyset.
      Keyset allows you to share the same keys in different contexts.
      For example, the key "Next" may have a different value in different components of the application, therefore,
      we can use the name of the component as a keyset value.

      #### Parameters

      * ##### key: string
      * ##### Optional params: [I18nParams](index.html#I18nParams)

      #### Returns string

### pluralizeText

* pluralizeText(pluralTranslation: [PluralTranslation](src_lang_interface.html#PluralTranslation), count: [CanUndef](index.html#CanUndef)<[PluralizationCount](src_core_prelude_i18n_interface.html#PluralizationCount)>): string

* + Defined in [src/core/prelude/i18n/helpers.ts:120](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/helpers.ts#L120)

  Returns the correct plural form to translate based on the given count

  example
  :   ```
      const result = pluralizeText([  
       {count} product,  // One  
       {count} products, // Some  
       {count} products, // Many  
       {count} products, // None  
      ], 5);  
        
      console.log(result); // '{count} products'
      ```

  #### Parameters

  + ##### pluralTranslation: [PluralTranslation](src_lang_interface.html#PluralTranslation)

    list of translation variants
  + ##### count: [CanUndef](index.html#CanUndef)<[PluralizationCount](src_core_prelude_i18n_interface.html#PluralizationCount)>

    the value on the basis of which the form of pluralization will be selected

  #### Returns string

### resolveTemplate

* resolveTemplate(value: [Translation](src_lang_interface.html#Translation), params?: [I18nParams](index.html#I18nParams)): string

* + Defined in [src/core/prelude/i18n/helpers.ts:88](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/helpers.ts#L88)

  Returns the form for plural sentences and resolves variables from the passed template

  example
  :   ```
      const example = resolveTemplate('My name is {name}, I live in {city}', {name: 'John', city: 'Denver'});  
        
      console.log(example); // 'My name is John, I live in Denver'  
        
      const examplePluralize = resolveTemplate([  
       {count} product,  // One  
       {count} products, // Some  
       {count} products, // Many  
       {count} products, // None  
      ], {count: 5});  
        
      console.log(examplePluralize); // '5 products'
      ```

  #### Parameters

  + ##### value: [Translation](src_lang_interface.html#Translation)

    a string for the default case, or an array of strings for the plural case
  + ##### Optional params: [I18nParams](index.html#I18nParams)

    a dictionary with parameters for internationalization

  #### Returns string