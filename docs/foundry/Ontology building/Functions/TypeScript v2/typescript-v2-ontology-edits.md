# [](#ontology-edits)Ontology edits本体编辑


In addition to writing functions that read data from the Ontology, you can also write functions that create objects and edit the properties and links between objects.
This page documents the object edit APIs available to you in functions.
For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).除了编写从本体中读取数据的函数外，您还可以编写创建对象以及编辑对象属性和对象间链接的函数。本页面记录了您在函数中可用的对象编辑 API。有关编辑函数如何工作的更多详细信息，请参阅概述页面。


For the edits created in a function to actually be applied, Ontology edit functions *must be configured as a [function-backed Action](/docs/foundry/action-types/function-actions-overview/)*.
Configuring an Action in this way allows you to provide additional metadata, configure permissions, and access the Action in various operational interfaces.
As noted in the [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied), running an edit function outside of an Action will not actually modify any object data.为了让函数中创建的编辑实际生效，本体编辑函数必须配置为基于函数的操作。以这种方式配置操作允许您提供额外的元数据、配置权限，并在各种操作界面中访问该操作。如文档中所述，在操作之外运行编辑函数实际上不会修改任何对象数据。


Warning警告Searching for objects immediately after editing them may return unexpected results. See the [Caveats section](/docs/foundry/functions/edits-overview/#edits-and-object-search) for details.编辑对象后立即搜索可能会返回意外结果。有关详细信息，请参阅注意事项部分。


## [](#define-an-edit-function)Define an edit function定义编辑函数


Functions that edit the Ontology must explicitly declare the entities that will be edited using the `Edits` type exported from the `@osdk/functions` package. The following example declares a new type representing edits to the `Employee` and `Ticket` object types, as well as a link type between `Employee` and `Ticket`. Edits to multiple entities need to be joined with the `|` operator.编辑本体（Ontology）的函数必须使用从 @osdk/functions 包中导出的 Edits 类型明确声明将要编辑的实体。以下示例声明了一个新类型，该类型表示对 Employee 和 Ticket 对象类型的编辑，以及 Employee 和 Ticket 之间的链接类型。对多个实体的编辑需要使用 | 运算符进行连接。


```
Copied!`1import { Employee, Ticket } from "@ontology/sdk";
2import { Edits } from "@osdk/functions";
3
4type OntologyEdit = Edits.Object<Employee> | Edits.Interface<Person> | Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;`
```


You must then declare that the function returns an array of edits of the new type.然后你必须声明该函数返回一个由新类型编辑组成的数组。


```
Copied!`1export default function createNewTicketAndAssignToEmployee(): OntologyEdit[] {
2    // ...
3}`
```


## [](#construct-an-ontology-edits-batch)Construct an Ontology edits batch构建本体编辑批处理


To perform Ontology edits in a TypeScript v2 function, first construct an Ontology edits batch using the `createEditBatch` function exported from `@osdk/functions`, passing the previously declared type as a type argument:要在 TypeScript v2 函数中执行本体编辑，首先使用从 @osdk/functions 导出的 createEditBatch 函数构建一个本体编辑批处理，将先前声明的类型作为类型参数传递：


```
Copied!`1import { Employee, Ticket } from "@ontology/sdk";
2import { Client } from "@osdk/client";
3import { createEditBatch, Edits } from "@osdk/functions";
4
5type OntologyEdit = Edits.Object<Employee> | Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;
6
7export default function createNewTicketAndAssignToEmployee(client: Client): OntologyEdit[] {
8
9    const batch = createEditBatch<OntologyEdit>(client);
10    // ...
11}`
```


This batch is used to keep track of all edits made in a function.此批处理用于跟踪函数中进行的所有编辑。


## [](#update-properties)Update properties更新属性


### [](#object-properties)Object properties对象属性


Use the `update` method available on the created batch to modify one or more object properties:使用创建的批次上的 update 方法来修改一个或多个对象属性：


```
Copied!`1batch.update(employee, { lastName: newName });`
```


If you have not loaded the `employee` object instance into memory, you can also update it by referencing the object's API name and primary key:如果你还没有将 employee 对象实例加载到内存中，也可以通过引用对象 API 名称和主键来更新它：


```
Copied!`1batch.update({ $apiName: "Employee", $primaryKey: 23 }, { lastName: newName });`
```


Subsequent access to the `lastName` property value of `employee` later in the same function execution will *not* reflect the changes that you make when calling `update` on the edit batch.在同一个函数执行过程中，后续对 lastName 属性值的访问不会反映你在调用 update 时对编辑批次所做的更改。


Sometimes, it is useful to copy all of the property values of one instance of an object type to another instance. The following example assigns the property values of `employee2` to `employee1`:有时，将一个对象类型的实例的所有属性值复制到另一个实例中很有用。以下示例将 employee2 的属性值赋给 employee1 ：


```
Copied!`1batch.update(employee1, employee2);`
```


Note that the primary key property value of an existing object cannot be updated.请注意，现有对象的主键属性值不能被更新。


### [](#interface-properties)Interface properties接口属性


You can use the `update` method to modify the interface properties of an object through an Ontology interface. In the example below, the type of `person` is an Ontology interface, but the underlying instance is an object that implements the `Person` interface.您可以使用 update 方法通过本体接口修改对象的接口属性。在下面的示例中， person 的类型是一个本体接口，但底层的实例是一个实现了 Person 接口的对象。


The `update` method takes two arguments both for object types and interfaces. For interfaces, it takes the interface that will be modified and the interface properties to be modified.update 方法接受两个参数，既适用于对象类型也适用于接口。对于接口，它接受将要被修改的接口以及要被修改的接口属性。


```
Copied!`1batch.update(person, { firstName: newFirstName });`
```


Note that an interface property that is implemented by the primary key property of the underlying object cannot be updated.请注意，由底层对象的主键属性实现的接口属性不能被更新。


## [](#update-links)Update links更新链接


For many-to-many links, the `link` and `unlink` methods are available on the created batch to add or remove links between objects.对于多对多链接，创建的批处理上可以使用 link 和 unlink 方法来添加或删除对象之间的链接。


```
Copied!`1// Assign an employee to an office.
2batch.link(employee, "office", office);
3
4// Unassign an office from an employee.
5batch.unlink(employee, "office", office);`
```


For one-to-one and one-to-many links, use the `update` method available on the created batch to modify the foreign key property of the source object. The example below illustrates a one-to-many link. An employee can have multiple tickets, but each ticket can only have one employee.对于一对一和多对一链接，使用创建的批处理上的 update 方法来修改源对象的外键属性。下面的示例说明了一个多对一链接。一个员工可以有多个工单，但每个工单只能有一个员工。


```
Copied!`1// Assign a ticket to an employee.
2batch.update({ $apiName: "Ticket", $primaryKey: 13 }, { assignedEmployeeId: 52 });
3
4// Unassign a ticket.
5batch.update({ $apiName: "Ticket", $primaryKey: 13 }, { assignedEmployeeId: undefined });`
```


As with updating properties, you can also reference either side of the link with an API name and primary key if you have not loaded a concrete instance of the object type previously.与更新属性类似，如果你之前没有加载过该对象类型的具体实例，也可以使用 API 名称和主键来引用链接的任一侧。


```
Copied!`1// Assign a ticket to an employee.
2batch.link({ $apiName: "Employee", $primaryKey: 23 }, "assignedTickets", { $apiName: "Ticket", $primaryKey: 12 });
3
4// Unassign a ticket from an employee.
5batch.unlink({ $apiName: "Employee", $primaryKey: 23 }, "assignedTickets", { $apiName: "Ticket", $primaryKey: 12 });`
```


## [](#create-objects)Create objects创建对象


### [](#objects)Objects对象


You can create new objects using the `create` method on the edit batch. When creating a new object, you must specify a value for its primary key and can optionally initialize any other properties.您可以使用编辑批次的 create 方法创建新对象。在创建新对象时，您必须为其主键指定一个值，并可以选择初始化任何其他属性。


In this example, we create a new `Ticket` object with the given ID, set its `dueDate` property, and assign it to the given `Employee` by modifying the `assignedTickets` link. To simplify the calculation of the new value of `dueDate`, we use the `luxon` library.在这个例子中，我们使用给定的 ID 创建了一个新的 Ticket 对象，设置了它的 dueDate 属性，并通过修改 assignedTickets 链接将其分配给给定的 Employee 。为了简化 dueDate 新值的计算，我们使用了 luxon 库。


```
Copied!`1import { Employee, Ticket } from "@ontology/sdk";
2import { Client, Osdk } from "@osdk/client";
3import { createEditBatch, Edits, Integer } from "@osdk/functions";
4import { DateTime } from "luxon";
5
6type OntologyEdit = Edits.Object<Employee> | Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;
7
8export default function createNewTicketAndAssignToEmployee(
9    client: Client,
10    employee: Osdk.Instance<Employee>,
11    ticketId: Integer,
12): OntologyEdit[] {
13    const batch = createEditBatch<OntologyEdit>(client);
14
15    batch.create(Ticket, {
16        ticketId,
17        dueDate: DateTime.now().plus({ days: 7 }).toFormat('yyyy-MM-dd'),
18    });
19
20    // The new ticket does not exist in the Ontology as a concrete instance, but we can link it
21    // by referencing its API name and primary key.
22    batch.link(employee, "assignedTickets", { $apiName: "Ticket", $primaryKey: ticketId });
23
24    return batch.getEdits();
25}`
```


### [](#interfaces)Interfaces接口


You can create new object instances through interfaces by calling the `create` method and specifying an interface, underlying object type, and a set of interface properties. One of the interface properties supplied must be implemented by the primary key property of the underlying object type.您可以通过调用 create 方法并指定接口、底层对象类型以及一组接口属性来创建新的对象实例。所提供的接口属性中必须有一个是由底层对象类型的 primary key 属性实现的。


```
Copied!`1editBatch.create(Person, {
2    $objectType: "Employee",
3    firstName: "John",
4    lastName: "Doe",
5});`
```


## [](#delete-objects)Delete objects删除对象


### [](#objects-1)Objects对象


You can delete an object by calling the `delete` method on the edit batch.您可以通过在编辑批次上调用 delete 方法来删除对象。


In this example, we delete all the tickets assigned to the given employee:在这个例子中，我们删除分配给给定员工的全部工单：


```
Copied!`1for await (const ticket of employee.$link.assignedTickets.asyncIter()) {
2    batch.delete(ticket);
3}`
```


Objects may also be deleted using a primary key instead of an instance:对象也可以使用主键而不是实例来删除：


```
Copied!`1batch.delete({ $apiName: "Ticket", $primaryKey: 12 });`
```


### [](#interfaces-1)Interfaces接口


You can delete an object through an interface by calling the `delete` method.你可以通过调用 delete 方法通过接口删除对象。


```
Copied!`1batch.delete(person);`
```


## [](#edits-on-struct-properties)Edits on struct properties结构属性编辑


Ontology struct properties for both object and interface types can be edited with TypeScript v2 functions. [Struct types](/docs/foundry/functions/types-reference/#structcustom-type) in TypeScript v2 are defined using TypeScript interfaces.  Struct types in functions can be used to edit Ontology struct properties, as long as they contain the same fields as the struct property, with field names matching the API names of the Ontology struct property fields.对象和接口类型的本体结构属性都可以使用 TypeScript v2 函数进行编辑。TypeScript v2 中的结构类型使用 TypeScript 接口定义。函数中的结构类型可以用来编辑本体结构属性，只要它们包含与结构属性相同的字段，并且字段名与本体结构属性字段的 API 名称匹配。


```
Copied!`1interface Address {
2    street: string,
3    city: string,
4    state: string,
5    country: string,
6    zipcode: string,
7}
8
9export default function updateEmployeeAddress(
10    client: Client,
11    employee: Osdk.Instance<Employee>,
12    newAddress: Address
13): OntologyEdit[] {
14    const batch = createEditBatch<OntologyEdit>(client);
15    batch.update(employee, { address: newAddress });
16    return batch.getEdits();
17}`
```

