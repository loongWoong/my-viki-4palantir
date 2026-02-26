# [](#add-value-formatting)Add value formatting增值格式


**Value formatting** refers to applying a special formatter to the value of a property, transforming the raw value to a more readable version. In the image below, the left-hand side (**Before**) shows the `weight` and `value` columns without any formatting. The right-hand side (**After**) has a unit (“kg”) applied to the `weight` column and the `value` column is displayed in a more compact form with a currency sign (“$100K”). These are both examples of numeric formatting. The Ontology also supports date and time formatting, as well as user ID formatting, resource RID formatting, and artifact GID formatting.值格式化是指对属性的值应用特殊的格式化器，将原始值转换为更易读的版本。在下图中，左侧（ 之前 ）显示了权重和值列，没有任何格式。右侧（ 之后 ）在权重栏上加了一个单位（“kg”）， 价值栏以更紧凑的形式显示，并带有货币符号（“$100K”）。这两种都是数字格式化的例子。本体还支持日期和时间格式化，以及用户 ID 格式化、资源 RID 格式化和工件 GID 格式化。


![Value formatting example](value-formatting-numeric-formatting-example.png?width=600)


## [](#supported-value-formatting)Supported value formatting支持的值格式化































| Type类型 | Description描述 |
| --- | --- |
| Numeric formatting数字格式化 | Add currencies/units/prefixes, various types of notations (compact, scientific), and percentages. See the [numeric formatting section](#numeric-formatting-options) for more details.添加货币/单位/前缀，各种符号（简洁、科学）和百分比。详情请参见数字格式部分 。 |
| Date and time formatting日期和时间格式 | Render timestamps and dates in a specific format as well as in a specific timezone.以特定格式和特定时区渲染时间戳和日期。 |
| Foundry ID formattingFoundry ID 格式化 | Display a Foundry ID as a user's first and last name or group name.将 Foundry ID 显示为用户的名字和姓氏或组名。 |
| Resource RID formatting资源 RID 格式化 | Display a Foundry resource ID (RID) as an icon and resource name, with a clickable link that routes to that resource.将 Foundry 资源 ID（RID）作为图标和资源名称显示，并配有可点击的链接指向该资源。 |
| Artifact GID formatting工件 GID 格式化 | Display an artifact global ID (GID) as an icon and artifact name, with a clickable link that routes to that artifact.将全局工件 ID（GID）作为图标和工件名称显示，并配有可点击的链接，可路由到该工件。 |


## [](#add-value-formatting-1)Add value formatting增值格式


In the property editor:在属性编辑器中：


1. Select the property to which you want to add value formatting.选择你想添加值格式的属性。
2. On the right hand side panel of the properties pane, you will see a type of formatting depending on the base type of the property (value formatting, numeric formatting, date and time formatting, etc.). Toggle on the formatting.在属性面板的右侧面板上，你会看到根据属性的基础类型（值格式、数字格式、日期和时间格式等）进行格式化。切换格式。


![Value formatting toggle](value-formatting-toggle.png?width=500)


1. Additional formatting options are available for numeric formatting and date and time formatting, as described below:
还有数字格式和日期时间格式选项，如下所述：- [Numeric formatting options数字格式选项](#numeric-formatting-options)
- [Date and time formatting options日期和时间格式选项](#date-and-time-formatting-options)
  - [Numeric formatting options数字格式选项](#numeric-formatting-options)
  - [Date and time formatting options日期和时间格式选项](#date-and-time-formatting-options)
  
  2. As you select the available formatting options, you will see a preview for how values of the property will be rendered with the new formatting applied.当你选择可用的格式选项时，你会看到一个预览，展示在应用新格式后该属性的值如何被渲染。


### [](#numeric-formatting-options)Numeric formatting options数字格式选项


![Numeric formatting options](value-formatting-numeric-formatting.png?width=500)





































| Name名称 | Description描述 | Usage用途 |
| --- | --- | --- |
| **Numeric formatting数字格式化** | On/Off toggle.开关。 | Toggle this to remove/add numeric formatting.切换这个功能以移除或添加数字格式。 |
| **Base type基础类型** | Contains various types of formatting available (Currency, Unit, Percentage, Prefix/Suffix, Fixed Values) as well as examples and descriptions of each type.包含多种格式类型（货币、单位、百分比、前缀/后缀、固定值），以及每种类型的示例和描述。 | If `Capacity in Pounds` has an associated unit, select "Unit" from this dropdown.如果 “承重” 单位（磅）有对应单位，请从下拉菜单中选择“单位”。 |
| **Use grouping使用分组** | Adds locale-aware comma separator.增加了区域感知逗号分隔符。 | Toggle this on to go from 123456 to 123,456.开启此键，从123456提升到123,456。 |
| **Notation符号** | Contains Compact/Scientific and Engineer notations.包含紧凑/科学和工程符号。 | Choose compact to approximate values, like 123K.选择紧致来近似值，比如 123K。 |
| **Preview result预览结果** | View and test numeric formatting.查看并测试数字格式。 | Add any number in the input that is similar to what you'd expect to see in your property's values for a preview of the formatting.输入中加入任何与你期望在属性值中看到的数字相似的数字，以便预览格式。 |


### [](#date-and-time-formatting-options)Date and time formatting options日期和时间格式选项


![Date and time formatting options](value-formatting-date-formatting.png?width=500)










































| Name名称 | Description描述 | Example示例 |
| --- | --- | --- |
| **Date日期** | Only the date (no time)只有日期（没有时间） | `Wed, Jul 22, 2020` |
| **Date and time (long)日期和时间（长篇）** | Both the date and time, in long form日期和时间，详细说明 | `Wed, July 22, 2020, 1:00:00 PM` |
| **Date and time (short)日期和时间（简短）** | Both the date and time, in short form日期和时间，简要说明 | `Jul 22, 2020, 1:00 PM` |
| **ISO instantISO 瞬间** | Both the date and time (ISO 8601 format)日期和时间（ISO 8601 格式） | `2020-07-22T13:00:00.000Z` |
| **Relative to now相对于现在** | The date relative to right now相对于现在的日期 | `8 minutes ago` |
| **Time时间** | Only the time (no date)只有时间（无日期） | `1:00 pm` |


When formatting **Relative to now**, applications will only format in relative terms up to 24 hours ago. After this, it will render in **Date and time (short)** form with the day of the week: `Wed, Jul 22, 2020, 1:00 PM`.在格式化“ 相对于现在 ”时，应用程序只会以 24 小时前的相对格式化。之后，它将以日期和时间（简短） 形式显示，显示星期几：2020 年 7 月 22 日星期三，下午 1：00。


![Relative to now](value-formatting-relative-to-now.png?width=300)


#### [](#time-zones)Time zones时区


If you are formatting a timestamp, you can specify which timezone to render the timestamp, either as a static timezone that you input, or as the application user's current timezone. When entering a static timezone, you can search for a timezone by inputting the UTC offset or the locale name.如果你在格式化时间戳，可以指定渲染时间戳的时区，可以是你输入的静态时区，也可以是应用用户当前的时区。输入静态时区时，可以通过输入 UTC 偏移或地区名称来搜索时区。


### [](#user-id-formatting)User ID formatting用户 ID 格式化


Value formatting can be applied to strings that are Foundry/Multipass user IDs or group IDs and convert them to display the user's first and last name or the group name by selecting the **Multipass username** option. This value formatting option is typically used when you have created an [Action](/docs/foundry/action-types/overview/) that edits a property and stores a user ID or group ID in one of the property fields. In the backing data, this information will be stored as the user's Foundry user ID or group ID, and the value formatting can be applied to render the user's name or the group instead of the ID.对于 Foundry/Multipass 用户 ID 或组 ID 的字符串，可以应用值格式，并通过选择 Multipass 用户名选项转换为显示用户的名字和姓氏或组名。这个值格式选项通常用于创建一个动作，该动作编辑属性并在属性字段中存储用户 ID 或组 ID。在后备数据中，这些信息将以用户的 Foundry 用户 ID 或组 ID 的形式存储，值格式化时可以渲染用户名或组，而非 ID。


## [](#faq)FAQ常见问题


### [](#will-this-work-with-existing-type-classes)Will this work with existing type classes?这对现有类型类有效吗？


Value formatting takes precedence over existing type classes in the UI. If you have both configured, value formatting will be displayed. You can however, use value formatting on one property and type classes on another.在 UI 中，值格式化优先于现有类型类。如果两者都配置好，会显示值格式。不过，你可以在一个属性上使用值格式化，在另一个属性上用类型类型。


### [](#will-this-work-with-editable-properties-in-object-views)Will this work with editable properties in Object Views?这对对象视图中的可编辑属性有效吗？


Value formatting is supported for properties configured for [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits). Properties with the legacy `hubble:editable` type class will disable value formatting.支持为内联编辑配置的属性使用值格式。带有旧有 hubble：editable 类型类的属性会禁用值格式化。

