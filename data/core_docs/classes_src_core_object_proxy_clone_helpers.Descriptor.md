# Class Descriptor
Class to create a custom property descriptor

### Hierarchy

* Descriptor

## Index

### Constructors

* [constructor](src_core_object_proxy_clone_helpers.Descriptor.html#constructor)

### Properties

* [descriptor](src_core_object_proxy_clone_helpers.Descriptor.html#descriptor)

### Methods

* [getValue](src_core_object_proxy_clone_helpers.Descriptor.html#getValue)
* [setValue](src_core_object_proxy_clone_helpers.Descriptor.html#setValue)

## Constructors

### constructor

* new Descriptor(value: PropertyDescriptor): [Descriptor](src_core_object_proxy_clone_helpers.Descriptor.html)

* + Defined in [src/core/object/proxy-clone/helpers.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/helpers.ts#L21)

  #### Parameters

  + ##### value: PropertyDescriptor

  #### Returns [Descriptor](src_core_object_proxy_clone_helpers.Descriptor.html)

## Properties

### descriptor

descriptor: PropertyDescriptor

* Defined in [src/core/object/proxy-clone/helpers.ts:19](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/helpers.ts#L19)

Original property descriptor

## Methods

### getValue

* getValue<T>(receiver: object): T

* + Defined in [src/core/object/proxy-clone/helpers.ts:29](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/helpers.ts#L29)

  Returns a value from the descriptor

  #### Type parameters

  + #### T = unknown

  #### Parameters

  + ##### receiver: object

    receiver for a get method

  #### Returns T

### setValue

* setValue(value: unknown, receiver: object): boolean

* + Defined in [src/core/object/proxy-clone/helpers.ts:47](https://github.com/V4Fire/Core/blob/master/src/core/object/proxy-clone/helpers.ts#L47)

  Sets a new value to the descriptor

  #### Parameters

  + ##### value: unknown
  + ##### receiver: object

    receiver for a set method

  #### Returns boolean