# [](#allow-users-to-edit-objects-and-links)Allow users to edit objects and links允许用户编辑对象和链接


## [](#editing-data-from-foundry-object-applications)Editing data from Foundry object applications编辑 Foundry 对象应用程序中的数据


You can allow users in user applications (like Workshop and Object Views) to edit property values, add and remove links, and create and delete objects. You can also configure side effects (like notifications) based on edits made by users.你可以允许用户在用户应用（如 Workshop 和 Object Views）中编辑属性值、添加和删除链接，以及创建和删除对象。你还可以根据用户的编辑设置副作用（比如通知）。


The supported way to configure this functionality is to create and configure action types in the Ontology Manager. [Learn more about how to set up action types.](/docs/foundry/action-types/overview/)支持的配置方式是在本体管理器中创建和配置动作类型。 了解更多关于如何设置动作类型的知识。


The remainder of this documentation covers what needs to be configured on object types and link types before users can take actions.文档的其余部分涵盖了用户在采取行动前需要配置的对象类型和链接类型。


## [](#editing-data-from-external-applications)Editing data from external applications编辑外部应用程序的数据


The [Objects API](/docs/foundry/api/ontology-resources/actions/apply-action/) provides endpoints for external clients to write and update objects, properties, and links with full permissions enforcement.Objects API 为外部客户端提供了端点，以编写和更新对象、属性和链接，并实现完全权限强制。


## [](#set-up-the-prerequisites)Set up the prerequisites设置先修条件


In order for a user to be able to take an action defined in an action type configuration, a writeback dataset must be created. The writeback dataset will read the edits made by users when it is built and will reflect the most up-to-date state of any given object.为了让用户能够执行在动作类型配置中定义的作，必须创建一个写回数据集。写回数据集在构建时会读取用户所做的编辑，并反映任何给定对象的最新状态。


Note that edits are written to the writeback dataset and not the dataset backing an object type or link type. This ensures that users have access to both the original data and the edited data in their analyses.注意，编辑是写入写回数据集，而不是支持对象类型或链接类型的数据集。这确保用户在分析中既能访问原始数据，也能访问编辑后的数据。


To set up a writeback dataset:要设置写回数据集：


1. Navigate to the **Datasources** page of the object type or link type you want to enable edits on.导航到你想启用编辑的对象类型或链接类型的 Datasource 页面。
2. Select **Generate** in the **Writeback dataset** portion of the page to create a new writeback dataset. A dialog will open asking you to choose a Project where you’d like to place the dataset. Select a location.在页面的写回数据集部分选择生成 ，以创建新的写回数据集。会弹出一个对话框，要求你选择一个项目，将数据集放置其中。选择一个地点。
3. Make sure the users who you want to be able to edit the object type or link type have edit permissions on the writeback dataset.确保你希望编辑对象类型或链接类型的用户拥有写回数据集的编辑权限。
4. Ensure that the users who you want to be able to view changes made to the object type or link type have view permissions on the writeback dataset.
确保你希望查看对象类型或链接类型更改的用户拥有对写回数据集的查看权限。- The ability to view objects and links is controlled by an object type and link type’s backing datasources.查看对象和链接的能力由对象类型及其链接类型的后备数据源控制。
- The ability to view the edits on objects and links is controlled by the permissions on the writeback dataset.查看对象和链接编辑的能力由写回数据集的权限控制。
- If users have access to only the former, they can see only the object as it exists without edits applied. If users have access to the latter, they can see both the edits and the object as it exists at present.如果用户只能访问前者，则只能看到该对象的真实状态，无需进行编辑。如果用户能访问后者，他们可以同时看到编辑内容和当前存在的对象。
  - The ability to view objects and links is controlled by an object type and link type’s backing datasources.查看对象和链接的能力由对象类型及其链接类型的后备数据源控制。
  - The ability to view the edits on objects and links is controlled by the permissions on the writeback dataset.查看对象和链接编辑的能力由写回数据集的权限控制。
  - If users have access to only the former, they can see only the object as it exists without edits applied. If users have access to the latter, they can see both the edits and the object as it exists at present.如果用户只能访问前者，则只能看到该对象的真实状态，无需进行编辑。如果用户能访问后者，他们可以同时看到编辑内容和当前存在的对象。
  
  

If you want a property in your object type to capture manually-entered data from an end user (via an Action or other writeback method) and this data does not yet exist in Foundry, you will need to add an empty column to the object type’s backing dataset and map it to a new property in your object type. You also need to enable edits; this is done by creating a writeback dataset in Object Storage V1 or by toggling on edits in Object Storage V2.如果你希望对象类型中的属性能够通过 Action 或其他写回方法捕获最终用户手动输入的数据，而这些数据尚未在 Foundry 中存在，你需要在该对象类型的后备数据集中添加一个空列，并将其映射到你的对象类型中的一个新属性。你还需要启用编辑功能;这可以通过在对象存储 V1 中创建写回数据集，或在对象存储 V2 中切换编辑来实现。

