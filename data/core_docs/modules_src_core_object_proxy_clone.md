# Module src/core/object/proxy-clone
[# core/object/proxy-clone](#coreobjectproxy-clone)

The module returns a function to create clones of the passed objects.
This function creates a Proxy object based on the given to create a clone.
It means that this operation is lazily and very effective but depends on the native support of proxy objects.

```
import proxyClone from 'core/object/proxy-clone';  
  
const original = {  
  user: {  
    name: 'Bob',  
    age: 56,  
    skills: ['singing', 'dancing', 'programming']  
  }  
};  
  
const  
  clone = proxyClone(original);  
  
clone.user.name = 'Jack';  
clone.user.skills.push('boxing');  
  
console.log(clone.user.name !== original.user.name);  
  
// ['singing', 'dancing', 'programming', 'boxing']  
console.log(clone.user.skills);  
  
// ['singing', 'dancing', 'programming']  
console.log(original.user.skills);
```

[## Known limitations](#known-limitations)

Because the process of cloning uses native Proxy objects, there are a few limitations:

1. You can't use `Object.preventExtension` at a clone object because it should be applied to the original object.
2. `Object.isExtensible` always returns a value from the original object.
3. If the original object prevents extensions, then a cloned object will also prevent these extensions.
4. You can't redefine a property descriptor if it contains `configurable: false` attribute in the original object.

[## Common clone](#common-clone)

The module also exports a common implementation to clone objects. If the runtime supports Proxy API, it will be used.

```
import { clone } from 'core/object/proxy-clone';  
  
const original = {  
  user: {  
    name: 'Bob',  
    age: 56,  
    skills: ['singing', 'dancing', 'programming']  
  }  
};  
  
const  
  clone = clone(original);  
  
clone.user.name = 'Jack';  
clone.user.skills.push('boxing');  
  
console.log(clone.user.name !== original.user.name);  
  
// ['singing', 'dancing', 'programming', 'boxing']  
console.log(clone.user.skills);  
  
// ['singing', 'dancing', 'programming']  
console.log(original.user.skills);
```

## Index

### Functions

* [clone](src_core_object_proxy_clone.html#clone)
* [default](src_core_object_proxy_clone.html#default)

## Functions

### clone

* clone<T>(obj: T): T

* + Defined in [src/core/object/proxy-clone/index.ts:27](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/index.ts#L27)

  Returns a clone of the specified object.
  If the runtime supports Proxy, it will be used to clone.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### obj: T

  #### Returns T

### default

* default<T>(obj: T): T

* + Defined in [src/core/object/proxy-clone/index.ts:37](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/index.ts#L37)

  Returns a clone of the specified object.
  The function uses a Proxy object to create a clone. The process of cloning is a lazy operation.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### obj: T

  #### Returns T