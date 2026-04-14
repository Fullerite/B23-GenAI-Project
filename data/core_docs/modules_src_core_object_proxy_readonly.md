# Module src/core/object/proxy-readonly
[# core/object/proxy-readonly](#coreobjectproxy-readonly)

The module returns a function to create read-only views of the passed objects.
This function creates a Proxy object based on the given to create a view.
It means that this operation is lazily and very effective but depends on the native support of proxy objects.

```
import proxyReadonly from 'core/object/proxy-readonly';  
  
const original = {  
  user: {  
    name: 'Bob',  
    age: 56,  
    skills: ['singing', 'dancing', 'programming']  
  }  
};  
  
const  
  readonly = proxyReadonly(original);  
  
try {  
  readonly.user.name = 'Jack';  
  
} catch (err) {  
  console.log(err);  
}  
  
try {  
  readonly.user.skills.push('boxing');  
  
} catch (err) {  
  console.log(err);  
}  
  
console.log(readonly.user.name === original.user.name);  
  
// ['singing', 'dancing', 'programming']  
console.log(readonly.user.skills);  
  
// ['singing', 'dancing', 'programming']  
console.log(original.user.skills);
```

[## Known limitations](#known-limitations)

Because the process of cloning uses native Proxy objects, there are a few limitations:

1. You can't use `Object.preventExtension` at a clone object because it should be applied to the original object.

[## Common readonly](#common-readonly)

The module also exports a common implementation to make objects read-only. If the runtime supports Proxy API, it will be used.

```
import { readonly } from 'core/object/proxy-readonly';  
  
const original = {  
  a: 1  
};  
  
const  
  readonly = proxyReadonly(original);  
  
try {  
  readonly.a++;  
  
} catch (err) {  
  console.log(err);  
}  
  
// 1  
console.log(readonly.a);
```

## Index

### Functions

* [default](src_core_object_proxy_readonly.html#default)
* [readonly](src_core_object_proxy_readonly.html#readonly)

## Functions

### default

* default<T>(obj: T): Readonly<T>

* + Defined in [src/core/object/proxy-readonly/index.ts:35](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-readonly/index.ts#L35)

  Returns a read-only view of the specified object.
  The function uses a Proxy object to create a view.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### obj: T

  #### Returns Readonly<T>

### readonly

* readonly<T>(obj: T): T

* + Defined in [src/core/object/proxy-readonly/index.ts:25](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-readonly/index.ts#L25)

  Returns a read-only view of the specified object.
  If the runtime supports Proxy, it will be used to create a view.

  #### Type parameters

  + #### T

  #### Parameters

  + ##### obj: T

  #### Returns T