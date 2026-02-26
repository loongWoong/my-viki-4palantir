# [](#link-types)Link types链接类型


A **link type** is the schema definition of a relationship between two object types. A **link** refers to a single instance of that relationship between two objects in the same Ontology.链接类型是两种对象类型之间关系的模式定义。 链接指的是同一本体中两个对象之间这种关系的单一实例。


For example, in the Ontology Manager, you may create a link type between the `Employee` object type and the `Company` object type that defines the relationship between `Employee` and `Employer`. A link refers to a single instance of the `Employee → Employer` link type, like the relationship between the notional employee “Melissa Chang” and her employer, “Acme, Inc.”例如，在 Ontology Manager 中，你可以创建 Employee 对象类型与公司对象类型之间的链接类型，定义 Employee 与 Employer 之间的关系。链接指的是员工 →雇主链接类型的单一实例，比如名义上的员工“Melissa Chang”与其雇主“Acme， Inc.”之间的关系。


Similarly, in the Ontology Manager, you may create a link type between the `Flight` object type and the `Aircraft` object type that defines the relationship between `Scheduled Flight` and `Assigned Aircraft`. A link refers to a single instance of the `Scheduled Flight → Assigned Aircraft` link type, like the relationship between “JFK → SFO 24-02-2021” and its assigned aircraft “Boeing 737-123”.同样，在本体管理器中，你可以创建航班对象类型与飞机对象类型之间的链接类型，定义定期航班与指定飞机之间的关系。链接指的是该 Scheduled Flight → Assigned Aircraft 链接类型的单一实例，比如“JFK → SFO 24-02-2021”与其分配的飞机“波音 737-123”之间的关系。


Links can also exist between two objects of the same type. A link type `Direct Report ↔ Manager` can be defined between the `Employee` object type and itself.两个同类型的对象之间也可能存在链接。可以在员工对象类型与自身之间定义链接类型直接报告↔管理器 。


Note that links between object types across different Ontologies is not supported. In this case, you may prefer to leverage a shared Ontology.注意，不支持跨不同本体的对象类型之间的链接。在这种情况下，你可能更倾向于利用共享本体。


The concepts underpinning the Ontology have analogous concepts in the structure of a dataset. The definition of a link type in the Ontology is analogous to that of a join between two datasets, while the definition of a link is analogous to that of a row joined with the fields of the same row in another dataset. For example, you can join the `Employee` dataset with the `Company` dataset to explore the relationship between `Employees` and their `Employers`. In the joined dataset, a single row that joins “Melissa Chang” with her employer “Acme, Inc.” represents a link.支撑本体论的概念在数据集结构中也有类似的概念。本体中链接类型的定义类似于两个数据集之间的连接，而链接的定义类似于与另一数据集中同一行字段连接的行为。例如，你可以将员工数据集与公司数据集合并，以探索员工与雇主之间的关系。在连接的数据集中，一行将“Melissa Chang”与其雇主“Acme， Inc.”连接起来，代表一个链接。


Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. Links are created and displayed in user applications by adding backing datasources to the object types referred to in the link type in the Ontology Manager. In the case of link types where object types are related with a many-to-many cardinality, datasources back the link types themselves. To create links of type `Employee → Employer`, an organization will add backing datasources to the `Employee` and `Company` object types and connect their employee directory and other enterprise data into the Ontology.Foundry 本体论不是抽象数据模型，而是将每个本体概念映射到组织的实际数据，使这些数据资产能够驱动现实应用。链接通过在本体管理器中链接类型中为相关对象类型添加后备数据源来创建和显示。对于对象类型与多对多基数相关联的链路类型，数据源支持链路类型本身。为了创建“ 员工”→“雇主 ”类型的链接，组织会为员工和公司对象类型添加支持数据源，并将员工目录及其他企业数据连接到本体中。


Get started by learning how to [create a new link type](/docs/foundry/object-link-types/create-link-type/).从学习如何创建新的链接类型开始。

