# [](#feature-support-by-language)Feature support by language语言的功能支持


Not all features are supported by all languages. Refer to the chart below for feature support by language.并非所有功能都由所有语言支持。请参考下表了解各语言的功能支持情况。































































































































| Functions capability by language语言的功能能力 | AIP LogicAIP 逻辑 | TypeScript v1 | TypeScript v2 | Python | Description描述 |
| --- | --- | --- | --- | --- | --- |
| Ontology object support本体对象支持 | Yes是 | Yes是 | Yes是 | Yes是 | The ability to [access Ontology objects](/docs/foundry/functions/foo-getting-started/) in your function.在函数中访问本体对象的能力。 |
| Ontology interfaces support本体接口支持 | No否 | No否 | Yes是 | No否 | The ability to access and edit Ontology interfaces in your function.在函数中访问和编辑本体接口的能力。 |
| Ontology edits support本体编辑支持 | Yes是 | Yes是 | Yes是 | Yes是 | The ability to [edit Ontology objects](/docs/foundry/functions/edits-overview/) in your function.在您的函数中编辑本体对象的能力。 |
| Queryable in Workshop可在工作坊中查询 | Yes是 | Yes是 | Yes是 | Yes是 | Invoking a function from a [Workshop application](/docs/foundry/workshop/functions-use/).从工作坊应用程序中调用函数。 |
| Usable in Pipeline Builder可在管道构建器中使用 | No否 | No否 | No否 | Yes是 | Calling a function from [Pipeline Builder pipelines](/docs/foundry/functions/python-functions-builder/).从管道构建器管道中调用函数。 |
| Functions on models support模型上的函数支持 | Yes是 | Yes是 | No否 | No否 | Executing live deployment models [from a function](/docs/foundry/functions/functions-on-models/).从函数中执行实时部署模型。 |
| Semantic search support语义搜索支持 | Yes是 | Yes是 | Yes是 | Yes是 | Use functions to create vectors for [semantic search](/docs/foundry/ontology/overview-semantic-search/).使用函数为语义搜索创建向量。 |
| Webhook supportWebhook 支持 | No否 | Yes是 | No否 | No否 | The ability to call [webhooks from functions](/docs/foundry/functions/webhooks/).从函数中调用 webhook 的能力。 |
| External API call support外部 API 调用支持 | No否 | Yes是 | Yes是 | Yes是 | Querying external services from [within functions](/docs/foundry/functions/api-calls/).在函数内部查询外部服务。 |
| Serverless execution support无服务器执行支持 | Yes是 | Yes是 | Yes是 | Yes是 | A serverless function will be spun up on demand when invoked.  Refer to [serverless functions](#serverless-functions) below for more information.当被调用时，将按需启动一个无服务器函数。有关更多信息，请参阅下文的无服务器函数。 |
| Deployed execution support部署执行支持 | No否 | No否 | Yes是 | Yes是 | A deployed function will have dedicated resources allocated to it, ready to serve requests.部署的函数将分配专用资源，准备服务请求。 |
| Call function from API gateway从 API 网关调用函数 | Yes是 | Yes是 | Yes是 | Yes是 | The ability to hit a [query function](/docs/foundry/functions/query-functions/) from the API gateway.从 API 网关调用查询函数的能力。 |
| Marketplace support市场支持 | Yes是 | Yes是 | Yes是 | Yes是 | The ability to package and ship functions in [Marketplace](/docs/foundry/marketplace/overview/).在 Marketplace 中打包和发送函数的能力。 |
| Bring-your-own-model自带模型 | Yes是 | Yes是 | No否 | No否 | The ability to register a function [as a model](/docs/foundry/aip/bring-your-own-model/).将函数注册为模型的能力。 |


## [](#ontology-sdk-support)Ontology SDK support本体 SDK 支持


Python and TypeScript v2 functions support the [Ontology SDK](/docs/foundry/ontology-sdk/overview/) (OSDK). The OSDK allows you to leverage the Ontology directly from your development environment and provides [benefits](/docs/foundry/ontology-sdk/overview/#osdk-benefits) such as compatibility with Developer Console and OSDK versioning. We recommend using Python or TypeScript v2 to access these benefits in your functions repository.Python 和 TypeScript v2 函数支持本体 SDK（OSDK）。OSDK 允许您直接从开发环境中利用本体，并提供与开发者控制台兼容以及 OSDK 版本控制等优势。我们建议使用 Python 或 TypeScript v2 来访问您函数仓库中的这些优势。


## [](#typescript-v1-vs-typescript-v2)TypeScript v1 vs. TypeScript v2TypeScript v1 与 TypeScript v2


Both TypeScript v1 and TypeScript v2 allow users to leverage TypeScript's core language features, but there are differences in supported platform features, as shown in the feature support table above. We recommend building workflows using TypeScript v2 functions to take advantage of several key improvements over TypeScript v1:TypeScript v1 和 TypeScript v2 都允许用户利用 TypeScript 的核心语言特性，但在支持的平台功能上存在差异，如上表所示。我们建议使用 TypeScript v2 函数来构建工作流，以利用 TypeScript v1 的几个关键改进：


- **Serverless execution in a full Node.js runtime:** TypeScript v2 functions run in a Node.js environment, supporting core modules like `fs`, `child_process`, and `crypto`. This enables greater compatibility with NPM libraries that interact with the file system, perform CPU-intensive tasks in parallel, or require other system-level operations.在完整的 Node.js 运行时中进行无服务器执行：TypeScript v2 函数在 Node.js 环境中运行，支持核心模块如 fs 、 child_process 和 crypto 。这提高了与交互文件系统、并行执行 CPU 密集型任务或需要其他系统级操作的 NPM 库的兼容性。
- **First-class OSDK support:** The OSDK can now be used seamlessly in TypeScript v2 functions, making it easy to reuse code, both in and out of the platform. It also provides more efficient APIs for working with large-scale Ontology data.一流的 OSDK 支持：现在可以在 TypeScript v2 函数中无缝使用 OSDK，轻松重用平台内外的代码。它还提供了更高效的 API 来处理大规模的本体数据。
- **Configurable resource requests:** TypeScript v2 functions allow you to request up to 8 vCPUs and 5GB of memory, offering greater control over performance and scalability.可配置的资源请求：TypeScript v2 函数允许您请求高达 8 个 vCPU 和 5GB 的内存，提供对性能和可扩展性的更多控制。


## [](#serverless-functions)Serverless functions无服务器函数


If serverless functions are enabled for your enrollment, new repositories will use serverless functions by default. We recommend using serverless functions instead of deployed functions for most use cases. With serverless functions, you can have multiple versions of a single function available on demand, making upgrades safer.如果您的注册启用了无服务器函数，新的存储库将默认使用无服务器函数。我们建议在大多数用例中改用无服务器函数而非部署的函数。使用无服务器函数，您可以在需要时提供同一函数的多个版本，使升级更安全。


When using Python or TypeScript v2 functions, there are also [some cases where deployed functions are preferred](/docs/foundry/functions/functions-deployed/#choose-between-deployed-and-serverless-execution-modes) or must be used instead of serverless, but these are not common. If available, serverless functions are preferred for several reasons:在使用 Python 或 TypeScript v2 函数时，也有一些情况下更倾向于或必须使用已部署的函数而不是无服务器函数，但这些情况并不常见。如果可用，无服务器函数通常更受青睐，原因如下：


- Serverless functions enable different versions of a single function to be executed on demand, making upgrades safer. With deployed functions, you can only run a single function version at a time.无服务器函数允许按需执行同一函数的不同版本，使升级更安全。对于已部署的函数，您一次只能运行一个函数版本。
- Serverless functions only incur costs when executed, while deployed functions incur costs as long as the deployment is running.无服务器函数只有在执行时才会产生费用，而已部署的函数只要部署在运行状态就会产生费用。
- Serverless functions require less upfront setup and long-term maintenance, as the infrastructure is managed automatically.无服务器函数需要较少的前期设置和长期维护，因为基础设施由系统自动管理。

