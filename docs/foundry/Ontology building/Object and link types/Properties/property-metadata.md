# [](#metadata-reference)Metadata reference元数据引用


A property is represented in the Ontology by the following metadata:本体中属性由以下元数据表示：


- **ID:** A unique identifier of the property, primarily used to reference the property when configuring an application. For example, `start-date` may be the ID of the start date property.ID： 属性的唯一标识符，主要用于在配置应用时引用该属性。例如， 起始日期可能是起始日期属性的 ID。
- **Display name:** The name shown to anyone accessing property values for this property in user applications. For example, the display name for the `start date` property may be `Start date`.显示名称： 用户应用程序中访问该属性值时，会显示该名称。例如， 起始日期属性的显示名称可能是起始日期 。
- **Description:** Explanatory text about the property that anyone can read in user applications. For example, the description of the `start date` property may be `The day the employee began new hire training`.描述： 关于该属性的解释性质文字，任何人都能在用户应用中阅读。例如， 起始日期属性的描述可能是 The day the employee began new hire training 。
- **RID:** An automatically generated unique identifier for every resource in Foundry. A property’s RID will be referenced in error messages across the platform.RID： 为 Foundry 中每个资源自动生成的唯一标识符。物业的 RID 会在平台上的错误信息中被引用。
- **Status:** A signal to users and other Ontology builders about where in the development process the property stands. It can be `active`, `experimental`, or `deprecated`. By default, the `start date` property will have status `experimental`. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).状态： 向用户和其他本体构建者发出信号，说明该物业在开发过程中处于何处。它可以是主动的、 实验性的，或者已经弃用的。默认情况下， 开始日期属性将显示为实验状态。阅读更多关于状态的信息 。
- **API name:** The name used when referring to the property programmatically in code. For example, the API name of the `start date` property may be `startDate`. Read more about [API names](/docs/foundry/functions/api-objects-links/).API 名称： 这是在代码中程序性地指代该属性时所使用的名称。例如， 起始日期属性的 API 名称可能是 startDate。阅读更多关于 API 名称的信息。
- **Keys:** An indication of whether the property is the object type’s title key or primary key.
注释： 表示该属性是对象类型的标题键还是主键。- The **title key** is the property that acts as a display name for objects of this type. For example, setting the `full name` property as the title key of the `Employee` object type will use the values of that property, such as the notional employees “Melissa Chang” and “Diego Rodriguez” as the display names for each respective `Employee` object.标题键是作为此类对象显示名称的属性。例如，将全名属性设置为员工对象类型的标题键，将使用该属性的值，例如名义员工“Melissa Chang”和“Diego Rodriguez”作为各自员工对象的显示名称。
- The **primary key** is the property that acts as a unique identifier for each instance of an object type, meaning that each row in the backing datasources must have a different value for this property. For example, the value of the `employee number` property may be used to identify “Melissa Chang” as a unique employee within the organization.主键是作为每个对象类型实例的唯一标识符的属性，这意味着支持数据源中的每一行必须对该属性有不同的值。例如，员工编号属性的价值可以用来识别“Melissa Chang”作为组织内唯一员工的身份。
  - The **title key** is the property that acts as a display name for objects of this type. For example, setting the `full name` property as the title key of the `Employee` object type will use the values of that property, such as the notional employees “Melissa Chang” and “Diego Rodriguez” as the display names for each respective `Employee` object.标题键是作为此类对象显示名称的属性。例如，将全名属性设置为员工对象类型的标题键，将使用该属性的值，例如名义员工“Melissa Chang”和“Diego Rodriguez”作为各自员工对象的显示名称。
  - The **primary key** is the property that acts as a unique identifier for each instance of an object type, meaning that each row in the backing datasources must have a different value for this property. For example, the value of the `employee number` property may be used to identify “Melissa Chang” as a unique employee within the organization.主键是作为每个对象类型实例的唯一标识符的属性，这意味着支持数据源中的每一行必须对该属性有不同的值。例如，员工编号属性的价值可以用来识别“Melissa Chang”作为组织内唯一员工的身份。
  
  - **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.基础类型： 表示该属性的值类型，并确定用户应用程序中可用的作集合。例如， 起始日期属性将具有基准类型日期 。用户应用程序允许你配置带有该属性的时间线小部件。
- **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Read more about [value formatting](/docs/foundry/object-link-types/value-formatting/).价值格式： 根据属性的基础类型，可以应用数字格式、日期和时间格式、用户 ID 和资源 ID 格式化，将原始值转换为用户应用程序中更易读的版本。阅读更多关于值格式的信息 。
- **Conditional formatting:** Rules set on a property that dictate how that property value will render (e.g coloring, alignment, etc.) in user facing applications. For example, you may set a rule on the `full name` property that colors its values green if the value of the `start date` property was less than 2 weeks ago, in order to indicate a new hire in user applications. Read more about [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/).条件格式： 设定在属性上的规则，决定该属性值在面向用户的应用中如何渲染（例如颜色、对齐等）。例如，你可以在全名属性上设置规则，如果入职日期属性的值少于两周，则其值变为绿色，以便在用户应用中表示新员工。阅读更多关于条件格式的信息 。
- **Type classes:** Additional metadata that are interpreted by user applications. Read more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).类型类别： 用户应用程序解释的额外元数据。阅读更多关于类型类别的信息 。
- **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type the property is defined on. For example, if you don’t expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Read more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).渲染提示： 向用户应用程序提示如何渲染可能与同一基类型大多数属性不同的属性。许多渲染提示可以用来影响该属性所定义对象类型的重索引性能。例如，如果你不期望用户在用户应用中搜索或排序起始日期属性，可以取消选择可搜索和可排序的渲染提示，并提升员工对象类型的重新索引性能。阅读更多关于渲染提示的信息。
- **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have visibility `normal`.能见度： 向用户应用程序提示该物业应多么显著地展示。 显著的房产会促使申请优先向用户展示该房产。 隐藏属性不会出现在用户应用程序中。默认情况下， 开始日期属性的可见性会是正常的。


[Learn more about creating and configuring properties in the Ontology and about validation requirements for property metadata.](/docs/foundry/object-link-types/create-object-type/)


## [](#property-base-types-with-limited-support)Property base types with limited support支持有限的房产基质类型


Some property base types have limited support. These types are indicated with the `Limited support` tag which is visible in the property base type picker.某些房产基础类型支持有限。这些类型通过有限支持标签表示，该标签在属性基类型选择器中可见。


- `byte`:
字节 ：- Properties of this type cannot be used within action types.此类属性不能用于动作类型中。
  - Properties of this type cannot be used within action types.此类属性不能用于动作类型中。
  
  - `decimal`:
小数点 ：- Properties of this type cannot be used within action types as the precision cannot be guaranteed when updating this data type due to the conversion between JSON and Java.由于 JSON 与 Java 之间的转换，该类型的属性无法用于动作类型中，因为更新该数据类型时无法保证精度。
- This type is also not supported in Object Storage V2.该类型在对象存储 V2 中也不支持。
  - Properties of this type cannot be used within action types as the precision cannot be guaranteed when updating this data type due to the conversion between JSON and Java.由于 JSON 与 Java 之间的转换，该类型的属性无法用于动作类型中，因为更新该数据类型时无法保证精度。
  - This type is also not supported in Object Storage V2.该类型在对象存储 V2 中也不支持。
  
  - `float`:
浮动 ：- Properties of this type cannot be used within action types.此类属性不能用于动作类型中。
  - Properties of this type cannot be used within action types.此类属性不能用于动作类型中。
  
  - `short`:
简短 ：- Properties of this type cannot be used within action types.此类属性不能用于动作类型中。
  - Properties of this type cannot be used within action types.此类属性不能用于动作类型中。
  
  - `vector`:
向量 ：- Vectors can only be queried by [KNN](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn).向量只能由 KNN 查询。
- The max vector dimension is 2048.最大向量维数为2048。
  - Vectors can only be queried by [KNN](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn).向量只能由 KNN 查询。
  - The max vector dimension is 2048.最大向量维数为2048。
  
  

For more information on the limitations of property base types in action types, see [the documentation on supported property types](/docs/foundry/action-types/scale-property-limits/#supported-property-types).有关动作类型中属性基类型的限制的更多信息，请参阅支持的属性类型的文档 。

