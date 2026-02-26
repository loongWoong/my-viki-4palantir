# [](#use-value-types)Use value types使用价值类型


Once you have [created a value type](/docs/foundry/object-link-types/create-value-type/), you can use it in as a data type across Foundry. Value types can be supported for the use cases listed below.一旦你创建了一个值类型 ，就可以在 Foundry 中作为数据类型使用它。以下用例可以支持价值类型。


- Assigning a value type to an object type property.为对象类型属性赋予值类型。
- Assigning a value type to a shared property.为共享属性分配值类型。
- Assigning a value type to a Pipeline Builder pipeline property as a logical type using the `logical type cast` expression and selecting the value type on the property when you write to the objects target.使用逻辑类型 cast 表达式为管道构建器的流水线属性分配值类型作为逻辑类型，并在写入目标对象时选择该属性上的值类型。


To assign a value type to a property, select the value type from the dropdown menu during property configuration.要为属性分配值类型，请在属性配置时从下拉菜单中选择该值类型。


![Constraint update warning](value-type-use.png?width=500)


If you apply a value type to an object property that contains property values that fail validation, that object type will fail to index. You can view such index failures in the object type health status in Ontology Manager, where you can correct your data or update your value type to fix the issue.如果你对包含失败验证的属性属性应用值类型，该对象类型将无法索引。你可以在 Ontology Manager 的对象类型健康状态中查看这些索引失败，在那里你可以修正数据或更新值类型来修复问题。

