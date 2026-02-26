# [](#create-a-shared-property)Create a shared property创建共享财产


Create and configure a new shared property from the shared property page in the Ontology Manager application.在 Ontology Manager 应用程序中的共享属性页面创建并配置新的共享属性。


To access the page, follow the steps below:要访问该页面，请按照以下步骤作：


1. Select the **Shared properties** menu option in Ontology Manager.在 Ontology Manager 中选择共享属性菜单选项。


![Shared properties page in Ontology Manager](shared-property-menu-option.png?width=800)


1. Once on the shared property page, select **New shared property** at the top right.进入共享财产页面后，选择右上角的新共享财产 。


![Create shared property button](new-shared-property-button.png?width=800)


1. This will open the shared property creation modal, where you can configure the name, description, type, and other metadata to create the shared property.这会打开共享属性创建模式，你可以配置名称、描述、类型及其他元数据来创建共享属性。


![Create shared property modal](create-shared-property-modal.png?width=500)


A shared property can be configured with a subset of regular property metadata:共享属性可以通过常规属性元数据的子集进行配置：


- **Name:** The name for the shared property.姓名： 这是这块共享财产的名称。
- **Description:** Explanatory text about the shared property. For example, the description of the `start date` shared property may be `The day the employee or contractor began working`.描述： 关于共享财产的说明文字。例如， 起始日期共享财产的描述可能为 The day the employee or contractor began working 。
- **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property. Base types are related to the underlying column type and must match the column type in order to be applied on an object type基础类型： 表示该属性的值类型，并确定用户应用程序中可用的作集合。例如， 起始日期属性将具有基准类型日期 。用户应用程序允许你配置带有该属性的时间线小部件。基类型与底层列类型相关，必须与该类型匹配才能应用于对象类型
- **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID, and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Learn more about [value formatting](/docs/foundry/object-link-types/value-formatting/).价值格式： 根据属性的基础类型，可以应用数字格式、日期和时间格式、用户 ID 和资源 ID 格式，将原始值转换为用户应用程序中更易读取的版本。了解更多关于值格式的知识 。
- **Type classes:** Additional metadata that are interpreted by user applications. Learn more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).类型类别： 用户应用程序解释的额外元数据。了解更多关于类型类的信息 。
- **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type on which the property is defined. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Learn more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).渲染提示： 向用户应用程序提示如何渲染可能与同一基类型大多数属性不同的属性。许多渲染提示可以用来影响定义该属性对象类型的重新索引性能。例如，如果你不期望用户在用户应用中对起始日期属性进行搜索或排序，你可以取消选择可搜索和可排序的渲染提示，并提升员工对象类型的重新索引性能。了解更多关于渲染提示的信息。
- **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have `normal` visibility.能见度： 向用户应用程序提示该物业应多么显著地展示。 显著的房产会促使申请优先向用户展示该房产。 隐藏属性不会出现在用户应用程序中。默认情况下， 起始日期属性将具有正常可见性。


1. To persist the shared property to the Ontology, select **Save** in the upper right of the Ontology Manager.要将共享属性持久化到本体，请在本体管理器右上角选择 “保存 ”。

