# [](#mandatory-control-properties)Mandatory control properties强制控制属性


Mandatory control properties are object type properties that allow for granular access control to the data stored in objects. You can use mandatory control properties to restrict access to all other properties in the same datasource for a given object, making those properties viewable only by users who satisfy the mandatory controls.强制控制属性是对象类型属性，允许对存储在对象中的数据进行细粒度访问控制。你可以使用强制控制属性来限制对同一数据源中对同一对象的所有其他属性的访问，使这些属性仅能被满足强制控制的用户查看。


**Note:** Mandatory control properties are **only available on Object Storage V2**.注： 强制控制属性仅在对象存储 V2 上可用 。


## [](#how-to-use-mandatory-control-properties)How to use mandatory control properties如何使用强制控制属性


1. First, create your marking-backed restricted view (RV). Learn more about [creating marking-backed restricted views](/docs/foundry/security/restricted-views/#create-marking-backed-restricted-views).首先，创建带有标记的受限视图（RV）。了解更多关于创建带标记的受限视图的方法。
2. Navigate to the Ontology Manager.导航到本体管理器。
3. Choose the object type for which you want to restrict property access, then create or select the property you want to set as a mandatory control property.选择你想限制属性访问的对象类型，然后创建或选择你想设置为强制控制属性的属性。
4. On the property sidebar, ensure the property is mapped to the corresponding **marking column** on your restricted view.在属性侧边栏，确保该属性映射到你受限视图中的对应标记栏 。
5. Set the base type of the property type to **Mandatory Control**.
将属性类型的基础类型设置为强制控制 。1. By default a mandatory control property supports **markings** and/or **organizations** to restrict access.默认情况下，强制控制属性支持标记和/或组织限制访问。
2. If you have CBAC enabled, you will have the option to choose **classification** based mandatory controls.如果你启用了 CBAC，你可以选择基于分类的强制控制。
  1. By default a mandatory control property supports **markings** and/or **organizations** to restrict access.默认情况下，强制控制属性支持标记和/或组织限制访问。
  2. If you have CBAC enabled, you will have the option to choose **classification** based mandatory controls.如果你启用了 CBAC，你可以选择基于分类的强制控制。
  
  6. Select the **Allowed markings** and/or **Allowed organizations** on the datasource. For classifications, select the **Max classification**.在数据源中选择允许的标记和/或允许的组织 。分类时，选择最大分类 。
7. If the object type has multiple datasources, select a mandatory control property for each of the other datasources to secure their properties as well.如果对象类型有多个数据源，请为其他数据源选择一个强制控制属性，以保护它们的属性。
8. Save your changes to the ontology and wait for the reindex to be completed.将你的更改保存到本体论中，等待重新索引完成。


## [](#types-of-mandatory-control-properties)Types of mandatory control properties强制控制属性的类型


There are three types of mandatory controls that can be set on a property:在财产上可以设置三种强制控制：


- [Markings标记](#markings)
- [Organizations组织](#organizations)
- [Classifications分类](#classifications)


### [](#markings)Markings标记


Markings are mandatory controls that restrict access by requiring a user to have a particular Marking in order to access data. If a resource has multiple markings, the user must have all of them to access the resource. Learn more about [markings](/docs/foundry/security/markings/).标记是强制性的控制措施，通过要求用户必须拥有特定的标记才能访问数据，从而限制访问。如果一个资源有多个标记，用户必须拥有所有标记才能访问该资源。了解更多关于标记的信息 。


To use markings, you are required to provide a set of allowed markings. Only markings in this set will be permitted on any mandatory control property on the datasource.使用标记时，你需要提供一套允许的标记。该集合中仅允许对数据源上任何强制控制属性进行标记。


### [](#organizations)Organizations组织


Organizations are access requirements that enforce strict silos between groups of users and resources. Every user is a memeber of only one organization, but can be a guest member of multiple Organizations. In order to access data marked with an organization, a user must be a member of that organization. If a resource has multiple organizations, the user must be a member of at least one of the organizations applied to the resource. Learn more about [organizations](/docs/foundry/security/orgs-and-spaces/#organizations).组织是访问要求，强制用户和资源组之间严格隔离。每个用户只属于一个组织，但可以作为多个组织的访客成员。为了访问带有组织标记的数据，用户必须是该组织的成员。如果一个资源有多个组织，用户必须至少是该资源所应用组织中至少一个的成员。了解更多关于组织的信息 。


To use organizations, you are required to provide a set of allowed organizations. Only organizations in this set will be permitted on any mandatory control property on the datasource.要使用公司，你需要提供一组允许的机构。只有该数据集中的组织才被允许使用数据源上的任何强制控制属性。


Markings and organizations can be used together on the same mandatory control property. In this case, a user must satisfy all the markings and at least one of the organizations to access the resource.标记和组织可以在同一强制控制属性上一起使用。在这种情况下，用户必须满足所有标记条件，并且至少满足其中一个组织才能访问该资源。


### [](#classifications)Classifications分类


Classification markings are mandatory controls used to protect sensitive government information. They are used to restrict access to sensitive information where sensitivity of information is defined in a hierarchical way. Every user can only access data that is classified at or below their own classification level.机密标记是保护敏感政府信息的强制性控制措施。它们用于限制对敏感信息的访问，其中信息的敏感性以层级方式定义。每个用户只能访问属于或低于其机密级别的数据。


You can only configure CBAC markings if you have CBAC enabled on your enrollment. Learn more about [CBAC (classification based access controls)](/docs/foundry/security/classification-based-access-controls/).只有在你的注册时启用了 CBAC 标记，才能配置 CBAC 标记。了解更多关于 CBAC（基于分类的访问控制） 的信息。


To use classifications, you need to provide a max classification. Only markings that satisfy this max classification will be permitted on any classificatoin based mandatory control property on the datasource.要使用分类，你需要提供最大分类。只有满足该最大分类的标记才被允许在数据源上基于分类的强制控制属性上使用。


Classifications can not be used together with markings or organizations on the same mandatory control property.分类不能与标记或组织在同一强制控制属性上同时使用。


## [](#datasource-level-permissioning)Datasource-level permissioning数据源级别的权限


A mandatory control property secures all other properties in the same datasource. For object types with a single datasource, this means that a user will only be able to view an object if they satisfy the value in the mandatory control property.强制控制属性保护同一数据源中的所有其他属性。对于具有单一数据源的对象类型，这意味着用户只有在对象满足强制控制属性中的值时才能查看。


However, for multi-datasource-backed object types (MDOs), each datasource could have its own mandatory control property. Only the properties backed by a specific datasource will be secured by the mandatory control in that datasource.然而，对于多数据源支持的对象类型（MDO），每个数据源都可以拥有自己的强制控制属性。只有由特定数据源支持的属性才会被该数据源的强制控制所保护。


This means that it is possible for a user to only have permission to see a subset of properties on an object, In this case, the user will only be able to see the properties mapped from those datasources. Other properties will appear as null when displaying an object instance to the user.这意味着用户可能只拥有查看对象上部分属性的权限，在这种情况下，用户只能看到这些数据源映射的属性。当向用户展示对象实例时，其他属性会显示为空。


To use mandatory control properties effectively, the backing datasources should be structured in such a way that only properties that should share a mandatory control are in the same datasource.为了有效使用强制控制属性，支持数据源应结构化，只有应共享强制控制的属性才属于同一数据源。


## [](#validations)Validations验证


The following validations are enforced on mandatory control properties:以下验证对强制控制属性进行：


- Mandatory control properties must be mapped to a **marking column** on a **restricted view.** The mandatory controls are enforced by backing the object type with a restricted view which has a policy that requires users to satisfy the markings in the mapped column to be able to view a row. See [Restricted Views](/docs/foundry/security/restricted-views/) for more information.强制控制属性必须映射到受限视图的标记列 。强制控制通过以受限视图支持对象类型来强制执行，该视图有策略要求用户满足映射列中的标记才能查看行。更多信息请参见 “受限视角 ”。
- **Mandatory control properties must be required.** This ensures that if an object with a mandatory control property is present on a datasource, the mandatory control must be defined to help maintain data consistency and integrity. All mandatory control properties must not be null. However, markings and organization values can be set to an empty array. In such cases, all users will meet the marking requirements and be able to view the row. Learn more about [required properties](/docs/foundry/object-link-types/required-properties/).必须要求必须具备强制控制属性。 这确保了如果数据源中存在具有强制控制属性的对象，必须定义该强制控制以帮助保持数据的一致性和完整性。所有强制控制属性不得为零。不过，标记和组织值可以设置为空数组。在这种情况下，所有用户都将满足标记要求，能够查看该行。了解更多关于所需房产的信息。
- Every datasource that contains a mandatory control property must define a constraint on what values can be added to those properties. These constrains come in the form of a max classification for classification based mandatory controls, or a set of allowed markings and/or allowed organizations. Any edits made to the mandatory control properties, as well as the values gotten from the backing dataset, must adhere to the constraint set on the datasource.
每个包含强制控制属性的数据源都必须定义可以添加哪些值的约束。这些限制以基于分类的强制控制的最大分类形式出现，或一组允许的标记和/或允许的组织。对强制控制属性以及从支持数据集获得的值所做的任何编辑，都必须遵守数据源上的约束设置。- This constraint is enforced on the object storage level, so even though you may be able to use Ontology Manager to save an object type that violates this constraint, the object type will fail to index if existing values in the dataset do not satisfy the constraints, or if the values in the dataset are updated to include invalid values for the mandatory controls. Also, any edits made that try to set an invalid value to the mandatory control property will be rejected and the Action will fail to submit.该约束在对象存储层面强制执行，因此即使你可以通过 Ontology Manager 保存违反该约束的对象类型，但如果数据集中已有的值不满足约束，或者数据集中的值被更新为无效的强制控制值，该对象类型将无法索引。此外，任何试图为强制控制属性设置无效值的编辑都会被拒绝，动作将无法提交。
- These allowed markings, allowed organizations or max classification will be used to mark any exported dataset that is materialized from this Object type. This ensures that only users who can view all rows on the Object type will be able to view the materialized dataset.这些允许的标记、允许的组织或最大分类将用于标记从该对象类型实体化的任何导出数据集。这确保只有能够查看对象类型所有行的用户才能查看实体化数据集。
  - This constraint is enforced on the object storage level, so even though you may be able to use Ontology Manager to save an object type that violates this constraint, the object type will fail to index if existing values in the dataset do not satisfy the constraints, or if the values in the dataset are updated to include invalid values for the mandatory controls. Also, any edits made that try to set an invalid value to the mandatory control property will be rejected and the Action will fail to submit.该约束在对象存储层面强制执行，因此即使你可以通过 Ontology Manager 保存违反该约束的对象类型，但如果数据集中已有的值不满足约束，或者数据集中的值被更新为无效的强制控制值，该对象类型将无法索引。此外，任何试图为强制控制属性设置无效值的编辑都会被拒绝，动作将无法提交。
  - These allowed markings, allowed organizations or max classification will be used to mark any exported dataset that is materialized from this Object type. This ensures that only users who can view all rows on the Object type will be able to view the materialized dataset.这些允许的标记、允许的组织或最大分类将用于标记从该对象类型实体化的任何导出数据集。这确保只有能够查看对象类型所有行的用户才能查看实体化数据集。
  
  

Note that mandatory control properties are set to `Hidden` by default. This is because mandatory control properties are meant to be used as markings for other fields, so there is usually no need for mandatory control properties to appear in object views or tables. However, mandatory control property visibility can still be enabled if needed.注意，强制控制属性默认设为隐藏 。这是因为强制控制属性旨在用作其他字段的标记，因此通常不需要在对象视图或表格中出现强制控制属性。不过，如果需要，强制控制属性的可视化仍可启用。


## [](#mandatory-controls-in-actions)Mandatory controls in actions行动中的强制控制


You can add a mandatory control parameter to your action type. This can be a marking parameter, or a classificaton parameter if CBAC is enabled. Organization parameters are currently not supported.你可以在动作类型中添加强制控制参数。这可以是标记参数，或者如果启用了 CBAC 则是分类卡顿参数。目前不支持组织参数。


Mandatory control parameters are commonly used to set a mandatory control property on an object that the action creates. In this case, the values provided must adhere to the property's allowed values, if an invalid value is provided, action submission will fail.强制控制参数通常用于在动作创建的对象上设置强制控制属性。在这种情况下，所提供的值必须符合属性允许的值，如果提供无效值，动作提交将失败。


You can also add a max classification at the parameter level, for classification based mandatory control parameters. This is an action type validation, and so will prevent the action from being submitted if the provided value does not satisfy the max classification, as opposed to relying on the datasource validation which will allow the action to be submitted but will fail to complete.你也可以在参数层面添加最大分类，用于基于分类的强制控制参数。这是一种动作类型验证，因此如果提供的值不满足最大分类，将阻止该动作提交，而不是依赖数据源验证，后者允许提交动作但无法完成。


Objects created by actions will be secured by the provided value for the mandatory control property, just like objects derived from a backing datasource.由动作创建的对象将由强制控制属性提供的值保护，就像从后台数据源派生的对象一样。


## [](#marketplace-usage)Marketplace usage市场使用


Object types with mandatory control properties and action types with mandatory control parameters can be packaged and installed through Marketplace.具有强制控制属性的对象类型和具有强制控制参数的动作类型可以通过市场打包并安装。


When packaging an object type with mandatory control properties, the allowed markings or max classification are declared as installation inputs for that product.当打包具有强制控制属性的对象类型时，允许的标记或最大分类会被声明为该产品的安装输入。


Similarly, if packaging an action type with a classification based mandatory control parameter with max classification set, the max classification is declared as installation inputs.同样，如果将基于分类的强制控制参数和最大分类设置打包为动作类型，则将最大分类声明为安装输入。


When installing the product, you will be prompted to select the allowed markings or max classification for each mandatory control property. The selected values will be set as allowed markings or max classification of the mandatory control properties upon install.安装产品时，系统会提示您选择每个强制控制属性的允许标记或最大分类。选定的数值将在安装时设定为强制控制属性的允许标记或最大分类。


![Selecting mandatory control inputs during Marketplace install](marking-inputs-install.png?width=800)


Note that packaging multiple mandatory control properties and/or parameters with the same values would results in only one mandatory control input being declared.注意，若将多个强制控制属性和/或参数打包为相同值，则只会声明一个强制控制输入。

