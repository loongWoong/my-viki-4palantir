# [](#use-shared-properties-on-object-types)Use shared properties on object types在对象类型上使用共享属性


To update a property on an object type to a shared property, complete the following steps:要将对象类型的属性更新为共享属性，请完成以下步骤：


1. Navigate to the object type in the Ontology Manager.在 Ontology Manager 中导航到对象类型。
2. Select the property on the panel that you want to update, then scroll down to the **Shared Property** section of the configuration.在面板上选择你想更新的属性，然后向下滚动到配置中的共享属性部分。


![Using a shared property](convert-shared-property.png?width=500)


1. Use the dropdown menu to select an existing shared property to use, or convert the property to a new shared property with the [shared property creation](/docs/foundry/object-link-types/create-shared-property/) modal.使用下拉菜单选择一个现有的共享财产来使用，或者用共享财产创建模式将该财产转换为新的共享财产。


The property will then display as a shared property. To persist the use of the shared property to the Ontology, select **Save** in the upper right.该财产随后将显示为共享财产。要将共享属性的使用权保留到本体中，请在右上角选择 “保存 ”。


- When using a shared property on an object, the property ID and API name of the object-specific property will remain unchanged so as to not break existing downstream workflows that leverage them.当对对象使用共享属性时，该对象特定属性的属性 ID 和 API 名称保持不变，以免破坏利用这些属性的现有下游工作流程。
- While associated with a shared property, direct edits to property metadata that is inherited from the shared property will be disabled. You can still add, delete, or edit type classes. When the property is loaded, the resulting set of type classes will be a union of those from the property and its associated shared property.虽然与共享属性关联，但对继承自共享属性的属性元数据的直接编辑将被禁用。你仍然可以添加、删除或编辑类类。当该属性被加载时，生成的类型类集合将是该属性及其关联共享属性的类的合并。
- If the shared property you use has different [render hint](/docs/foundry/object-link-types/metadata-render-hints/) configuration values than the selected property, using the shared property will override the configuration values of the selected property. Make sure your shared property is configured with the proper render hints for your use case.如果你使用的共享属性的渲染提示配置值与所选属性不同，使用共享属性会覆盖所选属性的配置值。确保你的共享属性配置了适合你用例的渲染提示。


### [](#detach-a-shared-property-from-an-object)Detach a shared property from an object将共享属性从对象中分离出来


To detach a property from a shared property, use the same property panel on an object type in the Ontology Manager and select **Detach**.要将属性从共享属性中分离，请在本体管理器中使用同一属性面板，选择分离 。


![Detach a shared property](detach-shared-property.png?width=500)


Doing so will remove the association between the property and the shared property.这样做会消除房产与共享财产之间的关联。

