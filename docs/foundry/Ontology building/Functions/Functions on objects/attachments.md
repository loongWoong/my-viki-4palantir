# [](#attachments)Attachments附件


TypeScript v1 functions are executed in an environment that has strict memory limits. Exceeding these memory limits can happen quickly when dealing with file data; we recommend only interacting with attachments under 20MB. Python and TypeScript v2 functions have a default limit of 1GB, which can be adjusted in Ontology Manager.TypeScript v1 函数在具有严格内存限制的环境中执行。处理文件数据时，超出这些内存限制可能会很快发生；我们建议仅与小于 20MB 的附件进行交互。Python 和 TypeScript v2 函数默认限制为 1GB，可在本体管理器中调整。


An attachment is a file that acts like an object property. Attachments are uploaded as temporary files and [attached to objects using actions](/docs/foundry/action-types/upload-attachments/). Once attached to an object, an attachment is persisted and can be accessed similarly to other properties.附件是一个像对象属性一样起作用的文件。附件作为临时文件上传，并使用操作附加到对象上。一旦附加到对象，附件就会被持久化，并可以像访问其他属性一样访问。


## [](#attachments-in-functions)Attachments in functions函数中的附件


Attachments can be passed into functions as inputs from actions, or accessed as properties on objects. You can also create and return attachments in functions.附件可以作为动作的输入传递到函数中，或作为对象上的属性进行访问。你也可以在函数中创建和返回附件。


When using Python, attachments are managed using the [API Gateway](/docs/foundry/api/ontologies-v2-resources/attachments/attachment-basics/). An attachment type is provided in the [Python OSDK](/docs/foundry/ontology-sdk/python-osdk/).使用 Python 时，附件通过 API 网关进行管理。Python OSDK 提供了附件类型。


Below is the import syntax for attachments by language:以下是按语言划分的附件导入语法：


TypeScript v1TypeScript v2Python```
Copied!`1import { Attachment } from "@foundry/functions-api";`
```

```
Copied!`1import { Attachment } from "@osdk/functions";`
```

```
Copied!`1# For convenience, the OSDK Attachment type is re-exported from the Python functions `functions.api` package.
2from functions.api import Attachment`
```


## [](#read-attachment-data)Read attachment data读取附件数据


A read method is provided on attachments to read their raw data. The signature for the method is as follows:


TypeScript v1TypeScript v2Python```
Copied!`1// Blob is a standard JavaScript type, representing a file-like object of immutable, raw data.
2// https://developer.mozilla.org/en-US/docs/Web/API/Blob
3readAsync(): Promise<Blob>;`
```

```
Copied!`1// Response interface is part of the Fetch API, and is provided by `undici` in the TypeScript v2 environment.
2// https://developer.mozilla.org/en-US/docs/Web/API/Response
3fetchContents(): Promise<Response>;`
```

```
Copied!`1# BytesIO is a standard Python type, representing a binary stream.
2# https://docs.python.org/3/library/io.html#io.BytesIO
3def read(self) -> BytesIO: ...`
```


You may need to use libraries or write your own custom code for handling complex file types. For example, PDFs must be parsed with an appropriate library. [Learn more about adding dependencies to functions repositories](/docs/foundry/functions/add-dependencies/).


### [](#file-parsing-in-typescript-v1)File parsing in TypeScript v1


TypeScript v1 functions do not offer filesystem support. Often, dependencies related to parsing file data will rely on the `fs` module, which is not available in the functions environment. This restriction may cause `fs` module errors during compilation and execution. To work around this restriction, you can introduce a dependency on an in-memory file system (`memfs`, for example). Then, alias the dependency under the `fs` name.


Below is an example using the NPM dependency `memfs` in a `package.json` file:下面是一个在 package.json 文件中使用 NPM 依赖 memfs 的示例：


```
Copied!`1"fs": "npm:memfs@^x.x.x"`
```


## [](#create-attachments)Create attachments创建附件


Functions can also be used to create attachments and attach them to objects. For attachments created in functions to be persisted, the function must make an [Ontology edit](/docs/foundry/functions/api-ontology-edits/) that links the attachment to an object.函数也可以用来创建附件并将它们附加到对象上。为了持久化函数中创建的附件，函数必须执行一个本体编辑操作，将附件链接到对象。


Attachments that are not attached to an object can only be viewed by the uploader and are automatically deleted after a certain period of time. 未附加到对象的附件只能由上传者查看，并在一定时间后自动删除。


TypeScript v2 functions do not support creating attachments.TypeScript v2 函数不支持创建附件。


To create an attachment, use an upload function on the attachment. The signature for the upload function by language is as follows:要创建附件，请在附件上使用上传函数。上传函数的签名按语言如下：


TypeScript v1Python```
Copied!`1import { Attachments, Attachment } from "@foundry/functions-api";
2
3// On Attachments:
4uploadFile(filename: string, blob: Blob): Promise<Attachment>;`
```

```
Copied!`1from ontology_sdk import FoundryClient
2from foundry_sdk_runtime.attachments import AttachmentMetadata
3
4# On FoundryClient:
5def upload(file_path: str, attachment_name: str) -> AttachmentMetadata: ...
6# `file_path` is a local file to be uploaded.`
```


The following example shows the process for uploading a file and assigning the resulting attachment to an object.以下示例展示了上传文件并将生成的附件分配给对象的过程。


TypeScript v1Python```
Copied!`1import { Attachments, Attachment, OntologyEditFunction } from "@foundry/functions-api";
2
3@OntologyEditFunction()
4public async updateMaintenanceLog(aircraft: Aircraft): Promise<void> {
5    const aircraftMaintenanceLogData: Blob = await aircraft.maintenanceLog.readAsync();
6    const completedMaintenanceLogData: Blob = await completedMaintenanceLog.readAsync();
7
8    // You will likely need to rely on libraries or custom code to create the `Blob` object, which is
9    // passed as a parameter into the `uploadFile` method.
10
11    // Compare the current aircraft logs and completed logs and create a new maintenance log.
12    const updatedMaintenanceLogData: Blob;
13
14    aircraft.maintenanceLog = await Attachments.uploadFile("maintenance-log.txt", updatedMaintenanceLogData);
15}`
```

```
Copied!`1from io import BytesIO
2
3from functions.api import function, Attachment, OntologyEdit
4from ontology_sdk import FoundryClient
5from ontology_sdk.ontology.objects import Aircraft
6
7
8@functions(edits=[Aircraft])
9def update_maintenance_log(
10    aircraft: Aircraft,
11    completed_maintenance_log: Attachment
12) -> list[OntologyEdit]:
13    client = FoundryClient()
14    ontology_edits = client.ontology.edits()
15
16    maintenance_log_data: BytesIO = aircraft.maintenance_log.read()
17    completed_maintenance_log_data: BytesIO = completed_maintenance_log.read()
18
19    # Compare the current aircraft logs and completed logs and create a new maintenance log
20    updated_maintenance_log_data: BytesIO = get_updated_maintenance_log(
21        maintenance_log_data,
22        completed_maintenance_log_data
23    )
24
25    editable_aircraft = ontology_edits.objects.Aircraft.edit(aircraft)
26
27    with open("updated-maintenance-log.txt", "wb") as f:
28        f.write(updated_maintenance_log_data.getbuffer())
29
30    editable_aircraft.maintenance_log = client.ontology.attachments.upload(
31        "updated-maintenance-log.txt",
32        "my_attachment"
33    )
34
35    return ontology_edits.get_edits()`
```

