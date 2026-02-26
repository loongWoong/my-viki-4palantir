# [](#function-backed-actions)Function-backed actions基于函数的操作


In an action type, [rules](/docs/foundry/action-types/rules/) define the ways objects should change when the action is applied. Many action types can be defined using simple rules which allow you to create, modify, and delete objects, or create and delete links between objects.在一个操作类型中，规则定义了当操作被应用时对象应该如何变化。许多操作类型可以使用简单的规则来定义，这些规则允许你创建、修改和删除对象，或在对象之间创建和删除链接。


In some cases, however, simple rules are not sufficient to describe the changes that you want to make. For example, you may want to:然而，在某些情况下，简单的规则不足以描述你想要进行的更改。例如，你可能想要：


- Modify multiple objects that are currently linked together. For example, you may want to set the `status` field of an `Incident` object to `Closed`, and also set the `status` of all linked `Alert` objects to `Resolved`.修改当前链接在一起的多個对象。例如，你可能想要将 status 对象的 Incident 字段设置为 Closed ，同时将所有链接的 Alert 对象的 status 设置为 Resolved 。
- Modify an object's properties based on some more complex logic. For example, you may want to compute a value based on some business logic that reads data from several objects, then write that value into an object property.根据更复杂的逻辑修改对象的属性。例如，您可能需要根据某些业务逻辑计算一个值，该逻辑从多个对象中读取数据，然后将该值写入对象的属性。
- Create several different types of objects and set up links between them.创建多种不同类型的对象，并在它们之间建立链接。


To support use cases like these, action types can be configured to call a [function](/docs/foundry/functions/overview/) that defines the logic of how objects should be modified. These action types are often referred to as **function-backed actions**. By using a function, you can create action types of any level of complexity, reading any number of objects and modifying objects as you see fit.为了支持这些用例，可以配置动作类型来调用一个定义对象应如何修改逻辑的函数。这些动作类型通常被称为函数支持动作。通过使用函数，您可以创建任何复杂程度的动作类型，读取任意数量的对象，并根据需要修改对象。


Although function-backed action types are very flexible, you should note that they are subject to both [action type limits](/docs/foundry/action-types/scale-property-limits/) and [function execution limits](/docs/foundry/functions/manage-functions/#enforced-limits).尽管函数支持动作类型非常灵活，但请注意它们既受动作类型限制的限制，也受函数执行限制的限制。


Get started with function-backed actions by following the [tutorial](/docs/foundry/action-types/function-actions-getting-started/).通过遵循教程来开始使用基于函数的操作。

