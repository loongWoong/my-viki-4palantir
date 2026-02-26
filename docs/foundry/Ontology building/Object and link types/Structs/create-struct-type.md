# [](#create-a-struct-property-type)Create a struct property type创建一个结构体属性类型


Create and configure a new struct property from the **Object types** page in Ontology Manager. For more information about struct properties, see the [overview](/docs/foundry/object-link-types/structs-overview/).从 Ontology Manager 的对象类型页面创建并配置一个新的 struct 属性。有关结构性质的更多信息，请参见概述 。


1. In Ontology Manager, open the **Object types** tab in the left sidebar and select an existing object type.在 Ontology Manager 中，打开左侧边栏的对象类型标签，选择一个现有的对象类型。
2. In the object type details page, open the **Properties** tab in the left sidebar, and select the **Create property** button on the top right of the **Properties** table.在对象类型详情页面，打开左侧边栏的属性标签，选择属性表右上角的创建属性按钮。


![The object type Properties table and 'Property editor' panel.](create-struct-from-ontology-manager.png?width=500)


1. In the **Property editor** panel, add a name and description, and select **Struct** from the **Base type** dropdown menu.在属性编辑器面板中，添加名称和描述，然后从基础类型下拉菜单中选择结构 。


![The Base type dropdown with 'Struct' selected.](name-struct-from-ontology-manager.png?width=500)


1. Scroll down to the **Data** section and select a **Backing column** from the dropdown.向下滚动到数据部分，从下拉菜单中选择一个支持栏 。


![Choose a backing column in the Data section of the Property editor.](backing-column-struct-ontology-manager.png?width=500)


1. In the **Struct fields** section, select **Add field**, then **New field**.在结构体字段部分，选择添加字段 ，然后选择新字段 。


![Sample struct fields in a struct property type.](struct-field-ontology-manager.png?width=500)


1. Name the new struct field and optionally add a description.给新的结构体字段命名，并可选地添加描述。
2. Lastly, map a column from a datasource to the new struct field.最后，将数据源中的一列映射到新的结构体字段。

