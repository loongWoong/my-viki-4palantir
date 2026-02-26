# [](#edit-a-struct-property-type)Edit a struct property type编辑结构体属性类型


1. In Ontology Manager, open the **Object types** tab in the left sidebar and select an existing object type.在 Ontology Manager 中，打开左侧边栏的对象类型标签，选择一个现有的对象类型。
2. In the object type details page, open the **Properties** tab in the left sidebar, and select the relevant struct property type from the **Properties** table.在对象类型详情页面，打开左侧侧边栏的属性标签，从属性表中选择相关的结构属性类型。
3. In the **Property editor** panel, scroll to the **Struct fields** section and select the struct field you would like to edit. The number of edits made will appear on the top right of the Ontology Manager interface.在属性编辑器面板中，滚动到结构字段部分，选择你想编辑的结构字段。编辑次数会显示在本体管理器界面的右上角。


![Struct fields in the 'Property editor' panel.](Edit-struct.png?width=500)


1. Make the necessary edits in the **Edit struct field** dialog, and select **Confirm**.在 “编辑结构”字段对话框中进行必要的编辑，然后选择确认 。


![The 'Edit struct field' dialog.](confirm-struct-edit.png?width=500)


Note that changing a struct field's API name will result in a new struct field RID being generated. This will override the existing index, similar to the behavior of changing the property ID of a property type. Any applications that reference the updated struct field will need to be updated as well.注意，更改结构体字段的 API 名称会导致生成一个新的结构体字段 RID。这将覆盖现有索引，类似于更改属性类型的属性 ID。任何引用更新过的结构字段的应用程序也都需要更新。

