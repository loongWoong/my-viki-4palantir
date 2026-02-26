# [](#media)Media媒体


Foundry enacts strict memory limits when executing TypeScript v1 functions. To ensure you do not exceed those memory limits, you should only interact with media files under 20MB.Foundry 在执行 TypeScript v1 函数时会实施严格的内存限制。为确保您不会超出这些内存限制，您应该仅与小于 20MB 的媒体文件进行交互。


Functions enable you to access and modify media using [TypeScript v1](/docs/foundry/functions/typescript-v1-getting-started/), [TypeScript v2](/docs/foundry/functions/typescript-v2-getting-started/), and [Python](/docs/foundry/functions/python-getting-started/). TypeScript v1 functions provide a `MediaItem` type that exposes a number of methods for conveniently interacting with the underlying media, with built-in operations that allow you to easily interact with different kinds of media without external libraries. TypeScript v2 and Python support media uploads through [Ontology edits.](/docs/foundry/functions/edits-overview/)函数使您能够使用 TypeScript v1、TypeScript v2 和 Python 访问和修改媒体。TypeScript v1 函数提供了一个 MediaItem 类型，该类型公开了许多方便与底层媒体交互的方法，具有内置操作，允许您轻松地与不同类型的媒体交互，而无需外部库。TypeScript v2 和 Python 通过本体编辑支持媒体上传。


If you need any operations that don't currently exist out-of-the-box, you will likely need to use external libraries or write your own custom code. [Learn more about adding dependencies to functions repositories.](/docs/foundry/functions/add-dependencies/)如果您需要任何当前现成的操作，您可能需要使用外部库或编写自己的自定义代码。了解更多关于向函数存储库添加依赖项的信息。


## [](#upload-media-in-ontology-edit-functions)Upload media in Ontology edit functions在本体编辑功能中上传媒体


You cannot pass uploaded media into a query function within the same uploaded function. 您不能将上传的媒体传递到同一上传功能内的查询功能中。


Uploading media within a function is not supported in TypeScript v1.在 TypeScript v1 中，函数内不支持上传媒体。


Use Ontology edit functions to upload media and create objects in the Ontology. Once uploaded, you can read and download media files from objects for use in your application. [Learn more about media sets in Foundry.](/docs/foundry/media-sets-advanced-formats/media-overview/)使用本体编辑功能上传媒体并在本体中创建对象。上传后，您可以从对象中读取和下载媒体文件以供应用程序使用。了解更多关于 Foundry 中的媒体集的信息。


You can construct Ontology edits in TypeScript v2 and Python functions using media types by uploading media to the Ontology to obtain a `MediaReference`. While you can use the `MediaReference` to construct an Ontology edit, you can also do so by passing existing media into the function parameter.您可以通过上传媒体到本体来构建 TypeScript v2 和 Python 函数中的本体编辑，以获取 MediaReference 。虽然您可以使用 MediaReference 来构建本体编辑，但也可以通过将现有媒体传递到函数参数中来实现。


TypeScript v1TypeScript v2Python```
Copied!`1import { OntologyEditFunction, MediaItem } from "@foundry/functions-api";
2import { Aircraft } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @OntologyEditFunction()
6    public async setExistingMediaToObject(
7        aircraft: Aircraft,
8        mediaItem: MediaItem
9    ): Promise<void> {
10        // Ontology Edits with passed in MediaItems are supported
11        aircraft.myMediaProperty = mediaItem;
12    }
13}`
```

```
Copied!`1// Ensure you are using TypeScript OSDK 2.6 or greater to use media uploads
2// in Ontology Edit Functions.
3
4import type { Client } from "@osdk/client";
5import { Aircraft } from "@ontology-sdk/sdk";
6import type { Edits } from "@osdk/functions";
7import { createEditBatch, uploadMedia } from "@osdk/functions";
8
9async function uploadTextToNewPlane(client: Client): Promise<Edits.Object<Aircraft>[]> {
10    const batch = createEditBatch<Edits.Object<Aircraft>>(client);
11    const blob = new Blob(["Hello, world"], { type: "text/plain" });
12    const mediaReference = await uploadMedia(
13        client,
14        { data: blob, fileName: "/planes/aircraft.txt" }
15    );
16    batch.create(Aircraft, { myMediaProperty: mediaReference, /* ... */ });
17    return batch.getEdits();
18}
19
20export default uploadTextToNewPlane;`
```

```
Copied!`1# Ensure you are using Python OSDK 2.145 or greater to use media uploads
2# in Ontology Edit Functions.
3
4from ontology_sdk import FoundryClient
5from ontology_sdk.ontology.objects import Aircraft
6from functions.api import function, OntologyEdit
7
8@function(beta=True, edits=[Aircraft])
9def upload_text_to_new_plane() -> list[OntologyEdit]:
10    client = FoundryClient()
11    edits = client.ontology.edits()
12    media_reference = client.ontology.media.upload_media(
13        body="Hello, world".encode("utf8"),
14        filename="/planes/aircraft.txt",
15    )
16    edits.objects.Aircraft.create(
17        pk = "primary_key",
18        my_media_property=media_reference,
19        # ...
20    )
21    return edits.get_edits()`
```


## [](#media-item-parameter)Media item parameter媒体项参数


There are two ways to interact with media items in functions:在函数中与媒体项交互有两种方式：


- Using a media property on an object type在对象类型上使用媒体属性
- Passing a media reference parameter of an action type to the function将动作类型的媒体引用参数传递给函数


### [](#using-media-property-of-an-object-type)Using media property of an object type使用对象类型的媒体属性


The following example shows the `isAudio` media operations on a media reference property of an object type.以下示例展示了 isAudio 媒体操作在对象类型的媒体引用属性上。


TypeScript v1```
Copied!`1MediaItem.isAudio(objectType.mediaReferenceProperty)`
```


### [](#passing-a-media-reference-parameter-on-action-type)Passing a media reference parameter on action type在动作类型上传递媒体引用参数


Action parameters of type media reference can be passed to the function as a parameter.媒体引用类型的操作参数可以作为参数传递给函数。


The screenshot below shows an action passing a media parameter to its backing function.下图显示了操作将媒体参数传递给其支撑函数。


![action](media-tutorial-media-action-parameter.png?width=600)


## [](#universal-operations)Universal operations通用操作


The universal operations outlined below are currently not available for the TypeScript v2 and Python `MediaReference` type. However, they *are* available for the TypeScript v2 and Python `Media` type, which is a property on an object type.下面列出的通用操作目前不适用于 TypeScript v2 和 Python MediaReference 类型。但是，它们适用于 TypeScript v2 和 Python Media 类型，该类型是对象类型上的一个属性。


Some operations are supported by all media types.某些操作由所有媒体类型支持。


### [](#read-raw-media-data)Read raw media data读取原始媒体数据


You can access a media item by selecting the media reference property on the object. The signature for the method is as follows:您可以通过选择对象上的媒体引用属性来访问媒体项。该方法签名如下：


TypeScript v1TypeScript v2Python```
Copied!`1// Blob is a standard JavaScript type, representing a file-like object of immutable, raw data.
2// https://developer.mozilla.org/en-US/docs/Web/API/Blob
3readAsync(): Promise<Blob>;`
```

```
Copied!`1fetchContents(): Promise<Response>;
2
3// Example usage:
4const mediaContents = await myAircraft.myMediaProperty.fetchContents();
5if (mediaContents.ok) {
6    const mediaMimeType = mediaContents.headers.get("Content-Type");
7
8    // Blob is a standard JavaScript type, representing a file-like object of immutable, raw data.
9    // https://developer.mozilla.org/en-US/docs/Web/API/Blob
10    const mediaBlob: Blob = mediaContents.blob();
11}`
```

```
Copied!`1from io import BytesIO
2
3get_media_content(self) -> BytesIO: ...
4
5# Example usage:
6raw_data: BytesIO = my_aircraft.my_media_property.get_media_content()`
```


### [](#get-media-metadata)Get media metadata获取媒体元数据


You can access a media item's metadata. The signature for the method is as follows:您可以访问媒体项的元数据。该方法的签名如下：


TypeScript v1TypeScript v2Python```
Copied!`1getMetadataAsync(): Promise<IMediaMetadata>;`
```

```
Copied!`1fetchMetadata(): Promise<MediaMetadata>;
2
3// Example usage:
4const mediaMetadata = await myAircraft.myMediaProperty.fetchMetadata();
5const sizeBytes = mediaMetadata.sizeBytes;
6const mediaType = mediaMetadata.mediaType;`
```

```
Copied!`1from foundry_sdk.v2.ontologies.models import MediaMetadata
2
3get_media_metadata(self) -> MediaMetadata:
4
5# Example usage:
6media_metadata: MediaMetadata = my_aircraft.my_media_property.get_media_metadata()
7size_bytes = media_metadata.size_bytes
8media_type = media_metadata.media_type`
```


#### [](#type-guards-in-typescript-v1)Type guards in TypeScript v1TypeScript v1 中的类型守卫


Type guards in TypeScript v1 allow you to access functionality that is specific to certain media types. The following type guards can be used on media item metadata:TypeScript v1 中的类型守卫允许您访问特定于某些媒体类型的功能。以下类型守卫可用于媒体项元数据：


- `isAudioMetadata()`
- `isDicomMetadata()`
- `isDocumentMetadata()`
- `isImageryMetadata()`
- `isSpreadsheetMetadata()`
- `isUntypedMetadata()`
- `isVideoMetadata()`


As an example, you could use the imagery type guard to pull out image specific metadata fields:例如，你可以使用图像类型守卫来提取图像特定的元数据字段：


TypeScript v1```
Copied!`1const metadata = await myObject.mediaReference?.getMetadataAsync();
2if (isImageryMetadata(metadata)) {
3    const imageWidth = metadata.dimensions?.width;
4    ...
5}`
```


You can also use type guards on the media item namespace, which then gives you access to more methods on the type-specific media item. The type guards you can use here are:你也可以在媒体项命名空间上使用类型守卫，这样你就可以访问类型特定的媒体项上的更多方法。这里可以使用以下类型守卫：


- `MediaItem.isAudio()`
- `MediaItem.isDicom()`
- `MediaItem.isDocument()`
- `MediaItem.isImagery()`
- `MediaItem.isSpreadsheet()`
- `MediaItem.isVideo()`


## [](#document-specific-operations)Document-specific operations特定文档的操作


Document-specific operations are not currently available in TypeScript v2 and Python functions.在 TypeScript v2 和 Python 函数中，目前没有提供特定文档的操作。


### [](#text-extraction)Text extraction文本提取


To extract text from a document, you can either use optical character recognition (OCR) or extract embedded text on the media item.要从文档中提取文本，您可以使用光学字符识别（OCR）或提取媒体项中的嵌入文本。


For machine-generated PDFs, it may be faster and/or more accurate to extract text embedded digitally in the PDF rather than using optical character recognition (OCR). Below is an example of text extraction usage:对于机器生成的 PDF 文件，提取 PDF 中嵌入的数字文本可能比使用光学字符识别（OCR）更快和/或更准确。以下是文本提取使用的示例：


TypeScript v1```
Copied!`1extractTextAsync(options: IDocumentExtractTextOptions): Promise<string[]>;`
```


When using TypeScript v1, the following can optionally be provided as an object:在使用 TypeScript v1 时，以下可以作为对象可选提供：


- `startPage`: The zero-indexed start page (inclusive).startPage : 零索引的起始页（包含）。
- `endPage`: The zero-indexed end page (exclusive).endPage : 零索引的结束页（不包含）。


For non-machine-generated PDFs, it would be best to use the OCR method for extracting text.对于非机器生成的 PDF，最好使用 OCR 方法来提取文本。


TypeScript v1```
Copied!`1ocrAsync(options: IDocumentOcrOptions): Promise<string[]>;`
```


The following can optionally be provided as a TypeScript object:以下可以作为 TypeScript 对象可选提供：


- `startPage`: The zero-indexed start page (inclusive).startPage : 零索引的起始页（包含）。
- `endPage`: The zero-indexed end page (exclusive).endPage : 零索引的结束页（不包含在内）。
- `languages`: A list of languages to recognize (can be empty).languages : 要识别的语言列表（可以为空）。
- `scripts`: A list of scripts to recognize (can be empty).scripts : 要识别的脚本列表（可以为空）。
- `outputType`: Specifies the output type as `text` or `hocr`.outputType : 指定输出类型为 text 或 hocr 。


Remember that you need to use type guards in order to access media-type specific operations. Here's an example of using the `isDocument()` type guard to then perform OCR text extraction:记得你需要使用类型守卫来访问特定媒体类型的操作。这里是一个使用 isDocument() 类型守卫来执行 OCR 文本提取的示例：


TypeScript v1```
Copied!`1import { MediaItem } from "@foundry/functions-api";
2import { ArxivPaper } from "@foundry/ontology-api";
3
4@Function()
5public async firstPageText(paper: ArxivPaper): Promise<string | undefined> {
6    if (MediaItem.isDocument(paper.mediaReference)) {
7        const text = (await paper.mediaReference.ocrAsync({ endPage: 1, languages: [], scripts: [], outputType: 'text' }))[0];
8        return text;
9    }
10
11    return undefined;
12}`
```


## [](#audio-specific-operations)Audio-specific operations音频特定操作


Audio-specific operations are not currently available in TypeScript v2 and Python functions.音频特定操作目前 TypeScript v2 和 Python 函数中不可用。


### [](#transcription)Transcription转录


Audio media items support transcription using the transcribe method. The signature is as follows:音频媒体项支持使用 transcribe 方法进行转录。其签名如下：


TypeScript v1```
Copied!`1transcribeAsync(options: IAudioTranscriptionOptions): Promise<string>;`
```


The following can optionally be passed in to specify how the transcription should run. The available options are:以下可以可选地传递以指定转录应如何运行。可用选项为：


- `language`: The language to transcribe, passed using the `TranscriptionLanguage` enum.language : 用于转写的语言，通过 TranscriptionLanguage 枚举传入。
- `performanceMode`: Runs transcriptions in `More Economical` or `More Performant` mode, passed using the `TranscriptionPerformanceMode` enum.performanceMode : 在 More Economical 或 More Performant 模式下运行转写，通过 TranscriptionPerformanceMode 枚举传入。
- `outputFormat`: Specifies the output format by passing an object of `type` `plainTextNoSegmentData` (plain text) or `pttml`. `pttml` is a [TTML-like ↗](https://en.wikipedia.org/wiki/Timed_Text_Markup_Language) format where the object also takes a boolean `addTimestamps` parameter if the type is `plainTextNoSegmentData`.outputFormat : 通过传入 type plainTextNoSegmentData 对象指定输出格式（纯文本）或 pttml 。 pttml 是类似 TTML ↗ 的格式，当类型为 plainTextNoSegmentData 时，对象还接受一个布尔参数 addTimestamps 。


Here's an example of providing options for transcription:这里是一个提供转写选项的示例：


TypeScript v1```
Copied!`1import { Function, MediaItem, TranscriptionLanguage, TranscriptionPerformanceMode } from "@foundry/functions-api";
2import { AudioFile } from "@foundry/ontology-api";
3
4@Function()
5public async transcribeAudioFile(file: AudioFile): Promise<string|undefined> {
6    if (MediaItem.isAudio(file.mediaReference)) {
7        return await file.mediaReference.transcribeAsync({
8            language: TranscriptionLanguage.ENGLISH,
9            performanceMode: TranscriptionPerformanceMode.MORE_ECONOMICAL,
10            outputFormat: {type: "plainTextNoSegmentData", addTimestamps: true}
11        });
12    }
13
14    return undefined;
15}`
```

