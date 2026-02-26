# [](#struct-main-fields-beta)Struct main fields [Beta]结构主字段 [Beta]


Beta贝塔Struct main fields are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.结构主字段目前处于开发的测试阶段，可能无法在你的注册时提供。功能在积极开发过程中可能会发生变化。


**Struct main fields** enable you to designate a [struct's](/docs/foundry/object-link-types/structs-overview/) core value and supplementary metadata. For example, an `Address` struct may contain fields capturing `streetName` and `postalCode` as its main values, while other fields like `collectionDate` and `collectorName` represent metadata that describe how the `Address` was obtained.结构主字段允许你指定结构的核心值和补充元数据。例如， 地址结构体可能包含捕获街道名称和邮政编码作为主要值的字段，而其他字段如 collectionDate 和 collectorName 表示描述地址获取过程的元数据。


Many struct properties follow this pattern: one or more fields contain the primary data you care most about displaying in applications, while other fields provide context, tracking information, or audit details.许多结构性属性遵循这一模式：一个或多个字段包含你最关心的应用中显示的主要数据，而其他字段则提供上下文、跟踪信息或审计细节。


You can designate any of the [supported struct field types](/docs/foundry/object-link-types/structs-overview/#struct-configuration) as main fields.你可以将任何支持的结构字段类型指定为主字段。


## [](#when-to-use-struct-main-fields)When to use struct main fields何时使用 struct 主字段


Use struct main fields when:在以下情况下使用结构主字段：


- Your struct contains core value fields in addition to fields that represent supplementary metadata.你的结构体除了包含核心值字段外，还包含代表补充元数据的字段。
- You want cleaner table displays without losing access to metadata.你希望表格显示更干净，同时不丢失元数据访问权限。
- You need to [implement interfaces](/docs/foundry/interfaces/implement-interface/) using only a single field or subset of fields from a struct.你需要仅用结构体中的单个字段或子集字段来实现接口 。


## [](#configure-struct-main-fields)Configure struct main fields配置结构体主字段


1. Navigate to **Ontology Manager**.进入 Ontology Manager。
2. Search for and select your object type by choosing **Object types** under **Resources** in the left panel.在左侧面板的资源下选择 “对象类型 ”，搜索并选择你的对象类型。
3. Select the struct property to configure from your object type's **Properties** tab.从你的对象类型的属性选项卡中选择要配置的 struct 属性。
4. Choose the field to designate from the **Struct fields** section of the **General** tab that appears in the property editor panel on the right.在右侧属性编辑器面板中，从 “通用 ”标签的结构字段部分选择要指定的字段。


![Main fields configuration location](struct-main-fields-sidebar-location.png?width=400)


1. Toggle on **Struct main field** in the **Edit {propertyName} struct field** popup window before you select **Confirm**. You can designate multiple main fields and reorder them for clarity by clicking and dragging a field's panel.在选择确认前，先在编辑 {propertyName} struct 字段弹窗中切换 Struct 主字段 。你可以指定多个主字段，并通过点击和拖动字段面板来重新排序以求清晰。


![Struct main field toggle](struct-main-fields-toggle.png?width=450)


1. **Save** your changes. Configured main fields display a **Struct main field** tag in the **Struct fields** list.保存你的更改。配置的主字段会在结构体字段列表中显示一个结构体主字段标签。


![Struct main field tags](struct-main-fields-tags.png?width=400)


## [](#how-struct-main-fields-appear-in-applications)How struct main fields appear in applications结构主字段在应用中的出现方式


Applications that support struct main fields display only the main fields in compact views, like the [Object Table](/docs/foundry/workshop/widgets-object-table/) and [Object List](/docs/foundry/workshop/widgets-object-list/) widgets in [Workshop](/docs/foundry/workshop/overview/), while providing access to the full struct through an expanded view or upon hover. This enables you to quickly scan the most important data without seeing every struct field, while still being able to inspect the complete struct when needed.支持结构主字段的应用程序在紧凑视图中只显示主字段，如 Workshop 中的对象表和对象列表控件，同时通过展开视图或悬停时访问完整结构体。这使你能够快速扫描最重要的数据，而无需看到每个结构字段，同时在需要时检查整个结构体。


Applications support struct main fields in several ways:应用程序以多种方式支持结构主字段：


- **Main fields only:** Display only main fields in compact views like tables or summary cards.仅限主要领域： 在表格或摘要卡等紧凑视图中只显示主字段。
- **Main fields with hover:** Show main fields by default and reveal metadata fields on hover.主要悬停场： 默认显示主字段，悬停时显示元数据字段。
- **Full struct:** Display all fields in detailed views or forms where complete information is needed.完整结构： 在需要完整信息的地方，将所有字段显示为详细视图或表单。


## [](#use-struct-fields-with-interfaces)Use struct fields with interfaces使用带有接口的结构体字段


You can map any struct field to an interface property. When implementing an interface, you can select a specific field from a struct property to satisfy the interface contract and fulfill the property requirement.你可以将任何结构体字段映射到接口属性。在实现接口时，你可以从结构体属性中选择特定字段以满足接口契约并满足属性要求。


For example, if an interface requires a `String` property called `cityName`, you can fulfill it using a struct property's `city` field. The interface picker displays all available struct fields with their types, allowing you to choose the appropriate field.例如，如果某个接口需要一个叫 cityName 的 String 属性，你可以用结构体属性的 city 字段来实现它。界面选择器会显示所有可用的结构体字段及其类型，方便你选择合适的字段。


![Selecting a struct field to map to an interface property](struct-main-fields-interface-picker.png?width=700)


After mapping a struct field to an interface property, the implementation shows the struct property and the specific field being used.在将结构体字段映射到接口属性后，实现会显示结构体属性和所使用的具体字段。


![Mapped struct field to interface property](struct-main-fields-interface-mapped.png?width=700)


Main fields are indicated with a **Struct main field** tag in the picker, making them easy to identify. However, you can select any field from the struct regardless of whether it is designated as a main field.主字段通过 Struct 主字段标签在选择器中表示，便于识别。不过，你可以从结构体中选择任何字段，无论它是否被指定为主字段。


## [](#combine-main-fields-with-property-reducers)Combine main fields with property reducers将主场与属性还原器结合


Combine struct main fields with [property reducers](/docs/foundry/object-link-types/property-reducers/) to enable additional flexibility in struct array property representation and interface implementation. A single struct array property can implement interfaces requiring `Struct Array`, the main field's array type, `Struct`, or the main field's base type.将结构体主字段与属性缩减器结合，以增强结构数组属性表示和接口实现的灵活性。单个结构数组属性可以实现需要结构数组 、主字段数组类型、Struct 或主字段基类型接口的接口。


See the [property reducers documentation](/docs/foundry/object-link-types/property-reducers/#combine-property-reducers-with-struct-main-fields) for detailed examples and implementation options.请参阅属性减量器文档以获取详细示例和实现方案。


## [](#limitations-and-considerations)Limitations and considerations局限性与考虑


- **Query behavior:** Queries operate on all struct fields, not just main fields. You can search and filter based on any field in the struct.查询行为： 查询作用于所有结构体字段，而不仅仅是主字段。你可以根据结构体中的任何字段搜索和筛选。


## [](#faqs)FAQs常见问题解答


### [](#can-i-change-which-fields-are-main-fields-later)Can I change which fields are main fields later?我可以以后更改哪些字段为主字段吗？


Yes, you can reconfigure main fields in Ontology Manager at any time. This may render some interface implementations invalid, which you will need to update.是的，你可以随时在 Ontology Manager 中重新配置主字段。这可能会导致某些接口实现失效，你需要更新它们。


### [](#do-main-fields-affect-how-foundry-stores-data)Do main fields affect how Foundry stores data?主字段会影响 Foundry 存储数据的方式吗？


No, main fields only affect how Foundry displays data and implements interfaces. The underlying struct contains all fields with full fidelity, so all fields remain queryable and accessible.不，主字段只影响 Foundry 如何显示数据和实现接口。底层结构体包含所有字段以完全保真度，因此所有字段都保持可查询和访问。


### [](#can-i-use-main-fields-with-struct-arrays)Can I use main fields with struct arrays?我可以用主字段搭配结构数组吗？


Yes. Main fields work with *both* single struct properties and struct array properties. When combined with [reducers](/docs/foundry/object-link-types/property-reducers/), you get maximum flexibility in how Foundry represents the property across applications.是的。主字段同时处理单个结构属性和结构数组属性。结合缩减器 ，Foundry 在不同应用中呈现该性质时，可以获得最大灵活性。


### [](#do-i-need-to-configure-main-fields-to-use-struct-fields-with-interfaces)Do I need to configure main fields to use struct fields with interfaces?我需要配置主字段来使用带接口的结构体字段吗？


No. You can map any struct field to an interface property regardless of whether it is designated as a main field. Main fields simply provide a visual indicator in the interface picker and affect how applications display the struct in compact views.不。你可以将任何结构体字段映射到接口属性，无论它是否被指定为主字段。主字段仅在界面选择器中提供可视化指示，影响应用程序在紧凑视图中如何显示结构体。

