# [](#ontologies)Ontologies本体论


An ontology is an artifact which stores ontological resources or entities, including the following:本体论是一种产物，用于存储本体资源或实体，包括以下内容：


- [Object types对象类型](/docs/foundry/object-link-types/object-types-overview/)
- [Link types链接类型](/docs/foundry/object-link-types/link-types-overview/)
- [Action types动作类型](/docs/foundry/action-types/overview/)
- [Interfaces接口](/docs/foundry/interfaces/interface-overview/)
- [Shared properties共享财产](/docs/foundry/object-link-types/shared-property-overview/)
- [Object type groups对象类型组](/docs/foundry/object-link-types/type-groups/)


We call these resources **Ontology resources**. An ontology can either be private and assigned to a single [organization](/docs/foundry/security/orgs-and-spaces/) or shared among multiple organizations. Shared ontologies allow users of different organizations to share data and workflows safely. Grouping entities in ontologies ensures that only users of the specified organizations can access ontological entities.我们称这些资源为本体资源 。本体可以是私有的并分配给单一组织 ，也可以在多个组织之间共享。共享本体允许不同组织的用户安全地共享数据和工作流程。在本体中分组实体确保只有指定组织的用户才能访问本体实体。


## [](#relation-with-spaces)Relation with spaces与空间的关系


An ontology is mapped 1:1 with a [space](/docs/foundry/security/orgs-and-spaces/#spaces). When a new space is created, a corresponding ontology with the same name is simultaneously created with the same organization [markings](/docs/foundry/security/markings/) as the space. A private space will map to a private ontology, while a shared space will map to a shared ontology.本体与一个空间以 1：1 的映射方式。当创建新空间时，会同时创建一个同名的对应本体，并带有与该空间相同的组织标记 。私有空间映射到私有本体，而共享空间映射到共享本体。

