# [](#types-reference)Types reference类型参考


When you define your Ontology, you can use a wide variety of types to represent real-world definitions of the data you brought into Foundry. The types used in Foundry are categorized as *Ontology* types or *data* types:当你定义本体时，可以使用多种类型来表示你带入 Foundry 的数据的现实世界定义。Foundry 中使用的类型分为本体类型或数据类型：


- **Ontology types** are used to model a real-world domain into an Ontology.本体类型用于将现实世界领域建模为本体。
- **Data** types are used to represent data values. Data types in Foundry are inspired by similar concepts in [RDF ↗](https://w3c.github.io/rdf-concepts/spec/#section-Datatypes), [OWL ↗](https://www.w3.org/TR/owl-ref/#Datatype) and [XSD ↗](https://www.w3.org/TR/xmlschema-2/#datatype).数据类型用于表示数据值。Foundry 中的数据类型灵感来源于 RDF ↗、OWL ↗ 和 XSD ↗ 中的类似概念。


## [](#ontology-resources)Ontology resources本体资源


The following types are available to build and define your Ontology.以下类型可用于构建和定义你的本体论。


### [](#object-type)Object type对象类型


An **object type** is a schema definition of a real-world entity or event, comprised of individual objects. For example, both `JFK` and `LHR` can be objects of an `Airport` object type.对象类型是现实世界实体或事件的模式定义，由单个对象组成。例如，JFK 和 LHR 都可以是机场对象类型。


[Learn more about object types.](/docs/foundry/object-link-types/object-types-overview/)


#### [](#property)Property财产


A **property** of an object type is a characteristic that informs a real-world entity or event. For example, if `LHR` is an object type of `Airports`, `name` and `country` are properties of `Airports`. For the `LHR` object, the property values would be the following:对象类型的属性是指影响现实世界实体或事件的特征。例如，如果 LHR 是机场的对象类型， 名称和国家则是机场的属性。对于 LHR 对象，属性值如下：


- **name:** LHR名称：LHR
- **country:** United Kingdom乡村音乐： 英国


[Learn more about properties.了解更多关于房产的信息。](/docs/foundry/object-link-types/properties-overview/)


### [](#shared-property)Shared property共享财产


A **shared property** is a property that can be used on multiple object types in your Ontology. Shared properties allow for consistent data modeling across object types and centralized management of property metadata.共享属性是指可以在本体论中用于多个对象类型的属性。共享属性允许跨对象类型实现一致的数据建模和属性元数据的集中管理。


[Learn more about shared properties.了解更多关于共享物业的信息。](/docs/foundry/object-link-types/shared-property-overview/)


### [](#link-type)Link type链接类型


A **link type** is the schema definition of a relationship between two object types. A **link** refers to a single instance of that relationship between two objects.链接类型是两种对象类型之间关系的模式定义。 链接指的是两个对象之间这种关系的单一实例。


[Learn more about link types.](/docs/foundry/object-link-types/link-types-overview/)


### [](#action-type)Action type动作类型


An **action type** is the schema definition of a set of changes or edits to objects, property values, and links that a user can make all at once. Action types also include the side effect behaviors that happen when an Action occurs. Once an action type is configured in the Ontology, end users can make changes to objects by applying Actions.动作类型是对对象、属性值和链接进行一组修改或编辑的模式定义，用户可以一次性完成这些修改。动作类型还包括在动作发生时产生的副作用行为。一旦在本体中配置了动作类型，终端用户可以通过应用动作对对象进行修改。


[Learn more about action types.](/docs/foundry/action-types/overview/)


### [](#object-type-groups)Object type groups对象类型组


Object type groups are a classification primitive that helps users better search and explore their ontology.对象类型组是一种分类原语，帮助用户更好地搜索和探索其本体。


[Learn more about object type groups.了解更多关于对象类型组的信息。](/docs/foundry/object-link-types/type-groups/)


### [](#interfaces)Interfaces接口


An **interface** is an Ontology type that describes the shape of an object type and its capabilities. Interfaces provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape.接口是一种本体类型，用于描述对象类型的形状及其功能。接口提供对象类型多态性，使得对共享相同形状的对象类型进行一致建模和交互。


Learn more about [interfaces](/docs/foundry/interfaces/interface-overview/).了解更多关于接口的信息 。


## [](#difference-between-object-types-and-objects)Difference between object types and objects对象类型与对象的区别


To clarify the difference between object types and objects, examples are provided below. Note that the same distinction applies to link types and links.为了澄清对象类型和对象之间的区别，下面提供了示例。请注意，链接类型和链接也有同样的区别。


### [](#object-type-definitions)Object type definitions对象类型定义


Object type definitions, sometimes just referred to as "object types", refer to type-level information about ontology entities such as object types, link types, and action types. For example, the metadata for an object type may include display name, property names, property data types, and description. Metadata does not refer to the actual data or values of an object type’s properties or primary key; these are considered ontology data.对象类型定义，有时简称为“对象类型”，指的是关于本体实体的类型级信息，如对象类型、链接类型和动作类型。例如，对象类型的元数据可能包括显示名称、属性名称、属性数据类型和描述。元数据不指对象类型属性或主键的实际数据或值;这些被视为本体数据。


### [](#object-instances)Object instances对象实例


Object instances, sometimes just referred to as "objects", are the actual primary key and property values for specific instances of an ontology entity. For example, an `Airplane` object type can have an object instance with a `Plane ID` property having the value `my_plane_id1`, and a `Maximum Occupancy` property having value `240`.对象实例，有时简称为“对象”，是本体实体特定实例的实际主键和属性值。例如，一个 Airplane 对象类型可以有一个具有 Plane ID 属性的对象实例，其值为 my_plane_id1，以及一个 Maximum Occupancy 属性，其值为 240。


## [](#value-types)Value types价值类型


**Value types** are semantic wrappers around a field type comprised of metadata and constraints that can enhance type safety, improve expressiveness, and provide additional context. Value types encapsulate domain-specific data types and enforce data validation in a manner reusable across the platform. Commonly used value types include email addresses, URLs, UUIDs, and enumerations.值类型是围绕由元数据和约束组成的字段类型的语义包装器，能够增强类型安全性、增强表达性并提供额外的上下文。值类型封装了领域特定的数据类型，并以可跨平台重用的方式强制数据验证。常用的值类型包括电子邮件地址、URL、UUID 和枚举。


While field types and base types are defined statically, value types are customized within the context of a given [space](/docs/foundry/security/orgs-and-spaces/). As a result, users cannot create new field types or base types but are able to create **value types** dynamically.字段类型和基类型是静态定义的，而值类型则在给定空间的上下文中进行定制。因此，用户无法创建新的字段类型或基类型，但可以动态创建值类型 。


[Learn more about value types.了解更多关于价值类型的信息。](/docs/foundry/object-link-types/value-types-overview/)

