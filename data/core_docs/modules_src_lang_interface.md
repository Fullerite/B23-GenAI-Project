# Module src/lang/interface
## Index

### Type aliases

* [KeysetTranslations](src_lang_interface.html#KeysetTranslations)
* [LangPacs](src_lang_interface.html#LangPacs)
* [PluralTranslation](src_lang_interface.html#PluralTranslation)
* [Translation](src_lang_interface.html#Translation)
* [Translations](src_lang_interface.html#Translations)

## Type aliases

### KeysetTranslations

KeysetTranslations: [Dictionary](../interfaces/index.Dictionary.html)<[Translations](src_lang_interface.html#Translations)>

* Defined in [src/lang/interface.ts:19](https://github.com/V4Fire/Core/blob/master/src/lang/interface.ts#L19)

### LangPacs

LangPacs: { [ key in [Language](index.html#Language)]?: [KeysetTranslations](src_lang_interface.html#KeysetTranslations) }

* Defined in [src/lang/interface.ts:9](https://github.com/V4Fire/Core/blob/master/src/lang/interface.ts#L9)

### PluralTranslation

PluralTranslation: [one: string, some: string, many: string, none: string]

* Defined in [src/lang/interface.ts:15](https://github.com/V4Fire/Core/blob/master/src/lang/interface.ts#L15)

### Translation

Translation: string | [PluralTranslation](src_lang_interface.html#PluralTranslation)

* Defined in [src/lang/interface.ts:13](https://github.com/V4Fire/Core/blob/master/src/lang/interface.ts#L13)

### Translations

Translations: [Dictionary](../interfaces/index.Dictionary.html)<[Translation](src_lang_interface.html#Translation)>

* Defined in [src/lang/interface.ts:17](https://github.com/V4Fire/Core/blob/master/src/lang/interface.ts#L17)