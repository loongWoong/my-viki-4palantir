# [](#why-create-an-ontology)Why create an Ontology?为什么要创建本体论？


Organizations can gain several key benefits from building and using an Ontology to organize and leverage their data, as described below:组织可以通过构建和使用本体来组织和利用数据，获得以下若干关键优势：


- [Connectivity at scale大规模连接](#connectivity-at-scale)
- [Interpretability可解释性](#interpretability)
- [Economies of scale规模经济](#economies-of-scale)
- [Decision capture决策捕获](#decision-capture)
- [Powering operational AI/ML驱动运营 AI/ML](#powering-operational-aiml)


In practice, these benefits are realized by using Foundry's Ontology-aware applications which enable rapid analysis, workflow development, and decision capture. [Learn more about Ontology-aware applications.](/docs/foundry/ontology/applications/)在实际作中，这些优势通过使用 Foundry 的本体感知应用实现，这些应用支持快速分析、工作流开发和决策捕获。 了解更多关于本体感知应用的信息。


## [](#connectivity-at-scale)Connectivity at scale大规模连接


The Ontology is a shared source of truth for decision-making and decision capture across a large organization.本体论是大型组织中决策和决策捕获的共享真源。


By providing a single source of truth, the Ontology enables users to easily discover and understand the data available across their organization as well as view their local decisions in a more global context, providing connectivity at scale. The Ontology is used not only to read data, but also to write data back and capture decisions made by users.通过提供单一的真实来源，本体使用户能够轻松发现和理解组织内可用的数据，并在更全球的语境下查看本地决策，实现大规模连接。本体不仅用于读取数据，还用于写回数据并记录用户做出的决策。


Operating from standard data lakes can lead to unmanageable complexity from an ever-growing number of datasets, dashboards, and applications. Over time, increasing effort is required simply to understand what data assets exist or should be used, while new projects "reinvent the wheel" instead of reusing or leveraging existing data assets.在标准数据湖上运行可能导致数据集、仪表盘和应用数量不断增加，导致难以管理的复杂性。随着时间推移，仅仅了解现有或应使用的数据资产就需要越来越多的努力，而新项目则“重新发明轮子”，而不是重复利用或利用现有数据资产。


In contrast, the Ontology provides a well-defined system into which new information is modeled into a common language for the organization. With an Ontology, organizations can make the most of their data as the data asset grows, enabling a digital transformation at scale, while controlling complexity and reducing the difficulty of data management.相比之下，本体提供了一个定义明确的系统，将新信息建模为组织的通用语言。有了本体，组织可以最大化利用数据资产，实现大规模数字化转型，同时控制复杂性并降低数据管理难度。


Example示例An energy company uses the Ontology to create a shared view of the health and performance of a well across petroleum engineers, well integrity engineers, and well management staff. Instead of building several isolated views on the well’s performance, they share their inputs to the same Ontology well object type, allowing short-term decisions about the well’s management and long-term decisions around the asset’s investment strategy to be generated from the same information and insights.一家能源公司利用本体论创建了石油工程师、井完整性工程师和管理人员对井的健康状况和性能的共享视图。它们不再构建多个孤立的油井表现视图，而是将输入共享到同一井体对象类型，从而使井的管理短期决策和资产投资策略的长期决策都能从相同的信息和洞察中生成。


## [](#interpretability)Interpretability可解释性


The most challenging element of operating as a data-driven organization is deploying the data to the various decision makers across the organization. In particular, many decision makers are not technical users comfortable with code or IT concepts such as datasets or joins.作为数据驱动组织运营最具挑战性的部分是将数据部署给组织内各方决策者。尤其是，许多决策者对代码或 IT 概念（如数据集或连接）并不熟悉技术用户。


The Ontology abstracts away these digital concepts and allows users to engage with data represented in the standard terms they use every day. More importantly, the Ontology provides a shared language across different users and functions, allowing them to collaborate without lengthy reconciliation processes to confirm that everyone is looking at the same information.本体论抽象化了这些数字概念，使用户能够与他们日常使用的标准术语中表示的数据互动。更重要的是，本体为不同用户和功能提供了共享语言，使他们能够协作，无需冗长的对账过程来确认所有人都在看同一信息。


Example示例At a manufacturing customer, monitoring data from aircraft sensors was previously inaccessible to both operational users and data scientists due to its scale, complexity, and esoteric format. Today, because of the Ontology modeled on top of the monitoring data, designers can search for parts, see related sensor readings that may signal unexpected or anomalous behavior, and improve future designs without needing to think about tables or joins or going through a complex data preparation process. Although this data was among the most valuable and useful in the organization, under the previous system the process of preparing the data could take days or weeks, limiting use of the data to special projects. Now, this data is immediately accessible not only to data scientists, but to engineers, quality control specialists, and designers.在制造客户中，由于规模庞大、复杂性和晦涩的格式，飞机传感器的数据监测此前对运营用户和数据科学家来说都是无法访问的。如今，由于基于监控数据建模的本体论，设计师可以搜索零件，查看可能提示意外或异常行为的相关传感器读数，并改进未来设计，而无需考虑表格或连接，也无需经历复杂的数据准备过程。尽管这些数据是组织中最有价值和有用的之一，但在之前的系统下，准备数据的过程可能需要数天甚至数周，因此数据的使用受限于特殊项目。现在，这些数据不仅对数据科学家可立即访问，还对工程师、质量控制专家和设计师开放。


## [](#economies-of-scale)Economies of scale规模经济


The Ontology enables significant economies of scale in the construction of an operational platform by converging effort onto a single reusable data asset that supports all analytical work and application development.本体通过将工作集中到支持所有分析工作和应用开发的单一可复用数据资产上，实现了运营平台构建的显著规模经济。


Rather than requiring a dedicated data integration and data layer effort for every new use case or project, data integration is only required for new data entering the platform. Entire applications and use cases can be built on the existing Ontology; the shared data asset lets application builders focus on the organizational problem and the user workflow, instead of on data wrangling.数据集成不需要为每个新用例或项目都进行专门的数据集成和数据层工作，只需针对新数据进入平台时进行。整个应用和用例可以在现有本体上构建;共享数据资产让应用构建者能够专注于组织问题和用户工作流程，而非数据整理。


## [](#decision-capture)Decision capture决策捕获


As an organization's "digital twin", the Ontology supports data writeback and continuous improvement by capturing decisions being made in the organization as data. The Ontology allows for the configuration of writeback and [action types](/docs/foundry/action-types/overview/), which define how users can edit and enrich the data backing the Ontology.作为组织的“数字孪生”，本体支持数据写回和持续改进，通过记录组织内的决策作为数据。本体支持配置写回和动作类型 ，定义用户如何编辑和丰富支持本体的数据。


Capturing decision-making outcomes in the Ontology enables organizations to learn from and improve their decision-making. Data writeback also allows the value of the data asset to compound over time, as insights captured by one user can contribute to the decision-making of another user.在本体中捕捉决策结果使组织能够从中学习并改进决策。数据写回还允许数据资产的价值随着时间累积，因为一个用户捕获的洞察可以促进另一个用户的决策。


## [](#powering-operational-aiml)Powering operational AI/ML驱动运营 AI/ML


For data science and AI/ML teams, the Ontology enables collaboration with operational teams and others on a shared platform. Models (and their features) can be bound directly to the building blocks and processes that drive the organization. This allows models to be governed, released, and implemented directly into core applications and systems, without additional adapters or glue code, before being served in-platform (batch, streaming, or query-driven) or externally. As decisions are made and actions are taken, operational and process data are written back into the Ontology, creating a feedback loop that enables model monitoring, evaluation, re-training, and MLOps.对于数据科学和人工智能/机器学习团队，本体支持与运营团队及其他团队在共享平台上的协作。模型（及其特征）可以直接绑定到驱动组织的构建模块和流程。这使得模型能够被治理、发布并直接实现到核心应用和系统中，无需额外的适配器或胶合代码，然后再在平台内（批处理、流式或查询驱动）或外部提供。随着决策和行动的实施，运营和流程数据会被写回本体，形成反馈循环，支持模型监控、评估、再训练和 MLOps。


Foundry enables quick iteration towards outcomes. The Ontology and other best-in-class tooling make it easy to get started and deliver AI/ML-enabled operational outcomes, whether through new applications or by augmenting existing systems. Subsequent use cases can leverage interconnected datasets and model assets throughout the enterprise, decreasing time-to-value for new projects.Foundry 支持快速迭代以实现成果。本体论和其他一流的工具使得启动和实现人工智能/机器学习驱动的运营成果变得轻松，无论是通过新应用还是增强现有系统。后续的用例可以利用企业内互联的数据集和建模资产，缩短新项目的价值实现时间。


Learn more about [Models in the Ontology](/docs/foundry/ontology/models/).了解更多关于本体中的模型的信息。

