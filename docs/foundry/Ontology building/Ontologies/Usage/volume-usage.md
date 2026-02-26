# [](#ontology-volume-usage)Ontology volume usage本体卷的使用


Foundry’s Ontology is a fast-access storage layer that allows you to bind object definitions to interactive data for queries, links, scenarios, and actions. Data in the Foundry Ontology is indexed for fast access and for safe edits by multiple simultaneous editors. Ontology volume is a measure of the total size of the indexed object sets and their links with each other. Ontology volume is an average metric that has the unit of GB for an instantaneous reading, but has the unit of GB-Month when measuring over the course of one month.Foundry 的本体论是一个快速访问的存储层，允许你将对象定义绑定到查询、链接、场景和动作的交互数据上。Foundry 本体中的数据被索引，以便多个同时编辑者快速访问并安全编辑。本体体积是衡量索引对象集及其相互关联总规模的指标。本体体积是一个平均指标，单位为 GB，表示瞬时读数，但在一个月内测量时单位为 GB-月。


## [](#measuring-ontology-volume)Measuring Ontology volume本体体积的测量


Ontology volume is recorded by measuring the size of the indexes that back the object type. Each object type has a number of objects and a number of properties per object. Each property can be of arbitrary size. The total size of the index is calculated by summing the size of each indexed property for every object of that object type.本体体积是通过测量支持对象类型的索引大小来记录的。每种对象类型都有若干对象和每个对象的属性。每个属性的大小可以是任意的。索引的总大小是通过对该对象类型中每个索引属性的大小相加计算得出的。


It’s important to note that Ontology volume can be larger than dataset volume because Ontology data cannot be compressed, and Ontology indexing requires additional storage to facilitate faster queries.需要注意的是，本体量可能大于数据集体积，因为本体数据无法被压缩，而本体索引需要额外的存储以促进更快的查询。


Every hour, the Foundry platform records a measurement of Ontology volume per object. When measuring Ontology volume over time, all hourly measurements are averaged over the given time period. Averaging over the course of one calendar month produces the *GB-Month* unit.每小时，Foundry 平台会记录每个对象的本体体积测量值。在测量本体体积随时间变化时，所有小时测量均在给定时间段内进行平均。在一个日历月内平均计算即可得到 GB-Month 单位。


## [](#investigating-ontology-volume-usage)Investigating Ontology volume usage本体卷的使用研究


Objects are managed in the Ontology Manager, the hub for all administration and monitoring of objects. The Ontology Manager allows users to configure which datasets should become objects, what types of properties are attached to these objects, and which link sets are defined between object types.对象由本体管理器管理，该管理中心是所有对象管理和监控的中心。本体管理器允许用户配置哪些数据集应成为对象，这些对象附加哪些属性类型，以及对象类型之间定义哪些链接集。


The total Ontology volume for objects and their corresponding link types are listed in the Resource Management Application.对象及其对应链路类型的总本体体积列于资源管理应用中。


## [](#factors-that-drive-ontology-volume)Factors that drive Ontology volume驱动本体体积的因素


Ontology volume is effectively a measure of the size of all objects in the ontology, including their properties and links. The following two factors are the main drivers of total volume.本体体积实际上是衡量本体中所有对象大小的指标，包括它们的属性和链接。以下两个因素是推动总成交量的主要因素。


- **The number and size of objects per object type每个对象类型的对象数量和大小**
- When creating an ontology object type out of a dataset, an object will be indexed per row of that dataset. Therefore, the number of rows in that dataset is tied 1:1 to the number of objects in the corresponding object type.当从数据集创建本体对象类型时，每个数据集的每一行都会索引一个对象。因此，该数据集中的行数与对应对象类型的对象数量成1：1的关联。
- Additionally, datasets that have more columns or that contain more data (e.g. free text fields) can produce individual objects that are larger, because each column is turned into a property.此外，列数更多或包含数据更多（如自由文本字段）的数据集，可以生成更大的单个对象，因为每列都被转化为属性。
  - When creating an ontology object type out of a dataset, an object will be indexed per row of that dataset. Therefore, the number of rows in that dataset is tied 1:1 to the number of objects in the corresponding object type.当从数据集创建本体对象类型时，每个数据集的每一行都会索引一个对象。因此，该数据集中的行数与对应对象类型的对象数量成1：1的关联。
  - Additionally, datasets that have more columns or that contain more data (e.g. free text fields) can produce individual objects that are larger, because each column is turned into a property.此外，列数更多或包含数据更多（如自由文本字段）的数据集，可以生成更大的单个对象，因为每列都被转化为属性。
  
  - **The number of links between objects when using join tables使用连接表时对象之间的链接数量**
- In many-to-many relationships, the Ontology requires the definition of a join table to define all of the links between objects based on their primary keys. These tables are indexed alongside the objects in the Ontology and use ontology volume.在多对多关系中，本体论要求定义连接表，以根据对象的主键定义所有连接。这些表与本体论中的对象并列索引，并使用本体卷。
- In general, look-up tables have a constant size per record and grow linearly in volume with the number of links that are defined.一般来说，查找表每条记录大小恒定，且随着定义的链接数量线性增长。
  - In many-to-many relationships, the Ontology requires the definition of a join table to define all of the links between objects based on their primary keys. These tables are indexed alongside the objects in the Ontology and use ontology volume.在多对多关系中，本体论要求定义连接表，以根据对象的主键定义所有连接。这些表与本体论中的对象并列索引，并使用本体卷。
  - In general, look-up tables have a constant size per record and grow linearly in volume with the number of links that are defined.一般来说，查找表每条记录大小恒定，且随着定义的链接数量线性增长。
  
  

## [](#managing-ontology-volume)Managing Ontology volume管理本体体积


The Ontology is designed to be a fast-access backend for operational usage and querying. In the general case, the Ontology is best used with highly refined data that is synthesized from a larger data asset. The volume of the Ontology should therefore be smaller than the total raw and intermediate data size in Foundry’s transformation framework.本体旨在作为快速访问的后端，用于作使用和查询。一般情况下，本体最好用于从更大数据资产合成的高度精炼数据。因此，本体论的体积应小于 Foundry 转换框架中的原始和中间数据总量。


To manage Ontology volume usage, pay attention to the number of object types that are defined in the Ontology, as well as the number of objects per object type and the number of properties per object. Overall, the best way to manage Ontology volume usage is to understand and deliberately manage object numbers, property counts, and property sizes.管理本体卷使用时，请注意本体中定义的对象类型数量，以及每个对象类型和每个对象属性的数量。总体而言，管理本体卷使用的最佳方法是理解并有意识地管理对象编号、属性数量和属性大小。

