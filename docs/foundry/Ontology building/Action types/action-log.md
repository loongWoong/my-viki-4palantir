# [](#action-log)Action log操作日志


The action log models all action submissions as object types to be analyzed and displayed in object-aware Foundry tooling. Use an action log object type as an input to decision-making workflows and to monitor changes to your Ontology.操作日志将所有操作提交建模为待分析和在对象感知 Foundry 工具中显示的对象类型。将操作日志对象类型用作决策工作流输入，并监控您的本体变化。


The action log is designed to capture decisions made by submitting actions and make these decision available as data in the Ontology. For use cases where
logging all edits to an object is desired, [edit history](/docs/foundry/object-edits/user-edit-history/) can be enabled for an object type.操作日志旨在捕获通过提交操作做出的决策，并将这些决策作为数据在本体中提供。对于希望记录对象所有编辑用例，可以为对象类型启用编辑历史。


## [](#background)Background背景


Actions are the primary way to modify the Ontology and trigger related side effects. Often, these Ontology modifications are the result of a specific decision or are accompanied by data audit requirements. The action log simplifies generation and maintenance of object types that represent these decisions and data edits. For easy identification, all action log object types are prefaced with `[LOG]`.操作是修改本体和触发相关副作用的主要方式。通常，这些本体修改是特定决策的结果，或伴随数据审计要求。操作日志简化了表示这些决策和数据编辑的对象类型的生成和维护。为便于识别，所有操作日志对象类型均以 [LOG] 为前缀。


## [](#action-log-ontology)Action log Ontology动作日志本体


Action log object types map one-to-one with action types. Submitting an action generates a single new object of the corresponding action log object type. This newly-created object is automatically linked to all objects edited by the submitted action. By modeling log object types one-to-one with action types, the action log supports capturing context beyond specific object edits, such as which other objects were concurrently edited and the state of the world (as represented by the Ontology) at the time of action submission.动作日志对象类型与动作类型一一对应。提交一个动作会生成一个对应动作日志对象类型的新对象。这个新创建的对象会自动链接到所有被提交动作编辑过的对象。通过将日志对象类型与动作类型一一建模，动作日志支持捕获特定对象编辑之外的上下文信息，例如哪些其他对象同时被编辑以及动作提交时世界状态（由本体表示）的情况。


For example, imagine a `Close Alerts` action type that modifies the "Status" property of many selected `Alert` objects to "Closed". When configured with an action log, closing 10 `Alert` objects at once will yield a single `action log` object with foreign key links to all 10 `Alert` objects.例如，想象一个 Close Alerts 动作类型，它将多个选中的 Alert 对象的"状态"属性修改为"已关闭"。当配置了动作日志时，一次性关闭 10 个 Alert 对象将生成一个 action log 对象，该对象通过外键链接到所有 10 个 Alert 对象。


To apply an action log-backed action type, users need the appropriate permissions for the action log object type, just as they do for any other object types that the action type might create or modify through rules and functions.要应用基于动作日志的动作类型，用户需要拥有相应权限，就像他们需要拥有通过规则和函数创建或修改的动作类型可能涉及的其他对象类型的权限一样。


### [](#action-log-schema)Action log schema操作日志模式


By default, action log object types store:默认情况下，操作日志对象类型存储：


- **Action RID:** Unique identifier for a single action submission操作 RID：单个操作提交的唯一标识符
- **Action type RID:** Unique identifier for a single action type操作类型 RID：单个操作类型的唯一标识符
- **Action type version:** Version number that auto-increments each time an action type is updated动作类型版本：每次更新动作类型时自动递增的版本号
- **Timestamp:** UTC timestamp of action submission时间戳：动作提交的 UTC 时间戳
- **UserId:** Multipass user ID for action submitting user用户 ID：提交动作的用户的多路通行用户 ID
- **Edited objects:** Primary key values of all objects edited by the action. Note that storing properties of edited objects other than the primary key is not supported.编辑对象：动作编辑的所有对象的主键值。注意，不支持存储除主键外的编辑对象属性。
- [Optional] **Summary:** A customizable string to describe the action[可选] 摘要：用于描述操作的定制字符串
- [Optional] **Parameter values**[可选] 参数值
- [Optional] **Property values of object reference parameters** (this is not supported for object reference parameters if `allow multiple values` is enabled)[可选] 对象引用参数的属性值（如果启用 allow multiple values ，则不支持对象引用参数）


Action log object types can be configured to store object properties that are not edited by the action. This allows you to store data edits as well as relevant information about the context of or motivation for the Ontology edits.操作日志对象类型可以配置为存储操作未编辑的对象属性。这允许您存储数据编辑以及与本体编辑的上下文或动机相关的信息。


Returning to the example of a `Close Alerts` action type, imagine the `Alert` objects also have a "Priority" property containing values "High Priority" and "Low Priority" as well as a "Created at" timestamp and a "Source" machine. The action log supports storing these properties, even if they are not edited by `Close Alerts`. By aggregating on "Priority", without editing the column we can answer questions such as "where is the source of most "High Priority" alerts?" or "how long does it take to close "High Priority" alerts?".回到 Close Alerts 动作类型的示例，想象 Alert 对象还包含一个"优先级"属性，其中包含"高优先级"和"低优先级"的值，以及一个"创建时间"的时间戳和一个"来源"机器。动作日志支持存储这些属性，即使它们没有被 Close Alerts 编辑。通过按"优先级"聚合，而无需编辑列，我们可以回答诸如"最高优先级警报的来源在哪里？"或"关闭最高优先级警报需要多长时间？"等问题。


## [](#action-log-on-function-backed-action-types)Action log on function-backed action types基于函数的动作类型的动作日志


To configure the action log for a function-backed action type, the backing Ontology edit function must have `Edits` provenance configured. See the [functions documentation](/docs/foundry/functions/edits-overview/) for more information on `Edits` provenance.要配置基于函数的动作类型的动作日志，支撑的本体编辑函数必须配置 Edits 可追溯性。有关 Edits 可追溯性的更多信息，请参阅函数文档。


## [](#action-log-timeline)Action log timeline动作日志时间线


You can view action log object types in a timeline using a custom Workshop widget. With this widget, the timeline can be configured to support data audits in order to help answer the questions "what changed, by whom, and when?"您可以使用自定义的 Workshop 小部件在时间轴上查看操作日志对象类型。通过这个小部件，时间轴可以配置为支持数据审计，以帮助回答"什么被更改、由谁更改以及何时更改"的问题。


Within Workshop, action log object types can be unioned together for a holistic view of edits within a use case or across an Ontology.在 Workshop 中，行动日志对象类型可以联合起来，以获得用例内或跨本体编辑的整体视图。


Configure the action log timeline by selecting the edited object type. Then choose which action log object types to display, along with the desired action log object type properties.通过选择编辑的对象类型来配置操作日志时间线。然后选择要显示的操作日志对象类型，以及所需的操作日志对象类型属性。

