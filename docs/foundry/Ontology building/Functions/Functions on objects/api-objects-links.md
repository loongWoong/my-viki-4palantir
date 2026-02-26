# [](#api-objects-and-links)API: Objects and linksAPI：对象和链接


Every [object type](/docs/foundry/object-link-types/object-types-overview/) imported into your project is converted to a TypeScript API so you can easily access and manipulate objects available in Foundry.你项目导入的每个对象类型都会转换为 TypeScript API，以便你能够轻松访问和操作 Foundry 中可用的对象。


### [](#properties)Properties属性


[Properties](/docs/foundry/object-link-types/properties-overview/) of each object type are converted to fields on the TypeScript interface generated for each object type. The generated field name uses the API Name specified in the ontology.每个对象类型的属性都会转换为为每个对象类型生成的 TypeScript 接口上的字段。生成的字段名使用本体中指定的 API 名称。


You can access the fields for each property with simple dot notation:你可以使用简单的点表示法访问每个属性的字段：


```
Copied!`1const firstName = employee.firstName;`
```


Note that because properties may not have a concrete value set, the returned type when accessing a property value could be `undefined`. The TypeScript compiler will give an error unless you explicitly handle the `undefined` case. See [this guide](/docs/foundry/functions/undefined-values/) for more details on this.请注意，因为属性可能没有设置具体的值，所以在访问属性值时返回的类型可能是 undefined 。除非你显式处理 undefined 情况，否则 TypeScript 编译器会报错。有关此问题的更多详细信息，请参阅此指南。


#### [](#array-properties)Array properties数组属性


Array properties on an object type are converted to `ReadOnlyArray` types. This is so that the semantics for [editing](/docs/foundry/functions/api-ontology-edits/) an array property are clear—the only way to modify the values of an array property is to update it with an entirely new array value.对象类型的数组属性会被转换为 ReadOnlyArray 类型。这是为了使编辑数组属性的语义清晰——修改数组属性值的唯一方式是用一个全新的数组值来更新它。


If you want to manipulate the values of an array property, make a copy of it:如果你想要操作数组属性中的值，请先复制它：


```
Copied!`1// Copy to a new array
2let arrayCopy = [...myObject.myArrayProperty];
3// Now you can modify the copied array
4arrayCopy.push(newItem);`
```


### [](#link-types)Link types链接类型


[Link types](/docs/foundry/object-link-types/link-types-overview/) between object types are also converted to fields on the TypeScript interface for each object type. To traverse the link, access the field and then call one of the methods used to load the objects. Link type field names are generated using the API Name specified in the ontology.对象类型之间的链接类型也会转换为每个对象类型的 TypeScript 接口上的字段。要遍历链接，访问该字段，然后调用用于加载对象的一种方法。链接类型字段名使用本体中指定的 API 名称生成。


The Foundry Ontology supports defining 1-to-1, 1-to-many, and many-to-many link types. When accessing the `1` side of a link, the generated field is of the `SingleLink` type. You can access the linked object using the `get()` or `getAsync()` methods:Foundry 本体支持定义 1 对 1、1 对多和多对多的链接类型。当访问链接的 1 端时，生成的字段是 SingleLink 类型。你可以使用 get() 或 getAsync() 方法访问链接对象：


```
Copied!`1const manager = employee.manager.get();`
```


As with properties, when you traverse a 1-to-1 or many-to-1 link, the return value may be `undefined` if there is no linked object. Follow the [guide](/docs/foundry/functions/undefined-values/) for handling `undefined` values for these links.与属性类似，当你遍历一个 1 对 1 或多对 1 的链接时，如果没有任何链接的对象，返回值可能是 undefined 。请遵循处理这些链接的 undefined 值的指南。


When accessing the `many` side of a link, the generated field is of the `MultiLink` type. You can access an Array of linked objects using the `all()` or `allAsync()` methods. If there are no linked objects, these methods will return an empty Array.当访问链接的 many 侧时，生成的字段是 MultiLink 类型。你可以使用 all() 或 allAsync() 方法访问链接对象的数组。如果没有链接的对象，这些方法将返回一个空数组。


```
Copied!`1const employees = employee.reports.all();`
```


Traversing links can be expensive because it requires loading which objects are linked in the backend. For details about how to perform link traversals more efficiently, see [this section](/docs/foundry/functions/optimize-performance/#optimizing-link-traversals).遍历链接可能很昂贵，因为它需要加载后端中哪些对象被链接。有关如何更有效地执行链接遍历的详细信息，请查看本节。


The array of linked objects returned from calling `.all()` or `.allAsync()` is a `ReadOnlyArray`. If you want to modify the array, make a copy of it first:从调用 .all() 或 .allAsync() 返回的链接对象数组是一个 ReadOnlyArray 。如果你想修改数组，请先复制它：


```
Copied!`1let copiedEmployees = [...employee.reports.all()];`
```


You can traverse links as an `ObjectSet` to avoid loading linked object instances in the memory. When links are created in the Ontology, APIs will be generated on an object set of this type to "search around" to other linked object sets.你可以通过 ObjectSet 遍历链接，以避免在内存中加载链接的对象实例。当在本体中创建链接时，API 将在该类型的对象集上生成，以"搜索周围"到其他链接的对象集。


```
Copied!`1import { ObjectSet, Employee } from "@foundry/ontology-api";
2
3// Assume you have an object set available:
4// const employee_id = "123";
5// const employeeObjectSet : ObjectSet<Employee> = Objects.search().employee().filter(exactMatch(employee_id));
6
7const linkedObjs: ObjectSet<OtherObjectType> = employeeObjectSet.searchAroundToOtherObjectType();`
```


If you operate on a single instance of an object and search around from there, you will get a `MultiLink<objectType>`. You cannot convert this `MultiLink` to an `ObjectSet`; you must convert the object instance to an object set to pivot to other object sets.如果你对一个对象的单个实例进行操作并从此处搜索，你将得到 MultiLink<objectType> 。你不能将这个 MultiLink 转换为 ObjectSet ；你必须将对象实例转换为对象集，以转换到其他对象集。


```
Copied!`1// Assuming:
2// const employee: Employee
3
4// MultiLink can be loaded in memory to process further.
5
6const linkedObjs: MultiLink<objectType> = employee.reports
7
8// Convert a sole object instance to an object set. This statement will take longer than an `employee().filter()` statement.
9const employeeObjectSet : ObjectSet<Employee> = Objects.search().employee([employee])
10
11// From there, you can use the above "searchAroundToOtherObjectType" to process only object sets.`
```


### [](#ontology-metadata)Ontology metadata本体元数据


Functions provides access to the available Ontology by providing the list of objects and properties. Ontology metadata information is available by accessing the constant types of each object type. See the sections below for more details.函数通过提供对象和属性的列表来访问可用的本体。通过访问每种对象类型的常量类型，可以获取本体元数据信息。更多详情请参见下文。


#### [](#object-property-metadata)Object property metadata对象属性元数据


Object properties also include type metadata, which provides programmatic access to the type of each property. You can use this functionality for advanced workflows like identifying all properties of a given type or validating that a given property name has a specific type.对象属性还包括类型元数据，它提供了对每种属性类型的程序化访问。您可以使用此功能进行高级工作流，例如识别给定类型的所有属性或验证给定属性名是否具有特定类型。


For instance, for an Ontology that contains an employee object **type**, you can access the type information on that object **type's** property as follows:例如，对于一个包含员工对象类型的本体，您可以按以下方式访问该对象类型的属性类型信息：


```
Copied!`1import { Employee } from "@foundry/ontology-api";
2...
3const type = Employee.properties.firstName;`
```


In this case, if `firstName` is a string property on the `Employee` object type, then its type will be a `StringPropertyBaseType`.在这种情况下，如果 firstName 是 Employee 对象类型上的一个字符串属性，那么它的类型将是 StringPropertyBaseType 。


The following property types are available:以下可用的属性类型：


- `BooleanPropertyBaseType`
- `BytePropertyBaseType`
- `DatePropertyBaseType`
- `FloatPropertyBaseType`
- `TimestampPropertyBaseType`
- `ShortPropertyBaseType`
- `GeohashPropertyBaseType` (To be used with `geopoint` properties, previously named `geohash` properties.)GeohashPropertyBaseType （与 geopoint 属性一起使用，以前称为 geohash 属性。）
- `DecimalPropertyBaseType`
- `StringPropertyBaseType`
- `LongPropertyBaseType`
- `IntegerPropertyBaseType`
- `DoublePropertyBaseType`
- `ArrayPropertyBaseType`
- `VectorPropertyBaseType`

