# Module src/lang
[# lang](#lang)

This module provides language pack maps for internationalizing the application.
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

## Index

### References

* [KeysetTranslations](src_lang.html#KeysetTranslations)
* [LangPacs](src_lang.html#LangPacs)
* [PluralTranslation](src_lang.html#PluralTranslation)
* [Translation](src_lang.html#Translation)
* [Translations](src_lang.html#Translations)

### Properties

* [default](src_lang.html#default)

## References

### KeysetTranslations

Re-exports [KeysetTranslations](src_lang_interface.html#KeysetTranslations)

### LangPacs

Re-exports [LangPacs](src_lang_interface.html#LangPacs)

### PluralTranslation

Re-exports [PluralTranslation](src_lang_interface.html#PluralTranslation)

### Translation

Re-exports [Translation](src_lang_interface.html#Translation)

### Translations

Re-exports [Translations](src_lang_interface.html#Translations)

## Properties

### default

default: [LangPacs](src_lang_interface.html#LangPacs)