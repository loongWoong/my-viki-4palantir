# [](#struct-properties-and-shared-property-types)Struct properties and shared property types结构属性与共享属性类型


Struct properties can be used by local and shared property types. When converting, or promoting a local property type to a shared property type, struct fields need to be re-mapped. Local struct property types backed by shared property types will inherit shared property type fields except for the struct field resource identifiers (RIDs). Struct field metadata (display name, description, aliases) will then be inherited from the shared property type, but struct fields with keep their original RIDs.结构属性可以用于本地和共享属性类型。在转换或将本地属性类型提升为共享属性类型时，结构体字段需要重新映射。由共享属性类型支持的本地结构体属性类型将继承共享属性类型字段，唯独结构体字段资源标识符（RID）除外。结构体字段元数据（显示名称、描述、别名）将继承共享属性类型，但结构字段保留原始的 RID。


## [](#create-a-struct-type-shared-property)Create a struct type shared property创建一个结构类型共享属性


1. In Ontology Manager, you can create a struct type shared property in two ways:在 Ontology Manager 中，你可以通过两种方式创建结构型共享属性：


- From the top right of the homepage, select **New > Shared property**
![Shared property option from the New dropdown menu.](new-dropdown-menu-shared-property.png?width=300)

在主页右上角，选择新的 > 共享财产
- Select **Shared properties > + New shared property**
![+ New shared property option in the Shared properties tab.](new-shared-property-button.png?width=500)

选择共享属性 > + 新共享属性
  - From the top right of the homepage, select **New > Shared property**
  ![Shared property option from the New dropdown menu.](new-dropdown-menu-shared-property.png?width=300)
  
  在主页右上角，选择新的 > 共享财产
  - Select **Shared properties > + New shared property**
  ![+ New shared property option in the Shared properties tab.](new-shared-property-button.png?width=500)
  
  选择共享属性 > + 新共享属性
  
  2. In the main panel, select the **New shared property** button. This will open a helper where you can configure metadata of the shared property including the name, description, aliases, and API name. Then select  to proceed.在主面板中，选择 “新的共享属性 ”按钮。这会打开一个辅助工具，你可以配置共享属性的元数据，包括名称、描述、别名和 API 名称。然后选择 “下一步 ”继续。


 ![The 'Create shared property' dialog.](create-shared-property-modal.png?width=500)
3. Configure the base type, value type, visibility, and whether to require values for the property.配置基础类型、值类型、可见性，以及是否需要属性的值。


 ![Create shared property window on the configuration step.](create-shared-property-configuration.png?width=500)
4. Select a project to save this shared property to.选择一个项目来保存这个共享属性。


 ![Select save location for the shared property.](create-shared-property-save-location.png?width=500)
5. Back in Ontology Manager, select **Save** in the upper right corner to [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/).回到本体管理器，选择右上角的 “保存 ”以更改你的本体。


## [](#attach-a-struct-type-shared-property)Attach a struct type shared property附加一个结构体类型的共享属性


1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.在 Ontology Manager 中，打开属性标签，从属性表中选择目标属性。
2. In the **Property editor** to the right, scroll down to **Shared property** and select a shared property under **Assign**. This will share property metadata among both properties.在右侧的属性编辑器中，向下滚动到共享属性 ，在分配下选择共享属性。这将在两个物业之间共享属性元数据。


![The shared property dropdown in the Assign section.](spt-attachment.png?width=500)


**Note:** To add new struct fields after assigning a shared property type to a local struct property type, you must add the new struct fields to the shared property type and map them to datasource columns for all local struct property types that are backed by the shared property.注： 在将共享属性类型分配给本地结构体属性类型后添加新的结构体字段，必须将新的结构体字段添加到共享属性类型，并将其映射到所有由共享属性支持的本地结构体属性类型的数据源列。


## [](#convert-a-struct-property-type-into-a-shared-property)Convert a struct property type into a shared property将一个结构性属性类型转换为共享属性


The following instructions detail how to convert a struct property into a struct property backed by a shared property type.以下说明详细说明了如何将结构属性转换为由共享属性类型支持的结构属性。


1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.在 Ontology Manager 中，打开属性标签，从属性表中选择目标属性。
2. In the **Property editor** to the right, scroll down and select **Convert to a shared property**, which backs the struct property by a shared property type.在右侧的属性编辑器中，向下滚动，选择 “转换为共享属性 ”，该属性以共享属性类型支持结构属性。


![The 'Convert to a shared property' button in the Property editor.](spt-convert.png?width=500)

