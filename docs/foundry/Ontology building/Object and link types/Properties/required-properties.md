# [](#required-properties)Required properties所需属性


Required properties are object type properties that must have a value. You can use this object type property to validate that there are no objects that have a null value for this property, or an empty array if it is an array property. This validation applies to data from the backing datasource and edits via actions.必需属性是必须有值的对象类型属性。你可以用这个对象类型属性来验证没有对象对该属性有空值，或者如果是数组属性，则没有空数组。这种验证适用于来自后备数据源的数据，并通过动作进行编辑。


## [](#summary-of-required-properties)Summary of required properties所需属性摘要


When working with required properties, keep the following in mind:在处理所需房产时，请牢记以下几点：


- **Validation happens when data is being indexed into the object:** The check for null values happens as backing datasources are indexed into Object Storage. This means that the ontology modification itself will succeed if the column backing a required property contains null values.验证发生在数据被索引到对象中时： 当备份数据源被索引到对象存储时，会检查空值。这意味着如果支持某项要求属性的列包含空值，则本体修改本身将成功。
- **Array properties cannot be empty:** Setting an array property to required ensures the presence of at least one item.数组属性不能为空： 将数组属性设置为必需，确保至少存在一个项目。
- **Changes via actions are validated at apply time:** If you attempt to write a null or empty value to a property via an action, the action will fail to execute.通过动作进行的变更在应用时进行验证： 如果你尝试通过动作写入空值或空值，该动作将无法执行。
- **Available only in Object Storage V2:** Required properties are only supported by object types leveraging Object Storage V2.仅在对象存储 V2 中提供： 所需属性仅由利用对象存储 V2 的对象类型支持。


### [](#create-a-required-property)Create a required property创建一个必需属性


1. Navigate to **Ontology Manager**.进入 Ontology Manager。
2. Choose the object type, and then the property you want to set as required.选择对象类型，然后选择你想设置的属性。
3. Select **Create Property** and fill in the required details, including the property name, type, and description.选择创建物业 ，填写所需信息，包括物业名称、类型和描述。
4. Under the **Configuration** section, toggle on the **Required** toggle.在配置部分，切换“ 必需 ”开关。
5. **Save** your changes to the Ontology and wait for the reindex to be completed.将你的更改保存到本体中，等待重新索引完成。


Note that if there is any null value currently set on the backing column for the property, the reindex will fail. To fix this, you must either update the backing datasource to no longer have nulls in the column, or unset the property as required.注意，如果该属性的背景列当前设置了任何空值，重新索引将失败。要解决这个问题，你要么必须更新后备数据源，使其列中不再有空，要么按需要取消该属性。


![Required property toggled in configuration pane.](required_property.png?width=500)


### [](#required-properties-that-allow-empty-arrays)Required properties that allow empty arrays允许空数组的必要属性


You can configure your required property to allow empty arrays. This means that the property will still reject null values, but will accept empty arrays. This is useful for mandatory control properties which can never be null, but can be configured to allow empty arrays. Learn more about [mandatory control properties](/docs/foundry/object-link-types/mandatory-control-properties/).你可以配置所需属性，允许空数组。这意味着该性质仍会拒绝空值，但接受空数组。这对于强制控制属性非常有用，这些属性永远不会为空，但可以配置为允许空数组。了解更多关于强制控制属性的信息 。


It is important to note that Actions will write an empty array to any property that is mapped to a parameter, but the parameter is not set. This means that if you have a required property that allows empty arrays, and you leave the parameter blank in an Action, the Action will succeed and write an empty array to the property. If you do not want this behavior and want to enforce that users always set a value for this property via Actions, you should not allow empty arrays on your required property.需要注意的是，Actions 会为任何映射到参数但该参数未被设置的属性写入空数组。这意味着如果你有一个允许空数组的必要属性，并且你在某个动作中保持参数空，该动作将成功并写入空数组。如果你不希望这种行为，并且想强制用户通过 Actions 始终为该属性设置值，那么你不应该允许在所需属性上设置空数组。


![Advanced required property configuration](advanced_required_property.png?width=500)


### [](#required-properties-for-object-types-with-multiple-backing-datasources)Required properties for object types with multiple backing datasources具有多个后备数据源的对象类型所需的属性


You may occasionally encounter situations where null values appear in required properties of object types backed by multiple datasources. This phenomenon occurs when a record for the object is present in some datasources, but absent in the datasource that supplies the required property.你偶尔会遇到在多个数据源支持的对象类型所需属性中出现空值的情况。当某些数据源中存在该对象的记录，但在提供所需属性的数据源中缺失时，就会发生这种现象。


The following example illustrates this behavior. Assume there is a `Movie` object type with two backing datasources and a `Genre` property that is required.以下示例说明了这种行为。假设有一个电影对象类型 ，带有两个备份数据源和一个类型属性，并且需要一个类型属性。


**Datasource 1数据来源 1**































| Movie Id电影本位 | Title标题 | Box office票房 | Regions地区 |
| --- | --- | --- | --- |
| 101 | The Adventure Begins冒险开始 | 200m200米 | ["USA", "Canada", "UK"][“美国”、“加拿大”、“英国”] |
| 102 | Love in the City城市之爱 | 75m75米 | [] |
| 103 | Galactic Battles银河战役 | 500m500米 | ["USA", "UK", "Australia"][“美国”、“英国”、“澳大利亚”] |


**Datasource 2数据来源2**































| Movie Id电影本位 | Budget预算 | Genre (Required)类型（必备） | Director导演 |
| --- | --- | --- | --- |
| 101 | 50m50米 | Adventure冒险 | Michael John Smith迈克尔·约翰·史密斯 |
| 102 | 20m20米 | Romance恋爱 | Jane Doe无名女尸 |
| 103 | 150m150米 | Sci-Fi科幻 |  |


If a new `Movie` is added to both backing datasources without providing a value for `Genre`, it will fail to index to the Ontology.如果新电影被添加到两个支持数据源中但未提供类型值，则无法索引到本体。


However, suppose only Datasource 1 had a row for the new `Movie` object.然而，假设只有 Datasource 1 有一行用于新的 Movie 对象。


**Datasource 1数据来源 1**





































| Movie Id电影本位 | Title标题 | Box office票房 | Regions地区 |
| --- | --- | --- | --- |
| 101 | The Adventure Begins冒险开始 | 200m200米 | ["USA", "Canada", "UK"][“美国”、“加拿大”、“英国”] |
| 102 | Love in the City城市之爱 | 75m75米 | [] |
| 103 | Galactic Battles银河战役 | 500m500米 | ["USA", "UK", "Australia"][“美国”、“英国”、“澳大利亚”] |
| 104 | Happy Ending幸福结局 | 150m150米 | ["UK", "FRANCE"][“英国”、“法国”] |


**Datasource 2数据来源2**































| Movie Id电影本位 | Budget预算 | Genre (Required)类型（必备） | Director导演 |
| --- | --- | --- | --- |
| 101 | 50m50米 | Adventure冒险 | Michael John Smith迈克尔·约翰·史密斯 |
| 102 | 20m20米 | Romance恋爱 | Jane Doe无名女尸 |
| 103 | 150m150米 | Sci-Fi科幻 |  |


The example above will successfully get indexed into the Ontology, despite the fact that the resulting object would have no value for the required property.上述示例将成功索引到本体中，尽管最终对象对所需属性没有任何值。







































| Property财产 | Value价值 |
| --- | --- |
| Movie Id电影本位 | 104 |
| Title标题 | Happy Ending幸福结局 |
| Box Office票房 | 150m150米 |
| Regions地区 | ["UK", "FRANCE"][“英国”、“法国”] |
| Budget预算 |  |
| Genre (Required)类型（必备） |  |
| Director导演 |  |


The same applies to objects created via Action edits. `Movie` objects can be created or modified successfully, if they only contain properties tied to columns in `Datasource 1`. However if the Action adds a property to the object that is sourced from `Datasource 2`, such as `Budget`, then the Action will be invalid and will fail to execute. This is because the object will now be present on `Datasource 2` and thus `Genre` must be set.通过动作编辑创建的对象也是如此。如果电影对象只包含与 Datasource 1 列相关联的属性，就可以成功创建或修改。然而，如果动作在对象中添加了来源于数据源 2 的属性，如  预算 ，则该动作将无效且无法执行。这是因为该对象现在会出现在 Datasource 2 上，因此 必须设置类型  。

