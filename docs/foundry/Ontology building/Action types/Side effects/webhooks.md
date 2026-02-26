# [](#webhooks)Webhooks


A [webhook](/docs/foundry/data-connection/webhooks-overview/) is a concept in Data Connection that enables sending a request to an external system, such as Salesforce, SAP, or any configured HTTP server, typically to modify data in that external system.Webhook 是数据连接中的一个概念，它允许向外部系统（如 Salesforce、SAP 或任何配置的 HTTP 服务器）发送请求，通常用于修改该外部系统中的数据。


By setting up a webhook and then configuring it for use in an action, you can send data to an external system when end users apply an action in Foundry. This enables workflows in Foundry to connect directly with source systems and write back data and decisions into those systems.通过设置一个 webhook 并将其配置为在操作中使用，当最终用户在 Foundry 中应用操作时，可以将数据发送到外部系统。这使得 Foundry 中的工作流能够直接与源系统连接，并将数据和决策写回这些系统。


This section details the various options available for configuring webhooks in an action. For a step-by-step tutorial, see the documentation on [how to add a webhook in an action](/docs/foundry/action-types/set-up-webhook/).本节详细介绍了在操作中配置 webhooks 的各种选项。有关逐步教程，请参阅有关如何在操作中添加 webhook 的文档。


## [](#webhooks-writeback-vs-side-effect)Webhooks: Writeback vs. side effectWebhooks：写入回传与副作用


There are two ways that webhooks can be configured for use in an action: as a **writeback** or as a **side effect**.在操作中配置 webhooks 有两种方式：作为写入回传或作为副作用。


![Add webhook](webhooks-add-webhook.png?width=400)


For convenience, below is a table comparing the behavior of writeback and side effect webhooks.为方便起见，以下表格比较了写入回传和副作用 webhooks 的行为。

























| Type类型 | When applied应用时 | Failure shown to end user?向用户显示失败？ | Timing时间 |
| --- | --- | --- | --- |
| **Writeback写入** | Before object changes在对象变更之前 | Yes是 | Before user sees success or failure在用户看到成功或失败之前 |
| **Side effect副作用** | After object changes对象变更后 | No否 | May be after user sees success message可能在用户看到成功消息后 |


The following sections describe writeback webhooks and side effect webhooks in more detail.以下部分将更详细地描述回写 webhooks 和副作用 webhooks。


### [](#writeback-webhooks)Writeback webhooks回写 webhooks


When configured as a **writeback**, the webhook will be executed *before* any other rules are evaluated; if the webhook execution fails, no other changes will be made. If you want to ensure that changes are not made in Foundry before the external system, you should set up your webhook as a writeback.当配置为回写时，webhook 将在任何其他规则被评估之前执行；如果 webhook 执行失败，则不会进行任何其他更改。如果您希望确保在外部系统之前 Foundry 不会做出更改，您应该将您的 webhook 配置为回写。


This behavior enables some degree of transactionality between Foundry and the external system. Using a writeback webhook guarantees that if the request to the external system fails, no changes will be applied to the Foundry Ontology. However, it is still possible that the external request may succeed but Ontology changes could fail.这种行为在 Foundry 和外部系统之间提供了一定程度的交易性。使用回写 webhook 可以保证如果对外部系统的请求失败，则不会将更改应用于 Foundry 本体。然而，仍然有可能外部请求成功但本体更改失败。


Because the action stops being applied when a writeback webhook fails, you can only configure a single webhook as a writeback. If this webhook fails when the action is applied, an error will be shown to the end user describing the failure.因为当回写 webhook 失败时操作会停止应用，所以您只能配置一个 webhook 为回写。如果当操作应用时这个 webhook 失败，将向最终用户显示一个错误信息描述失败情况。


When a webhook is configured as a writeback, its output parameters can be used in subsequent rules. See the [output parameters](#output-parameters) section below for more details.当 webhook 配置为写回时，其输出参数可以在后续规则中使用。更多详情请参阅下方的输出参数部分。


### [](#side-effect-webhooks)Side effect webhooks副作用 webhooks


When configured as a **side effect**, a webhook will be executed *after* other rules are evaluated. This means that modifications to Foundry objects will occur before side effects are applied. You can configure multiple side effect webhooks in a single action, and they will be executed in no particular order. In an action with side effect webhooks, the end user will see a success message after Foundry objects are modified; executing the side effects may happen after the success message is shown.当配置为副作用时，webhook 将在其他规则评估后执行。这意味着 Foundry 对象的修改将在应用副作用之前发生。您可以在单个操作中配置多个副作用 webhooks，它们将按无特定顺序执行。在具有副作用 webhooks 的操作中，用户在 Foundry 对象修改后会看到成功消息；执行副作用可能会在成功消息显示之后发生。


If you need to call a webhook multiple times from a single action, this can be achieved with a side effect webhook by providing a list of payloads as an input. This will trigger the webhook as many times as there are payloads in the list provided and will be processed in no guaranteed order. An example of this can be found below in the [input parameters](#input-parameters) section.如果您需要从单个操作中多次调用 webhook，可以通过将有效载荷列表作为输入来实现，这会触发 webhook 执行次数与列表中提供的有效载荷数量相同，并且将按无保证的顺序处理。以下输入参数部分提供了一个示例。


You should use side effect webhooks when you want to send best-effort notifications or write back to multiple external systems.当你需要发送尽力而为的通知或写入多个外部系统时，应使用副作用 webhooks。


## [](#input-parameters)Input parameters输入参数


In order to configure a Webhook in an Action, you must populate all of its required input parameters. General reference material about Webhook input parameters is available in the [Data Connection documentation](/docs/foundry/data-connection/webhooks-reference/#input-parameters).要在操作中配置 Webhook，你必须填写其所有必需的输入参数。有关 Webhook 输入参数的通用参考材料可在数据连接文档中找到。


There are two ways to configure Webhook input parameters: by mapping to Action parameters, or by using a Function.配置 Webhook 输入参数有两种方式：映射到 Action 参数，或使用 Function。


When mapping to **Action parameters**, each required Webhook input must be set to either an Action parameter of the same type, a static value, or a property of an object parameter.在映射到 Action 参数时，每个必需的 Webhook 输入必须设置为相同类型的 Action 参数、静态值或对象参数的属性。


![Input parameters](webhooks-input-parameters.png?width=400)


When using a [Function](/docs/foundry/functions/overview/), you must select a Function that returns a custom type that includes all of the required Webhook input parameters and strongly matches the Webhook type, otherwise you will receive an `OntologyMetadata:ActionWebhookInputsDoNotHaveExpectedType` error. Using a Function to populate Webhook input parameters can be useful when you want to use logic to populate inputs, especially if this logic is based on Ontology objects. For example, you can retrieve linked objects and pull property values from those objects to prepopulate Webhook inputs.在使用函数时，你必须选择一个返回自定义类型的函数，该自定义类型包含所有必需的 Webhook 输入参数，并且与 Webhook 类型强匹配，否则你将收到一个 OntologyMetadata:ActionWebhookInputsDoNotHaveExpectedType 错误。当你想使用逻辑来填充输入时，使用函数来填充 Webhook 输入参数会很有用，特别是当这个逻辑基于本体对象时。例如，你可以检索链接对象，并从这些对象中提取属性值来预填充 Webhook 输入。


As an example, suppose you have a Webhook which takes three input parameters with IDs `name`, `industry`, and `country`:例如，假设你有一个 Webhook，它接受三个输入参数，ID 分别为 name 、 industry 和 country ：


![Input parameters example](webhooks-input-parameters-example.png?width=400)


You can write a Function that returns a custom interface of the same structure:你可以编写一个返回相同结构的自定义接口的函数：


```
Copied!`1export interface MyWebhookInput {
2    name: string;
3    industry: string;
4    country: string;
5}`
```


Then, you can select this Function when configuring Webhook inputs in an Action, mapping Action parameters to the parameters required by the Function:然后，在配置操作的 Webhook 输入时，你可以选择此功能，将操作参数映射到功能所需的参数：


![Mapping Action parameters to the parameters required by a Function](webhooks-input-parameters-define-using-action.png?width=400)


Below is a full code example of a Function that loads data from an Ontology object and uses it to populate Webhook inputs.下面是一个完整的函数代码示例，该函数从本体对象加载数据，并使用这些数据来填充 Webhook 输入。


```
Copied!`1import { Function, UserFacingError } from "@foundry/functions-api";
2import { Company } from "@foundry/ontology-api";
3
4export interface MyWebhookInput {
5    name: string;
6    industry: string;
7    country: string;
8}
9
10export class MyWebhookFunctions {
11    @Function()
12    public returnWebhookInput(company: Company): MyWebhookInput {
13        if (!company.name || !company.industry || !company.country) {
14            throw new UserFacingError("Some required fields are not set.");
15        }
16        return {
17            name: company.name,
18            industry: company.industry,
19            country: company.country,
20        }
21    }
22}`
```


A side effect Webhook may be called multiple times by returning a list of payloads from a Function. Below is an example Function which takes two companies as inputs, and returns a list containing two payloads matching the input parameters expected by a Webhook. If this Function is used from Actions to return the inputs for a side effect Webhook, it will result in two separate Webhook executions.一个副作用 Webhook 可能会通过从 Function 返回一个 payload 列表而被多次调用。下面是一个 Function 的示例，它接受两个公司作为输入，并返回一个包含两个 payload 的列表，这些 payload 与 Webhook 期望的输入参数相匹配。如果这个 Function 从 Actions 中用于返回副作用 Webhook 的输入，它将导致两次独立的 Webhook 执行。


```
Copied!`1import { Function } from "@foundry/functions-api";
2import { Company } from "@foundry/ontology-api";
3
4export interface MyWebhookInput {
5    arg1: string;
6    arg2: string;
7}
8
9export class MyFunctions {
10    @Function()
11    public createWebhookRequest(company1: Company, company2: Company): MyWebhookInput[] {
12        return [
13        {
14           arg1: company1.someProperty,
15           arg2: company1.someOtherProperty,
16        },
17        {
18           arg1: company2.someProperty,
19           arg2: company2.someOtherProperty,
20        }
21        ];
22    }
23}`
```


## [](#output-parameters)Output parameters输出参数


When a Webhook is configured as a [writeback Webhook](#writeback-webhooks), you can use its output parameters in subsequent rules. This is useful when the external system returns data that you want to immediately write into a Foundry object or use in a subsequent [notification](/docs/foundry/action-types/notifications/) or [side effect Webhook](#side-effect-webhooks).当 Webhook 配置为写回 Webhook 时，您可以在后续规则中使用其输出参数。当外部系统返回您希望立即写入 Foundry 对象或用于后续通知或副作用 Webhook 的数据时，这很有用。


General reference material about Webhook output parameters is available in the [Data Connection documentation](/docs/foundry/data-connection/webhooks-reference/#output-parameters).有关 Webhook 输出参数的通用参考材料可在数据连接文档中找到。


To use an output parameter in a subsequent logic rule, select **Writeback response** when populating the value for a logic rule, then select the specific output you wish to use:要在后续的逻辑规则中使用输出参数，在为逻辑规则填充值时选择写入响应，然后选择您希望使用的特定输出：


![Using an output parameters in a Logic Rule](webhooks-output-parameters-in-logic-rule.png?width=400)

