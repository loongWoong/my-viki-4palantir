# [](#metadata-reference)Metadata reference元数据引用


A shared property is represented in the Ontology by the following metadata:共享属性在本体中由以下元数据表示：


- **Name:** The name for the shared property.姓名： 这是这块共享财产的名称。
- **Description:** Explanatory text about the shared property that anyone can read in user applications. For example, the description of the `start date` shared property may be `The day the employee began new hire training`.描述： 关于共享属性的解释性，任何人都可以在用户应用中阅读。例如， 起始日期共享财产的描述可能为 The day the employee began new hire training 。
- **RID:** An automatically generated unique identifier for every resource in Foundry. A property’s RID will be referenced in error messages across the platform.RID： 为 Foundry 中每个资源自动生成的唯一标识符。物业的 RID 会在平台上的错误信息中被引用。
- **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.基础类型： 表示该属性的值类型，并确定用户应用程序中可用的作集合。例如， 起始日期属性将具有基准类型日期 。用户应用程序允许你配置带有该属性的时间线小部件。
- **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID, and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Learn more about [value formatting](/docs/foundry/object-link-types/value-formatting/).价值格式： 根据属性的基础类型，可以应用数字格式、日期和时间格式、用户 ID 和资源 ID 格式，将原始值转换为用户应用程序中更易读取的版本。了解更多关于值格式的知识 。
- **Type classes:** Additional metadata that are interpreted by user applications. Learn more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).类型类别： 用户应用程序解释的额外元数据。了解更多关于类型类的信息 。
- **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type on which the property is defined. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Learn more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).渲染提示： 向用户应用程序提示如何渲染可能与同一基类型大多数属性不同的属性。许多渲染提示可以用来影响定义该属性对象类型的重新索引性能。例如，如果你不期望用户在用户应用中对起始日期属性进行搜索或排序，你可以取消选择可搜索和可排序的渲染提示，并提升员工对象类型的重新索引性能。了解更多关于渲染提示的信息。
- **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have `normal` visibility.能见度： 向用户应用程序提示该物业应多么显著地展示。 显著的房产会促使申请优先向用户展示该房产。 隐藏属性不会出现在用户应用程序中。默认情况下， 起始日期属性将具有正常可见性。
- **Usage:** The obect types on which a shared property is used. For example, the `start date` property can be in use by the `Employee`, `Contractor`, and other object types within the Ontology.使用情况： 共享属性所使用的对象类型。例如， 起始日期属性可以被本体中的员工 、 承包商及其他对象类型使用。

