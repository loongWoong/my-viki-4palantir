![Ontology overview header image.](3-Ontology.png)

gaileyix
# [](#ontology-building)Ontology building本体构建


The Palantir **Ontology** is an operational layer for the organization. The Ontology sits on top of the digital assets integrated into the Palantir platform ([datasets](/docs/foundry/data-integration/datasets/), [virtual tables](/docs/foundry/data-integration/virtual-tables/), and [models](/docs/foundry/integrate-models/integrate-overview/)) and connects them to their real-world counterparts, ranging from physical assets like plants, equipment, and products to concepts like customer orders or financial transactions. In many settings, the Ontology serves as a digital twin of the organization, containing both the semantic elements (objects, properties, links) and kinetic elements (actions, functions, dynamic security) needed to enable use cases of all types.Palantir  本体是该组织的一个运营层。本体建立在集成于 Palantir 平台中的数字资产（数据集 、 虚拟表格和模型 ）之上，并将其与现实世界的对应物连接起来，从工厂、设备和产品等物理资产到客户订单或金融交易等概念。在许多环境中，本体作为组织的数字孪生，包含实现各种用例所需的语义元素（对象、属性、链接）和动力元素（动作、函数、动态安全）。


## [](#object-and-link-types)Object and link types对象和链接类型


Defining the semantics of your organization happens by mapping existing datasources into **objects, properties, and links** in the Ontology. Far beyond data cataloging or schema design solutions, the Ontology allows you to define a robust foundation for end-user workflows, including rich metadata for all fields and complete with granular security and governance for all changes.定义组织语义是通过将现有数据源映射为对象、属性和本体中的链接来实现的。远不止数据编目或模式设计解决方案，本体还允许你为终端用户工作流定义坚实的基础，包括所有字段的丰富元数据，并为所有变更提供细致的安全和治理。


Learn about creating the semantic elements of the Ontology: [object types](/docs/foundry/object-link-types/object-types-overview/) and [link types](/docs/foundry/object-link-types/link-types-overview/).学习如何创建本体论的语义元素： 对象类型和链接类型 。


## [](#action-types-and-functions)Action types and functions动作类型与功能


The kinetics of the organization—enabling change while complying with organizational controls and governance—are defined in the Ontology using **action types** and **functions**. Action types enable you to capture data from operators in your organization or orchestrate decision-making processes that connect to your existing systems, while functions provide a way to author and evolve business logic with arbitrary complexity.组织的动力学——在遵守组织控制和治理的同时实现变革——在本体中通过动作类型和功能进行了定义。动作类型使你能够从组织中的那里获取数据，或协调与现有系统连接的决策流程，而功能则提供了一种编写和演进任意复杂度的业务逻辑的方式。


Learn about creating the kinetic elements of the Ontology: [action types](/docs/foundry/action-types/overview/) and [functions](/docs/foundry/functions/overview/).学习如何创建本体论中的动力元素： 动作类型和功能 。


## [](#interfaces)Interfaces接口


An **interface** is an Ontology type that describes the shape of an object type and its capabilities. Interfaces provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape.接口是一种本体类型，用于描述对象类型的形状及其功能。接口提供对象类型多态性，使得对共享相同形状的对象类型进行一致建模和交互。


Learn more about [interfaces](/docs/foundry/interfaces/interface-overview/).了解更多关于接口的信息 。


## [](#powering-decision-making)Powering decision-making决策驱动


The goal of investing in the Ontology is to facilitate better decision-making in an organization at scale. To achieve this, the Ontology is deeply integrated into Palantir's user-facing analytical and operational tools: users can create reusable Object Views, search for objects of interest in Object Explorer, perform complex analyses in Quiver, build high-quality applications in Workshop, and more.投资本体论的目标是促进组织规模化的更好决策。为此，本体深度集成到 Palantir 面向用户的分析和作工具中：用户可以创建可复用的对象视图，在对象探索器中搜索感兴趣的对象，在 Quiver 中执行复杂分析，在 Workshop 中构建高质量应用，等等。


[Learn more about how to leverage the Ontology in user-facing applications.了解更多关于如何在面向用户的应用中利用本体论的信息。](/docs/foundry/ontology/applications/)


Palantir Learning portalPalantir 学习门户Now that you know the theory, get started on building your first Ontology with our course on [learn.palantir.com ↗](http://learn.palantir.com/deep-dive-creating-your-first-ontology).既然你已经了解了理论，就开始通过我们的课程构建你的第一个本体论 learn.palantir.com ↗。

