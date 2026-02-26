# [](#upload-attachments)Upload attachments上传附件


Actions support uploading attachments from Workshop, Object Explorer, Object Views, Quiver, and Slate. Permissions to view, edit, and delete an attachment are consistent with the object to which they are uploaded. For example, if a user has view permissions to an object, they will be able to view and download attachments stored on this object. Replacing an existing attachment would require edit permissions on the object.操作支持从工作坊、对象浏览器、对象视图、Quiver 和 Slate 中上传附件。查看、编辑和删除附件的权限与所上传的对象权限一致。例如，如果用户对某个对象有查看权限，他们将能够查看和下载该对象上存储的附件。替换现有附件需要对该对象有编辑权限。


You can upload a single attachment or a list of attachments. To upload an attachment using actions, follow the configuration steps for both action types and object types.您可以上传单个附件或附件列表。要使用操作上传附件，请按照操作类型和对象类型的配置步骤进行操作。


## [](#configuring-action-types)Configuring action types配置操作类型


In the parameter configuration view, select **Attachment** as the parameter type. Attachments can only be uploaded using attachment parameter types. The corresponding column in the object-backing dataset must be a **String** and the edited object property must be of type **Attachment**.在参数配置视图中，将参数类型选择为附件。只能使用附件参数类型上传附件。对象支持数据集中的相应列必须是字符串类型，并且编辑的对象属性必须是附件类型。


To upload several media files at once, select **Allow multiple values**. Note that support for several media files in one action requires an additional toggle during [object type configuration](#configuring-object-types) to **Allow multiple**, as described below.要一次性上传多个媒体文件，请选择允许多个值。请注意，在一个操作中支持多个媒体文件需要在进行对象类型配置时开启额外的切换按钮，如下所述。


## [](#configuring-object-types)Configuring object types配置对象类型


In the object detail view, select **Attachment** as the property type. Attachments can only be uploaded to attachment property types.在对象详情视图中，将属性类型选择为附件。只能上传到附件属性类型。


To upload several media files to one property, toggle **Allow multiple**. In this case, the property in the object-backing dataset must be an **Array**.要向一个属性上传多个媒体文件，请切换允许多个。在这种情况下，对象支持数据集中的该属性必须是数组类型。


## [](#architecture-and-limits)Architecture and limits架构和限制


Attachments are immediately uploaded to Foundry once they are added to an action form. Upon form submission, permissions to view, edit, and delete an attachment are inferred from the user's permissions on the underlying object type. If form submission fails or is cancelled, the outstanding attachment is no longer directly reachable and will automatically be permanently deleted after some time. Similarly, attachments that belong to deleted objects or are no longer mapped to an object (which occurs when the corresponding property is deleted) are no longer directly reachable and will eventually automatically be permanently deleted.附件一旦添加到操作表单中，就会立即上传到 Foundry。提交表单时，查看、编辑和删除附件的权限将根据用户对底层对象类型的权限推断得出。如果表单提交失败或被取消，未处理的附件将不再可直接访问，并在一段时间后自动永久删除。类似地，属于已删除对象或不再映射到对象的附件（这发生在相应属性被删除时）将不再可直接访问，并最终自动永久删除。


Attachments are supported for both logic-backed and function-backed actions. There is a global, fixed file size limit of 200MB.逻辑支持和函数支持的附件都受支持。有一个全局固定的文件大小限制为 200MB。


- Each attachment can be linked to a maximum of ten objects in its lifetime. If an attachment has been linked to ten objects, it cannot be linked to any other objects even if one or more of the original linked objects has been deleted. After reaching this limit of ten linked objects, you can upload the file again as a new attachment to link it to more objects.每个附件在其生命周期内最多可以链接到十个对象。如果一个附件已经链接了十个对象，即使其中有一个或多个原始链接的对象被删除，它也无法再链接到其他任何对象。当达到这个链接对象的上限（十个）后，你可以将文件重新上传作为新的附件，以便链接到更多对象。

