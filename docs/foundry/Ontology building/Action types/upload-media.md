# [](#upload-media)Upload media上传媒体


Actions support uploading media files using an action form or table. For most use cases in Foundry, uploading to media reference properties is the recommended method.操作支持通过操作表单或表格上传媒体文件。在 Foundry 中的大多数用例中，推荐将文件上传到媒体引用属性。


Media reference properties (backed by [media sets](/docs/foundry/data-integration/media-sets/)) offer several advantages over attachment properties:媒体引用属性（由媒体集支持）相比附件属性具有以下优势：


- **Scalability:** Support for billions of files with efficient storage and retrieval.可扩展性：支持数十亿个文件，具有高效的存储和检索功能。
- **Built-in transformations:** Many media transformations and LLM capabilities are supported and easy to use out of the box.内置转换：许多媒体转换和 LLM 功能都得到支持，开箱即用，易于使用。
- **Advanced previews:** Built-in rendering and rich preview functionality for supported formats.高级预览：内置渲染和丰富的预览功能，支持多种格式。
- **Format support:** Support for tailored workflows on both standard formats and specialized formats, such as NITF, GeoTIFF, and DICOM.格式支持：支持在标准格式和特殊格式（如 NITF、GeoTIFF 和 DICOM）上定制工作流程。


Users can upload media files via a file-picker interface, with files persisted to the media set upon successful action submission.用户可以通过文件选择界面上传媒体文件，文件将在成功提交操作后持久化到媒体集中。


[Format conversions](/docs/foundry/media-sets-advanced-formats/media-overview/#additional-input-formats) only happen after the action completes and the media file has been uploaded to the media set.格式转换仅在操作完成后且媒体文件已上传到媒体集时才会发生。


## [](#configuration)Configuration配置


For detailed instructions on configuring media reference properties and setting up media upload actions, see [Configure media reference properties](/docs/foundry/object-link-types/base-types/#configure-media-reference-properties) and [Upload media](/docs/foundry/media-sets-advanced-formats/upload-media/).有关配置媒体引用属性和设置媒体上传操作的详细说明，请参阅 Configure media reference properties and Upload media。


## [](#permissions)Permissions权限


Permissions for uploading media via an action are managed by the [action submission criteria](/docs/foundry/action-types/submission-criteria/). If users satisfy the action submission criteria, they do not need any permissions on the backing media set to upload media.通过操作上传媒体文件的权限由操作提交标准管理。如果用户满足操作提交标准，他们不需要在底层媒体集上拥有任何权限即可上传媒体。


Edit permission on a media set will be checked when it is added to an object type or referenced by an action type for the first time. Adding a media set to your ontology delegates access control from the media set to the ontology. This means that anyone who can manage actions on the object type, can control who is able to upload media to the media set.当媒体集首次添加到对象类型或被操作类型引用时，会检查其在媒体集上的编辑权限。将媒体集添加到您的本体会将访问控制从媒体集委托给本体。这意味着任何能够管理对象类型上操作的人，都可以控制谁能够上传媒体到媒体集。

