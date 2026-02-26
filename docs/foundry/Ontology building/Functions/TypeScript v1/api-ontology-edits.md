# [](#ontology-edits)Ontology edits本体编辑


In addition to writing functions that return derived values based on the Ontology, you can also write functions that edit the properties and links between objects in the Ontology. This page documents the object edit APIs available to you in functions. For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).除了编写基于本体返回派生值的函数外，您还可以编写编辑本体中对象属性和对象之间链接的函数。本页面记录了您在函数中可用的对象编辑 API。有关编辑函数如何工作的更多详细信息，请参阅概述页面。


To actually be used in an operational context, **Ontology edit functions must be configured as an Action**, known as a [function-backed Action](/docs/foundry/action-types/function-actions-overview/). Configuring an Action in this way allows you to provide additional metadata, configure permissions, and access the Action in various operational interfaces. As noted in the [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied), running an edit function outside of an Action will not actually modify any object data.要在操作环境中实际使用，本体编辑函数必须配置为 Action，称为基于函数的 Action。以这种方式配置 Action 允许您提供额外的元数据、配置权限，并在各种操作界面中访问该 Action。如文档中所述，在 Action 之外运行编辑函数实际上不会修改任何对象数据。


Warning警告Searching for objects after editing them may return unexpected results. See the [Caveats section](/docs/foundry/functions/edits-overview/#edits-and-object-search) for details.编辑对象后搜索可能会返回意外结果。有关详细信息，请参阅注意事项部分。


## [](#declaring-an-edit-function)Declaring an edit function声明编辑函数


Functions that edit the Ontology must:编辑本体（Ontology）的函数必须：


- Be decorated with the `@OntologyEditFunction()` decorator imported from `@foundry/functions-api`使用从 @foundry/functions-api 导入的 @OntologyEditFunction() 装饰器进行装饰
- Be decorated with the `@Edits([object type])` decorator imported from `@foundry/functions-api` to specify the object types that will be edited使用从 @foundry/functions-api 导入的 @Edits([object type]) 装饰器来指定将要编辑的对象类型
- Have an explicit `void` return type明确 void 返回类型


## [](#updating-properties)Updating properties更新属性


You can edit property values by simply reassigning the property value for an object. For example:你可以通过简单地重新赋值对象属性来编辑属性值。例如：


```
Copied!`1employee.lastName = newName;`
```


If you access the `lastName` property value later in the same function execution, the new value that you just set will be returned.如果你在同一个函数执行中稍后访问 lastName 属性值，你刚刚设置的新值将被返回。


[Array properties](/docs/foundry/functions/api-objects-links/#array-properties) on objects are generated with the `ReadOnlyArray` type. To modify an array, create a copy of it, modify the copy, then update the property:对象上的数组属性使用 ReadOnlyArray 类型生成。要修改数组，创建它的副本，修改副本，然后更新属性：


```
Copied!`1// Copy to a new array
2let arrayCopy = [...myObject.myArrayProperty];
3// Now you can modify the copied array
4arrayCopy.push(newItem);
5// Then overwrite the property value
6myObject.myArrayProperty = arrayCopy;`
```


Note that you cannot update the primary key property value of an existing object.请注意，您无法更新现有对象的主键属性值。


## [](#updating-links)Updating links更新链接


The `SingleLink` and `MultiLink` interfaces have various methods you can use to update links:SingleLink 和 MultiLink 接口有各种方法可用于更新链接：


```
Copied!`1// Set an Employee's supervisor
2employee.supervisor.set(newSupervisor);
3
4// Clear an Employee's supervisor
5employee.supervisor.clear();
6
7// Add a new report to the given employee
8employee.reports.add(newReport);
9
10// Remove an old report associated with the given employee
11employee.reports.remove(oldReport);`
```


As with updating properties, accessing links after they have been updated reflects the updates you have made.更新属性时一样，访问更新后的链接反映了你所做的更新。


## [](#creating-objects)Creating objects创建对象


You can create new objects using the `Objects.create()` interface available from `@foundry/ontology-api`. When creating a new object, you have to specify a value for its primary key.你可以使用从 @foundry/ontology-api 可用的 Objects.create() 接口创建新对象。在创建新对象时，你必须为其主键指定一个值。


In this example, we create a new Ticket object with the given ID, set its `dueDate` property, and assign it to the given Employee (by modifying the `assignedTickets` link).在这个例子中，我们创建了一个具有给定 ID 的新 Ticket 对象，设置了它的 dueDate 属性，并将其分配给给定的 Employee（通过修改 assignedTickets 链接）。


```
Copied!`1import { OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Employee, Objects, Tickets } from "@foundry/ontology-api";
3
4export class TicketActionFunctions {
5    @Edits(Employee, Tickets)
6    @OntologyEditFunction()
7    public createNewTicketAndAssignToEmployee(employee: Employee, ticketId: Integer): void {
8        const newTicket = Objects.create().ticket(ticketId);
9
10        newTicket.dueDate = LocalDate.now().plusDays(7);
11
12        employee.assignedTickets.add(newTicket);
13    }
14}`
```


## [](#deleting-objects)Deleting objects删除对象


You can delete an object by calling the `.delete()` method.您可以通过调用 .delete() 方法来删除对象。


In this example, we delete all the tickets assigned to the given employee.在这个例子中，我们删除了分配给指定员工的所有工单。


```
Copied!`1const tickets = employee.tickets.all();
2tickets.forEach(ticket => ticket.delete());`
```


## [](#how-edits-are-captured)How edits are captured编辑的捕获方式


When an Ontology edit function is executed, all updates to objects are captured by the functions infrastructure and returned at the end of the function execution. This includes new object creations via the `Objects.create()` API, all property updates, and object deletions.当执行本体编辑函数时，所有对象更新都会被函数基础设施捕获，并在函数执行结束时返回。这包括通过 Objects.create() API 创建的新对象、所有属性更新以及对象删除。


Edits are collapsed intelligently so that the minimal set of edits are applied in an action. For example, if you create a new object and then update its properties, a single **Create Object** edit will be returned containing the property updates. Similarly, updating multiple properties of an existing object will return a single **Update Object** edit containing all of the property edits. Deleting an object will erase any other property edits that were done before the deletion. The entire function must succeed in order to generate the list of edits which is passed to the actions service executing the atomic transaction.编辑会智能地合并，以便在操作中应用最少的编辑集。例如，如果你创建了一个新对象然后更新其属性，将返回一个包含属性更新的单一创建对象编辑。类似地，更新现有对象的多处属性将返回一个包含所有属性编辑的单一更新对象编辑。删除对象将清除删除前所做的任何其他属性编辑。整个函数必须成功，才能生成传递给执行原子事务的操作服务的编辑列表。


The captured Ontology edits are returned as a list from the function execution, which is why Ontology edit functions must have a return type of `void` or `Promise<void>`. When they are executed, the true return type of the function is a list of Ontology edits, so it is not possible to simultaneously return another value.从函数执行中捕获的 Ontology 编辑以列表形式返回，这就是为什么 Ontology 编辑函数必须具有 void 或 Promise<void> 的返回类型。当它们被执行时，函数的真实返回类型是 Ontology 编辑的列表，因此不可能同时返回其他值。


Edits are captured in a single edit store over the entire lifecycle of a single function execution. This means that it is possible to call into helper functions which create, update, or delete objects, even if those helper functions are not published as Ontology edit functions. For example:编辑在整个函数执行的生命周期中捕获在单个编辑存储中。这意味着即使那些辅助函数没有被发布为本体编辑函数，也可以调用它们来创建、更新或删除对象。例如：


```
Copied!`1export class HelperEditFunctions {
2    @Edits(ObjectA, ObjectB)
3    @OntologyEditFunction()
4    public createAndLink(): void {
5        const objectA = this.createObjectA();
6        const objectB = this.createObjectB();
7        objectA.linkToB.set(objectB);
8    }
9
10    /**
11     * Even though these helper functions are not annotated with @OntologyEditFunction(),
12     * they can create new objects for use in other edit functions.
13     */
14    private createObjectA(): ObjectA {
15        const objectA = Objects.create().objectA(this.generateRandomId());
16        objectA.prop1 = "example";
17        objectA.prop2 = 42;
18        return objectA;
19    }
20
21    private createObjectB(): ObjectB {
22        const objectB = Objects.create().objectB(this.generateRandomId());
23        objectB.prop1 = "another example";
24        return objectB;
25    }
26
27    /* Generate your primary keys as needed. For example,
28    import { Uuid } from "@foundry/functions-utils";
29    private generateRandomId(){
30       return Uuid.random();
31    }
32    */
33}`
```


## [](#retrieving-edited-values)Retrieving edited values获取编辑后的值


When edits are done in a function, the functions infrastructure will return the edited values when you read them. For example, setting a property of an object and then retrieving it will return the new value:当在函数中进行编辑时，函数基础设施在读取时会返回编辑后的值。例如，设置一个对象的属性然后检索它将返回新值：


```
`airplane.departureTime = newDepartureTime;
console.log(airplane.departureTime); // Will log newDepartureTime
`
```


Deleting an object will remove it from search results and prevent access to its properties.删除对象会将其从搜索结果中移除并阻止对其属性的访问。


## [](#the-edits-decorator)The @Edits decorator@Edits 装饰器


Actions may require provenance information to enforce its permissions. To provide actions with this information, you can use the `@Edits` decorator and specify the object types for which your function returns edits.操作可能需要来源信息来执行其权限。为了向操作提供这些信息，你可以使用 @Edits 装饰器并指定你的函数返回编辑的对象类型。


Consider the following when using the `@Edits` decorator:使用 @Edits 装饰器时请注意以下几点：


- When editing properties, the type of the object that was edited should be declared.编辑属性时，应声明所编辑对象的类型。
- When editing one-to-one or one-to-many links, the type of the object with the foreign key property should be declared.编辑一对一或多对一链接时，应声明具有外键属性的对象类型。
- When editing join table links, both the source and target object types should be declared.编辑连接表链接时，应声明源对象和目标对象类型。


Functions perform static analysis of your code to automatically detect referenced object types. However, static analysis *may fail* to properly detect a reference. We strongly recommend that you always use the `@Edits` decorator to provide provenance information about referenced object types.函数对您的代码进行静态分析，以自动检测引用的对象类型。但是，静态分析可能无法正确检测引用。我们强烈建议您始终使用 @Edits 装饰器来提供关于引用对象类型的来源信息。


For the following example, the object types `Employee` and `Aircraft` are edited by a function:对于以下示例，对象类型 Employee 和 Aircraft 由一个函数进行编辑：


```
Copied!`1import { OntologyEditFunction } from "@foundry/functions-api";
2import { Employee, Aircraft, Objects } from "@foundry/ontology-api";
3
4export class MyOntologyEditFunction {
5    @Edits(Aircraft, Employee)
6    @OntologyEditFunction()
7    public myFunction(): void {
8        const x = Objects.search().aircraft().all()[0];
9        x.businessCapacity = 3;
10        const y = Objects.search().employee().all()[0];
11        y.department = "HR";
12    }
13}`
```


If you retrieve (or materialize) a previously edited object through the `Objects.search()` API, the edited value will be returned:如果你通过 Objects.search() API 检索（或实例化）一个之前编辑过的对象，编辑后的值将被返回：


```
Copied!`1import { OntologyEditFunction } from "@foundry/functions-api";
2import { Employee, Objects } from "@foundry/ontology-api";
3
4export class CaveatEditFunctions {
5    @Edits(Employee)
6    @OntologyEditFunction()
7    public async editAndSearch(): Promise<void> {
8        const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
9        employeeOne.name = "Bob";
10
11        // Retrieve the already edited object
12        const employeeOneAgain = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
13        console.log(employeeOneAgain.name); // Prints "Bob"
14    }
15}`
```

