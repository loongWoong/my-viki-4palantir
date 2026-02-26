# [](#edit-only-properties)Edit-only properties仅编辑属性


Edit-only properties allow you to define Ontology properties that are not directly mapped to a column in the backing dataset of the object type.
This is particularly useful for situations where you may want to store additional information alongside your object types without modifying the underlying dataset.仅编辑属性允许你定义本体属性，这些属性不会直接映射到对象类型后备数据集中的某一列。这对于你可能想在对象类型之外存储额外信息而不修改底层数据集的情况尤其有用。


## [](#summary-of-edit-only-properties)Summary of edit-only properties仅编辑属性总结


When working with edit-only properties, keep the following in mind:在使用仅编辑属性时，请牢记以下几点：


- **No mapping to a column in the backing dataset:** Edit-only properties are not required to be mapped to a specific column in the backing dataset. This allows you to easily create new properties before the backing column exists, or create properties that will only be edited through the ontology.没有映射到支持数据集中的某一列： 仅编辑属性不必映射到后备数据集中的特定列。这让你可以轻松地在支持列存在之前创建新属性，或者创建只能通过本体编辑的属性。
- **Permissioned to one of the datasets backing the object type:** To ensure data consistency and security, edit-only properties must be permissioned to one of the datasets backing the object type.授权到支持该对象类型的数据集之一： 为了确保数据一致性和安全，编辑仅限属性必须授权给支持该对象类型的数据集之一。
- **Available only in Object Storage V2:** Edit-only properties are a feature that is exclusively available for object types leveraging Object Storage V2.仅在对象存储 V2 中提供： 仅编辑属性是利用对象存储 V2 的对象类型独有的功能。


### [](#creating-edit-only-properties)Creating edit-only properties创建仅编辑属性


1. Navigate to the **Ontology Manager**.导航到本体管理器 。
2. Choose the object type to which you want to add an edit-only property.选择你想添加仅编辑属性的对象类型。
3. Select **Create Property** and fill in the required details, including the property name, type, and description.选择创建物业 ，填写所需信息，包括物业名称、类型和描述。
4. Under the **Data** section, toggle on the **Edit-only property** toggle and choose a dataset to permission to (if you have more than one dataset backing the object type).在数据部分，切换“ 仅编辑属性 ”开关，选择一个数据集获得权限（如果你有多个支持该对象类型的数据集）。
5. **Save** your changes to create the edit-only property.保存你的更改以创建仅编辑属性。


![Edit-only property](edit_only_property.png?width=300)


### [](#mapping-edit-only-properties-to-dataset-columns)Mapping edit-only properties to dataset columns将仅编辑属性映射到数据集列


If you later decide to add a column to your backing dataset that corresponds to a property that is currently edit-only, you can easily map that property to the new column.如果你后来决定向备份数据集添加一列对应当前仅编辑属性的属性，你可以轻松地将该属性映射到新列。


1. Navigate to the **Ontology Manager**.导航到本体管理器 。
2. Choose the object type with the edit-only property you want to map.选择带有你想映射的仅编辑属性的对象类型。
3. Select the edit-only property to open its details.选择仅编辑属性以打开其详细信息。
4. Under the **Data** section, untoggle the edit-only property and choose a column from one of the backing datasets.在数据部分，取消切换仅编辑属性，选择一个支持数据集中的一列。
5. **Save** your changes.保存你的更改。

