# [](#property-reducers-beta)Property reducers [Beta]财产缩减器 [Beta]


Beta贝塔Property reducers are in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development.房产减价器目前处于开发的测试阶段，可能无法在您的注册中提供。功能在积极开发过程中可能会发生变化。


A **property reducer** enables you to transform an [array property](/docs/foundry/object-link-types/properties-overview/#supported-property-types) into a single value in the array for display and interface implementation purposes. Reduction does *not* change the underlying property type or property data stored; instead, it provides access to the reduced value in the array when reading the property value.属性简化器可以将数组属性转换为数组中的单个值，用于显示和接口实现。减少不会改变基础属性类型或存储的属性数据;相反，它在读取属性值时，提供数组中的约简值访问。


For example, applying a reducer to an array with multiple inspection dates allows you to display only the most recent date when viewing the property in a table or application but ensures the full array remains accessible for queries and other operations. Applications that support reducers, such as [Workshop](/docs/foundry/workshop/overview/), also enable you to view the complete array on hover or in expanded views.例如，对具有多个检查日期的数组应用缩减器，可以在表格或应用程序中查看属性时只显示最近的日期，同时确保整个数组在查询和其他作时依然可访问。支持缩减器的应用程序，如 Workshop，也允许你在悬停或展开视图中查看整个阵列。


Reducers work with array properties containing numeric, temporal, string, and boolean base types. You can reduce [struct](/docs/foundry/object-link-types/structs-overview/) arrays based on any struct field that uses a supported base type. Review the [tables below](#supported-and-unsupported-base-types) to learn more about a property reducer's supported base types.缩减器处理包含数值、时间、字符串和布尔基类型的数组属性。你可以根据任何使用支持基类型的结构字段来缩减结构数组。 请查看下表 ，了解房产减压器的支撑基底类型。


## [](#when-to-use-property-reducers)When to use property reducers何时使用房产减压器


Use property reducers when:在以下情况下使用房屋减压器：


- Your historical or temporal data is stored in arrays, such as inspection dates, status updates, or measurement readings.您的历史或时间数据存储在数组中，如检查日期、状态更新或测量读数。
- You want to display the latest/earliest, highest/lowest, or first/last array value in a table or application while preserving the property's full history.你希望在表或应用中显示最新/最早、最高/最低或第一个/最后一个数组值，同时保留该属性的完整历史。
- Array properties require non-array types to satisfactorily implement [interface properties](/docs/foundry/interfaces/implement-interface/).数组属性要求非数组类型能够满意地实现接口属性 。


## [](#supported-and-unsupported-base-types)Supported and unsupported base types支持和不支持的基类型


Reducers work with array properties based on the underlying base type. The following tables categorize which array subtypes support reducers and which do not.减少器基于底层基类型处理数组属性。下表分类了哪些数组子类型支持缩减器，哪些不支持。


### [](#supported-base-types)Supported base types支持的基底类型


Property reducers are available for arrays containing the following subtypes:包含以下子类型的数组可用属性简化器：





































| Category类别 | Base types基础类型 | Reducer options减速器选项 |
| --- | --- | --- |
| **Numeric数值** | `Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`, `Decimal`字节 、 短、 整数 、 长 、 浮点数、 双倍 、 十进制 | Highest, lowest最高，最低 |
| **Temporal时间** | `Date`, `Timestamp`日期 ， 时间戳 | Most recent (latest), Least recent (earliest)最新（最新）、最晚（最早） |
| **String弦** | `String` | First, last (lexicographically)第一，最后（字典序） |
| **Boolean布尔值** | `Boolean` | True first, false first真先，假先 |
| **Struct结构** | By any supported struct field [outlined below](#support-for-struct-arrays)由下文列出的任何支撑结构场 | Depends on the base type of the struct field这取决于结构字段的基类型 |


### [](#unsupported-base-types)Unsupported base types无支持基底类型


Property reducers are *not* available for arrays containing the following subtypes:包含以下子类型的数组不提供属性缩减器：


- `Attachment`
- `Cipher Text`
- `Geohash`
- `Geoshape`
- `Geotime Series Reference`
- `Marking`
- `Media Reference`
- `Time Dependent`
- `Vector`


### [](#support-for-struct-arrays)Support for struct arrays结构数组的支持


Reducers function on struct arrays based on a specific **field** within the struct, not the struct itself. You can only reduce by struct fields that use one of the [supported base types](#supported-base-types) listed above. You can also configure multiple reducers using different struct fields to handle tie-breaking scenarios.Reducer 的作用是基于结构体内特定字段的结构数组，而不是结构本身。你只能通过使用上述支持基类型之一的结构体字段来减少。你还可以配置多个缩减器，使用不同的结构字段来处理平局破坏情景。


## [](#configure-a-property-reducer)Configure a property reducer配置属性减排器


1. Navigate to **Ontology Manager**.进入 Ontology Manager。
2. Search for and select your object type by choosing **Object types** under **Resources** in the left panel.在左侧面板的资源下选择 “对象类型 ”，搜索并选择你的对象类型。
3. Select the array property to configure from your object type's **Properties** tab.从你的对象类型的属性标签页中选择要配置的数组属性。
4. Choose the **Interaction** tab in the property editor panel that opens on the right.选择右侧打开的属性编辑器面板中的交互标签。
5. Scroll to the **Reduce array** section.滚动到 “减少数组 ”部分。


![Property sidebar with Interactions tab](property-reducers-interactions-tab.png?width=800)


1. Select **Add array reducer**.选择添加阵列缩减器 。
2. Select your desired [reducer option](#supported-base-types) based on the property's base type.根据房产的基底类型选择你想要的减压器选项 。


![Add reducer section](property-reducers-add-reducer-section.png?width=600)


1. **Save** your changes.保存你的更改。


## [](#configure-a-property-reducer-for-struct-arrays)Configure a property reducer for struct arrays为 struct 数组配置属性缩减器


Struct arrays offer the most flexibility for reducers. You can reduce based on any field in the struct that uses a [supported base type](#supported-base-types) and configure multiple reducers for tie-breaking scenarios.结构阵列对缩减器提供了最大的灵活性。你可以根据结构中任何使用支持基类型的字段进行简化，并配置多个简化器以应对平局。


### [](#example-customer-review-history)Example: Customer review history示例：客户评价历史


Consider a `Product` object type with a `customerReviews` struct array property that contains the following fields:考虑一个产品对象类型，其 customerReviews 结构数组属性包含以下字段：


- `rating` (`Integer`): A one to five star rating.评分 （ 整数 ）：一到五星。
- `reviewDate` (`Date`): The date the customer posted the review.reviewDate（ 日期 ）：客户发布评论的日期。
- `reviewerName` (`String`): The reviewer's name.评审者姓名 （ 字符串 ）：评审者的名字。
- `verifiedPurchase` (`Boolean`): Indicates whether or not the purchase was verified.验证购买 （ 布尔值 ）：表示购买是否已验证。


Sample data for a `Product` object's `customerReviews` property resembles:产品对象的 customerReviews 属性示例数据类似于：































| `rating` | `reviewDate` | `reviewerName` | `verifiedPurchase` |
| --- | --- | --- | --- |
| 5 | 2024-11-20 | Alice Chen陈爱丽丝 | true确实如此 |
| 3 | 2024-11-15 | Bob Smith鲍勃·史密斯 | false错误 |
| 4 | 2024-11-22 | Carol Lee卡罗尔·李 | true确实如此 |


### [](#configure-a-single-reducer)Configure a single reducer配置一个减速器


Tip提示Review the [property reducer configuration instructions](#configure-a-property-reducer) and the [supported base types](#supported-base-types) table before proceeding.在继续之前，请查看属性减排器的配置说明和支持的基类型表。


You can configure a single reducer on a struct field, which Foundry uses to reduce the array of structs to a single struct, sorting the values to display by the field with the configured reducer.你可以在结构体字段上配置一个缩减器，Foundry 用它来将结构数组缩减为单个结构体，并用配置的缩减器按字段排序显示的值。


- **Single reducer:** Render the latest `reviewDate`.单减速器： 呈现最新的审核日期 。
- **Result:** Displays the struct containing Carol Lee's four star review from `2024-11-22`.结果： 显示包含 Carol Lee 于 2024-11-22 的四星评价的结构。


Users can still query for and access the full review history.用户仍可查询并访问完整的评论历史。


### [](#configure-multiple-reducers)Configure multiple reducers配置多个减速器


You can configure multiple reducers to handle tie-breaking scenarios:你可以配置多个减免器来处理平局决胜情景：


- **Primary reducer:** Sort the structs and display the struct with the latest `reviewDate`.初级减速器： 排序结构体并显示带有最新 reviewDate 的结构体。
- **Fallback reducer:** Render the highest `rating`.备用减速器： 提供最高评分 。
- **Use case:** If two reviews are posted on the same day, render the higher-rated review.使用场景： 如果同一天发布两条评论，请发布评分更高的评论。


The fallback reducer *only* applies when the primary reducer results in multiple items. The primary reducer is always evaluated first, and only items that tie on the primary criteria are further reduced by the fallback reducer. This reduction behavior is repeated for any additional configured reducers.备用缩减器仅在主缩减器产生多个项目时适用。主缩减器总是先被评估，只有符合主要标准的项目才会被备用缩减器进一步减少。这种减排行为会对任何额外的配置减小器重复。


![Struct array reducer configuration](property-reducers-struct-configuration.png?width=600)


## [](#how-reducers-appear-in-applications)How reducers appear in applications减小器在应用中的表现


Applications that support reducers display the reduced value in compact views like tables or lists, while providing access to the full array through an expanded view or on-hover mechanism. This approach allows users to quickly scan data without seeing verbose array representations, while still being able to inspect the complete array when needed.支持缩减器的应用程序会在紧凑视图（如表格或列表）中显示简化值，同时通过扩展视图或悬停机制访问整个数组。这种方法允许用户快速扫描数据而不看到冗长的数组表示，同时在需要时仍能检查整个数组。


For example, an application might display only `2024-11-22` (the most recent date) in a table cell, but reveal the full array of dates when the user hovers over or expands that cell.例如，应用程序可能只在表格单元格显示 2024-11-22（最近的日期），但当用户悬停或展开该单元格时，会显示完整的日期阵列。


## [](#use-property-reducers-with-interfaces)Use property reducers with interfaces使用带有接口的属性降低器


Use property reducers to ensure an array property can implement non-array interface properties. This allows object types with array data to be mapped to [interface properties](/docs/foundry/interfaces/implement-interface/) that expect single values.使用属性缩减器确保数组属性能够实现非数组接口属性。这使得带有数组数据的对象类型可以映射到期望单个值的接口属性 。


### [](#example-render-the-most-recent-equipment-maintenance-date-through-an-interface-implementation)Example: Render the most recent equipment maintenance date through an interface implementation示例：通过接口实现渲染最近的设备维护日期


**Interface:** `Asset`接口： 资产


- Property: `lastMaintenanceDate` (`Date`)财产：lastMaintenanceDate（ 日期 ）


**Object type:** `Equipment`对象类型： 设备


- Property: `maintenanceHistory` (`Date` array)
财产： 维护历史 （ 日期排列）- Values: `[2024-01-15, 2024-03-22, 2024-11-01]`价值观： [2024-01-15, 2024-03-22, 2024-11-01]
  - Values: `[2024-01-15, 2024-03-22, 2024-11-01]`价值观： [2024-01-15, 2024-03-22, 2024-11-01]
  
  - **Reducer:** Latest `maintenanceHistory` date.减小器： 最新维护历史日期。
- **Implementation:** `Date` array property implements a single `Date` through the configured reducer. A user will see `2024-11-01` when viewing the property via the interface.实现日期数组属性通过配置的缩减器实现单个日期 。用户通过界面查看房产时会看到 2024-11-01。


The `Equipment` object type can implement the `Asset` interface because the reducer allows its `maintenanceHistory` array property to be represented as a single `Date` value. When users view an `Equipment` object through the `Asset` interface, they see only the most recent maintenance date.设备对象类型可以实现资产接口，因为缩减器允许其 maintenanceHistory 数组属性表示为单一日期值。当用户通过资产界面查看设备对象时，他们只看到最近的维护日期。


![Interface implementation via reducer](property-reducers-interface-implementation.png?width=700)


When using a reduced array value on an object type to satisfy an interface property that is a parameter of an [interface action](/docs/foundry/action-types/actions-on-interfaces/), the action will return an error when called on objects of that type. However, you can still use the interface action for objects that do not implement the interface through a reduced array value.当使用对象类型的简化数组值满足接口属性（该接口行为的参数） 时，该动作在该类型对象上调用时会返回错误。不过，对于不通过缩减数组实现接口的对象，你仍然可以使用接口动作。


## [](#combine-property-reducers-with-struct-main-fields)Combine property reducers with struct main fields将属性缩减器与结构主字段结合


When you combine property reducers with [struct main fields](/docs/foundry/object-link-types/struct-main-fields/), you enable property display and expand the number and shape of interfaces they can implement.当你将属性缩减器和结构主字段结合时，你会启用属性显示，并扩展它们能实现的接口数量和形状。


Consider the `Event` object type below, which contains a `Locations` property that is an array of structs:请考虑下面的事件对象类型，其中包含一个 Locations 属性，这是一个结构数组：


**Object type:** `Event`对象类型： 事件


- Property: `locations` (`Struct` array)
属性： 位置（ 结构数组）- Struct fields: `streetName` (`String`), `dateCollected` (`Date`), `numberOfGuests` (`Integer`).结构体字段：streetName（ 字符串 ）、dateCollected（ 日期 ）、numberOfGuest（ 整数 ）。
  - Struct fields: `streetName` (`String`), `dateCollected` (`Date`), `numberOfGuests` (`Integer`).结构体字段：streetName（ 字符串 ）、dateCollected（ 日期 ）、numberOfGuest（ 整数 ）。
  
  - **Main field configured:** `streetName`主字段配置： 街道名称
- **Reducer configured:** Most recent by `dateCollected`.减速器配置如下： 最新日期  已收集 。


With the `streetName` field configured as the main field and most recent `dateCollected` as the property reducer, this enables multiple interface implementation options:将 streetName 字段配置为主字段，最新的 dateCollected 作为属性缩减器，这支持多种接口实现选项：



























| Configuration配置 | Can implement可以实现 |
| --- | --- |
| Neither feature configured这两个功能都未配置 | `Struct Array` only仅限结构数组 |
| Main field only仅限主场 | `Struct Array`, `String Array`结构数组 ， 字符串数组 |
| Reducer only仅限减速器 | `Struct Array`, `Struct`结构数组 ， 结构 |
| **Both configured两者都配置好了** | `Struct Array`, `String Array`, `Struct`, `String`结构数组 ， 字符串数组 ， 结构体， 字符串 |


As an example, with both a struct main field and property reducer configured, you can use the `locations` property to fulfill a *single* string property from an interface, such as `Event street name` from the notional `Event` interface in the image below.举个例子，在结构主字段和属性减少器都配置好后，你可以用 locations 属性满足接口中的单个字符串属性，比如下图中假想事件接口的事件街名 。


![Single string implementation via reducer and main field](property-reducers-combination-single-string.png?width=700)


When you configure both a struct main field and a property reducer, the transformation:当你同时配置结构体主字段和属性缩减器时，转换过程：


- Applies the configured property reducer, fetching the most recent location based on its date.应用配置的属性缩减器，根据日期获取最近的位置。
- Extracts the configured main field and returns its value as a string.提取配置的主字段，并返回其字符串值。


This means a single property can implement interfaces requiring any of these types: `Struct Array`, `String Array`, `Struct`, or `String`.这意味着单个属性可以实现需要以下任意类型的接口： 结构数组 、 字符串数组 、 结构体或字符串 。


## [](#limitations-and-considerations)Limitations and considerations局限性与考虑


- **No direct querying of reduced value:** You cannot filter or query based on the reduced value. Queries operate on the full array, not the reduced representation.不直接查询降低价值： 你不能根据缩减值进行筛选或查询。查询作的是整个数组，而不是简化表示。


## [](#faqs)FAQs常见问题解答


### [](#can-i-change-or-remove-a-reducer-after-configuration)Can I change or remove a reducer after configuration?配置后我可以更换或移除减速器吗？


Yes, you can modify or remove reducers at any time in Ontology Manager. Changes do not require a reindex and take effect immediately.是的，你可以随时在 Ontology Manager 中修改或移除缩减器。变更无需重新索引，立即生效。


### [](#what-happens-if-multiple-items-tie-for-the-reducer-criteria)What happens if multiple items tie for the reducer criteria?如果多个物品符合减量器标准，会发生什么？


For struct arrays, you can configure fallback reducers to handle ties. The fallback reducer is only evaluated for items that tie on the primary reducer. For primitive arrays or structs without fallback reducers, one of the tied values is returned in a deterministic but unordered manner.对于结构数组，你可以配置备用缩减器来处理平局。备用减速器只针对与主减速器相连的项目进行评估。对于没有退回缩减器的原始数组或结构体，其中一个绑定值以确定性但无序的方式返回。


### [](#can-i-use-reducers-with-edit-only-properties)Can I use reducers with edit-only properties?我可以用带有仅编辑属性的缩减器吗？


Yes, you can configure reducers for [edit-only properties](/docs/foundry/object-link-types/edit-only-properties/). The reducer configuration is independent of whether the property has a backing column.是的，你可以配置仅编辑属性的减员器。减压器配置与该物业是否有背衬柱无关。


### [](#do-reducers-function-across-all-applications)Do reducers function across all applications?减针在所有应用中都能正常工作吗？


Applications are progressively rolling out support for reduced properties. If you configure a reducer on a property and use an application that doesn't yet support reducers, it should not break any existing functionality, the property will simply continue to be displayed as an array. Only applications that support reducers will have the ability to display the reduced value.应用程序正在逐步推广对低成本房产的支持。如果你在某个属性上配置了缩减器，并且使用了一个还不支持缩减器的应用程序，它不应该破坏任何已有的功能，属性会继续以数组形式显示。只有支持减量器的应用程序才能显示减量值。

