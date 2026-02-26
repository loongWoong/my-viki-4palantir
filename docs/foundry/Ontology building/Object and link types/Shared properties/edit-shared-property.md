# [](#edit-shared-properties)Edit shared properties编辑共享属性


### [](#edit-shared-property-metadata)Edit shared property metadata编辑共享属性元数据


You can edit metadata for a shared property by first selecting the shared property to edit from the **Shared property** page of the Ontology Manager.你可以先从 Ontology Manager 的共享属性页面中选择要编辑的共享属性来编辑共享属性的元数据。


![Edit shared property metadata](edit-shared-property.png?width=500)


The available options for editing shared property metadata are clustered into four different tabs: **General**, **Display**, **Interaction**, and **Details**. These tabs contain the following configurations:编辑共享属性元数据的选项被集中在四个不同的标签页中： 通用 、 显示 、 交互和细节 。这些标签包含以下配置：


- **Name:** The name for the shared property.姓名： 这是这块共享财产的名称。
- **Description:** Explanatory text about the shared property. For example, the description of the `start date` shared property may be `The day the employee or contractor began working`.描述： 关于共享财产的说明文字。例如， 起始日期共享财产的描述可能为 The day the employee or contractor began working 。
- **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.基础类型： 表示该属性的值类型，并确定用户应用程序中可用的作集合。例如， 起始日期属性将具有基准类型日期 。用户应用程序允许你配置带有该属性的时间线小部件。
- **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID, and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Learn more about [value formatting](/docs/foundry/object-link-types/value-formatting/).价值格式： 根据属性的基础类型，可以应用数字格式、日期和时间格式、用户 ID 和资源 ID 格式，将原始值转换为用户应用程序中更易读取的版本。了解更多关于值格式的知识 。
- **Type classes:** Additional metadata that are interpreted by user applications. Learn more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).类型类别： 用户应用程序解释的额外元数据。了解更多关于类型类的信息 。
- **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type on which the property is defined. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Learn more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).渲染提示： 向用户应用程序提示如何渲染可能与同一基类型大多数属性不同的属性。许多渲染提示可以用来影响定义该属性对象类型的重新索引性能。例如，如果你不期望用户在用户应用中对起始日期属性进行搜索或排序，你可以取消选择可搜索和可排序的渲染提示，并提升员工对象类型的重新索引性能。了解更多关于渲染提示的信息。
- **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have `normal` visibility.能见度： 向用户应用程序提示该物业应多么显著地展示。 显著的房产会促使申请优先向用户展示该房产。 隐藏属性不会出现在用户应用程序中。默认情况下， 起始日期属性将具有正常可见性。


Additionally, you can view the object types that use this shared property on the **Usage** tab and update the permissions on the shared property on the **Permissions** tab.此外，你可以在使用标签页查看使用该共享属性的对象类型，并在权限选项卡中更新共享属性的权限。


### [](#delete-a-shared-property)Delete a shared property删除共享属性


To delete a shared property, complete the following steps:要删除共享属性，请完成以下步骤：


1. Navigate to the **Shared property** page of the Ontology Manager.导航到本体管理器的共享属性页面。
2. Select one or more shared properties for deletion, then select **Delete property**.选择一个或多个共享属性进行删除，然后选择删除属性 。


![Delete shared property](delete-shared-property-button.png?width=500)


1. Confirm the delete action in the modal.在模态中确认删除作。


![Confirm shared property deletion](delete-shared-property-modal.png?width=500)


1. Select **Save** in the upper right.选择右上角的保存 。


When a shared property is deleted, all object types using this shared property will revert to regular properties.当共享属性被删除时，使用该共享属性的所有对象类型都会恢复为常规属性。

