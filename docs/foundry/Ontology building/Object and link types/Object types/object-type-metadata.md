# [](#metadata-reference)Metadata reference元数据引用


An object type is represented in the Ontology by the following metadata:对象类型在本体中由以下元数据表示：


- **ID:** A unique identifier of the object type, primarily used to reference objects of this type when configuring an application. For example, `employee` may be the ID of the `Employee` object type.ID： 对象类型的唯一标识符，主要用于在配置应用时引用此类对象。例如，employee 可能是 Employee 对象类型的 ID。
- **RID:** An automatically generated unique identifier for every resource in Foundry. An object type’s RID will be referenced in error messages across the platform.RID： 为 Foundry 中每个资源自动生成的唯一标识符。对象类型的 RID 会在平台的错误消息中被引用。
- **Icon:** A picture and color used as a visual identifier of the object type that will appear in user applications when a user views an object of this type. For example, the person icon may be used to depict the `Employee` object type.图标： 一种图像和颜色，用作对象类型的视觉标识符，用户查看该类型对象时会在用户应用程序中显示。例如，人物图标可以用来表示员工对象类型。
- **Display name:** The name shown to anyone accessing an object of this type in user applications. For example, the display name for the `Employee` object type may be `Employee`.显示名称： 用户应用中访问此类对象时会显示的名称。例如， 员工对象类型的显示名称可能是 Employee。
- **Plural display name:** The name shown to anyone accessing multiple objects of this type in user applications. For example, the plural display name for the `Employee` object type may be `Employees`.复数显示名称： 该名称显示给访问用户应用程序中多个此类对象的人。例如， 员工对象类型的复数显示名称可能是 Employees。
- **Description:** Explanatory text about the object type that anyone can read in user applications. For example, the description of the `Employee` object type may be `All full-time and part-time employees of Organization X`.描述： 关于对象类型的解释性文字，任何人都能在用户应用中阅读。例如， 员工对象类型的描述可能是 All full-time and part-time employees of Organization X 。
- **Groups:** A group is a label that helps you categorize your object types. For example, the `Employee` object type may belong to groups `HR` and `Employee 360`.团体： 组是一个标签，帮助你分类你的对象类型。例如，Employee 对象类型可能属于 HR 和 Employee 360 组。
- **API name:** The name used when referring to the object type programmatically in code. For example, the API name of the `Employee` object type may be `Employee`. Read more about [API names](/docs/foundry/functions/api-objects-links/).API 名称： 在代码中用来编程指代对象类型的名称。例如，Employee 对象类型的 API 名称可能是 Employee。阅读更多关于 API 名称的信息。
- **Visibility:** An indication to user applications for how prominently to display the object type. A `prominent` object type will lead applications to show this object type first to users. A `hidden` object type will not appear in user applications. By default, the `Employee` object type will have visibility `normal`.能见度： 这是向用户应用程序指示对象类型应如何显著显示的。 显著的对象类型会促使应用程序首先向用户展示该对象类型。 隐藏对象类型不会出现在用户应用程序中。默认情况下， 员工对象类型会保持正常可见性。
- **Status:** A signal to users and other Ontology builders about where in the development process the object type stands. It can be `active`, `experimental`, or `deprecated`. By default, the `Employee` object type will have status `experimental`. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).状态： 这是向用户和其他本体构建者发出的信号，说明对象类型在开发过程中处于何种位置。它可以是主动的、 实验性的，或者已经弃用的。默认情况下， 员工对象类型将处于实验状态状态。阅读更多关于状态的信息 。
- **Index status:** The status of the last reindex of the object type and its backing datasources. It can be `success`, `failed`, or `not started`. Read more about [index statuses](/docs/foundry/object-databases/object-storage-v1/).指数状态： 对象类型及其支持数据源的最后一次重新索引状态。这可能是成功 、 失败或未开始 。阅读更多关于索引状态的信息 。
- **Writeback:** An indication of whether the object type has a writeback dataset generated, and whether allowing end users to make edits to objects of this type is `enabled` or `disabled`. Read more about [writeback datasets](/docs/foundry/object-link-types/allow-editing/).写回： 该对象类型是否生成了写回数据集，以及是否允许终端用户对该类型对象进行编辑的指示。 阅读更多关于写回数据集的信息。


[Learn more about creating and configuring an object type in the Ontology and about validation requirements for object type metadata.了解更多关于在本体中创建和配置对象类型，以及对象类型元数据的验证要求。](/docs/foundry/object-link-types/create-object-type/)


[Learn more about Properties (characteristics of an object type).](/docs/foundry/object-link-types/properties-overview/)

