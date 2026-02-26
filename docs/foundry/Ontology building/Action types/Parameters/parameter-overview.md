# [](#parameters)Parameters参数


**Parameters** are the inputs of an action type. They are the interface between the **Rules** and other Foundry applications, such as [Workshop](/docs/foundry/workshop/overview/), [Slate](/docs/foundry/slate/overview/), and [Object Views](/docs/foundry/object-views/overview/). Parameters are treated like variables that contain external values. Each parameter is defined by a type, which dictates what kind of values it can take. Beyond its type, parameters have a variety of other potential configurations. Each parameter can be individually configured as to whether they are exposed in the form or not, or whether they can be changed by the user or not.参数是动作类型的输入。它们是规则与其他 Foundry 应用程序（如 Workshop、Slate 和对象视图 ）之间的接口。参数被视为包含外部值的变量。每个参数由类型定义，该类型决定了它能取的值类型。除了类型外，参数还有多种其他潜在配置。每个参数都可以单独配置，决定是否以表单形式暴露，或者用户是否可以更改。


Parameters transport values across the action type and can be referenced in rules to pass the value back on an object, link, or side effect, in submission criteria, to check if an action can be submitted, to access the current value of an object property before it is changed by the action or in overrides to change the configuration of a following parameter.参数在动作类型间传输值，可以在规则中引用，用于将值传回对象、链接或副作用，在提交条件中引用，检查动作是否可提交，访问对象属性的当前值，或在覆盖中更改后续参数的配置。


Example示例A parameter can take the form of a `Ticket` object type in an action type which allows users to modify the status of a selected ticket. A `Status` parameter is defined as a string. When submitting the action, the object type parameter will take the value of a selected `Ticket` object and the `Status` parameter contains the future status. The action type then passes both parameter values to the rules and executes them to edit the object.参数可以表现为工单对象类型，作为动作类型，允许用户修改所选工单的状态。Status 参数定义为字符串。提交作时，对象类型参数会取选中的工单对象值，Status 参数包含未来状态。动作类型随后将两个参数值传递给规则并执行它们以编辑对象。


Example示例As a variable in Workshop, `previous_status` can take the current value of the `Status` property of the selected `Ticket` object. This can be passed to a hidden parameter in the action, `Previous Status`, and the `Status` parameter can contain the updated status. Upon submitting the action, the action type then passes both the `Previous Stats` and the `Status` values to the rules and executes them to edit the object.作为 Workshop 中的变量，previous_status 可以取选中工单对象 Status 属性的当前值。这可以传递到动作中的隐藏参数“Previous Status”，而 Status 参数可以包含更新后的状态。提交动作后，动作类型会将之前的属性和状态值传递给规则，并执行它们以编辑对象。

