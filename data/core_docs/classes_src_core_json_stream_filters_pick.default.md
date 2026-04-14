# Class default
### Hierarchy

* [default](src_core_json_stream_filters_abstract_filter.default.html)
  + default

## Index

### Constructors

* [constructor](src_core_json_stream_filters_pick.default.html#constructor)

### Properties

* [depth](src_core_json_stream_filters_pick.default.html#depth)
* [expectedToken](src_core_json_stream_filters_pick.default.html#expectedToken)
* [filter](src_core_json_stream_filters_pick.default.html#filter)
* [multiple](src_core_json_stream_filters_pick.default.html#multiple)
* [passKey](src_core_json_stream_filters_pick.default.html#passKey)
* [passNumber](src_core_json_stream_filters_pick.default.html#passNumber)
* [passString](src_core_json_stream_filters_pick.default.html#passString)
* [previousToken](src_core_json_stream_filters_pick.default.html#previousToken)
* [skipKey](src_core_json_stream_filters_pick.default.html#skipKey)
* [skipNumber](src_core_json_stream_filters_pick.default.html#skipNumber)
* [skipString](src_core_json_stream_filters_pick.default.html#skipString)
* [stack](src_core_json_stream_filters_pick.default.html#stack)

### Accessors

* [processToken](src_core_json_stream_filters_pick.default.html#processToken)

### Methods

* [check](src_core_json_stream_filters_pick.default.html#check)
* [checkToken](src_core_json_stream_filters_pick.default.html#checkToken)
* [finishTokenProcessing](src_core_json_stream_filters_pick.default.html#finishTokenProcessing)
* [pass](src_core_json_stream_filters_pick.default.html#pass)
* [passObject](src_core_json_stream_filters_pick.default.html#passObject)
* [passValue](src_core_json_stream_filters_pick.default.html#passValue)
* [skip](src_core_json_stream_filters_pick.default.html#skip)
* [skipObject](src_core_json_stream_filters_pick.default.html#skipObject)
* [skipValue](src_core_json_stream_filters_pick.default.html#skipValue)
* [createPathFilter](src_core_json_stream_filters_pick.default.html#createPathFilter)
* [createRegExpFilter](src_core_json_stream_filters_pick.default.html#createRegExpFilter)

## Constructors

### constructor

* new default(filter: [TokenFilter](../modules/src_core_json_stream_filters_interface.html#TokenFilter), opts?: [FilterOptions](../interfaces/src_core_json_stream_filters_interface.FilterOptions.html)): [default](src_core_json_stream_filters_pick.default.html)

* Overrides [default](src_core_json_stream_filters_abstract_filter.default.html).[constructor](src_core_json_stream_filters_abstract_filter.default.html#constructor)

  + Defined in [src/core/json/stream/filters/pick.ts:15](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/pick.ts#L15)

  #### Parameters

  + ##### filter: [TokenFilter](../modules/src_core_json_stream_filters_interface.html#TokenFilter)
  + ##### Optional opts: [FilterOptions](../interfaces/src_core_json_stream_filters_interface.FilterOptions.html)

  #### Returns [default](src_core_json_stream_filters_pick.default.html)

## Properties

### Protected depth

depth: number = 0

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[depth](src_core_json_stream_filters_abstract_filter.default.html#depth)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:110](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L110)

Depth of the current structure

### Protected Optional expectedToken

expectedToken?: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[expectedToken](src_core_json_stream_filters_abstract_filter.default.html#expectedToken)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:120](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L120)

Name of the next expected token from a stream

### Protected filter

filter: [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[filter](src_core_json_stream_filters_abstract_filter.default.html#filter)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:100](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L100)

Function to filter a sequence of parsed tokens

param stack

param chunk

### Readonly multiple

multiple: boolean = false

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[multiple](src_core_json_stream_filters_abstract_filter.default.html#multiple)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:72](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L72)

If true the filtration will return all matched filter results, otherwise only the first match will be returned

### Protected Readonly passKey

passKey: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)> = ...

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[passKey](src_core_json_stream_filters_abstract_filter.default.html#passKey)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:145](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L145)

Method to pass key tokens

### Protected Readonly passNumber

passNumber: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)> = ...

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[passNumber](src_core_json_stream_filters_abstract_filter.default.html#passNumber)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:125](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L125)

Method to pass numeric tokens

### Protected Readonly passString

passString: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)> = ...

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[passString](src_core_json_stream_filters_abstract_filter.default.html#passString)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:135](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L135)

Method to pass string tokens

### Protected previousToken

previousToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName) = ''

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[previousToken](src_core_json_stream_filters_abstract_filter.default.html#previousToken)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:115](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L115)

Name of the previous parsed token

### Protected Readonly skipKey

skipKey: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)> = ...

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[skipKey](src_core_json_stream_filters_abstract_filter.default.html#skipKey)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:150](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L150)

Method to skip key tokens

### Protected Readonly skipNumber

skipNumber: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)> = ...

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[skipNumber](src_core_json_stream_filters_abstract_filter.default.html#skipNumber)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:130](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L130)

Method to skip numeric tokens

### Protected Readonly skipString

skipString: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)> = ...

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[skipString](src_core_json_stream_filters_abstract_filter.default.html#skipString)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:140](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L140)

Method to skip string tokens

### Protected stack

stack: [FilterStack](../modules/src_core_json_stream_filters_interface.html#FilterStack) = []

Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[stack](src_core_json_stream_filters_abstract_filter.default.html#stack)

* Defined in [src/core/json/stream/filters/abstract-filter.ts:105](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L105)

Stack of processed tokens

## Accessors

### processToken

* get processToken(): [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>
* set processToken(val: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>): void

* Inherited from Super.processToken

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:77](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L77)

  Processes the passed JSON token and yields tokens

  #### Returns [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>
* Inherited from Super.processToken

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:84](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L84)

  Sets a new process function to parse JSON chunk and yield tokens

  #### Parameters

  + ##### val: [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>

  #### Returns void

## Methods

### Protected check

* check(token: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)): Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[check](src_core_json_stream_filters_abstract_filter.default.html#check)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:186](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L186)

  Check the specified token for filter satisfaction

  #### Parameters

  + ##### token: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)

  #### Returns Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

### Protected checkToken

* checkToken(chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)): Generator<boolean | [Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>

* Overrides [default](src_core_json_stream_filters_abstract_filter.default.html).[checkToken](src_core_json_stream_filters_abstract_filter.default.html#checkToken)

  + Defined in [src/core/json/stream/filters/pick.ts:20](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/pick.ts#L20)

  Checks that specified token is matched for the filter

  #### Parameters

  + ##### chunk: [Token](../interfaces/src_core_json_stream_parser_interface.Token.html)

  #### Returns Generator<boolean | [Token](../interfaces/src_core_json_stream_parser_interface.Token.html), any, unknown>

### finishTokenProcessing

* finishTokenProcessing(): Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[finishTokenProcessing](src_core_json_stream_filters_abstract_filter.default.html#finishTokenProcessing)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:178](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L178)

  Closes all unclosed tokens and returns a Generator of filtered tokens.
  The method must be called after the end of filtration.

  #### Returns Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

### Protected pass

* pass(token: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)): Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[pass](src_core_json_stream_filters_abstract_filter.default.html#pass)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:275](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L275)

  Passes the passed token into an output token stream

  #### Parameters

  + ##### token: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)

  #### Returns Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

### Protected passObject

* passObject(token: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)): Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[passObject](src_core_json_stream_filters_abstract_filter.default.html#passObject)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:291](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L291)

  Passes the passed object token into an output token stream

  #### Parameters

  + ##### token: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)

  #### Returns Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

### Protected passValue

* passValue(currentToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName), expectedToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)): [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[passValue](src_core_json_stream_filters_abstract_filter.default.html#passValue)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:352](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L352)

  Creates a function to pass tokens into an output token stream

  #### Parameters

  + ##### currentToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)
  + ##### expectedToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)

  #### Returns [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>

### Protected skip

* skip(\_: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)): Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[skip](src_core_json_stream_filters_abstract_filter.default.html#skip)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:283](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L283)

  Skips the passed token from an output token stream

  #### Parameters

  + ##### \_: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)

  #### Returns Generator<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html), any, unknown>

### Protected skipObject

* skipObject(chunk: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)): void

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[skipObject](src_core_json_stream_filters_abstract_filter.default.html#skipObject)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:324](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L324)

  Skips the passed object token from an output token stream

  #### Parameters

  + ##### chunk: [FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)

  #### Returns void

### Protected skipValue

* skipValue(currentToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName), expectedToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)): [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[skipValue](src_core_json_stream_filters_abstract_filter.default.html#skipValue)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:394](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L394)

  Creates a function to skip tokens from an output token stream

  #### Parameters

  + ##### currentToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)
  + ##### expectedToken: [TokenName](../modules/src_core_json_stream_parser_interface.html#TokenName)

  #### Returns [TokenProcessorFn](../interfaces/src_core_json_stream_parser_interface.TokenProcessorFn.html)<[FilterToken](../interfaces/src_core_json_stream_filters_interface.FilterToken.html)>

### Static createPathFilter

* createPathFilter(path: string): [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[createPathFilter](src_core_json_stream_filters_abstract_filter.default.html#createPathFilter)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:38](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L38)

  Creates a function to filter only chunks by the specified path

  example
  :   ```
      const filter = createPathFilter('foo.bla.bar');
      ```

  #### Parameters

  + ##### path: string

  #### Returns [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)

### Static createRegExpFilter

* createRegExpFilter(rgxp: RegExp): [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)

* Inherited from [default](src_core_json_stream_filters_abstract_filter.default.html).[createRegExpFilter](src_core_json_stream_filters_abstract_filter.default.html#createRegExpFilter)

  + Defined in [src/core/json/stream/filters/abstract-filter.ts:65](https://github.com/V4Fire/Core/blob/master/src/core/json/stream/filters/abstract-filter.ts#L65)

  Creates a function to filter only chunks with paths matched to the specified regular expression

  example
  :   ```
      const filter = createRegExpFilter(/\d+\.foo\.bar/);
      ```

  #### Parameters

  + ##### rgxp: RegExp

  #### Returns [TokenFilterFn](../interfaces/src_core_json_stream_filters_interface.TokenFilterFn.html)