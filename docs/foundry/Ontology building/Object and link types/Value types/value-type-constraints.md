# [](#value-type-constraints)Value type constraints值类型约束


Each value type may optionally define a constraint to enforce data validation. You can configure these constraints when [creating a new value type](/docs/foundry/object-link-types/create-value-type/) in the **Value Type Manager** application. The available value type constraints, along with what base types they can be applied to, are below:每种值类型都可以选择性地定义一个约束以强制数据验证。你可以在值类型管理器应用中创建新值类型时配置这些约束。可用的值类型约束及其可应用的基类型如下：


- **Enum (one of):** A constraint representing a static set of allowed values.
Enum（其中一种）： 一个表示静态允许值集合的约束。- **Valid base types:** String, Boolean, Decimal, Double, Float, Integer, or Short.有效的基底类型： 字符串、布尔、十进制、双数、浮点数、整数或短。
- For String properties, the enum values may optionally be case-sensitive or case-insensitive.对于字符串属性，枚举值可以选择区分大小写或不区分大小写。
  - **Valid base types:** String, Boolean, Decimal, Double, Float, Integer, or Short.有效的基底类型： 字符串、布尔、十进制、双数、浮点数、整数或短。
  - For String properties, the enum values may optionally be case-sensitive or case-insensitive.对于字符串属性，枚举值可以选择区分大小写或不区分大小写。
  
  - **Range:** A minimum value, maximum value, or range of allowed values.
射程： 最小值、最大值或允许值范围。- **Valid base types:** Decimal, Double, Float, Integer, Short, Date, Timestamp, String, or Array.有效的基底类型： 小数、双数、浮点数、整数、短、日期、时间戳、字符串或数组。
- For String properties, the length of the string is constrained.对于字符串属性，字符串的长度是受限的。
- For Array properties, the size of the array is constrained.对于数组属性，数组的大小是受限的。
  - **Valid base types:** Decimal, Double, Float, Integer, Short, Date, Timestamp, String, or Array.有效的基底类型： 小数、双数、浮点数、整数、短、日期、时间戳、字符串或数组。
  - For String properties, the length of the string is constrained.对于字符串属性，字符串的长度是受限的。
  - For Array properties, the size of the array is constrained.对于数组属性，数组的大小是受限的。
  
  

Additionally, the following property types have additional type-specific constraints available:此外，以下属性类型还有额外的类型特定的约束：


- **String:弦：**
- **Regex:** A regex pattern that the string must match. The regex validation may optionally pass when matching only a substring of the property value.正则表达式： 字符串必须匹配的正则表达式模式。当仅匹配属性值的子串时，正则表达式验证可选择性通过。
- **RID:** The string must be a valid rid.RID： 字符串必须是有效的 rid。
- **UUID:** The string must be a valid UUID.UUID： 字符串必须是有效的 UUID。
  - **Regex:** A regex pattern that the string must match. The regex validation may optionally pass when matching only a substring of the property value.正则表达式： 字符串必须匹配的正则表达式模式。当仅匹配属性值的子串时，正则表达式验证可选择性通过。
  - **RID:** The string must be a valid rid.RID： 字符串必须是有效的 rid。
  - **UUID:** The string must be a valid UUID.UUID： 字符串必须是有效的 UUID。
  
  - **Array:阵列：**
- **Uniqueness:** All elements of the array must be unique.独特性： 数组中的所有元素必须是唯一的。
- **Nested:** A value type constraint can be applied to the elements of the array. For example, a regex constraint could be applied to every string in an array.嵌套： 可以对数组的元素应用值类型约束。例如，可以对数组中的每个字符串应用正则表达式约束。
  - **Uniqueness:** All elements of the array must be unique.独特性： 数组中的所有元素必须是唯一的。
  - **Nested:** A value type constraint can be applied to the elements of the array. For example, a regex constraint could be applied to every string in an array.嵌套： 可以对数组的元素应用值类型约束。例如，可以对数组中的每个字符串应用正则表达式约束。
  
  - **Struct:结构：**
- **Element constraints:** A mapping between a struct field identifier and a value type reference, where the struct field identifier indicates the struct component to which the referenced value type should be applied.元素约束： 结构体字段标识符与值类型引用之间的映射，其中结构字段标识符表示应应用该引用值类型应应用的结构组件。
  - **Element constraints:** A mapping between a struct field identifier and a value type reference, where the struct field identifier indicates the struct component to which the referenced value type should be applied.元素约束： 结构体字段标识符与值类型引用之间的映射，其中结构字段标识符表示应应用该引用值类型应应用的结构组件。
  
  
