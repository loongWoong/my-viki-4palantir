# [](#compute-usage-with-ontology-queries)Compute usage with Ontology queries利用本体查询计算使用情况


The Foundry Ontology is a data backend that maps file-based data to organization-centric objects and serves high-speed queries for data exploration, data analysis, operational data editing, scenario analysis, and more. The Ontology stores data in multi-modal storage backends that each have their own purposes and can be flexibly queried in a single request. Querying the Foundry Ontology requires knowledge of some foundational concepts discussed below.Foundry 本体是一个数据后端，将基于文件的数据映射到组织中心的对象，并提供高速查询，用于数据探索、数据分析、作性数据编辑、场景分析等。本体将数据存储在多模态存储后端，每个后端都有其用途，并且可以在一次请求中灵活地查询。查询 Foundry 本体需要了解下面讨论的一些基础概念。


If you have an enterprise contract with Palantir, contact your Palantir representative before proceeding with compute usage calculations.如果您与 Palantir 签有企业合同，请在开始计算用量前联系您的 Palantir 代表。


## [](#core-concepts-object-types-and-object-sets)Core concepts: Object types and object sets核心概念：对象类型与对象集


The first important concept is the difference between an **object type** and its corresponding **object set**. An **object type** is the semantic representation of the entity itself (such as the name and properties of the object).第一个重要概念是对象类型与其对应对象集之间的区别。 对象类型是实体本身的语义表示（例如对象的名称和属性）。


An object type has a corresponding **object set**, which contains the objects themselves. The size of the **object set** corresponds to the number of rows of the incoming dataset and the number of objects created and deleted by Ontology actions.一个对象类型有一个对应的对象集 ，包含了这些对象本身。 对象集的大小对应于新来数据集的行数以及本体作创建和删除对象的数量。


## [](#core-concept-query-types)Core concept: Query types核心概念：查询类型


The second important concept is the idea of **query types**, which include filters, aggregations, Search Arounds, and writeback operations. Each query type requires compute to execute.第二个重要概念是查询类型的概念，包括筛选、聚合、搜索环节和写回作。每种查询类型都需要计算才能执行。


- Filters will consider a full object set and apply a filtering criteria to produce a smaller output set.过滤器会考虑完整的对象集，并应用过滤条件来生成更小的输出集。
- Aggregations will take an input object set and run an aggregating function (such as `sum` or `avg`) on one of the properties for all objects in the set.聚合会对输入对象集运行聚合函数（如求和或平均值）处理该集合中所有对象的某个属性。
- Search Arounds will take an incoming object set and run a secondary filter on another object set based on a certain property of the incoming set.搜索环绕会根据一个入来的对象集合，对另一个对象集合运行次级过滤器，基于该集合的某个属性。
- Writeback operations will replace the values of properties of objects in a designated object set.写回作将替换指定对象集中对象属性的值。


[View the API documentation to learn more about query types.查看 API 文档以了解更多关于查询类型的信息。](/docs/foundry/api/ontology-resources/objects/aggregate)


When using the Foundry Ontology, **query types** are executed against **object sets** by the following [Foundry Applications](/docs/foundry/ontology/applications/):使用 Foundry 本体时， 查询类型由以下 Foundry 应用程序针对对象集执行：


- Object Explorer对象浏览器
- Workshop车间
- Quiver箭袋
- Slate板岩
- Vertex顶点
- Foundry Rules铸造厂规则
- Foundry Machinery铸造机械
- Object APIs (OPIs)对象 API（OPI）


Querying the ontology from any of these sources will use compute-seconds to run the query, as follows:从任一来源查询本体时，运行查询的时间将为计算秒，具体如下：


- A fixed, minimum number of compute-seconds for query overhead.一个固定的、最小的查询开销计算秒数。
- An additional scaling number of compute-seconds, which are measured by the amount of compute used to service the query.额外的计算秒数，通过用于查询的计算量来衡量。


## [](#measuring-foundry-compute-with-ontology-object-queries)Measuring Foundry compute with Ontology object queriesMeasuring Foundry 计算与本体对象查询


### [](#measuring-compute-with-object-storage-v1)Measuring compute with Object Storage V1使用对象存储 V1 测量计算


Object Storage V1 (Phonograph) stores data in a distributed set of indices in a durable, horizontally scalable cluster. In these indices, data sits in large data structures that are traversed by the Ontology query engine. When a query is executed, the engine can avoid processing large swaths of data during its search by traversing the index. This process is known as "pruning".对象存储 V1（留声机）将数据存储在分布式索引集合中，集成为一个持久且可水平扩展的集群。在这些索引中，数据存在于由本体查询引擎遍历的大型数据结构中。当查询执行时，引擎可以通过遍历索引来避免在搜索过程中处理大量数据。这一过程被称为“修剪”。


Using this engine, you can search through billions of records by evaluating up to 1000x fewer records. Each physical evaluation of a record is called a "hit". Object Storage V1 is designed to minimize the number of hits in each query.使用这个引擎，你可以通过评估多达 1000 倍的记录，搜索数十亿条记录。对一张唱片的每次物理评估都称为“安打”。对象存储 V1 旨在最小化每个查询的命中次数。


### [](#measuring-compute-with-object-storage-v2)Measuring compute with Object Storage V2使用对象存储 V2 进行计算测量


Object Storage V2 (OSv2) stores objects in an enhanced indexing format that is optimized by Palantir for high-speed indexing, Search Arounds, and writeback, as well as smooth hand-offs to multiple compute backends to accomplish complex tasks. This includes a combination of fully parallelized Spark compute as a part of a query.对象存储 V2（OSv2）以增强型索引格式存储对象，经过 Palantir 优化，支持高速索引、搜索环和写回，同时实现对多个计算后端的平滑切换以完成复杂任务。这包括将完全并行化的 Spark 计算结合在查询中。


Given that Object Storage V2 also uses an efficient indexing structure, the same principle of **hits** from Object Storage V1 applies on basic queries. However, compute-seconds can also be used by on-demand Spark containers that are spun up as a part of the query.鉴于对象存储 V2 也采用高效的索引结构，基本查询同样适用对象存储 V1  的命中原则。然而，按需 Spark 容器也可以利用计算秒，这些容器作为查询的一部分被启动。


Queries made to objects in the Object Storage V2 backend use compute in the following pattern:在对象存储 V2 后端对对象进行的查询计算模式如下：


- A fixed compute-second overhead of `16` compute-seconds per query for objects in the Object Storage V1 backend.在 Object Storage V1 后端，每个查询固定计算秒开销为 16 秒。
- A fixed compute-second overhead of `4` compute-seconds per query for objects in the Object Storage V2 backend. The optimized structure of Object Storage V2 requires less overhead than Object Storage V1 and therefore has a reduced fixed compute-second overhead.对象存储 V2 后端的对象每次查询固定计算秒开销为 4 秒。对象存储 V2 的优化结构比对象存储 V1 需要更少开销，因此固定的计算秒开销更低。
- Additional compute-seconds are required when the process does computational work through the pruning process of the query. The additional compute-seconds scale with the number of objects in the index as well as the type of query.当进程通过查询的剪枝过程进行计算工作时，需要额外的计算秒。额外的计算秒数会随着索引中对象数量和查询类型而增加。
- In Object Storage V2 (OSv2), the index pruning similarly requires additional compute seconds. However, OSv2 supports also on-demand Spark cluster searches when running search-arounds on over 100,000 objects, or running writeback operations on over 10,000 objects in a single request. These Spark clusters utilize usage in the same way as all other Spark-based applications on the platform. See the [parallelized compute documentation](/docs/foundry/resource-management/usage-types/) for a description.在对象存储 V2（OSv2）中，索引修剪同样需要额外的计算秒。然而，OSv2 也支持在对超过 100,000 个对象进行搜索绕行，或在单次请求中对超过 10,000 个对象执行写回作时，按需进行 Spark 集群搜索。这些 Spark 集群的使用方式与平台上所有其他基于 Spark 的应用相同。详见并行计算文档中的描述。
- Actions with write-back into the Ontology have a minimum overhead. Each action has a compute-second overhead of `18`. Actions also scale with the number of objects that are edited in the write-back request, incurring an additional `1` compute-second per object edited beyond the first.带有写回本体的动作开销最小。每个动作的计算秒开销为 18。动作还会随写回请求中被编辑的对象数量而增加，每编辑一个超过第一个对象，计算时间会增加 1 秒。
- Functions run via Functions on Objects have a minimum overhead. Specifically, each function execution has a fixed overhead of `4` compute-seconds.通过对象上的函数运行的函数开销最小。具体来说，每个函数执行的开销固定为 4 个计算秒。


**The following table summarizes the minimum compute-second usage per query type.下表总结了每种查询类型的最小计算秒使用时间。**



























| Query Type查询类型 | minimum compute-seconds最小计算秒 |
| --- | --- |
| Ontology V1 Query本体论 V1 查询 | 16 |
| Ontology V2 Query本体论 V2 查询 | 4 |
| Action on Objects对物体的作用 | 18 |
| Function on Objects对象功能 | 4 |


## [](#understanding-drivers-of-foundry-compute-usage-with-ontology-queries)Understanding drivers of Foundry compute usage with Ontology queries理解 Foundry 计算使用本体查询的驱动因素


- As a very simple rule, the fixed compute-usage per query grows linearly with the number of queries. Performing fewer queries will use less compute in aggregate.一个非常简单的规则是，每次查询的固定计算使用量会随着查询次数的增加线性增长。执行更少的查询会在总量内消耗更少的计算量。
- More complex queries to the object set service, such as generic multi-object searches, will kick off multiple sub-queries to each object type. Limit your search to individual object types to reduce the number of queries you are using.对对象集服务的更复杂查询，如通用多对象搜索，会触发多个子查询到每个对象类型。将搜索限制在单个对象类型中，以减少查询数量。
- Queries on smaller object sets will use less compute than those on larger object sets, as the number of **hits** in a query are proportional to the size of the object set being queried.对较小对象集的查询比大对象集的查询消耗的计算更少，因为查询中的命中次数与被查询对象集的大小成正比。
- Up-front filtering before performing other operations will take advantage of the highly indexed backend structure. This will reduce the number of **hits** in a query, reducing the overall compute usage. This is especially important with aggregations and Search Arounds, where filtered object sets use require less compute to process than full object sets.在执行其他作前进行前期过滤将利用高度索引化的后端结构。这将减少查询中的命中次数，从而降低整体计算使用。这在聚合和搜索环节尤为重要，因为过滤对象集的处理比完整对象集需要更少的计算量。


## [](#investigating-foundry-compute-usage-from-ontology-queries)Investigating Foundry compute usage from Ontology queries从本体查询中研究 Foundry 计算的使用


In Foundry, compute-seconds are attributed to resources in the platform rather than to the users that are interacting with those resources.在 Foundry 中，计算秒数归属于平台上的资源，而非与这些资源交互的用户。


When it comes to Ontology queries, there are multiple ways in which compute is attributed. As a general rule, the compute is attached to the resource where the query originated. However, when there is no saved resource that is used to generate the compute (such as via API), the compute will be attached to the object type(s) that are being queried. If multiple objects are queried in a single request, then the compute is attributed via an even split between the objects.关于本体查询，计算的归属方式有多种。一般来说，计算会附加到查询起源的资源上。然而，当没有用于生成计算的已保存资源（如通过 API 时），计算将附加到查询对象类型上。如果单个请求中查询多个对象，则计算通过在对象间均匀分配来归属。


The following resource types have Ontology query compute attributed to them, rather than the underlying objects:以下资源类型赋予了本体查询计算，而非底层对象：


- Workshop Applications研讨会应用
- Carbon Pages碳页
- Quiver Analyses and DashboardsQuiver 分析与仪表盘
- Vertex Applications顶点应用
- Slate Applications板岩应用
- Foundry Machinery Applications铸造机械应用
- Foundry Rules Resources铸币厂规则资源
- Foundry Automate铸造自动化
- AIP LogicAIP 逻辑
- SQL Console WorksheetsSQL 控制台工作表


The following interaction patterns have their Ontology query compute attached directly to the object types that they query, given there is no set resource to which the compute can be attached.以下交互模式的本体查询计算直接附加到所查询的对象类型上，前提是计算没有固定资源可供附加。


- Object Explorer对象浏览器
- Object APIs (including the OSDK)对象 API（包括 OSDK）


## [](#related-resources)Related resources相关资源


For best practices on writing efficient functions and Automate configurations that minimize compute usage:关于编写高效函数和自动化配置以最小化计算使用的最佳实践：


- [Optimize function performance优化功能性能](/docs/foundry/functions/optimize-performance/)
- [Automate performance best practices自动化性能最佳实践](/docs/foundry/automate/performance-best-practices/)

