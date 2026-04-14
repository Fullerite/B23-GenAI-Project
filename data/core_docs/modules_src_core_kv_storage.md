# Module src/core/kv-storage
[# core/kv-storage](#corekv-storage)

This module provides API to work with a persistent key-value storage using different runtime engines, like localStorage,
indexedDb, SQLite, etc.

[## Supported engines](#supported-engines)

* `browser-localstorage`
* `browser-indexeddb`
* `node-localstorage`

[## API](#api)
[### Synchronous and asynchronous API](#synchronous-and-asynchronous-api)

The module has interfaces to work with storage in a synchronous and asynchronous way.
In the case of asynchronous API, all defined methods have the same input parameters as the synchronous API but return promises.
Notice, not each engine implements the synchronous API, so we recommend preferring to use asynchronous API in most cases.

[### API structure](#api-structure)

Both API exposes methods to implement simple CRUD operations.

[#### has](#has)

Returns true if a value by the specified key exists in the storage.
Notice, the method can take a list of additional parameters provided to the used storage' engine.

```
import * as kv from 'core/kv-storage';  
  
kv.set('bla', 1);  
console.log(kv.has('bla') === true);
```

[#### get](#get)

Returns a value from the storage by the specified key.

The returning value automatically parses by using `Object.parse` from a string to equivalent JS value, i.e.,
`'1'` will be parsed to `1`, `'true'` to `true`, `'2021-07-09T08:15:57.753Z'` to `Date`, etc.

Notice, the method can take a list of additional parameters provided to the used storage' engine.

```
import * as kv from 'core/kv-storage';  
  
kv.set('bla', 1);  
console.log(kv.get('bla') === 1);
```

[#### set](#set)

Saves a value to the storage by the specified key.

The value to parse automatically serializes to a string by using `Object.trySerialize`, i.e.,
arrays and dictionaries will be serialized to JSON, etc.

Notice, the method can take a list of additional parameters provided to the used storage' engine.

```
import * as kv from 'core/kv-storage';  
  
kv.set('bla', {a: 1});  
console.log(kv.get('bla').a === 1);
```

[#### remove](#remove)

Removes a value from the storage by the specified key.
Notice, the method can take a list of additional parameters provided to the used storage' engine.

```
import * as kv from 'core/kv-storage';  
  
kv.set('bla', 1);  
console.log(kv.has('bla') === true);  
  
kv.remove('bla');  
console.log(kv.has('bla') === false);
```

[#### clear](#clear)

Clears the storage by the specified filter and returns a list of removed keys.
Notice, the method can take a list of additional parameters provided to the used storage' engine.

```
import * as kv from 'core/kv-storage';  
  
kv.set('bla', 1);  
kv.set('bla2', 2);  
  
// ['bla']  
kv.clear((el, key) => el === 1);  
  
console.log(kv.has('bla') === false);  
console.log(kv.has('bla2') === true);  
  
// ['bla2']  
kv.clear();  
  
console.log(kv.has('bla2') === false);
```

[#### namespace](#namespace)

All values are stored within a local storage in the global namespace, i.e., you can override any value you have.
If you want to isolate data from other data, you can specify the custom namespace. Mind, you still can override or remove these
values from the storage by using global API.

```
import * as kv from 'core/kv-storage';  
  
kv.set('bla', 1);  
  
const blaStore = kv.namespace('[[BLA]]');  
  
blaStore.set('baz', true);  
blaStore.clear();  
  
console.log(kv.has('bla') === true);  
  
blaStore.set('foo', 1);  
  
kv.clear();  
console.log(blaStore.has('foo') === false);
```

[### Asynchronous API](#asynchronous-api)

If you need to work with an asynchronous local storage, you can use `asyncLocal. The API is pretty similar to local, but its
methods return a promise instead of a raw result.

```
import { asyncLocal } from 'core/kv-storage';  
  
asyncLocal.set('bla', 1).then(async () => {  
  console.log(await asyncLocal.get('bla') === 1);  
});  
  
const blaStore = asyncLocal.namespace('[[BLA]]');  
  
blaStore.set('bla', 1).then(async () => {  
  console.log(await blaStore.get('bla') === 1);  
});
```

[### Session API](#session-api)

If you need to store data only during the active session, you can use `session` and `asyncSession` API-s.

```
import { session, asyncSession } from 'core/kv-storage';  
  
session.set('bla', 1);  
console.log(session.get('bla') === 1);  
session.clear();  
  
asyncSession.set('bla', 1).then(async () => {  
  console.log(await asyncSession.get('bla') === 1);  
});  
  
const blaStore = asyncSession.namespace('[[BLA]]');  
  
blaStore.set('bla', 1).then(async () => {  
  console.log(await blaStore.get('bla') === 1);  
});
```

[### Providing API as a strategy](#providing-api-as-a-strategy)

You can pass your storage API as a strategy to another function or method.

```
import { local, asyncLocal, SyncStorage, AsyncStorage } from 'core/kv-storage';  
  
function save(kv: SyncStorage): void {  
  kv.set('bla', 1);  
  console.log(kv.get('bla') === 1);  
  console.log(kv.has('bla') === true);  
  
  kv.set('obj', {a: 1});  
  console.log(kv.get('obj').a === 1);  
  
  kv.remove('bla');  
  kv.clear((el, key) => el.a === 1);  
}  
  
save(local);  
  
function asyncSave(kv: AsyncStorage): void {  
  asyncLocal.set('bla', 1).then(async () => {  
    console.log(await asyncLocal.get('bla') === 1);  
  });  
}  
  
save(asyncLocal);
```

[## Specifying engines to store](#specifying-engines-to-store)

By default, in a browser, the module uses native `window.localStorage` and `window.sessionStorage` API-s.
Also, there is a storage based on `IndexedDb`. Use the `factory` method to specify an engine to store.

```
import { factory } from 'core/kv-storage';  
import * as idb from 'core/kv-storage/engines/browser-indexeddb';  
  
const asyncStorage = factory(idb.asyncLocalStorage, true);  
  
asyncStorage.set('bla', 1).then(async () => {  
  console.log(await asyncLocal.get('bla') === 1);  
});  
  
const asyncSessionStorage = factory(idb.asyncSessionStorage, true);
```

[### Specifying a custom engine](#specifying-a-custom-engine)

You can specify your engine by using the `factory` method.

```
import { factory } from 'core/kv-storage';  
  
const syncStorage = factory(YourSyncStorage);  
const asyncStorage = factory(YourAsyncStorage, true);
```

The wrapped engine need to have CRUD methods from the interface:

```
interface StorageEngine {  
  get?(key: unknown): unknown;  
  getItem?(key: unknown): unknown;  
  set?(key: unknown, value: unknown): unknown;  
  setItem?(key: unknown, value: unknown): unknown;  
  remove?(key: unknown): unknown;  
  removeItem?(key: unknown): unknown;  
  delete?(key: unknown): unknown;  
  exist?(key: unknown): unknown;  
  exists?(key: unknown): unknown;  
  includes?(key: unknown): unknown;  
  has?(key: unknown): unknown;  
  keys?(): Iterable<unknown>;  
  clear?(): unknown;  
  clearAll?(): unknown;  
  truncate?(): unknown;  
}
```

## Index

### References

* [AsyncStorage](src_core_kv_storage.html#AsyncStorage)
* [AsyncStorageNamespace](src_core_kv_storage.html#AsyncStorageNamespace)
* [ClearFilter](src_core_kv_storage.html#ClearFilter)
* [StorageEngine](src_core_kv_storage.html#StorageEngine)
* [SyncStorage](src_core_kv_storage.html#SyncStorage)
* [SyncStorageNamespace](src_core_kv_storage.html#SyncStorageNamespace)

### Variables

* [asyncLocal](src_core_kv_storage.html#asyncLocal)
* [asyncSession](src_core_kv_storage.html#asyncSession)
* [clear](src_core_kv_storage.html#clear)
* [get](src_core_kv_storage.html#get)
* [has](src_core_kv_storage.html#has)
* [local](src_core_kv_storage.html#local)
* [namespace](src_core_kv_storage.html#namespace)
* [remove](src_core_kv_storage.html#remove)
* [session](src_core_kv_storage.html#session)
* [set](src_core_kv_storage.html#set)

### Functions

* [factory](src_core_kv_storage.html#factory)

## References

### AsyncStorage

Re-exports [AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html)

### AsyncStorageNamespace

Re-exports [AsyncStorageNamespace](src_core_kv_storage_interface.html#AsyncStorageNamespace)

### ClearFilter

Re-exports [ClearFilter](../interfaces/src_core_kv_storage_interface.ClearFilter.html)

### StorageEngine

Re-exports [StorageEngine](../interfaces/src_core_kv_storage_interface.StorageEngine.html)

### SyncStorage

Re-exports [SyncStorage](../interfaces/src_core_kv_storage_interface.SyncStorage.html)

### SyncStorageNamespace

Re-exports [SyncStorageNamespace](../interfaces/src_core_kv_storage_interface.SyncStorageNamespace.html)

## Variables

### Const asyncLocal

asyncLocal: [AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html) = ...

* Defined in [src/core/kv-storage/index.ts:59](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L59)

API for asynchronous local storage

example
:   ```
    asyncLocal.set('foo', 'bar').then(async () => {  
      console.log(await asyncLocal.get('foo')); // 'foo'  
    });
    ```

### Const asyncSession

asyncSession: [AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html) = ...

* Defined in [src/core/kv-storage/index.ts:82](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L82)

API for asynchronous session storage

example
:   ```
    asyncSession.set('foo', 'bar').then(async () => {  
      console.log(await asyncSession.get('foo')); // 'foo'  
    });
    ```

### Const clear

clear: any = ...

* Defined in [src/core/kv-storage/index.ts:122](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L122)

Alias for a clear method of the synchronous local storage API

alias

see
:   [local](src_core_kv_storage.html#local)

### Const get

get: any = ...

* Defined in [src/core/kv-storage/index.ts:98](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L98)

Alias for a get method of the synchronous local storage API

alias

see
:   [local](src_core_kv_storage.html#local)

### Const has

has: any = ...

* Defined in [src/core/kv-storage/index.ts:90](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L90)

Alias for a has method of the synchronous local storage API

alias

see
:   [local](src_core_kv_storage.html#local)

### Const local

local: [SyncStorage](../interfaces/src_core_kv_storage_interface.SyncStorage.html) = ...

* Defined in [src/core/kv-storage/index.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L47)

API for synchronous local storage

example
:   ```
    local.set('foo', 'bar');  
    local.get('foo'); // 'foo'
    ```

### Const namespace

namespace: any = ...

* Defined in [src/core/kv-storage/index.ts:138](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L138)

Alias for a namespace method of the synchronous local storage API

alias

see
:   [local](src_core_kv_storage.html#local)

example
:   ```
    const storage = namespace('REQUEST_STORAGE');  
    storage.set('foo', 'bar');  
    storage.get('foo'); // 'foo'  
    local.get('foo'); // undefined
    ```

### Const remove

remove: any = ...

* Defined in [src/core/kv-storage/index.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L114)

Alias for a remove method of the synchronous local storage API

alias

see
:   [local](src_core_kv_storage.html#local)

### Const session

session: [SyncStorage](../interfaces/src_core_kv_storage_interface.SyncStorage.html) = ...

* Defined in [src/core/kv-storage/index.ts:70](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L70)

API for synchronous session storage

example
:   ```
    session.set('foo', 'bar');  
    session.get('foo'); // 'foo'
    ```

### Const set

set: any = ...

* Defined in [src/core/kv-storage/index.ts:106](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L106)

Alias for a set method of the synchronous local storage API

alias

see
:   [local](src_core_kv_storage.html#local)

## Functions

### factory

* factory(engine: [StorageEngine](../interfaces/src_core_kv_storage_interface.StorageEngine.html), async: true): [AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html)
* factory(engine: [StorageEngine](../interfaces/src_core_kv_storage_interface.StorageEngine.html), async?: false): [SyncStorage](../interfaces/src_core_kv_storage_interface.SyncStorage.html)

* + Defined in [src/core/kv-storage/index.ts:153](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L153)

  Creates a new kv-storage API with the specified engine

  example
  :   ```
      const storage = factory(window.localStorage);  
      storage.set('foo', 'bar');  
      storage.get('foo'); // 'foo'
      ```

  #### Parameters

  + ##### engine: [StorageEngine](../interfaces/src_core_kv_storage_interface.StorageEngine.html)
  + ##### async: true

    if true, then the storage is implemented async interface

  #### Returns [AsyncStorage](../interfaces/src_core_kv_storage_interface.AsyncStorage.html)
* + Defined in [src/core/kv-storage/index.ts:154](https://github.com/V4Fire/Core/blob/master/src/core/kv-storage/index.ts#L154)

  #### Parameters

  + ##### engine: [StorageEngine](../interfaces/src_core_kv_storage_interface.StorageEngine.html)
  + ##### Optional async: false

  #### Returns [SyncStorage](../interfaces/src_core_kv_storage_interface.SyncStorage.html)