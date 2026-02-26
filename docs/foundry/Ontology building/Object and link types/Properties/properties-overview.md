# [](#properties)Properties性质


A **property** of an [object type](/docs/foundry/object-link-types/object-types-overview/) is the schema definition of a characteristic of a real-world entity or event. A **property value** refers to the value of a property on an object, or a single instance of that real world entity or event.对象类型的属性是对现实世界实体或事件特征的模式定义。 属性值指的是属性在对象或该现实世界实体或事件的单个实例上的价值。


For example, in the Ontology Manager, an `Employee` object type may have properties `employee number`, `start date`, and `role`. The notional employee “Melissa Chang” may have property values “11502” for `employee number`, “October 9, 2016” for `start date`, and “software engineer” for `role`.例如，在本体管理器中， 员工对象类型可能具有员工编号 、 起始日期和角色等属性。名义员工“Melissa Chang”的物业价值可能为“11502”作为员工编号 ，“2016 年 10 月 9 日”作为入职日期 ，“软件工程师”作为职位 。


Similarly, in the Ontology Manager, a `Flight` object type may have properties `departure date`, `arrival date`, and `passenger count`. The object “JFK → SFO 24-02-2021” may have property values “24-02-2021” for `departure date`, “25-02-2021” for `arrival date`, and “150” for `passenger count`.同样，在本体管理器中， 飞行对象类型可能具有出发日期 、 到达日期和乘客数量等属性。物品“JFK → SFO 24-02-2021”可能包含“24-02-2021”（ 出发日期 ）、“25-02-2021”（ 抵达日期 ）和“150”（乘客数量 ）。


The concepts underpinning the Ontology have analogous concepts in the structure of a dataset. The definition of a property in the Ontology is analogous to that of a column in a dataset, while the definition of a property value is analogous to that of a field in the dataset. For example, an `Employee` dataset may have columns for `departure date`, `arrival date`, and `passenger count`. In this case, a single field will have the value “11502” for the `employee number` column of the row for employee “Melissa Chang.”支撑本体论的概念在数据集结构中也有类似的概念。本体中属性的定义类似于数据集中的列，而属性值的定义类似于数据集中的字段。例如， 员工数据集可能包含出发日期 、 到达日期和乘客数量的列。在这种情况下，员工“Melissa Chang”行的员工编号列将有一个字段值为“11502”。


Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. Property values are created and displayed in user applications by adding backing datasources to an object type in the Ontology Manager. To create property values for properties `employee number`, `start date`, and `role` on objects of type `Employee`, an organization will add backing datasources to the `Employee` object type and feed their employee directory and other enterprise data into the Ontology.Foundry 本体论不是抽象数据模型，而是将每个本体概念映射到组织的实际数据，使这些数据资产能够驱动现实应用。属性值通过在 Ontology Manager 中向对象类型添加后备数据源来创建和显示。为了为类型为 Employee  的对象创建属性值， 组织会将后备数据源添加到 Employee 对象类型，并将员工目录及其他企业数据输入本体。


## [](#supported-property-types)Supported property types支持的财产类型





















































































| Property base type财产基底类型 | Valid as title key?作为标题密钥有效吗？ | Valid as primary key?作为主键有效吗？ | Notes注释 |
| --- | --- | --- | --- |
| Commonly used: `String`, `Integer`, `Short`常用： 字符串 、 整数 、 短字符串 | Yes是的 | Yes是的 |  |
| Time-based: `Date`, `Timestamp`基于时间： 日期 ， 时间戳 | Yes是的 | Discouraged沮丧 | Typically, time values are inappropriate as primary keys, due to potentially unexpected collisions / uniqueness based on the storage format differing from the display format. In most cases, we recommend using `String` instead.通常，时间值作为主键不合适，因为存储格式与显示格式不同，可能导致意外碰撞或唯一性。大多数情况下，我们建议使用 String。 |
| Number-like: `Boolean`, `Byte`, `Long`类数字： 布尔、 字节 、 长 | Yes是的 | Discouraged沮丧 | `Boolean` limits your object type to two object instances. `Byte` properties can only be assigned in Actions via an `Integer` parameter, so in most cases we recommend using `Integer` properties instead. `Long` has [representational issues in Javascript](https://www.w3schools.com/js/js_numbers.asp#:~:text=JavaScript%20Numbers%20are%20Always%2064,the%20international%20IEEE%20754%20standard.), so not all frontend libraries and code work well with `Long` values greater than 1e15. In most cases, we recommend using `String` instead.布尔限制你的对象类型只有两个对象实例。字节属性只能通过整数参数在动作中分配，因此大多数情况下我们建议使用整数属性。Long 在 Javascript 中存在表示问题 ，所以并非所有前端库和代码都能很好地支持 Long 值大于 1e15。大多数情况下，我们建议使用 String。 |
| Float-like: `Float`, `Double`, `Decimal`浮点式： 浮点 、 双倍 、 十进制 | Yes是的 | No不 |  |
| `Vector` | No不 | No不 |  |
| `Array` | Yes是的 | No不 | Array properties cannot contain null elements.数组属性不能包含空元素。
If the inner type of the `Array` is not a valid title property, the `Array` property also cannot be used as the title property.如果数组的内部类型不是有效的标题属性，那么数组属性也不能用作标题属性。
Nested arrays are not supported in Object Storage V2.对象存储 V2 不支持嵌套数组。 |
| `Struct` | No不 | No不 | Struct properties do not support nesting, and fields cannot be arrays. See the [struct documentation](/docs/foundry/object-link-types/structs-overview/#struct-configuration) for detailed information on supported field types.结构体属性不支持嵌套，字段不能是数组。有关支持字段类型的详细信息，请参阅结构文档 。 |
| `Media Reference`, `Time Series`, `Attachment`媒体参考 、 时间序列 、 附件 | No不 | No不 |  |
| `Geopoint` | Yes是的 | No不 |  |
| `Geoshape` | No不 | No不 |  |
| `Marking` | No不 | No不 |  |
| `Cipher` | Yes是的 | No不 |  |


To learn more about base types, see [base types](/docs/foundry/object-link-types/base-types/).想了解更多关于碱型的信息，请参见 Base types。

