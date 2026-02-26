# [](#structs)Structs结构体


A **struct** is an Ontology property [base type](/docs/foundry/object-link-types/base-types/) that allows users to create schema-based properties with multiple fields. Struct properties are created from struct type dataset columns. Struct property fields can have different data sources as long as the property is transformed into a single struct type column before being defined in the Ontology.结构体是一种本体属性基类型 ，允许用户创建包含多个字段的基于模式的属性。结构体属性由结构体类型数据集列创建。只要在定义本体之前，将属性转换为单一结构类型列，结构属性字段可以有不同的数据源。


Many common object properties can be modeled as structs. For example, a `Full Name` property with the fields `First Name` and `Last Name`, or an `Address` property that includes `Street`, `City`, `Postal Code`, and `Country` fields.许多常见对象属性都可以建模为结构体。例如，包含 “名字”和 “ 姓氏”字段的全名属性，或包含街道 、 城市 、 邮政编码和国家字段的地址属性。


## [](#struct-configuration)Struct configuration结构配置


The following is a list of struct property constraints and allowed configurations:以下是结构体属性约束和允许配置的列表：


- Structs have a depth of one and cannot be nested.结构体深度为1，且无法嵌套。
- Structs must have at least 1 field, and can contain up to 10 fields.结构体必须至少有1个字段，最多可包含10个字段。
- Only the following field types are currently supported:
目前仅支持以下字段类型：- `BOOLEAN`
- `BYTE`
- `DATE`
- `DECIMAL`
- `DOUBLE`
- `FLOAT`
- `GEOPOINT`
- `INTEGER`
- `LONG`
- `SHORT`
- `STRING`
- `TIMESTAMP`
  - `BOOLEAN`
  - `BYTE`
  - `DATE`
  - `DECIMAL`
  - `DOUBLE`
  - `FLOAT`
  - `GEOPOINT`
  - `INTEGER`
  - `LONG`
  - `SHORT`
  - `STRING`
  - `TIMESTAMP`
  
  

## [](#query-semantics)Query semantics查询语义


Structs are indexed similarly to [ElasticSearch object field types ↗](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/object), which means that arrays can have unintuitive behavior. For example, if you have an array of `Full Name` properties, an object containing `[{"firstName": "Harvey", "lastName": "Dent"}, {"firstName": "Two", "lastName": "Face"}]` would match a query for `"firstName": "Harvey" AND "lastName": "Face"`. The two conditions are treated independently, rather than requiring to match on the same struct within the array.结构体的索引类似于 ElasticSearch 对象字段类型↗，这意味着数组可能表现得不直观。例如，如果你有一个全名属性数组，包含 [{"firstName": "Harvey", "lastName": "Dent"}, {"firstName": "Two", "lastName": "Face"}] 的对象会匹配查询 。 "firstName": "Harvey" AND "lastName": "Face" 这两个条件是独立处理的，而不是要求在数组内的同一结构上匹配。


## [](#current-levels-of-support)Current levels of support当前支持水平


As support for struct property types expands, availability will vary across the Palantir platform.随着对结构属性类型的支持扩展，Palantir 平台上的可用性也会有所不同。


Structs are currently supported in the following applications and services:目前，以下应用程序和服务支持结构体：


- **[Ontology Manager](/docs/foundry/ontology-manager/overview/):** Define and edit structs.本体管理器 ： 定义并编辑结构体。
- **[Actions](/docs/foundry/action-types/overview/):** Use actions to [create and modify struct property values](/docs/foundry/action-types/actions-on-structs/).行动： 使用动作来创建和修改结构体属性值 。
- **[Pipeline Builder](/docs/foundry/pipeline-builder/overview/):** Define and edit structs.管道建设者： 定义并编辑结构体。
- **[Workshop](/docs/foundry/workshop/overview/):** Display and use struct properties as variables.工作坊 ： 将 struct 属性作为变量显示并使用。
- **[Marketplace](/docs/foundry/marketplace/overview/):** Package and install struct properties.市场 ： 打包并安装 struct 属性。
- **[Object Explorer](/docs/foundry/object-explorer/search-objects/):** Search for objects by their struct property values (struct field search is under development).对象浏览器 ： 通过结构体属性值搜索对象（结构体字段搜索正在开发中）。
- **[Ontology SDK](/docs/foundry/ontology-sdk/overview/):** Load struct properties and search for objects by their struct property values in Ontology SDK applications. Not all Ontology SDKs support struct properties. Refer to the OSDK [unsupported property types](/docs/foundry/ontology-sdk/unsupported-types/#object-types-unsupported-property-types) for more information.本体 SDK： 在 Ontology SDK 应用中，加载结构属性并根据其结构属性值搜索对象。并非所有 Ontology SDK 都支持结构属性。更多信息请参阅 OSDK 不支持属性类型 。
- **[Functions](/docs/foundry/functions/overview/):** Struct parameters and struct property edits are supported in TypeScript v2 and Python functions.职能：TypeScript v2 和 Python 函数支持结构参数和结构属性编辑。


Structs will not be supported in Object Storage V1 (Phonograph) and can currently only be created from datasets and Restricted Views.Object Storage V1（留声机）中不支持结构体，目前只能从数据集和受限视图创建。

