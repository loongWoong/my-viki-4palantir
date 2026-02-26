# [](#models-in-the-ontology)Models in the Ontology本体论中的模型


Organizations are looking to leverage artificial intelligence (AI) and machine learning (ML) to accelerate and improve decision-making. But the reality of operationalizing AI/ML is complex, and the typical return on investment rarely lives up to expectations.组织正寻求利用人工智能（AI）和机器学习（ML）来加速和提升决策效率。但人工智能/机器学习的实际作化现实复杂，典型的投资回报率很少达到预期。


Foundry provides the key capabilities necessary to bridge this gap: a trustworthy data foundation, tools for evaluating and comparing models against organizational objectives, and functionality for deploying models into user-facing operational workflows. This page focuses on the last step: deploying an evaluated model into production.Foundry 提供了弥合这一差距的关键能力：可信的数据基础、用于评估和比较模型与组织目标的工具，以及将模型部署到面向用户的运营流程的功能。本页重点介绍最后一步：将评估过的模型部署到生产环境中。


## [](#end-to-end-workflow)End-to-end workflow端到端工作流程


At a high level, these are the end-to-end steps required to operationalize AI/ML in Foundry for live inference with the Ontology:从大体来看，以下是将 AI/ML 在 Foundry 中实现实时推理所需的端到端步骤：


1. [Create a model](/docs/foundry/integrate-models/integrate-overview/) in Foundry.在 Foundry 中创建一个模型 。
2. Configure a [direct model deployment](/docs/foundry/manage-models/create-a-model-deployment/).配置直接模型部署 。
3. [Publish a simple wrapper function for your model](/docs/foundry/model-integration/model-functions-guide/) and [optionally call it from another function](/docs/foundry/functions/functions-on-models/) to orchestrate complex logic around your model.发布一个简单的模型包装函数 ，并可选地从另一个函数调用它 ，以围绕模型编排复杂逻辑。
4. Use that function for live inference in [Workshop](/docs/foundry/workshop/functions-use/), [Vertex](/docs/foundry/vertex/overview/) and other end-user facing applications.在 Workshop、Vertex 及其他面向终端用户的应用中，使用该函数进行实时推理。


Ontology Objects can also be backed with datasets that leverage a model for batch inference - [learn how to use a model in Code Repositories](/docs/foundry/model-integration/tutorial-train-code-repositories/).本体对象还可以支持利用模型进行批量推断的数据集—— 学习如何在代码仓库中使用模型 。


## [](#benefits)Benefits优点


Just like mapping datasets to Ontology concepts provides [benefits](/docs/foundry/ontology/why-ontology/) for workflow development and decision-making, mapping models to the Ontology provides a number of benefits:正如将数据集映射到本体概念对工作流开发和决策具有好处一样，将模型映射到本体论也带来了多项好处：


- **Interpretability**. Because all modeling results are defined in terms of real-world concepts (properties of an object type), end users do not need to understand machine learning in order to use modeling results. Instead, users simply interact with simple concepts such as a *forecast*, *estimate*, or *classification*.可解读性。由于所有建模结果都是基于现实世界的概念（对象类型的属性）来定义的，终端用户不需要理解机器学习即可使用建模结果。用户只需与预测 、 估计或分类等简单概念进行交互。
- **Economies of scale**. Instead of each modeling project being a bespoke effort created in service of a specific use case, modeling efforts can build on each other over time. For example, a forecast produced for one use case can immediately be used for subsequent use cases as well, reducing duplicated effort and providing end-user value more quickly over time.规模经济 。建模工作不再是为特定用例量身定制的项目，而是可以相互推移。例如，为一个用例生成的预测可以立即用于后续用例，减少重复工作，并随着时间推移更快地为终端用户提供价值。
- **Connectivity at scale**. By incorporating ML models, the Ontology becomes a single source of truth for the organization, not just in terms of data, but also in terms of *logic*. Models encode the organization's expectations for how things may change in the future. In this way, the Ontology becomes a "digital twin" for the entire enterprise, which unlocks the ability to simulate changes across the organization in ways that would never be possible with a wide array of disparate modeling efforts.大规模的连接性。通过引入机器学习模型，本体论不仅在数据方面，也在逻辑上成为组织的唯一真实来源。模型编码了组织对未来可能变化的预期。通过这种方式，本体成为整个企业的“数字孪生”，从而释放了以各种不同建模方法无法实现的方式模拟整个组织的变化的能力。

