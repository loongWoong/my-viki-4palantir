# [](#rules)Rules规则


**Rules** define the logic of the action type that transform the parameters into Ontology edits or other effects. There are two main types of rules: ones that edit the Ontology, and ones that trigger another effect in Foundry.规则定义了将参数转换为本体编辑或其他效果的动作类型的逻辑。规则主要有两种：一种是编辑本体论的，另一种是触发 Foundry 中其他效果的。


## [](#ontology-rules)Ontology rules本体规则


An Ontology rule changes specific elements of the Ontology. They can create, modify, or delete objects and links of existing types. To create or delete one-to-many or one-to-one links, object rules need to be used and the foreign key property on the object needs to be modified.本体规则会改变本体论中的具体元素。它们可以创建、修改或删除现有类型的对象和链接。要创建或删除一对多或一对一链接，需要使用对象规则，并且需要修改对象上的外键属性。


1. **Create object:** Can be used to create an object of a predefined type. The primary key of the object type is a required property which has to be filled. Additional properties can be added optionally.创建对象： 可以用来创建预定义类型的对象。对象类型的主键是一个必须填充的属性。额外的属性也可以选择添加。
2. **Modify object(s):** Can be used to modify an existing object whose primary key is derived from object reference parameters. This cannot reference an object created as a part of the current action.修改对象： 可以用来修改主键源自对象引用参数的现有对象。这不能引用作为当前动作一部分创建的对象。
3. **Create or modify object(s):** Can be used to modify an existing object based on an object reference parameter. If an object is not selected, a new object will be created with either an automatically generated unique ID, or with a user submitted primary key.创建或修改对象： 可以用来根据对象引用参数修改现有对象。如果未选择某个对象，将创建一个新对象，带有自动生成的唯一 ID，或使用用户提交的主键。
4. **Delete object(s):** Can be used to delete an existing object whose primary key is derived from object reference parameters. This cannot reference an object created as a part of the current action.删除对象： 可以用来删除主键来源于对象引用参数的现有对象。这不能引用作为当前动作一部分创建的对象。
5. **Create link(s):** Can be used to create a many-to-many link between objects that are passed via object reference parameters. For foreign key links, one has to use **Modify object** rule to explicitly modify the foreign key property.创建链接： 可用于通过对象引用参数传递的对象之间创建多对多的链接。对于外键链接，必须使用修改对象规则来显式修改外键属性。
6. **Delete link:** Can be used to delete a many-to-many link between objects that are passed via object reference parameters. For foreign key links, one has to use **Modify object** rule to explicitly modify the foreign key property.删除链接： 可用于删除通过对象引用参数传递的对象之间的多对多链接。对于外键链接，必须使用修改对象规则来显式修改外键属性。
7. **Function rule:** Can be used to reference an Ontology edit function whose inputs are derived from parameters of the action. When this rule is present, no other rule may be configured since function code alone is capable of handling everything that other rules can do. Read more about [function action types](/docs/foundry/action-types/function-actions-overview/).函数规则： 可以用来引用本体编辑函数，其输入源自动作的参数。当该规则存在时，就无法配置其他规则，因为函数代码本身就能处理其他规则能做的所有事情。阅读更多关于函数动作类型的内容 。
8. **Create object(s) of interface:** Can be used to create objects of any type that implements a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).创建接口对象： 可用于创建任何实现特定接口的对象。阅读更多关于接口作的信息 。
9. **Modify object(s) of interface:** Can be used to modify objects of types that implement a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).修改接口对象： 可以用来修改实现特定接口的类型对象。阅读更多关于接口作的信息 。
10. **Delete object(s) of interface:** Can be used to delete objects of types that implement a particular interface. Read more about [actions on interfaces](/docs/foundry/action-types/actions-on-interfaces/).删除接口中的对象： 可用于删除实现特定接口的类型对象。阅读更多关于接口作的信息 。


### [](#values-and-parameters)Values and parameters数值与参数


When creating or modifying links and objects, the Rules require additional values for their operation. When modifying an object, the rules also define which properties are modified. Each property in return is mapped to a value provided by one of multiple options (Rules on links can only take object reference parameters):在创建或修改链接和对象时，规则需要额外的值来实现其作。修改对象时，规则还定义了哪些属性被修改。返回中的每个属性都映射到多个选项之一提供的值（链接规则只能接受对象引用参数）：


- **From parameter:** An existing parameter of the same type as the property. By default, every new property being added to the rule will automatically create a parameter with the same name and will be mapped to take the value of this parameter.参数来源： 与该属性类型相同的现有参数。默认情况下，规则中每添加一个新属性都会自动创建一个同名参数，并映射为取该参数值。
- **Object parameter property:** A property of an existing object reference parameter. The property type of the object parameter needs to match the property type it is mapped to.对象参数属性： 是现有对象参考参数的属性。对象参数的属性类型必须与其映射的属性类型相匹配。
- **Static value:** A static value that only exists in the Rules part of the action type. This value is cannot be changed when interacting with the action in Workshop, Slate, or Object Views.静态数值： 一个静态值，只存在于动作类型的规则部分。在与工作坊、Slate 或对象视图中的动作交互时，该值无法更改。
- **Current User/Time:** String and timestamp properties can also take on contextual values in the form of the actions current user or the time of submission. Just like the **Static value**, these values cannot be interacted with when submitting the action and cannot be used in other parts of the action type.当前用户/时间： 字符串和时间戳属性还可以以当前用户的作或提交时间的形式具有上下文值。与静态值类似，提交动作时无法交互这些值，也无法用于动作类型的其他部分。


### [](#creating-an-object--many-to-many-link)Creating an object & many-to-many link创建对象与多对多链接


You can also create objects and linked many-to-many at the same time. While just creating a many-to-many link requires objects on both sides of the link to exist prior, you can create both entities via one action type. Start by configuring a **Create object** rule with an object type that has a many-to-many link. Then click the **Add link** button below **Add property** to select the link type and configure the links.你还可以同时创建对象并进行多对多连接。虽然创建多对多链接需要链路两侧的对象先存在，但你可以通过一种动作类型创建这两个实体。首先，将创建对象规则配置为具有多对多链接的对象类型。然后点击“ 添加链接 ”下方的添加链接按钮，选择链接类型并配置链接。


In order to create a one-to-many or one-to-one link type, simply edit the foreign key on the object.要创建一对多或一一链接类型，只需编辑对象上的外键即可。


### [](#invalid-combinations)Invalid combinations无效组合


Action types can include combinations of Ontology rules. When multiple rules are defined, the actions backend compiles rules to generate a single edit per object (e.g., **Add object**, **Modify object(s)**, or **Delete object(s)**). For example, if the result of one rule updates a property to "A", but another rule in the same action type updates the same object's property to "B", the resulting edit would just update the property to "B". The order of rules affects the final object edit. As a result, the following combinations of object edits are not supported:动作类型可以包含本体规则的组合。当定义多个规则时，动作后端会编译规则，生成每个对象的单一编辑（例如， 添加对象 、 修改对象或删除对象 ）。例如，如果一个规则的结果将属性更新为“A”，但同一动作类型的另一个规则将同一对象的属性更新为“B”，那么最终的编辑就会将该属性更新为“B”。规则的顺序会影响最终的对象编辑。因此，以下对象编辑组合不被支持：


- Objects cannot be deleted before they are added or modified.对象在添加或修改之前不能被删除。
- Objects cannot be modified before they are added.对象在添加之前不能被修改。
- Objects cannot be created twice in one form submission.在同一表单提交中，对象不能被创建两次。


## [](#other-rules)Other rules其他规则


There are two types of rules that trigger a [side effect](/docs/foundry/action-types/side-effects-overview/):触发副作用的规则有两种类型：


- [**Notification**](/docs/foundry/action-types/notifications/) rules can be used to send a notification about the action. Parameters may be used to customize the content of the notification and the recipients. End users may adjust their preferences to receive notifications via in-platform push notification, email, or both. Notifications are sent once all action edits have been applied, however the content of the notification will be generated based on the state of the Ontology before edits are applied.通知规则可用于发送有关动作的通知。可以使用参数来定制通知内容和收件人。终端用户可以调整偏好，通过平台内推送通知、电子邮件或两者兼有接收通知。所有动作编辑应用完成后，通知才会发送，但通知内容会根据本体状态生成，编辑应用前的状态。
- [**Webhooks**](/docs/foundry/action-types/webhooks/) enable an action to make a request to an external system when the action is applied. Action parameters can be passed into the webhook, which can in turn pass parameters through to the external request. Webhooks may be configured to run before or after edits are applied.Webhook 使动作在应用该动作时能够向外部系统发出请求。动作参数可以传递到 webhook 中，webhook 再将参数传递给外部请求。Webhook 可以配置为在编辑应用前或后运行。

