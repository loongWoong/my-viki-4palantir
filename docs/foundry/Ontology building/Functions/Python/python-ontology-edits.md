# [](#ontology-edits)Ontology edits本体编辑


In addition to writing functions that read data from the Ontology, you can also write functions that create objects and edit the properties and links between objects.
This page documents the object edit APIs available to you in functions.
For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).除了编写从本体中读取数据的函数外，您还可以编写创建对象以及编辑对象属性和对象间链接的函数。本页面记录了您在函数中可用的对象编辑 API。有关编辑函数如何工作的更多详细信息，请参阅概述页面。


For the edits created in a function to actually be applied, Ontology edit functions *must be configured as a [function-backed Action](/docs/foundry/action-types/function-actions-overview/)*.
Configuring an Action in this way allows you to provide additional metadata, configure permissions, and access the Action in various operational interfaces.
As noted in the [documentation](/docs/foundry/functions/edits-overview/#when-edits-are-applied), running an edit function outside of an Action will not actually modify any object data.为了让函数中创建的编辑实际生效，本体编辑函数必须配置为基于函数的操作。以这种方式配置操作允许您提供额外的元数据、配置权限，并在各种操作界面中访问该操作。如文档中所述，在操作之外运行编辑函数实际上不会修改任何对象数据。


Warning警告Searching for objects immediately after editing them may return unexpected results. See the [Caveats section](/docs/foundry/functions/edits-overview/#edits-and-object-search) for details.编辑对象后立即搜索可能会返回意外结果。有关详细信息，请参阅注意事项部分。


## [](#define-an-edit-function)Define an edit function定义一个编辑函数


Functions that edit the Ontology must:编辑本体（Ontology）的函数必须：


- Be decorated with the `@function(edits=[MyObjectType])` decorator imported from `functions.api` to specify the object types that will be edited.使用从 functions.api 导入的 @function(edits=[MyObjectType]) 装饰器来指定将要编辑的对象类型。
- Have an explicit `list[OntologyEdit]` return type hint imported from `functions.api`.具有从 functions.api 导入的明确的 list[OntologyEdit] 返回类型提示。


## [](#construct-an-ontology-edits-container)Construct an Ontology edits container构建一个本体编辑容器


To perform Ontology edits in a Python function, first construct an Ontology edits container from the [OSDK client](/docs/foundry/functions/python-functions-on-objects/). For example:在 Python 函数中执行本体编辑，首先需要从 OSDK 客户端构建一个本体编辑容器。例如：


```
Copied!`1ontology_edits = FoundryClient().ontology.edits()`
```


This container is used to keep track of all edits made in a function.该容器用于跟踪函数中所有已进行的编辑。


## [](#update-properties)Update properties更新属性


Ontology objects in Python functions are read-only by default. Attempts to modify their properties will raise an exception.Python 函数中的本体对象默认为只读。尝试修改其属性将引发异常。


In order to edit an object, first obtain an editable view of that object using an Ontology edits container, either from an existing object instance:为了编辑一个对象，首先需要使用本体编辑容器获取该对象的可编辑视图，可以从现有的对象实例获取：


```
Copied!`1editable_object = ontology_edits.objects.MyObjectType.edit(my_object)`
```


or given an object primary key:或者给定对象的主键：


```
Copied!`1editable_object = ontology_edits.objects.MyObjectType.edit(object_primary_key)`
```


Once you have an editable object, you can edit property values by reassigning the property value for an object. For example:一旦你获取了可编辑的对象，可以通过重新分配对象属性值来编辑属性值。例如：


```
Copied!`1editable_employee.last_name = new_name`
```


Subsequent access to the `last_name` property value of `editable_employee` later in the same function execution will yield the new value that was just set. However, the original non-editable object will *not* reflect the changes.在同一个函数执行过程中后续访问 last_name 的 editable_employee 属性值将得到刚刚设置的新值。然而，原始的非可编辑对象不会反映这些变化。


[Array properties](/docs/foundry/functions/api-objects-links/#array-properties) on editable objects are read-only. To modify an array, create a copy of it, modify the copy, then update the property:可编辑对象上的数组属性是只读的。要修改数组，创建它的副本，修改副本，然后更新属性：


```
Copied!`1# Copy to a new array
2array_copy = list(editable_object.my_array_property)
3# Now you can modify the copied array
4array_copy.append(new_item)
5# Then overwrite the property value
6editable_object.my_array_property = array_copy`
```


Note that the primary key property value of an existing object cannot be updated.请注意，现有对象的主键属性值不能被更新。


## [](#update-links)Update links更新链接


Single-link and multi-link properties have various methods for updating links:单链接和多链接属性有多种更新链接的方法：


```
Copied!`1# Set an Employee's supervisor
2editable_employee.supervisor.set(new_supervisor)
3
4# Clear an Employee's supervisor
5editable_employee.supervisor.clear()
6
7# Add a new report to the given employee
8editable_employee.reports.add(new_report)
9
10# Remove an old report associated with the given employee
11editable_employee.reports.remove(new_report)`
```


As with updating properties, accessing links of `editable_employee` after they have been updated will reflect the updates you have made.与更新属性类似，在 editable_employee 更新后访问其链接将反映您所做的更新。


## [](#create-objects)Create objects创建对象


You can create new objects using the `MyObjectType.create()` method on the Ontology edits container. When creating a new object, you must specify a value for its primary key.您可以使用本体编辑容器上的 MyObjectType.create() 方法创建新对象。在创建新对象时，必须为其主键指定一个值。


In this example, we create a new Ticket object with the given ID, set its `due_date` property, and assign it to the given Employee by modifying the `assigned_tickets` link.在这个示例中，我们创建了一个具有给定 ID 的新 Ticket 对象，设置了其 due_date 属性，并通过修改 assigned_tickets 链接将其分配给给定的员工。


```
Copied!`1from datetime import datetime, timedelta
2
3from functions.api import function, Integer, Array, OntologyEdit
4from ontology_sdk import FoundryClient
5from ontology_sdk.ontology.objects import Employee, Ticket
6
7@function(edits=[Employee, Ticket])
8def create_new_ticket_and_assign_to_employee(
9    employee: Employee,
10    ticket_id: Integer
11) -> list[OntologyEdit]:
12    ontology_edits = FoundryClient().ontology.edits()
13
14    new_ticket = ontology_edits.objects.Ticket.create(ticket_id)
15    new_ticket.due_date = datetime.now() + timedelta(days=7)
16
17    editable_employee = ontology_edits.objects.Employee.edit(employee)
18    editable_employee.assigned_tickets.add(new_ticket)
19
20    return ontology_edits.get_edits()`
```


Property values may also be passed directly to the create method in addition to the primary key. For example:属性值也可以直接传递给创建方法，除了主键。例如：


```
Copied!`1new_due_date = datetime.now() + timedelta(days=7)
2new_ticket = ontology_edits.objects.Ticket.create(ticket_id, due_date=new_due_date)`
```


## [](#delete-objects)Delete objects删除对象


You can delete an object by calling the `MyObjectType.delete()` method on the Ontology edits container.您可以通过在本体编辑容器上调用 MyObjectType.delete() 方法来删除对象。


In this example, we delete all the tickets assigned to the given employee:在这个例子中，我们删除分配给给定员工的全部工单：


```
Copied!`1for ticket in employee.tickets:
2    ontology_edits.objects.Ticket.delete(ticket)`
```


Objects may also be deleted using a primary key instead of an instance:对象也可以使用主键而不是实例来删除：


```
Copied!`1ontology_edits.objects.Ticket.delete(ticket_id)`
```

