# [](#side-effects)Side effects副作用


Action types are designed to support the full range of decision-making processes within an organization. When the Ontology serves as the system of record for a decision-making process, using [rules](/docs/foundry/action-types/rules/) to define object modifications allows you to express business processes with great flexibility. In order to support the full range of organizational processes, action types support a few additional features:动作类型旨在支持组织内部的各种决策过程。当本体作为决策过程的系统记录时，使用规则定义对象修改允许你以极大的灵活性表达业务流程。为了支持各种组织流程，动作类型支持一些附加功能：


- For real-time processes, you may need to *notify* users about changes that are happening in the system so they can take action in response.对于实时流程，你可能需要通知用户系统中正在发生的变化，以便他们能够做出响应。
- In cases when a system besides Foundry is the source of truth for your organization, you may need to *integrate* with the other system to support the existing business process. This pattern is sometimes referred to as "decision orchestration."当你的组织系统记录来源是 Foundry 以外的系统时，你可能需要与其他系统集成以支持现有的业务流程。这种模式有时被称为“决策编排”。


**Side effects** in action types enable you to send data out of Foundry to integrate with existing organizational processes. There are two main types of side effects:在动作类型中的副作用使您能够将数据从 Foundry 发送出去，以集成现有的组织流程。副作用主要有两种类型：


- [Notifications](/docs/foundry/action-types/notifications/) allow you to flexibly configure how a user should be notified when an action is applied. This includes the ability to send an email to users on the platform.通知允许您灵活配置当动作被应用时如何通知用户。这包括向平台上的用户发送电子邮件的能力。
- [Webhooks](/docs/foundry/action-types/webhooks/) allow you to connect to systems outside Foundry in a highly flexible way, including sending requests to a REST API or an ERP system. This enables you to write to other sources systems in your organization, or more flexibly send notifications to users by integrating with messaging systems.Webhooks 允许您以高度灵活的方式连接到 Foundry 外部的系统，包括向 REST API 或 ERP 系统发送请求。这使您能够写入组织中的其他源系统，或通过集成消息系统更灵活地向用户发送通知。


You can learn more about notifications and webhooks using the links above, or review these guides to get started:您可以通过上面的链接了解更多关于通知和 Webhooks 的信息，或查阅这些指南开始使用：


- [Set up notifications设置通知](/docs/foundry/action-types/set-up-notification/)
- [Set up a webhook设置 Webhook](/docs/foundry/action-types/set-up-webhook/)

