# [](#compute-usage-ontology-indexing)Compute usage: Ontology indexing计算使用：本体索引


Foundry’s Ontology stores objects in an Ontology index, a storage format optimized for rapid access. Data in Foundry datasets can be of any size or format, meaning a data transformation is required to prepare dataset data for storage in an Ontology index. This process is known as *Ontology indexing* and can be applied to datasets and objects of arbitrary size. The processing cost of Ontology indexing is measured compute-seconds. This documentation describes how Ontology indexing uses compute as well as how to manage compute usage.Foundry 的本体论将对象存储在本体索引中，这是一种优化以快速访问的存储格式。Foundry 数据集中的数据可以是任意大小或格式，这意味着为了准备数据集数据以存储在本体索引中，需要进行数据转换。这一过程称为本体索引， 可以应用于任意大小的数据集和对象。本体索引的处理成本以计算秒计量。本文档描述了本体索引如何使用计算以及如何管理计算使用情况。


## [](#measuring-compute-usage-from-ontology-indexing)Measuring compute usage from Ontology indexing从本体索引测量计算使用情况


Ontology Indexing uses a parallelized Spark backend to read arbitrarily large sets of data and transform them into the Ontology format. The amount of compute that is used to run an indexing job is based on the amount of computational resources (driver and executors) and the total wall-clock duration of the indexing job itself.本体索引使用并行化的 Spark 后端读取任意大量数据并转换成本体格式。用于运行索引作业的计算量取决于计算资源（驱动程序和执行者）以及索引作业本身的总时钟持续时间。


For more information on how Spark usage translates to compute-seconds, see the main [Usage Types](/docs/foundry/resource-management/usage-types/) documentation. Below, you can find [examples of the calculations for compute-seconds used by Ontology Indexing](#example-indexing-compute-calculation).关于 Spark 使用如何转化为计算秒的更多信息，请参阅主要的使用类型文档。下面，你可以找到 Ontology Indexing 用于计算秒的计算示例 。


## [](#investigating-usage-from-ontology-indexing)Investigating usage from Ontology Indexing从本体索引中研究使用情况


Ontology indexing jobs are exposed in Foundry’s Builds application and are attached to the object that is being indexed. Ontology indexing jobs are Spark jobs and so are classified as parallelized batch compute; thus, Ontology indexing jobs can be measured in the same way as other jobs on the same backend, such as Code Repositories transforms and Contour queries.本体索引作业在 Foundry 的 Builds 应用中公开，并附加到被索引的对象上。本体索引作业属于 Spark 作业，因此被归类为并行批处理计算;因此，本体索引作业可以与同一后端的其他作业一样进行测量，如代码仓库的变换和轮廓查询。


Indexing jobs can be categorized based on how they are triggered.索引工作可以根据触发方式进行分类。


- *Ontology indexing jobs* index datasets into the Ontology backend. This compute is used to produce indexed objects from datasets.本体索引工作将数据集索引到本体后端。这种计算用于从数据集中生成索引对象。
- *Ontology export jobs* persist edits made directly in the Ontology to datasets in the Foundry transformation framework. These jobs tend to be smaller than full indexing jobs as ontology export jobs are generally dealing with edits, which are strict subsets of the total object set.本体导出作业会将本体中直接编辑的编辑保存到 Foundry 转换框架中的数据集。这些作业通常比完整索引作业小，因为本体导出作业通常处理编辑，编辑是整体对象集中的严格子集。


## [](#drivers-of-usage-for-ontology-indexing)Drivers of usage for Ontology indexing本体索引使用的驱动因素


Ontology indexing jobs must read all of the data that needs to be indexed and transform it into a format that the Ontology backend can store, search, and edit quickly.本体索引作业必须读取所有需要索引的数据，并将其转换为本体后端能够快速存储、搜索和编辑的格式。


Compute usage when reading and indexing data is driven by the following factors:读取和索引数据时的计算使用受以下因素驱动：


- **Number of records per object每个对象的记录数量**
- The number of objects increases as the number of records in the dataset being indexed increases. Each object requires a certain number of computational operations for indexing, so increasing the number of objects increases the amount of compute used for indexing.对象数量随着被索引数据集中记录数量的增加而增加。每个对象索引都需要一定数量的计算作，因此对象数量增加，索引所需的计算量也会增加。
  - The number of objects increases as the number of records in the dataset being indexed increases. Each object requires a certain number of computational operations for indexing, so increasing the number of objects increases the amount of compute used for indexing.对象数量随着被索引数据集中记录数量的增加而增加。每个对象索引都需要一定数量的计算作，因此对象数量增加，索引所需的计算量也会增加。
  
  - **Number of properties per object每个对象的属性数量**
- Each property of each object must be individually analyzed by the indexing job and then written into the object index. More compute is used if there are more properties to analyze and index.索引作业必须对每个对象的每个属性进行单独分析，然后写入对象索引中。如果有更多属性需要分析和索引，计算量会更多。
  - Each property of each object must be individually analyzed by the indexing job and then written into the object index. More compute is used if there are more properties to analyze and index.索引作业必须对每个对象的每个属性进行单独分析，然后写入对象索引中。如果有更多属性需要分析和索引，计算量会更多。
  
  - **Size of each property各物业规模**
- Some properties are much larger than others. For instance, a text property containing a lot of content will require more space and compute to analyze than a simple number property. Objects with larger, more complex property types will require more compute to index.有些房产比其他的大得多。例如，包含大量内容的文本属性会比简单的数字属性需要更多的空间和计算量来分析。具有更大、更复杂属性类型的对象需要更多的计算来索引。
  - Some properties are much larger than others. For instance, a text property containing a lot of content will require more space and compute to analyze than a simple number property. Objects with larger, more complex property types will require more compute to index.有些房产比其他的大得多。例如，包含大量内容的文本属性会比简单的数字属性需要更多的空间和计算量来分析。具有更大、更复杂属性类型的对象需要更多的计算来索引。
  
  

Indexing frequency also plays a large role in how much compute is used for Ontology updates. Schedules set on upstream datasets will trigger auto-reindexes of objects. When examining the usage implications of keeping an object up-to-date, consider the update schedules on that object and its upstream datasets.索引频率也在本体更新中使用的计算量中起着重要作用。在上游数据集上设置的调度会触发对象的自动重新索引。在评估保持对象更新的使用影响时，考虑该对象及其上游数据集的更新计划。


## [](#managing-ontology-indexing-compute)Managing Ontology indexing compute管理本体索引计算


Ontology indexing jobs can be optimized to reduce compute usage. The first and simplest method of optimization is to reduce the size of the input data for the index, which decreases the amount of work needed to complete the job. This involves doing the following where possible:本体索引作业可以优化以减少计算使用。第一种也是最简单的优化方法是减少索引输入数据的大小，从而减少完成工作所需的工作量。这包括尽可能做以下几件事：


- Managing the number of input records管理输入记录数量
- Managing the number of properties per object管理每个对象的属性数量
- Managing the size of each property per object管理每个对象属性的大小


Another optimization method is configuring Ontology index jobs to use changelog strategies for indexing. Changelog indexing significantly reduces the number of objects that need to be created or updated per indexing job by comparing the job against existing objects prior to execution. Changelog indexing requires more configuration and adherence to an update strategy, but can produce orders-of-magnitude performance and efficiency gains.另一种优化方法是配置本体索引作业，使其使用变更日志策略进行索引。变更日志索引通过在执行前将作业与现有对象进行比较，显著减少了每个索引作业需要创建或更新的对象数量。变更日志索引需要更多的配置和遵循更新策略，但能带来数量级的性能和效率提升。


## [](#example-indexing-compute-calculation)Example indexing compute calculation示例索引计算计算


Indexing jobs take the form of parallelized Spark jobs and can be seen in the Builds application. See the following example for an indexing job. Note that Ontology indexing jobs will automatically choose the size of the driver and executors for the indexing job, depending on the size of the job.


```
`Driver:
    num_vcpu: 1
    GiB_RAM: 6
Executors:
    num_vcpu: 1
    GiB_RAM: 4
    num_executors: 2
Total Runtime: 10 seconds

Calculation: 

driver_compute_seconds = max(num_vcpu, GiB_RAM / 7.5) * runtime_in_seconds
                       = max(1vcpu, 6GiB / 7.5) * 10sec
                       = 1 * 10 = 10 compute-seconds

executor_compute_seconds = max(num_vcpu, GiB_RAM / 7.5) * num_executors * runtime_in_seconds
                         = max(1vcpu, 4GiB / 7.5) * 2executors * 10sec
                         = 1 * 2 * 10 = 20 compute-seconds

total_compute_seconds = driver_commpute_seconds + exeucutor_compute_seconds
                      = 10 compute-seconds + 20 compute-seconds
                      = 30 compute-seconds

`
```

