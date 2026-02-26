# [](#shared-properties)Shared properties共享财产


A **shared property** is a [property](/docs/foundry/object-link-types/properties-overview/) that can be used on multiple [object types](/docs/foundry/object-link-types/object-types-overview/) in your ontology. Shared properties allow for consistent data modeling across object types and centralized management of property metadata. While property metadata is shared across objects, the underlying object data is not.共享属性是指可以在本体论中用于多个对象类型的属性 。共享属性允许跨对象类型实现一致的数据建模和属性元数据的集中管理。虽然属性元数据在对象间共享，但底层对象数据则不共享。


For example, in Ontology Manager, you may have `Employee` and `Contractor` object types that both have the property `start date`. By creating a `start date` shared property and using it for both object types, you can model your data using a consistent property and update `start date` metadata in one place instead of on each object type.例如，在 Ontology Manager 中，你可能有员工和承包商对象类型，它们都带有属性的开始日期 。通过创建一个起始日期共享属性并用于两种对象类型，你可以用一致的属性建模数据，并在一个地方更新起始日期元数据，而不是在每个对象类型上更新。


Shared properties can be [created directly](/docs/foundry/object-link-types/create-shared-property/), or existing properties on object types can be converted into shared properties. Once added to your ontology, shared properties can be [used](/docs/foundry/object-link-types/use-shared-property/) on object types as part of ontologizing your data and [edited](/docs/foundry/object-link-types/edit-shared-property/) in a manner similar to regular properties.共享属性可以直接创建 ，或者将对象类型上的现有属性转换为共享属性。一旦添加到你的本体论中，共享属性可以作为数据本体论的一部分用于对象类型，并以类似普通属性的方式进行编辑 。


Shared properties on objects are denoted with a globe icon next to their name.对象上的共享属性会在其名称旁用地球图标表示。


![Shared properties page in Ontology Manager](shared-property-menu-option.png?width=800)

