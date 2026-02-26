# [](#action-types)Action types动作类型


In the Ontology, users can make changes to objects, properties, and links by applying actions. An action is a single transaction that changes the properties of one or more objects, based on a user-defined logic. Actions enable users to handle and manage data while thinking about overall objectives instead of specific property edits.在本体中，用户可以通过应用动作对对象、属性和链接进行更改。动作是基于用户定义逻辑改变一个或多个对象属性的单一事务。作使用户能够在考虑整体目标而非具体属性编辑的同时处理和管理数据。


An **action type** is the definition of a set of changes or edits to objects, property values, and links that a user can take at once. It also includes the side effect behaviors that occur with action submission.动作类型是对对象、属性值和链接进行一组更改或编辑的定义，用户可以一次性处理这些内容。它还包括与行动服从相关的副作用行为。


**Example:**


You may create an `Assign Employee` action type that defines how users can change the `role` property value for a given `Employee` object. This action type could require a parameter definition enabling users to input the new role in a standardized form and can include rules for how to automatically create a link between the `Employee` object and that of a new `Manager`.你可以创建一个 “分配员工 ”动作类型，定义用户如何更改给定员工对象的角色属性值。该动作类型可能需要参数定义，使用户能够以标准化表单输入新角色，并包含如何自动创建员工对象与新经理对象之间的链接规则。


The action could also:该行动还可能：


- Include a notification side effect that will notify the old and new manager of the change.加入通知副作用，通知旧经理和新经理更改。
- Validate that authorized employees such as those working in human resources can perform the action.验证授权员工，如人力资源人员，能够执行该行动。


With these parameters set, an HR employee can then take an action to switch "Melissa Chang" to a "Product Manager" `role`, for example.设定好这些参数后，人力资源员工可以采取措施将“Melissa Chang”切换为“产品经理” 角色 。


Rather than being an abstract data model, the Foundry Ontology maps each ontological concept to an organization's actual data, enabling this data asset to power real-world applications. The data asset grows in richness and value as user decisions and insights are captured in the form of edits to the Ontology.Foundry 本体论不是抽象数据模型，而是将每个本体概念映射到组织的实际数据，使这些数据资产能够驱动现实应用。随着用户决策和洞察通过本体的编辑被捕捉，数据资产的丰富性和价值不断提升。


Any changes made to objects, property values, and links will be committed to the Ontology when the user takes the action and will be reflected in all user applications. Likewise, the same action logic and validations can be made available across all user-facing applications, ensuring consistent edits to the Ontology. The most up-to-date version of object data with user edits incorporated will be captured in an object type's writeback dataset.对对象、属性值和链接所做的任何更改，都会在用户执行作时提交到本体中，并反映在所有用户应用中。同样，所有面向用户的应用程序都可以提供相同的动作逻辑和验证，确保本体的编辑保持一致。包含用户编辑的对象数据最新版本将被捕获在对象类型的写回数据集中。


Get started by learning how to [create an action type](/docs/foundry/action-types/getting-started/), or learn about [rules](/docs/foundry/action-types/rules/), [parameters](/docs/foundry/action-types/parameter-overview/), and [submission criteria](/docs/foundry/action-types/submission-criteria/).从学习如何创建动作类型 ，或了解规则 、 参数和提交标准开始。

