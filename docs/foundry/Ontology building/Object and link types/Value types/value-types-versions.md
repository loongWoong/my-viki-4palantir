# [](#value-type-versions)Value type versions价值类型版本


Value types are versioned to handle breaking and non-breaking edits. Value type versions include two parts: metadata and constraints. The metadata values for name, description, and apiName can be changed whenever necessary. The base type metadata and the constraints that define the validation rules for the type are immutable.值类型会被版本化处理，以处理中断和非破坏编辑。值类型版本包括两部分：元数据和约束。名称、描述和 apiName 的元数据值可以随时更改。基础类型元数据和定义该类型验证规则的约束是不可变的。


If you choose to update the constraints of a value type, a new version of the value type is created. If your value type has no consumers, you can freely change these constraints. However, if you make breaking changes to the constraints and your value type has consumers, we recommend deprecating the current value type and creating a new one instead. This approach avoids potential runtime errors and data inconsistencies.如果你选择更新某个值类型的约束，会创建一个新的版本。如果你的值类型没有消费者，你可以自由更改这些约束。然而，如果你对约束进行了破坏性更改，且你的值类型包含了消费者，我们建议弃弃当前的值类型，并创建一个新的。这种方法避免了运行时可能出现的错误和数据不一致。


![Constraint update warning](value-type-versioning.png?width=500)


When you make non-breaking changes to a value type, a new version is also created. This new version will automatically propagate to the Ontology, ensuring that all uses of the value type across the Ontology are updated to the latest version.当你对某个值类型做出非破坏性更改时，也会创建一个新版本。该新版本会自动传播到本体，确保该值类型在本体中的所有使用均更新为最新版本。

