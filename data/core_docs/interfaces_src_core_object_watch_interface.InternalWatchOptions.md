# Interface InternalWatchOptions
### Hierarchy

* [WatchOptions](src_core_object_watch_interface.WatchOptions.html)
  + InternalWatchOptions

## Index

### Properties

* [collapse](src_core_object_watch_interface.InternalWatchOptions.html#collapse)
* [deep](src_core_object_watch_interface.InternalWatchOptions.html#deep)
* [dependencies](src_core_object_watch_interface.InternalWatchOptions.html#dependencies)
* [engine](src_core_object_watch_interface.InternalWatchOptions.html#engine)
* [eventFilter](src_core_object_watch_interface.InternalWatchOptions.html#eventFilter)
* [fromProto](src_core_object_watch_interface.InternalWatchOptions.html#fromProto)
* [immediate](src_core_object_watch_interface.InternalWatchOptions.html#immediate)
* [pathModifier](src_core_object_watch_interface.InternalWatchOptions.html#pathModifier)
* [postfixes](src_core_object_watch_interface.InternalWatchOptions.html#postfixes)
* [prefixes](src_core_object_watch_interface.InternalWatchOptions.html#prefixes)
* [tiedWith](src_core_object_watch_interface.InternalWatchOptions.html#tiedWith)
* [withProto](src_core_object_watch_interface.InternalWatchOptions.html#withProto)

## Properties

### Optional collapse

collapse?: boolean

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[collapse](src_core_object_watch_interface.WatchOptions.html#collapse)

* Defined in [src/core/object/watch/interface.ts:154](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L154)

The option enables or disables collapsing of mutation events.
When it toggles to `true`, all mutation events fire as if they occur on top properties of the watchable object.

```
const {proxy} = watch({a: {b: {c: 1}}}, {collapse: true, deep: true}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// {b: {c: 2}} {b: {c: 2}} ['a', 'b', 'c']  
proxy.a.b.c = 2;
```

When it toggles to `false,` and the watcher binds to the specified path, the callback takes a list of mutations.
Otherwise, the callback takes only the last mutation.

```
const {proxy} = watch({a: {b: {c: 1}}}, 'a.b', {collapse: false}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path, info.originalPath);  
  });  
});  
  
// 2 1 ['a', 'b'] ['a', 'b', 'c']  
proxy.a.b.c = 2;  
  
const {proxy: proxy2} = watch({a: {b: {c: 1}}}, 'a.b', (value, oldValue, info) => {  
  console.log(value, oldValue, info.path, info.originalPath);  
});  
  
// {c: 2} {c: 2} ['a', 'b'] ['a', 'b', 'c']  
proxy2.a.b.c = 2;
```

default
:   `false`

### Optional deep

deep?: boolean

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[deep](src_core_object_watch_interface.WatchOptions.html#deep)

* Defined in [src/core/object/watch/interface.ts:68](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L68)

If true, then the callback of changing is also fired on mutations of nested properties

default
:   `false`

example
:   ```
    const {proxy} = watch({a: {b: {c: 1}}}, {deep: true}, (mutations) => {  
      mutations.forEach(([value, oldValue, info]) => {  
        console.log(value, oldValue, info.path);  
      });  
    });  
      
    // 2 1 ['a', 'b', 'c']  
    proxy.a.b.c = 2;  
      
    // {c: 2} {e: 2} ['a', 'b']  
    proxy.a.b = {e: 2};
    ```

### Optional dependencies

dependencies?: [WatchDependencies](../modules/src_core_object_watch_interface.html#WatchDependencies)

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[dependencies](src_core_object_watch_interface.WatchOptions.html#dependencies)

* Defined in [src/core/object/watch/interface.ts:343](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L343)

When providing the specific path to watch, this parameter can contain a list of dependencies for the watching path.
This parameter can help to watch accessors.

```
const obj = {  
  get foo() {  
    return this.bla * this.baz;  
  },  
  
  bla: 2,  
  baz: 3  
};  
  
const {proxy} = watch(obj, 'foo', {dependencies: ['bla', 'baz']}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path, info.originalPath, info.parent);  
});  
  
// This mutation will invoke our callback  
proxy.bla++;
```

When providing the specific path to watch, this parameter can contain an object or `Map` with lists of
dependencies to watch.

```
const obj = {  
  foo: {  
    get value() {  
      return this.bla * this.baz;  
    }  
  },  
  
  bla: 2,  
  baz: 3  
};  
  
const depsAsObj = {  
  'foo.value': ['bla', 'baz']  
};  
  
const {proxy: proxy1} = watch(obj, {dependencies: depsAsObj}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path, info.originalPath, info.parent);  
  });  
});  
  
// This mutation will fire an additional event for `foo.value`  
proxy1.bla++;  
  
const depsAsMap = new Map([  
  [  
    // A path to the property with dependencies  
    ['foo', 'value'],  
  
    // Dependencies  
    ['bla', 'baz']  
  ]  
]);  
  
const {proxy: proxy2} = watch(obj, {dependencies: depsAsMap}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path, info.originalPath, info.parent);  
  });  
});  
  
proxy2.baz++;
```

### Optional engine

engine?: [WatchEngine](src_core_object_watch_interface.WatchEngine.html)

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[engine](src_core_object_watch_interface.WatchOptions.html#engine)

* Defined in [src/core/object/watch/interface.ts:349](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L349)

Watch engine to use.
By default, will be used proxy if supported, otherwise accessors.

### Optional eventFilter

eventFilter?: [WatchHandler](src_core_object_watch_interface.WatchHandler.html)<unknown, unknown>

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[eventFilter](src_core_object_watch_interface.WatchOptions.html#eventFilter)

* Defined in [src/core/object/watch/interface.ts:198](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L198)

A filter function for mutation events.
The function allows skipping some mutation events.

example
:   ```
    function eventFilter(value, oldValue, info) {  
      return info.path[0] !== '_a';  
    }  
      
    const {proxy} = watch({a: 1, b: 2, _a: 1}, {eventFilter}, (mutations) => {  
      mutations.forEach(([value, oldValue, info]) => {  
        console.log(value, oldValue, info.path, info.originalPath);  
      });  
    });  
      
    // This mutation won't invoke our callback  
    proxy._a = 2;
    ```

### Optional fromProto

fromProto?: boolean | 1

* Defined in [src/core/object/watch/interface.ts:376](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L376)

### Optional immediate

immediate?: boolean

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[immediate](src_core_object_watch_interface.WatchOptions.html#immediate)

* Defined in [src/core/object/watch/interface.ts:114](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L114)

If true, then all mutation events will be fired immediately.
Notice, with enabling this option, the callback changes its interface:

```
// Before  
type Cb = (mutations: [[unknown, unknown, WatchHandlerParams]]) => any;  
  
// After  
type CbWithImmediate = (newValue: unknown, oldValue: unknown, info: WatchHandlerParams) => any;
```

default
:   `false`

example
:   ```
    const {proxy} = watch(a: 1}, {immediate: true}, (value, oldValue, info) => {  
      console.log(value, oldValue, info.path);  
    });  
      
    // 2 1 ['a']  
    proxy.a = 2;
    ```

### Optional pathModifier

pathModifier?: [PathModifier](src_core_object_watch_interface.PathModifier.html)

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[pathModifier](src_core_object_watch_interface.WatchOptions.html#pathModifier)

* Defined in [src/core/object/watch/interface.ts:176](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L176)

A function that takes a path of the mutation event and returns a new path.
The function is used when you want to mask one mutation to another one.

example
:   ```
    function pathModifier(path) {  
      return path.map((chunk) => chunk.replace(/^_/, ''));  
    }  
      
    const {proxy} = watch({a: 1, b: 2, _a: 1}, 'a', {pathModifier}, (mutations) => {  
      mutations.forEach(([value, oldValue, info]) => {  
        console.log(value, oldValue, info.path, info.originalPath);  
      });  
    });  
      
    // 2 1 ['a'], ['_a']  
    proxy._a = 2;
    ```

### Optional postfixes

postfixes?: string[]

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[postfixes](src_core_object_watch_interface.WatchOptions.html#postfixes)

* Defined in [src/core/object/watch/interface.ts:272](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L272)

List of postfixes for paths to watch.
This parameter can help to watch accessors.

example
:   ```
    const obj = {  
      get foo() {  
        return this.fooStore * 2;  
      },  
      
      fooStore: 2  
    };  
      
    const {proxy} = watch(obj, 'foo', {postfixes: ['Store']}, (value, oldValue, info) => {  
      console.log(value, oldValue, info.path, info.originalPath, info.parent);  
    });  
      
    // This mutation will invoke our callback  
    proxy.fooStore++;
    ```

### Optional prefixes

prefixes?: string[]

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[prefixes](src_core_object_watch_interface.WatchOptions.html#prefixes)

* Defined in [src/core/object/watch/interface.ts:248](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L248)

List of prefixes for paths to watch.
This parameter can help to watch accessors.

example
:   ```
    const obj = {  
      get foo() {  
        return this._foo * 2;  
      },  
      
      _foo: 2  
    };  
      
    const {proxy} = watch(obj, 'foo', {prefixes: ['_']}, (value, oldValue, info) => {  
      console.log(value, oldValue, info.path, info.originalPath, info.parent);  
    });  
      
    // This mutation will invoke our callback  
    proxy._foo++;
    ```

### Optional tiedWith

tiedWith?: object

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[tiedWith](src_core_object_watch_interface.WatchOptions.html#tiedWith)

* Defined in [src/core/object/watch/interface.ts:224](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L224)

Link to an object that should connect with the watched object, i.e.,
changing of properties of the tied object, will also emit mutation events

example
:   ```
    const data = {  
      foo: 2  
    };  
      
    class Bla {  
      data = data;  
      
      constructor() {  
        watch(this.data, {tiedWith: this}, (val) => {  
          console.log(val);  
        });  
      }  
    }  
      
    const bla = new Bla();  
    bla.foo = 3;
    ```

### Optional withProto

withProto?: boolean

Inherited from [WatchOptions](src_core_object_watch_interface.WatchOptions.html).[withProto](src_core_object_watch_interface.WatchOptions.html#withProto)

* Defined in [src/core/object/watch/interface.ts:89](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/interface.ts#L89)

If true, then the callback of changing is also fired on mutations of properties from prototypes

default
:   `false`

example
:   ```
    const {proxy} = watch(a: 1, {__proto__: {b: 1}}, {withProto: true}, (mutations) => {  
      mutations.forEach(([value, oldValue, info]) => {  
        console.log(value, oldValue, info.path, info.fromProto);  
      });  
    });  
      
    // 2 1 ['a'] false  
    proxy.a = 2;  
      
    // 2 1 ['b'] true  
    proxy.b = 2;
    ```