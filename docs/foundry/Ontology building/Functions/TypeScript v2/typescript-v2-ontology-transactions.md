# [](#ontology-transactions-beta)Ontology transactions [Beta]本体交易 [Beta]


BetaOntology transactions is in the [beta](/docs/foundry/platform-overview/development-life-cycle/) phase of development and may not be available on your enrollment. Functionality may change during active development. Contact Palantir Support to request access.本体交易处于开发测试阶段，可能无法在您的注册服务中提供。在积极开发期间，功能可能会有所变化。请联系 Palantir 支持以请求访问权限。


Ontology transactions provide an additional execution model for functions that edit objects in the Ontology. Unlike edits made via regular [Ontology edit functions](/docs/foundry/functions/typescript-v2-ontology-edits/), transaction functions:本体交易为编辑本体中对象的功能提供了一个额外的执行模型。与通过常规本体编辑功能进行的编辑不同，交易功能：


- Provide a read-after-write guarantee for Ontology edits applied in the function. All edits applied within the function are staged in the transaction and will be reflected in Ontology queries and aggregations later in the function.为函数中应用的本体编辑提供写后读保证。函数内所有编辑都会被暂存到事务中，并在函数后续的本体查询和聚合中反映出来。
- Allow nested calls to other transaction functions making Ontology edits.允许嵌套调用其他进行本体编辑的事务函数。


This page shows how to write transaction functions and documents unique properties. For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).本页面展示了如何编写事务函数并记录独特属性。有关编辑函数工作原理的更多详细信息，请参阅概述页面。


## [](#key-differences-from-regular-ontology-edit-functions)Key differences from regular Ontology edit functions与常规本体编辑函数的关键区别


Transaction-based edit functions differ from regular edit functions in several important ways.基于事务的编辑功能与常规编辑功能在几个重要方面有所不同。


### [](#read-after-write-guarantee)Read-after-write guarantee写入后读取保证


Within a transaction function, any Ontology data read will reflect all edits previously made in the transaction function (and all edits made in a calling transaction function within the same action execution). Such edits are staged only within the transaction and are not visible in queries made by other users or through functions outside the context of the transaction. This allows you to query the Ontology from within the transaction function using search requests and aggregations with all staged edits being reflected in the result of the query.在事务函数中，读取的任何本体数据都将反映事务函数中先前所做的所有编辑（以及在同一操作执行中调用的同一事务函数中进行的所有编辑）。此类编辑仅在事务内部进行，对其他用户或通过事务上下文外的函数进行的查询不可见。这允许您在事务函数内部使用搜索请求和聚合来查询本体，所有已暂存的编辑都将反映在查询结果中。


### [](#no-requirement-to-return-edits-at-the-end-of-the-function)No requirement to return edits at the end of the function函数结束时无需返回编辑


Regular Python and TypeScript V2 Ontology edit functions require returning a batch of Ontology edits as the return value of the function for those edits to be applied. In transaction functions, the Ontology edits are automatically staged in the transaction and will be applied to the Ontology at the end of the function execution when the action completes. This frees up the return value of the function to return other information to the caller.常规 Python 和 TypeScript V2 本体编辑函数需要将一批本体编辑作为函数的返回值，以便这些编辑能够被应用。在事务函数中，本体编辑会自动提交到事务中，并在函数执行结束时，当操作完成时，将这些编辑应用到本体上。这使函数的返回值可以返回其他信息给调用者。


For example, you can apply an action that executes a TypeScript V2 transaction function which then makes some edits and further calls an AIP Logic function. Queries made by the AIP Logic function will return the Ontology changes made in the TypeScript V2 function; any additional edits made by the AIP Logic function will be added to the same transaction without a need to return them as part of the Logic function. All staged edits will be applied automatically once the action completes.例如，你可以应用一个执行 TypeScript V2 事务函数的操作，该函数会进行一些编辑，然后进一步调用 AIP Logic 函数。AIP Logic 函数进行的查询将返回 TypeScript V2 函数中做出的本体变更；AIP Logic 函数做出的任何额外编辑将添加到同一事务中，无需将其作为 Logic 函数的一部分返回。所有提交的编辑将在操作完成时自动应用。


### [](#transactional-execution)Transactional execution事务执行


All operations within the transaction function, including queries, function calls, and AIP Logic executions, run within the same transaction. The transaction is started by the action that executes the function and is committed (that is, the staged Ontology edits are applied to the Ontology) after the function completes successfully. If the function throws an error, no edits are applied and the transaction is rolled back before being retried by the action.交易函数内的所有操作，包括查询、函数调用和 AIP 逻辑执行，都在同一个交易内运行。该交易由执行函数的操作启动，并在函数成功完成后提交（即，将暂存的本体编辑应用到本体上）。如果函数抛出错误，则不会应用任何编辑，并且交易将在操作重新尝试之前回滚。


### [](#writeableclient)WriteableClient可写客户端


Transaction functions use a `WriteableClient` instead of the standard `Client`. The `WriteableClient` provides direct methods for creating, updating, and deleting objects without needing to construct an edit batch.交易函数使用 WriteableClient 而不是标准的 Client 。 WriteableClient 提供了直接创建、更新和删除对象的方法，而无需构建编辑批次。


## [](#define-a-transaction-function)Define a transaction function定义一个交易函数


Transaction functions must explicitly declare the entities that will be edited using the `Edits` type exported from the `@osdk/functions` package. The first parameter must be a `WriteableClient<T>` where `T` is the union of all edit types the function will perform. The return value is no longer constrained to be an array of edits so you can return any value. The following example declares a function that will edit the `Employee` object type:事务函数必须使用从 @osdk/functions 包中导出的 Edits 类型显式声明将要编辑的实体。第一个参数必须是一个 WriteableClient<T> ，其中 T 是函数将执行的所有编辑类型的联合。返回值不再受限于必须是编辑数组的约束，因此你可以返回任何值。以下示例声明了一个将编辑 Employee 对象类型的函数：


```
Copied!`1import { Employee } from "@ontology/sdk";
2import { Edits } from "@osdk/functions";
3import { WriteableClient } from "@osdk/functions/experimental";
4
5type OntologyEdit = Edits.Object<Employee>;
6
7export default async function assignTicket(
8    client: WriteableClient<OntologyEdit>,
9    employeeId: string,
10    ticketId: string
11): Promise<void> {
12    // ...
13}`
```


## [](#create-objects)Create objects创建对象


Use the `create` method on the `WriteableClient` to create new objects. You must specify the object type and provide a value for the primary key, along with any other properties you want to initialize.在 WriteableClient 上使用 create 方法来创建新对象。你必须指定对象类型，并为主键提供值，以及任何你想要初始化的其他属性。


```
Copied!`1import { Employee } from "@ontology/sdk";
2import { Edits } from "@osdk/functions";
3import { WriteableClient } from "@osdk/functions/experimental";
4
5type OntologyEdit = Edits.Object<Employee>;
6
7async function createEmployee(
8    client: WriteableClient<OntologyEdit>,
9    employeeId: string,
10    firstName: string,
11    lastName: string
12): Promise<Integer> {
13    await client.create(Employee, {
14        employeeId: employeeId,
15        firstName: firstName,
16        lastName: lastName
17    });
18
19    return employeeId;
20}
21
22export default createEmployee;`
```


### [](#creating-with-generated-ids)Creating with generated IDs使用生成的 ID 创建


When you need to generate an ID and then use it immediately:当你需要生成一个 ID 并立即使用它时：


```
Copied!`1import { Ticket } from "@ontology/sdk";
2import { Edits, Integer } from "@osdk/functions";
3import { WriteableClient } from "@osdk/functions/experimental";
4import { randomUUID } from "crypto";
5
6type OntologyEdit = Edits.Object<Ticket>;
7
8async function createTicket(
9    client: WriteableClient<OntologyEdit>,
10    title: string
11): Promise<string> {
12    const ticketId = randomUUID();
13
14    await client.create(Ticket, {
15        ticketId: ticketId,
16        title: title,
17        status: "open"
18    });
19
20    return ticketId;
21}
22
23export default createTicket;`
```


## [](#update-objects)Update objects更新对象


### [](#object-properties)Object properties对象属性


Use the `update` method on the `WriteableClient` to modify object properties:在 WriteableClient 上使用 update 方法来修改对象属性：


```
Copied!`1await client.update(employee, { lastName: newName });`
```


You can also update an object by referencing its API name and primary key:您也可以通过引用对象的 API 名称和主键来更新对象：


```
Copied!`1await client.update({ $apiName: "Employee", $primaryKey: 23 }, { lastName: newName });`
```


### [](#interface-properties)Interface properties接口属性


You can use the `update` method to modify interface properties of an object through an Ontology interface:您可以使用 update 方法通过本体接口来修改对象的接口属性


```
Copied!`1await client.update(person, { firstName: newFirstName });`
```


Note that an interface property that is implemented by the primary key property of the underlying object cannot be updated.请注意，由底层对象的主键属性实现的接口属性不能被更新。


## [](#delete-objects)Delete objects删除对象


You can delete an object by calling the `delete` method on the `WriteableClient`:您可以通过在 WriteableClient 上调用 delete 方法来删除对象：


```
Copied!`1await client.delete(ticket);`
```


Objects may also be deleted using a primary key instead of an instance:对象也可以使用主键而不是实例来删除：


```
Copied!`1await client.delete({ $apiName: "Ticket", $primaryKey: 12 });`
```


## [](#create-or-delete-links)Create or delete links创建或删除链接


Use the `link` and `unlink` methods on the `WriteableClient` to add or remove many to many links between objects:在 WriteableClient 上使用 link 和 unlink 方法来添加或删除对象之间的多对多链接：


```
Copied!`1// Assign a ticket to an employee
2await client.link(employee, "assignedTickets", ticket);
3
4// Unassign a ticket from an employee
5await client.unlink(employee, "assignedTickets", ticket);`
```


You can also reference either side of the link with an API name and primary key:您也可以使用 API 名称和主键来引用链接的任一侧：


```
Copied!`1await client.link(
2    { $apiName: "Employee", $primaryKey: 23 },
3    "assignedTickets",
4    { $apiName: "Ticket", $primaryKey: 12 }
5);`
```


To edit one to many links, edit the foreign key property using a create or update object edit.要编辑一对多链接，请使用创建或更新对象编辑来编辑外键属性。


## [](#read-after-write-within-transactions)Read-after-write within transactions事务内的写后读


One of the key advantages of transaction functions is the ability to read data that was just written in the same transaction. This is useful for implementing workflows that require immediate consistency.事务函数的一个主要优势是能够读取在同一事务中刚刚写入的数据。这对于实现需要立即一致性的工作流程很有用。


```
Copied!`1import { Employee, Ticket } from "@ontology/sdk";
2import { Edits, Integer } from "@osdk/functions";
3import { WriteableClient } from "@osdk/functions/experimental";
4import { randomUUID } from "crypto";
5
6type OntologyEdit = Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;
7
8async function assignTicketAndCheckWorkload(
9    client: WriteableClient<OntologyEdit>,
10    employeeId: Integer,
11    title: string
12): Promise<{ ticketId: string, totalAssignedTickets: number }> {
13    const ticketId = randomUUID();
14
15    // Create the ticket
16    await client.create(Ticket, {
17        ticketId: ticketId,
18        title: title,
19        status: "open"
20    });
21
22    // Assign the ticket to the employee
23    await client.link(
24        { $apiName: "Employee", $primaryKey: employeeId },
25        "assignedTickets",
26        { $apiName: "Ticket", $primaryKey: ticketId }
27    );
28
29    // Query the employee's total workload including the newly assigned ticket
30    // This works because of the read-after-write guarantee
31    const result = await client.aggregate(Ticket, (tickets) =>
32        tickets
33            .where(ticket => ticket.assignedTo.employeeId.exactMatch(employeeId))
34            .where(ticket => ticket.status.exactMatch("open"))
35            .count()
36    );
37
38    return {
39        ticketId: ticketId,
40        totalAssignedTickets: result
41    };
42}
43
44export default assignTicketAndCheckWorkload;`
```


## [](#executing-functions-within-transactions)Executing functions within transactions在事务内执行函数


When you execute other functions or queries inside a transaction function, those operations run within the same transaction. This means any reads to the ontology will reflect changes made to the transaction prior. This applies to:当你在事务函数内部执行其他函数或查询时，这些操作将在同一个事务内运行。这意味着对本体论的任何读取都将反映事务之前的更改。这适用于：


- Other TypeScript functions其他 TypeScript 函数
- AIP Logic functionsAIP 逻辑函数
- Ontology queries本体查询


Any edits made by nested function calls are also part of the same transaction and will be committed or rolled back together.由嵌套函数调用所做的任何编辑也是同一事务的一部分，并将一起提交或回滚。


```
Copied!`1import { Employee, Ticket } from "@ontology/sdk";
2import { Edits, Integer } from "@osdk/functions";
3import { WriteableClient } from "@osdk/functions/experimental";
4
5type OntologyEdit = Edits.Object<Ticket> | Edits.Link<Employee, "assignedTickets">;
6
7async function bulkAssignTickets(
8    client: WriteableClient<OntologyEdit>,
9    employeeId: Integer,
10    ticketIds: string[]
11): Promise<Integer> {
12    let assignedCount = 0;
13
14    for (const ticketId of ticketIds) {
15        // Each link operation is part of the same transaction
16        await client.link(
17            { $apiName: "Employee", $primaryKey: employeeId },
18            "assignedTickets",
19            { $apiName: "Ticket", $primaryKey: ticketId }
20        );
21
22        // Update ticket status
23        await client.update(
24            { $apiName: "Ticket", $primaryKey: ticketId },
25            { status: "assigned" }
26        );
27
28        assignedCount++;
29    }
30
31    // All edits will be committed together when the function completes
32    return assignedCount;
33}
34
35export default bulkAssignTickets;`
```


## [](#transaction-lifecycle)Transaction lifecycle事务生命周期


Understanding when transactions start and commit is important for building reliable functions:理解事务何时开始和提交对于构建可靠的函数非常重要：


1. **Transaction start:** The transaction begins when the action executes the function.事务开始：当操作执行函数时，事务开始。
2. **Function execution:** All operations (creates, updates, deletes, reads, nested function calls) occur within the transaction.函数执行：所有操作（创建、更新、删除、读取、嵌套函数调用）都在事务内发生。
3. **Transaction commit:** If the function completes successfully, the transaction is committed before the action finishes.事务提交：如果函数成功完成，事务在操作结束前提交。
4. **Rollback on error:** If the function throws an error, the transaction is rolled back and no edits are applied. The function is retried by the action.出错回滚：如果函数抛出错误，事务将被回滚且不会应用任何编辑。该操作将重试该函数。


```
Copied!`1import { Employee } from "@ontology/sdk";
2import { Edits, Integer } from "@osdk/functions";
3import { WriteableClient } from "@osdk/functions/experimental";
4
5async function updateEmployeeWithValidation(
6    client: WriteableClient<Edits.Object<Employee>>,
7    employeeId: Integer,
8    newSalary: number
9): Promise<void> {
10    // Validate input
11    if (newSalary < 0) {
12        // Transaction will be rolled back
13        throw new Error("Salary cannot be negative");
14    }
15
16    // Update the employee
17    await client.update(
18        { $apiName: "Employee", $primaryKey: employeeId },
19        { salary: newSalary }
20    );
21
22    // If we reach here, the transaction will be committed
23}
24
25export default updateEmployeeWithValidation;`
```

