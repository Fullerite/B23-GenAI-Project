# Module src/core/object/watch
[# core/object/watch](#coreobjectwatch)

The module provides API to watch changes of JS objects, like, maps, arrays, etc.
The watching supports different strategies:

* based on rewriting property accessors (ES5 runtime);
* based on JS Proxy objects (ES6 runtime).

By default, if runtime supports Proxy objects, then will be used an approach based on these objects.
Otherwise, will be used a strategy based on accessors. Also, you can manually define a strategy to use for each watcher.

```
import watch from 'core/object/watch';  
  
const obj = {  
  a: 1,  
  b: [],  
  c: new Map(),  
  d: {}  
};  
  
const {proxy, unwatch} = watch(obj, {deep: true, immediate: true}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path);  
});  
  
proxy.a++;  
proxy.b.push(1);  
proxy.c.set(1, 2);  
proxy.d.foo = 'bar';  
  
unwatch();
```

[## Known limitations](#known-limitations)

1. The assessors' based engine doesn't watch array indices. To add or remove new elements to an array, use array methods.
   Or, you can use `set/unset` methods from a watcher to add or remove elements by a path.
2. The assessors' based engine doesn't watch newly added elements.
   To add watching for these properties, use `set/unset` methods from a watcher to add or remove elements by a path.
3. To watch invoking of mutating methods, like `add` or `delete`, the watcher wraps the original methods of the passed object.

[## How it works?](#how-it-works)

The module provides a function to watch changes. It takes an object to watch, optionally some watching options,
and a callback function that accumulates mutations and invokes on the next tick after the first mutation.
After this, the function returns API to watch changes. The API has an interface below.

```
export interface Watcher<T extends object = object> {  
  /**  
   * A proxy object to watch  
   */  
  proxy: T;  
  
  /**  
   * Sets a new watchable value for the proxy object by the specified path  
   *  
   * @param path  
   * @param value  
   */  
  set(path: WatchPath, value: unknown): void;  
  
  /**  
   * Deletes a watchable value from the proxy object by the specified path  
   * @param path  
   */  
  delete(path: WatchPath): void;  
  
  /**  
   * Cancels watching for the proxy object  
   */  
  unwatch(): void;  
}
```

The function to watch supports: objects, arrays, Map-s, Set-s.

```
import watch from 'core/object/watch';  
  
const user = new Map([  
  ['name', 'Kobezzza'],  
  ['age', 31]  
]);  
  
const {proxy} = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// This mutation will invoke our callback  
proxy.set('name', 'Andrey');
```

Notice, the function creates a new object that wraps the original and adds the watching functionality.
The new object is connected to the original, and if you change the value of some property of the proxy object,
it will affect the original object. The connection works with the reverted direction too, when you change the original object,
but in this case, you can't watch these mutations.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const {proxy} = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// This mutation will invoke our callback  
proxy.name = 'Andrey';  
  
// This mutation won't invoke our callback  
user.age++;
```

Also, the API provides a function to remove watching from the proxy object.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const {proxy, unwatch} = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// This mutation will invoke our callback  
proxy.name = 'Andrey';  
  
unwatch();  
  
// This mutation won't invoke our callback  
proxy.age++;
```

The rest two methods of the API allow adding or removing properties to the proxy object.
If your environment supports Proxy objects, you can add new properties without invoking `set`,
but the invoking is necessary for a strategy based on accessors.

```
import watch from 'core/object/watch';  
  
import * as proxyEngine from 'core/object/watch/engines/proxy';  
import * as accEngine from 'core/object/watch/engines/accessors';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const proxyWatcher = watch(user, {engine: proxyEngine}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// This mutation will invoke our callback  
proxyWatcher.proxy.skills = ['programming', 'JS'];  
  
const accWatcher = watch(user, {engine: accEngine}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// If we add a new property, we have to register a new accessor to watch.  
// This mutation will invoke our callback.  
accWatcher.set('skills', ['programming', 'JS']);  
  
// Now we can change it without any doubt  
accWatcher.skills = ['programming', 'JS', 'music'];
```

To delete a property from the proxy object, we can set it to `undefined`, or use the `delete` operator,
or invoke the `delete` method of the watcher. All of these methods have different semantic and work the same with any engine.
Let's watch these in action.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const watcher = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
/* ***************** */  
/* The first variant */  
/* ***************** */  
  
// This mutation will invoke our callback  
watcher.proxy.age = undefined;  
  
// true  
console.log('age' in watcher.proxy);  
  
// This mutation will invoke our callback  
watcher.proxy.age = 32;  
  
/* ****************** */  
/* The second variant */  
/* ****************** */  
  
// This mutation won't invoke our callback  
delete watcher.proxy.age;  
  
// false  
console.log('age' in watcher.proxy);  
  
// This mutation won't invoke our callback  
watcher.proxy.age = 32;  
  
// Invoke set to register a property to watch.  
// This mutation will invoke our callback.  
watcher.set('age', 31)  
  
// This mutation will invoke our callback  
watcher.proxy.age = 32;  
  
/* ***************** */  
/* The third variant */  
/* ***************** */  
  
// This mutation will invoke our callback  
watcher.delete('age');  
  
// false  
console.log('age' in watcher.proxy);  
  
// This mutation won't invoke our callback  
watcher.proxy.age = 32;  
  
// Invoke set to register a property to watch.  
// This mutation will invoke our callback.  
watcher.set('age', 31)  
  
// This mutation will invoke our callback  
watcher.proxy.age = 32;
```

[## Parameters of a mutation handler](#parameters-of-a-mutation-handler)

A function that handles mutations can take a list of mutations or a single mutation.
The list of mutations contains sub-arrays, where the first two parameters refer to new and old values of the mutated property.
The third parameter refers to an object that contains some information about a particular mutation, like, where the mutation has occurred.
In case when the function takes a single mutation, the function takes tree arguments instead of one.

```
interface WatchHandlerParams {  
  /**  
   * Link to an object that is watched  
   */  
  obj: object;  
  
  /**  
   * Link to the root object of watching  
   */  
  root: object;  
  
  /**  
   * Link to the top property of watching  
   * (the first level property of the root)  
   */  
  top?: object;  
  
  /**  
   * Information about a parent mutation event  
   */  
  parent?: WatchHandlerParentParams;  
  
  /**  
   * True if a mutation has occurred on a prototype of the watched object  
   */  
  fromProto: boolean;  
  
  /**  
   * Path to a property that was changed  
   */  
  path: unknown[];  
  
  /**  
   * The original path to a property that was changed  
   */  
  originalPath: unknown[];  
}  
  
interface WatchHandlerParentParams {  
  value: unknown;  
  oldValue: unknown;  
  info: WatchHandlerParams;  
}
```

[## Watching for the specific path](#watching-for-the-specific-path)

We can set watching not to the whole object properties, but only the property by the specified path.
To do it, just provide a path as the second parameter of the watching function.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: {  
      js: 80,  
      rust: 30  
    },  
  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, 'skills.programming', (value, oldValue, info) => {  
  console.log(value, oldValue, info.path, info.originalPath);  
});  
  
// This mutation won't invoke our callback  
proxy.name = 'Andrey';  
  
// This mutation will invoke our callback  
// {js: 81, rust: 30} {js: 81, rust: 30} ['skills', 'programming'] ['skills', 'programming', 'js']  
proxy.skills.programming.js++;  
  
// Also, we can provide a path in the array form, like, ['skills', 'programming'].  
// It helps provide a path with non-string keys.  
  
const key = {};  
  
const data = {  
  map: new Map([[key, 1]])  
};  
  
const {proxy: proxy2} = watch(data, ['map', key], (value, oldValue, info) => {  
  console.log(value, oldValue, info.originalPath);  
});  
  
proxy2.map.set(key, proxy2.map.get(key) + 1);
```

There are some nuances of using this approach:

* Because we watch the specific path, the callback function will take not a list of mutations, but just a single mutation.

  ```
  import watch from 'core/object/watch';  
    
  const user = {  
    name: 'Kobezzza',  
    skills: {  
      programming: {  
        js: 80,  
        rust: 30  
      },  
    
      singing: 10  
    }  
  };  
    
  const {proxy} = watch(user, (mutations) => {  
    mutations.forEach(([value, oldValue, info]) => {  
      console.log(value, oldValue, info.path);  
    })  
  });  
    
  const {proxy: proxyByPath} = watch(user, 'skills.programming', (value, oldValue, info) => {  
    console.log(value, oldValue, info.path);  
  });
  ```
* Mutations of nested properties that match the path also invoke the callback.
  To get a path of the mutated property, use `info.originalPath`, because `info.path` always refers to the path that we watched.

  ```
  import watch from 'core/object/watch';  
    
  const user = {  
    name: 'Kobezzza',  
    skills: {  
      programming: {  
        js: 80,  
        rust: 30  
      },  
    
      singing: 10  
    }  
  };  
    
  const {proxy: proxyByPath} = watch(user, 'skills.programming', (value, oldValue, info) => {  
    console.log(value, oldValue, info.originalPath);  
  });  
    
  // This mutation will invoke our callback  
  // info.path: ['skills', 'programming']  
  // info.originalPath: ['skills', 'programming', 'js']  
  proxyByPath.skills.programming.js++;  
    
  // This mutation will invoke our callback  
  // info.path: ['skills', 'programming']  
  // info.originalPath: ['skills', 'programming']  
  proxyByPath.skills.programming = {js: 80, rust: 30, python: 30};  
    
  // This mutation will invoke our callback  
  // info.path: ['skills', 'programming']  
  // info.originalPath: ['skills']  
  proxyByPath.skills = {programming: {js: 80, rust: 30, python: 30, haskell: 20}};
  ```
* By default, all mutations that occur on the same tick are accumulated within a mutation list.
  The provided handler function is invoked on the next tick and takes the last value from this list as an argument, i.e., it works lazily.
  To force a watcher to invoke its handler immediately after the occurred mutation, provide the `immediate` option.
  To watch the whole list of mutations, provide the `collapse` option to `false`.

  ```
  import watch from 'core/object/watch';  
    
  const user = {  
    name: 'Kobezzza',  
    skills: {  
      programming: {  
        js: 80,  
        rust: 30  
      },  
    
      singing: 10  
    }  
  };  
    
  const {proxy: collapsedProxy} = watch(user, 'skills.programming', (value, oldValue, info) => {  
    console.log(value, oldValue, info.originalPath);  
  });  
    
  collapsedProxy.skills.programming.js++;  
    
  // This mutation overwrites the previous  
  //  {js: 80, rust: 30, python: 30} {js: 81, rust: 30} ['skills', 'programming']  
  collapsedProxy.skills.programming = {js: 80, rust: 30, python: 30};  
    
  const {proxy} = watch(user, (mutations) => {  
    mutations.forEach(([value, oldValue, info]) => {  
      console.log(value, oldValue, info.originalPath);  
    })  
  });  
    
  // 81, 80, ['skills', 'programming', 'js']  
  proxy.skills.programming.js++;  
    
  // {js: 80, rust: 30} {js: 81, rust: 30, python: 30} ['skills']  
  proxy.skills = {programming: {js: 80, rust: 30}};
  ```
* The provided handler function takes new and old values of a property by the provided path.
  Notice, if a mutation of some nested property occurs, the new and old values will be equal because they refer to the same object.
  To get values of changed nested properties, provide the `collapse` option to `false`.

  ```
  import watch from 'core/object/watch';  
    
  const user = {  
    name: 'Kobezzza',  
    skills: {  
      programming: {  
        js: 80,  
        rust: 30  
      },  
    
      singing: 10  
    }  
  };  
    
  const {proxy: collapsedProxy} = watch(user, 'skills.programming', (value, oldValue, info) => {  
    console.log(value, oldValue, info.originalPath);  
  });  
    
  // {js: 81, python: 30} {js: 81, rust: 30} ['skills', 'programming', 'js']  
  collapsedProxy.skills.programming.js++;  
    
  const {proxy} = watch(user, (mutations) => {  
    mutations.forEach(([value, oldValue, info]) => {  
      console.log(value, oldValue, info.originalPath);  
    })  
  });  
    
  // 82, 81, ['skills', 'programming', 'js']  
  proxy.skills.programming.js++;
  ```

[## Separated and shared watchers](#separated-and-shared-watchers)

The important point is that the watch function doesn't mutate the passed object but creates a new object based on the original and returns it.
Only mutation of this new object will create events of modifications, and when we make another one watcher based on the original object,
they can't watch mutations of each other.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const {proxy: proxy1} = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
const {proxy: proxy2} = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
  
// proxy2 won't handle this mutation  
proxy1.name = 'Andrey';  
  
// proxy1 won't handle this mutation  
proxy2.age++;
```

If we want to share mutations between different watchers, we should invoke the watch function by providing the previous proxy object instead of the original.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const {proxy: proxy1} = watch(user, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
const {proxy: proxy2} = watch(proxy1, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
  
// proxy2 will handle this mutation  
proxy1.name = 'Andrey';  
  
// proxy1 will handle this mutation  
proxy2.age++;
```

[## Options of watching](#options-of-watching)
[### deep](#deep)

By default, are watched only mutations from the top object properties, i.e., all nested mutations, are ignored.
To enable watching of nested properties, provide the `deep` option.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: 80,  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, {deep: true}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
// This mutation will invoke our callback  
// 11 10 ['skills', 'singing']  
proxy.skills.singing++;
```

[### withProto](#withproto)

By default, all mutations of properties from a prototype of the proxy object are ignored.
To enable watching of prototype properties, provide the `withProto` option.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  __proto__: {  
    age: 31  
  }  
};  
  
const {proxy} = watch(user, {withProto: true}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path, info.fromProto);  
  });  
});  
  
// This mutation will invoke our callback  
// 32 31 ['age'] true  
proxy.age++;
```

[### immediate](#immediate)

By default, all mutations that occur on the same tick are accumulated within a mutation list.
The provided handler function is invoked on the next tick and takes the list of mutations as an argument, i.e., it works lazily.
To force a watcher to invoke its handler immediately after the occurred mutation, provide the `immediate` option.
In this case, the callback function doesn't take a list of mutations but parameters of the single mutation.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const {proxy} = watch(user, {immediate: true}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path);  
});  
  
// This mutation will invoke our callback  
// 32 31 ['age']  
proxy.age++;
```

[### collapse](#collapse)

The option enables or disables collapsing of mutation events.
When it toggles to `true`, all mutation events fire as if they occur on top properties of the watchable object.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: 80,  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, {collapse: true, deep: true}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path, info.obj === info.top);  
  });  
});  
  
// {programming: 81, singing: 10} {programming: 81, singing: 10} ['skills', 'programming'] true  
proxy.skills.programming++;
```

When it toggles to `false,` and the watcher binds to the specified path, the callback takes a list of mutations.
Otherwise, the callback takes only the last mutation.

```
import watch from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: {  
      js: 80,  
      rust: 30  
    },  
  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, 'skills.programming', {collapse: false}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.top, info.path, info.originalPath);  
  });  
});  
  
// 81 80 {programming: {js: 81, rust: 30}, singing: 10} ['skills', 'programming'] ['skills', 'programming', 'js']  
proxy.skills.programming.js++;  
  
const {proxy: collapsedProxy} = watch({a: {b: {c: 1}}}, 'skills.programming', (value, oldValue, info) => {  
  console.log(value, oldValue);  
});  
  
// {programming: {js: 82, rust: 30}, singing: 10} {programming: {js: 82, rust: 30}, singing: 10}  
collapsedProxy.skills.programming.js++;
```

[### pathModifier](#pathmodifier)

A function that takes a path of the mutation event and returns a new path.
The function is used when you want to mask one mutation to another one.

```
import watch from 'core/object/watch';  
  
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

[### eventFilter](#eventfilter)

A filter function for mutation events.
The function allows skipping some mutation events.

```
import watch from 'core/object/watch';  
  
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

[### tiedWith](#tiedwith)

A link to an object that should connect with the watched object, i.e., changing of properties of the tied object, will also emit mutation events.

```
import watch from 'core/object/watch';  
  
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

[### prefixes](#prefixes)

A list of prefixes for paths to watch. This parameter can help to watch accessors.

```
import watch from 'core/object/watch';  
  
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

[### postfixes](#postfixes)

A list of postfixes for paths to watch. This parameter can help to watch accessors.

```
import watch from 'core/object/watch';  
  
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

[### dependencies](#dependencies)

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

[### engine](#engine)

A watch engine to use.
By default, will be used proxy if supported, otherwise accessors.

```
import watch from 'core/object/watch';  
  
import * as proxyEngine from 'core/object/watch/engines/proxy';  
import * as accEngine from 'core/object/watch/engines/accessors';  
  
const user = {  
  name: 'Kobezzza',  
  age: 31  
};  
  
const proxyWatcher = watch(user, {engine: proxyEngine}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});  
  
const accWatcher = watch(user, {engine: accEngine}, (mutations) => {  
  mutations.forEach(([value, oldValue, info]) => {  
    console.log(value, oldValue, info.path);  
  });  
});
```

[## Global API](#global-api)

The module provides a bunch of additional helper functions.

[### mute](#mute)

The function temporarily mutes all mutation events for the specified proxy object.

```
import watch, { mute } from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: 80,  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path);  
});  
  
// 81 80 ['skills', 'programming']  
proxy.skills.programming++;  
mute(proxy);  
  
// This mutation won't invoke our callback  
proxy.skills.programming++;
```

[### unwatchable](#unwatchable)

Wraps the specified object with unwatchable proxy, i.e. any mutations of this proxy can’t be watched.

```
const obj = {  
  a: 1,  
  b: unwatchable({c: 2})  
};  
  
const {proxy} = watch(obj, {immediate: true}, (value, oldValue) => {  
 console.log(value, oldValue);  
});  
  
// This mutation will be ignored by the watcher  
proxy.b.c = 3;  
  
// 1 2  
proxy.a = 2;
```

[### unmute](#unmute)

The function unmutes all mutation events for the specified proxy object.

```
import watch, { mute, unmute } from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: 80,  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path);  
});  
  
// 81 80 ['skills', 'programming']  
proxy.skills.programming++;  
  
mute(proxy);  
  
// This mutation won't invoke our callback  
proxy.skills.programming++;  
  
unmute(proxy);  
  
// 83 82 ['skills', 'programming']  
proxy.skills.programming++;
```

[### set](#set)

The function sets a new watchable value for a proxy object by the specified path.
It is actual when using an engine based on accessors to add new properties to the watchable object.
Or when you want to restore watching for a property after deleting it.

```
import watch, { set } from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: 80,  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path);  
});  
  
// This mutation will invoke our callback  
set(proxy, 'bla.foo', 1);
```

[### unset](#unset)

The function deletes a watchable value from a proxy object by the specified path.
To restore watching for this property, use `set`.

```
import watch, { set, unset } from 'core/object/watch';  
  
const user = {  
  name: 'Kobezzza',  
  skills: {  
    programming: 80,  
    singing: 10  
  }  
};  
  
const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
  console.log(value, oldValue, info.path);  
});  
  
// This mutation will invoke our callback  
unset(proxy, 'skills.programming');  
  
console.log('programming' in proxy.skills === false);  
  
// This mutation won't invoke our callback  
proxy.skills.programming = 80;  
  
// Invoke set to register a property to watch.  
// This mutation will invoke our callback.  
set(proxy, 'skills.programming', 80)  
  
// This mutation will invoke our callback  
proxy.skills.programming++;
```

## Index

### References

* [InternalWatchOptions](src_core_object_watch.html#InternalWatchOptions)
* [MultipleWatchHandler](src_core_object_watch.html#MultipleWatchHandler)
* [PathModifier](src_core_object_watch.html#PathModifier)
* [RawWatchHandler](src_core_object_watch.html#RawWatchHandler)
* [RawWatchHandlerParams](src_core_object_watch.html#RawWatchHandlerParams)
* [WatchDependencies](src_core_object_watch.html#WatchDependencies)
* [WatchEngine](src_core_object_watch.html#WatchEngine)
* [WatchHandler](src_core_object_watch.html#WatchHandler)
* [WatchHandlerParams](src_core_object_watch.html#WatchHandlerParams)
* [WatchHandlerParentParams](src_core_object_watch.html#WatchHandlerParentParams)
* [WatchHandlersSet](src_core_object_watch.html#WatchHandlersSet)
* [WatchOptions](src_core_object_watch.html#WatchOptions)
* [WatchPath](src_core_object_watch.html#WatchPath)
* [Watcher](src_core_object_watch.html#Watcher)
* [blackList](src_core_object_watch.html#blackList)
* [getProxyType](src_core_object_watch.html#getProxyType)
* [isProxy](src_core_object_watch.html#isProxy)
* [muteLabel](src_core_object_watch.html#muteLabel)
* [toOriginalObject](src_core_object_watch.html#toOriginalObject)
* [toProxyObject](src_core_object_watch.html#toProxyObject)
* [toRootObject](src_core_object_watch.html#toRootObject)
* [toTopObject](src_core_object_watch.html#toTopObject)
* [unwrap](src_core_object_watch.html#unwrap)
* [watchHandlers](src_core_object_watch.html#watchHandlers)
* [watchOptions](src_core_object_watch.html#watchOptions)
* [watchPath](src_core_object_watch.html#watchPath)

### Functions

* [default](src_core_object_watch.html#default)
* [mute](src_core_object_watch.html#mute)
* [set](src_core_object_watch.html#set)
* [unmute](src_core_object_watch.html#unmute)
* [unset](src_core_object_watch.html#unset)
* [unwatchable](src_core_object_watch.html#unwatchable)

## References

### InternalWatchOptions

Re-exports [InternalWatchOptions](../interfaces/src_core_object_watch_interface.InternalWatchOptions.html)

### MultipleWatchHandler

Re-exports [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)

### PathModifier

Re-exports [PathModifier](../interfaces/src_core_object_watch_interface.PathModifier.html)

### RawWatchHandler

Re-exports [RawWatchHandler](../interfaces/src_core_object_watch_interface.RawWatchHandler.html)

### RawWatchHandlerParams

Re-exports [RawWatchHandlerParams](../interfaces/src_core_object_watch_interface.RawWatchHandlerParams.html)

### WatchDependencies

Re-exports [WatchDependencies](src_core_object_watch_interface.html#WatchDependencies)

### WatchEngine

Re-exports [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)

### WatchHandler

Re-exports [WatchHandler](../interfaces/src_core_object_watch_interface.WatchHandler.html)

### WatchHandlerParams

Re-exports [WatchHandlerParams](../interfaces/src_core_object_watch_interface.WatchHandlerParams.html)

### WatchHandlerParentParams

Re-exports [WatchHandlerParentParams](../interfaces/src_core_object_watch_interface.WatchHandlerParentParams.html)

### WatchHandlersSet

Re-exports [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)

### WatchOptions

Re-exports [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)

### WatchPath

Re-exports [WatchPath](src_core_object_watch_interface.html#WatchPath)

### Watcher

Re-exports [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)

### blackList

Re-exports [blackList](src_core_object_watch_const.html#blackList)

### getProxyType

Re-exports [getProxyType](src_core_object_watch_engines_helpers.html#getProxyType)

### isProxy

Re-exports [isProxy](src_core_object_watch_engines_helpers.html#isProxy)

### muteLabel

Re-exports [muteLabel](src_core_object_watch_const.html#muteLabel)

### toOriginalObject

Re-exports [toOriginalObject](src_core_object_watch_const.html#toOriginalObject)

### toProxyObject

Re-exports [toProxyObject](src_core_object_watch_const.html#toProxyObject)

### toRootObject

Re-exports [toRootObject](src_core_object_watch_const.html#toRootObject)

### toTopObject

Re-exports [toTopObject](src_core_object_watch_const.html#toTopObject)

### unwrap

Re-exports [unwrap](src_core_object_watch_engines_helpers.html#unwrap)

### watchHandlers

Re-exports [watchHandlers](src_core_object_watch_const.html#watchHandlers)

### watchOptions

Re-exports [watchOptions](src_core_object_watch_const.html#watchOptions)

### watchPath

Re-exports [watchPath](src_core_object_watch_const.html#watchPath)

## Functions

### default

* default<T>(obj: T, handler?: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* default<T>(obj: T, opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html) & { immediate: true }, handler?: [WatchHandler](../interfaces/src_core_object_watch_interface.WatchHandler.html)<unknown, unknown>): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* default<T>(obj: T, opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html), handler?: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* default<T>(obj: T, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), handler?: [WatchHandler](../interfaces/src_core_object_watch_interface.WatchHandler.html)<unknown, unknown>): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* default<T>(obj: T, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html) & { collapse: false }, handler?: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* default<T>(obj: T, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html), handler?: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>): [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>

* + Defined in [src/core/object/watch/index.ts:49](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L49)

  Watches for changes of the specified object

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### Optional handler: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/index.ts:58](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L58)

  Watches for changes of the specified object

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html) & { immediate: true }

    additional options
  + ##### Optional handler: [WatchHandler](../interfaces/src_core_object_watch_interface.WatchHandler.html)<unknown, unknown>

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/index.ts:71](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L71)

  Watches for changes of the specified object

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)

    additional options
  + ##### Optional handler: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/index.ts:80](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L80)

  Watches for changes of the specified object

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)

    path to a property to watch
  + ##### Optional handler: [WatchHandler](../interfaces/src_core_object_watch_interface.WatchHandler.html)<unknown, unknown>

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/index.ts:94](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L94)

  Watches for changes of the specified object

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)

    path to a property to watch
  + ##### opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html) & { collapse: false }

    additional options
  + ##### Optional handler: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>
* + Defined in [src/core/object/watch/index.ts:109](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L109)

  Watches for changes of the specified object

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)

    path to a property to watch
  + ##### opts: [WatchOptions](../interfaces/src_core_object_watch_interface.WatchOptions.html)

    additional options
  + ##### Optional handler: [MultipleWatchHandler](../interfaces/src_core_object_watch_interface.MultipleWatchHandler.html)<unknown, unknown>

  #### Returns [Watcher](../interfaces/src_core_object_watch_interface.Watcher.html)<T>

### mute

* mute(obj: object): boolean

* + Defined in [src/core/object/watch/index.ts:682](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L682)

  The function temporarily mutes all mutation events for the specified proxy object

  example
  :   ```
      const user = {  
        name: 'Kobezzza',  
        skills: {  
          programming: 80,  
          singing: 10  
        }  
      };  
        
      const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
        console.log(value, oldValue, info.path);  
      });  
        
      // 81 80 ['skills', 'programming']  
      proxy.skills.programming++;  
      mute(proxy);  
        
      // This mutation won't invoke our callback  
      proxy.skills.programming++;
      ```

  #### Parameters

  + ##### obj: object

  #### Returns boolean

### set

* set(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), value: unknown, engine?: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)): void
* set(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), value: unknown, handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), engine?: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)): void

* + Defined in [src/core/object/watch/index.ts:793](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L793)

  Sets a new watchable value for a proxy object by the specified path.
  The function is actual when using an engine based on accessors to add new properties to the watchable object.
  Or when you want to restore watching for a property after deleting it.

  example
  :   ```
      const user = {  
        name: 'Kobezzza',  
        skills: {  
          programming: 80,  
          singing: 10  
        }  
      };  
        
      const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
        console.log(value, oldValue, info.path);  
      });  
        
      // This mutation will invoke our callback  
      set(proxy, 'bla.foo', 1);
      ```

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### value: unknown
  + ##### Optional engine: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)

  #### Returns void
* + Defined in [src/core/object/watch/index.ts:811](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L811)

  Sets a new watchable value for a proxy object by the specified path.
  The function is actual when using an engine based on accessors to add new properties to the watchable object.
  Or when you want to restore watching for a property after deleting it.

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### value: unknown
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)
  + ##### Optional engine: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)

  #### Returns void

### unmute

* unmute(obj: object): boolean

* + Defined in [src/core/object/watch/index.ts:753](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L753)

  The function unmutes all mutation events for the specified proxy object

  example
  :   ```
      const user = {  
        name: 'Kobezzza',  
        skills: {  
          programming: 80,  
          singing: 10  
        }  
      };  
        
      const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
        console.log(value, oldValue, info.path);  
      });  
        
      // 81 80 ['skills', 'programming']  
      proxy.skills.programming++;  
      mute(proxy);  
        
      // This mutation won't invoke our callback  
      proxy.skills.programming++;  
      unmute(proxy);  
        
      // 83 82 ['skills', 'programming']  
      proxy.skills.programming++;
      ```

  #### Parameters

  + ##### obj: object

  #### Returns boolean

### unset

* unset(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), engine?: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)): void
* unset(obj: object, path: [ObjectPropertyPath](index.html#ObjectPropertyPath), handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet), engine?: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)): void

* + Defined in [src/core/object/watch/index.ts:877](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L877)

  Deletes a watchable value from a proxy object by the specified path

  example
  :   ```
      const user = {  
        name: 'Kobezzza',  
        skills: {  
          programming: 80,  
          singing: 10  
        }  
      };  
        
      const {proxy} = watch(user, {immediate: true, deep: true}, (value, oldValue, info) => {  
        console.log(value, oldValue, info.path);  
      });  
        
      // This mutation will invoke our callback  
      unset(proxy, 'skills.programming');  
        
      console.log('programming' in proxy.skills === false);  
        
      // This mutation won't invoke our callback  
      proxy.skills.programming = 80;  
        
      // Invoke set to register a property to watch.  
      // This mutation will invoke our callback.  
      set(proxy, 'skills.programming', 80)  
        
      // This mutation will invoke our callback  
      proxy.skills.programming++;
      ```

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### Optional engine: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)

  #### Returns void
* + Defined in [src/core/object/watch/index.ts:892](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L892)

  Deletes a watchable value from a proxy object by the specified path.
  To restore watching for this property, use `set`.

  #### Parameters

  + ##### obj: object
  + ##### path: [ObjectPropertyPath](index.html#ObjectPropertyPath)
  + ##### handlers: [WatchHandlersSet](src_core_object_watch_interface.html#WatchHandlersSet)
  + ##### Optional engine: [WatchEngine](../interfaces/src_core_object_watch_interface.WatchEngine.html)

  #### Returns void

### unwatchable

* unwatchable<T>(obj: T): T

* + Defined in [src/core/object/watch/index.ts:716](https://github.com/V4Fire/Core/blob/master/src/core/object/watch/index.ts#L716)

  Wraps the specified object with unwatchable proxy, i.e. any mutations of this proxy can’t be watched

  example
  :   ```
      const obj = {  
        a: 1,  
        b: unwatchable({c: 2})  
      };  
        
      const {proxy} = watch(obj, {immediate: true}, (value, oldValue) => {  
       console.log(value, oldValue);  
      });  
        
      // This mutation will be ignored by the watcher  
      proxy.b.c = 3;  
        
      // 1 2  
      proxy.a = 2;
      ```

  #### Type parameters

  + #### T: object

  #### Parameters

  + ##### obj: T

  #### Returns T