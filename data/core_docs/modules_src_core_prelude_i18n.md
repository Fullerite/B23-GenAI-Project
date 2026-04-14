# Module src/core/prelude/i18n
[# core/prelude/i18n](#corepreludei18n)

This module provides an API for internationalizing an application.
Keep in mind, this module provides functions, but the language packs themselves for internationalization are specified in the `lang` module.

```
// Getting a language translation for a key  
i18n('my-keyset-name')('my key');  
  
// Resolve variables in text  
i18n('my-keyset-name')('My name is {name}', {name: 'John'});     // My name is John  
  
// Pluralize text  
i18n('my-keyset-name')('I have {count} toy', {count: 10});       // I have 10 toys  
  
// Using of several keysets, to implement inheritance or reuse shared translations  
i18n(['my-keyset-name', 'dates'])('February')  
  
// Using translations other than the app default language  
i18n('my-keyset-name', 'ru')('I have {count} toy', {count: 10}); // У меня 10 игрушек
```

[## Using the i18n function as a string tag](#using-the-i18n-function-as-a-string-tag)

To reduce syntactic noise, it is allowed to use the internationalization function as a regular string tag.
Please note that in this option we cannot forward additional parameters (for example, for pluralization).

```
const t = i18n('my-keyset-name');  
console.log(t`my key`);
```

[## Language pack structure](#language-pack-structure)

The structure of the language map consists of several levels:

1. The symbolic name of the language or locale for which translations are provided.

   ```
   export default {  
     'ru': { /* ... */ },  
     'en-gb': { /* ... */ },  
     'en-us': { /* ... */ }  
   };
   ```
2. Namespace for language keys (hereinafter "keyset"). Keyset allows you to share the same keys in different contexts.
   For example, the key "Next" may have a different value in different components of the application, therefore,
   we can use the name of the component as a keyset value.

   ```
   export default {  
     ru: {  
       'b-reg-form': {  
         Next: 'Далее'  
       },  
     
       'b-queue': {  
         Next: 'Следующий'  
       }  
     }  
   };
   ```
3. Keys and translations. The key can be any symbolic sequence. The key values will be replaced with the corresponding translation.
   If there is no translation for the given locale or keyset, then the key itself will be displayed.

[## Interpolation of variables in translations](#interpolation-of-variables-in-translations)

Some translations may include special constructions in their text, which will be replaced by other meanings during translation.
To use such variables, it is enough to place them inside the `{variableName}` construct, and pass the values for
translation as an additional parameter to the `i18n` function.

```
export default {  
  en: {  
    "my-component": {  
      "my name is {name}": "my name is {name}",  
      "apple": "apple"  
    }  
  }  
};
```

```
i18n('my-component')('My name is {name}', {name: 'John'});
```

[## Pluralization of translations](#pluralization-of-translations)

Some keys may have multiple translations depending on some numeric value. For example, "1 apple" or "5 apples".
To specify such translations, a special macro `{count}` is used, and translations are specified as a tuple `[one, some, many, none]`.

```
export default {  
  ru: {  
    "my-component": {  
      "time": "время",  
      "{count} product": [  
        "{count} продукт",  
        "{count} продукта",  
        "{count} продуктов",  
        "{count} продуктов"  
      ]  
    }  
  },  
  
  en: {  
    "my-component": {  
      "{count} product": [  
        "{count} product",  
        "{count} products",  
        "{count} products",  
        "{count} products"  
      ]  
    }  
  }  
};
```

```
i18n('my-component', 'ru')('{count} product', {count: 10});
```

[## API](#api)
[### Getters](#getters)
[#### emitter](#emitter)

The event emitter to broadcast localization events.

[#### locale](#locale)

The default application language.

```
interface Locale {  
  /**  
   * The locale value  
   */  
  value: CanUndef<Language>;  
  
  /**  
   * True if the locale is already defined  
   */  
  isDefined: boolean;  
  
  /**  
   * The locale initialization promise  
   */  
  isInitialized: Promise<void>;  
}
```

[### Functions](#functions)
[#### setLocale](#setlocale)

Sets a new application language.

```
import { setLocale } from 'core/prelide/i18n';  
  
// Set Russian as default language  
setLocale('ru', true);
```

[#### i18n](#i18n)

Creates a function to internationalize strings in an application based on the given locale and keyset.
Keyset allows you to share the same keys in different contexts. For example, the key "Next" may have a different value
in different components of the application, therefore, we can use the name of the component as a keyset value.

Keep in mind that this function is global, i.e. it does not need to be explicitly imported.

```
i18n('my-component')('My name is {name}', {name: 'John'});
```

## Index

### References

* [Locale](src_core_prelude_i18n.html#Locale)
* [LocaleKVStorage](src_core_prelude_i18n.html#LocaleKVStorage)
* [PluralizationCount](src_core_prelude_i18n.html#PluralizationCount)
* [emitter](src_core_prelude_i18n.html#emitter)
* [event](src_core_prelude_i18n.html#event)
* [i18nFactory](src_core_prelude_i18n.html#i18nFactory)
* [locale](src_core_prelude_i18n.html#locale)
* [pluralizeMap](src_core_prelude_i18n.html#pluralizeMap)
* [pluralizeText](src_core_prelude_i18n.html#pluralizeText)
* [resolveTemplate](src_core_prelude_i18n.html#resolveTemplate)

### Functions

* [setLocale](src_core_prelude_i18n.html#setLocale)

## References

### Locale

Re-exports [Locale](../interfaces/src_core_prelude_i18n_interface.Locale.html)

### LocaleKVStorage

Re-exports [LocaleKVStorage](../interfaces/src_core_prelude_i18n_interface.LocaleKVStorage.html)

### PluralizationCount

Re-exports [PluralizationCount](src_core_prelude_i18n_interface.html#PluralizationCount)

### emitter

Re-exports [emitter](src_core_prelude_i18n_const.html#emitter)

### event

Re-exports [event](src_core_prelude_i18n_const.html#event)

### i18nFactory

Re-exports [i18nFactory](src_core_prelude_i18n_helpers.html#i18nFactory)

### locale

Re-exports [locale](src_core_prelude_i18n_const.html#locale)

### pluralizeMap

Re-exports [pluralizeMap](src_core_prelude_i18n_const.html#pluralizeMap)

### pluralizeText

Re-exports [pluralizeText](src_core_prelude_i18n_helpers.html#pluralizeText)

### resolveTemplate

Re-exports [resolveTemplate](src_core_prelude_i18n_helpers.html#resolveTemplate)

## Functions

### setLocale

* setLocale(value: [CanUndef](index.html#CanUndef)<[Language](index.html#Language)>, def?: boolean): [CanUndef](index.html#CanUndef)<[Language](index.html#Language)>

* + Defined in [src/core/prelude/i18n/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/prelude/i18n/index.ts#L47)

  Sets a new application language

  emits
  :   `setLocale(value: string, oldValue?: string)`

  #### Parameters

  + ##### value: [CanUndef](index.html#CanUndef)<[Language](index.html#Language)>
  + ##### Optional def: boolean

  #### Returns [CanUndef](index.html#CanUndef)<[Language](index.html#Language)>