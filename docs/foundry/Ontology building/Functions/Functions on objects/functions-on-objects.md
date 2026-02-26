# [](#functions-on-objects-foo)Functions on objects (FOO)对象上的函数（FOO）


Functions in Foundry natively support accessing and modifying data from objects and links in the Ontology. After defining object and link types in the Ontology, you can import these types into a functions repository to have code bindings automatically generated. These code bindings include support for:Foundry 原生支持访问和修改本体中对象和链接的数据。在本体中定义对象和链接类型后，您可以将这些类型导入函数库以自动生成代码绑定。这些代码绑定包括对以下功能的支持：


- Passing object and object set types into a function as [parameters](/docs/foundry/functions/types-reference/#ontology-types)将对象和对象集类型作为参数传递给函数
- Searching for object sets on demand using the [Object set APIs](/docs/foundry/functions/api-object-sets/)使用对象集 API 按需搜索对象集
- Modifying objects using [OntologyEditFunctions](/docs/foundry/functions/edits-overview/)使用 OntologyEditFunctions 修改对象


Because of this native support for the Ontology, functions in Foundry go far beyond commonly used Functions-as-a-Service (FaaS) platforms by providing native support for data storage, retrieval, and modification—all subject to Foundry's guarantees for data security, lineage, and transparency.由于对本体论的原生支持，Foundry 中的函数远超常见的函数即服务（FaaS）平台，它提供了对数据存储、检索和修改的原生支持——所有这些均受 Foundry 对数据安全、血缘关系和透明性的保证。


[Learn how to get started with functions on objects.](/docs/foundry/functions/foo-getting-started/)


The term "functions on objects" (sometimes referred to as "FOO") is used loosely to refer to functions that read object data, either as a parameter or using an object search, but there is no formal notion of a "function on objects" in Foundry as being distinct from any other function.术语“对象上的函数”（有时也称为“FOO”）被宽泛地用来指读取对象数据的函数，无论是作为参数还是使用对象搜索，但在 Foundry 中，并没有将“对象上的函数”作为一个与其他函数不同的正式概念。

