# [](#object-identifiers)Object identifiers对象标识符


The identity of an object in Foundry is represented in a few different ways, and understanding these different representations can be important for writing correct code in functions. This section explains the various ways that objects are identified and the implications for your code.在 Foundry 中，对象的身份以几种不同的方式表示，理解这些不同的表示方式对于在函数中编写正确代码非常重要。本节解释了对象的各种标识方式以及它们对代码的影响。


## [](#types-of-identifiers)Types of identifiers标识符类型


### [](#object-rids)Object RIDs对象 RID


A "RID" refers to a [Resource Identifier ↗](https://github.com/palantir/resource-identifier), Palantir’s open-source specification used to identify an entity. Ontology objects have a RID assigned to them when they are created, either from indexing a backing dataset or as part of an Action.一个"RID"指的是一个资源标识符 ↗，这是 Palantir 的开源规范，用于识别一个实体。本体对象在创建时会被分配一个 RID，这可以来自索引一个支撑数据集，或作为一部分行动。


In functions, every [Ontology object](/docs/foundry/functions/api-objects-links/) has a `rid` field of type `string | undefined`. The reason a RID may be undefined is that it’s possible to create a new object in functions using the [object creation](/docs/foundry/functions/api-ontology-edits/#creating-objects) API. Newly created objects always have a `rid` value of `undefined`, while existing objects always have a defined `rid`.在函数中，每个本体对象都有一个类型为 string | undefined 的 rid 字段。RID 可能未定义的原因是，可以使用对象创建 API 在函数中创建新对象。新创建的对象始终具有 undefined 的 rid 值，而现有对象始终具有定义好的 rid 。


### [](#primary-keys)Primary keys主键


Objects can also be uniquely identified by their object type and primary key. A primary key is a unique `propertyId` and value pair. For example, an Employee object type may be uniquely identified by a `string` property called `employeeId`.对象也可以通过其对象类型和主键来唯一标识。主键是一个唯一的 propertyId 属性和值对。例如，Employee 对象类型可能通过一个称为 employeeId 的 string 属性来唯一标识。


All Ontology objects always have a `typeId` and `primaryKey` field that is present, including newly created objects. This is because you are required to provide the primary key when creating a new object.所有本体对象始终都有一个 typeId 和 primaryKey 字段，包括新创建的对象。这是因为创建新对象时必须提供主键。


## [](#implications-for-code)Implications for code对代码的影响


### [](#checking-for-equality)Checking for equality检查相等性


Within functions, each Ontology object is represented using a [JavaScript object ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object). It’s possible for one Ontology object to be represented as multiple JavaScript objects. For example, this can happen if you load the Ontology object from an [Object search](/docs/foundry/functions/api-object-sets/) multiple times, or load an object from an Object search in addition to having it passed in as a parameter:在函数中，每个本体对象都使用 JavaScript 对象 ↗ 表示。一个本体对象可能被表示为多个 JavaScript 对象。例如，如果多次从对象搜索中加载本体对象，或者除了作为参数传递外还从对象搜索中加载对象，就可能会发生这种情况。


```
Copied!`1public myFunction(employee: Employee): void {
2    const employee2 = Objects.search().employee()
3        .filter(e => e.id.exactMatch(employee.id))
4        .all()[0];
5    console.log(employee == employee2); // false
6    console.log(employee === employee2); // false
7    console.log(employee.id === employee2.id); // true
8}`
```


Even though both `employee` and `employee2` refer to the same conceptual Ontology object in the above example, comparing them using the `==` and `===` operators returns `false` because the variables refer to two distinct JavaScript objects. Simply comparing the `rid` fields can be problematic because newly created objects have a `rid` of `undefined`.尽管在上面的示例中， employee 和 employee2 都指向同一个概念上的本体对象，但使用 == 和 === 运算符比较它们时会返回 false ，因为这两个变量指向的是两个不同的 JavaScript 对象。仅仅比较 rid 字段可能会存在问题，因为新创建的对象具有 rid 的 undefined 值。


As a result, the best way to compare two Ontology objects for equality is to compare the `typeId` and `primaryKey`:因此，比较两个本体对象是否相等的最佳方法是比较 typeId 和 primaryKey ：


```
Copied!`1function isEqual(o1: OntologyObject, o2: OntologyObject) {
2    return o1.typeId === o2.typeId
3        && JSON.stringify(o1.primaryKey) == JSON.stringify(o2.primaryKey);
4}`
```


### [](#object-mappings)Object mappings对象映射


It can often be useful to store a mapping from an object to some value. For example, you may want to iterate through an array of objects and store values for more efficient lookup.通常情况下，将对象映射到某个值会很有用。例如，你可能想要遍历一个对象数组，并存储值以实现更高效的查找。


Because of the equality checking issues described above, you cannot simply use a JavaScript Map to store values for each object. Instead, you can use a [FunctionsMap](/docs/foundry/functions/types-reference/#collection-types) which is specifically designed to support OntologyObjects as keys.由于上述描述的相等性检查问题，你不能简单地使用 JavaScript Map 来存储每个对象的值。相反，你可以使用 FunctionsMap，它专门设计用来支持 OntologyObjects 作为键。

