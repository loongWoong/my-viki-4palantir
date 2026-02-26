# [](#object-types)Object types对象类型


An **object type** is the schema definition of a real-world entity or event.
An **object or object instance** refers to a single instance of an object type; an object corresponds to a single real-world entity or event.
An **object set** refers to a collection of multiple object instances; that is, an object set represents a group of real-world entities or events.对象类型是现实世界实体或事件的模式定义。 对象或对象实例指的是一个对象类型的单个实例;一个对象对应于一个现实世界的单一实体或事件。 对象集指的是多个对象实例的集合;也就是说，一个对象集代表一组现实世界的实体或事件。


For example, in the Ontology Manager, you may create an `Employee` object type that defines the characteristics for “All employees” or all objects of that type. An object refers to a single instance of the `Employee` object type, like the notional employees “Melissa Chang”, “Akriti Patel”, or “Diego Rodriguez.” A group of objects like “All tenured employees” represents an object set.例如，在本体管理器中，你可以创建一个员工对象类型，定义“所有员工”或该类型所有对象的特征。对象指的是员工对象类型的单个实例，比如名义上的员工“Melissa Chang”、“Akriti Patel”或“Diego Rodriguez”。一组对象，比如“所有有终身职的员工”，代表一个对象集。


Similarly, in the Ontology Manager, you may create a `Flight` object type that defines characteristics for “All flights” or all objects of that type. An object refers to a single instance of the `Flight` object type, like “JFK → SFO 2021-02-24” or “TLV → LHR 2020-04-16.” A group of objects like “All arrived flights” represents an object set.同样，在本体管理器中，你可以创建一个飞行对象类型，定义“所有飞行”或该类型所有对象的特征。对象指的是飞行对象类型的单个实例，比如“JFK → SFO 2021-02-24”或“TLV → LHR 2020-04-16”。一组对象，比如“所有到达航班”表示一个对象集合。


The concepts underpinning the Ontology have analogous concepts in the structure of a dataset. The definition of an object type in the Ontology is analogous to that of a dataset, while the definition of an object is analogous to that of a row in the dataset. The definition of an object set is analogous to a filtered set of rows in a dataset. For example, an `Employee` dataset may define the schema for “All employee rows.” In this case, a single row refers to a single employee, like “Melissa Chang,” “Akriti Patel,” or “Diego Rodriguez." If you filter the dataset based on tenure, you will have a set of rows that represent “All tenured employees.”支撑本体论的概念在数据集结构中也有类似的概念。本体论中对象类型的定义类似于数据集的定义，而对象的定义类似于数据集中的行。对象集的定义类似于数据集中过滤过的行集合。例如， 员工数据集可能定义“所有员工行”的模式。在这种情况下，单一行指的是单个员工，比如“Melissa Chang”、“Akriti Patel”或“Diego Rodriguez”。如果你根据资历筛选数据集，会得到一组表示“所有有资历员工”的行。


Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. Objects are created and displayed in user applications by adding backing datasources to an object type in the Ontology Manager. To create objects of type `Employee`, an organization will add backing datasources to the `Employee` object type and connect their employee directory and other enterprise data into the Ontology.Foundry 本体论不是抽象数据模型，而是将每个本体概念映射到组织的实际数据，使这些数据资产能够驱动现实应用。通过在 Ontology Manager 中的对象类型中添加后备数据源，在用户应用中创建和显示对象。要创建 Employee 类型的对象，组织会将备份数据源添加到 Employee 对象类型，并将员工目录及其他企业数据连接到本体中。


Get started by learning how to [create an object type](/docs/foundry/object-link-types/create-object-type/).先学会创建对象类型 。

