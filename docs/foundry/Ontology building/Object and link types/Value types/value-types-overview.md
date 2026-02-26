# [](#value-types)Value types价值类型


**Value types** are semantic wrappers around a [field type](/docs/foundry/data-integration/datasets/#supported-field-types) that include metadata and constraints that can enhance type safety, improve expressiveness, and provide additional context. Value types encapsulate domain-specific data types and enforce data validation in a manner reusable across the platform. Unlike object types, properties, link types, or other types that define and build the Ontology, value types are associated with a [space](/docs/foundry/security/orgs-and-spaces/#spaces) in the platform. A space can hold a single ontology. Value types can only be used within the space in which they were defined. Value types are not available for the Default ontology.值类型是包围字段类型的语义包装器，包含元数据和约束，这些可以提升类型安全性、增强表达性并提供额外的上下文。值类型封装了领域特定的数据类型，并以可跨平台重用的方式强制数据验证。与定义和构建本体的对象类型、属性、链接类型或其他类型不同，值类型与平台中的某个空间相关联。一个空间可以容纳单一本体。值类型只能在其定义的空间内使用。默认本体不提供值类型。


Dataset [field types](/docs/foundry/data-integration/datasets/#supported-field-types) and property [base types](/docs/foundry/object-link-types/base-types/) reflect the primitive types found in programming languages. These types are domain-agnostic and provide no domain context. By contrast, value types capture the context and semantic meaning of data and centralize data validation. Users define and consume meaning directly from the value type, rather than relying on surrounding information such as column names or property descriptions. Value types also enforce their validation constraints on data in Builder pipelines and the ontology, so data integrators and ontology managers can ensure proper semantic typing in their data flows and models.数据集字段类型和属性基类型反映了编程语言中存在的原始类型。这些类型与域名无关，不提供领域上下文。相比之下，价值类型捕捉数据的语义和上下文，并集中数据验证。用户可以直接从价值类型中定义和获取意义，而不是依赖列名或属性描述等周围信息。值类型还会在构建器流水线和本体论中强制其对数据的验证约束，因此数据集成器和本体管理者可以确保其数据流和模型中的语义类型正确。


For example, a user can define an “email” value type that has a regular expression constraint to ensure any property that uses the value type represents a valid email address. This value type can then be reused across multiple object types and pipelines without having to duplicate the validation logic for every such property. Additionally, each property that uses this value type is explicitly understood to contain an email address.例如，用户可以定义一个带有正则表达式约束的“邮件”值类型，以确保任何使用该值类型的属性代表有效的电子邮件地址。该值类型可以跨多个对象类型和管道重复使用，而无需为每个此类属性重复验证逻辑。此外，每个使用该值类型的属性都明确理解为包含一个电子邮件地址。


Since value types are intended for reuse across multiple pipelines and object types, they are [permissioned](/docs/foundry/object-link-types/value-types-permissions/) to ensure users can apply them where needed and [versioned](/docs/foundry/object-link-types/value-types-versions/) to handle both breaking and non-breaking edits.由于值类型旨在跨多个管道和对象类型重复使用，它们被授权以确保用户能在需要时应用，并且对破坏性和非破坏性编辑都有版本控制 。


Get started by learning how to [create a new value type](/docs/foundry/object-link-types/create-value-type/) or [use an existing value type](/docs/foundry/object-link-types/use-value-type/) on a property.从学习如何创建新的价值类型或在物业上使用现有的价值类型开始。

