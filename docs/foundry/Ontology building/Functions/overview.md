# [](#functions)Functions函数


**Functions** enable code authors to write logic that can be executed quickly in operational contexts, such as dashboards and applications designed to empower decision-making processes. This logic is executed on the server side in an isolated environment.函数使代码作者能够编写可在操作环境中快速执行的逻辑，例如用于支持决策过程的仪表板和应用程序。该逻辑在服务器端的隔离环境中执行。


Notably, functions include first-class support for authoring logic based on the Ontology. This includes support for reading the properties of various object types, traversing links, and flexibly making Ontology edits.值得注意的是，函数提供了对基于本体编写逻辑的一流支持。这包括对读取各种对象类型的属性、遍历链接以及灵活地编辑本体的支持。


Common use cases for functions include:函数的常见用例包括：


- Returning object sets or variable values for use in [Workshop](/docs/foundry/workshop/functions-use/).返回用于工作坊的对象集或变量值。
- Displaying transformed values in a derived table column using [Workshop's function-backed columns](/docs/foundry/workshop/derived-properties/).使用工作坊的函数支持列，在派生表列中显示转换后的值。
- Aggregating object type values to display as [Workshop charts](/docs/foundry/workshop/widgets-chart/#function-aggregations-function-backed-layers).聚合对象类型值以在工作坊中显示为图表。
- Expressing a complex edit to the Ontology that updates many objects through a [function backed action](/docs/foundry/action-types/function-actions-overview/).对本体进行复杂编辑，通过函数支持的操作更新许多对象。
- Running logic in the backend to return information to be displayed in the frontend in [Slate](/docs/foundry/slate/overview/).在后台运行逻辑，以返回信息在 Slate 中显示。
- Computing custom metrics or aggregations for display in [Quiver](/docs/foundry/quiver/overview/).为 Quiver 计算自定义指标或聚合。
- Querying external systems to enrich objects in the Ontology through [external functions](/docs/foundry/functions/webhooks/).查询外部系统，通过外部函数丰富本体中的对象。
- Using Python functions as a sidecar container in [Pipeline Builder](/docs/foundry/functions/python-functions-builder/).在 Pipeline Builder 中使用 Python 函数作为侧边容器。


The languages supported by functions are [TypeScript ↗](https://www.typescriptlang.org/docs/handbook/basic-types.html) and [Python ↗](https://www.python.org/).函数支持的语言是 TypeScript ↗ 和 Python ↗。


For more information on feature support by language and choosing a language or language version, refer to the [language feature support specifications](/docs/foundry/functions/language-feature-support/).有关语言功能支持和选择语言或语言版本的信息，请参阅语言功能支持规范。


To get started using functions in Foundry, we recommend the following tutorials:要在 Foundry 中使用函数，我们推荐以下教程：


- [Getting started with TypeScript v1 functions使用 TypeScript v1 函数入门](/docs/foundry/functions/typescript-v1-getting-started/)
- [Getting started with TypeScript v2 functions开始使用 TypeScript v2 函数](/docs/foundry/functions/typescript-v2-getting-started/)
- [Getting started with Python functions开始使用 Python 函数](/docs/foundry/functions/python-getting-started/)


Palantir Learning portalPalantir 学习门户Try our ["Speedrun: Your first Ontology function" course ↗](https://learn.palantir.com/speedrun-your-first-ontology-function) on learn.palantir.com.在 learn.palantir.com 上尝试我们的 "速成：你的第一个本体函数" 课程 ↗。

